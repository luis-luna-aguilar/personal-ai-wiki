---
type: proposal
source: raw/repos/deeplethe-utopia.md
status: pending
created: 2026-09-09
---

# Proposal: Utopia (deeplethe/utopia) — open-source enterprise bitemporal knowledge graph

## Summary

### The source

Utopia is an open-source (Apache-2.0) project from DeepLethe, describing itself as an "enterprise world model" — the first open substrate for knowledge engineering that learns passively and governs itself. Its founding idea is a **bitemporal knowledge graph**: every extracted fact carries both when it was true in the world and when the system came to believe it. Correcting a fact never overwrites it — the old version is closed and linked to the new one — so when a decision is reviewed later, the system can reproduce the exact course it took and the grounds it rested on. The project is explicit that it doesn't want to be read as "open-source Palantir"; it frames itself as a different, bottom-up route to enterprise intelligence, built from knowledge governance up to trustworthy decisions and simulation, rather than top-down from an existing data platform. Technically it's deliberately minimal: one Rust binary plus Postgres (full-text search embedded via Tantivy, vectors in pgvector, the job queue is a table), so a company can run it fully air-gapped behind any OpenAI-compatible endpoint — DeepSeek, Qwen, GLM, Ollama, vLLM all work. On top of that it ships a complete web application (system console, graph browser, ontology workbench), broad document/source ingestion (PDF/DOCX/PPTX/XLSX/CSV/Markdown/HTML/plain text, plus scheduled sync from web pages, RSS, GitHub, Jira, Notion, WebDAV, and S3), a built-in agent harness exposed identically over MCP (search documents, walk the graph as of any date, query a mounted database), ontology-driven cold-start (five bundled packs: schema.org, W3C Org, PROV-O, FOAF, IOF Core), forward-chaining derivation from ontology axioms (off by default, and an asserted fact always beats a derived one it contradicts), three-stage reversible entity resolution, dual conflict detection (fact-vs-fact and fact-vs-ontology, with the ontology checked first), an ontology-to-SQL mapper for querying a mounted database alongside documents (Ontology2SQL, with a submitted BIRD Mini-Dev result), and an append-only decision ledger that outlives the objects it records. It's still v0.1 — schema migrations only roll forward — with an "execution gate" (checking agent tool calls against ontology rules before they run) and full decision-replay named as roadmap items, not shipped features.

### What changes

The wiki already tracks the idea of using a formal ontology as a machine-checkable rule layer for agent reasoning, but so far only from a single conference-talk recap with no working implementation to point to. Since the 9 September terminology reorganization there is also a `knowledge-platform` tool subcategory and a [Knowledge architectures](../wiki/concepts/knowledge-architectures.md) hub that pins "world model" to its physical or video-prediction sense and rules that a vendor naming a knowledge product a "world model" is recorded as a marketing alias on the relevant row, not as a second sense of the term.

- New page `wiki/tools/utopia.md`, filed under `knowledge-platform`, tagged into the knowledge cluster, stating that the product is *marketed as* an "enterprise world model" and that in the wiki's vocabulary it is an ontology-backed bitemporal knowledge graph.
- **Ontologies as agent guardrails** gains a new Current-status bullet naming Utopia as a concrete, deployable open-source system implementing that exact pattern — ontology-compiled derivation rules, ontology-checked-first conflict detection, and a specifically named "execution gate" roadmap item that would check agent tool calls against ontology rules directly. The page's existing "no benchmark, unresolved maintenance burden" caveats are left standing, since Utopia's own review-queue machinery is itself an acknowledgment of that burden, not a resolution of it. One Recent-changes entry is added (2 entries live, no spill). Page date moves to 9 September.
- **Knowledge architectures** gets Utopia appended to the ontology row's examples, a DeepLethe "enterprise world model" marketing-alias clause appended to the world-model row of the term map, Utopia added to the knowledge-graph row as an ontology-engine user, the source id, and a Recent-changes entry. No date change.
- **State of Agents** gains a Utopia line under its new "Knowledge platforms" subcategory. The page's Recent-changes list is at its 10-entry cap, so its oldest entry spills to history.
- **Subcategories schema** has Utopia appended to the examples line of `knowledge-platform` (no new vocabulary).
- **Wiki index** gains one new line under Tools; the tools and total-page counts each move up by one.
- One new source page is created for the project's README.

### What to weigh

The only available source is the project's own README — there's no independent benchmark, production case study, or third-party review of the tool as a whole, only a linked pull-request submission for the specific Ontology2SQL/BIRD Mini-Dev claim. The new tool page states this plainly under Weaknesses rather than repeating "state of the art" as settled fact. This proposal was rewritten on 9 September: the earlier version asked for a new `enterprise-knowledge-graph` subcategory, which the reorganization superseded with the broader `knowledge-platform` family, so no schema addition is requested any more.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/utopia.md` — new tool page
    > See draft below

- [ ] **Update** `wiki/concepts/ontology-agent-guardrails.md` — add 1 Current-status bullet, 1 Recent-changes entry (2 entries live, no spill), bump `as_of` to 2026-09-09, add source id
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — append Utopia to the ontology-row examples, append the marketing-alias clause to the world-model row, add Utopia to the knowledge-graph row, append the source id, add 1 Recent-changes entry; no `as_of` change
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — add 1 leader line under "Knowledge platforms", add 1 Recent-changes entry, bump `as_of` to 2026-09-09, add source id
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — the list is at its 10-entry cap; the oldest entry at apply time (currently `[2026-06-19] Kimi Work adds Goal Mode…`) moves to history
    > See draft below

- [ ] **Update** `wiki/_schema/subcategories.md` — append Utopia to the `knowledge-platform` examples line
    > See draft below

- [ ] **Update** `wiki/index.md` — add 1 line under Tools, bump `tools:` and `Total content pages:` counts by 1 each
    > See draft below

- [ ] **Create** `wiki/sources/repos/deeplethe-utopia-2026-09-09.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/tools/utopia.md (new)

```md
---
title: Utopia
type: tool
domains: [agents]
subcategory: knowledge-platform
tags: [open-source, knowledge-cluster]
as_of: 2026-09-09
sources: [deeplethe-utopia-2026-09-09]
---

# Utopia

Utopia is an open-source (Apache-2.0) bitemporal knowledge graph and ontology engine built by DeepLethe, which markets it as an "enterprise world model". In the wiki's vocabulary that phrase is a marketing alias: the product occupies the ontology row of the [Knowledge architectures](../concepts/knowledge-architectures.md) matrix (domain-scope classes, relations, and axioms used as machine-checked rules), not the physical or video-prediction sense the wiki reserves for "world model". Companies can deploy it air-gapped on their own hardware. Every extracted fact carries both when it was true in the world and when the system came to believe it — correcting a fact closes the old version and links the new one rather than overwriting, so a decision reviewed later can reproduce the exact grounds it rested on. The project explicitly positions itself as a different route to enterprise intelligence than Palantir-style systems: built bottom-up from knowledge governance toward trustworthy decisions, not top-down from an existing data platform.

## Also called

Enterprise world model (DeepLethe's marketing term), bitemporal knowledge graph, ontology engine.

## Current status (as of 2026-09-09)
- Ships as one Rust binary plus Postgres (Tantivy full-text search embedded, pgvector for vectors, job queue is a table) — runs fully air-gapped behind any OpenAI-compatible endpoint
- Ingests PDF/DOCX/PPTX/XLSX/CSV/Markdown/HTML/plain text, plus scheduled sync from web pages, RSS, GitHub, Jira, Notion, WebDAV, and S3-compatible buckets
- Built-in agent harness (and the same read-only tools over MCP) can search documents, walk the graph as of any date, and query a mounted database
- Ontology axioms (transitivity, symmetry, inverses, relation hierarchy) compile into forward-chaining derivation rules, off by default; a derived fact never overrides an asserted one it contradicts
- Three-stage entity resolution (exact match → embedding similarity → model judgment), every merge reversible, uncertain cases go to a review queue
- **Ontology2SQL** maps a mounted database's tables onto the ontology so chat can query structured data alongside documents; reported state-of-the-art on BIRD Mini-Dev (SQLite/PostgreSQL)
- Append-only decision ledger records every confirm/reject/merge/revert/rebuild, outliving the object or knowledge base it belonged to
- Still v0.1 — schema migrations only roll forward, no rollback; version pinning and backups recommended before upgrading

## Strengths
- Bitemporal design plus an append-only decision ledger gives a genuine audit trail for "why did the system believe this at the time," not just current-state search
- Fully air-gapped deployment (one binary, one Postgres, any OpenAI-compatible endpoint) suits regulated or on-prem-only environments
- Conflict detection treats ontology violations and fact clashes as separate, explicit decision points rather than silently overwriting data

## Weaknesses / caveats
- Early-stage (v0.1); no rollback path on schema migrations
- Source is the project's own README — no independent benchmark or production case study beyond the cited BIRD Mini-Dev submission for Ontology2SQL specifically

## Recent changes
- [2026-09-09] Page created from the project's GitHub README (no dated release event in the source).

## Related
- [Knowledge architectures](../concepts/knowledge-architectures.md) — the hub that places this product on the ontology row and pins "enterprise world model" as a marketing alias
- [Ontologies as agent guardrails](../concepts/ontology-agent-guardrails.md) — the formal-ontology-as-guardrail concept this tool implements concretely, including a working "execution gate" roadmap item that checks agent calls against ontology rules
- [Company brain](../concepts/company-brain.md) — Zep/Graphiti's "knowledge graph with a clock" in the company-brain survey is the same bitemporal idea at a different scope

## Sources
- [deeplethe/utopia (GitHub)](../sources/repos/deeplethe-utopia-2026-09-09.md)
```

### wiki/concepts/ontology-agent-guardrails.md (updated)

Frontmatter: bump `as_of: 2026-07-30` → `as_of: 2026-09-09`; append `deeplethe-utopia-2026-09-09` to `sources:`. Change the heading `## Current status (as of 2026-07-30)` → `## Current status (as of 2026-09-09)`.

Add to `## Current status`, as a new bullet at the end of the list:

```
- [Utopia](../tools/utopia.md) (open-source, Apache-2.0) is the clearest move yet from conference-talk concept to working product: ontology axioms compile directly into forward-chaining derivation rules, conflict detection checks the ontology itself before looking at fact-level clashes, and a named "execution gate" roadmap item would check an agent's tool calls against ontology rules and symbolic logic before allowing them to run. It doesn't resolve the maintenance-burden caveat below — its own review-queue and entity-resolution machinery is an acknowledgment of that burden, not a solution to it — but it's a concrete, deployable reference implementation of the pattern this page otherwise only describes in the abstract.
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-09] Added Utopia (open-source bitemporal knowledge graph / ontology engine) as a concrete, deployable implementation of the ontology-as-guardrail pattern: compiled derivation rules, ontology-checked-first conflict detection, and a named "execution gate" roadmap item for checking agent tool calls against ontology rules.
```

The list has 2 entries live (cap is 10) — no spill needed.

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter: append `deeplethe-utopia-2026-09-09` to `sources:`. `as_of` unchanged.

In the `## Canonical pages` table, ontology row, examples cell: change `Neo4j's three-layer ontology stack` → `Neo4j's three-layer ontology stack, [Utopia](../tools/utopia.md)`.

In the `## Term map` table, knowledge-graph row, note: change `used by company brains (Zep/Graphiti) and by personal assistants` → `used by company brains (Zep/Graphiti), by ontology engines ([Utopia](../tools/utopia.md)), and by personal assistants`.

In the world-model row, replace the final sentence of the note:

```
A vendor that names a knowledge product a "world model" is recorded as a marketing alias on the relevant row, not as a second sense of the term
```

with:

```
DeepLethe markets [Utopia](../tools/utopia.md) as an "enterprise world model"; that is a marketing alias for an ontology-backed bitemporal knowledge graph and maps to the ontology row, not to this sense
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-09] Utopia added as an ontology-row example and as the first recorded "world model" marketing alias, which the term map keeps on the ontology row.
```

Add to `## Sources`:

```
- [deeplethe/utopia (GitHub)](../sources/repos/deeplethe-utopia-2026-09-09.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter: bump `as_of: 2026-08-13` → `as_of: 2026-09-09`; append `deeplethe-utopia-2026-09-09` to `sources:`.

Add under `### Knowledge platforms`, after the OpenWiki line:

```
- [Utopia](../tools/utopia.md) — DeepLethe; open-source bitemporal knowledge graph and ontology engine, air-gapped one-binary deployment, agent harness over MCP; marketed as an "enterprise world model" *(as of 2026-09-09)*
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-09] Utopia (DeepLethe) added under Knowledge platforms: open-source bitemporal knowledge graph / ontology engine with an agent harness over MCP.
```

Then spill the oldest entry (see next draft) so the list stays at 10.

### wiki/history/state-of/agents.md (updated)

Append under the existing `## Archived from current page on 2026-09-09` header (create the header if a later apply date applies), the entry that is oldest at apply time — currently:

```
- [2026-06-19] Kimi Work adds Goal Mode, a long-running desktop-agent loop that continues until the user-defined objective is reached.
```

### wiki/_schema/subcategories.md (updated)

In the `### knowledge-platform` block, change:

```
- **Examples:** [OpenWiki](../tools/openwiki.md)
```

to:

```
- **Examples:** [OpenWiki](../tools/openwiki.md), [Utopia](../tools/utopia.md)
```

### wiki/index.md (updated)

Add under `## Tools`, in alphabetical position (after `tools/uipath-maestro` if present, otherwise at the end of the U entries):

```
- [tools/utopia](tools/utopia.md) — DeepLethe's open-source bitemporal knowledge graph and ontology engine, marketed as an "enterprise world model"; air-gapped one-binary deployment, agent harness over MCP, Ontology2SQL *(as_of: 2026-09-09)*
```

In `## Page count`, change `- tools: 93` → `- tools: 94` and `**Total content pages: 213.**` → `**Total content pages: 214.**` (re-derive from the live counts at apply time if other pages have landed).

### wiki/sources/repos/deeplethe-utopia-2026-09-09.md (new)

```md
---
title: "deeplethe/utopia (GitHub)"
type: source
source_type: repo
source_file: raw/repos/deeplethe-utopia.md
url: https://github.com/deeplethe/utopia
ingested: 2026-09-09
domains: [agents]
---

# deeplethe/utopia (GitHub)

README for Utopia, DeepLethe's open-source (Apache-2.0) bitemporal knowledge graph and ontology engine, marketed as an "enterprise world model": deployable air-gapped as one Rust binary plus Postgres, with a built-in agent harness (also exposed over MCP), ontology-driven cold-start, forward-chaining derivation, dual conflict detection, an ontology-to-SQL mapper, and an append-only decision ledger.

## Influenced pages

- [Utopia](../../tools/utopia.md) — new tool page
- [Ontologies as agent guardrails](../../concepts/ontology-agent-guardrails.md) — concrete implementation example
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — ontology-row example and world-model marketing-alias note now link to the tool page
- [State of Agents](../../state-of/agents.md) — new line under Knowledge platforms

## Key claims extracted

- Bitemporal knowledge graph: every fact carries both when it was true and when the system believed it; corrections close-and-link rather than overwrite
- Deployment: one Rust binary + Postgres (Tantivy full-text, pgvector, job queue as a table); fully air-gapped behind any OpenAI-compatible endpoint
- Built-in agent harness + identical read-only MCP tools: document search, graph-as-of-any-date, mounted-database queries
- Ontology-driven cold start: 5 bundled packs (schema.org, W3C Org, PROV-O, FOAF, IOF Core)
- Forward-chaining derivation from ontology axioms (transitivity, symmetry, inverses, relation hierarchy), off by default; asserted facts always beat contradicting derived facts
- Three-stage entity resolution (exact match → embedding similarity → model judgment), every merge reversible, review queue for uncertain cases
- Dual conflict detection: fact-vs-fact and fact-vs-ontology-axiom, ontology checked first
- Ontology2SQL: maps a mounted database onto the ontology for chat queries; submitted BIRD Mini-Dev result (SQLite/PostgreSQL)
- Append-only decision ledger; outlives the object or knowledge base it belonged to
- v0.1 — schema migrations only roll forward, no rollback
- Roadmap: execution gate (checks agent calls against ontology rules), business rules compiled to derived facts, decision reasoning/replay, more connectors, agent memory over MCP, enterprise features (SSO, backup/restore)
- "Enterprise world model" is the vendor's own framing; the README also explicitly declines the "open-source Palantir" framing
```
