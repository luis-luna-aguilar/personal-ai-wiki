---
title: AINews — Flint launch and local serving (2026-10-22)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
url: https://www.latent.space/p/ainews-openais-patch-the-planet-program
published: 2026-10-22
ingested: 2026-11-24
domains: [models, coding]
---

# AINews — Flint launch and local serving (2026-10-22)

The Flint story from AINews's 2026-10-22 issue (Other News plus the r/LocalLlama recap): Recursive's local coding MoE launched with broad local-serving support, claimed benchmark scores, measured local speeds, and the Eureka Machine's role in building it.

## Influenced pages

- [Recursive Flint](../../models/recursive-flint.md) — local speeds, availability, community reception, Eureka Machine contribution
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — Flint as a shipped model designed partly by an automated research loop

## Key claims extracted

- Apache 2.0 coding MoE, ~40B total / 2.5B active, 262K context; LM Studio says about 24GB locally; positioned as an on-device complement to frontier cloud agents
- Advertised short-context speeds over 125 tok/s on a MacBook Pro and 150 tok/s on RTX Spark; a user measured 114–132 tok/s on an M5 Max with int4 MLX
- NVIDIA (GTC Berlin) claims over 220 tok/s on a 64GB RTX Spark; Eureka Machine kernels improved RTX Spark generation speed by 55% without changing weights; NeMo Automodel SFT/LoRA and NeMo RL GRPO support
- Eureka Machine took part in ideation, implementation and validation (sparse architecture, low-bit training, kernels); claimed 71% size reduction with almost no quality loss; built from scratch in under four months
- Day-zero vLLM (500 tok/s on one GB200 at 100K context, NVFP4) and free OpenRouter access
- r/LocalLlama: the "35B-A3B"-class model people wanted, but Qwen3.8-27B made it less surprising
