---
type: proposal
sources:
  - raw/newsletters/2026-05-08-ainews-gpt-realtime-2-translate-and-whisper.md
  - raw/newsletters/2026-05-08-openai-drops-new-series-of-voice-models.md
status: pending
created: 2026-05-13
---

# Proposal: OpenAI GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper

## Summary

OpenAI released three new streaming audio models on May 8, 2026. GPT-Realtime-2 is the flagship: "GPT-5-class reasoning" in voice, 128K context (4× the previous 32K), five adjustable reasoning levels, tool use, and improved interruption recovery. GPT-Realtime-Translate handles live speech translation (70+ input languages → 13 output). GPT-Realtime-Whisper is streaming transcription/captions. All three are live in the Realtime API; ChatGPT voice upgrade is "coming soon."

## Intended changes

- [x] **Update** `wiki/state-of/voice.md` — add GPT-Realtime-2 and siblings under a new `Real-time speech-to-speech` subcategory; update `as_of` and `sources`
    > See draft below

- [x] **Create** `wiki/tools/gpt-realtime-2.md` — new tool page
    > See draft below

- [x] **Create** `wiki/sources/newsletters/gpt-realtime-2-2026-05-08.md`
    > See draft below

- [x] **Update** `wiki/index.md` — add entry for `tools/gpt-realtime-2`

## Schema / vocabulary additions

- [ ] Verify `real-time-voice` exists as a subcategory in `wiki/_schema/subcategories.md`; if not, add it:
    - Parent domain: `voice`
    - Applies to types: `tool`, `model`
    - Definition: Voice AI products whose primary mode is streaming speech-to-speech or speech-to-text at sub-second latency, with native interruption handling and conversational turn management.

## Page drafts

### wiki/state-of/voice.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-04-23`
> **After:** `as_of: 2026-05-08`

**Frontmatter `sources` — append:**
> Add `gpt-realtime-2-2026-05-08`

**Add new subcategory before `### Voice models` section:**

```markdown
### Real-time speech-to-speech

Streaming voice AI that processes and responds in real time with sub-second latency, native interruption handling, and multi-turn conversation management. Distinct from TTS (text-to-speech) which produces audio from text rather than handling live conversational audio.

- [GPT-Realtime-2](../tools/gpt-realtime-2.md) — OpenAI; "GPT-5-class reasoning" in voice; 128K context (4× prior), 5 reasoning levels (minimal→xhigh), tool use, interruption recovery, graceful failure handling; API: $1.15/hr input, $4.61/hr output *(as of 2026-05-08)*
- **GPT-Realtime-Translate** — OpenAI; live speech-to-speech translation; 70+ input languages → 13 output languages; available in Realtime API *(as of 2026-05-08)*
- **GPT-Realtime-Whisper** — OpenAI; streaming transcription and captions; available in Realtime API *(as of 2026-05-08)*
```

**Recent changes — prepend:**
```
- [2026-05-08] OpenAI releases GPT-Realtime-2 (128K context, GPT-5-class reasoning, 5 reasoning levels), GPT-Realtime-Translate (70+ → 13 languages), and GPT-Realtime-Whisper; all live in Realtime API; ChatGPT voice upgrade coming soon
- [2026-04-23] Created `state-of/voice` page; added voice models and speech-to-text subcategories from existing tool pages
```

*(The `[2026-04-23]` entry was already in Recent changes — replace it rather than duplicating.)*

### wiki/tools/gpt-realtime-2.md (new)

```markdown
---
title: GPT-Realtime-2
type: tool
domains: [voice]
subcategory: real-time-voice
tags: [openai, closed-source, agentic]
as_of: 2026-05-08
sources: [gpt-realtime-2-2026-05-08]
---

# GPT-Realtime-2

OpenAI's flagship streaming speech-to-speech voice model, released May 8 2026. Brings "GPT-5-class reasoning" into native voice with 128K context, adjustable reasoning effort, tool use, and improved interruption recovery.

## Current status (as of 2026-05-08)

- Live in the Realtime API as of May 8, 2026; ChatGPT voice upgrade "coming soon"
- Context window: 128K tokens (4× the previous 32K Realtime API limit)
- Reasoning: five levels of adjustable effort — minimal, low, medium, high, xhigh — configurable per request
- Benchmark scores (AINews technical breakdown): 96.6% Balanced Behavioral Alignment (BBA); 96.1% Conversational Dynamics; instruction retention improved from 36.7% → 70.8%
- Pricing: $1.15/hour input, $4.61/hour output
- Tool use: supports tool calls during conversation; model says "let me check that" audibly while waiting for results
- Interruption handling: recovers gracefully when the user interrupts; does not re-speak content already said
- Social awareness: does not interrupt when the speaker is talking to someone else in the room
- Failure recovery: graceful audio acknowledgment on tool-call failures rather than silent failure

## Companion models (released same day)

- **GPT-Realtime-Translate** — live speech-to-speech translation; 70+ input languages → 13 output languages
- **GPT-Realtime-Whisper** — streaming transcription and captions

## Strengths

- 128K context is a meaningful step for long-running voice agents that need to maintain session history
- Adjustable reasoning levels let developers trade latency for quality per-request
- Behavioral improvements (social awareness, graceful interruption) address real deployment friction

## Weaknesses / caveats

- Pricing ($1.15–$4.61/hr) remains expensive for consumer-scale voice applications
- ChatGPT voice is still running the older model; upgrade date not announced
- BBA and Conversational Dynamics benchmarks are reported by OpenAI; no independent replication yet

## Recent changes

- [2026-05-08] Initial release; GPT-Realtime-2 goes live in Realtime API with 128K context, GPT-5-class reasoning, and 5 reasoning levels

## Sources

- [GPT-Realtime-2, Translate, and Whisper launch](../sources/newsletters/gpt-realtime-2-2026-05-08.md)
```

### wiki/sources/newsletters/gpt-realtime-2-2026-05-08.md (new)

```markdown
---
title: OpenAI GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper launch
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-08-ainews-gpt-realtime-2-translate-and-whisper.md
published: 2026-05-08
ingested: 2026-05-13
domains: [voice]
---

# OpenAI GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper launch

Two newsletters cover the same release: AINews (technical breakdown) and "OpenAI drops new series of voice models" (product overview). AINews provided the benchmark numbers and pricing detail.

## Influenced pages

- [GPT-Realtime-2](../../tools/gpt-realtime-2.md) — new tool page created
- [State of Voice AI](../../state-of/voice.md) — new `Real-time speech-to-speech` subcategory added

## Key claims extracted

- GPT-Realtime-2 context: 128K tokens (up from 32K)
- Reasoning: "GPT-5-class reasoning" in native voice; 5 levels: minimal, low, medium, high, xhigh
- Benchmarks: 96.6% BBA (Balanced Behavioral Alignment), 96.1% Conversational Dynamics, instruction retention 36.7% → 70.8%
- Pricing: $1.15/hr input, $4.61/hr output
- Behavioral: says "let me check that" during tool calls; does not interrupt a speaker mid-conversation with someone else; graceful failure recovery
- GPT-Realtime-Translate: 70+ input → 13 output languages; live in Realtime API
- GPT-Realtime-Whisper: streaming transcription/captions; live in Realtime API
- ChatGPT voice upgrade to GPT-Realtime-2: "coming soon" (no date)
```

