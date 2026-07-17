# Ingestion Proposal: [Source Name]

**Source(s):** `[Path to raw source(s)]`
**Assigned Pipeline:** `[e.g., wiki/models/ — Foundation Model page]`

---

## Contradictions & Open Questions
*Explicitly highlight any conflicts between the new source and existing wiki content. Present both the existing claim and the new claim so the user can determine the source of truth.*
- `[Describe contradiction here or write "None identified."]`

---

## Terminology Reconciliation
*Map every concept in the source against the vocabulary catalog (`knowledge-graph/ontology/lexicon-map.yaml`) before proposing any new term.*

| Source concept | Action | Term / IRI |
|---|---|---|
| `[concept]` | Reuse existing / Normalize to / Upstream reuse / VCR opened | `[IRI or VCR ref]` |

---

## Schema & Logical Assertion Harvesting
*Per Rule 9: list every schema or logical assertion (validation rules, axioms) the source states or implies (cardinality, mandatory fields, enumerations, exclusivity, uniqueness, conditional dependencies, value ranges). For each, state its destination (SHACL shape or OWL axiom) and whether a VCR is needed.*

- `[Assertion found — or write "No enforceable schema/logical assertions identified."]`

---

## Datatype Domain Inventory
*Per Rule 10: list every datatype-valued field. For each: (a) datatype, (b) unit/dimension and how it will be modelled, (c) admissible range and the validating shape/axiom.*

| Field | Datatype | Unit / model | Range | Shape / axiom |
|---|---|---|---|---|
| `[field]` | `xsd:…` | `[reified individual / upstream term]` | `[bounds or enum]` | `[shape IRI or "pending VCR"]` |

*Write "No datatype-valued fields in source." if none apply.*

---

## Sidecar Authoring Checklist
*For each entity type you are creating or modifying, read the corresponding guide in `system/authoring-guides/` and paste the completed checklist here. This step is mandatory — do not skip it even if the type seems straightforward.*

| Type being authored | Guide consulted | All items checked? |
|---|---|---|
| `skos:Concept` | [`skos-concept.md`](../authoring-guides/skos-concept.md) | [ ] |
| `schema:SoftwareApplication` | [`software-application.md`](../authoring-guides/software-application.md) | [ ] |
| `aiw:FoundationModel` | *(guide not yet written — note gaps found)* | [ ] |

*For types with no guide yet: list any non-obvious authoring decisions you made so the lesson can be added to a future guide.*

---

## Assertion Consistency Check
*Run `knowledge-graph/scripts/validate-ingestion.sh <candidate>.ttl` and paste the result here. A clean run is required before approval.*

```
[Paste validator output here]
```

---

## Proposed Actions

**Approval must be against the near-final product, not a plan to produce it.** For each file below, include the **complete draft content** — never a bullet-point summary of what it will contain. A reviewer must be able to read this section and know what the wiki will say, without trusting a later, unseen extraction step to fill the gap faithfully. A one-line "Summary of Change" is a navigation aid on top of the full draft, not a replacement for it. For an `Update` action, show the complete new/changed sections in full, with enough surrounding unchanged content to see exactly where they land.

**The sidecar draft is `.ace`, not `.ttl`.** This repo's pipeline is `MD → ACE → TTL` (`AGENTS.md` §3) — `.ace` is the actual human-authored/reviewed artifact (controlled English, validated by APE); `.ttl` is a **mechanically compiled** build product of the `.ace`, never hand-authored as final content. So the sidecar you draft for review is the `.ace` file, written per `system/authoring-guides/controlled-english.md`. Two exceptions, both matching this repo's documented sidecar-annotation convention (see `knowledge-graph/governance/sync-model.md`'s "hand-authored blank-node enrichment" exemption): (a) nested/reified structured values that ACE's flat SVO grammar can't express (`schema:MonetaryAmount`, `schema:PropertyValue`, `schema:PostalAddress` blank nodes) are drafted directly as a small **hand-authored `.ttl` enrichment** block, clearly labeled "no ACE form"; (b) if the `.ace` draft uses a term not yet in `lexicon-map.yaml`/`aiw-lexicon.ulex` (i.e. it's pending a VCR), say so — it can't be run through `validate-ace.sh` (APE) until the VCR is approved and synced, same as it can't compile to `.ttl` until then.

If a file's full draft is genuinely too large to review in one pass even after applying `system/authoring-guides/large-source-ingestion.md`'s chunking, split it into a smaller chunk — never compress the draft to fit. Run the Assertion Consistency Check (above) against these drafts before presenting them, not after approval (a VCR-blocked draft can only be run once the VCR is synced — note that explicitly rather than skipping the check silently).

- To approve a file, check its box: `[x] Approve`
- To request changes, leave a note in the `Feedback` section.

### 1. `[File Path 1]`
- **Action:** `[Create | Update]`
- **Summary of Change:** `[One-sentence description, for navigation only]`
- **Full Draft — Markdown:**
  ```markdown
  [The complete page content as it would be committed: frontmatter + full body prose, every table reproduced in full. Not a summary.]
  ```
- **Full Draft — Sidecar (`.ace`):**
  ```
  [The complete controlled-English sentences for this file's sidecar, per controlled-english.md. Not a summary. Note any sentence blocked pending a VCR.]
  ```
- **Hand-authored `.ttl` enrichment (no ACE form), if any:**
  ```turtle
  [Only the nested/reified structured values ACE can't express — e.g. a MonetaryAmount or PostalAddress blank node. Omit this block entirely if the page has none.]
  ```
- [ ] **Approve**
- **Feedback:** 

### 2. `[File Path 2]`
- **Action:** `[Create | Update]`
- **Summary of Change:** `[One-sentence description, for navigation only]`
- **Full Draft — Markdown:**
  ```markdown
  [Complete content, as above.]
  ```
- **Full Draft — Sidecar (`.ace`):**
  ```
  [Complete controlled-English sentences, as above.]
  ```
- **Hand-authored `.ttl` enrichment (no ACE form), if any:**
  ```turtle
  [As above; omit if none.]
  ```
- [ ] **Approve**
- **Feedback:** 
