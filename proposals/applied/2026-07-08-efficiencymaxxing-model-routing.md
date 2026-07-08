---
type: proposal
source: raw/newsletters/2026-07-08-welcome-to-efficiencymaxxing.md
status: pending
created: 2026-07-08
---

# Proposal: Efficiencymaxxing and model-routing discipline

## Summary

Every's "Efficiencymaxxing" turns AI cost control into an operating practice: task decomposition, model routing, evals, stage-level token audits, and one-variable reruns. This updates cost-aware routing and company-wide enablement.

## Intended changes

- [x] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add efficiencymaxxing playbook.
- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add model-routing operating pattern.
- [x] **Create** `wiki/sources/newsletters/efficiencymaxxing-model-routing-2026-07.md` — source summary.

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated sections)

```md
---
title: Cost-aware AI task routing
type: training
domains: [agents, models]
tags: [agentic]
as_of: 2026-07-08
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07]
---

## Current guidance

- Treat "efficiencymaxxing" as routing discipline, not blanket cost cutting: decompose a workflow, decide which steps actually need frontier reasoning, and move stable low-risk steps to cheaper models, scripts, or fine-tuned specialists.
- Run token audits by stage for repeated agent workflows. Ask what each stage used, why it was necessary, and whether the difficulty of the step justifies the spend.
- Change one variable at a time: trim context, rewrite skill instructions, split a step into a subagent, or route a stage to a cheaper model, then rerun and compare quality plus cost.

## Evidence from practice

- **Spiral / OpenRouter routing.** Every reports Spiral uses 12 models through OpenRouter: Sonnet 4.6 for most prose, Gemini 2.5 Flash for a top-edit pass that removes AI tells, and a smaller OpenAI model for file summaries. The reason is not only price: OpenRouter also standardizes provider APIs and provides fallback paths when one provider is unavailable.

## Failure modes

- Calling a workflow "optimized" after reducing token spend without rechecking output quality, human review time, or failure-recovery cost.
- Letting the agent self-assess its own token inefficiency without human review; Every notes models are still poor judges of when their own spend is disproportionate.
```

### wiki/training/company-wide-ai-enablement.md (updated sections)

```md
## Proven patterns

- **Efficiencymaxxing as model-routing practice.** Treat model selection like an operating system for work: use evals to identify which workflow stages can move to cheaper models, audit token use by step, and keep frontier access for ambiguous or high-risk stages. This is the practical middle ground between tokenmaxxing and blanket restriction.

## Recent changes

- [2026-07-08] Added efficiencymaxxing: stage-level model routing, token audits, and one-variable reruns as a company-wide AI cost-control practice.
- [2026-07-01] Added explicit AI strategy bets and token allocation as governance.
```

### wiki/sources/newsletters/efficiencymaxxing-model-routing-2026-07.md (new)

```md
---
title: Efficiencymaxxing and model-routing discipline
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-08-welcome-to-efficiencymaxxing.md
url: https://every.to/context-window/welcome-to-efficiencymaxxing
published: 2026-07-08
ingested: 2026-07-08
domains: [training, agents, models]
---

# Efficiencymaxxing and model-routing discipline

Every's "Welcome to Efficiencymaxxing" argues that teams should route work to the cheapest competent model or tool rather than defaulting every stage to the most expensive frontier model. The piece recommends eval-gated model routing, stage-level token audits, and one-variable reruns to compare cost and output quality.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — adds efficiencymaxxing playbook and Spiral/OpenRouter example.
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — adds model-routing operating pattern.

## Key claims extracted

- Spiral uses 12 models through OpenRouter for different workflow stages.
- OpenRouter provides a standardized API layer and provider fallback in addition to model choice.
- Repeated workflows should be audited by token use per stage.
- The practical test is whether a cheaper route preserves quality and reduces total cost including human review.
```

## Schema / vocabulary additions

None.
