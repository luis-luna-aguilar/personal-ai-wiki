---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-08-13
sources: [deepseek-v4-preview, ainews-2026-04-25, ainews-all-model-labs-are-now-agent-labs, ainews-not-much-happened-2026-08-01, ainews-spacexai-grok-46-and-grok-bot-2026-08-13]
---

# DeepSeek V4

DeepSeek's April 2026 open-weight release for long-context agent workloads. The key contribution is not a clean overall frontier win, but a serious systems design point: V4 pairs competitive open-model capability with 1M-token context, much lower KV-cache pressure, explicit tool-use shaping, and a Pro/Flash split for different cost/performance needs.

## Current status (as of 2026-05-23)

- Released as **V4 Pro** (1.6T total / 49B active) and **V4 Flash** (284B total / 13B active), with base and instruct variants, 1M-token context, and MIT licensing
- V4 Pro is now positioned near the top of open weights, but still below GPT-5.x / Claude Opus 4.7 / Gemini 3.1 Pro in aggregate closed-frontier comparisons
- Independent benchmark synthesis in AINews places V4 Pro as a leading open model for agentic real-world work, while also noting very high token usage in some evaluations
- First-party API pricing reported in the AINews issue: V4 Pro at `$1.74 / $3.48` per 1M input/output tokens, V4 Flash at `$0.14 / $0.28`
- Huawei Ascend compatibility and rapid vLLM / third-party support make the release part of a broader inference-substrate story, not just a checkpoint drop
- **Permanent price cut (as of 2026-05-23):** DeepSeek made its previously-temporary 75% V4-Pro discount permanent (via AINews). Artificial Analysis (via AINews) quantifies first-party pricing at $0.435/M input, $0.87/M output, $0.0036/M cached input — a blended ~$0.18/M — and estimates running AA's Intelligence Index on V4-Pro costs ~3x less than Gemini 3.1 Pro Preview, ~12x less than GPT-5.5, and ~19x less than Claude Opus 4.7. **Caveat:** DeepSeek's own pricing page (`api-docs.deepseek.com/quick_start/pricing`), as fetched 2026-08-25, lists `deepseek-v4-pro` with a peak/off-peak, cache-hit/cache-miss structure whose figures no longer match the May numbers — treat the figures above as a May 2026 snapshot, not current pricing; current pricing needs its own dated ingest.

## V4-Flash 0731 update (as of 2026-07-31)

DeepSeek shipped a post-training-only upgrade to V4-Flash — same 284B total / 13B active architecture, no scaling or architecture change:

- **Benchmarks:** Terminal-Bench 56.9 → 82.7 (+25.8); Artificial Analysis Intelligence Index 40 → 50, one point behind GPT-5.6 Luna's 51 at roughly 60% lower cost per task on DeepSeek's own API; GDPval-AA v2 Elo 1189 → 1559; output-token usage down 12% versus the predecessor.
- **Pricing:** $0.14 / $0.28 per 1M input/output tokens, with a 98% cache-hit discount down to $0.0028/1M cached tokens.
- **Open weights:** released under MIT with immediate day-0 vLLM support — 256 routed experts, 6 active per token, three reasoning-effort levels, and an included DSpark speculative-decoding module enabled via a single flag. Local/quantized builds landed same-day (Unsloth: ~168GB RAM for lossless 4-bit, ~110GB for 3-bit).
- **Scope:** this update applies to V4-Flash only. V4-Pro's API, app, and web product are unchanged; an official V4-Pro release remains pending.
- Widely read as a direct competitive response to OpenAI's GPT-5.6 price cuts the day before.

## V4 Pro general availability (as of 2026-08-13)

DeepSeek's V4 Pro reached general availability, closing out the "official release still pending" status noted after the July V4-Flash update:

- **Pricing:** confirmed at $0.435/M input, $0.87/M output — Cline reports this as roughly 57x cheaper than Claude Fable 5
- **Benchmarks:** a reported 15.8% Terminal-Bench gain over the V4 Pro preview (absolute score not given in this source)
- **Reception:** mixed — some early users (Yuchen Jin, scaling01, teortaxesTex) found it solid but not clearly ahead of Kimi/Flash on all tasks; observers suggested DeepSeek's next gains may depend more on RL/agent-environment work than raw scale

## Strengths

- Serious open-weight long-context release with unusually concrete attention to KV-cache and long-trace economics
- Flash tier may matter more for practical adoption than Pro in workloads where 1M context and low per-token price dominate
- Competitive with top open-weight coding/agent models while exposing a richer technical report than many frontier releases

## Weaknesses / caveats

- Still behind the strongest closed frontier systems overall according to the captured independent benchmark framing
- Cheap per-token pricing does not guarantee cheap tasks; AINews highlights evaluations where V4 emitted very large token volumes
- Architecture complexity may limit how much the wider open ecosystem can reproduce the training-side gains, even if inference support spreads quickly

## Recent changes

- [2026-08-13] V4 Pro reached general availability: $0.435/$0.87 per M token pricing confirmed, +15.8% Terminal-Bench over its preview; capability reception mixed versus Kimi/Flash
- [2026-07-31] V4-Flash 0731: post-training-only update jumps Terminal-Bench to 82.7 (+25.8) and AA Intelligence Index to 50 (from 40), now 1pt behind GPT-5.6 Luna; open-weighted under MIT with day-0 vLLM support; V4-Pro unaffected, still pending its own release.
- [2026-05-23] DeepSeek made the 75% V4-Pro discount permanent; Artificial Analysis pricing/cost-per-Intelligence-Index comparison (via AINews) added, caveated as a May 2026 snapshot since DeepSeek's pricing page (fetched 2026-08-25) has since moved to peak/off-peak, cache-hit/miss tiers.
- [2026-04-25] AINews follow-up reframed DeepSeek V4 from preview to release: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Huawei Ascend compatibility, and token-volume caveats
- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning

## Sources

- [DeepSeek V4 Preview](../sources/articles/deepseek-v4-preview.md)
- [AINews - DeepSeek V4 Pro and Flash](../sources/newsletters/ainews-2026-04-25.md)
- [AINews — All model labs are now agent labs (DeepSeek V4-Pro permanent discount)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
- [AINews — not much happened today (DeepSeek V4-Flash 0731)](../sources/newsletters/ainews-not-much-happened-2026-08-01.md)
- [AINews — SpaceXAI Grok 4.6 and Grok Bot (DeepSeek V4 Pro GA)](../sources/newsletters/ainews-spacexai-grok-46-and-grok-bot-2026-08-13.md)
