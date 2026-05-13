---
title: Quantization
type: concept
domains: [models]
as_of: 2026-05-05
sources: [ngrok-quantization, local-offline-agents-2026-04-29]
---

# Quantization

A compression technique that reduces the precision of a model's parameters (weights) to make the model smaller and faster to run, at a modest accuracy cost. The headline result: 4× smaller, 2× faster, 5-10% accuracy loss.

## Current status (as of 2026-04-22)

- Standard technique for running large models on consumer hardware
- Typical tradeoff: INT4 quantization → ~4× size reduction, ~2× inference speed, 5-10% accuracy drop
- Qwen3-Coder-Next (80B params) is 159.4 GB unquantized; quantized it can run on a laptop
- Frontier models (estimated 1T+ params) would require 2TB+ RAM without quantization
- Common formats: GGUF (llama.cpp), GPTQ, AWQ — each with slightly different quality/speed tradeoffs

## How it works

LLMs store each parameter as a floating-point number. A 32-bit float gives high precision but uses 4 bytes. Quantization replaces floats with lower-precision integers:

- **FP32** (32-bit float): 4 bytes/param, highest precision
- **FP16 / BF16** (16-bit): 2 bytes/param; standard training precision
- **INT8**: 1 byte/param; moderate speedup
- **INT4**: 0.5 bytes/param; most common for local deployment; 4× smaller than FP16

The model's mathematical behavior changes slightly because values are rounded to the nearest representable integer. Most parameters in a large model contribute small, redundant adjustments — rounding them introduces minor errors that, in aggregate, cause a 5-10% accuracy drop.

## Why it matters

Quantization is what makes local model deployment practical. Without it, running an 80B model requires a $100K+ server. With INT4 quantization, it fits on a modern workstation. This matters for:

- **Privacy:** keeping inference local rather than sending prompts to an API
- **Cost:** eliminating per-token API costs for high-volume use
- **Latency:** local inference has no network round-trip
- **Open-weight models:** quantization is the primary reason open-weight models (Qwen3, Llama, etc.) are practically usable

## Local agent feasibility (as of 2026-04-29)

Quantization is increasingly the enabling layer for local and offline agents. AINews reports that hardware-aware Hugging Face model selection is now common practice — users match model size to local GPU/CPU capacity after quantization. Gemma family models running via MLX on Apple Silicon and browser-local agents running quantized models client-side are moving from demos toward practical workflows. The pattern: quantization + hardware-aware selection makes capable offline agents accessible without cloud API calls.

## Sources

- [Quantization from the ground up — ngrok blog](../sources/articles/ngrok-quantization.md)
- [Local and offline agents become more credible](../sources/newsletters/local-offline-agents-2026-04-29.md)
