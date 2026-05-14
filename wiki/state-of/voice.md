---
title: State of Voice AI
type: state-of
domains: [voice]
tags: []
as_of: 2026-05-13
sources: [eleven-v3, hume-evi-3, elevenlabs-scribe, voice-becomes-agent-interface, legacy-ai-tools-roadmap-xlsx, gpt-realtime-2-2026-05-08, thinking-machines-interaction-2026-05-12]
---

# State of Voice AI

Current state of AI voice products — text-to-speech, speech-to-speech conversation, and speech-to-text transcription. Voice is maturing from a feature into a primary agent interface layer. See [Voice becomes an agent interface](../trends/voice-becomes-agent-interface.md) for the broader trend.

Healthcare voice tools (Dragon Copilot, Zo, Kora) are tracked in [State of Healthcare](healthcare.md) because their primary value is clinical workflow integration rather than the voice model layer itself.

## Subcategories

### Real-time voice / interaction

Streaming AI systems that process live speech, audio, and sometimes screen/video context with sub-second response, native interruption handling, and multi-turn conversation management. This merges the "real-time voice" and "real-time interaction" categories rather than treating them as separate tracks.

- [GPT-Realtime-2](../tools/gpt-realtime-2.md) — OpenAI; "GPT-5-class reasoning" in voice; 128K context (4× prior), 5 reasoning levels (minimal→xhigh), tool use, interruption recovery, graceful failure handling; API: $1.15/hr input, $4.61/hr output *(as of 2026-05-08)*
- **GPT-Realtime-Translate** — OpenAI; live speech-to-speech translation; 70+ input languages → 13 output languages; available in Realtime API *(as of 2026-05-08)*
- **GPT-Realtime-Whisper** — OpenAI; streaming transcription and captions; available in Realtime API *(as of 2026-05-08)*
- **TML-Interaction-Small** — Thinking Machines Lab (Mira Murati); 276B-parameter interaction model; 200ms audio streams, 0.4s end-to-end response, mid-sentence interruption, and simultaneous live video/audio processing *(as of 2026-05-12)*
- **Gemini Magic Pointer** (Googlebook) — Google; Gemini-powered OS-level pointer that activates on clicked screen context; points toward real-time interaction as an operating-system surface rather than only a chat window *(as of 2026-05-13)*

### Voice models

AI products centered on expressive text-to-speech, speech-to-speech conversation, or voice cloning as a primary interface or output surface.

- [Eleven v3](../tools/eleven-v3.md) — ElevenLabs; high-control expressive text-to-speech; stronger for polished generated voice output than conversational turn-taking *(as of 2026-04-22)*
- [Hume EVI 3](../tools/hume-evi-3.md) — Hume; speech-to-speech voice model with strong emotional and empathic conversation framing; fits the "voice as agent interface" direction *(as of 2026-04-22)*

### Speech to text

Products focused primarily on transcription, speech recognition, and converting audio into structured text.

- [ElevenLabs Scribe](../tools/elevenlabs-scribe.md) — ElevenLabs; enterprise transcription stack for real-time and operational documentation workflows *(as of 2026-04-22)*

## Recent changes

- [2026-05-13] Added merged `Real-time voice / interaction` subcategory: GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper, TML-Interaction-Small, and Gemini Magic Pointer; treats real-time voice and interaction as one category
- [2026-04-23] Created `state-of/voice` page; added voice models and speech-to-text subcategories from existing tool pages that lacked state-of coverage
