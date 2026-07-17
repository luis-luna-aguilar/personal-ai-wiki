# Process Architecture — Wiki ⇄ Ontology

**Status:** Draft for validation · **Date:** 2026-05-21
Companion to [`master-plan.md`](./master-plan.md) and [`vocabulary-policy.md`](./vocabulary-policy.md).

This defines the two tracks, the handshake between them, and the gates that keep them clean.

---

## Track A — Wiki Ingestion (information)

Lives in `proposals/`, `wiki/`. Owns the existing ingestion pipeline in `AGENTS.md` (Phases 1–5). One change: every proposal now carries a **Terminology Reconciliation** section (see §3).

## Track B — Ontology Evolution (meaning)

Lives entirely in `knowledge-graph/`. Owns the vocabularies (`ontology/*.ttl`), shapes, and the term catalog. Evolves **only** through a Vocabulary Change Request (VCR) in `governance/change-requests/`. Never edited inline during ingestion.

---

## The handshake: Terminology Reconciliation

This is the single point where the two tracks meet. It runs while a wiki ingestion proposal is being drafted, **before** approval.

```
DRAFTING AN INGESTION PROPOSAL
│
├─ 1. Extract the concepts the new content expresses
│
├─ 2. For each concept, look it up in the VOCABULARY CATALOG
│      (knowledge-graph/ontology/lexicon-map.yaml)
│        ├─ match found  → REUSE the existing term/IRI; if the source used a
│        │                 different word, NORMALIZE the wiki prose to the canon
│        └─ no match     → candidate new term
│
├─ 3. For each candidate new term, attempt reuse one more level:
│        is there an UPSTREAM term (org/fibo/prov/skos/schema/foaf)?
│        ├─ yes → reuse upstream; add a catalog row (no native term)
│        └─ no  → open a VCR in governance/change-requests/
│
├─ 4. The proposal's "Terminology Reconciliation" section lists:
│        • Reused terms (concept → IRI)
│        • Normalizations applied (source word → canonical term)
│        • New-term VCRs opened (with links), pending Track-B approval
│
├─ 5. SCHEMA & LOGICAL ASSERTION HARVESTING — scan the source for validation rules and logical axioms
│        (cardinality, mandatory fields, enumerations, mutual exclusivity, uniqueness,
│        functional, conditional, value ranges). Each becomes a SHACL shape or
│        an OWL axiom, opened as a VCR (citing the source) and listed in the
│        proposal. This is the SUPPLY of assertions — it grows what we can enforce.
│
└─ 6. ASSERTION CONSISTENCY CHECK — run scripts/validate-ingestion.sh on the
       candidate sidecars. It checks them against the WHOLE current graph
       (HermiT consistency + reasoned SHACL) and flags any logical
       contradiction or constraint violation. Paste the result (incl. any
       robot explain output) into the proposal's "Assertion Consistency
       Check" section. See validation-architecture.md.
```

Two flows meet here. Steps 1–5 are the **supply side** — ingestion feeds the ontology new terms (4) and new schema/logical assertions (5), each governed by a VCR. Step 6 is the **enforcement side** — the accumulated assertions are run against the incoming facts. A document that states a constraint but never turns it into a shape/axiom has leaked an assertion; harvesting (step 5) is what prevents that.

The proposal references its VCRs but does **not** itself approve them. Ingestion of the affected sidecars proceeds only after the referenced VCRs are approved and the candidate passes the contradiction gate (G6).

## Gates

| Gate | Track | Rule |
|---|---|---|
| G1 — Reconciliation complete | A | No proposal is presented without a Terminology Reconciliation section. |
| G2 — Reuse exhausted | A→B | A VCR is opened only after catalog reuse *and* upstream reuse both fail. |
| G3 — VCR approved | B | A term exists only after its VCR passes `vocabulary-policy.md` review (research, definition, domain/range, SHACL, IRI registration). |
| G4 — Normalization | A | Wiki prose and sidecars use only canonical terms; source-specific synonyms are rewritten. |
| G5 — Separation | both | Governance/VCR artifacts live only in `knowledge-graph/governance/`; ingestion proposals only in `proposals/`. |
| G6 — No contradictions | A | `validate-ingestion.sh` passes: the candidate is logically consistent with the existing graph (HermiT) and violates no SHACL shape. A flagged contradiction must be resolved (fix facts) or formally amended (VCR on the axiom) before approval. |
| G7 — Assertions harvested | A→B | Every enforceable schema/logical assertion stated or implied in the source is captured as a SHACL-shape / OWL-axiom VCR (or the proposal explicitly states the source has none). No assertion is left to live only as prose. This is what keeps G6 meaningful over time. |

## Bootstrap exception

This deployment's knowledge-graph layer was bootstrapped in one pass rather than grown per-ingestion from a blank ontology. **VCR-0001** inherits the source repo's already-vetted `swe:`/`biz:` modules wholesale (admission-ladder rung 2 at repo-portability scale); **VCR-0002** folds the wiki's pre-existing `wiki/_schema` controlled vocabulary into the graph as SKOS concept schemes; **VCR-0003** authors this wiki's own small native module (`aiw:FoundationModel`/`Benchmark`/`BenchmarkResult`/`LicenseModel`) for the AI-domain vocabulary neither upstream nor the inherited modules cover. After bootstrap, all growth is per-ingestion via the handshake above.

## The health metric

Track the share of concepts per ingestion that **reuse** existing terms vs. **require** a new VCR. A healthy graph trends toward near-total reuse; a rising new-term rate signals vocabulary drift or an under-modeled domain worth a deliberate VCR batch.
