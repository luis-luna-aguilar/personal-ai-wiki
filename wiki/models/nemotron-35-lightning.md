---
title: Nemotron 3.5 Lightning
type: model
domains: [models]
subcategory: open-weight-model
tags: [open-weights, agentic]
as_of: 2026-08-12
sources: [unsloth-desktop-chatgpt-linux-2026-08-12]
---

# Nemotron 3.5 Lightning

NVIDIA's small, fast open-weight model for always-on agent workloads — a compact sibling to the larger [Nemotron 3 Ultra](nemotron-3-ultra.md), tuned for high-volume tool use rather than general chat.

## Current status (as of 2026-08-12)

- 31.6B total / 3.6B active MoE; OpenMDW-1.1 license; NVFP4 and BF16 weight releases
- Artificial Analysis Intelligence Index 24 — roughly gpt-oss-120b tier at a fraction of the size; ~670 tok/s median serving in pre-release testing
- Strong agentic results for its size: GDPval-AA v2 Elo 824, Terminal-Bench v2.1 24% — both large jumps over the prior Nemotron 3 Nano
- Harvey post-trained it on Legal Agent Bench: 0% to 8.3% on held-out tasks, beating Claude Opus 4.6 and Nemotron 3 Ultra in that setup while cutting average output from 90k to 37k tokens
- Day-0 availability across Together AI, Ollama, Baseten, vLLM, and Perplexity API

## Why it matters

Reinforces the pattern of pairing a cheap, fast execution model with a stronger planner via routing rather than chasing general-chat capability — NVIDIA is explicitly positioning Lightning as a "local agent workforce" complementing larger planning models.

## Recent changes

- [2026-08-12] Launched: initial benchmarks, day-0 provider support, and Harvey's Legal Agent Bench post-training result

## Sources

- [Local AI tooling: Unsloth Desktop, ChatGPT desktop for Linux (Nemotron 3.5 Lightning launch)](../sources/newsletters/unsloth-desktop-chatgpt-linux-2026-08-12.md)
