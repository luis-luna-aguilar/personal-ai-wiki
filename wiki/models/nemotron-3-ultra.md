---
title: Nemotron 3 Ultra
type: model
domains: [models]
subcategory: open-weight-model
tags: [open-weights, agentic]
as_of: 2026-06-02
sources: [ainews-cosmos-nemotron-june-2026]
---

# Nemotron 3 Ultra

NVIDIA's first-party frontier open-weight model, released at Computex 2026. A 550B total / 55B active MoE with a hybrid Mamba/attention + LatentMoE + native Multi-Token Prediction architecture, positioned for long-context agentic inference at high serving throughput.

## Current status (as of 2026-06-02)

- 550B total / ~55B active parameters (~10% active weight ratio — less sparse than Kimi K2 / DeepSeek V4 at ~3%)
- Hybrid Mamba/attention + LatentMoE + native MTP (Multi-Token Prediction)
- 1M context window
- 300-400+ tokens/second serving speed
- NVFP4 pretraining on 20T tokens
- 47.7 Intelligence Index (BF16) — claimed top US open-weight model at launch
- **OpenMDW 1.1** license (permissive open-model license)
- Day-0: OpenRouter, vLLM support

## Strengths

- Unusually high serving throughput for a model at this scale — 300-400+ tok/s makes long-context agent loops practically affordable
- First NVIDIA-origin open-weight model competing directly on agent benchmarks
- ~10% active weight ratio is higher than DeepSeek/Kimi MoEs, which may improve practical routing quality at the cost of slightly higher compute-per-token

## Weaknesses / caveats

- 10% active weight is less sparse than leading MoEs, meaning higher cost per token in inference than K2/DeepSeek at comparable total-param scale
- OpenMDW 1.1 license — less permissive than MIT; check enterprise use terms before deployment
- Claims are from NVIDIA's own launch materials; independent third-party benchmarks pending

## Recent changes

- [2026-06-02] Launched at Computex 2026; initial benchmarks and placement

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra (June)](../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
