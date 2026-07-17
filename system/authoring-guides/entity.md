# Authoring Guide — Entity Sidecars (organizations: AI labs, providers, parent companies)

Read this before writing any sidecar for an `org:FormalOrganization` individual — an AI lab or company such as Anthropic, OpenAI, Google DeepMind, or xAI. This wiki has no dedicated `wiki/orgs/` page type (unlike the source project's `wiki/entities/*.md` banks/companies, which each had their own page): here, an organization is usually a lightweight individual referenced from a `wiki/tools/*.md` (`schema:SoftwareApplication`) or `wiki/models/*.md` (`aiw:FoundationModel`) page's `schema:provider`/`biz:develops` triple, not a page of its own. Work through every checkbox; paste the completed list into the proposal's **Sidecar Authoring Checklist** section.

---

## Required triples

- [ ] `a org:FormalOrganization` — the class itself needs no narrowing; there is no FIBO-style "AI lab" subtype, and inventing one would fail `term-minting.md`'s Step 2 (it would just be an instance, not a new class).
- [ ] `rdfs:label "..."@en` — at least one English label (`"Anthropic"@en`).
- [ ] `rdfs:comment "..."@en` — one English gloss (what the org *is*; not a prose dump) — e.g. `"AI safety and research company; develops the Claude model family and Claude Code."@en`.
- [ ] If the org has aliases (a former name, a common short form), add `skos:altLabel "..."@en` for each, AND list them in the markdown frontmatter `aliases:` array of whichever page first introduces the org AND mention them in that page's first paragraph.

**Worked example:** `wiki/tools/claude-code.md` asserts `schema:provider aiw:anthropic` (see `software-application.md`). The org individual itself carries:

```turtle
aiw:anthropic a org:FormalOrganization ;
    rdfs:label "Anthropic"@en ;
    rdfs:comment "AI safety and research company based in San Francisco; develops the Claude model family, Claude Code, and the Claude API."@en ;
    schema:location dbp:San_Francisco ;
    schema:foundingDate "2021"^^xsd:gYear .
```

---

## Location (headquarters)

- [ ] `schema:location dbp:<CityOrCountry>` — use the DBpedia IRI (e.g. `dbp:San_Francisco`, `dbp:United_Kingdom` for a UK-based lab).
- [ ] Do **not** declare `dbp:<Place> a schema:Place` in this sidecar. Place typing lives in a shared seed file, the same way the inherited `knowledge-graph/ontology/seeds/countries.ttl` handles country typing — add a new entry there if the place does not already exist, rather than typing it inline per-org.

---

## Founding date

- [ ] If a founding year is known, add `schema:foundingDate "YYYY"^^xsd:gYear`.
- [ ] Ensure `@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .` is declared.
- [ ] Never use a plain string (`"2021"`) — the datatype-domain discipline (Rule 10) requires the typed `xsd:gYear` literal so a shape can validate it.

---

## Domain knowledge (schema:knowsAbout)

- [ ] All targets of `schema:knowsAbout` must be `skos:Concept` instances — check `lexicon-map.yaml` first: several cross-industry topic concepts (`biz:retail-banking`, `biz:insurance`, etc., inherited from the source project's VCR-0001) or this wiki's own `_schema`-derived concepts (`aiw:domain-coding`, `aiw:domain-agents`, VCR-0002) may already cover it. **Reuse those directly** — do not mint a parallel `aiw:<same-concept>` individual (one concept, one IRI).
- [ ] `biz:`/`swe:` namespaces otherwise hold predicates and classes, not concept instances — but a `skos:Concept` individual that happens to be reusable/cross-industry is the one exception, catalogued in the vocabulary module's own namespace per `vocabulary-policy.md` §6a. When in doubt, grep `lexicon-map.yaml` for the concept before minting.
- [ ] If the concept you need does not yet exist anywhere in `lexicon-map.yaml` or the `_schema` concept schemes, create it as `aiw:<slug> a skos:Concept` following the `skos-concept.md` authoring guide.

---

## Organization predicates

- [ ] `org:unitOf aiw:<parent>` — if the org is a subsidiary or division of a larger company (e.g. a lab acquired by, or operating as a unit of, a larger tech company).
- [ ] `org:linkedTo aiw:<partner>` — for peer partnerships (e.g. a model lab's infrastructure/compute partnership with a cloud provider) — symmetric: add the reverse triple on the partner's own individual too. `aiw:OrgLinkedToSymmetryShape` (inherited pattern) will flag missing reverse triples.
- [ ] `biz:develops aiw:<tool-or-model>` on the org's individual is the inverse direction of the tool/model page's own `schema:provider`/`prov:wasAttributedTo` — assert it on the org side only when a page needs to enumerate everything an org makes from the org's own individual (uncommon; usually the tool/model page's `schema:provider` triple alone is sufficient and this reverse assertion is skipped to avoid duplication).

---

## schema:about vs schema:knowsAbout

- [ ] `schema:knowsAbout` goes on **organizations** pointing to subject-matter concepts (e.g. `aiw:anthropic schema:knowsAbout aiw:domain-safety`).
- [ ] `schema:about` goes on **creative works and products** — `schema:SoftwareApplication` (tools), `aiw:FoundationModel` (models), source-summary records — pointing to concepts.
- [ ] Never write `schema:about` on an `org:FormalOrganization`.

---

## Before finishing

- [ ] Run `python3 system/scripts/verify_links.py` — confirms no broken markdown links.
- [ ] Run `knowledge-graph/scripts/validate-page.sh` on the sidecar — confirms shape conformance.
- [ ] Grep for any undefined IRI prefixes: `biz:<noun>`, `swe:<noun>` — these are bugs.
