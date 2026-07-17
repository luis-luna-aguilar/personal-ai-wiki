# Authoring Guide — Dual-Typing an Enum Member as `skos:Concept`

Read this before linking a page's prose to one specific value of a closed `owl:oneOf` enumeration (an `aiw:LicenseModel` or `swe:DeploymentModel` member) via `schema:knowsAbout`, `schema:about`, or `skos:related`. `term-minting.md` and `vocabulary-policy.md` §6c already tell you when a *new* controlled-vocabulary value is an OWL enum class vs. a `skos:Concept` — this guide covers the narrower, recurring case where **both apply to the same individual at once**, which the admission ladder alone doesn't resolve.

---

## The pattern

An enum member that a page also wants to treat as a linkable topic (something a concept page can be `skos:narrower` of, or something a `schema:about`/`skos:related` triple can point at) is **dual-typed**: it keeps its enum membership *and* gains `skos:Concept` + a normal SKOS annotation pair.

```turtle
aiw:open-weights a skos:Concept, aiw:LicenseModel ;
    skos:prefLabel "Open Weights"@en ;
    skos:definition "A license model where a foundation model's trained weights are published for download and local use, but the training code, data, or full commercial rights may remain proprietary — distinct from open-source (source and weights both open) and closed-source (neither published)."@en ;
    skos:broader aiw:model-licensing .
```

- [ ] Keep the enum type (`aiw:LicenseModel`, `swe:DeploymentModel`, …) — dual-typing **adds** `skos:Concept`, it never replaces the enum type. The `owl:oneOf` closure and any SHACL `sh:in` shape targeting the enum class still apply unchanged.
- [ ] Add `skos:prefLabel`/`skos:definition`, following `skos-concept.md`'s normal annotation rules.
- [ ] If the concept genuinely has a broader topic (e.g. a license model is `skos:broader` of a page-level "Model Licensing" concept), assert it — same symmetry rule as `skos-concept.md` (`skos:narrower` on the broader side).
- [ ] **This is not a license to dual-type every enum member.** Only do this when a real `schema:knowsAbout`/`schema:about`/`skos:related`/`skos:narrower` fact in the source actually needs to target the individual as a topic. An enum member that's only ever used as the object of its own typed property (e.g. `aiw:hasLicenseModel aiw:open-weights` with no concept-linking fact anywhere) does not need `skos:Concept` at all — see `term-minting.md`'s enum-vs-concept test for the default (non-dual-typed) case.

**Precedent from the source project this guide was ported from** (`muscle:fixed-cpp`/`muscle:prioritize-savings`/`muscle:value-sharing`, each `a skos:Concept, biz:PricingModality` with `skos:broader muscle:bank-loyalty-optimization`) shows the same dual-typing shape applied to a pricing-modality enum instead of a license-model enum — read that project's `wiki/concepts/glossary.ttl` for a second worked example of the identical pattern if this guide is ambiguous on a specific point. In this deployment, `aiw:LicenseModel`'s three members (`open-source`, `open-weights`, `closed-source`, VCR-0003) are the canonical target for dual-typing once a page actually needs one as a linkable topic.

---

## Before minting anything, check for reuse

- [ ] **Does the enum member already exist?** Grep `lexicon-map.yaml` and the relevant `knowledge-graph/ontology/*.ttl` module for the value name before minting a fresh individual — enum members are catalogued centrally (e.g. `aiw:LicenseModel`'s `owl:oneOf` list in `aiw.ttl`), so a "new" license model or deployment model almost certainly already exists.
- [ ] **Is `skos:Concept` actually earned here, or would a bare enum-typed reference already say what the source means?** If the source only ever states "this model is open-weights" (a property assertion), don't add `skos:Concept` — that's the ordinary, non-dual-typed enum-member case, already fully covered without this guide.

---

## Naming convention

- [ ] Reuse the enum member's existing IRI exactly — dual-typing never changes or duplicates the IRI (IRI permanence, `vocabulary-policy.md` §5). Add the `skos:Concept` type and annotations to the same individual, in whichever sidecar first needs it as a topic (typically `wiki/concepts/*.ttl` if it's a cross-page reusable topic).

## Before finishing

- [ ] Confirmed the individual keeps its original enum type alongside the new `skos:Concept` type.
- [ ] Confirmed a real `schema:knowsAbout`/`schema:about`/`skos:related`/`skos:narrower` fact justifies the dual-typing — not added speculatively.
- [ ] Confirmed the IRI is unchanged from its existing enum-member declaration.
