---
type: proposal
sources:
  - raw/newsletters/2026-04-20-training-transformers-to-solve-95-failure-rate.md
  - raw/tweets/2026-04-21-openai-2044861690911850863.md
status: pending
created: 2026-04-21
---

# Proposal: AI in biology — Noetik and GPT-Rosalind

## Summary

The science section is still thin and generic. This batch offers a stronger, more concrete direction: specialized AI systems for biology and drug discovery. Noetik is framed as using transformer models plus rich tumor data to improve treatment-response prediction and rescue clinical-trial outcomes; OpenAI positions GPT-Rosalind as a frontier reasoning model for biology and translational medicine.

## Intended changes

- [x] **Update** `wiki/trends/ai-in-science.md` — move from generic "AI helps science" examples toward concrete biology/drug-discovery signals
  > See snippet below.

- [x] **Update** `wiki/state-of/science.md` — add a `Recent changes` note pointing to biology / drug-discovery as the strongest current signal
  > Add:
  > `- [2026-04-21] Biology / drug discovery emerges as the strongest current productization signal: Noetik's tumor-response models and OpenAI's GPT-Rosalind`

- [x] **Create** `wiki/sources/newsletters/noetik-cancer-trials.md` — source summary
- [x] **Create** `wiki/sources/tweets/gpt-rosalind-launch.md` — source summary

## Page drafts

### wiki/trends/ai-in-science.md (updated snippet)

```md
---
title: AI in Science
type: trend
domains: [science]
tags: []
as_of: 2026-04-21
sources: [noetik-cancer-trials, gpt-rosalind-launch]
---

# AI in Science

AI is increasingly moving from generic scientific assistance toward domain-specific scientific reasoning systems. The strongest current signal in this wiki is biology and drug discovery: models are being positioned not just as literature copilots, but as systems that infer treatment response, model tumor environments, or support translational medicine workflows.

## Current status (as of 2026-04-21)

- Noetik is presented as using large multimodal tumor datasets and transformer models to predict treatment response and improve cancer-trial selection
- The company reportedly signed a $50M GSK deal tied to this stack
- OpenAI launched GPT-Rosalind as a frontier reasoning model for biology, drug discovery, and translational medicine
- The pattern is shifting from "AI helps researchers" to "specialized models target a scientific bottleneck directly"

## Recent changes

- [2026-04-21] Added biology / drug-discovery productization signals: Noetik and GPT-Rosalind
- [2026-04-10] Page seeded from Superhuman AI newsletter overview of AI-driven scientific breakthroughs
```

### wiki/sources/newsletters/noetik-cancer-trials.md (new)

```md
---
title: Latent Space — Noetik and cancer-trial failure
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-20-training-transformers-to-solve-95-failure-rate.md
ingested: 2026-04-21
domains: [science]
---

# Latent Space — Noetik and cancer-trial failure

Latent Space profile of Noetik's biology stack. The core claim is that many cancer-trial failures are really patient-selection failures, and that transformer models trained on large multimodal tumor datasets can identify which treatments will work for which patients.

## Key claims extracted

- Noetik trained on large tumor spatial transcriptomics and imaging datasets
- TARIO-2 is positioned as a transformer that predicts rich tumor maps from standard assays
- The commercial signal is strong: reported $50M GSK deal plus longer-term licensing
- The ambition is both trial rescue and better-targeted drug discovery
```

### wiki/sources/tweets/gpt-rosalind-launch.md (new)

```md
---
title: GPT-Rosalind launch
type: source
source_type: tweet
source_file: raw/tweets/2026-04-21-openai-2044861690911850863.md
url: https://x.com/openai/status/2044861690911850863
published: 2026-04-21
ingested: 2026-04-21
domains: [science]
---

# GPT-Rosalind launch

OpenAI announces GPT-Rosalind, described as a frontier reasoning model built to support research across biology, drug discovery, and translational medicine.
```

## Comments

- Please expand a bit into whats translational medicine.