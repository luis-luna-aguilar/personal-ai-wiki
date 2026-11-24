---
title: Cartesia
type: tool
domains: [voice, agents]
subcategory: voice-models
tags: []
as_of: 2026-10-29
sources: [cartesia-voice-june-2026, ainews-all-model-labs-are-now-agent-labs, cartesia-managed-agents-2026-10-29]
---

# Cartesia

AI voice company with two layers: low-latency streaming voice models (Sonic-3.5 text-to-speech, Ink-2 speech-to-text) and, since October 2026, Managed Agents, an end-to-end platform for enterprise phone agents built on those models.

## Current status (as of 2026-10-29)

- **Managed Agents** (launched 2026-10-29) — harness and voice models tuned as one system (listening, turn-taking, reasoning, tool calls, speech), with telephony, knowledge bases, backend tool integrations and outbound call campaigns on one platform; Cartesia says it has handled tens of millions of conversations in finance, retail, hospitality and healthcare.
- Managed Agents ranks #1 of 30 on Artificial Analysis's Speech Agent Arena (Elo 1115, October 2026) and #1 on ServiceNow's EVA-Bench (87.4% accuracy, 90.7% experience; Grok Voice 3.0 73.7% / 71.2%, GPT Realtime 2.1 59.0% / 61.6%). Both runs used GPT-5.5 as the reasoning model.
- 44 languages; English, Spanish, Hindi, French and Japanese switchable mid-call. In Cartesia's internal tests callers reported no turn-taking problems in 85% of calls, against 67% for other agents.
- **Sonic-3.5** — streaming TTS; #1 on Artificial Analysis's Speech Arena in May (Elo 1218) and on Together AI's benchmark; ~82ms first-audio latency claimed; strong on IDs, codes and alphanumeric strings.
- **Ink-2** — streaming STT; claims #1 on Together AI's benchmark; sub-90ms latency; 42 languages.

## Weaknesses / caveats

- The Managed Agents benchmark results depend on GPT-5.5 as the reasoning layer; the 85% turn-taking figure is Cartesia's internal evaluation.
- Ink-2's #1 STT claim still rests only on the Together AI benchmark.

## Recent changes

- [2026-10-29] Launched Managed Agents, an enterprise voice-agent platform; #1 on Speech Agent Arena (Elo 1115) and EVA-Bench (87.4% accuracy, 90.7% experience).
- [2026-06-16] Sonic-3.5 and Ink-2 first covered in this wiki (via AINews); claim #1 TTS and STT positions via Together AI. No earlier launch date for either model is documented in any source cited on this page — the 2026-05-23 entry below, reporting a Speech Arena #1 ranking for Sonic-3.5, predates this entry and implies Sonic-3.5 was already live by then.
- [2026-05-23] AINews reports Artificial Analysis ranked Sonic-3.5 #1 on its Speech Arena (Elo 1218, 42 languages); Cartesia separately claims ~82ms end-to-end first-audio latency in production. Second independent evaluator corroborating the Together AI #1 TTS claim.

## Sources

- [Cartesia voice models — June 2026](../sources/newsletters/cartesia-voice-june-2026.md)
- [AINews — All Model Labs are now Agent Labs (Speech Arena #1 ranking)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
- [Cartesia — Introducing Managed Agents](../sources/articles/cartesia-managed-agents-2026-10-29.md)
