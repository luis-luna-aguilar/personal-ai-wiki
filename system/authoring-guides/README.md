# Authoring Guides — Index

Each guide below documents a **structural pattern**: a fact modeled by composing several already-confirmed vocabulary terms together (a class + specific properties, used the same way every time). `knowledge-graph/ontology/lexicon-map.yaml` catalogs individual word↔IRI mappings — it does not, and should not, catalog these multi-property recipes. This directory is where that second kind of knowledge lives.

Read the matching guide **before** writing a sidecar for that shape of fact — it's prevention, not review (see `AGENTS.md`'s Sidecar Authoring Checklist).

This authoring-guides layer was ported from the MUSCLE company-brain repo (VCR-0001) and adapted to this wiki's own subject matter (AI tools, models, benchmarks, sources) rather than MUSCLE's (banks, pricing strategies, corporate structure). The table below lists only the guides that actually exist in **this** deployment.

| Guide | Covers | Trigger |
|---|---|---|
| `skos-concept.md` | `skos:Concept` individuals (open-ended subject-matter tags, `_schema` domains/subcategories/tags, topics) | Modeling a domain, a topic, a `schema:about`/`schema:knowsAbout` target, or any open-ended tag with no fixed membership |
| `entity.md` | Organization individuals (AI labs/providers — Anthropic, OpenAI, etc.) referenced via `schema:provider`/`org:unitOf`/`org:linkedTo` | Creating or modifying the org individual a tool/model page's `schema:provider` points at |
| `software-application.md` | `schema:SoftwareApplication` individuals (AI tools — `wiki/tools/*.md`) | Creating or modifying a tool sidecar — provider, embedding, API consumption, hosting availability |
| `numbered-process-steps.md` | An ordered workflow: `prov:Activity, schema:HowTo` + `schema:HowToStep`/`schema:position`/`schema:step`, plus the optional native `biz:Process`/`biz:ProtocolStep`/`biz:precedes` overlay | The source describes a numbered sequence of steps ("Step 1: ...", a 3-step explore-plan-code workflow) |
| `org-role.md` | `org:Role` individuals annotated with `skos:prefLabel`/`skos:definition` (not `skos:Concept`) | Modeling a named user-role/permission-level for a tool's access model — **dormant in this deployment**, no source yet documents a tool's roles in enough detail; kept on file |
| `record-page.md` | `wiki/sources/**/*.md` sidecars: `prov:Entity` + `dct:date` + `prov:wasDerivedFrom` | Creating or modifying a dated source-summary page |
| `enum-member-concept.md` | Dual-typing a closed enum member (`aiw:LicenseModel`, `swe:DeploymentModel`, ...) as `skos:Concept` when it also needs to be a `schema:knowsAbout`/`schema:about`/`skos:related`/`skos:narrower` target | An enum value the source also treats as a linkable topic, not just a property value |
| `term-minting.md` | Whether a concept needs a new class/property/individual at all, before any of the above apply | Proposing any new vocabulary term in a VCR |
| `controlled-english.md` | Writing valid `.ace` sentences | Authoring or editing a `.ace` sidecar |
| `large-source-ingestion.md` | Splitting a dense, multi-section raw source into per-section proposals, each with a line-by-line extraction map, instead of one flat proposal that compresses tables into summary bullets | The source has more than ~3-4 major sections carrying substantial tabular/structured detail — a single proposal's Proposed-Actions section would need one line per table row to stay honest |

**Guides from the source repo not carried over:** `kpi-metric.md`, `metric-concept.md`, `retail-category.md`, `api-vendor.md`, `payment-gateway.md`, and `corporate-legal-entity.md` covered MUSCLE-specific structural patterns (banking KPIs, retail categories, third-party API vendors, corporate ownership structures) with no current analog in this wiki's subject matter. If a future source needs one of these shapes (e.g. this wiki eventually tracks a measured metric with a value+unit+direction the way `kpi-metric.md` did), write a new guide rather than resurrecting the old MUSCLE-flavored one wholesale — check whether the shape still fits first.

## How this index stays honest

This list is only useful if it's complete. Two ways a pattern can exist without a guide: nobody noticed it recurring, or someone noticed but didn't write it down. Run this to check for the first kind:

```
python3 knowledge-graph/scripts/find-undocumented-patterns.py
```

It parses every `wiki/**/*.ttl`, finds individuals that share the same (type, predicate-set) signature two or more times, and reports any such signature not already listed in the script's `COVERED_SIGNATURES` registry. A "recurring signature with no covered entry" is a real, load-bearing pattern that just hasn't been written up yet — not a false positive to dismiss.

**Note on the script's current state:** `COVERED_SIGNATURES` still carries entries for the six MUSCLE-only guides listed above as "not carried over" (they were ported along with the rest of the script's registry and haven't been pruned). Those entries are harmless dead weight — this wiki has no individuals of those types yet, so they'll never match — but don't take their presence in the script as evidence those guides exist here; this README is the source of truth for what's actually documented in this deployment.

**When you add a new guide, add its signature to `COVERED_SIGNATURES` in that script** — otherwise every future run re-reports a pattern that's actually already documented, and the tool stops being trustworthy.

**When the script flags something and you decide *not* to write a guide for it yet** (too few instances, still evolving, not worth the overhead), say so explicitly in the VCR or proposal that surfaced it — a silently-ignored flag is worse than no flag at all, because the next person has no way to tell "considered and deferred" from "never seen."

### Status as of this deployment's bootstrap (2026-07-16)

No `wiki/**/*.ttl` sidecars exist yet in this deployment (per-page backfill is deferred to Phase C — see VCR-0002's "not yet asserted" note). `find-undocumented-patterns.py` has not yet been run against real content here; once backfill begins, run it periodically the same way the source project did, and update this index (and `COVERED_SIGNATURES`) as real recurring patterns emerge.
