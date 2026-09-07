---
title: Laguna S 2.1
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [open-weights, agentic]
as_of: 2026-07-23
sources: [poolside-model-factory-interview-2026-07-23, ainews-cybersecurity-top-of-mind-2026-07-22, ainews-laguna-kratsios-2026-07-23]
---

# Laguna S 2.1

Poolside AI's flagship open-weight coding model, released 2026-07-22/23. A 118B-total / 8B-active mixture-of-experts model with a 1M-token context window, released under Poolside's own OpenMDW-1.1 license. Small enough to run locally on a single NVIDIA DGX Spark. Poolside is a Western "neolab" — a from-scratch foundation-model company, not a lab spinout — that raised $500M and builds models through an internal "Model Factory" pipeline (streaming training data, 10,000-20,000 experiments/month, five-to-eight-week training cycles).

## Current status (as of 2026-07-23)

- Benchmarks: 70.2% Terminal-Bench 2.1, 78.5% SWE-bench Multilingual, 59.4% SWE-Bench Pro, 40.4% DeepSWE, 46.2% SWE Atlas Codebase Q&A, 49.7% Toolathlon Verified
- Cheaper than DeepSeek V4 Flash while beating V4 Pro on reported benchmarks
- Independent eval vs. Qwen3.5-122B (single RTX Pro 6000, private test): faster and better tool-calling (109 vs. 103 tok/s, cleaner tool-call syntax, deeper tool chains) but more prone to fabricating facts under pressure — 3 confirmed fabrications vs. 0 in the initial run, cut to 1 across 125 grounding runs after a tokenizer/sampling fix
- Poolside frames the release explicitly as resisting intelligence concentration in "three or four companies" — Eiso Kant says he'd rather see 100 foundation-model companies than five
- Trained end-to-end in 8 weeks via Poolside's Model Factory pipeline

## Strengths

- Strong agentic coding and tool-calling performance for its size class (118B total / 8B active)
- Practical local deployment — fits and runs at usable speed on a single DGX Spark or high-RAM consumer/prosumer hardware
- Detailed, well-regarded technical report (data streaming, reproducibility, Model Factory internals)

## Weaknesses / caveats

- More prone to fact fabrication under pressure than Qwen3.5-122B in one practitioner's private eval; not yet independently corroborated at scale
- Benchmark scores are self-reported by Poolside, not yet placed on a third-party leaderboard (e.g. Artificial Analysis)
- No vision support at launch

## Recent changes

- [2026-07-23] Initial page: Laguna S 2.1 release, benchmark scores, independent Qwen3.5-122B comparison, Poolside's Model Factory framing

## Sources

- [Poolside Laguna S 2.1 — Model Factory interview](../sources/newsletters/poolside-model-factory-interview-2026-07-23.md)
- [AINews — AI Cybersecurity becomes top of mind](../sources/newsletters/ainews-cybersecurity-top-of-mind-2026-07-22.md)
- [AINews — Laguna S 2.1 / Kratsios distillation accusation](../sources/newsletters/ainews-laguna-kratsios-2026-07-23.md)
