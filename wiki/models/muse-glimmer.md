---
title: Muse Glimmer
type: model
domains: [models, agents]
subcategory: open-weight-model
tags: [meta, open-weights, agentic]
as_of: 2026-08-11
sources: [anthropic-riemann-hypothesis-2026-08-11]
---

# Muse Glimmer

Muse Glimmer is Meta Superintelligence Labs' first genuinely open-weight frontier-adjacent model: a 30B dense, multimodal, agent-focused model released under Apache 2.0 on 2026-08-11, alongside a promise to open Muse Spark 1.2's own weights "soon." Unlike a conventional base-then-post-train release, Glimmer was logit-distilled from Muse Spark and trained from the outset on agentic traces.

## Current status (as of 2026-08-11)

- 30B dense parameters, interleaved text+image input via a dedicated perception encoder, 100+ languages, controllable reasoning effort
- Designed for always-on local agents: ~4-bit quantization brings the model under 20GB, paired with a lightweight DFlash speculative-decoding drafter for faster on-device generation; ~60GB at BF16
- 128K context; memory-efficient hybrid attention (community notes: Gemma-4-style hybrid attention plus scale-free QK norm, larger vision depth, longer sliding-window attention)
- Benchmarked on agent-specific suites: DeepSearch QA, MCP-Atlas, τ³-Bench, SWE-Bench
- Planned day-0/near-day-0 support: Ollama, LM Studio, Unsloth, torchtitan, llama.cpp, MLX, ExecuTorch, vLLM, SGLang; weights on Hugging Face

## Benchmarks

- Artificial Analysis Intelligence Index: 35 — just behind Qwen3.6-27B (38) and near Kimi K2.5 (36)
- Artificial Analysis Openness Index: 44 — a strong score reflecting the Apache 2.0 license and local-deployment focus
- Does well on Tau3-Banking tool-use follow-up; comparatively weak on hallucination/knowledge calibration and general agentic knowledge work versus similarly-sized peers

## Why it matters

Glimmer marks Meta's return to shipping genuinely open weights after Muse Spark 1.1 pivoted to a closed, metered API — arriving alongside Zuckerberg's sequel "Personal Superintelligence" essay reaffirming Meta's stated strategy of keeping frontier capability in individual hands rather than institutions. It's a small-footprint, locally-deployable agent model rather than a flagship capability play.

## Caveats

- Benchmark placement (AA Intelligence Index 35) trails several existing open-weight peers on raw capability; Glimmer's pitch is local-agent deployability, not frontier intelligence
- Hallucination/knowledge-calibration weakness is a real caveat for any workflow requiring factual reliability
- All benchmark figures here are third-party (Artificial Analysis) via an AINews summary, not independently verified by this wiki

## Sources

- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
