---
title: Hume Audio Decision Model
type: model
domains: [models, voice]
subcategory: decision-model
tags: [closed-source, voice]
as_of: 2026-11-08
sources: [hume-audio-decision-model-api-2026-11-08]
---

# Hume Audio Decision Model

Hume AI's audio-native [decision model](../concepts/decision-models.md), sold as the Audio Decisions API. A developer sends audio, a question and the possible answers, and the model returns a probability for each answer. It listens to the audio itself rather than a transcript, so it can judge tone, pacing, interruptions and background sound. It is the first audio decision model in the wiki. Hume's other product is the voice model [Hume EVI 3](../tools/hume-evi-3.md).

## Current status (as of 2026-11-08)

- Question types: yes/no (`noul`), pick one (`choice`) and scale. Several questions can run against the same audio in one call. Questions can be in any language.
- Agreement with a panel of human raters: 70.7%, against 56.5% for a single human rater.
- Averages 0.82 across 10 audio benchmarks (MMAU, ParaPair, EmphAssess and others) at 0.23 s median latency, ahead of Gemini 3.8 Flash (78%), Qwen3.8-Omni-Flash (76%), Inkling-Small (67%), gpt-audio-1.5, Gemini 3.5 Flash Lite and Nemotron 3 Nano Omni.
- Access is by request through Hume's API. No price is published.

## Where it fits

Hume pitches four uses: scoring voice models on naturalness, clarity, empathy or timing; re-running the same questions when a model or the criteria change; finding training examples and failures in recording collections (its demo scans 25,642 calls at 180 ms each); and acting as a decision layer inside a voice agent, next to speech recognition and generation.

## Weaknesses / caveats

- Compared only with general audio LLMs, not with other decision models, and it does not appear on any decision-model index.
- Launch page has no publish date or pricing.

## Recent changes

- [2026-11-08] Page created from Hume's Audio Decisions API launch page.

## Sources

- [Hume AI — Audio Decisions API launch page](../sources/articles/hume-audio-decision-model-api-2026-11-08.md)
