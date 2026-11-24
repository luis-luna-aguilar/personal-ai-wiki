---
type: proposal
source: raw/articles/2026-10-28-blockxyz-dessa.md
status: pending
created: 2026-10-28
---

# Proposal: Block's Dessa, a full-duplex voice model trained only on human speech

## Summary

### In short

A small Block research lab says a full-duplex conversational voice model can learn language, timing and emotion from raw human speech alone, with no text and no pretrained models, and still run on a laptop. Dessa was trained on one NVIDIA GB200 NVL72 rack, runs faster than real time on a MacBook Pro M4 Max, and is not publicly released: only safety researchers can ask for early access. The proposal creates a Dessa tool page and adds it to State of Voice and the voice-as-agent-interface trend. Reason to hesitate: the page carries no publish date, so the ingest date stands in.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

The source is Dessa's launch page on block.xyz, signed by Ragavan Thurairatnam, who leads a "(very) small" research lab inside Block, the payments company run by Jack Dorsey. The lab was founded by alumni of Dessa, a Toronto deep-learning startup, which gives the model its name.

The argument is that today's voice assistants turn speech into text, reason over the text and turn the answer back into speech, and that this pipeline throws away what text cannot carry: tone, sarcasm, laughter, a sigh, a voice cracking. Dessa is a speech-to-speech model in the strict sense. Audio goes in, audio comes out, and everything it knows was learned from recordings of human conversation, without text transcripts and without starting from an existing language model. It is full-duplex, meaning it listens and talks at the same time, so it can cut in, backchannel ("yeah", "got it"), or laugh mid-sentence. The page says it learned language from "hundreds of times fewer words" than a text LLM, and that training fit on a single GB200 NVL72, NVIDIA's 72-GPU rack-scale system.

The evidence is a set of live, unsteered recordings, including Dessa finishing a forgotten movie title and talking with OpenAI's GPT-Live-1. The lab frames it as research and presents emotional hearing as a safety issue: a voice AI that cannot hear distress keeps going when someone is in pain. There are no benchmarks, pricing or release plan.

### What changes

The wiki tracks real-time voice through OpenAI's GPT-Live and GPT-Realtime-2 and Thinking Machines' interaction model. Nothing in the wiki yet covers a model that skips text entirely.

- New page `tools/dessa.md` describes the model, how it was trained, where it runs and that access is limited, dated 28 October.
- **State of Voice** adds Dessa to the real-time voice and interaction section as a research-stage entry, not a leader, and gains one Recent-changes entry. Page date moves to 28 October.
- **Voice becomes an agent interface** gains one status bullet: speech-only training is a second route to natural voice interaction, alongside GPT-Live's approach of a conversational layer that hands work to a text model. One Recent-changes entry; page date moves to 28 October.
- The index gains the new tool page (tools count 101 to 102), plus one new source page.

### What to weigh

The rendered page shows no publication date. The site's privacy notice is effective 21 October 2026, which hints at when the page went up, but that is a guess, so every date uses the 28 October ingest date. Dessa is filed as a tool page under the existing `voice-models` subcategory, the same as GPT-Live and Hume EVI 3, rather than as a model page, and it is tagged `beta` because only safety researchers can use it.

## Intended changes

- [ ] **Create** `wiki/tools/dessa.md` — new tool page for Block's speech-only full-duplex model
    > See draft below

- [ ] **Update** `wiki/state-of/voice.md` — add a Dessa line to `### Real-time voice / interaction`; add `block-dessa-2026-10-28` to `sources:`; `as_of` 2026-07-07 → 2026-10-28; adds one Recent-changes entry dated 2026-10-28 (list goes from 4 to 5, no spill)
    > See draft below

- [ ] **Update** `wiki/trends/voice-becomes-agent-interface.md` — add one Current-status bullet; add `block-dessa-2026-10-28` to `sources:` and one link to `## Sources`; `as_of` 2026-08-05 → 2026-10-28; adds one Recent-changes entry dated 2026-10-28 (list goes from 5 to 6, no spill)
    > See draft below

- [ ] **Update** `wiki/index.md` — add `tools/dessa` line in the Tools section (alphabetical, before `tools/devin`); tools count 101 → 102
    > See draft below

- [ ] **Create** `wiki/sources/articles/block-dessa-2026-10-28.md` — source summary

## Page drafts

### wiki/tools/dessa.md (new)

```
---
title: Dessa
type: tool
domains: [voice, agents]
subcategory: voice-models
tags: [beta]
as_of: 2026-10-28
sources: [block-dessa-2026-10-28]
---

# Dessa

Dessa is a full-duplex speech-to-speech conversation model from a small research lab at Block. It was trained from scratch on recordings of human conversation only: no text, no transcripts, and no pretrained models. Block describes it as the first AI trained only on human speech that can hold a realistic live conversation.

## Current status (as of 2026-10-28)

- Research release; early access limited to a small group of AI safety researchers. No public API, pricing, or benchmarks.
- Full-duplex: listens and speaks at the same time, cuts in, backchannels ("yeah", "got it"), and laughs mid-sentence; picks its own voice and personality.
- Inference runs faster than real time locally on a MacBook Pro M4 Max or better.
- Trained on a single NVIDIA GB200 NVL72; Block says it learned language from hundreds of times fewer words than text LLMs need.
- Natively hears and produces emotion, sarcasm, laughter, and sighs, which a speech-to-text-to-speech pipeline loses.

## Why it matters

Most voice stacks route speech through text, and [GPT-Live](gpt-live.md) keeps a text model behind the voice layer for deeper work. Dessa tests the opposite route: conversational timing and paralinguistic cues learned directly from sound. Block frames this partly as a safety issue, since a voice AI that cannot hear distress keeps going when a user is in pain, and is inviting outside red-teaming before any wider release.

## Weaknesses / caveats

- Evidence so far is curated live recordings, not benchmarks; factual knowledge comes only from what was said in the training audio.
- No date, pricing, or release plan beyond safety-researcher access.

## Recent changes

- [2026-10-28] Announced by Block with demo recordings (including a conversation with GPT-Live-1) and a call for safety researchers.

## Sources

- [Dessa — the Conversation Model trained only on speech (Block)](../sources/articles/block-dessa-2026-10-28.md)
```

### wiki/state-of/voice.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-28
sources: [eleven-v3, hume-evi-3, elevenlabs-scribe, voice-becomes-agent-interface, legacy-ai-tools-roadmap-xlsx, gpt-realtime-2-2026-05-08, thinking-machines-interaction-2026-05-12, cartesia-voice-june-2026, gpt-live-launch-2026-07, block-dessa-2026-10-28]
```

`### Real-time voice / interaction` — append after the Gemini Magic Pointer line:

```
- [Dessa](../tools/dessa.md) — Block; research-stage full-duplex speech-to-speech model trained only on human speech (no text, no pretrained models); runs locally on a MacBook Pro M4 Max; safety-researcher early access only *(as of 2026-10-28)*
```

`## Recent changes` — insert at top (one new entry; 5 total, no spill):

```
- [2026-10-28] Added Dessa (Block) to real-time voice / interaction: first full-duplex conversation model trained only on human speech; research access only.
```

### wiki/trends/voice-becomes-agent-interface.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-28
sources: [voice-becomes-agent-interface, gpt-live-launch-2026-07, bfl-flux-3-2026-07-24, every-voice-guide-2026-07-31, every-team-of-specialists-2026-08-02, chatgpt-voice-mode-vibe-check-2026-08-05, block-dessa-2026-10-28]
```

`## Current status` — append as the last bullet:

```
- Block's Dessa (October 2026) tests a second route to natural voice: a full-duplex model trained only on human speech, with no text, that keeps emotion, backchannels, and turn timing a speech-to-text pipeline drops, and runs locally on a laptop. GPT-Live keeps a text model behind the voice layer; Dessa removes it. Block presents emotional hearing as a safety concern and has opened early access to safety researchers only.
```

`## Recent changes` — insert at top (one new entry; 6 total, no spill):

```
- [2026-10-28] Block announces Dessa, a full-duplex voice model trained only on human speech that runs locally on a MacBook Pro M4 Max; safety-researcher access only.
```

`## Sources` — append:

```
- [Dessa — the Conversation Model trained only on speech (Block)](../sources/articles/block-dessa-2026-10-28.md)
```

### wiki/index.md (updated)

Tools section, insert before the `tools/devin` line:

```
- [tools/dessa](tools/dessa.md) — Block's full-duplex speech-to-speech model trained only on human speech (no text); runs locally on a MacBook Pro M4 Max; safety-researcher access *(as_of: 2026-10-28)*
```

`## Page count`:

```
- tools: 102
```

### wiki/sources/articles/block-dessa-2026-10-28.md (new)

```
---
title: Dessa — the Conversation Model trained only on speech (Block)
type: source
source_type: article
source_file: raw/articles/2026-10-28-blockxyz-dessa.md
url: https://block.xyz/dessa
ingested: 2026-10-28
domains: [voice, agents]
---

# Dessa — the Conversation Model trained only on speech (Block)

Launch page for Dessa, a full-duplex speech-to-speech model from a small Block research lab founded by former members of the Toronto startup Dessa and led by Ragavan Thurairatnam. The model was trained from scratch on human conversation audio only, with no text and no pretrained models, and is shown through unsteered live recordings, including a conversation with OpenAI's GPT-Live-1. Block is offering early access to a small group of AI safety researchers. The page carries no publication date (the site privacy notice is effective 2026-10-21); the ingest date is used.

## Influenced pages

- [Dessa](../../tools/dessa.md) — new tool page
- [State of Voice AI](../../state-of/voice.md) — added to real-time voice / interaction
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — speech-only training as a second route to natural voice

## Key claims extracted

- Dessa is a true speech-to-speech, full-duplex model: audio in, audio out, listening and speaking at once.
- Trained from scratch only on human speech: no text, no pretrained models; Block calls it the first realistic live-conversation AI trained only on speech.
- Learned language from "hundreds of times fewer words" than LLMs need.
- Trained on a single NVIDIA GB200 NVL72.
- Inference runs faster than real time, locally on a MacBook Pro M4 Max or better.
- Handles backchanneling, interruptions, laughter, emotion, and sarcasm natively; picks its own voice and personality.
- Motivations: curiosity, better human-AI understanding, and safety (voice AI that cannot hear distress).
- Early access offered to a small group of AI safety researchers; no public release, pricing, or benchmarks.
- Lab reports directly to Jack Dorsey; has built generative speech models for over eight years.
```

## Schema / vocabulary additions

None.

## Open questions

None.
