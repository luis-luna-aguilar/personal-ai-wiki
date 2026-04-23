---
type: proposal
source: raw/articles/2026-04-22-ngrokcom-blog-quantization.md
status: pending
created: 2026-04-22
---

# Proposal: Quantization — concept page from ngrok blog

## Summary

Well-written ground-up explainer of LLM quantization from the ngrok blog. Covers: why models are large (parameters), how floating-point precision works, how quantization compresses floats, and how to measure accuracy loss. The headline claim: 4× smaller, 2× faster, 5-10% accuracy loss. Warrants a short concept page as a reference for understanding model size/speed tradeoffs that appear frequently in discussions about running models locally.

## Intended changes

- [x] **Create** `wiki/concepts/quantization.md` — new concept page
    > See draft below

- [x] **Create** `wiki/sources/articles/ngrok-quantization.md` — source summary
    > See draft below

## Page drafts

### wiki/concepts/quantization.md (new)

```md
---
title: Quantization
type: concept
domains: [models]
as_of: 2026-04-22
sources: [ngrok-quantization]
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

## Sources

- [[sources/articles/ngrok-quantization]]
```

### wiki/sources/articles/ngrok-quantization.md (new)

```md
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

- [[concepts/quantization]] — new concept page created

## Key claims extracted

- Qwen3-Coder-Next: 80B params, 159.4 GB unquantized
- Frontier models: estimated 1T+ params → 2TB+ RAM without quantization
- Quantization result: ~4× smaller, ~2× faster, 5-10% accuracy loss
- Parameters = weights = the bulk of what an LLM is on disk/in RAM
- FP32 (4B/param) → FP16 (2B) → INT8 (1B) → INT4 (0.5B) precision ladder
```
