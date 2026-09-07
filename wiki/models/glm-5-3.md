---
title: GLM-5.3
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-08-20
sources: [ainews-death-of-params-glm-53-2026-08-20]
---

# GLM-5.3

Z.ai's August 2026 open-weight frontier model, superseding [GLM-5.2](../history/models/glm-5-2.md). Same 753B total / 40B active MoE architecture and 1M context as its predecessor, at the same API price — this generation's gains come entirely from post-training reinforcement learning rather than a larger base model.

## Current status (as of 2026-08-20)

- 753B total / 40B active MoE; 1M context window; MIT license once weights land (not yet shipped at time of writing)
- GDPval-AA v2: +246 points over GLM-5.2 (to 1770 Elo)
- Artificial Analysis Intelligence Index: 60, tying Kimi K3
- Reported training mechanism (via a Zhihu summary relayed through AINews, not a Z.ai primary report): SAO (single-rollout asynchronous optimization), executable sandbox training on production-like long-horizon workflows — some tasks representing several days of an experienced engineer's work — and on-policy distillation to prevent catastrophic forgetting during RL
- Inherited from GLM-5.2: IndexShare sparse-attention indexer (2.9x lower FLOPs at 1M context), MTP speculative decoding, and a transparent anti-reward-hacking RL training story

## Why it matters

Z.ai co-founder and CEO Jie Tang argues parameter count alone is now a misleading capability proxy: "Parameter count is only meaningful alongside three others — how much data you have, where you intend to spend your compute, and who will run the model, under what conditions." He proposes model-family notation (e.g. "XA-YB" for MoE sparsity) to replace raw parameter counts, and argues advanced skills like vulnerability-finding require carrying long causal chains (20+ inference steps) that don't live in total parameter count once a baseline knowledge threshold is crossed — GLM-5.3's benchmark jump at an unchanged footprint is offered as the concrete evidence for that argument.

## Weaknesses / caveats

- The 246-point GDPval-AA v2 jump and the SAO/sandbox-training mechanism description come from a Zhihu summary relayed through AINews, not a Z.ai primary technical report
- Weights not yet shipped at time of writing (API-only)

## Recent changes

- [2026-08-20] Launched via API: same 753B/40B footprint and price as GLM-5.2, +246 GDPval-AA v2, ties Kimi K3 on AA Intelligence Index — gains attributed to post-training RL (SAO, sandbox training, on-policy distillation). Supersedes [GLM-5.2](../history/models/glm-5-2.md). Z.ai CEO Jie Tang argues parameter count alone now misleads on capability.

## Sources

- [AINews — Death of Params: Z.ai CEO Jie Tang on GLM 5.3](../sources/newsletters/ainews-death-of-params-glm-53-2026-08-20.md)
