---
title: "Artificial Analysis — HealthBench and HealthBench Professional leaderboards"
type: source
source_type: article
source_file: raw/articles/2026-11-24-artificialanalysisai-evaluations-healthbench.md
url: https://artificialanalysis.ai/evaluations/healthbench
ingested: 2026-11-24
domains: [healthcare]
---

# Artificial Analysis — HealthBench and HealthBench Professional leaderboards

Artificial Analysis' independent leaderboards for OpenAI's HealthBench (5,000 general health conversations) and HealthBench Professional (525 clinician conversations), graded against physician-written rubrics with OpenAI's judge model. Each model gets a raw and a length-adjusted score. The page has no publication date; it was read on 2026-11-24. The Professional tab is in the raw file above; the general-set tab was captured separately at `raw/articles/2026-11-24-artificialanalysisai-evaluations-healthbench-general.md`.

## Influenced pages

- [HealthBench](../../benchmarks/healthbench.md) — new page: scoring method, current results for both sets
- [State of Healthcare](../../state-of/healthcare.md) — new Medical-knowledge benchmarks subcategory

## Key claims extracted

- Rubric criteria worth −10 to +10 points; judge GPT-5.4 (low), as in OpenAI's implementation; four repeats per task
- Length adjustment penalises replies over 2,000 characters and raises shorter ones; reasoning excluded from length
- HealthBench (length-adjusted): Claude Sonnet 5.5 62.1%, DeepSeek V4.1 Flash 60.9%, Claude Fable 5.2 59.6%, GPT-6.2 Astra 53.5%
- Headline: Claude Fable 5.2 (xhigh) scores highest on HealthBench Professional at 68.1%
- HealthBench Professional (length-adjusted, max-effort rows): Claude Fable 5.2 67.7%, Claude Sonnet 5.5 63.0%, GPT-6 Luna 61.9%, Claude Opus 5.5 59.9%
- Cheapest Professional run: GPT-6 Luna at $0.0041 per task
