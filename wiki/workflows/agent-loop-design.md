---
title: Agent loop design
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-09-09
sources: [loopcraft-june-2026, aiewf-loops-debate-2026-07-03, claude-code-getting-started-with-loops-2026-06-30, what-the-hell-is-a-loop-anyway, andy-matuschak-agent-loop-tempo-2026-07, every-compound-engineering-upgrade-2026-05, aiewf-2026-five-trends-latentspace]
---

# Agent loop design

Patterns for designing the loop a single agent runs inside — trigger, goal condition, tool set, escalation, and stop signal — split out of [Agentic orchestration patterns](agentic-orchestration-patterns.md), which now covers context/harness, evaluation, and multi-agent patterns instead. See [Multi-agent coordination](multi-agent-coordination.md) for topology patterns across several agents.

## Loop design patterns

- **Loop-first design.** Before writing a single prompt, define what a successful loop looks like: trigger → goal condition → tool set → escalation. The loop is the unit of work, not the prompt. A well-designed loop handles variance you never predicted; a prompt just handles the case you imagined. *Source: Steipete/AINews, Satya Nadella essay, Hoop case study (June 2026)*
- **Loop taxonomy before loop complexity.** Anthropic's Claude Code team defines loops as agents repeating cycles of work until a stop condition is met, then separates four levels: turn-based loops hand off the check, goal-based loops hand off the stop condition, time-based loops hand off the trigger, and proactive loops hand off the prompt for recurring well-defined work. Use the lightest loop that fits the task.
- **Loop tempo selection.** Choose between close fast loops and slow delegated loops deliberately. Fast 1-2 minute loops preserve human control and comprehension; slow delegated loops work when the agent can proceed in the background with sparse checkpoints. The middle ground can be costly: 10-30 minute cycles often force parallelism, context switching, and weak comprehension.
- **Four-layer loop stack.** "Loop" now refers to at least four different architectures: execution loops iterate the agent's act-observe cycle inside one task; task loops restart one agent against one spec until an artifact satisfies tests; product loops run the software lifecycle around a codebase and backlog; system loops improve the prompts, harnesses, models, and evals behind the primary system.
- **Fresh-context task loops.** Ralph loops deliberately spend extra tokens by restarting a coding agent against the same specification in a fresh context window on each iteration. The goal is to avoid context rot and compaction drift; the loop should close on spec compliance and passing tests, not on the agent's self-assessment.
- **Oversight loop as the human layer.** Autonomy is not one global switch. Execution, task, product, and system loops can each have different human checkpoints, but the top-level loop that sets goals, allocates budgets, and culls work should remain explicit rather than disappearing into "full auto" rhetoric.
- **Pipeline versus loop.** Fan-out patterns such as Agentic MapReduce (see [Multi-agent coordination](multi-agent-coordination.md)) are useful topologies inside loops, but dispatch → gather → validate is only a pipeline unless the result feeds back into another cycle with a named signal.
- **Explicit stop criteria.** Goal-based and proactive loops work best when "done" is deterministic: tests pass, Lighthouse score clears a threshold, queue is empty, PR merges, or a turn cap is reached. Vague "make it better" loops increase both cost and drift.
- **Compound engineering loop.** For product-building agents, the practical loop is now ideate → brainstorm → plan → work → review → polish → compound → repeat. The agentic middle can be delegated when context and verification are strong; humans spend more time choosing the frame and polishing the outcome.

## Where these patterns surfaced

- Anthropic's Claude Code loop taxonomy turns loop choice into an operating decision: use normal turn-based prompts for exploration, `/goal` for deterministic exits, `/loop` or `/schedule` for time-triggered checks, and proactive routines only when the work is recurring and well-defined.
- Satya Nadella's June 2026 X essay (60M views) frames the loop as the primary product: build a learning loop where human capital and token capital compound, not just pick the best model.
- AINews coined "Loopcraft" (June 2026) to name the paradigm: designing loops that prompt agents rather than prompting agents directly.
- Dhinakaran and Seldo's loop map separates execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops, giving each a different iterated object, exit signal, and human role.
- AI Engineer World's Fair 2026 named the inner-loop/outer-loop split explicitly: Introspection's Roland Gavrilescu frames "autoresearch" as an outer-loop system that studies and maintains a primary inner-loop system; OpenClaw's Peter Steinberger put it plainly — "the agent runs the inner execution loop; I set the direction and I make decisions in the outer loop." A stage debate on whether fully autonomous loops are ready surfaced real disagreement: HumanLayer's Dex Horthy argued "the hype is outrunning the discipline" (loops need to be deterministic, like Kubernetes' control loops, not "frontier thinking"), while Ralph Loop creator Geoffrey Huntley likened the AI engineer's job to a locomotive engineer's: "[We're] kind of like locomotive engineers now. That's our job: to keep the locomotive on the rails."

## Recent changes

- [2026-09-09] Page created, split out of [Agentic orchestration patterns](agentic-orchestration-patterns.md)'s flat pattern list: loop-first design, loop taxonomy, loop tempo selection, the four-layer loop stack, fresh-context/Ralph loops, the oversight loop, pipeline-vs-loop, explicit stop criteria, and the compound engineering loop.
- [2026-07-14] Added named AI Engineer World's Fair 2026 detail to the loop-engineering pattern: inner/outer loop framing (Introspection, OpenClaw) and the autonomy-readiness stage debate (HumanLayer, Ralph Loop).
- [2026-07-08] Added loop-tempo selection from Andy Matuschak: fast controlled loops and slow delegated loops are easier to sustain than mid-speed partial-control loops.
- [2026-07-04] Dhinakaran and Seldo map loop discourse into execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops; they emphasize exit signals and per-loop autonomy dials.

## Related

- [Agentic orchestration patterns](agentic-orchestration-patterns.md) — context, harness, evaluation, and production patterns; the parent catalog this page split from
- [Multi-agent coordination](multi-agent-coordination.md) — topology patterns for running several agents together, as opposed to designing one agent's loop
- [Harness (agent)](../concepts/harness.md) — the scaffolding a loop runs inside

## Sources

- [Loopcraft and agent-native architecture — June 2026 digest](../sources/newsletters/loopcraft-june-2026.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Getting started with loops](../sources/articles/claude-code-getting-started-with-loops-2026-06-30.md)
- [What the hell is a loop, anyway?](../sources/articles/what-the-hell-is-a-loop-anyway.md)
- [Andy Matuschak on coding-agent loop tempo](../sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md)
- [Every - Compound Engineering Gets an Upgrade](../sources/newsletters/every-compound-engineering-upgrade-2026-05.md)
- [5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space](../sources/newsletters/aiewf-2026-five-trends-latentspace.md)
