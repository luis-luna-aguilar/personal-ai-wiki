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

## Related

- [AI work delegation modes](ai-work-delegation-modes.md) - task-shape framework for choosing autonomous delegation versus close collaboration.
- [Flex processing](../workflows/flex-processing.md) - lower-cost asynchronous execution for non-urgent OpenAI workloads.

## Sources

- [Task routing and cost discipline - May 2026](../sources/newsletters/task-routing-cost-discipline-2026-05-13.md)
