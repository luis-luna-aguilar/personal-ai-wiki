---
title: Quantization
type: concept
domains: [models]
as_of: 2026-07-15
sources: [ngrok-quantization, local-offline-agents-2026-04-29, gpt-56-raising-concerns-2026-07-15]
---

# Quantization

A compression technique that reduces the precision of a model's parameters (weights) to make the model smaller and faster to run, at a modest accuracy cost. The headline result: 4× smaller, 2× faster, 5-10% accuracy loss.

## Current status (as of 2026-07-15)

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

A July 2026 example pushes past standard INT4: PrismML compressed Alibaba's Qwen 3.6 27B into two Apache-2.0 variants — "Ternary Bonsai 27B" (5.9GB, 1.71 effective bits/parameter) and a "1-bit Bonsai 27B" (3.9GB, 1.125 effective bits) — claiming the 1-bit variant fits on an iPhone 17 Pro at 90% of the original model's performance (PrismML's own figure, not independently benchmarked). A developer-preview API is available via Together AI. Billed as the first 27B-class model that runs on a phone.

## Recent changes

- [2026-07-15] PrismML ships Bonsai 27B, a sub-2-bit quantization of Qwen 3.6 27B claimed to run on an iPhone 17 Pro at 90% of original performance.

## Sources

- [Quantization from the ground up — ngrok blog](../sources/articles/ngrok-quantization.md)
- [Local and offline agents become more credible](../sources/newsletters/local-offline-agents-2026-04-29.md)
- [The Code — GPT-5.6 is raising concerns (PrismML Bonsai 27B)](../sources/newsletters/gpt-56-raising-concerns-2026-07-15.md)
