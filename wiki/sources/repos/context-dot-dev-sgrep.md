---
title: context-dot-dev/sgrep (GitHub README)
type: source
source_type: repo
source_file: raw/repos/context-dot-dev-sgrep.md
url: https://github.com/context-dot-dev/sgrep
published: 2026-10-13
ingested: 2026-10-20
domains: [coding, agents]
---

# context-dot-dev/sgrep (GitHub README)

README for sgrep, Context.dev's MIT-licensed local search CLI for agents, launched 2026-10-13. Written in Rust, it finds code and document passages by words and meaning, or reranks the output of a focused ripgrep command (`rg --json ... | sgrep "<query>" --stdin`). Ranking uses Minish Lab static embeddings (one stored vector per token, averaged; no transformer pass at search time, 32–34 MB model, CPU only), blended 75% semantic / 25% BM25, with exact identifier matches ranked first. No account, hosted index, or model server. The README positions it against ripgrep (exact names and regexes), CK (local semantic search, which beats sgrep on CoSQA snippet retrieval) and mgrep (hosted, uploads files).

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — ranked/indexed local search pattern
- [Agent-local search](../../concepts/agent-local-search.md) — new grouping page: sgrep entry

## Key claims extracted
- Piped sgrep used 21.3% less LLM API spend than ripgrep on SWE-bench Verified (GPT-6 Luna, 50 tasks x 2 repeats), solving 70/100 vs 68/100 attempts
- Leads complete-function retrieval on RepoQA (600 questions); CK semantic leads snippet retrieval on CoSQA (500 questions)
- Use ripgrep for exact matches; sgrep returns approximate matches and its scores are relative ranking signals, not confidence values
- Code parsing via Tree-sitter for Python, C/C++, C#, Go, Java, Rust, JS/TS; no PDF or image parsing
