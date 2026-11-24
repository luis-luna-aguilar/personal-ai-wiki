---
title: RecursiveSI/flint model card — Hugging Face
type: source
source_type: article
source_file: raw/articles/2026-11-24-huggingfaceco-recursivesi-flint.md
url: https://huggingface.co/RecursiveSI/flint
published: 2026-10-21
ingested: 2026-11-24
domains: [models, coding]
---

# RecursiveSI/flint model card — Hugging Face

Recursive's Hugging Face model card for Flint, its open-weight MoE for coding agents: architecture, claimed benchmark scores and evaluation settings, SGLang serving kit, recommended sampling, training stages, limitations and the Apache 2.0 license. The card is undated; the release date comes from AINews's launch coverage.

## Influenced pages

- [Recursive Flint](../../models/recursive-flint.md) — new page
- [State of Models](../../state-of/models.md) — added to Coding models

## Key claims extracted

- 39.8B total parameters, about 2.5B active per token (2.2B excluding the output head); 49 layers (2 dense, 47 MoE); 256 routed experts, 6 per token, plus a shared expert
- 35 sliding-window layers (513-token window) and 14 full-attention layers; 262,144-token context; knowledge cutoff June 2026
- Terminal-Bench 2.1 54.9% (Terminus 2; solutions found via web retrieval counted as failures), SWE-bench Pro v2 89.7%, SWE-bench Verified 74.2% (mini-swe-agent); average pass@1 over at least five attempts
- Runs on one B300 or H200 per replica with the bundled SGLang kit; quantized variants for NVIDIA and Apple Silicon; no Transformers modeling code yet
- Trained from scratch through pretraining, mid-training, SFT and RL
- Recommended: temperature 1.0, top-p 0.95, top-k 20, at least 32,768 output tokens for hard problems
- Apache 2.0; hosted API terms are separate
