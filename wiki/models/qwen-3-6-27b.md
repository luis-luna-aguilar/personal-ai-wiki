---
title: Qwen 3.6 27B
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-05-01
sources: [ainews-2026-04-23, the-code-2026-04-23, qwen-3-6-27b-aa-2026-05-01]
---

# Qwen 3.6 27B

Alibaba's dense 27B open-weight coding model. Despite being 14× smaller than the previous 397B-param Qwen 3.6 MoE flagship, it outperforms it on every major coding benchmark — the clearest current signal that dense architecture plus better training can beat raw parameter count.

## Current status (as of 2026-04-23)

- 27B-parameter dense architecture (not MoE); Apache 2.0 license
- Unified thinking / non-thinking modes; native multimodal reasoning over images and video
- SWE-bench Verified 77.2 (vs 76.2 prior 397B model), SWE-bench Pro 53.5 (vs 50.9), Terminal-Bench 2.0 59.3 (vs 52.5), SkillsBench 48.2 (vs 30.0)
- Day-0 ecosystem: vLLM, Unsloth 18 GB GGUF, llama.cpp, Ollama; FP8 quantized variant available on Hugging Face
- Early user reports strong for local frontend/design and image tasks
- Artificial Analysis follow-up, as summarized by AINews, ranked Qwen 3.6 27B as the leading open-weight model under 150B parameters with an Intelligence Index score of 46; the same summary flags high output-token cost on the suite, roughly 21× Gemma 4 31B

## Strengths

- Best open coding benchmark scores at release for a sub-30B model
- Dense architecture: simpler to deploy than MoE, no expert routing overhead
- Runnable locally under 20 GB RAM with quantization

## Weaknesses / caveats

- Benchmark scores from Alibaba's release post; independent verification pending
- Scaffold choice dominates raw benchmarks: Qwen3.6-35B jumped 19% → 78.7% on Polyglot with a better agent harness — model numbers must be read with harness context

## Recent changes

- [2026-05-01] Artificial Analysis (via AINews) ranked Qwen 3.6 27B #1 open-weight under 150B with Intelligence Index 46; flagged ~21× Gemma 4 31B output-token cost on evaluation suite
- [2026-04-23] Released; day-0 vLLM/Unsloth/llama.cpp/Ollama support; beats prior 397B MoE on all major coding benchmarks

## Sources

- [AINews — Tasteful Tokenmaxxing](../sources/newsletters/ainews-2026-04-23.md)
- [The Code — OpenAI drops a privacy focused model](../sources/newsletters/the-code-2026-04-23.md)
- [Qwen 3.6 27B Artificial Analysis follow-up](../sources/newsletters/qwen-3-6-27b-aa-2026-05-01.md)
