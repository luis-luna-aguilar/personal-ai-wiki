# Overnight Run Report — Knowledge-Graph Layer Deployment

**Run date:** 2026-07-16 night → 2026-07-17 morning
**Mode:** Unattended (explicit overnight authorization from the user's other repo, `company-brain`)
**Full report with company-brain's own Phase A details:** `/Users/luis/Code/GitHub/muscle/company-brain/tmp/overnight-report.md` — read that one first for the complete picture; this is the AI-Wiki-focused half.

**tl;dr:** The knowledge-graph layer (Fuseki/SPARQL + SHACL/OWL validation) is deployed and working on branch `kg-layer` (2 commits, nothing merged to `main`, nothing pushed). A 5-page pilot extraction ran but deliberately stopped before compiling to `.ttl` — see §3.

---

## 1. What's live right now

- **Branch:** `kg-layer`, 2 commits ahead of `main` (`2a5cf54` the deployment, `e9f0900` the pilot WIP). Nothing merged, nothing pushed.
- **Fuseki:** running in Docker at `http://localhost:3031/aiwiki` (container `aiw-fuseki`, compose project `aiw-kg` — isolated from anything else that might run on this machine). Confirmed running alongside a second Fuseki instance on port 3030 with no interference.
- **Ontology:** `knowledge-graph/ontology/{swe,biz}.ttl` (inherited, pruned of dangling references — see §2), `aiw.ttl` (native: `FoundationModel`, `Benchmark`, `BenchmarkResult`, `LicenseModel`), `aiw-shapes.ttl` (SHACL), `seeds/schema-concepts.ttl` (your `wiki/_schema/{domains,subcategories,tags}.md` compiled into SKOS — 12 domains, 32 subcategories, 24 tags, all queryable now).
- **Query layer:** `.claude/agents/{query-orchestrator,wiki-answerer,kg-verifier,ace-extractor}.md` + `/query` command, adapted to this wiki (paths, `aiw:` prefix, examples). Verified working with a real round-trip — see §4.
- **AGENTS.md:** two new blocks added via your own proposal flow (not a direct edit) — search for "Knowledge graph sidecars" (new section) and "Graph impact" (new bullet in the existing Workflow 5 rules). The applied proposal is at `proposals/applied/2026-07-16-knowledge-graph-layer.md` if you want the full before/after.
- **Neo4j prototype:** retired. `agents/ontology/` and `agents/mcp/ontology/` moved to `agents/attic/` (via `git mv`, full history preserved, nothing deleted). `agents/mcp/engine.py` and `agents/pyproject.toml` cleaned of the dead wiring (the `use_personal_wiki` tool no longer exposes `ontology_search`/`ontology_expand`/`ontology_actions`). Note in `agents/FUTURE_WORK.md` explains the rationale if you want the full reasoning later.

## 2. Two real defects were found and fixed before I called this "done"

A checker-review pass (a fresh subagent re-verifying the drafted VCRs against the actual `.ttl` files and the governing policy — not just re-reading my own claims) found the first two of three VCRs had real problems, both fixed:

- **The "inherited vocabulary" VCR initially claimed `swe:`/`biz:` were pruned of MUSCLE-specific content, but weren't** — ~24 dangling references to a `muscle:PricingStrategy` class that was correctly excluded from this repo, but whose dependent properties (pricing-modality types, budget/redemption-limit fields, etc.) were never cleaned up. Fixed: removed 24 dead properties/classes that existed only to reference the missing class.
- **The native `aiw:` vocabulary module was missing some required structure**: three properties had no declared type range, the four new classes had no "these are different kinds of thing" safety rail (disjointness), and the license-model vocabulary accidentally duplicated a concept you already have in `wiki/_schema/tags.md` with no link between the two. Fixed: added the missing type constraints, added the safety-rail axioms, linked the duplicate concepts together.

Full details of what was found and fixed are documented in each VCR's own "Amendment" section — `knowledge-graph/governance/change-requests/0001-inherited-vocabulary-adoption.md` and `.../0003-aiw-native-vocabulary.md`.

The third VCR (mapping your `_schema` files into the graph) passed review cleanly with no issues.

## 3. The backfill (Phase C) is NOT done — 5 pages piloted, none compiled yet

Per the plan, I ran a 5-page pilot on stable concept pages (`mcp`, `spec-driven-development`, `agent-evals`, `harness`, `quantization`) before attempting any wider batch. Each page got a real `.ace` sidecar (the intermediate fact-extraction format) with high coverage (~98–100% of the source content captured). Real numbers are in `knowledge-graph/metrics/backfill-log.csv`.

**What's missing:** none of these 5 pages have a compiled `.ttl` yet. Combined, they surfaced **~277 candidate new vocabulary words** with no existing entry in the graph's dictionary (`lexicon-map.yaml`) — expected, since this wiki's inherited vocabulary came from a banking/travel-industry knowledge base with almost no AI terminology in it yet. Admitting ~277 terms correctly (deciding which module each belongs in, checking for near-duplicates, following the same review discipline that just caught the two real mistakes above) is a substantial, judgment-heavy task on its own. I chose not to rush it in the time remaining rather than risk shipping the same kind of mistake at 50x the scale, unreviewed.

**Bottom line:** the pipeline works end-to-end (proven by getting real, high-coverage extractions from real pages), but the wiki's vocabulary is still almost entirely unpopulated for AI-domain content. The next session's first job should be: read the 5 pages' new-term lists (in `tmp/ace-extractor/*.new-terms.yaml`, gitignored scratch files — still on disk), merge and dedupe them, and admit the merged set via one new VCR before compiling any of these 5 pages.

One small thing: the `agent-evals` page's extraction receipt landed in the wrong repo's scratch folder (harmless — it's in `company-brain`'s `tmp/ace-extractor/` instead of this repo's, both gitignored either way).

## 4. The query layer actually works — tested live

I ran a real question through `query-orchestrator` against this wiki's own graph (not the other repo's): "what subcategories exist under the coding domain, and what license models does the vocabulary define?" It correctly used *this* wiki's Fuseki (port 3031), gave a verdict-first answer (7 coding subcategories, 3 license models), and included the mandatory "What the graph guarantees" section citing actual SHACL/OWL rule checks — including an honest, technically interesting finding: the reasoner alone doesn't catch a model with two conflicting license-model claims, but the SHACL validation layer does. That's now fixed structurally (see §2's second bullet) but the query layer correctly reported the distinction either way.

## 5. What needs your attention, in order

1. **Skim `AGENTS.md`'s two new blocks** before your next content session — they change how proposals that touch `concepts/models/benchmarks/tools/workflows/trends/use-cases/training/state-of` pages should be written from now on (a lightweight new requirement, not a heavy one).
2. **Read the two VCR "Amendment" sections** (§2 above) — even a quick skim tells you what almost shipped wrong and how it was caught.
3. **Decide how you want to handle the 277-term vocabulary admission** — this is real, meaningful work, not busywork, and you may want to be involved in at least the "which module does this belong in" calls rather than have a future session run it fully unattended.
4. **Check the pilot's 5 `.ace` files** (`wiki/concepts/{mcp,spec-driven-development,agent-evals,harness,quantization}.ace`) if you're curious what the extraction actually captured — they're plain, readable English sentences.

## 6. Hard constraints — confirmed honored

- `raw/` and `raw_sources/` untouched.
- Nothing deleted — Neo4j retirement used `git mv`, full history intact in `agents/attic/`.
- No pushes, no merge to `main`.
- Docker containers isolated (`aiw-kg` compose project vs. whatever else runs on this machine) — verified both running with no port/name collisions.
