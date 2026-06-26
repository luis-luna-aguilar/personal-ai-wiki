---
type: proposal
sources:
  - raw/newsletters/2026-06-16-ainews-satya-on-loopcraft-building-frontier-eco.md
status: pending
created: 2026-06-17
---

# Proposal: Cartesia Sonic-3.5 + Ink-2 voice models

## Summary

Cartesia shipped both sides of real-time voice: Sonic-3.5 (streaming TTS) and Ink-2 (streaming STT). Claims #1 for both via Together AI benchmark, sub-90ms latency, 42 languages, and notably strong structured-utterance handling (codes, IDs). Updates `state-of/voice.md` with a new entrant for the voice models subcategory.

## Intended changes

- [x] **Create** `wiki/tools/cartesia.md` — new tool page for Cartesia (Sonic-3.5 + Ink-2)
- [x] **Update** `wiki/state-of/voice.md` — add Cartesia to voice models subcategory

## Page drafts

### wiki/tools/cartesia.md (new)

````md
---
title: Cartesia
type: tool
domains: [voice]
subcategory: voice-model
tags: [voice]
as_of: 2026-06-16
sources: [cartesia-voice-june-2026]
---

# Cartesia

AI voice platform focused on low-latency streaming voice models. Offers both text-to-speech (Sonic-3.5) and speech-to-text (Ink-2) as streaming services.

## Current status (as of 2026-06-16)

- **Sonic-3.5** — streaming TTS; claims #1 by Together AI benchmark; sub-90ms latency; 42 languages; strong on structured utterances (IDs, codes, alphanumeric strings)
- **Ink-2** — streaming STT; claims #1 by Together AI benchmark; sub-90ms latency; 42 languages; same structured-utterance strength as Sonic-3.5
- Both available now via API

## Strengths

- Sub-90ms latency positions it for real-time conversational agents
- Structured-utterance handling (IDs, codes) is a practical differentiator for voice agents that read alphanumeric strings aloud or transcribe them
- 42 languages covers broad international deployment

## Weaknesses / caveats

- Claims are from a Together AI benchmark; independent third-party validation limited at this stage
- Newsletter coverage only; primary Cartesia documentation not fetched

## Recent changes

- [2026-06-16] Sonic-3.5 and Ink-2 launched; claim #1 TTS and STT positions via Together AI

## Sources

- [Cartesia voice models — June 2026](../sources/newsletters/cartesia-voice-june-2026.md)
````

### wiki/state-of/voice.md (updated section)

> **Frontmatter: update `as_of` to 2026-06-16; add `cartesia-voice-june-2026` to sources.**

> **Voice models — add Cartesia entry:**

> **After:**
```
- [Hume EVI 3](../tools/hume-evi-3.md) — Hume; speech-to-speech voice model ...
```
> **Add:**
```
- [Cartesia](../tools/cartesia.md) — Cartesia; Sonic-3.5 (streaming TTS) + Ink-2 (streaming STT); claims #1 for both via Together AI; sub-90ms latency; 42 languages; strong structured-utterance handling *(as of 2026-06-16)*
```

> **Add to ## Recent changes (prepend):**
```
- [2026-06-16] Cartesia launches Sonic-3.5 (streaming TTS) and Ink-2 (streaming STT); claims #1 via Together AI benchmark; sub-90ms, 42 languages
```

### wiki/sources/newsletters/cartesia-voice-june-2026.md (new)

````md
---
title: Cartesia Sonic-3.5 and Ink-2 launch (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-16-ainews-satya-on-loopcraft-building-frontier-eco.md
published: 2026-06-16
ingested: 2026-06-17
domains: [voice]
---

# Cartesia Sonic-3.5 and Ink-2 launch (June 2026)

## Influenced pages

- [Cartesia](../../tools/cartesia.md) — new tool page
- [State of Voice AI](../../state-of/voice.md) — added to voice models subcategory

## Key claims extracted

- Sonic-3.5: streaming TTS, #1 Together AI benchmark, sub-90ms, 42 languages
- Ink-2: streaming STT, #1 Together AI benchmark, sub-90ms, 42 languages
- Both notable for structured utterance handling (IDs, codes)
- Source: AINews secondary coverage; Cartesia primary docs not fetched
````
