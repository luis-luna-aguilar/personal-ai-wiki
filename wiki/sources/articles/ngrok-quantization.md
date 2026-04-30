---
title: Quantization from the ground up — ngrok blog
type: source
source_type: article
source_file: raw/articles/2026-04-22-ngrokcom-blog-quantization.md
url: https://ngrok.com/blog/quantization
published: 2026-04-22
ingested: 2026-04-22
domains: [models]
---

# Quantization from the ground up

ngrok engineering blog explainer on LLM quantization. Covers: what makes models large (parameters/weights), floating-point precision, quantization mechanics, and accuracy measurement. Uses Qwen3-Coder-Next (80B, 159.4 GB) as the running example.

## Influenced pages

- [Quantization](../../concepts/quantization.md) — new concept page created

## Key claims extracted

- Qwen3-Coder-Next: 80B params, 159.4 GB unquantized
- Frontier models: estimated 1T+ params → 2TB+ RAM without quantization
- Quantization result: ~4× smaller, ~2× faster, 5-10% accuracy loss
- Parameters = weights = the bulk of what an LLM is on disk/in RAM
- FP32 (4B/param) → FP16 (2B) → INT8 (1B) → INT4 (0.5B) precision ladder
