---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-04-25
sources: [deepseek-v4-preview, ainews-2026-04-25]
---

# DeepSeek V4

DeepSeek's April 2026 open-weight release for long-context agent workloads. The key contribution is not a clean overall frontier win, but a serious systems design point: V4 pairs competitive open-model capability with 1M-token context, much lower KV-cache pressure, explicit tool-use shaping, and a Pro/Flash split for different cost/performance needs.

## Current status (as of 2026-04-25)

- Released as **V4 Pro** (1.6T total / 49B active) and **V4 Flash** (284B total / 13B active), with base and instruct variants, 1M-token context, and MIT licensing
- V4 Pro is now positioned near the top of open weights, but still below GPT-5.x / Claude Opus 4.7 / Gemini 3.1 Pro in aggregate closed-frontier comparisons
- Independent benchmark synthesis in AINews places V4 Pro as a leading open model for agentic real-world work, while also noting very high token usage in some evaluations
- First-party API pricing reported in the AINews issue: V4 Pro at `$1.74 / $3.48` per 1M input/output tokens, V4 Flash at `$0.14 / $0.28`
- Huawei Ascend compatibility and rapid vLLM / third-party support make the release part of a broader inference-substrate story, not just a checkpoint drop

## Strengths

- Serious open-weight long-context release with unusually concrete attention to KV-cache and long-trace economics
- Flash tier may matter more for practical adoption than Pro in workloads where 1M context and low per-token price dominate
- Competitive with top open-weight coding/agent models while exposing a richer technical report than many frontier releases

## Weaknesses / caveats

- Still behind the strongest closed frontier systems overall according to the captured independent benchmark framing
- Cheap per-token pricing does not guarantee cheap tasks; AINews highlights evaluations where V4 emitted very large token volumes
- Architecture complexity may limit how much the wider open ecosystem can reproduce the training-side gains, even if inference support spreads quickly

## Recent changes

- [2026-04-25] AINews follow-up reframed DeepSeek V4 from preview to release: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Huawei Ascend compatibility, and token-volume caveats
- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning

## Sources

- [DeepSeek V4 Preview](../sources/articles/deepseek-v4-preview.md)
- [AINews - DeepSeek V4 Pro and Flash](../sources/newsletters/ainews-2026-04-25.md)
