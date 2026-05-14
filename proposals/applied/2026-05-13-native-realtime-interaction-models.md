---
type: proposal
sources:
  - raw/newsletters/2026-05-12-geminis-next-video-model-leaks.md
  - raw/newsletters/2026-05-12-ex-openai-cto-drops-an-interaction-model.md
  - raw/newsletters/2026-05-13-googles-macbook-competitor.md
  - raw/newsletters/2026-05-12-ainews-thinking-machines-native-interaction-mod.md
status: pending
created: 2026-05-13
---

# Proposal: Native real-time interaction models — Thinking Machines Lab + Google Magic Pointer

## Summary

Two labs shipped AI that watches and responds to live video/audio simultaneously rather than waiting for a turn. Thinking Machines Lab (ex-OpenAI CTO Mira Murati's company) previewed TML-Interaction-Small: 276B parameters, 200ms audio streams, 0.4s end-to-end response, can interrupt mid-sentence, processes live video and audio simultaneously. Google announced "Magic Pointer" for Googlebook — a Gemini-native OS cursor that responds when you click anything on screen. Both move AI from chat-in-a-window toward ambient real-time co-presence.

## Intended changes

- [x] **Update** `wiki/state-of/models.md` — add a new `Real-time interaction models` subcategory; update `as_of` and `sources`
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add recent changes entry for ambient real-time presence
    > **Append to Recent changes:**
    > `- [2026-05-12] Native real-time interaction models arrive: Thinking Machines Lab TML-Interaction-Small (276B, 200ms audio, 0.4s response, mid-sentence interrupts) and Google Magic Pointer (Gemini OS-level cursor for Googlebook) move AI from chat-in-a-window toward ambient real-time co-presence`

- [x] **Create** `wiki/sources/newsletters/thinking-machines-interaction-2026-05-12.md`
    > See draft below

## Schema / vocabulary additions

- [x] Verify that `real-time-interaction` is not already a subcategory in `wiki/_schema/subcategories.md`; if not, propose adding it:
    - Parent domain: `models`
    - Applies to types: `model`, `tool`
    - Definition: AI systems that process live audio and/or video streams and respond with sub-second latency, supporting interruption and ambient co-presence rather than turn-taking conversation.

## Page drafts

### wiki/state-of/models.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-05-05`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append:**
> Add `thinking-machines-interaction-2026-05-12`

**Add new subcategory after `### Specialized utility models` section:**

```markdown
### Real-time interaction models

AI systems that process live audio and video simultaneously and respond with sub-second latency — ambient co-presence rather than turn-taking chat.

- **TML-Interaction-Small** — Thinking Machines Lab (Mira Murati); 276B-parameter model; 200ms audio streams, 0.4s end-to-end response, mid-sentence interruption; processes live video and audio simultaneously; research preview *(as of 2026-05-12)*
- **Gemini Magic Pointer** (Googlebook) — Google; OS-level cursor for the Googlebook laptop that activates Gemini when the user clicks anything on screen; integrates Gemini as a pointing intelligence layer *(as of 2026-05-13)*
```

**Recent changes — prepend before existing entries:**
```
- [2026-05-13] Added `Real-time interaction models` subcategory; TML-Interaction-Small (Thinking Machines Lab, 276B, 200ms audio, 0.4s response) and Google Magic Pointer (Googlebook OS cursor) are the first entries
- [2026-05-12] Thinking Machines Lab previews TML-Interaction-Small: moves AI from turn-taking toward ambient real-time co-presence with live video+audio processing and mid-sentence interruption
```

### wiki/sources/newsletters/thinking-machines-interaction-2026-05-12.md (new)

```markdown
---
title: Native real-time interaction models — Thinking Machines Lab and Google Googlebook
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-12-ex-openai-cto-drops-an-interaction-model.md
published: 2026-05-12
ingested: 2026-05-13
domains: [models, agents]
---

# Native real-time interaction models — Thinking Machines Lab and Google Googlebook

Coverage across four newsletters: ex-OpenAI CTO drops an interaction model, Gemini's next video model leaks, Google's MacBook competitor, and AINews thinking machines. Consolidated into one signal.

## Influenced pages

- [State of Models](../../state-of/models.md) — new `Real-time interaction models` subcategory added
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
- Both systems move AI from "chat in a window" to ambient real-time co-presence
- The interaction model category is distinct from voice models (TTS/STT) — it implies environmental awareness and sub-second reaction time
```

## Feedback

* we need to merge realtime voice with realtime interaction, is the same thing