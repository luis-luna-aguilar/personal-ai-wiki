---
type: proposal
source: raw/repos/helixdb-helix-foundry.md
status: pending
created: 2026-10-19
---

# Proposal: Helix Foundry (HelixDB GitHub repo)

## Summary

### In short

A coding agent can now stand up a queryable graph of a company's live business systems on one laptop: Helix Foundry ships as a repo plus a runbook the agent follows. It connects databases, Stripe, WorkOS, PostHog and files, matches the same customers and records across them into what it calls "one ontology", and answers questions with executed SQL that cites versioned snapshots. The proposal creates a tool page, lists it on State of Agents, and records its "ontology" on the Knowledge architectures hub as a vendor framing. Reason to hesitate: the repo has no release date, so 19 October stands in.

[[#Open questions|Open questions: 1 to answer.]]

### The source

Helix Foundry is an open-source (Apache 2.0) project from HelixDB, the company behind the graph database of the same name. Its README promises "your company's data, connected into one ontology, on your own computer." In practice it is a local data workspace: you connect the systems a company runs on (databases, Stripe, WorkOS, PostHog, APIs, files), and it proposes a single connected model in which the same customer, invoice or support ticket is recognised across sources and stored as objects and relationships in HelixDB. You confirm that model, then ask questions; answers come back as SQL that was actually run, with citations to the data snapshot it ran against. Data is kept as immutable snapshots, queried by sandboxed DuckDB processes.

Two things stand out. Setup is written for a coding agent: the README gives a prompt to paste into Claude Code, Codex or Cursor, and an AGENTS.md runbook tells the agent how to install, start and verify the stack and when to ask before deleting anything. And AI runs locally by default (a small Qwen model through Ollama), with Claude, OpenAI and others as options; AI-proposed changes wait for human review. The project says plainly that it is built for one person, has no accounts, and must never be exposed beyond localhost; its backup scripts have only stub tests so far.

### What changes

The wiki tracks two knowledge platforms, OpenWiki and Utopia, and its Knowledge architectures hub reserves "ontology" for formal rules that check what an agent asserts. Helix Foundry's ontology has no such rules; it is a matched graph of business records.

- New page `wiki/tools/helix-foundry.md` (subcategory `knowledge-platform`), saying the product is marketed as "one ontology" and placing it against the semantic-layer and ontology rows.
- **State of Agents** gains a Helix Foundry line under Knowledge platforms and one Recent-changes entry; the list is at its cap of 10, so the oldest entry (Vercel eve, 3 July) spills to history. Page date moves to 19 October.
- **Knowledge architectures** gains a term-map row for this sense of "ontology", adds Helix Foundry to the knowledge-graph row, and gets one Recent-changes entry. Page date moves from 7 September to 19 October.
- One new source page for the repo.

### What to weigh

A repository README has no publication date and the capture shows no release or commit date, so 19 October, the fetch date, is used throughout. The main judgment is placement: I treated the product as a tool page, following the Utopia precedent, and mapped its "ontology" to the hub's "knowledge graph, a data structure" row rather than opening a new matrix row. A one-person local workspace over a company's copied records is arguably a new combination of scope and contents; that is the open question.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/helix-foundry.md` — new tool page, subcategory `knowledge-platform`
- [ ] **Update** `wiki/state-of/agents.md` — add one line at the end of `### Knowledge platforms`; adds one Recent-changes entry dated 2026-10-19 at the top (10 → 11, over the cap of 10); append `helixdb-helix-foundry-2026-10-19` to frontmatter `sources:`; `as_of` 2026-10-14 → 2026-10-19
- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — spills the oldest Recent-changes entry (expected: `[2026-07-03] Vercel eve interview…`) under a new `## Archived from current page on <apply date>` block
- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — add one term-map row after the `knowledge graph` row and extend the `knowledge graph` row's note; adds one Recent-changes entry dated 2026-10-19 (4 → 5, no spill); append source id to frontmatter `sources:` and one link to `## Sources`; `as_of` 2026-09-07 → 2026-10-19
- [ ] **Create** `wiki/sources/repos/helixdb-helix-foundry-2026-10-19.md` — source summary

## Page drafts

### wiki/tools/helix-foundry.md (new)

```
---
title: Helix Foundry
type: tool
domains: [agents]
subcategory: knowledge-platform
tags: [open-source, knowledge-cluster]
as_of: 2026-10-19
sources: [helixdb-helix-foundry-2026-10-19]
---

# Helix Foundry

Helix Foundry is HelixDB's open-source (Apache 2.0) local-first data workspace, built on the HelixDB graph database and DuckDB. It connects the systems a company runs on, suggests one connected model that matches the same customers and records across them, and answers questions with executed SQL. HelixDB markets that model as "one ontology"; in the wiki's vocabulary it is a knowledge graph over business records, not an [ontology](../concepts/ontology-agent-guardrails.md) in the guardrail sense (it carries no axioms or machine-checked rules), and because it copies data into snapshots it is not a [semantic layer](../concepts/semantic-layer.md) either. See [Knowledge architectures](../concepts/knowledge-architectures.md).

## Also called

"One connected ontology" (HelixDB's marketing term), local-first data workspace.

## Current status (as of 2026-10-19)
- Connectors for Postgres, MySQL, Neon, Supabase, PlanetScale, Neo4j, Stripe, WorkOS, PostHog, REST APIs, S3-compatible storage, file uploads and an ingestion API; change capture on Postgres and MySQL where allowed, scheduled snapshots otherwise
- Suggested ontology matches records across sources and stores them as objects and relationships in HelixDB; the user confirms it during setup
- Data kept as immutable Parquet snapshots with profiles and schema-drift review; generated SQL runs in an isolated DuckDB executor with no internet access or credentials
- "Analyst" answers cite the executed SQL and the snapshot it ran on; AI-proposed changes are tested and wait for human review
- Local `qwen3:4b` through Ollama by default; Claude, OpenAI, Azure OpenAI, Bedrock or any OpenAI-compatible endpoint optional
- Installed by a coding agent: the README supplies a prompt for Claude Code, Codex or Cursor, and an AGENTS.md runbook covers preflight, setup, verification and when to ask before deleting data

## Strengths
- Nothing to host and no accounts; data and, by default, the model stay on the user's machine
- Answers are auditable: each one points to the SQL and the versioned snapshot behind it

## Weaknesses / caveats
- Built for one person: no sign-in, so anyone who can reach the app controls every workspace; must stay on localhost
- Backup, restore and upgrade scripts have only stub tests; Windows is untested; first run downloads several GB
- No dated release in the source; the HelixDB dependency is pinned at v0.0.12

## Recent changes
- [2026-10-19] Page created from the project's GitHub README (no dated release event in the source).

## Related
- [Knowledge architectures](../concepts/knowledge-architectures.md) — the hub that records "one ontology" as a vendor framing for a knowledge graph over business records
- [Utopia](../tools/utopia.md) — the other self-hosted knowledge platform tracked: also entity resolution plus SQL over mounted databases, but built on formal ontology axioms and a bitemporal decision ledger
- [Semantic layer](../concepts/semantic-layer.md) — governs metric definitions over a warehouse without copying data; Helix Foundry copies the data and matches records instead

## Sources
- [HelixDB/helix-foundry (GitHub)](../sources/repos/helixdb-helix-foundry-2026-10-19.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter (changed fields only; `sources:` appends `helixdb-helix-foundry-2026-10-19` at the end of the live list):

```
as_of: 2026-10-19
```

`### Knowledge platforms` — new line appended after the Utopia line:

```
- [Helix Foundry](../tools/helix-foundry.md) — HelixDB; open-source local-first data workspace that matches records across a company's databases and SaaS tools into one graph (marketed as "one ontology") and answers with cited SQL; installed by a coding agent *(as of 2026-10-19)*
```

`## Recent changes` — adds one entry at the top; the oldest entry (`[2026-07-03] Vercel eve interview…`) leaves the list (see Spill draft):

```
- [2026-10-19] Added [Helix Foundry](../tools/helix-foundry.md) to Knowledge platforms: HelixDB's local-first data workspace that joins a company's data sources into one graph and answers with SQL cited to versioned snapshots.
- [2026-10-14] Added `Agent web data extraction` subcategory with [Expand Fetch](../tools/expand-fetch.md): agent-oriented fetch API with trained Markdown (Iris) and hidden-JSON (X-Ray) models; vendor-run MDBench 74.1% vs Exa 55.3%, Firecrawl 27.2%.
- [2026-10-09] Added [Harness²](../tools/harness2.md) to Agent frameworks: Google's open-source recursive harnessing framework, frozen weights, up to +11.5 points on WorkBuddy-Bench.
- [2026-09-09] Utopia (DeepLethe) added under Knowledge platforms: open-source bitemporal knowledge graph / ontology engine with an agent harness over MCP.
- [2026-09-09] Added Mastra to Agent frameworks: YC-backed open-source TypeScript framework combining an agent abstraction with an explicit graph-based workflow engine, human-in-the-loop suspend/resume, and Observational Memory.
- [2026-09-09] Added a `Knowledge platforms` subcategory (new `knowledge-platform` schema entry) and moved [OpenWiki](../tools/openwiki.md) into it from Agent frameworks, as part of the knowledge-cluster terminology reorganization anchored on [Knowledge architectures](../concepts/knowledge-architectures.md).
- [2026-08-13] Grok Bot launched (xAI/SpaceXAI): "AI teammates with their own cloud computers," a new entrant in the AI-teammate category alongside Claude Tag.
- [2026-07-08] Added `Agent sandbox / compute infrastructure` subcategory with [Daytona](../tools/daytona.md), [Modal](../tools/modal.md), and [Railway](../tools/railway.md); agent execution-layer providers now tracked here and in [Agent-native compute infrastructure](../trends/agent-native-compute.md)
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
- [2026-07-08] Google managed agents in the Gemini API add MCP support, background execution, custom function calling, and credential refresh, making hosted agent runtime features first-party Gemini primitives.
```

### wiki/history/state-of/agents.md (updated)

Appended at the end of the file:

```

## Archived from current page on 2026-10-19

- [2026-07-03] Vercel eve interview adds an agent-framework signal: agents as a new software category needing resumability, long-running jobs, skills, sandboxes, observability, and evals.
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-19
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, dhravyashah-supermemory-company-brain-2026-07-28, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09, helixdb-helix-foundry-2026-10-19]
```

`## Term map` — the `knowledge graph` row is replaced, and one new row follows it:

```
| knowledge graph | a data structure, not a concept | used by company brains (Zep/Graphiti), by ontology engines ([Utopia](../tools/utopia.md)), by personal assistants ([Amazon Quick](../tools/amazon-quick.md)), and by local data workspaces ([Helix Foundry](../tools/helix-foundry.md)). Link to the page whose system uses it |
| "one ontology" over company data | a knowledge graph over business records | Helix Foundry's term for the model it suggests by matching the same customers and records across connected sources. It has no axioms or machine-checked rules, so it is not the ontology row's sense, and it copies data into snapshots, so it is not a semantic layer. A marketing alias; see [Helix Foundry](../tools/helix-foundry.md) |
```

`## Recent changes` (adds one entry dated 2026-10-19 at the top):

```
- [2026-10-19] Recorded Helix Foundry's "one ontology" as a marketing alias for a knowledge graph over business records, not the ontology row's sense, and added it to the knowledge-graph row.
- [2026-09-09] Utopia added as an ontology-row example and as the first recorded "world model" marketing alias, which the term map keeps on the ontology row.
- [2026-09-09] Page created as the vocabulary hub for the knowledge, memory, company-brain, and ontology cluster, after the four existing pages had drifted into contradictory "this vs that" descriptions of each other.
- [2026-08-21] Added the semantic-layer row (governed metric and data-source definitions over an existing warehouse) from PostHog's account, plus "context warehouse" and "metrics layer" term-map rows.
- [2026-07-28] Added Supermemory Company Brain to the Company brain row's tracked examples, mirroring the new production example on that page.
```

`## Sources` (appends one link):

```
- [HelixDB/helix-foundry (GitHub)](../sources/repos/helixdb-helix-foundry-2026-10-19.md)
```

### wiki/sources/repos/helixdb-helix-foundry-2026-10-19.md (new)

```
---
title: 'HelixDB/helix-foundry (GitHub)'
type: source
source_type: repo
source_file: raw/repos/helixdb-helix-foundry.md
url: https://github.com/HelixDB/helix-foundry
ingested: 2026-10-19
domains: [agents]
---

# HelixDB/helix-foundry (GitHub)

README for Helix Foundry, HelixDB's open-source (Apache 2.0) local-first data workspace built on HelixDB and DuckDB. It connects a company's databases, SaaS tools and files, suggests one connected "ontology" that matches the same records across sources, keeps data as versioned Parquet snapshots, and answers questions with executed SQL cited to those snapshots. Setup is delegated to a coding agent through a pasted prompt and an AGENTS.md runbook. The README gives no release date; the capture date (2026-10-19) is used.

## Influenced pages

- [Helix Foundry](../../tools/helix-foundry.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new line under Knowledge platforms
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "one ontology" recorded as a marketing alias for a knowledge graph over business records

## Key claims extracted

- Tagline: "Your company's data, connected into one ontology, on your own computer"; no accounts, nothing to host, AI local by default
- Connectors: Neon, Supabase, PlanetScale, PostgreSQL, MySQL, Neo4j, Stripe, WorkOS, PostHog, REST APIs, S3-compatible storage, CSV/JSON/JSONL/Parquet uploads, ingestion API
- Automatic sync via native Postgres/MySQL change capture where allowed, scheduled snapshot refreshes otherwise
- Suggested ontology matches the same customers and records across sources, stored as objects and relationships in HelixDB; confirmed by the user in guided setup (AI → Data → Ontology)
- Immutable Parquet snapshots with profiles, schema-drift review and history; queried by isolated DuckDB processes with no internet, no credentials, no Linux capabilities
- Home shows key metrics; Analyst answers are backed by executed SQL with snapshot citations
- Default model `qwen3:4b` via Ollama; Claude, OpenAI, Azure OpenAI, Amazon Bedrock or custom OpenAI-compatible endpoints optional; AI-proposed changes are tested and wait for review
- Coding-agent install: paste a prompt into Claude Code, Codex or Cursor; the agent follows AGENTS.md and asks before deleting data or stopping running services; credentials are entered by the user in the browser, never given to the agent
- Built for one person on one computer: no sign-in, localhost only, API rejects foreign hosts and origins with 403; credentials encrypted with a local key
- Developer access: OpenAPI, TypeScript SDK, scoped read-only-by-default API tokens, backup/restore/upgrade scripts (only stub Docker tests so far)
- Validated on macOS Apple Silicon, CI on Linux, Windows untested; HelixDB pinned at v0.0.12
```

## Schema / vocabulary additions

None. `knowledge-platform`, `open-source` and `knowledge-cluster` already exist.

## Open questions

- Should a single-user workspace that copies and matches an organization's records get its own row in the Knowledge architectures matrix (it differs from the semantic layer, which copies nothing, and from the ontology row, which holds rules), or stay as a term-map alias until a second product of the same shape is ingested?
	- Yeah, its a variant of that approach
