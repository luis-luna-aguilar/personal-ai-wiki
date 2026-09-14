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
