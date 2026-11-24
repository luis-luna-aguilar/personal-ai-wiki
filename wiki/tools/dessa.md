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
