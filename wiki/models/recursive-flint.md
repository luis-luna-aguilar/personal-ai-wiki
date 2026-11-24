---
title: Recursive Flint
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights]
as_of: 2026-10-21
sources: [huggingface-recursive-flint-2026-10-21, ainews-recursive-flint-2026-10-22, latent-space-socher-recursive-2026-09-14]
---

# Recursive Flint

Recursive's open-weight mixture-of-experts model for coding agents, released 2026-10-21 under Apache 2.0. It has 39.8B total and about 2.5B active parameters per token and is built to run locally: Recursive positions it as an on-device complement to frontier cloud agents, not a replacement. Recursive (Richard Socher's company) says its automated research system, the Eureka Machine, helped design it.

## Current status (as of 2026-10-21)

- Claimed scores: Terminal-Bench 2.1 54.9% (Terminus 2 harness; web-retrieved solutions counted as failures), SWE-bench Pro v2 89.7%, SWE-bench Verified 74.2% (mini-swe-agent).
- 262K-token context; 49 layers (2 dense, 47 MoE), 256 routed experts with 6 per token plus a shared expert, mixed sliding-window and full attention; knowledge cutoff June 2026.
- Runs in about 24GB locally (LM Studio). Users measured 114–132 tok/s on an M5 Max (int4 MLX); NVIDIA cites over 220 tok/s on a 64GB RTX Spark; vLLM reports 500 tok/s on one GB200 at 100K context (NVFP4).
- Day-zero support in vLLM, SGLang (one B300 or H200 per replica) and OpenRouter (free at launch); NeMo fine-tuning recipes. No Transformers modeling code yet.

## Built by an automated research loop

Trained from scratch in under four months. Recursive says the Eureka Machine, which proposes ideas, implements them, runs experiments and picks follow-ups, contributed the sparse architecture, low-bit training and kernels, for a claimed 71% size reduction with almost no quality loss. Its kernels raised generation speed on RTX Spark by 55% without changing weights. See [Agent improvement loop](../concepts/agent-improvement-loop.md) for Recursive's earlier research-automation results.

## Weaknesses / caveats

- No independent benchmark results yet; comparison scores on the model card mix Recursive-measured and developer-reported numbers.
- r/LocalLlama read it as the "35B-A3B"-class model people wanted, but arriving after [Qwen 3.8 27B](qwen-3-8-27b.md) made it less of a surprise.
- Long reasoning can exhaust the output budget; Recursive recommends at least 32K output tokens for hard problems.

## Recent changes

- [2026-10-21] Released on Hugging Face (Apache 2.0) with day-zero vLLM, SGLang and OpenRouter support.

## Sources

- [RecursiveSI/flint model card — Hugging Face](../sources/articles/huggingface-recursive-flint-2026-10-21.md)
- [AINews — Flint launch and local serving (2026-10-22)](../sources/newsletters/ainews-recursive-flint-2026-10-22.md)
- [Latent Space — Richard Socher on AI for AI research](../sources/newsletters/latent-space-socher-recursive-2026-09-14.md)
