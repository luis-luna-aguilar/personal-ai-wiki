---
title: Cost-aware agent evaluation
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-28-major-updates-from-openai-and-devin.md
published: 2026-04-28
ingested: 2026-05-05
domains: [agents, coding]
---

# Cost-aware agent evaluation

Three newsletters connect a Google paper and broader evaluation discourse around token spend, run-to-run variance, retry behavior, benchmark instability, and eval costs. The emerging consensus: agent evals that only measure capability or correctness are incomplete if they ignore cost and variance.

## Key claims extracted

- A Google paper discussed in the coverage argues that benchmark instability (variance across runs) is an underappreciated problem in agent evaluation
- Token spend per task is a meaningful evaluation dimension alongside correctness — runaway loops and repeated retries inflate cost without improving results
- Retry behavior specifically matters: how an agent behaves after a failed step (sensible replanning vs. blind retry) affects both cost and reliability
- Eval costs themselves are real: running large agent eval suites repeatedly is expensive, and teams are starting to budget eval token spend explicitly

## Caveats

- Newsletter synthesis; the specific Google paper is not named; find and verify before citing
- Cost thresholds and variance tolerances vary by task type and team budget — no universal number applies

## Influenced pages

- `wiki/training/evals-for-agentic-software-development.md` — cost, variance, and retry evaluation
- `wiki/concepts/agent-evals.md` — cost-aware evaluation dimension
