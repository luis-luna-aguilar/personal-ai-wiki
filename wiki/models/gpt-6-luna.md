---
title: GPT-6 Luna
type: model
domains: [models]
subcategory: small-model
tags: [openai, closed-source]
as_of: 2026-10-08
sources: [ainews-gpt-6-sol-luna-launch-2026-09-23, ainews-gpt-6-1-sol-devday-2026-09-30, ainews-gpt-6-1-sol-evals-2026-10-01, ainews-gpt-6-1-sol-ultrafast-2026-10-08, openai-introducing-gpt-6-2-astra-sol]
---

# GPT-6 Luna

OpenAI's cheapest GPT-6 tier, launched with GPT-6 Sol on 2026-09-22 as a cheaper model built on [GPT-6 Astra](../history/models/gpt-6-astra.md)'s advances. It supersedes GPT-5.6 Luna (covered on the archived [GPT-5.6 Sol](../history/models/gpt-5-6-sol.md) page) at about half the price. The mid tier has since moved on to [GPT-6.1 Sol](../history/models/gpt-6-1-sol.md) and then [GPT-6.2 Sol](gpt-6-2-sol.md) (2026-11-23); no GPT-6.1 or GPT-6.2 Luna has been announced.

## Current status (as of 2026-10-08)

- **Price:** $0.10/$0.50 per 1M input/output tokens, about half GPT-5.6 Luna's; cached input reads up to 90% off
- **Availability:** Codex, ChatGPT Work and the API; Free/Go users get it in the desktop app, not yet in Chat mode
- **Launch claims:** OpenAI says Luna at max effort beats GPT-5.6 Sol at medium effort on OSWorld 2.0 (offline) at a tenth of the cost; Cognition reports it beats its predecessor in Devin at about a quarter of the cost
- **Decisions:** powers OpenAI's Decisions API (beta, announced at DevDay on 2026-09-29; see [Decision models](../concepts/decision-models.md)) and is the fastest decisions model on OpenRouter at 180ms
- **Artificial Analysis:** an early-October image-encoding fix added one point on the Intelligence Index

## Weaknesses / caveats

- Price parity with [Claude Haiku 5.5](claude-haiku-5-5.md), which launched at the same $0.10/$0.50 list price
- No GPT-6.1 or GPT-6.2 Luna yet, so Luna has not had the refreshes that cut Sol's per-task cost

## Recent changes

- [2026-10-08] Fastest decisions model on OpenRouter at 180ms; Claude Haiku 5.5 matches its $0.10/$0.50 price.
- [2026-10-01] Image-encoding fix added one point on Artificial Analysis's Intelligence Index.
- [2026-09-29] Powers OpenAI's new Decisions API (beta), announced at DevDay.
- [2026-09-22] Launched with GPT-6 Sol at $0.10/$0.50, about half GPT-5.6 Luna's price.

## Sources

- [AINews — GPT-6 Sol and Luna launch](../sources/newsletters/ainews-gpt-6-sol-luna-launch-2026-09-23.md)
- [AINews — OpenAI DevDay 2026: GPT-6.1 Sol](../sources/newsletters/ainews-gpt-6-1-sol-devday-2026-09-30.md)
- [AINews — GPT-6.1 Sol independent evals](../sources/newsletters/ainews-gpt-6-1-sol-evals-2026-10-01.md)
- [AINews — GPT-6.1 Sol Ultrafast and Arena Alignment Index](../sources/newsletters/ainews-gpt-6-1-sol-ultrafast-2026-10-08.md)
- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
