---
title: Neurons as an Interpretable Basis — Goodfire
type: source
source_type: article
source_file: raw/articles/2026-11-24-goodfirecom-research-neurons-as-an-interpretable-basis.md
url: https://www.goodfire.com/research/neurons-as-an-interpretable-basis
published: 2026-11-15
ingested: 2026-11-24
domains: [models]
---

# Neurons as an Interpretable Basis — Goodfire

Goodfire's technical companion to Nick Cammarata's essay [Neural Networks Are Already Clean](goodfire-already-clean-2026-10.md), and the first post in its series on "native interpretability": studying a network through its own units instead of through a learned replacement such as a sparse autoencoder. The page carries no date. Every's 15 November 2026 newsletter says it came out that week, so `published` is inferred.

## The question
Can individual neurons (the hidden units of a transformer's MLP layers) be studied directly, or are they too mixed to read? The team tests three ways neurons could fail as units: rarely having a clear role, firing on too wide a range of inputs to describe briefly, or resisting descriptions precise enough to predict them.

## What they did
They ran 10 billion tokens through Qwen3.6-35B-A3B (an open mixture-of-experts model with about 5 million neurons), collected examples at many activation strengths, traced which neurons feed each neuron and which read its output, and had a frontier model (Claude Fable 5.0/5.1, Opus 5.5 or GPT-6 Sol) in a research harness, the "Neuron Scientist", write and test descriptions for samples of neurons (500 for the detection test). All scores are computed on held-out text.

## Findings
- **Sparse already.** Switching off the weakest 92.2% of activations leaves the model close to the original (1.2–2.2 points lower on likelihood benchmarks). About 91M tokens of fine-tuning and 9M of RL restore full reasoning scores. Most of a neuron's effect comes from its top and bottom 3% of firings.
- **Few jobs per neuron.** In a 5,468-pole sample, 69% are dominated by one "mode" (a coherent group of jobs): 47% have a single one, and in 46% of multi-mode poles the main mode does ≥90% of the damage. Where there are several, they are few and can be told apart by what feeds them and what reads them.
- **Predictable from a sentence.** Given the description, a judge model picks the snippet that makes a neuron fire 95% of the time in the strongest range against random text, and 89% against text from the same expert (chance 50%). Opus 5.5 scores 86% on the weakest band studied.
- **Simulatable.** Replacing a neuron's real activations with ones predicted from its description recovers 73% of what a perfect reader recovers in the top bands, with no model trained for the task.
- **Steerable.** For 94% of neurons the agent can write text that fires the neuron harder than anything in the 10B-token corpus.
- A popular counterexample, a Qwen3-32B "Colorado" neuron that also fires on the Tornado web framework, gets about 98.8% of its effect from place-related text; the Tornado link is a real association in the model (it wrongly places Tornado in Colorado), not storage noise.

## Limits (authors' own)
- One model family; generalization to other models and behaviors is untested.
- Weak activations, which make up most firings, are not explained.
- Some neurons are genuinely mixed, and some behavior remains unexplained.

## Influenced pages
- [Mechanistic interpretability](../../concepts/mechanistic-interpretability.md) — companion-report results; caveats updated
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Goodfire bullet extended; watch item narrowed

## Key claims extracted
- Up to 92.2% of the weakest neuron activations in Qwen3.6-35B-A3B can be ablated with 1.2–2.2 points of benchmark loss; light fine-tuning restores reasoning
- 69% of a 5,468-pole sample are dominated by one mode; 47% have a single mode
- Description-based detection: 95% vs random text, 89% vs same-expert text, strongest band
- Description-based simulation recovers 73% of a perfect-reader ceiling
- 94% of neurons can be driven past their corpus maximum by agent-written text
