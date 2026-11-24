---
title: Eleven v4
type: tool
domains: [agents, voice]
subcategory: voice-models
tags: [elevenlabs, closed-source]
as_of: 2026-10-26
sources: [elevenlabs-eleven-v4, ainews-eleven-v4-turbo-2026-10-06, elevencreative-chimera-2026-10-21]
---

# Eleven v4

ElevenLabs' current text-to-speech model family and the successor to Eleven v3. **Eleven v4** is for expressive, directed generated speech; **Eleven v4 Turbo** carries the same expressive range at real-time latency for voice agents. Both run on a new architecture that reads a script "the way a voice actor would", tracking who is speaking and what just happened.

## Current status (as of 2026-10-26)

- **Eleven v4:** 90+ languages, multiple speakers, and built-in sound effects. Follows inline direction tags ([laughs], [whispers], [door slams]) more reliably than v3; "context stitching" keeps pacing steady across scripts of any length (an audiobook as "a single take"); regenerating a line keeps the same speaker identity.
- **Professional Voice Clones** are back: unsupported in v3, they now perform with v4's full emotional range in every language, and work identically on v4 and v4 Turbo.
- **Eleven v4 Turbo:** median inference latency ~100 ms, median time to first speech ~150 ms, bidirectional streaming (push text as the LLM generates it, audio returns before the sentence ends); available through the API and ElevenAgents. ElevenLabs' own chart puts time to first speech at 150 ms vs. 262 ms for Cartesia Sonic 3.6 and 814 ms for OpenAI GPT-4o mini TTS. Tops Artificial Analysis's Provider Voice TTS arena at half v4's price (2026-10-06).
- **Voice tooling:** 17,500+ library voices, instant cloning from ten seconds of audio, Voice Design from a one-sentence description, and a pronunciation dictionary with IPA support.
- **Access and price:** `model_id` `eleven_v4` through the REST API, streaming endpoints, and TypeScript/Python SDKs; free plan with 10,000 credits a month, paid plans from $6 a month, enterprise custom.
- **Chimera (ElevenCreative, 2026-10-21):** a template that pairs Eleven v4 with ByteDance's [Seedance 2.5](seedance-2-5.md) to make talking-character video. Upload or create a character (human, cartoon or pet), write the line, pick or design a voice, and direct it with audio tags ([whispers], [laughs], [yells]); v4 performs the voice and Seedance animates the face. Own audio can replace generated speech. Found under More Tools > Templates.

## Strengths

- One family covers both polished generated audio and live agent conversation, with one voice identity across both
- Direction lives in the script itself, which suits narration, dialogue, and character work

## Weaknesses / caveats

- The latency comparison is ElevenLabs' own chart, and the product page gives no release date
- Turbo's expressive range at conversational speed is described, not measured, on the source page

## Recent changes

- [2026-10-26] Page created for Eleven v4 and v4 Turbo; supersedes [Eleven v3](../history/tools/eleven-v3.md), which moved to history.
- [2026-10-21] ElevenCreative launches Chimera, pairing Eleven v4 voices with Seedance 2.5 face animation for talking characters.

## Sources

- [Eleven v4 and Eleven v4 Turbo (ElevenLabs product page)](../sources/articles/elevenlabs-eleven-v4.md)
- [AINews — Eleven v4 Turbo (Oct 6)](../sources/newsletters/ainews-eleven-v4-turbo-2026-10-06.md)
- [ElevenCreative — Chimera launch post](../sources/tweets/elevencreative-chimera-2026-10-21.md)
