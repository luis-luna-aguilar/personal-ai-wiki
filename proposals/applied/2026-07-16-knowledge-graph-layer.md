---
type: proposal
source: internal — knowledge-graph layer deployment (ported from MUSCLE company-brain repo, VCR-0001/0002/0003)
status: pending
created: 2026-07-16
---

# Proposal: Adopt the Knowledge-Graph Sidecar Layer into AGENTS.md

## Summary

A knowledge-graph layer (Fuseki/SPARQL + SHACL/OWL validation, MD→ACE→TTL sidecar pipeline) has been deployed under `knowledge-graph/`, per the user's explicit instruction to port it from the MUSCLE company-brain repo and run it here at full-sync fidelity as a high-volume stress test. This proposal has two distinct edits to `AGENTS.md`: (1) a purely additive new section documenting the sidecar convention, and (2) one new bullet in the existing "Rules for proposals" list (Workflow 5) making a lightweight "Graph impact" note part of any proposal that touches a sidecarred page. Neither has been applied yet — both wait on your approval via the normal checkbox flow, same as any other proposal in this repo.

## Intended changes

- [x] **Create/Update** `AGENTS.md` — insert a new `## Knowledge graph sidecars` section between `## History handling` and `## Maintenance`.
    > See draft below
- [x] **Update** `AGENTS.md` — add one new bullet to Workflow 5's "Rules for proposals" list (after the existing "Schema / vocabulary additions" bullet).
    > **Before:**
    > ```
    > - Include a "Schema / vocabulary additions" section whenever you want to introduce a new tag, domain, or subcategory. This requires explicit approval via checkbox.
    > ```
    > **After:** (new bullet appended)
    > ```
    > - Include a "Schema / vocabulary additions" section whenever you want to introduce a new tag, domain, or subcategory. This requires explicit approval via checkbox.
    > - If the proposal touches a sidecarred wiki page (`wiki/{concepts,models,benchmarks,tools,workflows,trends,use-cases,training,state-of}/`), add a short "Graph impact" note: touched vocabulary terms, any new-term VCR reference, and whether `gen-schema-concepts.py` needs re-running for a schema addition — or simply "No durable-fact changes." See `AGENTS.md`'s "Knowledge graph sidecars" section for what this covers.
    > ```

## Page drafts

### AGENTS.md (updated — new section inserted after "## History handling", before "## Maintenance")

```md
## Knowledge graph sidecars

The wiki carries a machine-readable knowledge-graph layer alongside the Markdown. Selected wiki pages have two sibling sidecar files:

- **`<page>.ace`** — the page's assertable facts in Attempto Controlled English (one sentence per line). Generated from the `.md` by the `ace-extractor` subagent; must pass `knowledge-graph/scripts/validate-ace.sh` (APE parser). Never hand-edit to change facts — edit the `.md` and regenerate.
- **`<page>.ttl`** — RDF triples compiled FROM the `.ace` by `knowledge-graph/scripts/drs2ttl.py`. A pure build artifact; never hand-authored (exception: a small labeled enrichment block for reified structured values ACE cannot express — `schema:MonetaryAmount` and similar).

**Pipeline: MD → ACE → TTL.** The Markdown is the system of record. When an applied proposal changes a sidecarred page's content, regenerate its `.ace` (ace-extractor) and recompile its `.ttl` in the same apply, then run:
1. `knowledge-graph/scripts/validate-ace.sh <page>.ace`
2. `python3 knowledge-graph/scripts/drs2ttl.py <page>.ace` (candidate) → promote
3. `knowledge-graph/scripts/validate-page.sh <page>.ttl` (reasoner + SHACL)
4. `knowledge-graph/scripts/validate-ingestion.sh <page>.ttl` (whole-graph contradiction gate)
5. `knowledge-graph/scripts/rebuild.sh` (refresh the SPARQL store)

`knowledge-graph/scripts/validate-sync.sh` is the drift guard — it recompiles every `.ace` and fails on divergence from the committed `.ttl`. **This deployment runs full sync deliberately** (a stress test of the pipeline at this wiki's real update volume, not a lighter-touch "durable facts only" policy a lower-churn wiki might choose) — every sidecarred page's `.ace`/`.ttl` regenerates when its `.md` changes, volatile facts (benchmark scores, leader claims) included. Volatile datatype facts are reified with their `as_of` date (`aiw:BenchmarkResult` pattern) — a bare number with no date is non-conformant.

**IRI rule:** every sidecarred page is one graph node: `aiw:<filename-slug>` (e.g. `wiki/tools/claude-code.md` → `aiw:claude-code`). IRIs are permanent — never rename them; renames get `skos:altLabel`/`owl:sameAs` instead.

**Vocabulary is controlled — same spirit as `wiki/_schema/`, same gate.** Facts are expressed only in terms from `knowledge-graph/ontology/lexicon-map.yaml` (word ↔ IRI catalog). A genuinely new term (class/property) is admitted only via a Vocabulary Change Request in `knowledge-graph/governance/change-requests/`, exactly like a new tag/domain/subcategory needs schema approval. **The `wiki/_schema` controlled vocabularies are mirrored in the graph as SKOS concept schemes (VCR-0002)** — adding an approved subcategory/domain/tag updates BOTH `wiki/_schema/*.md` and the graph concept scheme (`knowledge-graph/scripts/gen-schema-concepts.py`) in the same apply.

**Querying.** `/query "<question>"` (or the `query-orchestrator` agent) answers questions with a mandatory "What the graph guarantees" section — per load-bearing fact, the SHACL shape / OWL axiom that certifies it. Requires Fuseki up (`docker compose up -d` in `knowledge-graph/docker`, port 3031) and a fresh store (`knowledge-graph/scripts/rebuild.sh`).

**Scope.** Sidecars cover `wiki/{concepts,models,benchmarks,tools,workflows,trends,use-cases,training,state-of}/`. NOT sidecarred: `wiki/sources/`, `wiki/history/`, `wiki/_schema/` (lives in the graph as concept schemes instead), `personal/`, `index.md`, `log.md`.

**Governance.** The knowledge-graph layer's own operating rules (module boundaries, term-minting discipline, sync model) live in `knowledge-graph/governance/` and `system/authoring-guides/` — read `system/authoring-guides/term-minting.md` before proposing any new vocabulary term, exactly as this file's own controlled-vocabulary rule above requires for tags/domains/subcategories.
```

## Schema / vocabulary additions

None — this proposal only documents an existing, already-approved layer (VCR-0001/0002/0003); it introduces no new tags/domains/subcategories/terms itself.

## Open questions

- Should `wiki/sources/` eventually get lightweight `prov:Entity` sidecars (deferred in VCR-0002/0003 as future backfill scope, not decided here)? Left for a future proposal once the concepts/models/benchmarks/tools backfill shows whether it's worth the volume.
- The full-sync-vs-durable-facts-only policy was your explicit choice for the purpose of stress-testing the pipeline at this wiki's real churn rate. Once enough real daily-digest cycles have run through it (a separate, longer trial — not part of this proposal), you may want to revisit whether full sync is the right steady-state policy or whether a scoped-down variant makes more sense. Not a decision for this proposal.
- Should the second checkbox's new "Graph impact" bullet apply to `training`/`state-of` too, or only to the more fact-dense sections (`concepts/models/benchmarks/tools/workflows`)? Drafted as applying to all nine sidecarred sections for simplicity; narrow it if that turns out to be noisy in practice.
