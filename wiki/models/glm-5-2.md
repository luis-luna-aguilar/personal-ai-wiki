---
title: GLM-5.2
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-06-17
sources: [ainews-glm-52-june-2026]
---

# GLM-5.2

Z.ai's June 2026 open-weight frontier model. MIT-licensed, 744B total / 40B active MoE, 1M context. Released opportunistically right after the Fable 5 export-control ban; positioned as the practical open alternative for teams that lost access to the strongest closed frontier models.

## Current status (as of 2026-06-17)

- MIT license; 744B total / 40B active MoE; 1M context window
- Two reasoning modes: high and max
- Pricing: $1.4 / $4.4 per million input / output tokens (same as GLM-5.1)
- **IndexShare:** reuses one sparse-attention indexer across four layers → 2.9× lower FLOPs at 1M context vs naive sparse attention
- **MTP (Multi-Token Prediction):** speculative decoding acceptance +20% over prior version
- **Anti-reward-hacking during RL training:** LLM judge blocked suspicious tool calls, returned dummy info, let trajectories continue — an unusually transparent description of RL reward gaming mitigation

## Benchmarks (independent, June 2026)

- **FrontierSWE / DeepSWE:** #3 (behind Fable 5 [banned] and Opus 4.8)
- **Design Arena:** #1 (Fable 5 unavailable)
- **Agent Arena:** #10 overall / #1 open-weight
- **Code Arena (frontend):** #2 (behind Fable 5 [unavailable] → effectively #1 accessible)
- **Terminal-Bench 2.1:** 81.0 (vs 62.0 for GLM-5.1)

Practitioners described it as the first open-weight model they could comfortably substitute for Opus/GPT-class coding workflows. The timing — released immediately after Fable 5's suspension — amplified adoption intent.

## Strengths

- MIT license: no usage restrictions, self-hostable
- IndexShare enables genuine 1M-context use without prohibitive compute cost
- Strong independent benchmark validation (not just vendor-reported)
- Transparent RL training story

## Weaknesses / caveats

- FrontierSWE still behind Fable 5 and Opus 4.8 when Fable is available
- Benchmark positions reflect a week where the top closed model (Fable 5) was unavailable globally

## Recent changes

- [2026-06-17] Released; MIT license; #1 open-weight Agent Arena; #1 Design Arena; #2 Code Frontend; Terminal-Bench 2.1: 81.0; supersedes GLM-5.1

## Sources

- [GLM-5.2 release coverage](../sources/newsletters/ainews-glm-52-june-2026.md)
