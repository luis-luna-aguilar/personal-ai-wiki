---
title: Hume AI — Audio Decisions API launch page
type: source
source_type: article
source_file: raw/articles/2026-11-08-humeai-products-decision-model-api.md
url: https://www.hume.ai/products/decision-model-api
ingested: 2026-11-08
domains: [models, voice]
---

# Hume AI — Audio Decisions API launch page

Hume AI's product page for its Audio Decisions API, an audio-native decision model. A developer sends audio, a question and possible answers (yes/no, pick one, or scale), and the model returns a probability for each answer, judging how something sounds rather than what a transcript says. Hume reports 70.7% agreement with a panel of human raters (56.5% for a single rater) and a 0.82 average across 10 audio benchmarks at 0.23 s median latency, ahead of six general audio LLMs. Access is by request. The page has no publish date; dates use the ingest date.

## Influenced pages
- [Hume Audio Decision Model](../../models/hume-audio-decision-model.md) — new page
- [Decision models](../../concepts/decision-models.md) — first audio-native entrant in the rival list
- [State of Models](../../state-of/models.md) — new Decision models line
- [State of Voice AI](../../state-of/voice.md) — new Audio understanding / decision models section
- [Hume EVI 3](../../tools/hume-evi-3.md) — Related link to Hume's second product

## Key claims extracted
- Input: audio, a question and possible answers; output: a probability per answer. Question types yes/no (`noul`), pick one (`choice`) and scale; several questions per call; any language.
- Agreement with a panel of human raters: 70.7%; a single human rater: 56.5%.
- 0.82 average over 10 audio benchmarks (MMAU, ParaPair, EmphAssess, etc.) at 0.23 s median latency per screen.
- Per-model scores: Hume 82%, Gemini 3.8 Flash 78%, Qwen3.8-Omni-Flash 76%, Inkling-Small 67%. gpt-audio-1.5, Gemini 3.5 Flash Lite and Nemotron 3 Nano Omni also plotted as lower and slower.
- Demo: 25,642 files scanned at 180 ms each. Hume cites 1B client hours processed and 10M+ human judgments.
- Uses: voice-model evaluation and training-data mining, failure and escalation triage, decision layer in voice agents.
- Access by request ("Request API Access"); no pricing shown.
