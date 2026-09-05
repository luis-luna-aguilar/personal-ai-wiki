---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-05-23
sources: [deepseek-v4-preview, ainews-2026-04-25, ainews-all-model-labs-are-now-agent-labs]
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

## Strengths

- Serious open-weight long-context release with unusually concrete attention to KV-cache and long-trace economics
- Flash tier may matter more for practical adoption than Pro in workloads where 1M context and low per-token price dominate
- Competitive with top open-weight coding/agent models while exposing a richer technical report than many frontier releases

## Weaknesses / caveats

- Still behind the strongest closed frontier systems overall according to the captured independent benchmark framing
- Cheap per-token pricing does not guarantee cheap tasks; AINews highlights evaluations where V4 emitted very large token volumes
- Architecture complexity may limit how much the wider open ecosystem can reproduce the training-side gains, even if inference support spreads quickly

## Recent changes

- [2026-05-23] DeepSeek made the 75% V4-Pro discount permanent; Artificial Analysis pricing/cost-per-Intelligence-Index comparison (via AINews) added, caveated as a May 2026 snapshot since DeepSeek's pricing page (fetched 2026-08-25) has since moved to peak/off-peak, cache-hit/miss tiers.
- [2026-04-25] AINews follow-up reframed DeepSeek V4 from preview to release: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Huawei Ascend compatibility, and token-volume caveats
- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning

## Sources

- [DeepSeek V4 Preview](../sources/articles/deepseek-v4-preview.md)
- [AINews - DeepSeek V4 Pro and Flash](../sources/newsletters/ainews-2026-04-25.md)
- [AINews — All model labs are now agent labs (DeepSeek V4-Pro permanent discount)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
