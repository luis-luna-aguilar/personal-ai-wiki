---
title: Cost-aware AI task routing
type: training
domains: [agents, models]
tags: [agentic]
as_of: 2026-07-02
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02]
---

# Cost-aware AI task routing

AI cost discipline is moving from token counting to routing work to the cheapest competent executor: deterministic code, small models, frontier models, agents, or humans. The goal is not to minimize model spend in isolation, but to minimize total task cost, including human review and failure recovery.

## Current guidance

- Use scripts for deterministic transformations and validations.
- Use smaller models for cheap classification, extraction, first drafts, and low-risk routing.
- Use frontier models for ambiguous synthesis, high-stakes reasoning, and tasks where failure is expensive.
- Use humans for intent, taste, accountability, exceptions, and final review on consequential work.
- When a task has repeated domain-specific judgment and stable evaluation examples, compare three routes before defaulting to frontier models: expert prompt on a frontier model, expert prompt on a cheaper strong model, and fine-tuned/open-weight model with task-specific examples.

## Evidence from practice

- **Bridgewater / Thinking Machines finance case.** Thinking Machines reports that Bridgewater AIA Labs used expert-labeled data to train a Qwen3-235B model for six investor information-filtering tasks. Frontier models with naive prompts averaged roughly 50% accuracy; expert prompts raised them to the mid-70s; the final trained model improved from 78.2% to 84.7%, made 29.8% fewer mistakes than the best frontier model evaluated, and reduced inference cost per task by 13.8x. The routing lesson is durable: for repeated expert-judgment tasks, domain examples and smaller tuned models can beat generic frontier defaults on both quality and cost.

## Failure modes

- Spending frontier-model tokens on work a script could do exactly.
- Saving model cost while increasing human review burden.
- Letting flat-rate subscriptions hide runaway agent workloads until pricing or limits change.
- Treating model prestige as a routing rule. The Bridgewater case suggests expert data and task-specific tuning can matter more than using the newest frontier model.

## Related

- [AI work delegation modes](ai-work-delegation-modes.md) - task-shape framework for choosing autonomous delegation versus close collaboration.
- [Flex processing](../workflows/flex-processing.md) - lower-cost asynchronous execution for non-urgent OpenAI workloads.

## Sources

- [Task routing and cost discipline - May 2026](../sources/newsletters/task-routing-cost-discipline-2026-05-13.md)
- [Thinking Machines - Learning to Replicate Expert Judgment in Financial Tasks](../sources/articles/thinking-machines-financial-expert-judgment-2026-07-02.md)
- [Superhuman - A $5B startup emerges from stealth](../sources/newsletters/superhuman-bridgewater-thinking-machines-2026-07-02.md)
