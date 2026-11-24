---
title: 'AINews — Inference systems: DeepInfer economics, TorchTPU, EAGLE-4 (22 October 2026)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
url: https://www.latent.space/p/ainews-openais-patch-the-planet-program
published: 2026-10-22
ingested: 2026-11-24
domains: [models]
---

# AINews — Inference systems: DeepInfer economics, TorchTPU, EAGLE-4 (22 October 2026)

The inference-systems story from AINews's 2026-10-22 issue (the "Inference Systems" section plus the r/LocalLlama recap): follow-up accounting on DeepInfer's throughput figures, Google's open-source TorchTPU, and the EAGLE-4 speculative decoder.

## Influenced pages

- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — TorchTPU and EAGLE-4 in the open inference serving bullet

## Key claims extracted

- DeepInfer's 1.5M input tokens/s per prefill accelerator includes cache hits; excluding them it is about 60K at a 96% hit rate; decode about 14K output tokens/s per accelerator
- Google open-sourced TorchTPU for training and serving through PyTorch tooling; SGLang's TorchTPU plugin reportedly powers production inference at Meta; vLLM-TorchTPU adds prefix caching, speculative decoding and disaggregated serving
- EAGLE-4: source-available speculative decoding with hardware/workload-calibrated draft trees; claimed 3.59x over vanilla decoding on Qwen3.8-27B (vs 2.57x DSpark, 2.80x DFlash 2); gains shrink at higher concurrency; draft model about 3 GB larger than DFlash2
