---
title: Claude Sonnet 5.5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic]
as_of: 2026-10-20
sources: [claude-sonnet-5-5-launch, claude-haiku-5-5-launch-2026-10-19]
---

# Claude Sonnet 5.5

Anthropic's middle-tier Claude 5.5 model, superseding [Claude Sonnet 5](../history/models/claude-sonnet-5.md). It is the faster, cheaper complement to [Claude Opus 5.5](claude-opus-5-5.md): strongest at well-scoped everyday tasks, bug fixing, and polished documents, slides and spreadsheets, while Opus 5.5 stays clearly stronger on open-ended work that needs sustained judgment.

## Current status (as of 2026-10-20)

- Available on the Claude Platform as `claude-sonnet-5-5`, and on AWS, Google Cloud and Microsoft Azure. Users running thinking off must switch to the new `between_tools` setting.
- Pricing per 1M tokens: $2 input, $10 output (same as Sonnet 5), $2.50 cache writes, $0.10 cache reads. Anthropic says it costs up to 30% less per task than Sonnet 5 and outputs 30%+ faster, its fastest Sonnet yet.
- Launch benchmarks (Sonnet 5.5 / Sonnet 5 / Opus 5.5): Terminal-Bench 4.0 70.6% / 10.3% / 66.4%; CursorBench 4.0 55.5% / 34.1% / 57.8%; GDPval-AA v2.1 1844 / 1449 / 1846; OSWorld 2.1 80.1% / 57.0% / 81.8%. Anthropic says Sonnet 5.5 at Low or Medium effort beats Sonnet 5's best score on several benchmarks at about a tenth of the cost per task.
- First Sonnet to launch with Opus-class cyber safeguards (higher-risk cyber tasks fall back to Sonnet 5) and anti-distillation classifiers; biology safeguards unchanged from Sonnet 5.

## Evidence from early users

- Base44: across 118 app builds, Sonnet 5.5 matched Opus 5's scores in 3.6 iterations per build against Opus 5's 7.7. Balyasny: about 121k tokens per finance answer against Sonnet 5's 497k.

## Recent changes

- [2026-10-20] Page created from Anthropic's launch post. The post carries no date; it followed Opus 5.5 and preceded Haiku 5.5. Supersedes Sonnet 5.
- [2026-10-19] Cache reads halved from $0.20 to $0.10 per 1M tokens, announced with Haiku 5.5; Anthropic says this makes Sonnet 5.5 about 20% cheaper on most agentic work.

## Sources

- [Claude Sonnet 5.5 launch](../sources/articles/claude-sonnet-5-5-launch.md)
- [Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
