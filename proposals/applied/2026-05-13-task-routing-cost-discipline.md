---
type: proposal
sources:
  - raw/newsletters/2026-05-03-codex-goes-to-work.md
  - raw/newsletters/2026-04-27-you-are-the-most-expensive-model.md
  - raw/newsletters/2026-04-24-model-wars.md
status: pending
created: 2026-05-13
---

# Proposal: Cost discipline shifts to task routing

## Summary

The digest argues that AI cost discipline is shifting from simple token accounting toward routing work among humans, scripts, small models, and frontier models based on risk, determinism, and review cost. This pairs with flat-rate subscription pressure under agent workloads.

## Intended changes

- [x] **Create** `wiki/training/cost-aware-ai-task-routing.md` — practical routing page
    > See draft below

- [x] **Update** `wiki/training/ai-work-delegation-modes.md` — cross-link cost/routing
    > Add to Proven patterns: `Route by determinism and risk: scripts for deterministic transformations, small models for cheap classification or drafting, frontier models for ambiguous synthesis, and humans for intent, taste, and accountability.`

- [x] **Create** `wiki/sources/newsletters/task-routing-cost-discipline-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (new)

```markdown
---
title: Cost-aware AI task routing
type: training
domains: [agents, models]
tags: [agentic]
as_of: 2026-05-13
sources: [task-routing-cost-discipline-2026-05-13]
---

# Cost-aware AI task routing

AI cost discipline is moving from token counting to routing work to the cheapest competent executor: deterministic code, small models, frontier models, agents, or humans. The goal is not to minimize model spend in isolation, but to minimize total task cost, including human review and failure recovery.

## Current guidance

- Use scripts for deterministic transformations and validations.
- Use smaller models for cheap classification, extraction, first drafts, and low-risk routing.
- Use frontier models for ambiguous synthesis, high-stakes reasoning, and tasks where failure is expensive.
- Use humans for intent, taste, accountability, exceptions, and final review on consequential work.

## Failure modes

- Spending frontier-model tokens on work a script could do exactly.
- Saving model cost while increasing human review burden.
- Letting flat-rate subscriptions hide runaway agent workloads until pricing or limits change.

## Sources

- [Task routing and cost discipline — May 2026](../sources/newsletters/task-routing-cost-discipline-2026-05-13.md)
```

### wiki/sources/newsletters/task-routing-cost-discipline-2026-05-13.md (new)

```markdown
---
title: Task routing and cost discipline — May 2026
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-27-you-are-the-most-expensive-model.md
published: 2026-04-27
ingested: 2026-05-13
domains: [agents, models]
---

# Task routing and cost discipline — May 2026

The batch argues for routing work among frontier models, smaller models, deterministic scripts, and humans based on risk and determinism. Related model-wars coverage says flat-rate subscriptions are strained by agent workloads, pushing providers toward usage-based pricing.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md)
- [AI work delegation modes](../../training/ai-work-delegation-modes.md)

## Key claims extracted

- Humans are often the most expensive executor and should focus on intent, review, and accountability.
- Deterministic steps should be handled by code where possible.
- Agent workloads make cost more about task routing than prompt token budgeting alone.
```

