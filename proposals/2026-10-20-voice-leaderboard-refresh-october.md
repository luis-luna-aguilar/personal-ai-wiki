---
type: proposal
source: raw/articles/2026-10-20-tco-lkxbuf7u65.md
sources:
  - raw/articles/2026-10-20-tco-lkxbuf7u65.md
  - raw/tweets/2026-10-14-spacexsi-2110416580899168305.md
  - raw/articles/2026-10-20-microsoftai-news-our-first-streaming-transcription-model.md
  - raw/tweets/2026-10-13-fishaudio-2110038429199450126.md
  - raw/articles/2026-10-20-sunocom-blog-introducing-speech-beta.md
  - raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
  - raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
  - raw/newsletters/2026-10-14-ainews-ai-engineer-nyc-gemini-4-argon-vals-ai.md
  - raw/newsletters/2026-10-15-ainews-modals-1b-arr-16b-series-d-makes-it-n.md
  - raw/newsletters/2026-10-16-ainews-agents-disprove-polysemanticity-greatly.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Voice leaderboard refresh (October 2026)

## Summary

### In short
Voice AI's leader lines turned over in October: SpaceXAI's Grok Voice 3.0 ranks first on Artificial Analysis's speech-to-speech index, ahead of OpenAI's GPT-Live-1 (86.9 vs 83.2), and Microsoft's streaming transcription model took first place for accuracy, both pitched at voice agents that answer support calls and act before the caller finishes. Starlink says Grok Voice resolves about 70% of its support calls alone. The proposal refreshes State of Voice across all three subcategories, creates a Grok Voice page, and updates GPT-Live, the MAI family table, the voice trend and the AI-music line. One reason to hesitate: the Suno item has no publication date.

[[#Open questions|Open questions: 2 to answer.]]

### The source
Ten raw files feed this, most of them short. The two substantive posts are launches. On 1 October Microsoft AI released MAI-Transcribe-2-Streaming, its first real-time transcription model: 60 languages with continuous language detection, first rough transcripts ("partials") in just over 100 milliseconds, and first place for accuracy on Artificial Analysis (an independent benchmarking firm) for both partial and final text, at an introductory $0.54 an hour. Alongside it came two text-to-speech models, MAI-Voice-2.1 and a faster Flash variant (150 ms end to end, $15 per million characters), where one cloned voice keeps a native accent across 23 languages. Microsoft frames the pairing around the voice-agent loop: every millisecond saved on hearing and speaking is time the agent can spend reasoning or calling tools.

On 14 October SpaceXAI launched Grok Voice 3.0. Its blog reproduces Artificial Analysis's table: 86.9 on the Speech-to-Speech Index against 83.2 for GPT-Live-1 and 82.6 for Gemini 3.8 Live, 71.6% on τ-Voice (simulated support calls with accents, noise and interruptions), matching GPT-Live-1 at about 40% lower latency, and 97% on Full Duplex Bench, a turn-taking test. It costs $0.08 a minute, runs in Tesla cars and Grok Bot's voice mode, and handles 20,000 Starlink calls a day.

AINews filled in the rest: HeyGen Voice tops the controlled-voice TTS arena, Eleven v4 Turbo tops the provider-voice arena at half Eleven v4's price, Whistle is a 16.9 MB on-device transcriber, and OpenAI shipped GPT-Live-1.1 with multilingual voices and less filler. Fish Audio's open-weight Drama 3 lets users control how single words sound and leads pronunciation robustness, but ranks only 10th and 14th overall on quality. Suno's Speech beta generates narration and music as one track.

### What changes
The voice dashboard was last refreshed on 7 July and names GPT-Live and Cartesia as the newest leaders, with no Microsoft, SpaceXAI, HeyGen or Fish Audio entry.

- **State of Voice** gets Grok Voice as the speech-to-speech leader, GPT-Live moved to second with its 1.1 update, Cartesia's June #1 claim dated, new TTS lines (MAI-Voice-2.1, HeyGen Voice, Drama 3), an Eleven v3 line noting v4, and MAI-Transcribe-2-Streaming leading transcription plus Whistle. Page date moves to 16 October.
- New page `tools/grok-voice.md`.
- **GPT-Live** gains the 1.1 update and its second place; date moves to 16 October.
- **MAI-Thinking-1**'s family table updates the transcription and voice rows; date moves to 1 October.
- **Voice becomes an agent interface** gains one bullet on support-call voice agents; date moves to 14 October.
- **State of Creative** adds Suno Speech to the Suno line; its Recent changes is full, so the oldest entry (22 May) spills to history.
- Ten new source pages.

### What to weigh
The Suno post carries no date, so its lines use the ingest date, 20 October. Eleven v3 now has a successor, but the sources mention v4 only in passing, so the proposal keeps the Eleven v3 page rather than archiving it (see Open questions). Fish Audio's $52M seed round is left out as funding news.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/voice.md` — rewrite the three subcategory lists (new Grok Voice leader line, GPT-Live demoted and updated, four new lines, Eleven v3 line updated); adds one Recent-changes entry dated 2026-10-16 (5 of 10, no spill); merge 10 source ids; `as_of` 2026-07-07 → 2026-10-16.

- [ ] **Create** `wiki/tools/grok-voice.md` — new tool page for the current speech-to-speech leader.

- [ ] **Update** `wiki/tools/gpt-live.md` — two Current-status bullets; adds one Recent-changes entry dated 2026-10-16 (4 of 10); merge sources; `as_of` 2026-08-05 → 2026-10-16.

- [ ] **Update** `wiki/models/mai-thinking-1.md` — replace the MAI-Transcribe-1.5 and MAI-Voice-2 table rows; adds one Recent-changes entry dated 2026-10-01 (3 of 10); merge source; `as_of` 2026-08-13 → 2026-10-01.

- [ ] **Update** `wiki/trends/voice-becomes-agent-interface.md` — one Current-status bullet; adds one Recent-changes entry dated 2026-10-14 (6 of 10); merge sources; `as_of` 2026-08-05 → 2026-10-14.

- [ ] **Update** `wiki/state-of/creative.md` — Suno line extended; adds one Recent-changes entry dated 2026-10-20 (list at cap of 10, so one spill); merge source; `as_of` 2026-09-01 → 2026-10-20.

- [ ] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — the oldest Recent-changes entry (dated 2026-05-22) moves to history.

- [ ] **Create** `wiki/sources/articles/xai-grok-voice-3-2026-10-14.md`
- [ ] **Create** `wiki/sources/tweets/spacexsi-grok-voice-3-2026-10-14.md`
- [ ] **Create** `wiki/sources/articles/microsoft-mai-transcribe-2-streaming-2026-10-01.md`
- [ ] **Create** `wiki/sources/tweets/fishaudio-drama-3-2026-10-13.md`
- [ ] **Create** `wiki/sources/articles/suno-speech-beta-2026-10.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-heygen-voice-whistle-2026-10-10.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-eleven-v4-turbo-2026-10-06.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-fish-drama-3-2026-10-14.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-grok-voice-3-results-2026-10-15.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-live-1-1-2026-10-16.md`

- [ ] **Update** `wiki/index.md` — add `tools/grok-voice`; update the `state-of/voice` and `tools/gpt-live` descriptions and dates.

## Page drafts

### wiki/state-of/voice.md (updated)

Frontmatter: `as_of: 2026-10-16`; append to `sources:` `xai-grok-voice-3-2026-10-14, spacexsi-grok-voice-3-2026-10-14, microsoft-mai-transcribe-2-streaming-2026-10-01, fishaudio-drama-3-2026-10-13, ainews-heygen-voice-whistle-2026-10-10, ainews-eleven-v4-turbo-2026-10-06, ainews-fish-drama-3-2026-10-14, ainews-grok-voice-3-results-2026-10-15, ainews-gpt-live-1-1-2026-10-16`.

Replace the three subcategory lists (intros unchanged):

```
### Real-time voice / interaction

- [Grok Voice](../tools/grok-voice.md) — SpaceXAI; Grok Voice 3.0 is #1 on Artificial Analysis's Speech-to-Speech Index (86.9 vs GPT-Live-1 83.2, Gemini 3.8 Live 82.6); 71.6% τ-Voice at ~40% lower latency than GPT-Live-1; $0.08/min *(as of 2026-10-14)*
- [GPT-Live](../tools/gpt-live.md) — OpenAI; full-duplex ChatGPT Voice family that delegates deeper work to frontier models; GPT-Live-1 is now second on the AA index; GPT-Live-1.1 adds multilingual voices and less filler, API later *(as of 2026-10-16)*
- [GPT-Realtime-2](../tools/gpt-realtime-2.md) — OpenAI; "GPT-5-class reasoning" in voice; 128K context (4× prior), 5 reasoning levels (minimal→xhigh), tool use, interruption recovery, graceful failure handling; API: $1.15/hr input, $4.61/hr output *(as of 2026-05-08)*
- **GPT-Realtime-Translate** — OpenAI; live speech-to-speech translation; 70+ input languages → 13 output languages; available in Realtime API *(as of 2026-05-08)*
- **GPT-Realtime-Whisper** — OpenAI; streaming transcription and captions; available in Realtime API *(as of 2026-05-08)*
- **TML-Interaction-Small** — Thinking Machines Lab (Mira Murati); 276B-parameter interaction model; 200ms audio streams, 0.4s end-to-end response, mid-sentence interruption, and simultaneous live video/audio processing *(as of 2026-05-12)*
- **Gemini Magic Pointer** (Googlebook) — Google; Gemini-powered OS-level pointer that activates on clicked screen context; points toward real-time interaction as an operating-system surface rather than only a chat window *(as of 2026-05-13)*

### Voice models

AI products centered on expressive text-to-speech, speech-to-speech conversation, or voice cloning as a primary interface or output surface.

- **HeyGen Voice** — HeyGen; tops Artificial Analysis's Controlled Voice TTS arena (Elo 1,201); $30 per 1M characters *(as of 2026-10-10)*
- [Eleven v3](../tools/eleven-v3.md) — ElevenLabs; expressive, high-control TTS, now followed by Eleven v4; the cheaper Eleven v4 Turbo tops AA's Provider Voice TTS arena at half v4's price *(as of 2026-10-06)*
- **MAI-Voice-2.1 / MAI-Voice-2.1-Flash** — Microsoft AI (see [MAI family](../models/mai-thinking-1.md)); 23 languages, one cloned voice keeps a native accent across all of them; Flash: 150ms end-to-end, $15 per 1M characters *(as of 2026-10-01)*
- **Fish Audio Drama 3** — open-weight controllable TTS (35B MoE, 3B active, 83 languages, community license); word-level delivery and mid-sentence tone control; leads AA pronunciation robustness (93.2%) and is #1 open-weight, but 10th/14th overall on quality *(as of 2026-10-14)*
- [Hume EVI 3](../tools/hume-evi-3.md) — Hume; speech-to-speech voice model with strong emotional and empathic conversation framing; fits the "voice as agent interface" direction *(as of 2026-04-22)*
- [Cartesia](../tools/cartesia.md) — Cartesia; Sonic-3.5 (streaming TTS) + Ink-2 (streaming STT); claimed #1 for both on Together AI's benchmark in June; sub-90ms latency; 42 languages; strong structured-utterance handling *(as of 2026-06-16)*

### Speech to text

Products focused primarily on transcription, speech recognition, and converting audio into structured text.

- **MAI-Transcribe-2-Streaming** — Microsoft AI; #1 on Artificial Analysis for accuracy on both partial and final transcripts; first partials in just over 100ms so agents can act mid-sentence; 60 languages with continuous detection; $0.54/hr introductory *(as of 2026-10-01)*
- [ElevenLabs Scribe](../tools/elevenlabs-scribe.md) — ElevenLabs; enterprise transcription stack for real-time and operational documentation workflows *(as of 2026-04-22)*
- **Whistle** — 16.9MB on-device speech-to-text model said to rival Whisper base *(as of 2026-10-10)*
```

`## Recent changes` — insert at top:

```
- [2026-10-16] October refresh: Grok Voice 3.0 ranks #1 on AA's Speech-to-Speech Index (86.9), ahead of GPT-Live-1 (83.2), which gets a 1.1 update; MAI-Transcribe-2-Streaming leads streaming STT accuracy; new TTS lines for MAI-Voice-2.1, HeyGen Voice (controlled-voice arena #1), and open-weight Fish Audio Drama 3; Eleven v4 Turbo tops the provider-voice arena.
```

`## Sources` — this page has no `## Sources` section today; add one at the end:

```
## Sources

- [Introducing Grok Voice 3.0 (x.ai)](../sources/articles/xai-grok-voice-3-2026-10-14.md)
- [SpaceXSI — Grok Voice 3.0 launch thread](../sources/tweets/spacexsi-grok-voice-3-2026-10-14.md)
- [Microsoft AI — MAI-Transcribe-2-Streaming and MAI-Voice-2.1](../sources/articles/microsoft-mai-transcribe-2-streaming-2026-10-01.md)
- [Fish Audio — Drama 3 launch](../sources/tweets/fishaudio-drama-3-2026-10-13.md)
- [AINews — HeyGen Voice and Whistle (Oct 10)](../sources/newsletters/ainews-heygen-voice-whistle-2026-10-10.md)
- [AINews — Eleven v4 Turbo (Oct 6)](../sources/newsletters/ainews-eleven-v4-turbo-2026-10-06.md)
- [AINews — Fish Audio Drama 3 results (Oct 14)](../sources/newsletters/ainews-fish-drama-3-2026-10-14.md)
- [AINews — Grok Voice 3.0 results (Oct 15)](../sources/newsletters/ainews-grok-voice-3-results-2026-10-15.md)
- [AINews — GPT-Live-1.1 (Oct 16)](../sources/newsletters/ainews-gpt-live-1-1-2026-10-16.md)
```

### wiki/tools/grok-voice.md (new)

```
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
```

### wiki/tools/gpt-live.md (updated)

Frontmatter: `as_of: 2026-10-16`; append `xai-grok-voice-3-2026-10-14, ainews-gpt-live-1-1-2026-10-16` to `sources:`.

Heading becomes `## Current status (as of 2026-10-16)`; insert these two bullets at the top of the list:

```
- GPT-Live-1.1 (2026-10-16) adds multilingual voices and cuts filler; rolling out to ChatGPT, Codex, and dots, with the API to follow.
- On Artificial Analysis's Speech-to-Speech Index, GPT-Live-1 (Astra, Medium) scores 83.2, second to [Grok Voice](grok-voice.md) 3.0 (86.9); it still edges Grok on τ-Voice support-call success (74.5% vs 71.6%) but at higher latency and cost per task.
```

`## Recent changes` — insert at top:

```
- [2026-10-16] GPT-Live-1.1: multilingual voices and less filler, rolling out to ChatGPT, Codex, and dots; API later. GPT-Live-1 now ranks second on AA's Speech-to-Speech Index (83.2), behind Grok Voice 3.0 (2026-10-14).
```

`## Sources` — append:

```
- [Introducing Grok Voice 3.0 (x.ai)](../sources/articles/xai-grok-voice-3-2026-10-14.md)
- [AINews — GPT-Live-1.1 (Oct 16)](../sources/newsletters/ainews-gpt-live-1-1-2026-10-16.md)
```

### wiki/models/mai-thinking-1.md (updated)

Frontmatter: `as_of: 2026-10-01`; append `microsoft-mai-transcribe-2-streaming-2026-10-01` to `sources:`.

In `## MAI family members`, replace the last two rows:

```
| MAI-Transcribe-2-Streaming | — | #1 AA accuracy (partial and final transcripts); partials in ~100ms; 60 langs | Real-time transcription |
| MAI-Voice-2.1 / 2.1-Flash | — | 23 langs, cross-language cloned voices; Flash 150ms end-to-end | Voice synthesis |
```

`## Recent changes` — insert at top:

```
- [2026-10-01] MAI audio refresh: MAI-Transcribe-2-Streaming (#1 AA streaming accuracy, $0.54/hr intro) and MAI-Voice-2.1 / 2.1-Flash ($22 / $15 per 1M characters) replace the Transcribe-1.5 and Voice-2 rows; see [State of Voice](../state-of/voice.md).
```

`## Sources` — append:

```
- [Microsoft AI — MAI-Transcribe-2-Streaming and MAI-Voice-2.1](../sources/articles/microsoft-mai-transcribe-2-streaming-2026-10-01.md)
```

### wiki/trends/voice-becomes-agent-interface.md (updated)

Frontmatter: `as_of: 2026-10-14`; append `xai-grok-voice-3-2026-10-14, microsoft-mai-transcribe-2-streaming-2026-10-01` to `sources:`.

Append to `## Current status`:

```
- Customer support is where voice agents now run at volume (October 2026). Grok Voice 3.0 handles 20,000 Starlink calls a day with about 70% resolved without a human, and Microsoft pitches streaming transcription partials (first text in ~100ms) so agents can start reasoning and calling tools before the caller finishes. Vendors now compete on agent-task benchmarks (τ-Voice, ServiceNow's EVA-Bench) and latency, not only voice quality.
```

`## Recent changes` — insert at top:

```
- [2026-10-14] Support-call voice agents at scale: Grok Voice 3.0 resolves ~70% of 20,000 daily Starlink calls; Microsoft's streaming STT lets agents act before the caller finishes.
```

`## Sources` — append:

```
- [Introducing Grok Voice 3.0 (x.ai)](../sources/articles/xai-grok-voice-3-2026-10-14.md)
- [Microsoft AI — MAI-Transcribe-2-Streaming and MAI-Voice-2.1](../sources/articles/microsoft-mai-transcribe-2-streaming-2026-10-01.md)
```

### wiki/state-of/creative.md (updated)

Frontmatter: `as_of: 2026-10-20`; append `suno-speech-beta-2026-10` to `sources:`.

Suno line under `### AI music generation` becomes:

```
- **Suno** — category anchor for AI-generated music with reported subscriber and revenue milestones; Speech (beta, open to all users) generates spoken voice and original background music together as one track; no dedicated tool page yet *(as of 2026-10-20)*
```

`## Recent changes` — insert at top, then remove the oldest entry (2026-05-22, see Spill):

```
- [2026-10-20] Suno opened Speech (beta), billed as the first audio model that generates voice and music together as one track.
```

`## Sources` — append:

```
- [Suno — Introducing Speech (beta)](../sources/articles/suno-speech-beta-2026-10.md)
```

### wiki/history/state-of/creative.md (updated)

Append:

```
## Archived from current page on <apply date>

- [2026-05-22] Figma released a native in-canvas design agent (Gemini Flash + Claude Sonnet + Figma fine-tuned models; Every hands-on: good for first drafts, weak on detail fidelity) and Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video (AINews recap); both newsletter-sourced, no primary announcement fetched, no dedicated pages yet.
```

### wiki/index.md (updated)

Add under tools (alphabetical position):

```
- [tools/grok-voice](tools/grok-voice.md) — SpaceXAI speech-to-speech model family; Grok Voice 3.0 is #1 on Artificial Analysis's Speech-to-Speech Index (86.9), $0.08/min, resolves ~70% of Starlink support calls *(as_of: 2026-10-14)*
```

Update existing lines:

```
- [state-of/voice](state-of/voice.md) — current state of AI voice and real-time interaction tools: speech-to-speech, TTS, and speech-to-text leaders *(as_of: 2026-10-16)*
- [tools/gpt-live](tools/gpt-live.md) — OpenAI full-duplex ChatGPT Voice model family; GPT-Live-1 and mini power natural voice interaction while delegating deeper work to frontier models; 1.1 adds multilingual voices; second to Grok Voice 3.0 on AA's index *(as_of: 2026-10-16)*
```

Also bump the dates on the `models/mai-thinking-1` (2026-10-01), `trends/voice-becomes-agent-interface` (2026-10-14), and `state-of/creative` (2026-10-20) lines; increment the page count by one.

### wiki/sources/articles/xai-grok-voice-3-2026-10-14.md (new)

```
---
title: Introducing Grok Voice 3.0 (x.ai)
type: source
source_type: article
source_file: raw/articles/2026-10-20-tco-lkxbuf7u65.md
url: https://x.ai/news/grok-voice-3
published: 2026-10-14
ingested: 2026-10-20
domains: [voice, agents]
---

# Introducing Grok Voice 3.0 (x.ai)

SpaceXAI's launch post for Grok Voice 3.0, with Artificial Analysis's speech-to-speech comparison table against Grok Voice 2.0, GPT-Live-1 (Astra) and Gemini 3.8 Live, plus deployment figures from Tesla and Starlink. The raw file carries no date; the launch thread dates it 2026-10-14.

## Influenced pages

- [Grok Voice](../../tools/grok-voice.md) — page created
- [State of Voice](../../state-of/voice.md) — new real-time leader line
- [GPT-Live](../../tools/gpt-live.md) — index ranking context
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — support-call agents at scale

## Key claims extracted

- #1 on AA Speech-to-Speech Index: 86.9 (Grok Voice 2.0 81.3; GPT-Live-1 Astra Medium 83.2; Gemini 3.8 Live 82.6)
- Big Bench Audio 98.5%; Speech Agent Arena Elo 1070; task success 94.8%; Full Duplex Bench 97.0%
- τ-Voice 71.6% (GPT-Live-1 74.5%, Gemini 3.8 Live 68.6%, Grok Voice 2.0 56.5%) at ~40% lower latency than GPT-Live-1
- AA cost per task on Big Bench Audio: $0.025 vs $0.030 (GPT-Live-1) and $0.055 (GPT-Realtime-2.1 High)
- EVA-Bench (ServiceNow): highest accuracy, 74%
- Millions of conversations a day in Tesla vehicles; powers Grok Bot voice mode
- Starlink: 20,000 calls/day, ~70% resolved with no human, one in four sales calls ends in a purchase
- $0.08/min ($4.80/hr), same as Grok Voice 2.0; `grok-voice-latest` auto-upgraded
```

### wiki/sources/tweets/spacexsi-grok-voice-3-2026-10-14.md (new)

```
---
title: SpaceXSI — Grok Voice 3.0 launch thread
type: source
source_type: tweet
source_file: raw/tweets/2026-10-14-spacexsi-2110416580899168305.md
url: https://x.com/SpaceXSI/status/2110416580899168305
published: 2026-10-14
ingested: 2026-10-20
domains: [voice]
---

# SpaceXSI — Grok Voice 3.0 launch thread

Three-post launch thread for Grok Voice 3.0 pointing to the x.ai blog post, which holds the substance.

## Influenced pages

- [Grok Voice](../../tools/grok-voice.md) — launch date, Starlink figure, pricing

## Key claims extracted

- "The world's most intelligent speech-to-speech model"; responds in under a second
- Frontier voice-agent performance at 40% lower latency; resolves 70% of Starlink support calls on its own
- Available in the API and Voice Agent Builder at $0.08/min
```

### wiki/sources/articles/microsoft-mai-transcribe-2-streaming-2026-10-01.md (new)

```
---
title: "Microsoft AI — Our first streaming transcription model debuts at no. 1 on Artificial Analysis"
type: source
source_type: article
source_file: raw/articles/2026-10-20-microsoftai-news-our-first-streaming-transcription-model.md
url: https://microsoft.ai/news/our-first-streaming-transcription-model/
published: 2026-10-01
ingested: 2026-10-20
domains: [voice, agents]
---

# Microsoft AI — MAI-Transcribe-2-Streaming and MAI-Voice-2.1

Microsoft AI launch post for MAI-Transcribe-2-Streaming, MAI-Voice-2.1 and MAI-Voice-2.1-Flash, framed as building blocks for low-latency voice agents ("a voice agent is a loop: hear, understand, decide, speak").

## Influenced pages

- [State of Voice](../../state-of/voice.md) — STT leader line; MAI-Voice-2.1 TTS line
- [MAI-Thinking-1](../../models/mai-thinking-1.md) — family table rows
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — act-before-the-caller-finishes pattern

## Key claims extracted

- MAI-Transcribe-2-Streaming: 60 languages, automatic continuous language detection; #1 AA accuracy for final and partial transcripts; on AA's accuracy-vs-latency Pareto frontier
- First partial hypotheses in just over 100ms; words appear 2x faster than the closest competitor in Microsoft's internal dictation/subtitle evals
- Introductory price $0.54 per audio hour through end of year
- MAI-Voice-2.1: 23 languages / 26 locales; one voice keeps a native accent across languages; $22 per 1M characters
- MAI-Voice-2.1-Flash: 45s of audio at 150ms end-to-end latency; 55% faster inference, ~60% cheaper than comparable models; $15 per 1M characters
- Both voice models clone from a few seconds of reference audio, with built-in consent guardrails
- Available via Microsoft Foundry, MAI Playground ("Chatter" demo), Vercel, Azure Voice Live, OpenRouter (voice models); LiveKit coming soon
```

### wiki/sources/tweets/fishaudio-drama-3-2026-10-13.md (new)

```
---
title: Fish Audio — Drama 3 open-weight TTS launch
type: source
source_type: tweet
source_file: raw/tweets/2026-10-13-fishaudio-2110038429199450126.md
url: https://x.com/FishAudio/status/2110038429199450126
published: 2026-10-13
ingested: 2026-10-20
domains: [voice]
---

# Fish Audio — Drama 3 open-weight TTS launch

Fish Audio's launch thread for Drama 3, an open-weight text-to-speech model with word-level delivery control. The thread opens with a $52M seed round and 15M+ users; only the model is in scope.

## Influenced pages

- [State of Voice](../../state-of/voice.md) — Drama 3 TTS line

## Key claims extracted

- Drama 3: "the most emotive and controllable TTS model in the world"; open-weight
- Control how a single word sounds, change its tone, shift voice mid-sentence
- Day-one availability across ComfyUI, Runway, Pika, OpenRouter, Vercel, and others; day-0 SGLang support
```

### wiki/sources/articles/suno-speech-beta-2026-10.md (new)

```
---
title: Suno — Introducing Speech (beta)
type: source
source_type: article
source_file: raw/articles/2026-10-20-sunocom-blog-introducing-speech-beta.md
url: https://suno.com/blog/introducing-speech-beta
ingested: 2026-10-20
domains: [creative]
---

# Suno — Introducing Speech (beta)

Suno's announcement of Speech, a beta feature that turns a typed idea or text into spoken audio over original background music, described as the first audio model that generates voice and music together. The post has no date; it was forwarded in early October 2026.

## Influenced pages

- [State of Creative](../../state-of/creative.md) — Suno line

## Key claims extracted

- Speech generates voice and music together as one cohesive track
- Users type text and describe the voice and musical style
- Tested for a month with a small group, now open to everyone as a beta; accents and pauses can misbehave
- Suno frames it as "creative entertainment"; music remains the core product
```

### wiki/sources/newsletters/ainews-heygen-voice-whistle-2026-10-10.md (new)

```
---
title: AINews — HeyGen Voice and Whistle (Oct 10)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
published: 2026-10-10
ingested: 2026-10-20
domains: [voice]
---

# AINews — HeyGen Voice and Whistle (Oct 10)

Speech-model items from the 10 October AINews issue.

## Influenced pages

- [State of Voice](../../state-of/voice.md) — HeyGen Voice and Whistle lines

## Key claims extracted

- HeyGen Voice tops Artificial Analysis's Controlled Voice TTS arena, Elo 1,201, $30 per 1M characters, 40 characters/s
- Whistle: 16.9MB on-device STT model said to rival Whisper base
```

### wiki/sources/newsletters/ainews-eleven-v4-turbo-2026-10-06.md (new)

```
---
title: AINews — Eleven v4 Turbo (Oct 6)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
published: 2026-10-06
ingested: 2026-10-20
domains: [voice]
---

# AINews — Eleven v4 Turbo (Oct 6)

One-line TTS item from the 6 October AINews issue.

## Influenced pages

- [State of Voice](../../state-of/voice.md) — Eleven line

## Key claims extracted

- Eleven v4 Turbo tops Artificial Analysis's Provider Voice TTS arena at half the price of Eleven v4
```

### wiki/sources/newsletters/ainews-fish-drama-3-2026-10-14.md (new)

```
---
title: AINews — Fish Audio Drama 3 results (Oct 14)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-14-ainews-ai-engineer-nyc-gemini-4-argon-vals-ai.md
published: 2026-10-14
ingested: 2026-10-20
domains: [voice]
---

# AINews — Fish Audio Drama 3 results (Oct 14)

Drama 3 specifications and Artificial Analysis results from the 14 October AINews issue.

## Influenced pages

- [State of Voice](../../state-of/voice.md) — Drama 3 TTS line

## Key claims extracted

- 35B MoE, 3B active, 83 languages, Fish Audio Community License
- Word-level delivery changes and mid-sentence tone shifts
- Leads AA pronunciation robustness at 93.2% (Eleven v4 91.7%); #1 open-weight on all three AA speech leaderboards; 10th overall in Provider Voice, 14th in Controlled Voice
- API pricing $15 per 1M characters
```

### wiki/sources/newsletters/ainews-grok-voice-3-results-2026-10-15.md (new)

```
---
title: AINews — Grok Voice 3.0 results (Oct 15)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-15-ainews-modals-1b-arr-16b-series-d-makes-it-n.md
published: 2026-10-15
ingested: 2026-10-20
domains: [voice]
---

# AINews — Grok Voice 3.0 results (Oct 15)

Grok Voice 3.0 and Drama 3 follow-ups from the 15 October AINews issue.

## Influenced pages

- [Grok Voice](../../tools/grok-voice.md) — time to first audio
- [State of Voice](../../state-of/voice.md) — Grok Voice leader line

## Key claims extracted

- AA Speech-to-Speech Index: Grok Voice 3.0 #1 at 86.9, ahead of GPT-Live-1 Astra 83.2
- 71.6% τ-Voice, 98.5% Big Bench Audio, 0.81s time to first audio
- Drama 3 weights on Hugging Face; INT4 checkpoint cuts engine weight memory from 37.0 GB to 20.8 GB on SGLang Omni
```

### wiki/sources/newsletters/ainews-gpt-live-1-1-2026-10-16.md (new)

```
---
title: AINews — GPT-Live-1.1 (Oct 16)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-16-ainews-agents-disprove-polysemanticity-greatly.md
published: 2026-10-16
ingested: 2026-10-20
domains: [voice]
---

# AINews — GPT-Live-1.1 (Oct 16)

One voice item from the 16 October AINews issue.

## Influenced pages

- [GPT-Live](../../tools/gpt-live.md) — 1.1 update
- [State of Voice](../../state-of/voice.md) — GPT-Live line

## Key claims extracted

- GPT-Live-1.1 adds multilingual voices and cuts filler
- Rolling out to ChatGPT, Codex, and dots; API coming later
```

## Schema / vocabulary additions

None.

## Open questions

- Eleven v3 is now followed by Eleven v4 and v4 Turbo, which operating principle 12 would normally handle by archiving `tools/eleven-v3.md` and creating a v4 page. The sources here give v4 two passing mentions only, so the proposal keeps the v3 page and names v4 on its State of Voice line. Archive now, or wait for a primary v4 source (assumed wait)?
- Should Microsoft's audio models get their own `tools/mai-voice.md` page instead of living as rows on the MAI-Thinking-1 family table (assumed no)?
