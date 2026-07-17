# VCR 0002 — `wiki/_schema` Controlled Vocabulary as SKOS Concept Schemes

**Status:** Implemented · **Date:** 2026-07-16
**Module:** `aiw:` (`https://ai-wiki.luisluna.dev/ontology/#`) — instance data (SKOS individuals), no new classes
**Triggered by:** Deploying the knowledge-graph layer onto the AI Wiki

Governed by [`vocabulary-policy.md`](../vocabulary-policy.md) §6c (OWL enum vs `skos:Concept` test) and `system/authoring-guides/skos-concept.md` (inherited guide).

---

## Rationale

The AI Wiki already has a controlled, approval-gated vocabulary in `wiki/_schema/{domains,subcategories,tags}.md` — the same discipline `vocabulary-policy.md` enforces for the ontology, just enforced on Markdown frontmatter instead of RDF (`AGENTS.md` §"Controlled vocabulary": "Never use a tag, domain, or subcategory that isn't in these files... propose it explicitly in a proposal file"). Rather than build a parallel, disconnected vocabulary-approval process for the graph, this VCR makes the *existing* `_schema` files the graph's controlled vocabulary too: every domain/subcategory/tag becomes a `skos:Concept`, and the wiki's existing approval gate (a proposal's "Schema / vocabulary additions" checkbox) becomes the same event as a VCR term admission for these three vocabularies specifically.

This is the §6c "open-ended tag with no fixed cardinality rule" case for `domains`/`tags` (subject-matter/attribute tags a page can carry zero-to-many of) and, for `subcategories`, a hybrid: subcategories are open-ended as a *set* (grows by proposal) but each page has *at most one*, matching how `subcategory:` frontmatter already behaves — modeled as `skos:Concept` (not a closed OWL enum) because the set is explicitly designed to grow via ordinary proposals, not VCRs, and forcing every schema addition through the heavier VCR/OWL-enum path would defeat the wiki's existing lightweight approval flow.

## What was minted

Three `skos:ConceptScheme` individuals — `aiw:domain-scheme`, `aiw:subcategory-scheme`, `aiw:tag-scheme` — and one `skos:Concept` per declared slug in each `_schema` file, generated mechanically (not hand-authored) by the new `knowledge-graph/scripts/gen-schema-concepts.py`:

- **12 domains** → `aiw:domain-<slug>` (e.g. `aiw:domain-coding`), each `skos:inScheme aiw:domain-scheme`.
- **32 subcategories** → `aiw:subcategory-<slug>`, each `skos:inScheme aiw:subcategory-scheme` and `skos:broader aiw:domain-<parent>` for every parent domain listed in the subcategory's "Parent domain(s)" line (subcategories.md already declares this hierarchy in prose; the generator makes it a real SKOS triple).
- **24 tags** → `aiw:tag-<slug>`, each `skos:inScheme aiw:tag-scheme`.

Every concept carries `skos:prefLabel` (the slug) and `skos:definition` (the `_schema` file's own one-line description, copied verbatim) — satisfying `aiw:ConceptShape` (inherited from the source layer's `ConceptShape`, unchanged).

IRIs are namespaced by kind (`domain-`/`subcategory-`/`tag-` prefixes) specifically so they can never collide with page-slug instance IRIs (`aiw:<page-slug>`) — a domain and a page could otherwise coincidentally share a slug.

## Regeneration is mechanical, not a VCR event

`gen-schema-concepts.py` is a **pure compiler** from `_schema/*.md` to `ontology/seeds/schema-concepts.ttl` — analogous to `gen-ulex.py` compiling `lexicon-map.yaml` to `.ulex`. It must be re-run (and its output committed) every time a proposal adds an approved domain/subcategory/tag, **in the same apply as the `.md` change** — this is not a new VCR each time, because the *vocabulary of vocabularies* (SKOS as the modeling choice) was admitted once, here. This mirrors how the source repo's `gen-ulex.py`/`gen-seeds.py` regenerate derived artifacts from a canonical source without a fresh VCR per regeneration.

**AGENTS.md amendment note (see VCR-adjacent Phase B3 proposal):** the wiki's "Apply proposal" workflow gains a step — when a proposal's "Schema / vocabulary additions" section is checked, `gen-schema-concepts.py` runs as part of the same apply, and the regenerated `schema-concepts.ttl` is committed alongside the `_schema/*.md` change.

## Not adopted / deferred

- `source-types.md` (the fourth `_schema` file) is **not** modeled as SKOS — it defines per-type *ingest playbooks* (procedural guidance for the LLM), not a controlled value set a page's frontmatter draws from. No graph representation needed.
- Cross-links between `wiki/tools/*.md` pages and their `domains`/`subcategory`/`tags` frontmatter values are **not yet asserted** — that requires per-page sidecars (Phase C backfill), which will assert e.g. `aiw:claude-code aiw:hasSubcategory aiw:subcategory-terminal-coding-agent`. This VCR only admits the vocabulary itself; wiring pages to it is backfill, not a vocabulary decision.

## Implementation checklist

- [x] Write `knowledge-graph/scripts/gen-schema-concepts.py` (parses `_schema/*.md`, emits `seeds/schema-concepts.ttl`).
- [x] Register `seeds/schema-concepts.ttl` in `kg.config.yaml` → `ontology.abox_seeds` (concatenated into every whole-graph build, same pattern as the inherited `countries.ttl` seed).
- [x] Run the generator: 12 domains, 32 subcategories, 24 tags → verified the output parses as valid Turtle (393 triples).
- [x] Confirm every subcategory's parent-domain reference resolves (no dangling `skos:broader` — the generator warns and skips any parent not found in `domains.md`, none triggered).
