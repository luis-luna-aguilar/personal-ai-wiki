---
title: '[AINews] Xiaomi MiMo-V2.6-Pro 1T-A42B: the new top Open Weights model, trained for $3M'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-22-ainews-xiaomi-mimo-v26-pro-1t-a42b-the-new-top.md
url: https://www.latent.space/p/ainews-xiaomi-mimo-v26-pro-1t-a42b
published: 2026-09-22
ingested: 2026-10-20
domains: [models]
---

# AINews — Xiaomi MiMo-V2.6-Pro 1T-A42B

AINews' lead story for 19–21 September 2026: Xiaomi released MiMo-V2.6-Pro and -Flash, natively omnimodal open-weight models under MIT, with a technical report, training code and RL environments, plus a Pro-UltraSpeed variant. Artificial Analysis placed Pro at the top of open-weight models on its Intelligence Index. Commentary focused on the RL stack: live-published final RL runs, three-axis RL scaling, a cheap RL run, and the argument that open RL environments are now strategic.

## Influenced pages

- [Xiaomi MiMo-V2.6](../../models/mimo-v2-6.md) — new page
- [State of Models](../../state-of/models.md) — Open-weight models leader line
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new-entrant bullet
- [RL harness quality](../../concepts/rl-harness-quality.md) — open RL environments

## Key claims extracted

- MiMo-V2.6-Pro: 1.02T total / 42B active, natively omnimodal, MIT license; AA Intelligence Index 46 (top open-weights model per AA); $0.435 / $0.87 per 1M input/output tokens
- Pro-UltraSpeed: up to 20x faster output at the same quality (Xiaomi)
- RL scaled on three axes: 1,568 samples per update, up to 1M context, 3.5–3.7B tokens per step; multi-task suite across coding, agents, visual and cyber in several harnesses; more grader compute
- Final RL run: 130 hours, 75B tokens, about $2.6M (@zephyr_z9); JAX + TPU
- Environment code and recipes open-sourced; ~7K environments planned, full task datasets not yet released
- Environment/data-factory paper generates RL tasks from open repositories with agents in the loop for robustness and anti-cheating
