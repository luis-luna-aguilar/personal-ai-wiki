---
title: GPT-Realtime-2
type: tool
domains: [voice]
subcategory: voice-models
tags: [openai, closed-source, agentic]
as_of: 2026-05-08
sources: [gpt-realtime-2-2026-05-08]
---

# GPT-Realtime-2

OpenAI's flagship streaming speech-to-speech voice model, released May 8, 2026. Brings "GPT-5-class reasoning" into native voice with 128K context, adjustable reasoning effort, tool use, and improved interruption recovery.

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

## Companion models

- **GPT-Realtime-Translate** — live speech-to-speech translation; 70+ input languages → 13 output languages
- **GPT-Realtime-Whisper** — streaming transcription and captions

## Strengths

- 128K context is a meaningful step for long-running voice agents that need to maintain session history
- Adjustable reasoning levels let developers trade latency for quality per request
- Behavioral improvements (social awareness, graceful interruption) address real deployment friction

## Weaknesses / caveats

- Pricing ($1.15-$4.61/hr) remains expensive for consumer-scale voice applications
- ChatGPT voice is still running the older model; upgrade date not announced
- BBA and Conversational Dynamics benchmarks are reported by OpenAI; no independent replication yet

## Recent changes

- [2026-05-08] Initial release; GPT-Realtime-2 goes live in Realtime API with 128K context, GPT-5-class reasoning, and 5 reasoning levels

## Sources

- [GPT-Realtime-2, Translate, and Whisper launch](../sources/newsletters/gpt-realtime-2-2026-05-08.md)
