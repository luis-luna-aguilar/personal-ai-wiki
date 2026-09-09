---
title: GLM-5.3
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-08-27
sources: [ainews-death-of-params-glm-53-2026-08-20, ainews-nvidia-buys-huggingface-2026-08-27, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29]
---

# GLM-5.3

Z.ai's August 2026 open-weight frontier model, superseding [GLM-5.2](../history/models/glm-5-2.md). Same 753B total / 40B active MoE architecture and 1M context as its predecessor, at the same API price — this generation's gains come entirely from post-training reinforcement learning rather than a larger base model.

## Current status (as of 2026-08-20)

- 753B total / 40B active MoE; 1M context window; MIT license once weights land (not yet shipped at time of writing)
- GDPval-AA v2: +246 points over GLM-5.2 (to 1770 Elo)
- Artificial Analysis Intelligence Index: 60, tying Kimi K3
- Reported training mechanism (via a Zhihu summary relayed through AINews, not a Z.ai primary report): SAO (single-rollout asynchronous optimization), executable sandbox training on production-like long-horizon workflows — some tasks representing several days of an experienced engineer's work — and on-policy distillation to prevent catastrophic forgetting during RL
- Inherited from GLM-5.2: IndexShare sparse-attention indexer (2.9x lower FLOPs at 1M context), MTP speculative decoding, and a transparent anti-reward-hacking RL training story

## GLM-5.3-Flash: a smaller open-weight sibling (as of 2026-08-27)

Z.ai revealed that "Ox Alpha" — a mystery model that had spent weeks impressing coding-agent users pre-launch — is GLM-5.3-Flash's public identity: a 320B-total/18B-active MoE, natively multimodal, MIT-licensed, 1M-token context.

- Claims parity with Claude Opus 4.8 on Z.ai's own coding benchmark
- Artificial Analysis Intelligence Index: 57 (3 points behind full GLM-5.3's 60)
- Cost: $0.09/task, ~7.5x cheaper per task than GLM-5.3 Max
- Z.ai says it runs entirely on Chinese AI chips at an estimated 100T tokens/day
- Adoption: Cline reports Flash already drives 11% of its coding traffic within days of reveal; day-0 serving support from CoreWeave, Baseten, and Ollama
- Quantization: community 2-bit build compresses to 239GB while retaining ~81% of full accuracy
- Independent pushback: weaker-than-advertised vision/object-detection results despite the "native vision" framing; lower Artificial Analysis Omniscience (knowledge/hallucination) score than full GLM-5.3

The full (non-Flash) GLM-5.3 also went open-weight in this window at its original 753B-total/40B-active footprint, with day-0 vLLM support.

## Why it matters

Z.ai co-founder and CEO Jie Tang argues parameter count alone is now a misleading capability proxy: "Parameter count is only meaningful alongside three others — how much data you have, where you intend to spend your compute, and who will run the model, under what conditions." He proposes model-family notation (e.g. "XA-YB" for MoE sparsity) to replace raw parameter counts, and argues advanced skills like vulnerability-finding require carrying long causal chains (20+ inference steps) that don't live in total parameter count once a baseline knowledge threshold is crossed — GLM-5.3's benchmark jump at an unchanged footprint is offered as the concrete evidence for that argument.

## Weaknesses / caveats

- The 246-point GDPval-AA v2 jump and the SAO/sandbox-training mechanism description come from a Zhihu summary relayed through AINews, not a Z.ai primary technical report
- GLM-5.3-Flash's benchmark and "100T tokens/day on Chinese chips" figures are likewise relayed through AINews tweet-recap coverage, not a Z.ai primary report
- ~~Weights not yet shipped at time of writing (API-only)~~ — corrected 2026-08-27: both GLM-5.3 and GLM-5.3-Flash have since gone open-weight

## Recent changes

- [2026-08-27] GLM-5.3-Flash launches, revealed as the mystery "Ox Alpha" model: 320B/18B MoE, MIT-licensed, claims Opus 4.8 parity on Z.ai's coding benchmark; full GLM-5.3 also goes open-weight with day-0 vLLM support.
- [2026-08-20] Launched via API: same 753B/40B footprint and price as GLM-5.2, +246 GDPval-AA v2, ties Kimi K3 on AA Intelligence Index — gains attributed to post-training RL (SAO, sandbox training, on-policy distillation). Supersedes [GLM-5.2](../history/models/glm-5-2.md). Z.ai CEO Jie Tang argues parameter count alone now misleads on capability.

## Sources

- [AINews — Death of Params: Z.ai CEO Jie Tang on GLM 5.3](../sources/newsletters/ainews-death-of-params-glm-53-2026-08-20.md)
- [AINews — NVIDIA buys Hugging Face for $13B, GLM-5.3-Flash reveal](../sources/newsletters/ainews-nvidia-buys-huggingface-2026-08-27.md)
- [AINews — OpenAI to reach AGI bar by end-2026 (Flash quantization reaction)](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — OpenAI shuts off Cursor (full GLM-5.3 open-weighting)](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
