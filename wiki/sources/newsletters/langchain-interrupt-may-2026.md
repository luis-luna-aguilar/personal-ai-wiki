---
title: "LangChain Interrupt conference — agent infra cluster (May 2026)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-15-ainews-everything-is-conductor.md
published: 2026-05-15
ingested: 2026-05-18
domains: [agents]
---

# LangChain Interrupt conference — agent infra cluster (May 2026)

AINews and AINews prior-day covered LangChain's Interrupt conference release: SmithDB (purpose-built agent trace database), LangSmith Engine (trace→cluster→fix improvement loop), and LangChain Labs (continual learning from production traces). Community commentary emphasized SmithDB's architectural shift toward object storage + custom query path for the agent-trace workload shape.

## Influenced pages

- [LangChain / LangSmith](../../tools/langchain-langsmith.md) — new tool page created
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — LangSmith Engine as new product example; SmithDB infrastructure layer
- [State of Agents](../../state-of/agents.md) — added to Agent frameworks

## Key claims extracted

- SmithDB: built on Apache DataFusion + Vortex; 12-15× faster access on nested long-running trace workloads
- LangSmith Engine: consumes traces, clusters failures, identifies code issues, proposes fixes/evals automatically
- LangChain Labs: continual learning for agents; production traces → training signal → targeted improvements; Prime Intellect partnership
- Also shipped at Interrupt: Managed Deep Agents, LLM Gateway, Context Hub, Deep Agents 0.6, streaming typed projections, checkpoint storage, code interpreter
- Community noted SmithDB's object storage + custom query path as the key architectural bet vs. adapting general-purpose log DBs
