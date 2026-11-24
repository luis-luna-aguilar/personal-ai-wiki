---
type: proposal
source: raw/articles/2026-11-08-humeai-products-decision-model-api.md
status: pending
created: 2026-11-08
---

# Proposal: Hume Audio Decisions API

## Summary

### In short
Decision models now reach audio. Hume's new model judges how speech sounds, not just its transcript, and Hume says it beats general audio LLMs on both accuracy and speed. On Hume's numbers it agrees with a panel of human raters 70.7% of the time, against 56.5% for a single rater, and averages 0.82 across ten audio benchmarks at 0.23 s median latency. The proposal creates one model page and adds pointers to Decision models, State of Models, State of Voice AI and Hume EVI 3. The reason to hesitate is placement: the model sits under Models only, and Voice gets a one-line pointer.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Hume AI, the company behind the empathic voice model EVI 3, has put up a product page for its Audio Decisions API. The page carries no publish date. The model follows the pattern that TypeSafe's Jev set in September. It does not write an answer. A developer sends an audio file, a question and the allowed answers (yes/no, pick one, or a point on a scale), and the model returns a probability for each answer. Several questions can go in one call. The request format even uses Jev-style question types ("noul" and "choice"). What is new is the input. The model listens to the audio directly, so it can answer questions a transcript cannot, such as whether a patient sounds anxious, whether two speakers talk over each other, or whether there is background speech.

Hume backs the launch with two charts. In the first, the model agrees with a panel of human raters 70.7% of the time, while a single human rater agrees with the panel 56.5% of the time. In the second, it averages 0.82 across ten audio benchmarks, including MMAU, ParaPair and EmphAssess, at 0.23 s median latency. It scores higher and answers faster than six general audio models: Gemini 3.8 Flash (78%), Qwen3.8-Omni-Flash (76%), Inkling-Small (67%), gpt-audio-1.5, Gemini 3.5 Flash Lite and Nemotron 3 Nano Omni. Hume pitches it for scoring and comparing voice models, mining training examples, flagging calls for escalation, and as a decision layer inside voice agents. Access is by request. No price is given.

### What changes
The wiki's decision-model coverage is text and image only so far: Jev, Clef, OpenAI's Decisions API, pplx-decider, Liquid d1, ScaleDown and MedDecider.

- New page `models/hume-audio-decision-model.md` holds all the numbers, the question types, the intended uses and the caveat that it has not been tested against other decision models.
- **Decision models** gets one sentence in its rival list naming Hume's model as the first audio-native one, plus a Related link. Page date moves to 8 November.
- **State of Models** gains one leader line in the Decision models section. Its Recent changes list is at its cap, so the oldest entry (Fable 5.1, 1 September) moves to history. Page date moves to 8 November.
- **State of Voice AI** gets one intro sentence pointing audio decision models to State of Models, and a Recent-changes entry. Page date moves to 8 November.
- **Hume EVI 3** gets a Related line linking Hume's two products. Its date stays the same.
- One new source page, and the index's model count goes from 37 to 38.

### What to weigh
The page has no publish date, so every date uses the ingest date, 8 November. That could be a few days after the actual launch. The bigger call is the new page versus a bold line only. The wiki gives a page to decision models that have their own launch source (Jev, ScaleDown, MedDecider) and keeps rivals known only from newsletters as bold lines, so this proposal creates a page. Placement is the other call. The `decision-model` subcategory belongs to the models and agents domains, so the page is tagged `models` and appears under State of Models. Voice gets only a pointer. Listing it on Voice as well would need `voice` added to the subcategory's parent domains. See Open questions.

## Intended changes

- [ ] **Create** `wiki/models/hume-audio-decision-model.md` — new model page; all benchmark detail lives here.

- [ ] **Update** `wiki/concepts/decision-models.md` — one sentence appended to the "Category formed in a month" bullet; one Related line; adds one Recent-changes entry dated 2026-11-08 (list has 1 entry, no spill); appends source id to frontmatter and Sources; `as_of` 2026-10-17 → 2026-11-08.

- [ ] **Update** `wiki/state-of/models.md` — adds one leader line in `### Decision models` after the OpenAI Decisions API line; adds one Recent-changes entry dated 2026-11-08; appends source id to `sources:`; `as_of` 2026-10-20 → 2026-11-08.

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — the list is at cap 10, so the oldest-dated entry (expected: [2026-09-01] Claude Fable 5.1 / Mythos 5.1) moves to history.

- [ ] **Update** `wiki/state-of/voice.md` — one pointer sentence in the intro; adds one Recent-changes entry dated 2026-11-08 (list has 4 entries, no spill); appends source id to `sources:`; `as_of` 2026-07-07 → 2026-11-08.

- [ ] **Update** `wiki/tools/hume-evi-3.md` — adds a `## Related` section with one line to the new model page; no `as_of` change.

- [ ] **Update** `wiki/index.md` — adds the new page under `## Models`; models count 37 → 38.

- [ ] **Create** `wiki/sources/articles/hume-audio-decision-model-api-2026-11-08.md` — source summary.

## Page drafts

### wiki/models/hume-audio-decision-model.md (new)

```md
---
title: Hume Audio Decision Model
type: model
domains: [models]
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
```

### wiki/concepts/decision-models.md (updated)

Frontmatter (changed fields only):

```md
as_of: 2026-11-08
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, jackyk02-clm-contrastive-language-model-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, latent-space-openai-decisions-api-2026-09-30, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17, hume-audio-decision-model-api-2026-11-08]
```

Current status heading and first bullet:

```md
## Current status (as of 2026-11-08)

- **Category formed in a month.** [Jev](../models/jev.md) launched on 2026-09-15; about 100 API clones followed within two weeks. By mid-October the field included Cloudflare's open-weight Clef and Clef-flash (2 October), OpenAI's Decisions API on GPT-6 Luna (public beta, $0.10/M input, no output charge), Perplexity's open pplx-decider (v1.1 27B, then v1.2 in 27B and 4B), Microsoft-Decision-1, Liquid d1 and vLLM Semantic Router's Decision 2.0. Unsloth published a notebook that turns Qwen3.5-4B into one on 8GB of VRAM. In November Hume AI added the first audio-native one, the [Hume Audio Decision Model](../models/hume-audio-decision-model.md), which judges how speech sounds rather than what a transcript says.
```

Related (one line added after the ScaleDown line):

```md
- [Hume Audio Decision Model](../models/hume-audio-decision-model.md) — the first audio-native decision model, for judging tone, pacing and background sound
```

Recent changes (one entry added at the top):

```md
- [2026-11-08] Hume AI's Audio Decision Model added to the rival list as the first audio-native decision model.
```

Sources (one line appended):

```md
- [Hume AI — Audio Decisions API launch page](../sources/articles/hume-audio-decision-model-api-2026-11-08.md)
```

### wiki/state-of/models.md (updated)

Frontmatter: `as_of: 2026-11-08`; append `hume-audio-decision-model-api-2026-11-08` to the end of `sources:`.

Decision models section (one line inserted after the OpenAI Decisions API line):

```md
- [Hume Audio Decision Model](../models/hume-audio-decision-model.md) — Hume AI; first audio-native decision model; judges how speech sounds; 0.82 average on 10 audio benchmarks at 0.23 s; access by request *(as of 2026-11-08)*
```

Recent changes (one entry added at the top; the oldest entry spills, see below):

```md
- [2026-11-08] Hume's Audio Decision Model added to Decision models, the first one that answers questions from audio directly; Hume reports it ahead of Gemini 3.8 Flash and Qwen3.8-Omni-Flash on 10 audio benchmarks.
```

### wiki/history/state-of/models.md (updated)

Appended at the end of the file (the entry is whatever is oldest at apply time; expected):

```md

## Archived from current page on <apply date>

- [2026-09-01] Claude Fable 5.1 / Mythos 5.1 launched, superseding Fable 5: AA Intelligence Index 66 (was 62), 75% cache-read price cut, same-weights/different-safety-routing debate between the two paired model names.
```

### wiki/state-of/voice.md (updated)

Frontmatter: `as_of: 2026-11-08`; append `hume-audio-decision-model-api-2026-11-08` to the end of `sources:`.

Intro (one sentence appended after the healthcare-tools paragraph):

```md
Audio decision models, which answer typed questions about how speech sounds (such as the [Hume Audio Decision Model](../models/hume-audio-decision-model.md)), are tracked under Decision models in [State of Models](models.md).
```

Recent changes (one entry added at the top):

```md
- [2026-11-08] Pointer added to the Hume Audio Decision Model: the first decision model that scores tone, pacing and background sound from audio directly, tracked under State of Models.
```

### wiki/tools/hume-evi-3.md (updated)

New section inserted before `## Sources`:

```md
## Related

- [Hume Audio Decision Model](../models/hume-audio-decision-model.md) — Hume's audio-native decision model, which scores recordings instead of generating speech
```

### wiki/index.md (updated)

Under `## Models` (after the Jev line):

```md
- [models/hume-audio-decision-model](models/hume-audio-decision-model.md) — Hume AI's audio-native decision model: probabilities for yes/no, choice and scale questions about how speech sounds; 0.82 on 10 audio benchmarks at 0.23 s; access by request *(as_of: 2026-11-08)*
```

Page count: `- models: 37` → `- models: 38`.

### wiki/sources/articles/hume-audio-decision-model-api-2026-11-08.md (new)

```md
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
- [State of Voice AI](../../state-of/voice.md) — pointer to audio decision models
- [Hume EVI 3](../../tools/hume-evi-3.md) — Related link to Hume's second product

## Key claims extracted
- Input: audio, a question and possible answers; output: a probability per answer. Question types yes/no (`noul`), pick one (`choice`) and scale; several questions per call; any language.
- Agreement with a panel of human raters: 70.7%; a single human rater: 56.5%.
- 0.82 average over 10 audio benchmarks (MMAU, ParaPair, EmphAssess, etc.) at 0.23 s median latency per screen.
- Per-model scores: Hume 82%, Gemini 3.8 Flash 78%, Qwen3.8-Omni-Flash 76%, Inkling-Small 67%. gpt-audio-1.5, Gemini 3.5 Flash Lite and Nemotron 3 Nano Omni also plotted as lower and slower.
- Demo: 25,642 files scanned at 180 ms each. Hume cites 1B client hours processed and 10M+ human judgments.
- Uses: voice-model evaluation and training-data mining, failure and escalation triage, decision layer in voice agents.
- Access by request ("Request API Access"); no pricing shown.
```

## Schema / vocabulary additions

None.

## Open questions

- Should the model also be listed on **State of Voice AI** as its own section? That needs `voice` added to the `decision-model` subcategory's parent domains in `wiki/_schema/subcategories.md` and `voice` added to the page's `domains`. This proposal keeps it under Models with a one-line pointer from Voice.
