---
title: 'Neural Networks Are Already Clean — Nick Cammarata (Goodfire)'
type: source
source_type: article
source_file: raw/articles/2026-10-19-already-cleangoodfirecom.md
url: https://already-clean.goodfire.com/
ingested: 2026-10-19
domains: [models]
---

# Neural Networks Are Already Clean — Nick Cammarata (Goodfire)

Long interactive essay (~40K words with appendices), Goodfire, 2026; the page gives the year only. The author co-wrote Zoom In, Multimodal Neurons and OpenAI's 2023 automated-interpretability project, so he is revisiting his own earlier evidence.

## The problem
To check what an AI model is doing, interpretability researchers try to read its parts. Neurons that seemed to respond to unrelated things ("polysemantic" neurons) made that look hopeless. The accepted explanation, **superposition**, said networks short on room pack unrelated concepts together because they rarely collide. If so, you can't read neurons directly. You first train a second model (a sparse autoencoder, or "dictionary") to unpack them, and study that instead.

## The claim
Most of that apparent mixing is **recursive generalization**: a neuron groups related things and then sprouts related offshoots, like a branch growing twigs. Example: a neuron detecting "iy" grew to "diy", then "do it yourself". Under this view the extra activations are leads, not noise, and the network can be studied as it is.

## Four-step argument (author's own)
1. Networks use one learning principle (generalization), not two, so ordinary science on them can start now.
2. With modern models and tools, that science goes much better than expected.
3. Understanding compounds like a crossword: each explained neuron constrains its neighbours, so the map fills in faster as it goes.
4. Highly speculative: this might be most of what interpretability needs, possibly soon.

## Evidence highlights
- **Cat-and-car neuron (InceptionV1 4e:55)** is a V-shape detector: its inputs and readers include pointed snouts, flames and fireboat jets, and its negative side responds to round O shapes.
- The canonical superposition circuit from Zoom In (a car feature spreading into dog neurons) has no downstream reader. He reads it as ordinary generalization, not hidden storage.
- InceptionV1's messy last layer was an architecture problem. With modern architecture fixes (no change to size or data), 99–100% of last-layer neurons are readable, at every scale across a 300× size range. Smaller models get coarser neurons, not mixed ones.
- Language models: preliminary Qwen3-32B audits find ~90% of neuron poles with one main job, ~7% with two related jobs, and ~2–4% not understood. Thresholds matter, and dense and MoE models look similar. A GPT-2 XL re-audit puts ~70% at roughly one thing, against <2% in 2023.
- SAEs on ConvNeXt: 88% of last-layer SAE activity is near-copies of single neurons. Removing the non-matching directions leaves accuracy unchanged, and what the SAE adds is loose groupings of existing neurons.
- First published attribution graph of a multi-trillion-parameter model (Kimi K3) using only neurons.
- Why the field missed it: 2023 explainer models couldn't run conjecture-and-test loops, metrics rewarded simulating activations over being right, nobody knew which language-neuron patterns to expect, and most studies used small models.

## What a solution might look like
A lab of automated scientist agents watching the network through training and inference, following a "mechanistic constitution": label neurons, find motifs, test explanations at many scales. Alignment might then proceed through many simple, targeted fixes, such as removing a toxic RL environment. Deception, he argues, can't hide from the model's own circuitry; the risk is failing to read what is in plain sight.

## Limits
- Single author; the companion paper with language-model detail is forthcoming
- Headline percentages depend on author-chosen thresholds and small audited samples
- Contradicts the field's dominant decomposition program; independent replication pending
- Step 4 is explicitly speculative

## Influenced pages
- [Mechanistic interpretability](../../concepts/mechanistic-interpretability.md) — new concept page
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — current-signal and watch bullets
- [Model internal workspace](../../concepts/model-internal-workspace.md) — Related link

## Key claims extracted
- Superposition was the wrong explanation for InceptionV1; the polysemantic examples in the vision literature were misread
- Recursive generalization explains most remaining apparent polysemanticity
- Qwen3-32B: ~90% one job / ~7% two related / ~2–4% unexplained (preliminary)
- SAE activity on ConvNeXt is 88% near-copies of single neurons
- Bigger models learn narrower, easier-to-recognize neurons
- Agents at scale can map vision models; language models "so far" similar up to trillions of parameters
