---
title: DiffusionGemma
type: model
domains: [models]
subcategory: open-weight-model
tags: [google, open-weights]
as_of: 2026-06-11
sources: [ainews-open-models-june-2026]
---

# DiffusionGemma

Google's DiffusionGemma is an experimental 26B mixture-of-experts text model that generates text through block denoising rather than the standard autoregressive next-token prediction used by every current frontier model. Released June 10–11 2026 under Apache 2.0. Built on Gemma 4.

## Current status (as of 2026-06-11)

- Google / Google DeepMind release; Apache 2.0 license
- 26B MoE (3.8B active parameters); Gemma 4 base
- Generates text by simultaneously denoising a block of 256 tokens rather than predicting token by token
- Claims 4× faster output than standard diffusion text model baselines
- First diffusion LLM natively supported in vLLM: 1,200+ output tok/s at batch size 1 on H200 with FP8
- Runs locally on ~18GB-class hardware (llama.cpp, Unsloth)
- Framed by the community as a research artifact and direction, not a production replacement for autoregressive models

## Why it matters

DiffusionGemma revives questions around iterative refinement, constrained editing, fill-in-the-middle, and error correction that are inherently difficult for autoregressive models. Potential advantages in tasks where parallel block generation is preferable to strict left-to-right decoding.

The serving story landed immediately: vLLM added native support, and the model runs locally on consumer hardware — unusual for a model at this scale with this architectural novelty.

## Weaknesses / caveats

- Explicitly framed as experimental and a research direction, not a benchmark-leading production model
- Quality comparisons against frontier autoregressive models have not been published at launch
- Architecture unfamiliarity may limit adoption until tooling and prompting patterns mature

## Recent changes

- [2026-06-11] Released; first diffusion LLM in vLLM; community reaction: strong on systems side, more cautious on capability claims

## Sources

- [AINews — Open models, Model Labs vs Agent Labs (June 11)](../sources/newsletters/ainews-open-models-june-2026.md)
