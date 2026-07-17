# Vocabulary Policy — Rules for Admitting Terms

**Status:** Draft for validation · **Date:** 2026-05-21
Companion to [`master-plan.md`](./master-plan.md) and [`process-architecture.md`](./process-architecture.md).

A term (class or property) enters the ontology **only** through an approved Vocabulary Change Request (VCR). This document is the rule set every VCR is judged against.

---

## 1. The admission ladder (try each rung before the next)

1. **Reuse a canonical term we already have.** Consult the catalog (`ontology/lexicon-map.yaml`). If the concept already has a term, use it — and normalize any differing source wording to it.
2. **Reuse an upstream term.** Research `org`, `fibo`, `prov`, `skos`, `schema`, `foaf` (and named others) for a genuine fit. A term is "a fit" only if its *defined* semantics match — not merely its label. Misusing an upstream term (e.g. SPDX `contains` for UI embedding) is worse than authoring a native one, because the reasoner will draw wrong inferences.
3. **Author a native term** in the correct domain module (`swe:` or `biz:` — see §6/§6a), or `aiw:` only if it passes the portability test in §6b. Requires a research note proving rungs 1–2 failed. **Before minting anything, work through `system/authoring-guides/term-minting.md`** — it operationalizes §6a/§6b/§6c as a step-by-step pre-flight check (rung-1 catalog search, class-vs-individual, module choice, enum-vs-concept, naming) and exists specifically to catch the mistakes it's named after.

## 1a. Disjointness is part of admission

When a VCR adds a new **top-level class** that is structurally incompatible with the existing categories, it must also add the appropriate `owl:disjointWith` / `owl:AllDisjointClasses` axiom in `ontology/disjointness.ttl`. Disjointness is what makes mistyping detectable as a contradiction (see `validation-architecture.md`) — a class that is never declared disjoint from anything can never trigger a contradiction. Keep it conservative: only assert disjointness you are confident about; widening later is cheap, retracting a wrong axiom after data depends on it is not. Amending or relaxing a disjointness axiom is itself a VCR.

## 2. Every native term must carry

- A precise one-line `rdfs:comment` definition that would make sense to an outside reader.
- `rdfs:domain` and `rdfs:range`, reusing upstream classes where possible.
- An inverse (`owl:inverseOf`) where the relation is naturally bidirectional, or `owl:SymmetricProperty` where it is peer.
- A SHACL shape if the term carries a wiki completeness constraint.
- **For a datatype property: its full datatype domain, modelled for machine-readability (Rule 10).** Declare the `rdfs:range` datatype, and represent the *unit/dimension* as structure rather than in the label — reuse `schema:MonetaryAmount`/`schema:value`, W3C OWL-Time, or QUDT, and **reify** a structured value (amount + currency + period) instead of encoding the unit in the property name. Any standalone value range, enumeration, or pattern is admitted as a SHACL shape (closed-world) or an OWL datatype restriction (open-world); a value *kind* that is just a pattern is a defined class via `owl:equivalentClass` restriction. See `validation-architecture.md`.
- A research note in its VCR proving no upstream equivalent exists.

## 3. One concept, one term (ambiguity reduction)

The ontology's purpose is to **shrink** the term space. Therefore:
- **No synonym terms in the vocabulary.** If "manages" exists, do not also admit "administers", "controls", or "operates" for the same relation. Pick one canonical term; rewrite content to match.
- **Entity-name aliases are different and allowed.** A single entity with multiple human names (e.g. a tool called both by its product name and its CLI binary name, "Claude Code" / `claude`) collapses to **one IRI** via `skos:altLabel` / `owl:sameAs`. This *reduces* ambiguity (many names → one thing) and is encouraged. The ban is on multiple *vocabulary terms* for one *relation/type*, not on recording that an entity is known by several names.

## 4. Naming

- Modules are **domain-named, not company-named**: `swe:` (software engineering), `biz:` (business). Never `msw:`-style company-branded prefixes.
- Namespaces: inherited `swe:`/`biz:` keep their original `https://musclepoints.com/ontology/<domain>#` IRIs per IRI permanence (§5) — they are reused upstream vocabulary (VCR-0001), not forked. This wiki's own native module lives at `https://ai-wiki.luisluna.dev/ontology/#` (`aiw:`), which — like the source repo's own `muscle:` — is deployment-branded by design because it is also the ABox/instance namespace, not a portable domain vocabulary.
- Prefer plain-English, widely-understood labels (`manages`, not `administers`).

## 5. IRI permanence

IRIs are forever. Never rename `swe:embeds`, `biz:clientOf`, or `aiw:claude-code`. If a label changes, update `rdfs:label`/`skos:altLabel`, not the IRI. If a wiki file is renamed, add `owl:sameAs`/`skos:altLabel` rather than re-minting.

## 6. Module boundaries

| Module    | Admits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Rejects                                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `swe:`    | software systems, architecture, integration, deployment; later: engineering process (inherited wholesale, VCR-0001)                                                                                                                                                                                                                                                                                                                                                                                                                                                | business relations; software packaging (SPDX-style)                                                                              |
| `biz:`    | general commercial relations lacking upstream, applicable to any company/industry (inherited wholesale, VCR-0001)                                                                                                                                                                                                                                                                                                                                                                                                                                                  | software concepts; vocabulary native to this wiki's own subject matter                   |
| `aiw:`    | the native classes this wiki's own subject matter needs with no upstream/inherited fit — `FoundationModel`, `Benchmark`, `BenchmarkResult`, `LicenseModel` (VCR-0003; see §6b for the portability test each had to pass) — + **all ABox instance data**: pages with their own wiki entry (`aiw:claude-code`), and singular named things belonging to this wiki (its `LicenseModel` enum members, individual `BenchmarkResult` measurements, etc.) | any *new* class that would still make sense as generic vocabulary if handed to an unrelated wiki about a different subject — route it to `swe:`/`biz:`/upstream instead. See §6b for the test. |

## 6a. Classifying a term when the module isn't obvious

Two recurring judgment calls cause most misclassification. Check both before assigning a module.

**Is this a genuine external/upstream concept, or this wiki's own design choice?** `biz:` and `swe:` are for concepts any company/team would recognize (`Customer`, `Transaction`, `Discount`, `DeploymentModel`, `PaymentType`) — generic enough that another product's data could reuse the class verbatim, even if every current instance happens to be this wiki's own. If the concept only exists because of a choice *this wiki* made about how its own content is organized — not a portable classification shape — it is not `biz:`/`swe:` vocabulary and belongs in `aiw:` instead (subject to the portability test in §6b). Do not let "this happens to be about AI/software" pull a wiki-specific concept into `swe:`; and do not let "no other wiki has this instance yet" pull a genuinely portable shape into `aiw:` — see the "common trap" callout in §6b.

**Before minting anything, check `schema.org` and the inherited `swe:`/`biz:` catalog first.** Most of what looks like it needs a new term is already covered: `schema.org`'s `SoftwareApplication` family (providers, `softwareVersion`, `applicationCategory`) or the inherited `swe:` infrastructure vocabulary (APIs, datastores, deployment environments, integration/hosting relations — VCR-0001). `aiw:FoundationModel`/`Benchmark`/`BenchmarkResult`/`LicenseModel` (VCR-0003) are the confirmed misses that remained *after* that check — each has a research note in VCR-0003 showing rungs 1–2 were exhausted first. A new term that skips straight to a native class without that check is a bigger miss than a generic one, precisely because the upstream/inherited fit is usually sitting right there.

**Where does an enum-member *individual*'s IRI live?** Two different kinds of individual get confused:
- An **enum-member value** — one of a closed set defined by a Class (e.g. `open-source`/`open-weights`/`closed-source` under `aiw:LicenseModel`) — is a reusable classification value, not a one-off fact. Its IRI lives in **that class's own module namespace** — here, `aiw:open-source` etc., since `aiw:` is both the class-owning module and this wiki's ABox namespace (unlike the source repo, which split a vertical vocabulary module from its ABox-only `muscle:`; this deployment has no such split, so the distinction is less consequential here but the underlying test still matters whenever an enum is defined in `swe:`/`biz:` instead). (Precedent for the inherited modules: `biz:commercial-banking`, `biz:insurance` — confirmed entries already do this.)
- A **singular, one-of-a-kind individual** that names a specific thing belonging to this wiki (a page with its own entry, like `aiw:claude-code`) is not a repeatable classification value. Its IRI lives in **`aiw:`**, per the slug rule ("instance IRIs live in the `aiw:` data namespace").

If in doubt: would a second, unrelated instance of this concept exist somewhere else in the data (another system's "open-source" license, another product's "admin" role)? If yes, it's an enum member → module namespace. If it only ever refers to this one specific thing, it's a singular individual → `aiw:`.

**`org:Role` individuals, if this wiki ever asserts them:** the source repo's precedent (its VCR-0020) is worth carrying forward as a test, even though no VCR here has needed it yet: `org:Role` can describe two genuinely different kinds of thing that route to different modules — a **product-configuration role** (an access-permission level defined by one specific product's own permission model) stays in that product's native module (here, `aiw:`, the same way the source repo kept its permission roles in `muscle:`); a **generic corporate-governance/business role** (director, CEO, manager — meaningful independent of any one product) is a cross-industry `biz:` enum member, same as any other `biz:` enum. Test: does the role's *meaning* come from a specific product's access-control design (not portable without the product) or from generic corporate practice (portable to any company)? Apply this the moment such a role is ingested; do not default it to `biz:` just because that's the module reached for when nothing else obviously fits.

## 6b. The portability test for `aiw:` — when does a *class* actually belong there?

`aiw:` holds four native classes — `FoundationModel`, `Benchmark`, `BenchmarkResult`, `LicenseModel` — and that set isn't an arbitrary starting point; each had to pass a real test, inherited from the source repo's own `muscle:PricingStrategy` precedent (its VCR 0002), that every future candidate must pass too:

> **The test:** delete this wiki's own content from the graph entirely. Does the class still make complete sense, unchanged, as something a wiki about a completely different subject could adopt wholesale? **If yes**, it is portable vocabulary — route it to `swe:`/`biz:`/upstream, no matter how central it is to this wiki's subject matter or how wiki-specific its *instances* are. **If no** — the class's definition is inseparable from this wiki's own subject matter, not just flavored by it — it belongs in `aiw:`.

This is why `FoundationModel`/`Benchmark`/`BenchmarkResult`/`LicenseModel` passed (VCR-0003): a benchmark result's shape — a score, a unit, a date, a link to the exact benchmark and the exact system measured — *is* the specific AI-evaluation mechanic this wiki tracks; a wiki about, say, agricultural equipment has no use for the class at all, portable framing or not. Contrast with `swe:DeploymentModel`/`biz:PaymentType`/`biz:ProgramType` (inherited, VCR-0001): even though every current instance in this deployment's data may end up describing this wiki's own tool pages, the *class* — "is this deployed cloud or on-device," "is this offering fixed-price or usage-based" — is a generic SaaS/product-configuration shape. Any other product catalog could reuse the class verbatim. That makes it portable vocabulary (`biz:`/`swe:`), even though every current instance happens to be this wiki's.

**Common trap:** "this is central to what this wiki covers" or "no other wiki has this exact instance yet" are *not* the test — `ProgramType`, `DeploymentModel`, `PaymentType` are all just as central to this wiki's tool pages and just as exclusively instantiated here today, yet they pass the portability test (their *shape* is generic) and correctly live in `biz:`/`swe:`. Only ask: is the class's *definition itself* — not its current instances — inseparable from this wiki's specific subject matter? That is a high bar, deliberately — it's why only four classes have cleared it so far.

## 6c. OWL enum class vs. `skos:Concept` — which one for a "kind of X"?

A recurring ambiguity: the source states something that reads as a controlled vocabulary — is it a new OWL class with `owl:oneOf` individuals, or a `skos:Concept` with `skos:narrower` children? Test:

- **Does the source state a closed, exhaustive set with a cardinality rule** — "every X is exactly one of A, B, or C"? → **OWL enum class** (`owl:oneOf`) in the vocabulary module (`biz:`/`swe:`/`aiw:`), per Rule 9/10 (CLAUDE.md/AGENTS.md) — this is what makes the constraint machine-checkable via SHACL. Examples already in the graph: `PaymentType`, `DeploymentModel`, `ProgramType` (inherited `biz:`/`swe:` enums, VCR-0001), `aiw:LicenseModel` (VCR-0003).
- **Is it an open-ended subject-matter tag** — an industry, a topic, something a `schema:knowsAbout`/`schema:about` points at, with no fixed membership or cardinality rule? → **`skos:Concept`** in `aiw:` (if genuinely native to this wiki per §6b) or the vocabulary module's namespace (if reusable — e.g. `biz:commercial-banking`). See `system/authoring-guides/skos-concept.md`. This is also the pattern VCR-0002 used for `wiki/_schema`'s domains/subcategories/tags: open-ended, page-carries-zero-to-many vocabularies modeled as `aiw:` `skos:Concept` instances rather than closed OWL enums.

Full checklist: `system/authoring-guides/term-minting.md`.

## 7. Scope discipline for `swe:`

`swe:` covers software engineering, **but grows by demand, not by anticipation.** Architecture/integration terms are admitted now (VCR 0001) because the base content needs them. Engineering-process terms (`Requirement`, `Build`, `Stakeholder`, dev `Activity`) are **deferred** — they enter only when real engineering content is ingested, each via its own VCR. We do not pre-build a speculative process ontology.

Software *packaging* (licenses, dependencies, supply chain — SPDX/CycloneDX) is permanently out of scope: this wiki ships no distributable artifacts of its own. (Note the distinct, in-scope concept `aiw:LicenseModel`, VCR-0003 — how a *third-party* AI system's weights/source are released to the public. That is subject-matter this wiki reports on, not packaging metadata about this wiki's own software.)

## 8. VCR lifecycle

`Proposed` → `Under review` (research + this policy) → `Approved` (terms defined, IRIs registered) → `Implemented` (written to `ontology/*.ttl`, shapes added, catalog updated, rebuild passes) → `Closed`. Each state is recorded in the VCR file. A VCR is the permanent record of *why* a term exists.

## 9. VCR table conventions — an IRI column states the current recommendation, never a superseded one

A human reviewing a VCR does a **fast pass**: scan the IRI-shaped column (`Proposed native IRI`, `IRI`, etc.) row by row and check whether each one makes sense. That fast pass is only possible if the column is trustworthy — it must show what is actually being recommended *as of the current draft*, never a stale ask that research has already rejected.

- **If review finds an upstream fit, a duplicate, or a module correction, update the IRI cell itself (or move the row out of the table).** Do not leave the original, now-wrong proposal sitting in the IRI column with the correction relegated to a prose note elsewhere in the row. A reviewer scanning only that column will read the stale IRI as still live.
- **A term whose disposition is settled — reuse upstream, fold into an existing term, reject as duplicate — does not belong in a REVIEW/candidate table at all.** Move it to the confirmed-reuse/fold bucket as a single resolved sentence (`term → schema:X, no native IRI needed`). Reserve REVIEW tables for terms whose disposition is genuinely still open.
- **Never let a table column double as a changelog.** If a draft's proposal changes during the same review pass, the reader should not have to diff drafts to know which IRI is current — the document as published shows only the resolution.

**What this looks like when it goes wrong:** a draft flags a candidate term for upstream reuse during review, but leaves the original native IRI (e.g. `aiw:SomeConcept`) sitting in the "Proposed native IRI" column of a REVIEW table, with the actual recommendation ("reuse `schema:X`, don't mint") buried in a Note cell instead. A fast scan of the IRI column alone then reads as if the native term is still live. Fix it by removing the row from the REVIEW table entirely and writing it into the confirmed-reuse bucket as a resolved disposition (`term → schema:X, no native IRI needed`).
