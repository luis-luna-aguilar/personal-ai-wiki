---
title: MAI-Transcribe and MAI-Voice
type: model
domains: [voice, agents]
subcategory: utility-model
tags: [microsoft, closed-source, voice]
as_of: 2026-10-01
sources: [microsoft-mai-transcribe-2-streaming-2026-10-01, ainews-mai-build-june-2026]
---

# MAI-Transcribe and MAI-Voice

Microsoft AI's audio model families: MAI-Transcribe for speech recognition and MAI-Voice for text-to-speech. Microsoft sells them as a pair for low-latency voice agents ("a voice agent is a loop: hear, understand, decide, speak"), where every millisecond saved on hearing and speaking leaves the agent more time to reason or call tools. They are a separate line from Microsoft's reasoning model [MAI-Thinking-1](mai-thinking-1.md).

## Current status (as of 2026-10-01)

- **MAI-Transcribe-2-Streaming** (2026-10-01), Microsoft's first streaming transcription model: #1 on Artificial Analysis for accuracy on both partial and final transcripts, and on its accuracy-vs-latency Pareto frontier. First partial transcripts arrive in just over 100ms, so an agent can start acting before the speaker finishes. 60 languages with continuous language detection; $0.54 per audio hour introductory through year end.
- **MAI-Voice-2.1** (2026-10-01): 23 languages / 26 locales, and one cloned voice keeps a native accent across all of them; $22 per 1M characters.
- **MAI-Voice-2.1-Flash** (2026-10-01): same languages, 45s of audio at 150ms end-to-end latency, 55% faster inference and ~60% cheaper than comparable models per Microsoft; $15 per 1M characters.
- Both voice models clone a voice from a few seconds of reference audio, with built-in consent guardrails.
- Available through Microsoft Foundry, MAI Playground (Chatter demo), Vercel and Azure Voice Live; the voice models also on OpenRouter; LiveKit coming soon.

## Family members

| Model | Released | Benchmark / spec | Use case |
|---|---|---|---|
| MAI-Transcribe-2-Streaming | 2026-10-01 | #1 AA accuracy (partial and final transcripts); partials in ~100ms; 60 langs | Real-time transcription |
| MAI-Voice-2.1 / 2.1-Flash | 2026-10-01 | 23 langs, cross-language cloned voices; Flash 150ms end-to-end | Voice synthesis |
| MAI-Transcribe-1.5 (previous) | 2026-06-03 (Build) | 276x realtime, 2.4% AA-WER, 43 langs, $6/1000 min | Transcription |
| MAI-Voice-2 (previous) | 2026-06-03 (Build) | — | Voice synthesis |

## Recent changes

- [2026-11-23] Page created, split out of the [MAI-Thinking-1](mai-thinking-1.md) family table (MAI-Transcribe and MAI-Voice rows).
- [2026-10-01] MAI-Transcribe-2-Streaming (#1 AA streaming accuracy, $0.54/hr intro) and MAI-Voice-2.1 / 2.1-Flash ($22 / $15 per 1M characters) replace MAI-Transcribe-1.5 and MAI-Voice-2 as current; see [State of Voice](../state-of/voice.md).
- [2026-06-03] MAI-Transcribe-1.5 and MAI-Voice-2 listed in the MAI family at Microsoft Build 2026.

## Sources

- [Microsoft AI — MAI-Transcribe-2-Streaming and MAI-Voice-2.1](../sources/articles/microsoft-mai-transcribe-2-streaming-2026-10-01.md)
- [AINews — Microsoft Build, MAI-Thinking-1 (June 3)](../sources/newsletters/ainews-mai-build-june-2026.md)
