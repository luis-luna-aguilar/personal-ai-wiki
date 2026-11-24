---
title: Mechanistic interpretability
type: concept
domains: [models]
tags: []
as_of: 2026-11-15
sources: [goodfire-already-clean-2026-10, goodfire-neurons-interpretable-basis-2026-11]
---

# Mechanistic interpretability

Mechanistic interpretability tries to explain how a neural network works from the inside: what individual neurons respond to, how they connect into circuits, and how information flows from input to output. It is the "read the source code" approach to AI safety, as opposed to judging a model only by what it says.

## Current status (as of 2026-11-15)
- The field's working assumption since Zoom In (2020) has been **superposition**: networks short on room pack unrelated concepts into the same neuron, so neurons are unreadable and must first be untangled with a second trained model, usually a sparse autoencoder (SAE).
- Nick Cammarata (Goodfire, 2026), a co-author of the original evidence, argues that evidence was misread and that networks are "already clean". The canonical cat-and-car neuron is a V-shape detector. With ordinary architecture fixes, 99–100% of InceptionV1's last-layer neurons become readable, up from almost none.
- He reports that in preliminary audits of Qwen3-32B, ~90% of neurons have one main job, ~7% two related jobs, and ~2–4% are unexplained. Results look similar in trillion-parameter MoE models (Kimi K3). He flags that these numbers depend on thresholds.
- **The companion report (November 2026)** tests the claim on the neurons of one open model, Qwen3.6-35B-A3B. Switching off the weakest 92.2% of activations costs 1.2–2.2 points on likelihood benchmarks, and a fine-tune of about 100M tokens restores reasoning. In a 5,468-pole sample, 69% are dominated by one mode (47% have a single one). Descriptions written by a "Neuron Scientist" agent let a judge model pick the text a neuron fires on 95% of the time in its strongest range (89% against same-domain text), and simulating a neuron from its description recovers 73% of a perfect reader's result.
- In his vision-model tests, 88% of SAE activity was near-copies of single neurons, and removing the rest left accuracy unchanged. He argues SAEs and probes belong at the end of an analysis, not the start.
- [Model internal workspace](model-internal-workspace.md) (Anthropic's J-space) is a separate line of work on a reportable internal representation.

## The disagreement in plain terms
**Superposition** says a neuron firing on "floppy dog ears + Latin poetry" is a storage trick: the pairing means nothing, so you must unfold the network before you can study it. **Recursive generalization** says neurons group *related* things and then sprout related offshoots. One neuron that detected "iy" grew into "diy" and then "do it yourself". Under this view, the odd extra activations are clues to follow. The two predict opposite things, and Cammarata says watching neurons grow during training settles it in favour of generalization.

## Why it matters
If networks are mostly legible as they are, interpretability becomes ordinary science that agents can run at scale: label neurons, find recurring patterns, test explanations, repeat. It stops being a search for a cleverer decomposition. Cammarata's safety claim is that deception has no reason to hide from the model's own circuitry, so the risk is not a hidden activation but failing to read what is in plain sight.

## Caveats
- The evidence comes from Goodfire alone, and the language-model results cover one model family (Qwen3.6-35B-A3B).
- Only strong activations are explained; the weak ones that make up most firings are left open, and some neurons are genuinely mixed.
- Contradicts the field's dominant SAE/dictionary-learning program; independent replication is pending.
- The step from "legible" to "solved" is labelled by the author as highly speculative.

## Recent changes
- [2026-11-15] Goodfire's companion report, "Neurons as an Interpretable Basis": on Qwen3.6-35B-A3B, 92.2% of weak activations can be dropped, most neurons have one dominant mode, and agent-written descriptions predict firing 95% of the time in the strongest range.
- [2026-10-19] Page created from Cammarata's "Neural Networks Are Already Clean" (Goodfire): challenges superposition as the explanation for messy neurons.

## Sources
- [Neural Networks Are Already Clean — Nick Cammarata (Goodfire)](../sources/articles/goodfire-already-clean-2026-10.md)
- [Neurons as an Interpretable Basis — Goodfire](../sources/articles/goodfire-neurons-interpretable-basis-2026-11.md)
