---
title: Weight-space programming
type: concept
domains: [models, agents]
tags: []
as_of: 2026-11-13
sources: [weight-space-programming-takehi-2026-11, cmpnd-dspy-wsp-2026-11-13]
---

# Weight-space programming

Weight-space programming treats a neural network's weights like a program: a frontier model reads them to work out what the network computes, then edits them directly to change it, by reasoning instead of by training. The term comes from a research post by Takehi, Teoh, Zhang and Khattab (public by 3 November 2026), who stress that it names an emerging model capability, not a method.

## Current status (as of 2026-11-13)
- **Reading.** From raw weights alone, GPT-6 Astra told which game a small network was trained on. It could not tell a sycophantic Gemma 3 270M from an honest one by weights alone, but did once shown attention patterns.
- **Fixing.** With no gradients and 10–50 test runs, Astra edited 0.016% of Qwen3.5-0.8B's weights to remove a known thinking-loop fault: MATH-500 rose from 7.9% to 48.1% and IFEval roughly tripled. It could not improve Gemma 3 270M, whose errors were ordinary reasoning mistakes rather than one faulty component.
- **Writing.** Astra wrote small game-playing networks from scratch that beat PPO trained for 100M steps; with 50 test runs, its 1.5M-parameter Go network beat an equal-sized one trained on 20M games.
- **Tooling.** Cmpnd's experimental [`dspy-wsp`](https://github.com/cmpnd-ai/dspy-wsp) DSPy optimizer applies it to small [decision models](decision-models.md): 25 test runs of GPT-6 Astra (about $5–10) added 1.9–16.1 accuracy points on five open models from 0.6B to 9B, and the edited model runs locally (Mac via MLX, or PyTorch/vLLM on NVIDIA).
- **Uptake.** Within days the post was replicated (Simon Willison, Hugging Face) and extended to robot policies and quantum circuits, and a benchmark (IWIBench) appeared; the authors are building their own benchmark and harness.

## Why it matters
Until now the wiki's model-improvement loops change weights only through training runs ([Agent improvement loop](agent-improvement-loop.md), Palantir AutoResearch). Direct edits touch a tiny share of weights, so in principle they avoid the forgetting that fine-tuning causes and need no dataset. The authors also see it as a new route for auditing models from their weights and for [mechanistic interpretability](mechanistic-interpretability.md).

## Caveats
- Results are on small models (under 1B parameters for language models); the authors say context length and harnesses limit it today.
- Fixing a known fault is not the same as adding skill: the large Qwen gain came from removing loops, and the non-looping Gemma did not improve.
- Cmpnd calls `dspy-wsp` very experimental; runs on text-generating LLMs are long, costly and may not help.

## Recent changes
- [2026-11-13] Page created: the weight-space programming research post (public by 3 November) and Cmpnd's `dspy-wsp` optimizer for decision models.

## Related
- [Agent improvement loop](agent-improvement-loop.md) — model improvement through training runs, which this skips
- [Decision models](decision-models.md) — the small models `dspy-wsp` targets
- [Mechanistic interpretability](mechanistic-interpretability.md) — reading networks from the inside with purpose-built tools

## Sources
- [Sparks of Weight-Space Programming — Takehi, Teoh, Zhang, Khattab](../sources/articles/weight-space-programming-takehi-2026-11.md)
- [Cmpnd — Weight-Space Programming with DSPy](../sources/articles/cmpnd-dspy-wsp-2026-11-13.md)
