---
title: AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
url: https://www.latent.space/p/ainews-deepseek-deepinfer-open-source
published: 2026-10-21
ingested: 2026-11-24
domains: [models, agents]
---

# AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)

AINews's lead story on DeepSeek releasing DeepInfer, the inference engine behind V4.1 Flash, with an engineering report on its production serving: architecture, cache hierarchy, speculative decoding, reported production figures, vLLM's comparison and the debate over what the revenue figure implies for margins. Also notes OpenAI's 12-hour API prompt caching.

## Influenced pages

- [DeepSeek V4.1 Flash](../../models/deepseek-v4-1-flash.md) — new Serving stack section
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — open inference serving and its economics
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — 12-hour prompt-cache retention

## Key claims extracted

- DeepInfer (Apache 2.0, vLLM-derived) released 2026-10-20 with `deepseek-recipe` for Chat Completions, Responses and Messages API processing; supports NVIDIA and Huawei Ascend
- KV-cache management and load balancing are not fully released because they are coupled to internal infrastructure
- Block KV cache on a ~100 PiB 3FS SSD cluster, retained 3 days for agent traffic and 7 for chat; any prefill worker can serve any cached prefix
- SWA Bounded Replay rebuilds short-lived state from the last 128 tokens, nearly halving prefill compute
- DSpark adaptive speculative decoding: +6% throughput over always verifying five draft tokens
- Reported: 155T tokens/day from one cluster, 96% input-cache hits, 400 ms average TTFT, 230 tok/s (300 for coding), $38 revenue per accelerator-hour off-peak
- vLLM: decode throughput within 6% of DeepInfer on GB200 under a matched configuration (decode only, not the whole service)
- Commentators' accelerator-only margins: about 73.7–86.8% at $5–10/hr; estimates omit SSD fleet, CPUs, networking, idle capacity and staff, and depend on the cache-heavy token mix
- OpenAI announced 12-hour API prompt-cache retention against a 30-minute default, with mixed retention durations within a request
