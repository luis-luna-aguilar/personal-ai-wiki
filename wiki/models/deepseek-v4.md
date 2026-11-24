---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-10-20
sources: [deepseek-v4-preview, ainews-2026-04-25, ainews-all-model-labs-are-now-agent-labs, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, ainews-deepseek-v4-1-flash-1017-2026-10-20]
---

# DeepSeek V4

DeepSeek's April 2026 open-weight release for long-context agent workloads; this page now tracks **V4 Pro**, DeepSeek's current Pro model. The key contribution is not a clean overall frontier win, but a serious systems design point: V4 pairs competitive open-model capability with 1M-token context, much lower KV-cache pressure, and explicit tool-use shaping. **The V4 Flash tier is superseded by [DeepSeek V4.1 Flash](deepseek-v4-1-flash.md)** (new 552B/16B architecture); its 0731 update and Vision-Exp build are archived in [history](../history/models/deepseek-v4.md).

## Current status (as of 2026-10-20)

- **V4 Flash superseded:** DeepSeek's current Flash model is [V4.1 Flash](deepseek-v4-1-flash.md) (1017 build, 20 October 2026); on Artificial Analysis' re-versioned Intelligence Index it scores 45 against V4 Pro 0813's 36
- **V4 Pro:** 1.6T total / 49B active, 1M-token context, MIT-licensed (the V4 Flash tier, 284B / 13B active, is archived)
- **V4 Pro reached general availability on 2026-08-13** after the April preview, with a reported 15.8% Terminal-Bench gain over the preview; reception was mixed, solid but not clearly ahead of Kimi/Flash on all tasks
- **Pricing:** V4 Pro $0.435 / $0.87 per 1M input/output tokens (the 75% discount made permanent in May, confirmed at GA; Cline puts it ~57x cheaper than Claude Fable 5), replacing the launch price of $1.74 / $3.48. **Caveat:** DeepSeek's own pricing page, as fetched 2026-08-25, shows a peak/off-peak, cache-hit/cache-miss structure whose figures do not match these numbers; current pricing needs its own dated ingest
- Still behind the strongest closed frontier systems overall, and very high token usage in some evaluations means cheap per-token pricing does not guarantee cheap tasks
- Huawei Ascend compatibility and rapid vLLM / third-party support make the release part of a broader inference-substrate story, not just a checkpoint drop

## V4 Pro general availability (as of 2026-08-13)

DeepSeek's V4 Pro reached general availability, closing out the "official release still pending" status noted after the July V4-Flash update:

- **Pricing:** confirmed at $0.435/M input, $0.87/M output — Cline reports this as roughly 57x cheaper than Claude Fable 5
- **Benchmarks:** a reported 15.8% Terminal-Bench gain over the V4 Pro preview (absolute score not given in this source)
- **Reception:** mixed — some early users (Yuchen Jin, scaling01, teortaxesTex) found it solid but not clearly ahead of Kimi/Flash on all tasks; observers suggested DeepSeek's next gains may depend more on RL/agent-environment work than raw scale

## Strengths

- Serious open-weight long-context release with unusually concrete attention to KV-cache and long-trace economics
- Competitive with top open-weight coding/agent models while exposing a richer technical report than many frontier releases

## Weaknesses / caveats

- Still behind the strongest closed frontier systems overall according to the captured independent benchmark framing
- Cheap per-token pricing does not guarantee cheap tasks; AINews highlights evaluations where V4 emitted very large token volumes
- Architecture complexity may limit how much the wider open ecosystem can reproduce the training-side gains, even if inference support spreads quickly

## Recent changes

- [2026-10-20] V4 Flash superseded by DeepSeek V4.1 Flash (552B/16B encoder-decoder MoE; 1017 build scores 45 on the current AA index, where V4 Pro 0813 scores 36); V4 Pro remains current. The V4 Flash 0731 and Vision-Exp sections moved to history.
- [2026-08-13] V4 Pro reached general availability: $0.435/$0.87 per M token pricing confirmed, +15.8% Terminal-Bench over its preview; capability reception mixed versus Kimi/Flash
- [2026-05-23] DeepSeek made the 75% V4-Pro discount permanent; Artificial Analysis pricing/cost-per-Intelligence-Index comparison (via AINews) added, caveated as a May 2026 snapshot since DeepSeek's pricing page (fetched 2026-08-25) has since moved to peak/off-peak, cache-hit/miss tiers.
- [2026-04-25] AINews follow-up reframed DeepSeek V4 from preview to release: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Huawei Ascend compatibility, and token-volume caveats
- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning

## Sources

- [DeepSeek V4 Preview](../sources/articles/deepseek-v4-preview.md)
- [AINews - DeepSeek V4 Pro and Flash](../sources/newsletters/ainews-2026-04-25.md)
- [AINews — All model labs are now agent labs (DeepSeek V4-Pro permanent discount)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
- [AINews — SpaceXAI Grok 4.6 and Grok Bot (DeepSeek V4 Pro GA)](../sources/newsletters/ainews-spacexai-grok-46-and-grok-bot-2026-08-13.md)
- [AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md)
