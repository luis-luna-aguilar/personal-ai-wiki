---
title: Cohere Command A+
type: model
domains: [models, agents]
subcategory: open-weight-model
tags: [cohere, open-weights]
as_of: 2026-05-21
sources: [cohere-command-a-plus-launch, ainews-erdos-benchmarks-cluster-2026-05-21]
---

# Cohere Command A+

Cohere's first fully open model release: Command A+ ships under an Apache 2.0 license, unifying and surpassing the prior Command A family (base, Reasoning, Vision, Translate) into one MoE model built for enterprise agentic workloads, born out of a year deploying Cohere's North workspace product.

## Current status (as of 2026-05-21)

- 218B total / 25B active MoE, 128K input context (64K max generation), text + image + tool-use input, 48 languages (up from 23 on prior Command A models)
- Runs on as little as 1x NVIDIA Blackwell GPU or 2x H100s at W4A4 quantization; ships in BF16/FP8/W4A4 on Hugging Face; day-0 vLLM support
- Artificial Analysis Intelligence Index: 37 (cited in Cohere's own post); AINews summarizes AA's placement as roughly Claude 4.5 Haiku territory, with especially strong non-hallucination behavior and decent speed but weaker scientific reasoning and coding than top peer models
- Cohere's own benchmarks show large gains over Command A Reasoning: 𝜏²-Bench Telecom 37% → 85%, Terminal-Bench Hard (agentic coding) 3% → 25%, MMMU 75.1%, MathVista 80.6%
- Community architecture analysis (unconfirmed by Cohere's own post): parallel transformer blocks, large shared-expert usage, LayerNorm over RMSNorm, and a comparatively shallow 32 layers

## Strengths

- Apache 2.0 with no usage restrictions — Cohere's first fully open model, per co-founder @aidangomez (via AINews); a lab that had kept its strongest models closed now ships fully open weights
- Efficiency-first design: quantization support, a faster tokenizer (~20% fewer tokens for Arabic, ~16-18% for Korean/Japanese), and 47-63% throughput gains over Command A Reasoning depending on quantization (Cohere's own figures)
- Strong non-hallucination behavior per Artificial Analysis (via AINews)

## Weaknesses / caveats

- Intelligence Index of 37 trails the strongest open-weight coding/agent models tracked in [State of Models](../state-of/models.md) (for example DeepSeek V4)
- Weaker coding and scientific reasoning than top peers per Artificial Analysis (via AINews)
- Architecture details (parallel transformer blocks, LayerNorm, 32-layer depth) come from community analysis, not Cohere's own announcement

## Recent changes

- [2026-05-21] Command A+ released: 218B/25B MoE, Apache 2.0, 48 languages, AA Intelligence Index 37

## Sources

- [Introducing Command A+](../sources/articles/cohere-command-a-plus-launch.md)
- [AINews — Erdős result and agent-benchmark cluster (Command A+ recap)](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
