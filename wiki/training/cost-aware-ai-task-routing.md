---
title: Cost-aware AI task routing
type: training
domains: [agents, models]
tags: [agentic]
as_of: 2026-07-08
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07]
---

# Cost-aware AI task routing

AI cost discipline is moving from token counting to routing work to the cheapest competent executor: deterministic code, small models, frontier models, agents, or humans. The goal is not to minimize model spend in isolation, but to minimize total task cost, including human review and failure recovery.

## Current guidance

- Use scripts for deterministic transformations and validations.
- Use smaller, local, or open-weight models for cheap classification, extraction, first drafts, private/low-latency processing, and low-risk routing; reserve frontier calls for ambiguous synthesis or high-stakes decisions.
- Use frontier models for ambiguous synthesis, high-stakes reasoning, and tasks where failure is expensive.
- Use humans for intent, taste, accountability, exceptions, and final review on consequential work.
- When a task has repeated domain-specific judgment and stable evaluation examples, compare three routes before defaulting to frontier models: expert prompt on a frontier model, expert prompt on a cheaper strong model, and fine-tuned/open-weight model with task-specific examples.
- Route by uncertainty, not only by task size. Use frontier models like Fable when the prompt, standard, or premise may be wrong; route settled, repeatable work to cheaper models, scripts, or task-specific fine-tunes.
- Treat "efficiencymaxxing" as routing discipline, not blanket cost cutting: decompose a workflow, decide which steps actually need frontier reasoning, and move stable low-risk steps to cheaper models, scripts, or fine-tuned specialists.
- Run token audits by stage for repeated agent workflows. Ask what each stage used, why it was necessary, and whether the difficulty of the step justifies the spend.
- Change one variable at a time: trim context, rewrite skill instructions, split a step into a subagent, or route a stage to a cheaper model, then rerun and compare quality plus cost.

## Evidence from practice

- **Bridgewater / Thinking Machines finance case.** Thinking Machines reports that Bridgewater AIA Labs used expert-labeled data to train a Qwen3-235B model for six investor information-filtering tasks. Frontier models with naive prompts averaged roughly 50% accuracy; expert prompts raised them to the mid-70s; the final trained model improved from 78.2% to 84.7%, made 29.8% fewer mistakes than the best frontier model evaluated, and reduced inference cost per task by 13.8x. The routing lesson is durable: for repeated expert-judgment tasks, domain examples and smaller tuned models can beat generic frontier defaults on both quality and cost.
- **Spiral / OpenRouter routing.** Every reports Spiral uses 12 models through OpenRouter: Sonnet 4.6 for most prose, Gemini 2.5 Flash for a top-edit pass that removes AI tells, and a smaller OpenAI model for file summaries. The reason is not only price: OpenRouter also standardizes provider APIs and provides fallback paths when one provider is unavailable.
- **Fable for unknowns.** Every reports using Fable to find missing questions, hidden standards, and invalid targets before execution. In one workflow, Fable diagnosed that a copy-editing target was unvalidated; in another, it turned a video-clipping job into scripts and instructions that a cheaper model could reuse.

## AI FinOps controls

AI cost discipline is becoming an operating function, not just a prompt-writing habit. Practical controls include:

- Set token budgets by role, team, workflow, or risk tier.
- Reserve frontier or heavy-reasoning models for work where cheaper models, scripts, or humans are not sufficient.
- Require opt-in approval for long-running or high-effort agent modes.
- Track cache hit rates, prompt reuse, context length, and cost per successful task.
- Use cheaper defaults, model routing, warm-cache reuse, and lean context before restricting useful adoption.
- Measure shipped outcomes and human review burden, not raw token volume.

## Failure modes

- Spending frontier-model tokens on work a script could do exactly.
- Saving model cost while increasing human review burden.
- Letting flat-rate subscriptions hide runaway agent workloads until pricing or limits change.
- Treating model prestige as a routing rule. The Bridgewater case suggests expert data and task-specific tuning can matter more than using the newest frontier model.
- Treating local AI as just a model download. Local/open routing needs surrounding infrastructure: search, documents, agents, harnesses, deployment tooling, and clear escalation to frontier models when needed.
- Cutting model spend in a way that increases hidden human review cost.
- Treating token volume as adoption success after the organization has moved into a per-token or usage-based pricing regime.
- Calling a workflow "optimized" after reducing token spend without rechecking output quality, human review time, or failure-recovery cost.
- Letting the agent self-assess its own token inefficiency without human review; Every notes models are still poor judges of when their own spend is disproportionate.

## Related

- [AI work delegation modes](ai-work-delegation-modes.md) - task-shape framework for choosing autonomous delegation versus close collaboration.
- [Flex processing](../workflows/flex-processing.md) - lower-cost asynchronous execution for non-urgent OpenAI workloads.
- [Claude Fable 5](../models/claude-fable-5.md) - frontier model whose practical niche is ambiguous or premise-risky work, not every large task.

## Sources

- [Task routing and cost discipline - May 2026](../sources/newsletters/task-routing-cost-discipline-2026-05-13.md)
- [Thinking Machines - Learning to Replicate Expert Judgment in Financial Tasks](../sources/articles/thinking-machines-financial-expert-judgment-2026-07-02.md)
- [Superhuman - A $5B startup emerges from stealth](../sources/newsletters/superhuman-bridgewater-thinking-machines-2026-07-02.md)
- [Local AI as open-weight infrastructure](../sources/newsletters/local-ai-infrastructure-2026-06.md)
- [Token tightening and AI FinOps](../sources/newsletters/token-tightening-ai-finops-2026-06.md)
- [Efficiencymaxxing and model-routing discipline](../sources/newsletters/efficiencymaxxing-model-routing-2026-07.md)
- [Fable for unknowns and cheaper specialists for settled work](../sources/newsletters/fable-unknowns-routing-2026-07.md)
