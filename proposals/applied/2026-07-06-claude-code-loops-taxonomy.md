---
type: proposal
source: raw/articles/2026-07-06-claudecom-blog-getting-started-with-loops.md
status: pending
created: 2026-07-06
---

# Proposal: Claude Code loop taxonomy

## Summary

Anthropic's Claude Code team published an official taxonomy for agentic loops: turn-based, goal-based, time-based, and proactive. The useful wiki update is to convert existing scattered Claude Code loop primitives (`/goal`, `/loop`, `/schedule`, dynamic workflows, skills, auto mode) into a clearer operating model with explicit trigger, stop condition, primitive, task fit, and token-management guidance.

The original X post was only a pointer to the official article, so this proposal uses the Claude blog post as the substantive source.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` - add the official loop taxonomy and token-management guidance.
    > **Before:** Claude Code lists `/goal`, `/loop`, routines, and dynamic workflows separately.
    > **After:** Claude Code explains how those primitives compose into turn-based, goal-based, time-based, and proactive loops.

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` - refine "loop-first design" with Anthropic's official four-loop taxonomy.

- [x] **Update** `wiki/state-of/coding.md` - add a recent-change note that Claude Code now has an official loop taxonomy for matching task type to loop primitive.

- [x] **Create** `wiki/sources/articles/claude-code-getting-started-with-loops-2026-06-30.md` - source summary.

## Page drafts

### wiki/tools/claude-code.md (updated snippet)

```md
## Loop taxonomy

Anthropic's June 30, 2026 "Getting started with loops" post defines a loop as an agent repeating cycles of work until a stop condition is met. The Claude Code team frames four levels:

| Loop type | Trigger | Stop condition | Claude Code primitive | Best fit |
| --- | --- | --- | --- | --- |
| Turn-based | User prompt | Claude judges the task done or asks for context | Normal prompt + verification skills | Short exploratory tasks |
| Goal-based | Manual prompt in real time | Goal achieved or turn cap hit | `/goal` | Tasks with deterministic exit criteria |
| Time-based | Interval or schedule | Cancelled, or external work completes | `/loop`, `/schedule` | Recurring checks, PR/CI monitoring, scheduled summaries |
| Proactive | Event or schedule, no human present | Each task exits when its goal is met; routine keeps running | `/schedule`, `/goal`, skills, dynamic workflows, auto mode | Recurring streams of well-defined work such as bug reports, triage, migrations, dependency upgrades |

The practical guidance is conservative: start with the simplest loop, define explicit success and stop criteria, pilot before large dynamic-workflow runs, use scripts for deterministic work, and review `/usage`, `/goal`, and `/workflows` token breakdowns to manage cost.

For code quality, Anthropic recommends encoding verification steps as skills, keeping project conventions clean, making docs easy to reach, and using a second agent or `/code-review` skill for review rather than letting the generator fully evaluate its own work.

## Recent changes
- [2026-06-30] Anthropic published the official Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops, with guidance on matching loop primitive to task type and controlling token usage.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated snippet)

```md
- **Loop taxonomy before loop complexity.** Anthropic's Claude Code team defines loops as agents repeating cycles of work until a stop condition is met, then separates four levels: turn-based loops hand off the check, goal-based loops hand off the stop condition, time-based loops hand off the trigger, and proactive loops hand off the prompt for recurring well-defined work. Use the lightest loop that fits the task.
- **Explicit stop criteria.** Goal-based and proactive loops work best when "done" is deterministic: tests pass, Lighthouse score clears a threshold, queue is empty, PR merges, or a turn cap is reached. Vague "make it better" loops increase both cost and drift.
- **Cost-aware loop primitives.** Use scripts for deterministic work, run small pilots before dynamic workflows that may spawn many agents, choose cheaper/faster models for routine parts, and monitor `/usage`, `/goal`, and `/workflows` breakdowns.
```

### wiki/state-of/coding.md (updated snippet)

```md
## Recent changes
- [2026-06-30] Anthropic published a Claude Code loop taxonomy tying task type to primitives: turn-based prompts, `/goal`, `/loop` or `/schedule`, and proactive routines composed with skills, dynamic workflows, and auto mode.
```

### wiki/sources/articles/claude-code-getting-started-with-loops-2026-06-30.md (new)

```md
---
title: Getting started with loops
type: source
source_type: article
source_file: raw/articles/2026-07-06-claudecom-blog-getting-started-with-loops.md
url: https://claude.com/blog/getting-started-with-loops
published: 2026-06-30
ingested: 2026-07-06
domains: [coding, agents]
---

# Getting started with loops

Anthropic's Claude Code team defines agentic loops as agents repeating cycles of work until a stop condition is met, then classifies Claude Code loops into turn-based, goal-based, time-based, and proactive patterns.

## Influenced pages
- [Claude Code](../../tools/claude-code.md) - official loop taxonomy and token-management guidance
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) - loop taxonomy, stop criteria, and cost-aware loop primitives
- [State of Coding](../../state-of/coding.md) - recent-change note for Claude Code's loop taxonomy

## Key claims extracted
- Turn-based loops are normal prompt-driven agentic loops where the human keeps directing each turn.
- Goal-based loops use `/goal` and work best when success criteria are deterministic and bounded by turn caps.
- Time-based loops use `/loop` locally or `/schedule` in routines for recurring checks and external-system monitoring.
- Proactive loops compose `/schedule`, `/goal`, skills, dynamic workflows, and auto mode for recurring well-defined work.
- Loops should start simple, use explicit success/stop criteria, pilot before large runs, route routine work to cheaper models where possible, and use scripts for deterministic steps.
```

## Schema / vocabulary additions

None.

## Open questions

- The article is official but the raw fetch did not capture the page's visible metadata block; the source date comes from the article page/search result and should be preserved as `published: 2026-06-30`.
	- Yeah, keep that one.
