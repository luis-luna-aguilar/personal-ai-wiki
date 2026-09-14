---
title: Mastra
type: tool
domains: [agents, coding]
subcategory: agent-framework
tags: [open-source, agentic]
as_of: 2026-09-09
sources: [mastra-ai-mastra-2026-09-09]
---

# Mastra

Mastra is an open-source TypeScript framework for building AI-powered applications and agents, backed by Y Combinator (W25 batch). It positions itself as a full-stack layer for going from prototype to production: model routing across 40+ providers through one interface, an agent abstraction (LLM + tools, autonomous reasoning to a stopping condition), a graph-based workflow engine for explicit multi-step control flow (`.then()`, `.branch()`, `.parallel()`), human-in-the-loop suspend/resume backed by durable storage, conversational memory plus RAG retrieval, MCP server authoring, and built-in evals/observability. It integrates into existing React/Next.js/Node apps or deploys standalone.

## Current status (as of 2026-09-09)
- Core framework is Apache 2.0; code under any `ee/` directory is source-available under a separate Mastra Enterprise License (free for dev/test, licensed for production)
- Distributed via `npm create mastra@latest`; ships a local dev/test surface called Mastra Studio (`localhost:4111`)
- "Observational Memory" gives agents human-like persistent memory alongside conversation history and RAG retrieval — see [Agent memory](../concepts/agent-memory.md)
- Positions workflows (deterministic graph control) and agents (open-ended tool-using reasoning) as distinct, composable primitives rather than one blended abstraction

## Strengths
- Explicit workflow/agent split gives teams a deterministic escalation path instead of forcing every step through agentic reasoning
- Model-routing layer decouples app code from any single provider

## Weaknesses / caveats
- Source is Mastra's own GitHub README — no dated release event, adoption numbers, or independent benchmark to evaluate the "production-ready" claim against

## Recent changes
- [2026-09-09] Page created from Mastra's GitHub README (no dated release event in the source).

## Sources
- [mastra-ai/mastra (GitHub)](../sources/repos/mastra-ai-mastra-2026-09-09.md)
