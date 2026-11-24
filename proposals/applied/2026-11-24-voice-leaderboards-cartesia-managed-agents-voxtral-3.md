---
type: proposal
source: raw/articles/2026-11-23-cartesiaai-blog-managed-agents.md
sources:
  - raw/articles/2026-11-23-cartesiaai-blog-managed-agents.md
  - raw/articles/2026-11-24-mistralai-news-voxtral-3.md
  - raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
  - raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
status: pending
created: 2026-11-24
---

# Proposal: Voice leaderboards — Cartesia Managed Agents leads voice agents; Voxtral 3, Grok Voice Transcribe 2.0 and Kyutai Pocket TTS

## Summary

### In short
Enterprise voice agents are now won by systems whose harness and voice models are tuned together, not by the best single speech-to-speech model: Cartesia's Managed Agents, launched 29 October, ranks first of 30 on Artificial Analysis's Speech Agent Arena (Elo 1115) and first on ServiceNow's EVA-Bench (87.4% accuracy), ahead of Grok Voice 3.0. The proposal adds that leader line to State of Voice, updates the Cartesia and Grok Voice pages and the voice trend, and adds speech-to-text and TTS lines for Mistral's Voxtral 3, Grok Voice Transcribe 2.0 and Kyutai Pocket TTS. One reason to hesitate: Voxtral 3 and Pocket TTS get state-of lines but no pages.

[[#Open questions|Open questions: 2 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 29 October Cartesia, until now known in this wiki for its Sonic text-to-speech and Ink speech-to-text models, launched Managed Agents: a complete platform for enterprise phone agents with telephony, knowledge bases, backend tool calls and outbound call campaigns. Its argument is that pipelines which chain separate transcription, reasoning and speech models lose naturalness, while single speech-to-speech models sound natural but are hard to control, so Cartesia tuned listening, turn-taking, reasoning, tool calls and speech as one system. It says the platform has already handled tens of millions of conversations in finance, retail, hospitality and healthcare. On Artificial Analysis's Speech Agent Arena, where blind raters compare agents booking appointments or ordering food, it ranks first of 30 at Elo 1115. On EVA-Bench, ServiceNow's open benchmark of 200+ customer-service, IT and HR calls, it scores 87.4% accuracy and 90.7% conversational experience; the next speech-to-speech systems are Grok Voice 3.0 (73.7% / 71.2%), Gemini 3.8 Live (45.9% / 88.6%) and GPT Realtime 2.1 (59.0% / 61.6%). Both results used GPT-5.5 as the reasoning model. It supports 44 languages, five switchable mid-call.

Three smaller releases fill out the transcription and speech side. Mistral's Voxtral 3 (22 October) is a family: Small Transcribe 3, which Artificial Analysis ranks third on its word-error index (2.1%), a sub-500 ms realtime transcriber, Mini TTS 3 at $13 per million characters, and a voice-agent SDK built on LiveKit, all on an EU-hosted API or the customer's own servers. Kyutai's Pocket TTS shrinks to 1.9M parameters and claims 103× realtime on one CPU core. In September, Grok Voice Transcribe 2.0 reached 2.7% word error on streaming transcripts, 0.49 s after speech ends, at unchanged prices.

### What changes
The wiki currently names Grok Voice 3.0 the EVA-Bench accuracy leader and lists Cartesia only for its June TTS and STT models; Voxtral appears only as a generic open-weight TTS remark.

- **State of Voice** gains a Cartesia Managed Agents line at the top of real-time voice; the Grok Voice line keeps its speech-to-speech index lead but now says it trails Cartesia on EVA-Bench. New lines for Voxtral 3 and Grok Voice Transcribe 2.0 under speech to text, and for Voxtral Mini TTS 3 and Kyutai Pocket TTS under voice models. One Recent-changes entry; the list reaches its cap of 10 with nothing spilled. Page date stays 8 November.
- **Cartesia** becomes a voice-models-plus-agent-platform page with a Managed Agents section; the "primary documentation not fetched" caveat goes. Page date moves to 29 October.
- **Grok Voice** loses its EVA-Bench lead and gains Grok Voice Transcribe 2.0. Page date moves to 29 October.
- **Voice becomes an agent interface** replaces the generic Voxtral bullet with Voxtral 3 and Pocket TTS, and adds a bullet on co-designed harness-and-model systems leading voice-agent boards. Page date moves to 29 October.
- Four new source pages: Cartesia's launch post, Mistral's Voxtral 3 post, and one story page each for the two AINews issues.

### What to weigh
Voxtral 3 and Kyutai Pocket TTS get bold state-of lines rather than tool pages, following how HeyGen Voice and Fish Audio Drama 3 are handled; a Voxtral page would be justified if Mistral's voice stack keeps coming up. Mistral's own post was fetched today and supplies the product facts and prices; the Artificial Analysis ranks for Voxtral and everything on Pocket TTS come from the AINews summary only.

## Intended changes

- [ ] **Update** `wiki/state-of/voice.md` — add Cartesia Managed Agents leader line; revise Grok Voice line; add Voxtral 3, Grok Voice Transcribe 2.0, Voxtral Mini TTS 3 and Kyutai Pocket TTS lines; append four source ids and links; adds one Recent-changes entry dated 2026-10-29 (list goes 9 → 10, no spill); `as_of` stays 2026-11-08
- [ ] **Update** `wiki/tools/cartesia.md` — Managed Agents section, domains gain `agents`, caveat revised; adds one Recent-changes entry dated 2026-10-29; `as_of` → 2026-10-29
- [ ] **Update** `wiki/tools/grok-voice.md` — EVA-Bench lead moves to Cartesia; Grok Voice Transcribe 2.0 added; adds two Recent-changes entries dated 2026-10-29 and 2026-09-19; `as_of` → 2026-10-29
- [ ] **Update** `wiki/trends/voice-becomes-agent-interface.md` — replace the Voxtral bullet; add one co-design bullet; adds one Recent-changes entry dated 2026-10-29 (list goes 9 → 10, no spill); `as_of` → 2026-10-29
- [ ] **Create** `wiki/sources/articles/cartesia-managed-agents-2026-10-29.md`
- [ ] **Create** `wiki/sources/articles/mistral-voxtral-3-2026-10-22.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-voxtral-3-pocket-tts-2026-10-21.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-grok-voice-transcribe-2-2026-09-19.md`

## Page drafts

### wiki/state-of/voice.md (updated)

Frontmatter: `as_of` unchanged (2026-11-08). Append to `sources:`:

```
cartesia-managed-agents-2026-10-29, mistral-voxtral-3-2026-10-22, ainews-voxtral-3-pocket-tts-2026-10-21, ainews-grok-voice-transcribe-2-2026-09-19
```

`### Real-time voice / interaction` — insert as the first bullet, and replace the Grok Voice bullet:

```
- [Cartesia Managed Agents](../tools/cartesia.md) — Cartesia; enterprise voice-agent platform whose harness and voice models are tuned together; #1 of 30 on AA's Speech Agent Arena (Elo 1115) and #1 on ServiceNow's EVA-Bench (87.4% accuracy, 90.7% experience); 44 languages *(as of 2026-10-29)*
- [Grok Voice](../tools/grok-voice.md) — SpaceXAI; Grok Voice 3.0 is #1 on Artificial Analysis's Speech-to-Speech Index (86.9 vs GPT-Live-1 83.2, Gemini 3.8 Live 82.6) and the top speech-to-speech model on EVA-Bench (73.7%), behind Cartesia's platform; $0.08/min *(as of 2026-10-29)*
```

`### Voice models` — append after the Fish Audio Drama 3 bullet:

```
- **Voxtral Mini TTS 3** — Mistral; context-aware emotion and pacing in 35+ languages, Pro Voice cloning from 30 minutes of audio; top 12 in both AA voice arenas at $13 per 1M characters (112 characters/s); EU-hosted API or self-deployed *(as of 2026-10-22)*
- **Kyutai Pocket TTS** — Kyutai; CPU-sized TTS variants down to 1.9M parameters, claimed 103× realtime on one CPU core, with voice cloning *(as of 2026-10-21)*
```

`### Speech to text` — insert after the MAI-Transcribe-2-Streaming bullet:

```
- **Voxtral 3** — Mistral; Small Transcribe 3 is #3 on AA's word-error index (2.1%), with diarization and keyphrase biasing in 50+ languages; Realtime Transcribe 3 under 500 ms (3.3% AA-WER at 960 ms); $0.0035–0.008/min; ships with a LiveKit-based voice-agent SDK *(as of 2026-10-22)*
- [Grok Voice Transcribe 2.0](../tools/grok-voice.md) — SpaceXAI; 2.7% WER on AA streaming final transcripts, delivered 0.49 s after end of speech (predecessor 3.9%); $0.20/hr streaming, $0.10/hr batch *(as of 2026-09-19)*
```

`## Recent changes` — insert directly below the 2026-11-08 entry:

```
- [2026-10-29] Cartesia Managed Agents takes the voice-agent lead (#1 Speech Agent Arena, #1 EVA-Bench at 87.4% vs Grok Voice 3.0's 73.7%); Grok Voice 3.0 keeps the speech-to-speech index. Speech-to-text and TTS lines added for Mistral's Voxtral 3 (2026-10-22), Grok Voice Transcribe 2.0 (2026-09-19) and Kyutai Pocket TTS (2026-10-21).
```

`## Sources` — append:

```
- [Cartesia — Introducing Managed Agents](../sources/articles/cartesia-managed-agents-2026-10-29.md)
- [Mistral — Voxtral 3](../sources/articles/mistral-voxtral-3-2026-10-22.md)
- [AINews — Voxtral 3 rankings and Kyutai Pocket TTS (Oct 21)](../sources/newsletters/ainews-voxtral-3-pocket-tts-2026-10-21.md)
- [AINews — Grok Voice Transcribe 2.0 (Sep 19)](../sources/newsletters/ainews-grok-voice-transcribe-2-2026-09-19.md)
```

### wiki/tools/cartesia.md (updated)

```
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
```

### wiki/tools/grok-voice.md (updated)

Frontmatter: `as_of: 2026-10-29`; append `ainews-grok-voice-transcribe-2-2026-09-19, cartesia-managed-agents-2026-10-29` to `sources:`.

Intro paragraph, replace with:

```
Grok Voice is SpaceXAI's (formerly xAI) voice model family for voice agents and in-product voice. The current speech-to-speech version, Grok Voice 3.0, is built for customer-support calls and hands-free assistant use, and is sold through the Voice Agent API and Voice Agent Builder. Grok Voice Transcribe 2.0 is the matching speech-to-text model.
```

`## Current status (as of 2026-10-29)` — heading date changes; replace the τ-Voice bullet and append one bullet:

```
- 71.6% on τ-Voice (support calls with accents, noise, and interruptions): close to GPT-Live-1 Astra (74.5% on the blog's chart) at about 40% lower latency. On ServiceNow's EVA-Bench it is the top speech-to-speech model (73.7% accuracy, 71.2% experience) but has been passed by Cartesia's Managed Agents platform (87.4% / 90.7%, 2026-10-29).
- **Grok Voice Transcribe 2.0** (September 2026): 2.7% WER on Artificial Analysis's streaming final-transcript test, delivered 0.49 s after end of speech, down from 3.9% for its predecessor; $0.20/hour streaming and $0.10/hour non-streaming, unchanged.
```

`## Recent changes` — adds two entries; resulting list:

```
- [2026-10-29] Cartesia Managed Agents passes Grok Voice 3.0 on EVA-Bench (87.4% vs 73.7% accuracy) and the Speech Agent Arena (Elo 1115 vs 1070).
- [2026-10-14] Grok Voice 3.0 launched; #1 on AA's Speech-to-Speech Index (86.9), $0.08/min.
- [2026-09-19] Grok Voice Transcribe 2.0: 2.7% streaming WER (was 3.9%), 0.49 s after end of speech, prices unchanged.
```

`## Sources` — append:

```
- [AINews — Grok Voice Transcribe 2.0 (Sep 19)](../sources/newsletters/ainews-grok-voice-transcribe-2-2026-09-19.md)
- [Cartesia — Introducing Managed Agents](../sources/articles/cartesia-managed-agents-2026-10-29.md)
```

### wiki/trends/voice-becomes-agent-interface.md (updated)

Frontmatter: `as_of: 2026-10-29`; append `cartesia-managed-agents-2026-10-29, mistral-voxtral-3-2026-10-22, ainews-voxtral-3-pocket-tts-2026-10-21` to `sources:`.

`## Current status` — replace the bullet "Mistral's Voxtral suggests open-weight text-to-speech is becoming production-relevant, not merely experimental" with:

```
- Self-hosted voice stacks are becoming production-relevant. Mistral's Voxtral 3 (October 2026) ships transcription, TTS and a LiveKit-based voice-agent SDK that can run on Mistral's EU-hosted API or the customer's own servers, with each stage swappable; Kyutai's Pocket TTS shrinks to 1.9M parameters and runs faster than realtime on one CPU core.
```

Insert after the "Customer support is where voice agents now run at volume" bullet:

```
- The voice-agent lead has moved from single speech-to-speech models to systems built as one product (October 2026). Cartesia's Managed Agents, whose harness and voice models were tuned together, tops both Artificial Analysis's Speech Agent Arena and ServiceNow's EVA-Bench, ahead of Grok Voice 3.0; ServiceNow's evaluator calls "harnesses and models designed together" a broader pattern in enterprise voice.
```

`## Recent changes` — insert at the top:

```
- [2026-10-29] Cartesia's co-designed Managed Agents platform leads both voice-agent benchmarks; Mistral's Voxtral 3 (2026-10-22) ships a self-hostable voice-agent stack.
```

`## Sources` — append:

```
- [Cartesia — Introducing Managed Agents](../sources/articles/cartesia-managed-agents-2026-10-29.md)
- [Mistral — Voxtral 3](../sources/articles/mistral-voxtral-3-2026-10-22.md)
- [AINews — Voxtral 3 rankings and Kyutai Pocket TTS (Oct 21)](../sources/newsletters/ainews-voxtral-3-pocket-tts-2026-10-21.md)
```

### wiki/sources/articles/cartesia-managed-agents-2026-10-29.md (new)

```
---
title: Cartesia — Introducing Managed Agents
type: source
source_type: article
source_file: raw/articles/2026-11-23-cartesiaai-blog-managed-agents.md
url: https://cartesia.ai/blog/managed-agents
published: 2026-10-29
ingested: 2026-11-24
domains: [voice, agents]
---

# Cartesia — Introducing Managed Agents

Cartesia's launch post for Managed Agents, an end-to-end enterprise voice-agent platform whose harness and voice models were designed together. It reports #1 rankings on Artificial Analysis's Speech Agent Arena and ServiceNow's EVA-Bench, both run with GPT-5.5 as the reasoning model.

## Influenced pages

- [Cartesia](../../tools/cartesia.md) — Managed Agents section
- [Grok Voice](../../tools/grok-voice.md) — EVA-Bench lead moves to Cartesia
- [State of Voice](../../state-of/voice.md) — new voice-agent leader line
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — co-designed systems bullet

## Key claims extracted

- Launched 2026-10-29; telephony, knowledge bases, tool integrations and outbound campaigns on one platform; tens of millions of conversations in finance, retail, hospitality and healthcare
- Speech Agent Arena (Artificial Analysis, October 2026): #1 of 30, Elo 1115
- EVA-Bench (ServiceNow, 200+ CSM/ITSM/HR scenarios): 87.4% accuracy, 90.7% experience; Grok Voice 3.0 73.7% / 71.2%; Gemini 3.8 Live 45.9% / 88.6%; GPT Realtime 2.1 59.0% / 61.6%
- Internal evaluation: no turn-taking issues in 85% of conversations vs 67% for other agents
- 44 languages; five switchable mid-conversation
```

### wiki/sources/articles/mistral-voxtral-3-2026-10-22.md (new)

```
---
title: Mistral — Voxtral 3
type: source
source_type: article
source_file: raw/articles/2026-11-24-mistralai-news-voxtral-3.md
url: https://mistral.ai/news/voxtral-3
published: 2026-10-22
ingested: 2026-11-24
domains: [voice]
---

# Mistral — Voxtral 3

Mistral's launch post for Voxtral 3: speech-to-text models, a text-to-speech model and a voice-agent SDK in one family, available on Mistral's EU, US and global API endpoints or for self-deployment.

## Influenced pages

- [State of Voice](../../state-of/voice.md) — Voxtral 3 speech-to-text and Voxtral Mini TTS 3 lines
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — self-hosted voice stack bullet

## Key claims extracted

- Voxtral Small Transcribe 3: 50+ languages, diarization, context biasing, end-of-turn detection; Mistral reports it beats Whisper, Scribe v2 and Gemini 3.5 Transcribe
- Voxtral Mini Transcribe 3 is 4B parameters; Realtime Transcribe 3 runs under 500 ms in 35+ languages
- Voxtral Mini TTS 3: 35+ languages and 50+ dialects, context-aware emotion; Pro Voice adaptation from 30 minutes of audio
- Voice-agent SDK built on LiveKit: streaming transcription, any LLM, TTS; SIP and WebRTC; each stage swappable
- Prices: $0.0035/min (Mini batch), $0.008/min (realtime), $0.0040/min (Small), $13 per 1M characters (TTS), $0.04–0.08/min for the voice-agent API
```

### wiki/sources/newsletters/ainews-voxtral-3-pocket-tts-2026-10-21.md (new)

```
---
title: AINews — Voxtral 3 rankings and Kyutai Pocket TTS (Oct 21)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
published: 2026-10-21
ingested: 2026-11-24
domains: [voice]
---

# AINews — Voxtral 3 rankings and Kyutai Pocket TTS (Oct 21)

The speech items from the 21 October AINews issue: Artificial Analysis's measurements of Mistral's Voxtral 3 and Kyutai's smaller Pocket TTS variants.

## Influenced pages

- [State of Voice](../../state-of/voice.md) — Voxtral 3 rankings, Kyutai Pocket TTS line
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — Pocket TTS on one CPU core

## Key claims extracted

- Artificial Analysis ranks Voxtral Small Transcribe 3 #3 at 2.1% AA-WER; the realtime model reaches 3.3% AA-WER at 960 ms
- Voxtral TTS enters the top 12 of both Artificial Analysis voice arenas; $13 per 1M characters at 112.3 characters/s
- Kyutai Pocket TTS variants go down to 1.9M parameters, claiming 103× realtime on one CPU core, with voice cloning
```

### wiki/sources/newsletters/ainews-grok-voice-transcribe-2-2026-09-19.md (new)

```
---
title: AINews — Grok Voice Transcribe 2.0 (Sep 19)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
published: 2026-09-19
ingested: 2026-11-24
domains: [voice]
---

# AINews — Grok Voice Transcribe 2.0 (Sep 19)

The speech item from the 19 September AINews issue: Artificial Analysis's measurement of Grok Voice Transcribe 2.0.

## Influenced pages

- [Grok Voice](../../tools/grok-voice.md) — Transcribe 2.0 bullet
- [State of Voice](../../state-of/voice.md) — speech-to-text line

## Key claims extracted

- Grok Voice Transcribe 2.0: 2.7% WER on streaming final transcripts, 0.49 s after end of speech (predecessor 3.9%)
- Pricing unchanged: $0.20/hour streaming, $0.10/hour non-streaming
```

## Schema / vocabulary additions

None.

## Open questions

- Should Voxtral 3 get its own `tools/voxtral-3.md` page instead of two bold state-of lines? Default: no page until a second source covers it.
	- No page
- Mistral's 22 October charts compare against "Cartesia Sonic 3.6", which the wiki does not track (the Cartesia page names Sonic-3.5). Leave the Cartesia page on Sonic-3.5 until a Cartesia source confirms 3.6 (assumed), or add a one-line note now?
	- Leave it
