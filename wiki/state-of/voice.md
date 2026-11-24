---
title: State of Voice AI
type: state-of
domains: [voice]
tags: []
as_of: 2026-10-20
sources: [eleven-v3, hume-evi-3, elevenlabs-scribe, voice-becomes-agent-interface, legacy-ai-tools-roadmap-xlsx, gpt-realtime-2-2026-05-08, thinking-machines-interaction-2026-05-12, cartesia-voice-june-2026, gpt-live-launch-2026-07, eleven-realtime-2026-10-20, xai-grok-voice-3-2026-10-14, spacexsi-grok-voice-3-2026-10-14, microsoft-mai-transcribe-2-streaming-2026-10-01, fishaudio-drama-3-2026-10-13, ainews-heygen-voice-whistle-2026-10-10, ainews-eleven-v4-turbo-2026-10-06, ainews-fish-drama-3-2026-10-14, ainews-grok-voice-3-results-2026-10-15, ainews-gpt-live-1-1-2026-10-16]
---

# State of Voice AI

Current state of AI voice products — text-to-speech, speech-to-speech conversation, and speech-to-text transcription. Voice is maturing from a feature into a primary agent interface layer. See [Voice becomes an agent interface](../trends/voice-becomes-agent-interface.md) for the broader trend.

Healthcare voice tools (Dragon Copilot, Zo, Kora) are tracked in [State of Healthcare](healthcare.md) because their primary value is clinical workflow integration rather than the voice model layer itself.

## Subcategories

### Real-time voice / interaction

Streaming AI systems that process live speech, audio, and sometimes screen/video context with sub-second response, native interruption handling, and multi-turn conversation management. This merges the "real-time voice" and "real-time interaction" categories rather than treating them as separate tracks.

- [Grok Voice](../tools/grok-voice.md) — SpaceXAI; Grok Voice 3.0 is #1 on Artificial Analysis's Speech-to-Speech Index (86.9 vs GPT-Live-1 83.2, Gemini 3.8 Live 82.6); 71.6% τ-Voice at ~40% lower latency than GPT-Live-1; $0.08/min *(as of 2026-10-14)*
- [GPT-Live](../tools/gpt-live.md) — OpenAI; full-duplex ChatGPT Voice family that delegates deeper work to frontier models; GPT-Live-1 is now second on the AA index; GPT-Live-1.1 adds multilingual voices and less filler, API later *(as of 2026-10-16)*
- [GPT-Realtime-2](../tools/gpt-realtime-2.md) — OpenAI; "GPT-5-class reasoning" in voice; 128K context (4× prior), 5 reasoning levels (minimal→xhigh), tool use, interruption recovery, graceful failure handling; API: $1.15/hr input, $4.61/hr output *(as of 2026-05-08)*
- **GPT-Realtime-Translate** — OpenAI; live speech-to-speech translation; 70+ input languages → 13 output languages; available in Realtime API *(as of 2026-05-08)*
- **GPT-Realtime-Whisper** — OpenAI; streaming transcription and captions; available in Realtime API *(as of 2026-05-08)*
- **TML-Interaction-Small** — Thinking Machines Lab (Mira Murati); 276B-parameter interaction model; 200ms audio streams, 0.4s end-to-end response, mid-sentence interruption, and simultaneous live video/audio processing *(as of 2026-05-12)*
- **Gemini Magic Pointer** (Googlebook) — Google; Gemini-powered OS-level pointer that activates on clicked screen context; points toward real-time interaction as an operating-system surface rather than only a chat window *(as of 2026-05-13)*
- [Eleven Realtime](../tools/eleven-realtime.md) — ElevenLabs; speech-to-speech v1 Mini (conversation) and v1 Max (reasoning, tool calls), ~0.6 s to first audio; served through an OpenAI-compatible Realtime API as well as ElevenAgents *(as of 2026-10-20)*

### Voice models

AI products centered on expressive text-to-speech, speech-to-speech conversation, or voice cloning as a primary interface or output surface.

- **HeyGen Voice** — HeyGen; tops Artificial Analysis's Controlled Voice TTS arena (Elo 1,201); $30 per 1M characters *(as of 2026-10-10)*
- [Eleven v3](../tools/eleven-v3.md) — ElevenLabs; expressive, high-control TTS, now followed by Eleven v4; the cheaper Eleven v4 Turbo tops AA's Provider Voice TTS arena at half v4's price *(as of 2026-10-06)*
- [MAI-Voice-2.1 / MAI-Voice-2.1-Flash](../models/mai-transcribe-voice.md) — Microsoft AI; 23 languages, one cloned voice keeps a native accent across all of them; Flash: 150ms end-to-end, $15 per 1M characters *(as of 2026-10-01)*
- **Fish Audio Drama 3** — open-weight controllable TTS (35B MoE, 3B active, 83 languages, community license); word-level delivery and mid-sentence tone control; leads AA pronunciation robustness (93.2%) and is #1 open-weight, but 10th/14th overall on quality *(as of 2026-10-14)*
- [Hume EVI 3](../tools/hume-evi-3.md) — Hume; speech-to-speech voice model with strong emotional and empathic conversation framing; fits the "voice as agent interface" direction *(as of 2026-04-22)*
- [Cartesia](../tools/cartesia.md) — Cartesia; Sonic-3.5 (streaming TTS) + Ink-2 (streaming STT); claimed #1 for both on Together AI's benchmark in June; sub-90ms latency; 42 languages; strong structured-utterance handling *(as of 2026-06-16)*

### Speech to text

Products focused primarily on transcription, speech recognition, and converting audio into structured text.

- [MAI-Transcribe-2-Streaming](../models/mai-transcribe-voice.md) — Microsoft AI; #1 on Artificial Analysis for accuracy on both partial and final transcripts; first partials in just over 100ms so agents can act mid-sentence; 60 languages with continuous detection; $0.54/hr introductory *(as of 2026-10-01)*
- [ElevenLabs Scribe](../tools/elevenlabs-scribe.md) — ElevenLabs; enterprise transcription stack for real-time and operational documentation workflows *(as of 2026-04-22)*
- **Whistle** — 16.9MB on-device speech-to-text model said to rival Whisper base *(as of 2026-10-10)*

## Recent changes

- [2026-10-20] ElevenLabs launches Eleven Realtime v1 Mini and v1 Max, speech-to-speech models with an OpenAI-compatible Realtime API.
- [2026-10-16] October refresh: Grok Voice 3.0 ranks #1 on AA's Speech-to-Speech Index (86.9), ahead of GPT-Live-1 (83.2), which gets a 1.1 update; MAI-Transcribe-2-Streaming leads streaming STT accuracy; new TTS lines for MAI-Voice-2.1, HeyGen Voice (controlled-voice arena #1), and open-weight Fish Audio Drama 3; Eleven v4 Turbo tops the provider-voice arena.
- [2026-07-07] GPT-Live launched as the new ChatGPT Voice default: full-duplex interaction plus background delegation to GPT-5.5/frontier models.
- [2026-06-16] Cartesia launches Sonic-3.5 (streaming TTS) and Ink-2 (streaming STT); claims #1 via Together AI benchmark; sub-90ms, 42 languages
- [2026-05-13] Added merged `Real-time voice / interaction` subcategory: GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper, TML-Interaction-Small, and Gemini Magic Pointer; treats real-time voice and interaction as one category
- [2026-04-23] Created `state-of/voice` page; added voice models and speech-to-text subcategories from existing tool pages that lacked state-of coverage

## Sources

- [Introducing Grok Voice 3.0 (x.ai)](../sources/articles/xai-grok-voice-3-2026-10-14.md)
- [SpaceXSI — Grok Voice 3.0 launch thread](../sources/tweets/spacexsi-grok-voice-3-2026-10-14.md)
- [Microsoft AI — MAI-Transcribe-2-Streaming and MAI-Voice-2.1](../sources/articles/microsoft-mai-transcribe-2-streaming-2026-10-01.md)
- [Fish Audio — Drama 3 launch](../sources/tweets/fishaudio-drama-3-2026-10-13.md)
- [AINews — HeyGen Voice and Whistle (Oct 10)](../sources/newsletters/ainews-heygen-voice-whistle-2026-10-10.md)
- [AINews — Eleven v4 Turbo (Oct 6)](../sources/newsletters/ainews-eleven-v4-turbo-2026-10-06.md)
- [AINews — Fish Audio Drama 3 results (Oct 14)](../sources/newsletters/ainews-fish-drama-3-2026-10-14.md)
- [AINews — Grok Voice 3.0 results (Oct 15)](../sources/newsletters/ainews-grok-voice-3-results-2026-10-15.md)
- [AINews — GPT-Live-1.1 (Oct 16)](../sources/newsletters/ainews-gpt-live-1-1-2026-10-16.md)
