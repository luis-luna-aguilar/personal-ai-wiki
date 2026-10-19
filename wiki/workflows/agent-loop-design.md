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
- **Loop taxonomy before loop complexity.** Anthropic's Claude Code team defines loops as agents repeating cycles of work until a stop condition is met, then separates four levels: turn-based loops hand off the check, goal-based loops hand off the stop condition, time-based loops hand off the trigger, and proactive loops hand off the prompt for recurring well-defined work. Use the lightest loop that fits the task (see the Claude Code loop taxonomy table below).
- **Loop tempo selection.** Choose between close fast loops and slow delegated loops deliberately. Fast 1-2 minute loops preserve human control and comprehension; slow delegated loops work when the agent can proceed in the background with sparse checkpoints. The middle ground can be costly: 10-30 minute cycles often force parallelism, context switching, and weak comprehension.
- **Four-layer loop stack.** "Loop" now refers to at least four different architectures: execution loops iterate the agent's act-observe cycle inside one task; task loops restart one agent against one spec until an artifact satisfies tests; product loops run the software lifecycle around a codebase and backlog; system loops improve the prompts, harnesses, models, and evals behind the primary system.
- **Fresh-context task loops.** Ralph loops deliberately spend extra tokens by restarting a coding agent against the same specification in a fresh context window on each iteration. The goal is to avoid context rot and compaction drift; the loop should close on spec compliance and passing tests, not on the agent's self-assessment.
- **Oversight loop as the human layer.** Autonomy is not one global switch. Execution, task, product, and system loops can each have different human checkpoints, but the top-level loop that sets goals, allocates budgets, and culls work should remain explicit rather than disappearing into "full auto" rhetoric.
- **Pipeline versus loop.** Fan-out patterns such as Agentic MapReduce (see [Multi-agent coordination](multi-agent-coordination.md)) are useful topologies inside loops, but dispatch → gather → validate is only a pipeline unless the result feeds back into another cycle with a named signal.
- **Explicit stop criteria.** Goal-based and proactive loops work best when "done" is deterministic: tests pass, Lighthouse score clears a threshold, queue is empty, PR merges, or a turn cap is reached. Vague "make it better" loops increase both cost and drift.
- **Compound engineering loop.** For product-building agents, the practical loop is now ideate → brainstorm → plan → work → review → polish → compound → repeat. The agentic middle can be delegated when context and verification are strong; humans spend more time choosing the frame and polishing the outcome.

## Claude Code loop taxonomy

Anthropic's June 30, 2026 "Getting started with loops" post defines a loop as an agent repeating cycles of work until a stop condition is met, and maps four levels onto Claude Code primitives:

| Loop type | Trigger | Stop condition | Claude Code primitive | Best fit |
| --- | --- | --- | --- | --- |
| Turn-based | User prompt | Claude judges the task done or asks for context | Normal prompt + verification skills | Short exploratory tasks |
| Goal-based | Manual prompt in real time | Goal achieved or turn cap hit | `/goal` | Tasks with deterministic exit criteria |
| Time-based | Interval or schedule | Cancelled, or external work completes | `/loop`, `/schedule` | Recurring checks, PR/CI monitoring, scheduled summaries |
| Proactive | Event or schedule, no human present | Each task exits when its goal is met; routine keeps running | `/schedule`, `/goal`, skills, dynamic workflows, auto mode | Recurring streams of well-defined work such as bug reports, triage, migrations, dependency upgrades |

The practical guidance is conservative: start with the simplest loop, define explicit success and stop criteria, pilot before large dynamic-workflow runs, use scripts for deterministic work, and review `/usage`, `/goal`, and `/workflows` token breakdowns to manage cost.

For code quality, Anthropic recommends encoding verification steps as skills, keeping project conventions clean, making docs easy to reach, and using a second agent or `/code-review` skill for review rather than letting the generator fully evaluate its own work.

## Where these patterns surfaced

- Satya Nadella's June 2026 X essay (60M views) frames the loop as the primary product: build a learning loop where human capital and token capital compound, not just pick the best model.
- AINews coined "Loopcraft" (June 2026) to name the paradigm: designing loops that prompt agents rather than prompting agents directly.
- Dhinakaran and Seldo's loop map separates execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops, giving each a different iterated object, exit signal, and human role.
- AI Engineer World's Fair 2026 named the inner-loop/outer-loop split explicitly: Introspection's Roland Gavrilescu frames "autoresearch" as an outer-loop system that studies and maintains a primary inner-loop system; OpenClaw's Peter Steinberger put it plainly — "the agent runs the inner execution loop; I set the direction and I make decisions in the outer loop." A stage debate on whether fully autonomous loops are ready surfaced real disagreement: HumanLayer's Dex Horthy argued "the hype is outrunning the discipline" (loops need to be deterministic, like Kubernetes' control loops, not "frontier thinking"), while Ralph Loop creator Geoffrey Huntley likened the AI engineer's job to a locomotive engineer's: "[We're] kind of like locomotive engineers now. That's our job: to keep the locomotive on the rails."

## Recent changes

- [2026-10-19] Merged the Claude Code loop-taxonomy table (trigger, stop condition, primitive, best fit per loop type) and Anthropic's loop and code-quality guidance from [Claude Code](../tools/claude-code.md); folded the duplicate "where surfaced" bullet into it.
- [2026-09-09] Page created, split out of [Agentic orchestration patterns](agentic-orchestration-patterns.md)'s flat pattern list: loop-first design, loop taxonomy, loop tempo selection, the four-layer loop stack, fresh-context/Ralph loops, the oversight loop, pipeline-vs-loop, explicit stop criteria, and the compound engineering loop.
- [2026-07-14] Added named AI Engineer World's Fair 2026 detail to the loop-engineering pattern: inner/outer loop framing (Introspection, OpenClaw) and the autonomy-readiness stage debate (HumanLayer, Ralph Loop).
- [2026-07-08] Added loop-tempo selection from Andy Matuschak: fast controlled loops and slow delegated loops are easier to sustain than mid-speed partial-control loops.
- [2026-07-04] Dhinakaran and Seldo map loop discourse into execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops; they emphasize exit signals and per-loop autonomy dials.
- [2026-06-30] Anthropic published the official Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops, with guidance on matching loop primitive to task type and controlling token usage.

## Related

- [Agentic orchestration patterns](agentic-orchestration-patterns.md) — context, harness, evaluation, and production patterns; the parent catalog this page split from
- [Multi-agent coordination](multi-agent-coordination.md) — topology patterns for running several agents together, as opposed to designing one agent's loop
- [Harness (agent)](../concepts/harness.md) — the scaffolding a loop runs inside
- [Claude Code](../tools/claude-code.md) — the tool whose `/goal`, `/loop`, `/schedule`, and routines primitives the loop taxonomy maps to

## Sources

- [Loopcraft and agent-native architecture — June 2026 digest](../sources/newsletters/loopcraft-june-2026.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Getting started with loops](../sources/articles/claude-code-getting-started-with-loops-2026-06-30.md)
- [What the hell is a loop, anyway?](../sources/articles/what-the-hell-is-a-loop-anyway.md)
- [Andy Matuschak on coding-agent loop tempo](../sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md)
- [Every - Compound Engineering Gets an Upgrade](../sources/newsletters/every-compound-engineering-upgrade-2026-05.md)
- [5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space](../sources/newsletters/aiewf-2026-five-trends-latentspace.md)
