---
title: Xiaomi MiMo-V2.6
type: model
domains: [models]
subcategory: open-weight-model
tags: [open-weights, multimodal]
as_of: 2026-09-25
sources: [ainews-xiaomi-mimo-v26-pro-2026-09-22, ainews-mimo-aa-comparison-hysparse2-2026-09-25]
---

# Xiaomi MiMo-V2.6

Xiaomi's open-weight model series, released around 2026-09-21: MiMo-V2.6-Pro (most capable), MiMo-V2.6-Flash (cost/efficiency tier) and Pro-UltraSpeed (Xiaomi claims up to 20x faster output at the same quality). Both models are natively omnimodal (one model for text, image, audio and video input) and ship under the MIT license with a technical report, training code and the RL environments used to post-train them.

## Current status (as of 2026-09-25)

- **Pro:** 1.02T total / 42B active parameters, 1M context; Artificial Analysis Intelligence Index 46 (GPT-5.6 Sol 47 on the same scale); $0.435 / $0.87 per 1M input/output tokens, about $0.13 per index task vs $1.99 for Sol
- **RL at scale, cheaply:** RL compute scaled along three axes (1,568 samples per update with up to 1M context; a multi-task mix across coding, agents, vision and cyber in several harnesses; more grader compute). One commentator puts the final RL run at 130 hours, 75B tokens and about $2.6M on JAX/TPU
- **Open RL environments:** environment code and recipes released for coding, cyber vulnerability reproduction, knowledge work, web development and music; about 7K environments planned, but the full task datasets are not yet out
- **Next:** MiMo-V3 will move to HySparse2, a sparse-attention design that cuts key-value cache size and long-prompt processing cost (tested on an 80B model so far)

## Why it matters

The release makes the post-training recipe, not only the weights, public. Commentators read it as a sign that open RL environments may become as strategic as open pretraining corpora were, and that RL is a cheaper route to frontier-adjacent scores than assumed. See [RL harness quality](../concepts/rl-harness-quality.md) and [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md).

## Weaknesses / caveats

- RL gains reportedly do not generalize to harder math evals
- Users report overthinking (long reasoning on simple prompts); a system-prompt mitigation circulates
- The Artificial Analysis score is on the index as of September 2026; older scores elsewhere in the wiki may sit on a different scale

## Recent changes

- [2026-09-25] Artificial Analysis cost comparison ($0.13 vs $1.99 per task against GPT-5.6 Sol); math-generalization and overthinking caveats; MiMo-V3 to use HySparse2.
- [2026-09-22] MiMo-V2.6-Pro, -Flash and Pro-UltraSpeed released under MIT with technical report, training code and RL environments; AA Intelligence Index 46 for Pro.

## Sources

- [AINews — Xiaomi MiMo-V2.6-Pro 1T-A42B](../sources/newsletters/ainews-xiaomi-mimo-v26-pro-2026-09-22.md)
- [AINews — MiMo-V2.6-Pro cost comparison and HySparse2](../sources/newsletters/ainews-mimo-aa-comparison-hysparse2-2026-09-25.md)
