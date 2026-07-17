# VCR 0004 — Benchmark-Demo Vocabulary (lexicon rows for VCR-0003's `aiw:` module)

**Status:** Implemented · **Date:** 2026-07-17
**Module:** `aiw:` (lexicon rows only — no new classes/properties beyond what VCR-0003 already minted, except `aiw:hasVariant`/`aiw:hasDomain`/`aiw:hasSubcategory`/`aiw:hasTag`, added here)
**Triggered by:** Preparing a same-day demo of query-layer capability on model-benchmark comparisons (user request, 2026-07-17) — the numerical, dated, unit-carrying `aiw:BenchmarkResult` pattern is the strongest available showcase of what SHACL/OWL certification actually buys over a plain wiki.

Governed by [`vocabulary-policy.md`](../vocabulary-policy.md). Unlike VCR-0001/0003, this VCR mints almost no new IRIs — it is primarily **ACE lexicon rows** (word ↔ grammar ↔ IRI mappings) for classes/properties VCR-0003 already defined, since the pilot round (5 concept pages, no lexicon rows written yet) never actually exercised the `aiw:` module through the ACE compiler.

---

## New classes/properties (beyond VCR-0003)

| Term | Definition | Domain → Range | Research note |
|---|---|---|---|
| `aiw:hasVariant` | A benchmark family's named variant (SWE-bench → SWE-bench Verified/Pro/Multilingual) | `aiw:Benchmark → aiw:Benchmark` | Deliberately **not** `skos:narrower` — benchmarks are not `skos:Concept`s, and inheriting `ConceptShape`'s prefLabel/definition obligation onto measurement-suite individuals would misapply a topic-tagging shape to a different kind of thing. |
| `aiw:hasDomain` | A page's frontmatter `domains:` value(s) → `aiw:domain-<slug>` (VCR-0002 scheme) | any → `skos:Concept` | Every one of the 5 pilot-batch extractions independently flagged this gap — admitted once, here, rather than per-page. |
| `aiw:hasSubcategory` | A page's frontmatter `subcategory:` value → `aiw:subcategory-<slug>` | any → `skos:Concept`, functional | Functional because the wiki's own rule is "a page has at most one subcategory" — enforced by the new `aiw:SubcategoryShape`. |
| `aiw:hasTag` | A page's frontmatter `tags:` value(s) → `aiw:tag-<slug>` | any → `skos:Concept` | Same rationale as `hasDomain`. |

SHACL added: `aiw:SubcategoryShape` (maxCount 1, `sh:class skos:Concept` — a typo'd slug fails because the individual is untyped), `aiw:DomainTagValueShape` (same class check for `hasDomain`/`hasTag`, no cardinality limit).

## Lexicon rows admitted (ACE surface forms for existing `aiw:` IRIs)

`benchmark`, `benchmark-result`, `foundation-model` (+ alias `model`, same alias-collapsing precedent as the source project's `strategy`/`pricing-strategy`), `is-measured-on` → `onBenchmark`, `is-achieved-by` → `achievedBy`, `has-benchmark-result` → `hasBenchmarkResult`, `has-variant` → `hasVariant`, `has-license-model` → `hasLicenseModel`, `has-domain`/`has-subcategory`/`has-tag` → the three new properties above, `open-source-license`/`open-weights-license`/`closed-source-license` → the three `aiw:LicenseModel` enum individuals (VCR-0003).

**Datatype properties — `score-value`, `score-unit`, `as-of-date`** (→ `aiw:scoreValue`/`scoreUnit`/`asOf`): declared `ace: {pos: noun}`, **not** `pos: tv`. A `DatatypeProperty` role lexicon entry is asserted via the `X has a <noun> that is "<literal>".` construction (confirmed empirically against real committed `.ace` precedent — `date-created`'s existing usage, `X has a date-created that is "2023-08-16".`), not a bare transitive-verb form. An earlier draft of this VCR wrongly declared these as `pos: tv` (`has-score-value 77.2.`) — caught in a throwaway grammar test before touching any real page, not after.

**One reused term, not re-minted:** `is-provided-by` → `schema:provider` was drafted, then found to duplicate an already-inherited row (`is-provided-by` → `biz:providedBy`, VCR-0020, domain `owl:Thing` / range `org:FormalOrganization` — generic enough to cover model/benchmark provider attribution as-is). Removed the duplicate; reused the existing row. Caught by the same grammar test, which surfaced the compiler silently preferring the first-matching row rather than erroring on the duplicate id — worth knowing for future VCRs: **duplicate lexicon ids do not fail loudly**, so grep for the id before adding a row, not just for the target IRI.

## Grammar patterns confirmed for this VCR (worth carrying forward)

1. **Referencing an enum-member Individual as a verb's object requires `the`:** `X has-license-model the open-weights-license.` — bare `open-weights-license` (no determiner) fails APE; `the <individual>` parses and the compiler correctly strips the determiner during IRI resolution (verified: compiles to `aiw:open-weights`, not a mangled lemma).
2. **`DatatypeProperty`-role lexicon rows use `has a <noun> that is "<value>"`, never a bare transitive verb.** Confirmed against real committed precedent (`date-created`) before minting the three new rows here.
3. **Duplicate lexicon `id`s are silently shadowed, not rejected** — the compiler resolves by first match. No structural gate catches this; manual `grep` discipline is the only safeguard until/unless `gen-ulex.py` grows a duplicate-id check (flagged as a gap, not fixed here — out of scope for a vocabulary VCR).

## Validation

A throwaway 16-sentence grammar test (`/tmp/demo-grammar-test2.ace`, not committed) exercising every new term — classes, object properties, the `the <individual>` pattern, all three datatype-property forms, and the reused `is-provided-by` — parsed 16/16 through APE and compiled to 16 correct triples (0 unmapped, 3 auto-generated SHACL datatype shapes) before any real wiki page was touched.

## Implementation checklist

- [x] Add `aiw:hasVariant`/`hasDomain`/`hasSubcategory`/`hasTag` to `aiw.ttl`.
- [x] Add `aiw:SubcategoryShape`/`DomainTagValueShape` to `aiw-shapes.ttl`.
- [x] Add 20 lexicon rows to `lexicon-map.yaml` (464 total, up from 446 post-VCR-0001 filter).
- [x] Regenerate `aiw-lexicon.ulex` (295 nouns · 15 mass nouns · 143 verbs · 11 adjectives).
- [x] Validate via throwaway grammar test before touching real pages (16/16 APE pass, clean compile).
- [x] Catch and fix one duplicate lexicon row (`is-provided-by`) and one wrong-POS mistake (3 datatype rows) before they reached real content.
