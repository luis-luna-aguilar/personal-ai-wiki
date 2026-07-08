---
type: proposal
source: raw/newsletters/2026-07-07-use-fable-before-you-know-what-to-ask.md
status: pending
created: 2026-07-08
---

# Proposal: Fable for unknowns, cheaper specialists for settled work

## Summary

Every's "Use Fable Before You Know What to Ask" gives a practical routing heuristic: use Fable when the assignment itself may be wrong or incomplete; use cheaper models or tuned specialists when the goal and evaluation are settled.

## Intended changes

- [x] **Update** `wiki/models/claude-fable-5.md` — add practical use-case niche.
- [x] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add uncertainty-based routing heuristic.
- [x] **Create** `wiki/sources/newsletters/fable-unknowns-routing-2026-07.md` — source summary.

## Page drafts

### wiki/models/claude-fable-5.md (updated sections)

```md
## What Fable 5 is best used for

Every's July 2026 guidance sharpens Fable's practical niche: do not reserve it only for the biggest tasks by size. Reserve it for tasks where the assignment may be incomplete, the standard is unstated, or the target itself may be wrong.

- Use Fable to surface "unknown knowns": criteria obvious to the user but not written in the prompt.
- Use Fable to surface "unknown unknowns": questions or invalid premises the user has not considered.
- Use cheaper models when the goal, constraints, and definition of good are already settled.
- Use Fable to turn a hard recurring job into scripts, skills, examples, and quality checks that cheaper models can execute later.

## Recent changes

- [2026-07-07] Every frames Fable's premium use case as finding unknowns and invalid premises before execution, then converting recurring work into cheaper-model instructions and scripts.
- [2026-07-02] Fable 5 returned online; Anthropic added visible safety fallback routing to Opus 4.8 for some sensitive domains; major coding tools restored access.
```

### wiki/training/cost-aware-ai-task-routing.md (updated sections)

```md
## Current guidance

- Route by uncertainty, not only by task size. Use frontier models like Fable when the prompt, standard, or premise may be wrong; route settled, repeatable work to cheaper models, scripts, or task-specific fine-tunes.

## Evidence from practice

- **Fable for unknowns.** Every reports using Fable to find missing questions, hidden standards, and invalid targets before execution. In one workflow, Fable diagnosed that a copy-editing target was unvalidated; in another, it turned a video-clipping job into scripts and instructions that a cheaper model could reuse.

## Related

- [Claude Fable 5](../models/claude-fable-5.md) — frontier model whose practical niche is ambiguous or premise-risky work, not every large task.
```

### wiki/sources/newsletters/fable-unknowns-routing-2026-07.md (new)

```md
---
title: Fable for unknowns and cheaper specialists for settled work
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-07-use-fable-before-you-know-what-to-ask.md
url: https://every.to/context-window/use-fable-before-you-know-what-to-ask
published: 2026-07-07
ingested: 2026-07-08
domains: [models, training]
tags: [anthropic]
---

# Fable for unknowns and cheaper specialists for settled work

Every argues that Fable is most worth using when the assignment itself may be incomplete: hidden standards, missing questions, invalid assumptions, or unsettled definitions of quality. The article contrasts this with cheaper specialist models, which can win on repeated, well-defined work.

## Influenced pages

- [Claude Fable 5](../../models/claude-fable-5.md) — adds practical use-case niche.
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — adds uncertainty-based routing.

## Key claims extracted

- Fable is useful for surfacing "unknown knowns" and "unknown unknowns."
- Every used Fable to find an unvalidated copy-editing target after weeks of work.
- Every used Fable to turn a failed recurring video-clipping workflow into scripts and instructions for cheaper future runs.
- Bridgewater AIA Labs / Thinking Machines fine-tuned Qwen3-235B to outperform tested frontier models on six financial tasks at 13.8x lower inference cost.
```

## Schema / vocabulary additions

None.
