---
title: "mastra-ai/mastra (GitHub)"
type: source
source_type: repo
source_file: raw/repos/mastra-ai-mastra.md
url: https://github.com/mastra-ai/mastra
ingested: 2026-09-09
domains: [agents, coding]
---

# mastra-ai/mastra (GitHub)

README for Mastra, a YC-backed open-source TypeScript framework for building AI applications and agents: model routing across 40+ providers, a separate agent/workflow primitive split, human-in-the-loop suspend/resume, memory + RAG, MCP server authoring, and built-in evals/observability.

## Influenced pages

- [Mastra](../../tools/mastra.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new leader line under Agent frameworks

## Key claims extracted

- Open-source (Apache 2.0 core; `ee/` directories under a separate Enterprise License), YC W25
- Model routing across 40+ providers through one interface
- Explicit split between agents (autonomous, tool-using) and workflows (deterministic graph control: `.then()`, `.branch()`, `.parallel()`)
- Human-in-the-loop suspend/resume backed by durable storage
- Conversational memory + RAG retrieval; "Observational Memory" for human-like persistent recall
- MCP server authoring
- Distributed via `npm create mastra@latest`; local dev surface "Mastra Studio" at localhost:4111
