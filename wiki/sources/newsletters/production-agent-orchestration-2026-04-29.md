---
title: Production agent orchestration primitives
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-29-ainews-not-much-happened-today.md
published: 2026-04-29
ingested: 2026-05-05
domains: [agents]
---

# Production agent orchestration primitives

AINews reports Mistral Workflows entering public preview alongside broader community discussion of production-agent infrastructure primitives: durable execution, state persistence, streaming outputs, subagent coordination, and session resumption.

## Key claims extracted

- Mistral Workflows (public preview): Mistral's hosted workflow execution platform for multi-step agent tasks
- Durable execution: tasks survive process crashes and infrastructure interruptions; can resume from last checkpoint
- State persistence: agent state (memory, partial outputs, tool results) persists across workflow steps and restarts
- Streaming: partial outputs are streamed to the caller before the full workflow completes
- Subagents: Mistral Workflows supports spawning subagent tasks within a parent workflow
- Resumption: interrupted workflows can be resumed from a specific step rather than restarted from scratch

## Caveats

- AINews synthesis; Mistral Workflows feature set should be verified against Mistral documentation
- "Public preview" status means the feature set may still be changing

## Influenced pages

- `wiki/workflows/agentic-orchestration-patterns.md` — durable execution and resumption patterns
- `wiki/state-of/agents.md` — production orchestration primitives
