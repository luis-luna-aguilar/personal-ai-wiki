---
title: Agent-local search
type: concept
domains: [coding, agents]
tags: [agentic]
as_of: 2026-10-13
sources: [context-dot-dev-sgrep, xerj-org, ainews-perplexity-grep-vs-semantic-2026-10-13]
---

# Agent-local search

Search tools built for coding agents that run on the developer's own machine, with no hosted index or model server, and decide what reaches the agent's context window. They sit between plain exact search (grep, ripgrep), which finds every match but cannot tell which one matters, and hosted semantic search, which needs an account and uploads files. Their pitch is cost: the agent reads fewer, better passages, so it spends fewer tokens for the same result.

## Current status (as of 2026-10-13)

- Two open-source Rust tools launched on 2026-10-13, one ranking ripgrep's output and one replacing file reads with an index
- Reported savings at an equal solve rate: 21.3% lower LLM spend (sgrep), 2.7x fewer output tokens (XERJ), 34% fewer API tokens (ColGrep-Agent-2B)
- Exact search still wins on exact text: Perplexity found grep beat semantic search 63% to 37% on financial-document questions
- Rule of thumb from the tools themselves: exact search for known names and regexes, ranked or indexed search for intent queries ("when does a failed scrape consume credits")

## Tools

- **sgrep** (Context.dev, MIT): a CLI that searches by words and meaning, or reranks a focused ripgrep command piped into it. It ranks with static embeddings (one stored vector per token, averaged, so no neural network runs at search time) blended 75/25 with BM25 keyword scores, and puts exact identifier matches first. CPU only, 32–34 MB model. On SWE-bench Verified with GPT-6 Luna it used 21.3% less LLM spend than ripgrep and solved 70 of 100 attempts against 68. Its README concedes that rival CK beats it on snippet retrieval.
- **XERJ** (Apache-2.0): one binary that indexes code, documents and data behind an Elasticsearch-compatible API, with a `/_memory` API for agent memory. Its "reference coding" idea is to index the open-source repos closest to your project so the agent looks up real definitions instead of inventing them. Reports 2.7x fewer output tokens than a grep-driven agent at the same solve rate over eight tasks, and the right file first 94% of the time with definition-first search against 38% for body-text search. On a ten-question data exam it only tied a grep-and-Python baseline (9 plus a partial, against 10).
- **ColGrep-Agent-2B**: a local code-search agent claiming 34% fewer API tokens; known only from a one-line newsletter mention.

## Related

- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — the "rank or index search results" pattern these tools serve
- [Harness (agent)](harness.md) — the harness layer where search tools are wired in

## Recent changes

- [2026-10-13] Page created: sgrep and XERJ launch the same day; Perplexity's grep-beats-semantic result as counterpoint; ColGrep-Agent-2B noted.

## Sources

- [context-dot-dev/sgrep (GitHub README)](../sources/repos/context-dot-dev-sgrep.md)
- [XERJ — the search engine built for AI agents](../sources/articles/xerj-org.md)
- [AINews — Perplexity: grep beats semantic search on financial documents](../sources/newsletters/ainews-perplexity-grep-vs-semantic-2026-10-13.md)
