---
title: Mistral Large 4
type: model
domains: [models]
subcategory: open-weight-model
tags: [mistral, multimodal]
as_of: 2026-10-07
sources: [ainews-reflection-beam-training-2026-10-07]
---

# Mistral Large 4

Mistral's flagship, nicknamed "Le Chonk": a natively multimodal mixture-of-experts model with 1T total and 49B active parameters, pre- and post-trained on about 3,800 Grace Blackwells in Europe. Previewed on API in early October 2026, with open weights promised for the end of October. It is the strongest model so far from outside the US and China, but expensive to run for its capability.

## Current status (as of 2026-10-07)

- API preview at $1.36/$4.18 per million input/output tokens ($0.14 cached, 50% off for the first two weeks); 512K context per Vals and Artificial Analysis, 1M per OpenRouter
- Artificial Analysis Intelligence Index 38, level with [GPT-6 Luna](gpt-6-luna.md) (max) and the top score outside the US and China, but behind [GLM-5.3](glm-5-3.md) and even GLM-5.3-Flash; $1.13 per task, over 4x similar-intelligence open models
- Vals: #1 open-weight on HLAB, #9 among open models on the Vals Index; heavy context use pushes cost to $13.78 per test
- Mistral's claims: beats GLM-5.3 on STEM, CAD and finance human evals and on DeepSWE, beats [Kimi K3](kimi-k3.md) on Terminal-Bench 4; #2 behind Opus 5 in a blind Surge coding review
- The RL run is "still in flight"; a larger model is in training

## Weaknesses / caveats

- Not open-weight until the weights ship, as Hugging Face's CEO pointed out
- Cline attributes its cyber-benchmark lead largely to fewer refusals than Opus 5.5 and Astra
- Mistral says many reported failures come from not setting `reasoning_effort="high"`

See [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md) for the October open-weight wave it arrived in.

## Recent changes

- [2026-10-07] Previewed on API: 1T/49B multimodal MoE, AA Intelligence Index 38, open weights promised for end of October.

## Sources

- [AINews — Beam training details and Mistral Large 4](../sources/newsletters/ainews-reflection-beam-training-2026-10-07.md)
