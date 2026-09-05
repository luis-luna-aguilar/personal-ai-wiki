---
title: Cartesia
type: tool
domains: [voice]
subcategory: voice-model
tags: [voice]
as_of: 2026-06-16
sources: [cartesia-voice-june-2026, ainews-all-model-labs-are-now-agent-labs]
---

# Cartesia

AI voice platform focused on low-latency streaming voice models. Offers both text-to-speech (Sonic-3.5) and speech-to-text (Ink-2) as streaming services.

## Current status (as of 2026-06-16)

- **Sonic-3.5** — streaming TTS; claims #1 by Together AI benchmark; per AINews, also ranked #1 on Artificial Analysis's Speech Arena (Elo 1218; AA cites 42 languages and strong naturalness/transcript-following) — a second independent benchmark corroborating the leadership claim; Cartesia itself claims ~82ms end-to-end first-audio latency in production; sub-90ms latency; strong on structured utterances (IDs, codes, alphanumeric strings)
- **Ink-2** — streaming STT; claims #1 by Together AI benchmark; sub-90ms latency; 42 languages; same structured-utterance strength as Sonic-3.5
- Both available now via API

## Strengths

- Sub-90ms latency positions it for real-time conversational agents
- Structured-utterance handling (IDs, codes) is a practical differentiator for voice agents that read alphanumeric strings aloud or transcribe them
- 42 languages covers broad international deployment
- Sonic-3.5's TTS leadership claim is cross-validated by a second independent benchmark (Artificial Analysis Speech Arena, in addition to Together AI), as reported by AINews

## Weaknesses / caveats

- Ink-2's #1 STT claim still rests only on the Together AI benchmark; independent third-party validation is limited on that side
- Newsletter coverage only; primary Cartesia documentation not fetched

## Recent changes

- [2026-06-16] Sonic-3.5 and Ink-2 launched; claim #1 TTS and STT positions via Together AI
- [2026-05-23] AINews reports Artificial Analysis ranked Sonic-3.5 #1 on its Speech Arena (Elo 1218, 42 languages); Cartesia separately claims ~82ms end-to-end first-audio latency in production. Second independent evaluator corroborating the Together AI #1 TTS claim.

## Sources

- [Cartesia voice models — June 2026](../sources/newsletters/cartesia-voice-june-2026.md)
- [AINews — All Model Labs are now Agent Labs (Speech Arena #1 ranking)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
