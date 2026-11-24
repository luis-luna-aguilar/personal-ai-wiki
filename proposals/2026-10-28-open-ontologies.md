---
type: proposal
source: raw/repos/fabio-rovai-open-ontologies.md
status: pending
created: 2026-10-28
---

# Proposal: Open Ontologies (fabio-rovai GitHub repo)

## Summary

### In short

A change to a production ontology should be planned and proved, not just diffed: Open Ontologies shows one correct-looking added line that touched zero triples yet created 901 new inferences, and it hands reviewers a certificate a separate Lean 4 checker can re-verify offline, refusing any forged conclusion. The proposal creates a tool page, lists it under Knowledge platforms on State of Agents, and adds it to Ontologies as agent guardrails as the first change-control tooling for ontologies. The term "ontology" is already mapped on the Knowledge architectures hub, so the hub is untouched. Reason to hesitate: the README carries no release date, so 28 October stands in.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

Open Ontologies is an MIT-licensed engine written in Rust by Fabio Rovai, who also sells a hosted version through his company, Tesseract Semantics. An ontology here is a formal description of a domain's classes and rules, written in Semantic Web standards such as OWL and RDFS, from which a reasoner derives new facts. The README's pitch is that changing such a file in production is like changing infrastructure, so it borrows Terraform's loop: plan a change, see its consequences, apply it, watch for drift, and roll back. Its headline example is a one-line change that a text diff calls harmless (no classes added or removed, nothing affected) but which gave a new type to every individual already using a property, 901 new consequences in all.

The second idea is proof. Each reasoning run writes a certificate as two small tab-separated files: what was asserted, and each derived step with its rule and premises. A checker written in Lean 4, a proof language, shares no code with the engine and has a proved soundness theorem; an auditor can run it months later with no network and no copy of the engine. If anyone edits a conclusion, it exits with an error and names the broken rule. When the user supplied their own rules, the verdict word changes, so the certificate shows they were assumptions. The engine also validates SHACL shapes, checks crosswalks between vocabularies, measures whether a retrieval slice for RAG still supports each claim, and runs as an MCP server for Claude Code, Claude Desktop and Cursor.

The README is candid about limits: it is not an editor, answers that something is unsatisfiable carry no guarantee, and storage defaults to memory, so a careless run certifies nothing.

### What changes

The wiki's page on ontologies as agent guardrails treats ontologies as a rule layer that checks agents, and names upkeep as the unsolved problem; its one working example is Utopia.

- New page `wiki/tools/open-ontologies.md` (subcategory `knowledge-platform`), placed on the hub's ontology row.
- **Ontologies as agent guardrails** gains one status bullet presenting Open Ontologies as change control for the ontology itself, a source, and a Recent-changes entry. Page date moves from 9 September to 28 October.
- **State of Agents** gains a line under Knowledge platforms and one Recent-changes entry; the list is at its cap of 10, so the oldest entry (Claude Cowork beta, 8 July) spills to history. Page date moves to 28 October.
- The index gains the tool, and one new source page records the repo.

### What to weigh

The README has no publication or release date, so 28 October, the fetch date, stands in throughout; the linked arXiv paper dates the project's work to May 2026 but not this README. Placement is a judgment: I filed it as a knowledge platform on the ontology row rather than as a verification tool, because its subject is the ontology file. The hub already maps "ontology" to that row, so no mapping row was needed and the hub, already at 111% of its length ceiling, is left alone.

## Intended changes

- [ ] **Create** `wiki/tools/open-ontologies.md` — new tool page, subcategory `knowledge-platform`
- [ ] **Update** `wiki/concepts/ontology-agent-guardrails.md` — one new Current-status bullet, heading and `as_of` to 2026-10-28, source id appended to frontmatter and `## Sources`, adds one Recent-changes entry dated 2026-10-28 (list is at 3, no spill)
- [ ] **Update** `wiki/state-of/agents.md` — one new line under `### Knowledge platforms`, `as_of` to 2026-10-28, source id appended, adds one Recent-changes entry dated 2026-10-28 and spills the oldest entry (cap 10)
- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — the oldest Recent-changes entry at apply time (expected: 2026-07-08 Claude Cowork beta)
- [ ] **Update** `wiki/index.md` — add the tool line after `tools/openwiki`; tools count 101 → 102, total 247 → 248
- [ ] **Create** `wiki/sources/repos/fabio-rovai-open-ontologies-2026-10-28.md` — source summary

## Page drafts

### wiki/tools/open-ontologies.md (new)

```
---
title: Open Ontologies
type: tool
domains: [agents]
subcategory: knowledge-platform
tags: [open-source, knowledge-cluster]
as_of: 2026-10-28
sources: [fabio-rovai-open-ontologies-2026-10-28]
---

# Open Ontologies

Open Ontologies is an open-source (MIT) engine, written in Rust and shipped as one binary, for changing a production ontology safely. It borrows Terraform's loop (plan, apply, watch for drift, roll back), but the plan is semantic: it reports what a change makes the ontology *entail*, not which lines moved. Its second job is proof: each reasoning run writes a certificate that a separate, formally verified Lean 4 checker re-checks without the engine. In the [Knowledge architectures](../concepts/knowledge-architectures.md) matrix it sits on the ontology row. Fabio Rovai maintains it; Tesseract Semantics sells a hosted version.

## Current status (as of 2026-10-28)
- Plan reports added and removed classes, blast radius, risk score, locked IRIs, and whether a change adds consequences over existing names. The README's example: one added `rdfs:domain` line, zero triples affected, 901 new inferences
- A certificate is two tab-separated files (assertions; each derived step with rule and premises). The Lean checker shares no code with the engine, refuses a forged conclusion with exit 1 and names the rule, and gives a different verdict when the rules were user-supplied
- Also: OWL/RDFS reasoning, SHACL validation, satisfiability with checked finite models, crosswalk checks that downgrade unsupported `exactMatch` mappings, and per-claim checks that a RAG retrieval slice still supports its answer
- Runs as an MCP server for Claude Code, Claude Desktop and Cursor; loads CSV, JSON, XML, XLSX, Parquet, PostgreSQL and DuckDB into RDF

## Weaknesses / caveats
- Not an ontology editor; the README points to Protégé for authoring
- Unsatisfiability answers carry no guarantee, and the tool says so
- Storage is in-memory by default, so a `load` then `reason` without persistent mode certifies nothing; the warning is easy to miss
- The pure-Python second engine runs the same algorithm as the Rust one, so their agreement is weak evidence against a shared misreading of a rule; the Lean checker is the independent leg
- Published binaries omit eight feature-gated tools (embeddings, plugins, SQL backends)

## Recent changes
- [2026-10-28] Page created from the project's GitHub README (no dated release in the source).

## Related
- [Ontologies as agent guardrails](../concepts/ontology-agent-guardrails.md) — the concept this tool serves, applied to change control of the ontology itself
- [Utopia](utopia.md) — the other ontology-row engine tracked; Utopia governs facts extracted from documents, Open Ontologies governs changes to the rules
- [Knowledge architectures](../concepts/knowledge-architectures.md) — the hub that places this tool on the ontology row

## Sources
- [fabio-rovai/open-ontologies (GitHub)](../sources/repos/fabio-rovai-open-ontologies-2026-10-28.md)
```

### wiki/concepts/ontology-agent-guardrails.md (updated)

Frontmatter fields changed:

```
as_of: 2026-10-28
sources: [ontologies-agentic-systems-2026-07-30, deeplethe-utopia-2026-09-09, fabio-rovai-open-ontologies-2026-10-28]
```

Heading change: `## Current status (as of 2026-09-09)` → `## Current status (as of 2026-10-28)`.

New bullet appended to the end of `## Current status`:

```
- [Open Ontologies](../tools/open-ontologies.md) (open-source, MIT) brings change control to the ontology itself: it plans a change like Terraform, reports the blast radius and the new consequences a text diff hides (one added line, zero triples affected, 901 new inferences in its README example), and writes a derivation certificate that a separate Lean 4 checker re-verifies offline, refusing forged conclusions. It does not reduce the upkeep burden below, but it makes each upkeep change reviewable and reversible.
```

`## Recent changes` — adds one entry at the top:

```
- [2026-10-28] Added Open Ontologies as change-control tooling for the ontology itself: semantic plan with blast radius, rollback, and Lean-checked derivation certificates.
```

`## Sources` — appends:

```
- [fabio-rovai/open-ontologies (GitHub)](../sources/repos/fabio-rovai-open-ontologies-2026-10-28.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter: `as_of: 2026-10-28`; append `fabio-rovai-open-ontologies-2026-10-28` to the end of `sources:`.

`### Knowledge platforms` — new line appended after the Helix Foundry line:

```
- [Open Ontologies](../tools/open-ontologies.md) — Tesseract Semantics; open-source (MIT) change control for production ontologies: semantic plan with blast radius, apply, rollback, and derivation certificates a Lean 4 checker re-verifies; MCP server *(as of 2026-10-28)*
```

`## Recent changes` — adds one entry at the top; removes the oldest entry (spilled below):

```
- [2026-10-28] Added [Open Ontologies](../tools/open-ontologies.md) to Knowledge platforms: open-source plan/apply/rollback for production ontologies, with derivation certificates an auditor can re-check offline.
```

### wiki/history/state-of/agents.md (updated)

Appended at the end of the file (the actual spill is whatever entry is oldest at apply time):

```

## Archived from current page on 2026-10-28

- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/index.md (updated)

New line after `tools/openwiki`:

```
- [tools/open-ontologies](tools/open-ontologies.md) — open-source (MIT) change control for production ontologies: semantic plan with blast radius, apply, rollback, and Lean-checked derivation certificates; MCP server (subcategory `knowledge-platform`) *(as_of: 2026-10-28)*
```

Page count:

```
- tools: 102
...
**Total content pages: 248.**
```

### wiki/sources/repos/fabio-rovai-open-ontologies-2026-10-28.md (new)

```
---
title: "fabio-rovai/open-ontologies (GitHub)"
type: source
source_type: repo
source_file: raw/repos/fabio-rovai-open-ontologies.md
url: https://github.com/fabio-rovai/open-ontologies
ingested: 2026-10-28
domains: [agents]
---

# fabio-rovai/open-ontologies (GitHub)

README for Open Ontologies, an MIT-licensed Rust engine (one binary, MCP server) for planning, applying and rolling back changes to a production ontology. It reports a semantic blast radius rather than a text diff, and writes derivation certificates that a separate Lean 4 checker with a soundness theorem re-verifies offline, refusing forged conclusions. Maintained by Fabio Rovai; a hosted version is sold by Tesseract Semantics. The README carries no release date; the ingest date is used.

## Influenced pages

- [Open Ontologies](../../tools/open-ontologies.md) — new tool page
- [Ontologies as agent guardrails](../../concepts/ontology-agent-guardrails.md) — change control for the ontology itself as a new status bullet
- [State of Agents](../../state-of/agents.md) — new line under Knowledge platforms

## Key claims extracted

- Terraform-style loop for ontologies: plan, apply, monitor, drift, certify, rollback; plan reports added/removed classes, blast radius, risk score, locked IRIs, conservativity
- Example: adding `ex:hasParent rdfs:domain ex:Person` affects 0 triples and changes no classes, yet adds 901 consequences under the OWL RL rule table (0.04s)
- Certificates are two TSV files (asserted, derivations); a core Lean 4 checker (`oo-cert`, theorem `OOCert.certificate_sound`) shares no code with the engine and exits 1 on a forged line, naming the rule
- User-supplied rules (SWRL, RIF Core, Horn table) yield the verdict `entailed_under_supplied_rules` instead of `entailed`
- Figure on ies-core.ttl: 426 asserted, 259 certified by one certificate, 1 forged line rejected
- HQDM audit: the RDFS file has 23 undeclared class terms and 12 ranges naming a relation; the OWL file has 39 unsatisfiable classes, the same 39 HermiT reports
- No guarantee on unsatisfiability answers, stated by the tool
- Also: SHACL validation, finite-model satisfiability, SSSOM crosswalk certification and `crosswalk-probe`, entailment preservation for RAG retrieval slices, locality-module extraction (pizza ontology: 238 of 1,345 axioms, zero conclusions lost)
- MCP server for Claude Code, Claude Desktop, Cursor, Windsurf, Zed, VS Code; loads CSV, JSON, XML, YAML, XLSX, Parquet, PostgreSQL, DuckDB into RDF
- Caveats in the README: not an editor (use Protégé); in-memory storage by default; Python and Rust engines are not independent; published binaries omit eight feature-gated tools; a certificate digest binds to bytes, not world state
- Stack: Rust 2024, Oxigraph 0.5, rmcp, SQLite, Lean 4 v4.33.1 (no Mathlib); papers arXiv:2605.09184 and arXiv:2605.09168 (CIVeX)
```

## Schema / vocabulary additions

None.

## Open questions

- The Knowledge architectures hub lists tracked examples on its ontology row (currently Neo4j's three-layer stack and Utopia). Adding Open Ontologies there is a few words but would add to a page already at 111% of its 1,200-word ceiling. I left the hub untouched. Should I add the example anyway, and if so, should the hub be split (for example, moving the term map to its own page) as a separate refactor?
