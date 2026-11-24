---
title: Cmpnd — Weight-Space Programming with DSPy
type: source
source_type: article
source_file: raw/articles/2026-11-24-cmpndai-blog-weight-space-programming-dspyhtml.md
url: https://cmpnd.ai/blog/weight-space-programming-dspy.html
published: 2026-11-13
ingested: 2026-11-24
domains: [models, agents]
---

# Cmpnd — Weight-Space Programming with DSPy

Drew Breunig's company Cmpnd releases `dspy-wsp`, a prototype DSPy optimizer that brings weight-space programming to existing DSPy programs. The post has no date; Every's 15 November 2026 newsletter says it was released "last Friday", 13 November.

## What it does
The `WeightSpace` optimizer hands a small model's weights to a "writer" LLM (GPT-6 Astra at maximum reasoning effort in the tests). In turns, the writer runs the program on practice examples, looks at layer activity, edits weights in a sandboxed Python kernel with no GPU, network or gradients, and re-tests. When a fixed budget of forward passes runs out, it keeps the best edit as a patch or full checkpoint. Works with DSPy 3.5; `pip install dspy-wsp`.

## Results
- Five open decision models from 0.6B to 9B, Typed Decisions benchmark, 400 held-out cases, 25 forward passes, about $5–10 per model.
- WeightSpace alone: +1.9 to +16.1 points; with Cmpnd's ReAnchor (refits each question's decision thresholds): +6.5 to +20.0. Examples: d1-omni-600M 50.9% → 69.1%; d1-2B 60.6% → 77.9%; Clef-Flash 68.8% → 75.3%.
- Edited models run locally: MLX on Apple silicon, PyTorch on Linux; 2B models used about 6 GB. A Mac or a GPU with 4 GB can run optimizations on d1-omni-600M.

## Caveats
- "Very experimental", tested in a handful of environments and model families; editing runs on text-generating LLMs are long, costly and may not help.

## Influenced pages
- [Weight-space programming](../../concepts/weight-space-programming.md) — tooling bullet
- [Decision models](../../concepts/decision-models.md) — tuning-after-release bullet
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — named as the packaged tool

## Key claims extracted
- `dspy-wsp` improved every one of five open decision models tested
- Cost about $5–10 of GPT-6 Astra usage per model
- Combines with ReAnchor for +6.5 to +20.0 points
