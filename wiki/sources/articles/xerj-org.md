---
title: XERJ — the search engine built for AI agents
type: source
source_type: article
source_file: raw/articles/2026-10-20-xerjorg.md
url: https://xerj.org
published: 2026-10-13
ingested: 2026-10-20
domains: [coding, agents]
---

# XERJ — the search engine built for AI agents

Homepage of XERJ, an Apache-2.0 search engine shipped as one static Rust binary that indexes code, documents and data and answers agent queries from the index instead of the agent's context window. It speaks the Elasticsearch API, parses source with tree-sitter (36 languages) into a definitions field, and adds a namespaced `/_memory` API for agent memory. The page carries no date; the published date is the launch tweet's (Ivan Novikov, 2026-10-13), which also names a public "Corpus Hub" of shared reference corpora.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — ranked/indexed local search pattern
- [Agent-local search](../../concepts/agent-local-search.md) — new grouping page: XERJ entry

## Key claims extracted
- "Reference coding": clone and index the open-source repos closest to the project so the agent retrieves exact definitions before writing code
- Eight tasks in four languages, 16 runs per arm: 2.7x fewer output tokens than a grep-driven agent at the same solve rate, roughly half the cost; 9/9 vs 0/9 on a Rust library the model had not seen
- Definition-first search puts the right file first 94% of the time on an 80-task cross-file benchmark, vs 38% for body-text search
- On a 518 MB, ten-question data exam, a XERJ-backed agent scored 9 plus 1 partial vs a grep-and-Python baseline's 10/10: "a tie on accuracy"
- Built-in embedder is lexical feature-hashing, not neural; neural encoder is an optional upgrade
