---
title: Grok Voice
type: tool
domains: [voice, agents]
subcategory: voice-models
tags: [xai, closed-source, voice, agentic]
as_of: 2026-10-14
sources: [xai-grok-voice-3-2026-10-14, spacexsi-grok-voice-3-2026-10-14, ainews-grok-voice-3-results-2026-10-15]
---

# Grok Voice

Grok Voice is SpaceXAI's (formerly xAI) speech-to-speech model family for voice agents and in-product voice. The current version, Grok Voice 3.0, is built for customer-support calls and hands-free assistant use, and is sold through the Voice Agent API and Voice Agent Builder.

## Current status (as of 2026-10-14)

- Grok Voice 3.0 launched 2026-10-14 and is #1 on Artificial Analysis's Speech-to-Speech Index at 86.9 (Grok Voice 2.0 81.3, GPT-Live-1 Astra 83.2, Gemini 3.8 Live 82.6). The index combines speech reasoning, τ-Voice, and blind head-to-head preference and task success.
- 98.5% Big Bench Audio, Speech Agent Arena Elo 1070, 94.8% task success, 97% Full Duplex Bench (pauses, turn-taking, interruptions); 0.81s time to first audio per AA.
- 71.6% on τ-Voice (support calls with accents, noise, and interruptions): close to GPT-Live-1 Astra (74.5% on the blog's chart) at about 40% lower latency. Highest accuracy (74%) on ServiceNow's EVA-Bench for enterprise voice agents.
- $0.08/min ($4.80/hr), unchanged from 2.0; `grok-voice-latest` switched automatically. AA's cost per task on Big Bench Audio: $0.025 vs $0.030 for GPT-Live-1 and $0.055 for GPT-Realtime-2.1.
- Deployed at scale: millions of conversations a day in Tesla vehicles and in [Grok Bot](grok-bot.md)'s voice mode; Starlink call centers take 20,000 calls a day, about 70% resolved with no human, and one agent verifies customers, troubleshoots hardware, issues credits, and ships replacements.

## Weaknesses / caveats

- On τ-Voice alone it trails GPT-Live-1 Astra slightly; its lead is in the combined index, latency, and price.

## Recent changes

- [2026-10-14] Grok Voice 3.0 launched; #1 on AA's Speech-to-Speech Index (86.9), $0.08/min.

## Sources

- [Introducing Grok Voice 3.0 (x.ai)](../sources/articles/xai-grok-voice-3-2026-10-14.md)
- [SpaceXSI — Grok Voice 3.0 launch thread](../sources/tweets/spacexsi-grok-voice-3-2026-10-14.md)
- [AINews — Grok Voice 3.0 results (Oct 15)](../sources/newsletters/ainews-grok-voice-3-results-2026-10-15.md)
