---
title: Devin Fusion — Frontier Performance at 35% Lower Cost
type: source
source_type: article
source_file: raw/articles/2026-07-14-cognitioncom-blog-devin-fusion.md
url: https://cognition.com/blog/devin-fusion
published: 2026-06-29
ingested: 2026-07-14
domains: [coding, agents]
---

# Devin Fusion — Frontier Performance at 35% Lower Cost

Cognition introduces Devin Fusion, a multi-model "sidekick" harness: a frontier model and a cheaper sidekick model each run as full agents with their own tools and persistent, separately-cached context; the frontier model plans and reviews while delegating mechanical work to the sidekick, and a classifier can dynamically reassign which model leads mid-session, timed to coincide with context-compaction boundaries to avoid extra cache-miss cost. On the new FrontierCode Extended benchmark, Fusion matches frontier performance at 35% lower cost than Opus 4.8/GPT-5.5 alone (41% lower with Fable 5, measured pre-suspension). Internally, 88% of Cognition's merged PRs were driven entirely by the automated Fusion router. Preview available at app.devin.ai/signup. Published 2026-06-29.

## Influenced pages

- [Devin](../../tools/devin.md) — Devin Fusion feature detail
- [FrontierCode](../../benchmarks/frontiercode.md) — new FrontierCode Extended tier scores/costs
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — new Sidekick multi-model harness pattern
- [Advisor strategy](../../workflows/advisor-strategy.md) — contrast with per-call cache-miss cost
- [State of Coding](../../state-of/coding.md) — Devin added to Terminal coding agent subcategory

## Key claims extracted

- Devin Fusion: two parallel agents (frontier + cheaper "sidekick"), each with its own persistent, separately-cached context; frontier model plans/reviews, delegates mechanical work.
- Dynamic mid-session routing switches models at context-compaction boundaries specifically to avoid paying an extra cache-miss cost.
- On FrontierCode Extended: Fusion matches frontier performance at 35% lower cost vs. Opus 4.8/GPT-5.5; 41% lower cost with Fable 5 (internal, pre-suspension measurement).
- 88% of Cognition's internal merged PRs were driven entirely by the automated Fusion router.
- Published 2026-06-29; preview available at app.devin.ai/signup.
