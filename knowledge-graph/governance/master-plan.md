# AI Wiki Knowledge Graph — Master Plan

**Status:** Draft for validation · **Date:** 2026-05-21

This document governs the relationship between the **Wiki** (information) and the **Ontology** (meaning). It is the top of the governance set:

- `master-plan.md` *(this file)* — the symbiotic model and its principles
- `process-architecture.md` — the two-track workflow and the handshake between them
- `vocabulary-policy.md` — the rules for admitting, naming, and retiring terms
- `change-requests/` — the audit trail; one Vocabulary Change Request (VCR) per addition

---

## 1. Two systems of record

| | **Wiki** (`wiki/`, `proposals/`) | **Ontology** (`knowledge-graph/`) |
|---|---|---|
| Governs | Information — what the AI Wiki knows | Meaning — the controlled terms that information is expressed in |
| Unit | Markdown page (+ `.ttl` sidecar) | Class / property / shape (+ permanent IRI) |
| Changes via | Ingestion proposal → approval | Vocabulary Change Request → approval |
| Authority | System of record for *facts* | System of record for *vocabulary* |

They are **separate processes with one controlled handshake.** The wiki never invents ontology terms inline; the ontology never stores business facts.

## 2. What the ontology is *for*

Beyond mapping concepts to IRIs, the ontology has a job that is easy to miss:

> **It reduces ambiguity by limiting the set of terms in which information may be described.**

A document could be written with dozens of near-synonyms ("administers", "manages", "controls", "operates", "runs"). The ontology forces a choice: one concept → one canonical term → one IRI. Ingestion is therefore authored **against the available vocabulary**, deliberately reusing existing terms instead of spending the large variety of terms it *could* use. Constraint is the feature, not a limitation.

## 3. The symbiosis

```
        new information                       new meaning (rare, governed)
   ────────────────────────▶                ◀────────────────────────
  WIKI                                                         ONTOLOGY
  (drives demand for terms)                    (constrains & normalizes terms)

    every ingestion:
      1. is written using existing vocabulary wherever possible   ← REUSE terms
      2. surfaces only genuinely-unmatched concepts as VCRs       ← GROW terms deliberately
      3. is normalized so its wording matches the canon           ← NO alias drift
      4. harvests SCHEMA & LOGICAL ASSERTIONS the source states   ← GROW constraints
         (cardinality, enumerations, mutual exclusivity, …)
         into shapes/axioms
      5. is checked against all accumulated assertions            ← ENFORCE (flag contradictions)
```

Ingestion supplies the ontology with **two** things, both governed by VCRs: **terms** (the vocabulary) and **assertions** (SHACL shapes + OWL axioms). The first lets us *describe* facts unambiguously; the second lets us *catch* facts that contradict each other or break a stated constraint. A source document that states a schema or logical assertion but never turns it into a shape/axiom has leaked enforceable knowledge — harvesting it (step 4) is a first-class duty, not an afterthought.

- **The wiki drives demand.** New content reveals both concepts the vocabulary can't yet express *and* assertions the constraint set doesn't yet enforce.
- **The ontology constrains supply.** New terms and new assertions are admitted only when genuinely needed, and only through a VCR (`vocabulary-policy.md`).
- **Both win over time.** As the term pool *and* the assertion set mature, more new content lands inside the existing vocabulary, and more incoming contradictions are caught automatically. Falling new-term frequency and rising contradiction-catch coverage are the twin health metrics. See `validation-architecture.md`.

## 4. The authored vocabularies + upstream

This deployment reuses upstream ontologies first, and — per VCR-0001 — inherits the source repo's already-vetted `swe:`/`biz:` modules wholesale rather than re-deriving generic software/business vocabulary from scratch. Where no upstream or inherited term exists, the wiki authors a term itself — but in its own **domain-named, independently publishable module**, never under a company-branded grab-bag:

| Module | Namespace · prefix | Scope |
|---|---|---|
| Upstream | `org: fibo: prov: skos: schema: foaf:` | reuse, unchanged |
| **Software Engineering** *(inherited, VCR-0001)* | `https://musclepoints.com/ontology/swe#` · `swe:` | software systems, architecture, integration, deployment — kept under its original namespace per IRI permanence (`vocabulary-policy.md` §5) |
| **Business** *(inherited, VCR-0001)* | `https://musclepoints.com/ontology/biz#` · `biz:` | general commercial relations with no upstream home (client-of, uses-product, deployment model, payment type) |
| **AI Wiki core + data** | `https://ai-wiki.luisluna.dev/ontology/#` · `aiw:` | the native classes this wiki's own subject matter needs with no upstream/inherited fit (`FoundationModel`, `Benchmark`, `BenchmarkResult`, `LicenseModel` — VCR-0003) **and all instance data** (`aiw:claude-code`, …) |

Key consequences:
- `swe:` and `biz:` are **vocabulary** (TBox) and contain **no AI-Wiki-specific facts** — so they remain donatable/reusable by anyone, exactly as they were before this wiki adopted them.
- `aiw:` holds the **ABox** (the actual pages) plus this wiki's small set of native classes. Instances are typed by classes drawn from upstream + `swe:` + `biz:` + `aiw:`.
- Minimization applies **inside** `swe:`/`biz:` too: reuse `prov:Activity`, `prov:Agent`, `org:Role`, etc. where the fit is clean; author native terms only for genuine gaps.

## 5. The wiki⇄ontology handshake also covers controlled Markdown vocabulary

Beyond ingestion prose, this deployment has a second, purely-Markdown controlled vocabulary — `wiki/_schema/{domains,subcategories,tags}.md` — that predates the graph layer. VCR-0002 folds it into the same handshake by mapping every declared domain/subcategory/tag to a `skos:Concept` (mechanically generated, not hand-authored, by `knowledge-graph/scripts/gen-schema-concepts.py`). This means the wiki's existing lightweight schema-approval process *is* the VCR admission event for these three vocabularies — there is no separate, parallel approval step. The source repo had no equivalent controlled-vocabulary Markdown to reconcile this way; it is this deployment's own addition to the model.

## 6. Non-goals

- The ontology does **not** model software *packaging* (SPDX/CycloneDX: licenses, supply chain) — inherited from `swe:`'s original scope discipline, and this wiki ships no distributable artifacts of its own either.
- Governance docs and VCRs live **only** under `knowledge-graph/governance/`. They are **never** placed in `proposals/`, which is reserved for wiki ingestion.
