---
type: proposal
sources:
  - raw/newsletters/2026-07-01-autoresearch-the-feedback-loop-behind-self-improv.md
  - raw/newsletters/2026-06-30-ainews-not-much-happened-today.md
status: pending
created: 2026-07-06
---

# Proposal: Autoresearch and agent recipes

## Summary
The Introspection interview frames autoresearch as an outer loop that improves an agent system through traces, evals, judges, human signals, and cost controls. The "agent recipe" concept packages harnesses, models, evals, judge logic, expertise, and failure history into a portable operating unit for agent improvement.

## Intended changes

- [x] **Update** `wiki/concepts/agent-improvement-loop.md` — add autoresearch as an outer-loop pattern.
    > **Add:** Autoresearch treats the agent system itself as the research subject: agents inspect traces, failures, eval results, and human feedback to propose improvements under cost and governance controls.

- [x] **Update** `wiki/concepts/harness.md` — add "agent recipe" as a harness packaging pattern.
    > **Add:** Agent recipe — a portable bundle of harness, model choices, evals, judges, captured human expertise, failure history, and signal-processing logic.

- [x] **Update** `wiki/concepts/agent-evals.md` — add note that humans often supply early high-value signals before automated judges stabilize.

- [x] **Update** `wiki/training/agent-skill-methodology.md` — connect reusable skills/recipes to auditability and Git-based change history.

- [x] **Create** `wiki/sources/newsletters/autoresearch-agent-recipes-2026-07.md` — source summary.

## Updated Page Snippets

### `wiki/concepts/agent-improvement-loop.md`

> **Before:**
> `A workflow for improving AI agents by studying execution traces: records of what the agent actually did during a run, including model calls, tool calls, intermediate steps, and outputs.`

> **After:**
> `A workflow for improving AI agents by studying execution traces and feedback signals: records of what the agent actually did during a run, eval results, human review, cost data, and recurring failure patterns. Autoresearch extends this into an outer loop where agents study and maintain the primary agent system itself.`

### `wiki/concepts/harness.md`

> **Before:**
> `- **Reusable operating modules** — skills, hook scripts, slash commands, and plugin bundles increasingly act as composable pieces of the harness, not just ad hoc project artifacts`

> **After:**
> `- **Reusable operating modules** — skills, hook scripts, slash commands, plugin bundles, and agent recipes increasingly act as composable pieces of the harness, not just ad hoc project artifacts. An agent recipe packages the harness, model choices, evals, judges, human expertise, failure history, and signal-processing logic needed to reproduce an agent workflow.`

### `wiki/concepts/agent-evals.md`

> **Before:**
> `- **Online (production)** — asynchronous scoring of live traffic to detect quality degradation, cost explosions, or latency spikes before users notice.`

> **After:**
> `- **Online (production)** — asynchronous scoring of live traffic to detect quality degradation, cost explosions, or latency spikes before users notice. In early autoresearch loops, human feedback often supplies the highest-value signal before automated judges are stable enough to trust.`

### `wiki/training/agent-skill-methodology.md`

> **Before:**
> `- Treat skills as portable operating knowledge, not only prompt snippets.`

> **After:**
> `- Treat skills and recipes as portable operating knowledge, not only prompt snippets. Durable agent behavior should carry instructions, references, eval cases, failure history, and audit-friendly change history rather than living only in a chat transcript.`

## Page Drafts

### `wiki/sources/newsletters/autoresearch-agent-recipes-2026-07.md` (new)

```md
---
title: Autoresearch and agent recipes
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-01-autoresearch-the-feedback-loop-behind-self-improv.md
published: 2026-07-01
ingested: 2026-07-06
domains: [agents, training]
---

# Autoresearch and agent recipes

Roland Gavrilescu describes autoresearch as an outer loop for improving agent systems: agents study traces, evals, failures, human feedback, and cost signals to maintain the primary system. The source introduces "agent recipes" as portable bundles that include harnesses, models, evals, judges, human expertise, failure history, and signal-processing logic.

## Influenced pages
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — autoresearch outer loop
- [Harness](../../concepts/harness.md) — agent recipe packaging pattern
- [Agent evals](../../concepts/agent-evals.md) — human signal as early eval source
- [Agent skill methodology](../../training/agent-skill-methodology.md) — reusable recipe/skill framing

## Key claims extracted
- Autoresearch makes agent improvement a continuous loop around the primary agent system.
- Recipes package the operational ingredients needed to reproduce or transfer an agent workflow.
- Provider-agnostic infrastructure, audit logs, secure deployment, and human feedback are central constraints.
```
