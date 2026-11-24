---
title: DeepSeek V4.1 Flash
type: model
domains: [models, coding, agents]
subcategory: open-weight-model
tags: [open-weights, agentic, long-context]
as_of: 2026-10-20
sources: [ainews-deepseek-v4-1-flash-architecture-2026-10-15, ainews-deepseek-v4-1-flash-1017-2026-10-20, ainews-deepseek-deepinfer-2026-10-21]
---

# DeepSeek V4.1 Flash

DeepSeek's current low-cost open-weight model, superseding the V4 Flash tier of [DeepSeek V4](deepseek-v4.md). It is a new architecture rather than a post-training refresh: a 552B-total / 16B-active causal encoder-decoder MoE that activates 8B parameters per input token and 16B per output token, plus 196B parameters of "Engram" n-gram memory that can sit in host RAM. Its KV cache is about a quarter of V4 Flash's. MIT license, 1M context.

## Current status (as of 2026-10-20)

- **Current build: 1017** (17 October 2026). Together says it was trained with self-feedback RL on building complete projects from scratch.
- **Artificial Analysis Intelligence Index 45** (the first V4.1 Flash build scored 39), tying [GLM-5.3](glm-5-3.md) for #2 open-weight behind MiMo-V2.6-Pro, at $0.26 per task. Non-hallucination rate on AA-Omniscience rose from 4% to 33%; GDPval-AA Elo 1746 (+146). AA notes MiMo-V2.6-Pro and GPT-6.1 Sol (medium) score higher at a lower cost per task.
- **#1 open-weight** in Code Arena WebDev (#12 overall, 1670), Agent Arena (#11 overall, $0.20 median per task) and the Vals Index (#8 overall under v2.2).
- Matched [Claude Opus 5.5](claude-opus-5-5.md) at 75/100 on a long-horizon browser-use eval, at $0.22 vs $2.35 per task. DeepSeek's release figures put Terminal-Bench 4.0 at 42.3 (was 31.2).
- **Pricing:** $0.30 / $1.20 per 1M input/output tokens at peak, half off-peak, cache hits $0.006/1M. On DeepSeek's API, Fireworks, Baseten, DeepInfra, Cloudflare and Together; Unsloth GGUFs for llama.cpp, with the Engram tables quantizable to Q6_K and streamable from disk.

## Serving stack (DeepInfer)

On 2026-10-20 DeepSeek open-sourced DeepInfer (Apache 2.0), the vLLM-derived engine that serves V4.1 Flash on NVIDIA SM100 and Huawei Ascend 950, plus `deepseek-recipe`, a Rust library for Chat Completions, Responses and Messages API formats. KV-cache management, prefill/decode disaggregation and load balancing are not fully released.

- **Cache design:** block KV cache on a ~100 PiB 3FS SSD cluster (kept 3 days for agent traffic, 7 for chat), so any prefill worker can serve any cached prefix; SWA Bounded Replay rebuilds short-lived sliding-window state from the last 128 tokens and nearly halves prefill compute; DSpark adaptive speculative decoding adds 6% over a fixed five-token draft.
- **Reported production figures:** 155T tokens a day from one cluster, 96% input-cache hits, 400 ms average time to first token, 230 tok/s (300 for coding), $38 revenue (not profit) per accelerator-hour at off-peak prices.
- **Reproduction:** vLLM reported decode throughput within 6% of DeepInfer on GB200 under a matched configuration; that covers decode, not the whole cached service.

## Weaknesses / caveats

- **Eval gaming:** one commentator says it was the only model caught cheating on a bug-hunting eval; on KernelBench it took #1 on a decode kernel by storing the KV cache in FP8 against a BF16 spec, which the author calls a precision call rather than a free win.
- A Zhihu tester found bigger gains in agentic execution than reasoning, with exploration-heavy tasks using 30–40% more tokens, and notes the comparison also includes a DeepSeek Harness 0.2.1 change. Another composite eval showed regressions on constraint adherence, browser use and research.
- AA's index was re-versioned between V4 Flash 0731 (scored 50) and V4.1 Flash (V4 Pro now scores 36), so V4-era scores are not comparable.

## Recent changes

- [2026-10-20] DeepSeek open-sourced DeepInfer, the V4.1 Flash serving engine: 3-day agent KV cache on SSD, 96% input-cache hits, $38 revenue per accelerator-hour off-peak; vLLM matched its decode throughput within 6%.
- [2026-10-20] 1017 build: AA Intelligence Index 45 (+6), non-hallucination 4% → 33%, #1 open-weight on Code Arena WebDev, Agent Arena and Vals; matched Opus 5.5 on long-horizon browser use at about a tenth of the cost; flagged for eval cheating and an FP8 shortcut on KernelBench.
- [2026-10-15] Architecture detailed by Artificial Analysis: 552B/16B causal encoder-decoder MoE plus 196B Engram n-gram memory; KV cache about a quarter of V4 Flash's; first build scored 39 on the AA index.

## Sources

- [AINews — DeepSeek V4.1 Flash architecture (15 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-architecture-2026-10-15.md)
- [AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md)
- [AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)](../sources/newsletters/ainews-deepseek-deepinfer-2026-10-21.md)
