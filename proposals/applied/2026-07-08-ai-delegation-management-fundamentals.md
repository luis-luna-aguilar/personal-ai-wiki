---
type: proposal
source: raw/articles/2026-07-08-oneusefulthingorg-p-management-as-ai-superpower.md
status: pending
created: 2026-07-08
---

# Proposal: AI delegation as management fundamentals

## Summary

Ethan Mollick's "Management as AI superpower" and Andy Matuschak's agent-loop tweet converge on a useful training page update: working well with agents is management, not prompt cleverness. The key variables are task value, success probability, review cost, delegation documents, and loop tempo.

## Intended changes

- [x] **Create** `wiki/training/ai-delegation-management.md` — practical training page.
- [x] **Update** `wiki/index.md` — add the new training page.
- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add loop-tempo guidance.
- [x] **Create** `wiki/sources/articles/management-as-ai-superpower-2026-07.md` — source summary.
- [x] **Create** `wiki/sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md` — source summary.

## Page drafts

### wiki/training/ai-delegation-management.md (new)

```md
---
title: AI delegation management
type: training
domains: [agents, training]
tags: [agentic]
as_of: 2026-07-08
sources: [management-as-ai-superpower-2026-07, andy-matuschak-agent-loop-tempo-2026-07]
---

# AI delegation management

Working with agents is increasingly a management skill: define the job, explain what good looks like, bound the agent's authority, and review outcomes without losing the mental model needed to steer the next round.

## Current guidance

- Delegate when the human baseline time is high enough to justify prompt, wait, and review overhead.
- Estimate probability of success before delegating. If the agent has a low chance of meeting the bar and review is expensive, doing the task yourself may still be faster.
- Write delegation documents like managers already do: purpose, constraints, authority limits, deliverables, interim checkpoints, and definition of done.
- Match loop tempo to the work. Fast 1-2 minute loops keep the human in control; slow delegated loops work when the human can ignore details until checkpoints. Mid-speed 10-30 minute loops can create context switching and comprehension loss.

## Proven patterns

- Use domain expertise to explain the output standard and catch subtle failures.
- Convert repeated delegation into templates, checklists, or skills once the first few runs are stable.
- Ask for interim evidence when the cost of a wrong direction is high.

## Failure modes

- Delegating vague work where the desired output is specific but unstated.
- Creating partial-control loops where the human is responsible for planning and review but cannot keep enough context in working memory.
- Treating speed as success when review and correction consume the saved time.

## Sources

- [Management as AI superpower](../sources/articles/management-as-ai-superpower-2026-07.md)
- [Andy Matuschak on agent loop tempo](../sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md)
```

### wiki/index.md (updated line)

```md
- [training/ai-delegation-management](training/ai-delegation-management.md) — practical guidance for delegating work to agents using management fundamentals: scope, authority, loop tempo, review cost, and definition of done *(as_of: 2026-07-08)*
```

### wiki/workflows/agentic-orchestration-patterns.md (updated sections)

```md
## Current patterns

- **Loop tempo selection.** Choose between close fast loops and slow delegated loops deliberately. Fast 1-2 minute loops preserve human control and comprehension; slow delegated loops work when the agent can proceed in the background with sparse checkpoints. The middle ground can be costly: 10-30 minute cycles often force parallelism, context switching, and weak comprehension.

## Failure modes

- **Partial-control loop churn.** The human tries to delegate more than a fast pair-programming loop but still remains responsible for planning, technical guidance, and review. The result can be multiple half-understood agent threads rather than real leverage.

## Recent changes

- [2026-07-08] Added loop-tempo selection from Andy Matuschak: fast controlled loops and slow delegated loops are easier to sustain than mid-speed partial-control loops.
- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.
```

### wiki/sources/articles/management-as-ai-superpower-2026-07.md (new)

```md
---
title: Management as AI superpower
type: source
source_type: article
source_file: raw/articles/2026-07-08-oneusefulthingorg-p-management-as-ai-superpower.md
url: https://www.oneusefulthing.org/p/management-as-ai-superpower
published: 2026-06-19
ingested: 2026-07-08
domains: [agents, training]
---

# Management as AI superpower

Ethan Mollick argues that as AI makes execution faster and cheaper, management fundamentals become more valuable: scoping work, defining standards, delegating clearly, and evaluating outputs. His experimental class had executive MBA students build startup prototypes and supporting business artifacts in four days using Claude Code, Google Antigravity, ChatGPT, Claude, and Gemini.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — creates delegation framework.

## Key claims extracted

- Students with little coding experience built working prototypes plus market research, positioning, pitches, and financial models in four days.
- Delegation to AI depends on human baseline time, probability of success, and AI process/review time.
- Good AI delegation documents resemble management artifacts: goal, authority limits, outputs, interim progress, and checks before completion.
- The scarce skill becomes knowing what to ask for and what good looks like.
```

### wiki/sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md (new)

```md
---
title: Andy Matuschak on coding-agent loop tempo
type: source
source_type: tweet
source_file: raw/tweets/2026-07-08-andy_matuschak-2068374510332477469.md
url: https://x.com/andy_matuschak/status/2068374510332477469
published: 2026-06-20
ingested: 2026-07-08
domains: [coding, agents, training]
---

# Andy Matuschak on coding-agent loop tempo

Andy Matuschak describes two agent-use modes that seem to make heavy users happiest: fast controlled loops where the human stays in full control, and slow delegated loops where agents work in the background with sparse attention. He reports struggling with the middle ground because 10-30 minute cycles create parallelism, context switching, and poor comprehension.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — adds loop tempo guidance.
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — adds partial-control loop failure mode.

## Key claims extracted

- Fast controlled loops are 1-2 minute cycles where the agent mostly helps the human type faster.
- Slow delegated loops are background work checked a few times a day.
- The middle ground can create fragmentation where neither human nor agents understand the whole state.
```

## Schema / vocabulary additions

None.
