---
title: Agent evals
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Agent evals

Evaluating an AI agent is not the same as evaluating an AI model. When you run a coding agent, you are not testing the underlying model in isolation. You are testing the combined system: `model + harness + tools + environment`. A change to any of those layers can change agent behavior even when the model itself has not changed.

That means agent evals are really about evaluating systems and behaviors: trajectories, tool use, policy adherence, failure recovery, and output quality together, not output quality alone.

## Why trajectory matters

Two agents can reach the same correct answer through very different paths. One got there efficiently in three steps. The other hallucinated a tool call, self-corrected, read thirty irrelevant files, and eventually succeeded. A result-only check marks both as passing. A trajectory eval catches the broken one.

This is why trajectory evaluation matters: the path reveals planning quality, tool efficiency, and failure risk, none of which are visible from the final answer alone.

## Five eval categories

A useful agent eval suite covers five categories, each catching a different class of failure:

- **Capability** — can the agent perform the task at all? This establishes baseline usefulness before worrying about efficiency or robustness.
- **Regression** — did a change to the prompt, tools, or underlying model break something that used to work?
- **Trajectory** — did the agent take a logical, efficient path? Did it avoid loops, call tools in the right order, and ask for clarification instead of guessing?
- **Unit-level** — does each component of the architecture work correctly in isolation? Examples: tool routing, retrieval, parsing, or permission checks.
- **Online (production)** — asynchronous scoring of live traffic to detect quality degradation, cost explosions, or latency spikes before users notice.

These categories are complementary. A unit-level failure suggests a routing or retrieval problem. A trajectory failure points to broken planning. A capability failure means the agent cannot do the task at all.

## How this changes eval design

Because the harness, tools, and environment are part of what you are evaluating:

- Eval results are not portable across harnesses. A score on one scaffold says little about the same model on another.
- Small harness changes such as a reworded system prompt or a new tool description can shift results significantly without any model update.
- The eval suite needs to cover multiple layers: result quality, trajectory quality, and component quality.
- Eval-driven development becomes a first-class practice: iterate on the harness using evals as the signal, separate from any model update. That is the premise of [Agent improvement loop](agent-improvement-loop.md).

## Caveats

- The five-category taxonomy here is a synthesis of common practice, not a single canonical industry standard.
- The harness-as-unit-under-test framing is widely shared, but the exact vocabulary varies by team and framework.

## Related

- [Harness (agent)](harness.md) — the scaffolding that is the primary unit under test in agent evals
- [Agent improvement loop](agent-improvement-loop.md) — the operational loop that uses evals to iteratively improve a harness
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — orchestration patterns that good evals help validate

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
