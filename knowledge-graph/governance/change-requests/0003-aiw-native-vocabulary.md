# VCR 0003 — `aiw:` Native Module: Foundation Models, Benchmarks, License Model

**Status:** Implemented · **Date:** 2026-07-16
**Module:** `aiw:` (`https://ai-wiki.luisluna.dev/ontology/#`)
**Triggered by:** Deploying the knowledge-graph layer onto the AI Wiki; bootstrapping the vocabulary this wiki's actual subject matter (AI tools, models, benchmarks) needs beyond the inherited `swe:`/`biz:` modules (VCR-0001).

Governed by [`vocabulary-policy.md`](../vocabulary-policy.md). Admission ladder followed per term below — every native term here failed rungs 1 (no `swe:`/`biz:` catalog match after VCR-0001's full inheritance) and 2 (no upstream fit — checked schema.org, PROV, SKOS; see per-term notes).

---

## Classes

| Term | Definition | Super / upstream | Research note |
|---|---|---|---|
| `aiw:FoundationModel` | A large pretrained AI model (language, image, voice, multimodal) released as a product or open weights — the subject of a `wiki/models/` page. | ⊑ `swe:AiModel` | `swe:AiModel` (inherited, VCR-0001) is the closest fit but is defined generically as "the core AI decisioning logic... housed by the platform" — a component *of* a software system, not a standalone product/release. Rather than widen that definition (which would blur its use in `swe:` contexts), `aiw:FoundationModel` narrows it as a subclass: every FoundationModel *is* an AiModel, but not every AiModel is a page-worthy foundation model release. No upstream class for "foundation model" as a distinct release artifact exists in schema.org or PROV. |
| `aiw:Benchmark` | A standardized evaluation suite measuring an AI system's capability (e.g. SWE-bench). | — | No upstream equivalent; schema.org has no benchmark/evaluation-suite type. |
| `aiw:BenchmarkResult` | A reified measurement: one system's score on one benchmark as of one date. | — | Required by Rule 10 (datatype-domain machine-readability): a bare score has no queryable date/unit. Reification is the same pattern the inherited layer uses for `biz:` KPI values (`biz:metricValue`+`biz:metricUnit`+`biz:measuredInYear`) — this wiki's full-sync policy (volatile facts ARE synced, per the plan's explicit choice to stress-test high-volume ingestion) makes dating non-negotiable: an undated score becomes a silent contradiction the moment a newer score for the same system/benchmark is asserted. |
| `aiw:LicenseModel` | How an AI system's source/weights are released. Closed 3-member enumeration. | — | The wiki's own `wiki/_schema/tags.md` already distinguishes `open-source`/`open-weights`/`closed-source` as tags — but tags (VCR-0002) are an open-ended, page-carries-zero-to-many vocabulary. License model is a closed, mutually-exclusive, at-most-one-per-system fact ("a model is fixed-cpp OR prioritize-savings OR value-sharing"-shaped, per `vocabulary-policy.md` §6c's test for OWL enum vs `skos:Concept`), so it is modeled twice deliberately: as a `tags:` frontmatter value (human browsing/filtering) and as an OWL enum (machine-checkable exactly-one-of constraint) — the same duality the source repo used for e.g. `biz:PaymentType`. |

## Properties

| Term | Characteristics | Domain → Range |
|---|---|---|
| `aiw:onBenchmark` | Functional | `BenchmarkResult → Benchmark` |
| `aiw:achievedBy` | Functional; `owl:inverseOf aiw:hasBenchmarkResult` | `BenchmarkResult → (schema:SoftwareApplication ⊔ aiw:FoundationModel)` |
| `aiw:hasBenchmarkResult` | inverse of `achievedBy` | `(SoftwareApplication ⊔ FoundationModel) → BenchmarkResult` |
| `aiw:scoreValue` | Functional, `xsd:decimal` | `BenchmarkResult → xsd:decimal` |
| `aiw:scoreUnit` | Functional, `xsd:string`, enum-constrained | `BenchmarkResult → {percentage, points, elo, rank}` |
| `aiw:asOf` | `xsd:date` | any dated-assertion node → `xsd:date` |
| `aiw:hasLicenseModel` | Functional | `(SoftwareApplication ⊔ FoundationModel) → LicenseModel` |

## SHACL shapes added (`aiw-shapes.ttl`)

Bootstrapped by copying the **generic core** of the inherited shape library (`WikiEntityShape`, `SoftwareApplicationShape`, `RecordShape`, `ConceptShape`, the two symmetry shapes, `FoundingDateDatatypeShape`, `HowToStepShape`, `ABTestStatusShape` — all domain-agnostic) and adding native shapes:

- `aiw:BenchmarkResultShape` — every `BenchmarkResult` must declare exactly one each of `onBenchmark`, `achievedBy`, `scoreValue`, `scoreUnit`, and **`asOf`** (min/maxCount 1 on all five — an undated or unit-less result is a SHACL violation, not a warning, matching the full-sync stress-test's explicit goal of surfacing exactly this class of problem early rather than letting it accumulate silently).
- `aiw:BenchmarkPercentageRangeShape` — when `scoreUnit = "percentage"`, `scoreValue` must be 0–100 (mirrors the inherited `KPIPercentageRangeShape` pattern, adjusted range: MUSCLE's KPI percentages are stored 0–1, this wiki's benchmark percentages are stored 0–100 as that's how sources report them, e.g. "74% SWE-bench").
- `aiw:LicenseModelShape` — `hasLicenseModel`, where stated, must be one of the three enum members.

**Not carried from the inherited shape library:** `BankShape`, `PricingStrategyShape`, `DeploymentModelShape`/`IntegrationModelShape`/`TravelVerticalRoutingShape` (MUSCLE-specific individuals), `KPIMetricUnitShape`/`KPIPercentageRangeShape` (superseded by the Benchmark shapes above, which cover this wiki's actual measured-value pattern), `ControlTowerRoleShape`, and all corporate-legal-entity shapes (`OwnershipStakeShape` etc.) — none apply here.

## Deferred (explicitly, not forgotten)

- **Per-subcategory/domain enum shapes** analogous to the inherited `DeploymentModelShape` pattern are not yet written — `wiki/_schema/subcategories.md`'s "at most one subcategory" and "must be a declared slug" rules are exactly this VCR's kind of constraint, but wiring frontmatter values to the graph requires per-page sidecars first (Phase C). This VCR admits the vocabulary (VCR-0002); enforcing frontmatter-to-graph consistency is a follow-up VCR once backfill reveals the actual usage pattern.
- **`aiw:Tool`** as a class distinct from `schema:SoftwareApplication` was considered and rejected: `schema:SoftwareApplication` (inherited, already used for MUSCLE's own dashboards/apps) is a complete fit for "AI coding tool", "AI voice product", etc. — no narrowing needed, unlike `FoundationModel` vs `AiModel` above. A `wiki/tools/*.md` page's sidecar types its subject `a schema:SoftwareApplication` directly.

## Implementation checklist

- [x] Author `aiw.ttl` (4 classes, 7 properties, 3 enum-member individuals).
- [x] Author `aiw-shapes.ttl` (10 shapes: 8 inherited-generic + `BenchmarkResultShape` + `BenchmarkPercentageRangeShape` + `LicenseModelShape`).
- [x] Register both files in `kg.config.yaml` (`tbox_modules`, `shapes_file`).
- [x] Verify no naming collision with inherited `swe:`/`biz:` terms (grep clean — `aiw:` namespace is disjoint by construction).

## Amendment (2026-07-16, same-day checker review)

A checker-review pass found three real gaps between this VCR's promises and the shipped `aiw.ttl`:

1. **§2 violation:** `aiw:achievedBy` shipped with no `rdfs:range`, `aiw:hasBenchmarkResult` and `aiw:hasLicenseModel` shipped with no `rdfs:domain` — the table above promised a `(schema:SoftwareApplication ⊔ aiw:FoundationModel)` union for all three, but no `owl:unionOf` blank node was ever written. **Fixed:** added the union domain/range to all three properties, matching the existing `owl:unionOf` idiom already used elsewhere in the inherited `biz:`/`swe:` modules (e.g. `biz:offers`, `swe:integratesWith`).
2. **§1a omission:** the four new classes (`FoundationModel`, `Benchmark`, `BenchmarkResult`, `LicenseModel`) were minted with no disjointness consideration at all — not even a decision to defer it. **Fixed:** added `Benchmark`/`BenchmarkResult`/`LicenseModel` to a new conservative `owl:AllDisjointClasses` set in `disjointness.ttl`, alongside `org:Organization`/`schema:SoftwareApplication`/`schema:Country`. `FoundationModel` deliberately excluded — it already inherits disjointness from `swe:Datastore` via its `swe:AiModel` superclass, and whether it can ever be dual-typed `schema:SoftwareApplication` is a genuine open judgment call, not one to conservatively foreclose without a real case forcing the decision (same discipline `vocabulary-policy.md` §1a asks for: "only assert disjointness you are confident about").
3. **§3 cross-VCR tension:** `aiw:LicenseModel`'s three enum members duplicated VCR-0002's tag-scheme `skos:Concept`s concept-for-concept (`aiw:open-source` vs. `aiw:tag-open-source`, same real-world meaning, two unlinked IRIs) — a "one concept, one term" violation in spirit (two representations of the same license-openness concept: an informal browsing tag and a machine-checked enum value). **Fixed:** added `skos:exactMatch` triples linking each `aiw:LicenseModel` member to its `aiw:tag-*` counterpart, rather than collapsing to one IRI (which would have coupled this TBox module to instance IRIs minted by a generated ABox seed file, `gen-schema-concepts.py`'s output — an architecturally riskier fix for no real benefit over an explicit crosswalk).

Re-verified: `aiw.ttl` parses clean via rdflib (96 triples), full `rebuild.sh` green after the fix, a live query-orchestrator round-trip against the rebuilt graph correctly enumerated the `LicenseModel` closed enum and confirmed (via a synthetic double-assignment fixture) that SHACL — not the OWL functional axiom alone — is what actually catches a `hasLicenseModel` cardinality violation, since no disjointness exists *between* the three enum members themselves (only between the class and the three other top-level types added above). That's expected and correct: enum-member mutual exclusivity is `aiw-shapes.ttl`'s `sh:in`/`maxCount` job, not an OWL axiom's.
