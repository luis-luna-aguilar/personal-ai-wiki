---
title: Harness engineering patterns
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-13-the-folder-is-the-agent.md
ingested: 2026-04-13
domains: [agents, coding]
---

# Harness engineering patterns

This source summary groups several closely aligned signals about how agents should be structured. The shared takeaway is that robust agent behavior comes from explicit context packaging, evaluator separation, and a thin orchestration layer rather than from maximal swarm complexity.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — adds folder-scoped specialization, evaluator separation, and thin-harness framing
- [Harness (agent)](../../concepts/harness.md) — clarifies the distinction between context packaging and loop logic

## Key claims extracted

- A project folder plus durable instructions and skills can function as the real unit of specialization for an agent
- Long-running work benefits from planner/generator/evaluator separation instead of one model grading itself
- "Fat skills / fat code / thin harness" is a useful design heuristic for where behavior should live
- Filesystems, memory, permissions, retries, evals, and subagents are increasingly treated as first-class agent surface
