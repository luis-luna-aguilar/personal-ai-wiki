# Validation Architecture — Reasoning & Contradiction Detection

**Status:** Active · **Date:** 2026-05-21
Companion to [`process-architecture.md`](./process-architecture.md). Defines how the graph's schema and logical assertions are enforced and how incoming contradictions are flagged.

---

## The core distinction: two kinds of "wrong"

| | **Logical contradiction** | **Constraint violation** |
|---|---|---|
| Means | The facts are logically impossible together | A completeness/shape constraint (schema assertion) is broken |
| World assumption | Open-world (OWL reasoner) | Closed-world (SHACL) |
| Needs | Disjointness / cardinality / functional / inverse axioms to be *detectable* | A `sh:NodeShape` describing the schema assertion |
| Example | A node typed both `org:Organization` and `swe:Datastore` | A `SoftwareApplication` with no `schema:provider` |
| Tool | HermiT / ELK (`robot reason`, `robot explain`) | Apache Jena SHACL (`validate-shacl.sh`) |

**Key insight:** a reasoner alone flags nothing useful unless the TBox contains axioms that *make* contradictions possible. That is why `disjointness.ttl` exists — it declares the top-level structural categories mutually disjoint so mistyped nodes become logically inconsistent and get caught. We therefore run **both** engines, and we feed SHACL the **reasoned** graph so inferred types participate in constraints.

## Where the assertions come from (the supply side)

Detection is only as good as the assertions we hold. The assertion set is grown deliberately, primarily by **harvesting schema and logical assertions from ingested source documents** (`AGENTS.md` Rule 9 + the Schema & Logical Assertion Harvesting step). When a document states "a `BenchmarkResult` declares exactly one score, unit, and date", "license model ∈ {open-source, open-weights, closed-source}", or "a model is closed-source or open-weights, never both", the ingestor turns that into:
- a **SHACL shape** in `aiw-shapes.ttl` for closed-world constraints (cardinality, required fields, enumerations via `sh:in`, value ranges, uniqueness, conditional rules), or
- an **OWL axiom** for open-world contradiction detection (`owl:disjointWith` in `disjointness.ttl`; cardinality/functional in the owning module).

Each is admitted through a VCR, citing the source. So the contradiction layer is fed by ingestion, not hand-authored in isolation — the more we ingest, the more we can catch.

**Datatype domains are a first-class supply category (Rule 10 + the Datatype Domain Inventory).** Beyond relational and structural assertions, every *datatype-valued* fact carries a domain — datatype + unit/dimension + admissible range — and we capture it machine-readably rather than as prose. This yields three kinds of enforceable assertions, all VCR-gated:
- **Datatype + range** → a SHACL shape (`sh:datatype`, `sh:minInclusive`/`maxInclusive`, `sh:in`, `sh:pattern`), or an OWL 2 datatype restriction (`rdfs:Datatype` + `owl:withRestrictions`) when reasoner-side detection is wanted.
- **Structure of a reified value** (money = amount + currency + period; this deployment's own instance of the pattern is `aiw:BenchmarkResult` = score + unit + date, VCR-0003) → qualified cardinality + `owl:oneOf` axioms make a missing/duplicated/unknown part a contradiction; HermiT catches it.
- **Value kind defined by pattern** (`biz:MonthlySalary` ≡ a compensation whose period is the month) → an `owl:equivalentClass` restriction so instances self-classify and their shapes apply automatically.
The supply of these assertions is the **Datatype Domain Inventory** every proposal now produces (`AGENTS.md` Rule 10 + Phase 2).

## Three layers of validation

### L1 — Query-time (the live Fuseki store)
- Dataset wraps an **OWLMicro inference model** (`docker/config-aiwiki.ttl`).
- Materializes `rdfs:subClassOf`/`subPropertyOf`, domain/range, `owl:inverseOf`, `owl:SymmetricProperty`, `owl:TransitiveProperty`, `sameAs`.
- Effect: queries see the assertions — symmetric `swe:integratesWith`, the `swe:embeds`/`embeddedIn` inverse, every `aiw:FoundationModel` instance also typed `swe:AiModel` (via `rdfs:subClassOf`, VCR-0003), `skos:altLabel` as `rdfs:label`.
- This layer is for **entailment in queries**, not contradiction detection.

### L2 — Build-time (`rebuild.sh`, the canonical full build)
1. Merge TBox: `aiw + swe + biz + alignments + disjointness + upstream extracts`.
2. **Reason with HermiT** (full OWL DL — `KG_REASONER=ELK` for a faster EL-only fallback). On inconsistency the build aborts and prints a `robot explain` reason.
3. **SHACL on the reasoned graph** (so inferred types are checked).
4. Load into Fuseki only if both pass.

### L3 — Ingestion-time gate (`validate-ingestion.sh`, runs on proposals)
- Validates the **whole prospective graph**: merged TBox + every current ABox sidecar + the candidate file(s) — so contradictions *between incoming facts and existing data* are caught, not just within one page.
- HermiT consistency → on failure, `robot explain --mode inconsistency` produces a human-readable reason → SHACL on the reasoned graph.
- Offline (uses committed extracts, no network) so it is fast enough to run while drafting a proposal.
- Exit codes: `0` clean · `2` logical contradiction · `3` SHACL violation.
- Compare `validate-page.sh`, which checks only `TBox + one page` — useful for a quick single-file syntax/shape check, but it cannot see cross-record contradictions. **The gate is `validate-ingestion.sh`.**

## Reasoner choice

| Reasoner | Profile | Catches | Used in |
|---|---|---|---|
| **OWLMicro** (Jena rules/inferences) | RL-ish | subclass, inverse, symmetric, transitive (materialization only) | L1 live store |
| **HermiT** | full OWL DL | + cardinality, functional, disjointness, full consistency | L2 build, L3 gate |
| **ELK** | OWL EL | class hierarchy, disjointness consistency, realization (fast, tolerant) | dev fallback (`KG_REASONER=ELK`) |

HermiT is the default for L2/L3 because it is the most complete and runs in seconds at this scale. If a future upstream extract introduces non-OWL-DL axioms and HermiT errors, fall back to `KG_REASONER=ELK` (which still catches disjointness contradictions) and fix the extract.

## What to do when a contradiction is flagged

The `robot explain` output names the exact assertions and the axiom that clash. Paste it into the proposal's **Assertion Consistency Check** section and resolve before approval — either correct the incoming facts, or, if the logical assertion itself is wrong, open a VCR to amend the axiom (e.g. relax a disjointness). Axioms are governed exactly like vocabulary terms (`vocabulary-policy.md`).
