# Authoring Guide — `skos:Concept` Sidecars

Read this before writing any sidecar that creates or modifies a `skos:Concept` instance. Work through every checkbox; paste the completed list into the proposal's **Sidecar Authoring Checklist** section.

---

## Required triples

- [ ] `a skos:Concept` declared.
- [ ] `skos:prefLabel "..."@en` — exactly one English preferred label.
- [ ] `skos:definition "..."@en` — one English definition (not a paraphrase of the label; a real explanation).

> **Lesson learned (source project, 2026-06-19):** a bare glossary-wide `skos:ConceptScheme` intermediate adds no information and creates maintenance overhead when the namespace itself already does the grouping. In this deployment, `skos:inScheme` **is** used, but only for the three purpose-built schemes from VCR-0002 (`aiw:domain-scheme`, `aiw:subcategory-scheme`, `aiw:tag-scheme` — the `_schema/{domains,subcategories,tags}.md` controlled vocabularies). Don't invent a fourth catch-all scheme for ad-hoc glossary concepts that aren't one of those three; a `skos:Concept` minted for a one-off topic (e.g. a concept page under `wiki/concepts/`) does not need `skos:inScheme` at all.

---

## Relation direction rules

These are the most common source of errors. Get the predicate on the right sidecar.

| Relationship | Wrong | Correct |
|---|---|---|
| A tool/model is about this concept | `this skos:related aiw:claude-code` | `schema:about aiw:this-concept` on the **tool's/model's** sidecar |
| An org's domain covers this concept | `this skos:related aiw:some-org` | `schema:knowsAbout aiw:this-concept` on the **org's** sidecar |
| Two concepts are mutually related | `this skos:related aiw:other` | Same triple on **both** sidecars (see symmetry rule below) |

### Symmetry rule for `skos:related`
`skos:related` is declared `owl:SymmetricProperty` by the SKOS spec. The SHACL validator (`aiw:SkosRelatedSymmetryShape`) will flag any one-sided assertion.

- [ ] For every `this skos:related ?other` you write, confirm that `?other`'s sidecar also asserts `?other skos:related this`. If not, add the reverse triple to that sidecar before closing the proposal.

---

## Hierarchy rules

- [ ] Named enumerations in the source — numbered lists, phrases like "X consists of Y, Z, and W", explicit sets — must be modelled as `skos:narrower` stubs (one `skos:Concept` per item), not compressed into the definition string.
- [ ] Each `skos:narrower` concept also declares `skos:broader` back to the parent (no `skos:inScheme` needed — see lesson above).
- [ ] If the new concept is itself a sub-concept of an existing one, assert `skos:broader` here and `skos:narrower` on the parent's sidecar.

---

## Namespace discipline

> **See `vocabulary-policy.md` §6c:** this file is for **open-ended subject-matter tags** used via `schema:knowsAbout`/`schema:about`/`skos:related` (e.g. "coding" as a domain a tool relates to) — these have no closed membership and no cardinality rule, so they're `skos:Concept` instances, either in `aiw:` (page-local/wiki-specific) or in the inherited `biz:`/`swe:` module namespace (reusable, cross-industry — e.g. `biz:commercial-banking`, `biz:insurance`, carried over from the source project's VCR-0001 inheritance and still valid precedent here).
>
> **This does NOT cover closed enumerations.** If the source states a closed/exhaustive set with a cardinality rule ("every X is exactly one of A, B, or C" — a license model, a deployment model, a score unit, …), that is an **OWL enum class** (`owl:oneOf`) in the vocabulary module (`aiw:`/`biz:`/`swe:`), not a `skos:Concept` hierarchy here — see `system/authoring-guides/term-minting.md` for the decision test. `aiw:LicenseModel` (`open-source`/`open-weights`/`closed-source`, VCR-0003) is exactly this case: a closed 3-member enumeration, so it belongs in `aiw:LicenseModel`, not as a `skos:Concept` hierarchy.
>
> Note the deliberate exception for this deployment's controlled vocabulary: `wiki/_schema/{domains,subcategories,tags}.md` **are** modeled as `skos:Concept` with `skos:inScheme` (VCR-0002), even though `domains`/`subcategory`/`tags` are, individually, closed-ish/growing sets — they were kept as `skos:Concept` rather than OWL enums specifically so new values can be added by an ordinary proposal instead of a full VCR (see VCR-0002's rationale). Don't treat that as license to model every enumeration this way — it's a one-time, explicitly-reasoned exception for the three `_schema` vocabularies only.

- [ ] Any `schema:knowsAbout` or `skos:related` target that represents an **open-ended subject-matter concept** (an industry, a subject area — not a closed enumeration) needs a `skos:Concept` declaration. Use `aiw:<slug>` if the concept is genuinely wiki-specific (per the §6b portability test); use the relevant vocabulary module's namespace (`biz:<slug>`, as `biz:commercial-banking` already does) if it's a reusable, cross-industry tag.
- [ ] Never use `biz:<concept-name>` or `swe:<concept-name>` as an IRI for a **class or property** — those namespaces hold TBox vocabulary. `skos:Concept` *instances* in a vocabulary module's namespace (e.g. `biz:commercial-banking`) are fine and already precedented; check `term-minting.md` if unsure which case you're in.

---

## Frontmatter (markdown side)

- [ ] `related_entities` values use IRI slug form (`"claude-code"`, `"claude-sonnet-5"`) — never display names (`"Claude Code"`, `"Claude Sonnet 5"`).

---

## Before finishing

- [ ] Run `python3 system/scripts/verify_links.py` — confirms no broken markdown links.
- [ ] Run `knowledge-graph/scripts/validate-page.sh` on the sidecar — confirms shape conformance (including `skos:inScheme` and symmetry).
