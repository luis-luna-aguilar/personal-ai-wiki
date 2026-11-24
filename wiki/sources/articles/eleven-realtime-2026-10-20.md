---
title: Eleven Realtime launch page (ElevenLabs)
type: source
source_type: article
source_file: raw/articles/2026-10-20-elevenlabsio-realtime.md
url: https://elevenlabs.io/realtime
ingested: 2026-10-20
domains: [voice, agents]
---

# Eleven Realtime launch page (ElevenLabs)

ElevenLabs' product page for Eleven Realtime, a speech-to-speech model family for voice agents with speech recognition, turn-taking, LLM and voice tuned as one system. Two models: v1 Mini for conversation and v1 Max for reasoning and tool calls. They are available in ElevenAgents and through a Realtime API compatible with OpenAI's. The page carries no publication date. The FAQ was expanded in a browser on 20 October.

## Influenced pages
- [Eleven Realtime](../../tools/eleven-realtime.md) — new page
- [State of Voice](../../state-of/voice.md) — new real-time voice line
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — OpenAI Realtime protocol as a cross-vendor plug

## Key claims extracted
- v1 Mini: Full-Duplex-Bench 95.8%, Speech Agent Arena Elo 988, 620 ms time to first audio
- v1 Max: Big Bench Audio 98.8%, task success 87.1%, 570 ms time to first audio
- Benchmarks run by Artificial Analysis; time to first audio averaged on Big Bench Audio
- Realtime API is OpenAI-compatible: same client/server events; OpenAI's SDK works after an endpoint and model-name change; migration skill `openai-realtime-migration`
- WebSocket only at launch, no WebRTC; ElevenAgents features (channels, knowledge base, guardrails, testing) not available via the API
- Pricing: per minute plus LLM tokens; no rates on the page
- 90+ languages, 17,500+ voices
