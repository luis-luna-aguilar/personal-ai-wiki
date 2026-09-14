---
type: proposal
source: raw/articles/2026-09-09-cerebrasai-blog-how-we-built-our-knowledge-base.md
status: pending
created: 2026-09-09
---

# Proposal: Cerebras — "How We Built Our Knowledge Base"

## Summary

### The source

Cerebras's own engineering team (Isaac Tai, Daniel Kim, Mike Gao) describes Cerebras Knowledge, an internal tool that was fielding more than 15,000 questions a day three months after launch, used by humans, automations, and agents across the company's chip-design, data-center, training, and inference teams. The architecture is a single Postgres table holding embeddings, raw summaries, and metadata, fed by a separate connector per source — Slack, wiki/Confluence, code repositories, netlists, custom internal databases — so that whatever lands in the table is immediately queryable through one shared interface regardless of where it came from. Slack gets the most engineering attention: messages arrive in real time over a Socket Mode bot, and any reply re-pulls the entire thread (not just the new message) so the stored record always reflects the full conversation; an LLM then distills each thread into a structured question/summary/resolution artifact for embedding, while short "bursts" of consecutive messages from one author are separately embedded (with the thread topic prepended for context) so a buried but important reply doesn't get lost inside a thread-level summary — bursts have to clear a rarity/length/reaction-based threshold first to keep low-signal noise out. Slack search itself blends four techniques — full-text for exact tokens, embeddings for paraphrase, inverse-document-frequency weighting so rare tokens beat filler, and age decay so newer answers win ties — because the team found no single technique sufficient on its own. Code repositories are chunked with an open-source tool (CocoIndex) using language-aware boundaries that try classes first and fall back to methods and smaller blocks, then incrementally re-embed only what changed on each commit. At query time, a planner picks from six tools (search, search_slack, search_code, subsystem_index, recent_prs, who_knows), fans them out in parallel, and fuses the results with reciprocal rank fusion before a small reranker model picks a final top ten and expands each winner with neighboring context. The same primitives are exposed as narrow, deliberately LLM-free MCP tools rather than one "answer this question" endpoint, so Claude Code or any other MCP client can call them directly and own the orchestration itself; a lightweight "projects" layer scopes each team's default search to its own sources so a compiler engineer isn't served infrastructure runbooks by default. No publish date appears on the post itself.

### What changes

[Company brain](../wiki/concepts/company-brain.md) already tracks two large production examples of the four-function company-brain pattern (Lovable's capabilities pivot, Cloudflare OS) beyond its 9-implementation survey. This proposal adds Cerebras Knowledge as a further production example — the intro sentence's count word is incremented by one to match whatever it reads at apply time — and moves the page's `as_of` forward to today, since this source carries no stated publish date and falls back to ingest date, which is newer than the page's current 2026-09-07. [Model Context Protocol](../wiki/concepts/mcp.md) gains a smaller addition: Cerebras's narrow, LLM-free MCP tool design is a second production confirmation of the same small-tool-count, precise-names, tightly-defined-outputs guidance the page already sources to Stainless's Alex Rattray, so it's added as a supporting bullet with its own `as_of` bump. One new source page is created.

### What to weigh

The post carries no publish date, so both touched pages' `as_of` move to the ingest date (2026-09-09) rather than a true publication date — flagged on the new source page. Otherwise this is a strong, detailed first-party engineering account with no unusual sourcing concerns.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/company-brain.md` — add Cerebras Knowledge as a production example, increment the intro count word, bump `as_of` to 2026-09-09, append the source id, add one Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/concepts/mcp.md` — add a narrow-tool-MCP-design bullet citing Cerebras as a second production example, bump `as_of` to 2026-09-09, append the source id, add one Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/articles/cerebras-knowledge-base.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/concepts/company-brain.md (updated)

Frontmatter: append `cerebras-knowledge-base` to `sources:`; bump `as_of` to `2026-09-09` (newer than the page's current 2026-09-07, using this source's ingest-date fallback).

Change `## Current status (as of 2026-09-07)` to `## Current status (as of 2026-09-09)`.

Change the intro sentence (word incremented by one from whatever the live page reads at apply time — currently "Two", or "Three" if the Supermemory proposal already landed):

```
Two larger production examples show the pattern scaling into full platforms rather than personal tools:
```

Append this bullet at the end of the production-examples list:

```md
- **Cerebras Knowledge:** an internal tool fielding 15,000+ questions/day three months after launch, built around one shared Postgres table of embeddings, summaries, and metadata fed by per-source connectors (Slack, wiki/Confluence, code repos, netlists, custom databases) so anything ingested is immediately queryable through the same interface. Retrieval fuses six parallel search lists — full-text, embedding, thread-summary, code-graph, wiki-vector, and Slack full-text — with reciprocal rank fusion before a small reranker model picks the final top ten. The same retrieval primitives are exposed as narrow, LLM-free MCP tools (search, search_slack, search_code, who_knows) rather than one black-box "answer this question" endpoint, so Claude Code or any MCP client owns the orchestration itself; "projects" scope a user's default search to their team's own sources instead of the whole company corpus.
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-09] Added Cerebras Knowledge as a production example: one shared Postgres embeddings table across Slack/wiki/code/custom sources, six-way retrieval fusion via reciprocal rank fusion, and narrow LLM-free MCP tools that let the calling client (e.g. Claude Code) own orchestration instead of one black-box answer endpoint.
```

Add to `## Sources`:

```
- [Cerebras — How We Built Our Knowledge Base](../sources/articles/cerebras-knowledge-base.md)
```

### wiki/concepts/mcp.md (updated)

Frontmatter: append `cerebras-knowledge-base` to `sources:`; bump `as_of` to `2026-09-09` (newer than the page's current 2026-09-07).

Add this bullet under `## Current status`, immediately after the Stainless/Rattray bullet:

```md
- **A second production system confirms narrow-tool MCP design.** Cerebras's internal knowledge base (see [Company brain](company-brain.md)) exposes its retrieval primitives — search, search_slack, search_code, who_knows — as separate, LLM-free MCP tools instead of one "answer this question" endpoint, so any MCP client, Claude Code included, calls them directly and owns the orchestration itself; echoes Stainless CEO Alex Rattray's small-tool-count / precise-names / tightly-defined-outputs guidance above.
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-09] Cerebras's internal knowledge base confirms the narrow-tool MCP design pattern (small, LLM-free, composable tools; client owns orchestration) with a second production example alongside Stainless's guidance.
```

Add to `## Sources`:

```
- [Cerebras — How We Built Our Knowledge Base](../sources/articles/cerebras-knowledge-base.md)
```

### wiki/sources/articles/cerebras-knowledge-base.md (new)

```md
---
title: How Cerebras Built Its Enterprise Knowledge Base
type: source
source_type: article
source_file: raw/articles/2026-09-09-cerebrasai-blog-how-we-built-our-knowledge-base.md
url: https://www.cerebras.ai/blog/how-we-built-our-knowledge-base
ingested: 2026-09-09
domains: [agents]
---

# How Cerebras Built Its Enterprise Knowledge Base

Engineering writeup (Isaac Tai, Daniel Kim, Mike Gao) describing Cerebras Knowledge, an internal tool fielding 15,000+ questions/day three months after launch. A single Postgres table holds embeddings, summaries, and metadata from per-source connectors (Slack, wiki/Confluence, code repos, netlists, custom databases), so every source lands in one immediately-queryable schema. Slack ingestion runs in real time over Socket Mode, re-pulls the whole thread on any reply, and distills each thread into a structured question/summary/resolution artifact via an LLM before embedding it, plus separately embeds high-signal "bursts" of consecutive messages that would otherwise be lost inside a thread summary. Code repositories are chunked with CocoIndex using language-aware, coarsest-boundary-first splitting and incrementally re-embedded on every commit. At query time, a planner picks which of six tools to fan out to (search, search_slack, search_code, subsystem_index, recent_prs, who_knows); results are fused across six parallel retrieval lists with reciprocal rank fusion, reranked by a small model, then expanded with neighboring context before a synthesis LLM answers with citations. The same primitives are exposed as narrow, LLM-free MCP tools so any MCP client can orchestrate retrieval directly. "Projects" scope default search to a team's own sources. No publish date found on the page; `ingested` is used as `published` is unknown.

## Influenced pages
- [Company brain](../../concepts/company-brain.md) — added as a production example: one shared embeddings table across heterogeneous sources, six-way retrieval fusion, and narrow MCP-exposed retrieval primitives
- [Model Context Protocol](../../concepts/mcp.md) — added as a second production confirmation of the narrow-tool MCP design pattern already sourced to Stainless's Alex Rattray

## Key claims extracted
- Cerebras Knowledge fields 15,000+ questions/day, three months after launch
- One Postgres table (pgvector, 3072-dim, HNSW) holds embeddings/summaries/metadata from every connected source
- Slack retrieval combines full-text search, embeddings, IDF-based rare-token weighting, and age decay because no single technique alone was sufficient
- Code repos are chunked language-aware (class → method → block boundaries) via CocoIndex and incrementally re-embedded per commit
- Retrieval fuses six parallel search lists via reciprocal rank fusion (k=60), then reranks the top candidates with a small model
- MCP tools are deliberately narrow and LLM-free (search, search_slack, search_code, who_knows) so the calling client owns orchestration
```
