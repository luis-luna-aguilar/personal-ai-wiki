---
title: Native real-time interaction models — Thinking Machines Lab and Google Googlebook
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-12-ex-openai-cto-drops-an-interaction-model.md
published: 2026-05-12
ingested: 2026-05-13
domains: [models, agents, voice]
---

# Native real-time interaction models — Thinking Machines Lab and Google Googlebook

Coverage across four newsletters: ex-OpenAI CTO drops an interaction model, Gemini's next video model leaks, Google's MacBook competitor, and AINews thinking machines. Consolidated into one signal.

## Influenced pages

- [State of Models](../../state-of/models.md) — real-time voice / interaction model note added
- [State of Voice AI](../../state-of/voice.md) — merged `Real-time voice / interaction` subcategory updated
- [State of Agents](../../state-of/agents.md) — ambient real-time presence note in Recent changes

## Key claims extracted

### Thinking Machines Lab (TML-Interaction-Small)
- Company: Thinking Machines Lab, founded by ex-OpenAI CTO Mira Murati
- Model name: TML-Interaction-Small
- Architecture: ~276B parameters
- Audio latency: 200ms audio streams; 0.4s end-to-end response to audio input
- Simultaneous video + audio: processes live video and audio at the same time — not sequential
- Interruption: can interrupt mid-sentence when the user starts speaking
- Framing: "interaction model" rather than "voice model" — the distinction is that it processes environmental context (video) rather than only audio turns
- Status: research preview (no commercial release date announced)

### Google Googlebook + Magic Pointer
- Product: Googlebook — Google's MacBook competitor laptop
- Feature: "Magic Pointer" — a Gemini-powered OS-level cursor
- Behavior: when the user clicks anything on screen, Gemini activates and responds to that context
- Runs Android apps natively (no emulation layer)
- Positioning: direct Apple competitor on AI-native hardware

### Broader framing
- These systems move AI from "chat in a window" to ambient real-time co-presence
- Per user feedback, this belongs with real-time voice rather than as a separate category: both require live context, interruption handling, and sub-second reaction time
