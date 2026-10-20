---
title: Claude Sonnet 5.5 launch
type: source
source_type: article
source_file: raw/articles/2026-10-20-anthropiccom-claude-sonnet-5-5.md
url: https://www.anthropic.com/claude-sonnet-5-5
ingested: 2026-10-20
domains: [models, coding]
---

# Claude Sonnet 5.5 launch

Anthropic's launch post for Claude Sonnet 5.5, the second Claude 5.5 model. Anthropic presents it as a clear upgrade on Sonnet 5 at the same token price, 30%+ faster and up to 30% cheaper per task, and as the faster, lower-cost complement to Opus 5.5. It includes a benchmark table against Sonnet 5, Opus 5.5 and GPT-6 Sol, pricing, about fifteen customer quotes, and safety notes. The post carries no publication date; it says Haiku 5.5 "will join the Claude 5.5 family in the coming weeks," so it predates Haiku 5.5. The ingest date (2026-10-20) is used. The fetched page already shows the $0.10 cache-read price that the Haiku 5.5 launch announced as a cut.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — new page: pricing, benchmarks, safeguards, availability
- [Claude Sonnet 5](../../history/models/claude-sonnet-5.md) — archived as superseded
- [State of Models](../../state-of/models.md) — Sonnet 5.5 replaces Sonnet 5 in Frontier models

## Key claims extracted
- Available on all platforms (AWS, Google Cloud, Microsoft Azure) and on the Claude Platform as `claude-sonnet-5-5`; thinking-off users must switch to the new `between_tools` setting.
- Pricing per 1M tokens: input $2, output $10, cache writes $2.50, cache reads $0.10 (half Sonnet 5's $0.20). Up to 30% cheaper per task than Sonnet 5; output 30%+ faster.
- Benchmarks (Sonnet 5.5 / Sonnet 5 / Opus 5.5 / GPT-6 Sol): Terminal-Bench 4.0 70.6 / 10.3 / 66.4 / —; FrontierCode 1.1 46.2 (max) or 52.1 (xhigh) / 42.4 / 54.4 / 49.3; CursorBench 4.0 55.5 / 34.1 / 57.8 / —; GDPval-AA v2.1 1844 / 1449 / 1846 / 1487; AA-Briefcase v1.1 1811 / 1359 / 1822 / 1483; HLE with tools 64.5 / 54.9 / 67.7; OSWorld 2.1 80.1 / 57.0 / 81.8; Chartography 61.6 / 15.6 / 64.4 / 53.6.
- At Low or Medium effort it beats Sonnet 5's best score on several benchmarks at about a tenth of the cost per task. First Sonnet to beat Pokémon Red from screenshots alone.
- Opus 5.5 remains clearly stronger at complex, open-ended work requiring sustained judgment.
- Default effort is Medium in Claude Code and the apps, High on the Claude Platform.
- Customer reports: Base44 matched Opus 5 in 3.6 iterations per build against 7.7; Balyasny about 121k tokens per answer against Sonnet 5's 497k; Zendesk tickets processed 20% faster; Box 2.4x faster with 12% fewer tokens.
- Safety: matches or improves on Sonnet 5 on most alignment measures; first Sonnet with Opus-class cyber safeguards (higher-risk cyber tasks fall back to Sonnet 5) and anti-distillation classifiers; biology safeguards same as Sonnet 5.
