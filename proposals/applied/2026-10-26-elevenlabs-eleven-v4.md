---
type: proposal
source: raw/articles/2026-10-26-elevenlabsio-v4.md
status: pending
created: 2026-10-26
---

# Proposal: Eleven v4 and v4 Turbo supersede Eleven v3

## Summary

### In short

ElevenLabs has merged its two text-to-speech lines, expressive and real-time, into one family. Eleven v4 is for directed, emotional speech in 90+ languages. Eleven v4 Turbo has the same range at about 150 ms to first speech, for voice agents. Professional Voice Clones, which v3 dropped, are back. The proposal applies the superseded-version rule. It creates an Eleven v4 page, moves the Eleven v3 page to history, swaps the State of Voice leader line, and re-points the index, the schema example and one source note. Reason to hesitate: the product page carries no release date, so ingest date stands in.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

The source is ElevenLabs' product page for Eleven v4 and Eleven v4 Turbo. ElevenLabs calls Eleven v4 its most emotive model. It runs on a new architecture that reads a script "the way a voice actor would", keeping track of who is speaking and what just happened. Writers put direction straight into the text with tags like [laughs], [whispers] or [door slams], and v4 follows those tags more reliably than v3. "Context stitching" keeps pacing steady over a script of any length, so an audiobook sounds like one take. Regenerating a line keeps the same speaker's voice. Professional Voice Clones, trained near-exact copies of a voice, were not supported in v3 and now return with v4's full emotional range.

Eleven v4 Turbo is the real-time variant, available through the API and ElevenAgents. It has a median inference latency of about 100 ms and a median time to first speech of about 150 ms. It streams in both directions, so audio starts before the language model finishes its sentence. On ElevenLabs' own chart, Cartesia Sonic 3.6 takes 262 ms and OpenAI's GPT-4o mini TTS 814 ms. Both models share the same clones, so one brand voice holds across a whole call. The page also lists 17,500+ stock voices, cloning from ten seconds of audio, voice design from a text description, and a pronunciation dictionary. Access is through `eleven_v4` in the API, with a free tier and paid plans from $6 a month. Salesforce's Agentforce Voice team says v4 Turbo raised the bar for its voice agents.

### What changes

The wiki lists Eleven v3, last checked in April, as ElevenLabs' latest expressive model.

- New page `tools/eleven-v4.md` covers both models: what v4 adds over v3, the Turbo latency figures and ElevenLabs' comparison, voice tooling, API access and pricing.
- The **Eleven v3** page moves to `wiki/history/tools/eleven-v3.md` unchanged, apart from a "superseded by" line and fixed relative links.
- **State of Voice** swaps the Eleven v3 leader line for Eleven v4 and adds a Recent-changes entry. Its page date moves to 26 October.
- The **index** replaces the v3 line with a v4 line, the `voice-models` **schema** example points to Eleven v4, and the **legacy roadmap source note** points its v3 link at the archived page.

### What to weigh

The page shows no publication date, so `as_of` uses the 26 October ingest date. Eleven v4 was already out earlier in October, so the new page reads newer than the release. The v4 Turbo latency comparison against Cartesia and OpenAI is recorded on the Eleven v4 page only. The Cartesia leader line on State of Voice is left alone.

## Intended changes

- [ ] **Create** `wiki/tools/eleven-v4.md` — current ElevenLabs TTS family (v4 and v4 Turbo); successor to Eleven v3
    > See draft below

- [ ] **Move** `wiki/tools/eleven-v3.md` → `wiki/history/tools/eleven-v3.md` — superseded by Eleven v4; removed from live `wiki/tools/`, `wiki/state-of/voice.md` and `wiki/index.md`
    > See draft below (verbatim copy of the live page plus a superseded line, links rewritten for the new depth)

- [ ] **Update** `wiki/state-of/voice.md` — replace the Eleven v3 leader line under `### Voice models` with an Eleven v4 line; add one Recent-changes entry dated 2026-10-26 at the top; append one source id; `as_of` 2026-07-07 → 2026-10-26
    > See draft below

- [ ] **Update** `wiki/index.md` — replace the `tools/eleven-v3` line with `tools/eleven-v4`; update the `state-of/voice` date; page counts unchanged (one page in, one out)
    > See draft below

- [ ] **Update** `wiki/_schema/subcategories.md` — re-point the `voice-models` example from Eleven v3 to Eleven v4
    > See draft below

- [ ] **Update** `wiki/sources/notes/legacy-ai-tools-roadmap-xlsx.md` — re-point the Eleven v3 influenced-page link to the archived page
    > See draft below

- [ ] **Create** `wiki/sources/articles/elevenlabs-eleven-v4.md` — source summary for the product page

## Page drafts

### wiki/tools/eleven-v4.md (new)

```
---
title: Eleven v4
type: tool
domains: [agents, voice]
subcategory: voice-models
tags: [elevenlabs, closed-source]
as_of: 2026-10-26
sources: [elevenlabs-eleven-v4]
---

# Eleven v4

ElevenLabs' current text-to-speech model family and the successor to Eleven v3. **Eleven v4** is for expressive, directed generated speech; **Eleven v4 Turbo** carries the same expressive range at real-time latency for voice agents. Both run on a new architecture that reads a script "the way a voice actor would", tracking who is speaking and what just happened.

## Current status (as of 2026-10-26)

- **Eleven v4:** 90+ languages, multiple speakers, and built-in sound effects. Follows inline direction tags ([laughs], [whispers], [door slams]) more reliably than v3; "context stitching" keeps pacing steady across scripts of any length (an audiobook as "a single take"); regenerating a line keeps the same speaker identity.
- **Professional Voice Clones** are back: unsupported in v3, they now perform with v4's full emotional range in every language, and work identically on v4 and v4 Turbo.
- **Eleven v4 Turbo:** median inference latency ~100 ms, median time to first speech ~150 ms, bidirectional streaming (push text as the LLM generates it, audio returns before the sentence ends); available through the API and ElevenAgents. ElevenLabs' own chart puts time to first speech at 150 ms vs. 262 ms for Cartesia Sonic 3.6 and 814 ms for OpenAI GPT-4o mini TTS.
- **Voice tooling:** 17,500+ library voices, instant cloning from ten seconds of audio, Voice Design from a one-sentence description, and a pronunciation dictionary with IPA support.
- **Access and price:** `model_id` `eleven_v4` through the REST API, streaming endpoints, and TypeScript/Python SDKs; free plan with 10,000 credits a month, paid plans from $6 a month, enterprise custom.

## Strengths

- One family covers both polished generated audio and live agent conversation, with one voice identity across both
- Direction lives in the script itself, which suits narration, dialogue, and character work

## Weaknesses / caveats

- The latency comparison is ElevenLabs' own chart, and the product page gives no release date
- Turbo's expressive range at conversational speed is described, not measured, on the source page

## Recent changes

- [2026-10-26] Page created for Eleven v4 and v4 Turbo; supersedes [Eleven v3](../history/tools/eleven-v3.md), which moved to history.

## Sources

- [Eleven v4 and Eleven v4 Turbo (ElevenLabs product page)](../sources/articles/elevenlabs-eleven-v4.md)
```

### wiki/history/tools/eleven-v3.md (new)

```
---
title: Eleven v3
type: tool
domains: [agents, voice]
subcategory: voice-models
tags: [elevenlabs, closed-source]
as_of: 2026-04-22
sources: [eleven-v3, legacy-ai-tools-roadmap-xlsx]
---

# Eleven v3

Eleven v3 is ElevenLabs' expressive text-to-speech model. Its core role is high-control, emotionally directed speech synthesis rather than low-latency real-time voice conversation.

**Superseded by [Eleven v4](../../tools/eleven-v4.md), 2026-10-26.**

## Current status (as of 2026-04-22)

- Latest expressive TTS model in ElevenLabs documentation
- Stronger fit for polished generated voice output than conversational turn-taking
- Useful to keep separate from speech-to-text and speech-to-speech products

## Sources

- [Eleven v3 docs](../../sources/articles/eleven-v3.md)
- [AI Tools & Roadmap legacy workbook](../../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
```

### wiki/state-of/voice.md (updated)

Frontmatter: `as_of: 2026-10-26`; `sources:` append `elevenlabs-eleven-v4`.

Under `### Voice models`, replace the Eleven v3 line:

> **Before:** `- [Eleven v3](../tools/eleven-v3.md) — ElevenLabs; high-control expressive text-to-speech; stronger for polished generated voice output than conversational turn-taking *(as of 2026-04-22)*`

```
- [Eleven v4](../tools/eleven-v4.md) — ElevenLabs; successor to Eleven v3: expressive, directed TTS in 90+ languages with inline audio tags and Professional Voice Clones, plus Eleven v4 Turbo for real-time agents (~150 ms median time to first speech) *(as of 2026-10-26)*
```

In `## Recent changes`, insert at the top:

```
- [2026-10-26] Eleven v4 and v4 Turbo replace Eleven v3 under Voice models; the v3 page moved to history.
```

### wiki/index.md (updated)

Under `## State of`, replace the `state-of/voice` line:

```
- [state-of/voice](state-of/voice.md) — current state of AI voice and real-time interaction tools *(as_of: 2026-10-26)*
```

Under `## Tools`, replace the `tools/eleven-v3` line:

> **Before:** `- [tools/eleven-v3](tools/eleven-v3.md) — expressive text-to-speech model optimized for high-control generated voice output *(as_of: 2026-04-22)*`

```
- [tools/eleven-v4](tools/eleven-v4.md) — ElevenLabs' current TTS family (supersedes Eleven v3): expressive v4 with inline direction tags and Professional Voice Clones, plus v4 Turbo for real-time agents (~150 ms to first speech) *(as_of: 2026-10-26)*
```

### wiki/_schema/subcategories.md (updated)

Under `### voice-models`:

> **Before:** `- **Examples:** [Hume EVI 3](../tools/hume-evi-3.md), [Eleven v3](../tools/eleven-v3.md)`

```
- **Examples:** [Hume EVI 3](../tools/hume-evi-3.md), [Eleven v4](../tools/eleven-v4.md)
```

### wiki/sources/notes/legacy-ai-tools-roadmap-xlsx.md (updated)

In `## Influenced pages`:

> **Before:** `- [Eleven v3](../../tools/eleven-v3.md)`

```
- [Eleven v3](../../history/tools/eleven-v3.md) (archived; superseded by Eleven v4)
```

### wiki/sources/articles/elevenlabs-eleven-v4.md (new)

```
---
title: Eleven v4 and Eleven v4 Turbo (ElevenLabs product page)
type: source
source_type: article
source_file: raw/articles/2026-10-26-elevenlabsio-v4.md
url: https://elevenlabs.io/v4
ingested: 2026-10-26
domains: [voice, agents]
---

# Eleven v4 and Eleven v4 Turbo (ElevenLabs product page)

ElevenLabs' product page for its v4 text-to-speech family: Eleven v4 for expressive generated speech and Eleven v4 Turbo for real-time agents. The page carries no publication date; derived pages use the ingest date.

## Influenced pages

- [Eleven v4](../../tools/eleven-v4.md) — new page
- [State of Voice](../../state-of/voice.md) — Voice models leader line swapped from Eleven v3
- [Eleven v3](../../history/tools/eleven-v3.md) — archived as superseded

## Key claims extracted

- Eleven v4: "our most emotive model yet"; new architecture that reads a script like a voice actor; 90+ languages, multi-speaker, built-in sound effects
- Follows inline tag sequences ([laughs], [whispers], [door slams]) more reliably than v3; context stitching for long-form audio; no vocal drift on regeneration
- Professional Voice Clones, unsupported in v3, return in v4 with full emotional range across languages
- Eleven v4 Turbo: median inference latency ~100 ms, median time to first speech ~150 ms; bidirectional streaming; available via API and ElevenAgents; same PVCs as v4
- ElevenLabs' chart of median time to first speech: v4 Turbo 150 ms, Cartesia Sonic 3.6 262 ms, OpenAI GPT-4o mini TTS 814 ms
- 17,500+ voices; cloning from ten seconds of audio; Voice Design from a description; pronunciation dictionary with IPA
- API `model_id: eleven_v4`; free plan 10,000 credits/month; paid from $6/month; enterprise custom
- Customer quotes: Salesforce Agentforce Voice (v4 Turbo), BeyondWords, Rosebud, Accenture, Spring Financial
```

## Schema / vocabulary additions

None.

## Open questions

- Eleven v4 shipped before the ingest date: an early-October newsletter in `raw/` already ranks v4 Turbo. Backdate `as_of` on the new page and on the State of Voice line to the earliest dated mention, or keep the ingest date the schema prescribes when the source has no date (assumed: keep 26 October)?
	- Keep it
