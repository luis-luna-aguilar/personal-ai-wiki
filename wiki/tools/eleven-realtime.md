---
title: Eleven Realtime
type: tool
domains: [voice, agents]
subcategory: voice-models
tags: [elevenlabs, closed-source, agentic]
as_of: 2026-10-20
sources: [eleven-realtime-2026-10-20]
---

# Eleven Realtime

ElevenLabs' speech-to-speech model family for voice agents. Speech recognition, turn-taking, the LLM and the voice are tuned together as one system, so a builder picks one model instead of assembling a pipeline. Two models: **v1 Mini** for natural conversation and **v1 Max** for reasoning and tool use.

## Current status (as of 2026-10-20)

- **v1 Mini**: the lower-cost option for assistants, tutors and interactive characters. Full-Duplex-Bench 95.8%, Speech Agent Arena Elo 988, 620 ms time to first audio.
- **v1 Max**: adds reasoning and tool calls for customer support, lead qualification and scheduling. Big Bench Audio 98.8%, task success 87.1%, 570 ms time to first audio.
- Benchmarks were run by Artificial Analysis. Time to first audio is the average on Big Bench Audio.
- Two surfaces: a model dropdown in ElevenAgents, where existing prompts, tools, knowledge base and channels carry over, and a Realtime API that is wire-compatible with OpenAI's Realtime API. The same events arrive, OpenAI's `@openai/agents-realtime` SDK connects by swapping the WebSocket URL and model name (`eleven_realtime_v1_mini`), and an agent skill (`openai-realtime-migration`) automates the switch.
- Pricing: in ElevenAgents, per-minute agent pricing plus LLM tokens; through the API, per minute of connected audio plus tokens. No rates are published on the launch page.
- 90+ languages; voices come from ElevenLabs' 17,500+ voice library.

## Weaknesses / caveats

- API is WebSocket-only at launch (no WebRTC).
- The Realtime API does not include ElevenAgents features (phone/WhatsApp channels, knowledge base, guardrails, testing, monitoring). Those need ElevenAgents.

## Related

- [GPT-Realtime-2](gpt-realtime-2.md): the OpenAI model whose API protocol Eleven Realtime mirrors
- [Eleven v3](eleven-v3.md): ElevenLabs' text-to-speech line
- [Voice becomes an agent interface](../trends/voice-becomes-agent-interface.md)

## Recent changes

- [2026-10-20] Launch of v1 Mini and v1 Max in ElevenAgents and an OpenAI-compatible Realtime API.

## Sources

- [Eleven Realtime launch page](../sources/articles/eleven-realtime-2026-10-20.md)
