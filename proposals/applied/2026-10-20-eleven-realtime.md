---
type: proposal
source: raw/articles/2026-10-20-elevenlabsio-realtime.md
status: pending
created: 2026-10-20
---

# Proposal: Eleven Realtime (ElevenLabs speech-to-speech v1 Mini and v1 Max)

## Summary

### In short
OpenAI's Realtime API is turning into the standard plug for voice agents. ElevenLabs' new Eleven Realtime models, v1 Mini for conversation and v1 Max for reasoning and tool calls, accept the same events and work with OpenAI's own SDK. Switching voice vendors now means changing an endpoint and a model name. Both models were tuned as one system and benchmarked by Artificial Analysis, with about 0.6 s to first audio. The proposal adds a tool page, a line in State of Voice and a point on the voice trend page. One reason to hesitate: the page has no launch date, so the ingest date (20 October) is used.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The source is ElevenLabs' product landing page for Eleven Realtime, read on 20 October. The FAQ section was expanded in a browser so its answers are included. ElevenLabs calls it "a new class of Speech to Speech models for building voice agents". Until now a voice agent on ElevenLabs was a pipeline the builder assembled: speech recognition, a turn-taking model that decides when the user has finished, an LLM, and text-to-speech. Eleven Realtime ships that whole chain as one model choice, tuned end to end.

There are two models. **v1 Mini** is the cheaper option for flowing conversation: assistants, tutors and interactive characters. It scores 95.8% on Full-Duplex-Bench, which measures how well a model handles interruptions and overlapping speech, and 988 Elo in the Speech Agent Arena, with 620 ms to first audio. **v1 Max** adds reasoning and tool calls for customer support, lead qualification and scheduling. It scores 98.8% on Big Bench Audio, a spoken-reasoning test, and 87.1% task success, with 570 ms to first audio. Artificial Analysis ran all of these measurements.

The more strategic part is distribution. Inside ElevenLabs' agent builder, ElevenAgents, a Realtime model is one dropdown choice. The same models are also served through a Realtime API that matches OpenAI's: every client and server event arrives in the same form, OpenAI's `@openai/agents-realtime` SDK connects as-is, and a published agent skill (`npx skills add elevenlabs/skills --skill openai-realtime-migration`) handles the switch. The FAQ lists the limits. At launch the API is WebSocket-only, with no WebRTC. API users don't get ElevenAgents features such as phone channels, knowledge base, guardrails and testing. Pricing is per minute of connected audio plus LLM tokens, and the page gives no rates. The page also mentions 90+ languages and a library of 17,500+ voices.

### What changes
The wiki's real-time voice section lists only OpenAI and Thinking Machines models, and its ElevenLabs coverage is text-to-speech (Eleven v3) and transcription (Scribe).

- New page `tools/eleven-realtime.md` covers the two models, their benchmarks, both ways to use them and the API's limits. It is dated 20 October.
- **State of Voice** gains an Eleven Realtime line under Real-time voice / interaction and one Recent-changes entry. Page date moves to 20 October.
- **Voice becomes an agent interface** gains a current-status point: a voice vendor now offers OpenAI's Realtime protocol as a drop-in, so the voice layer is becoming swappable. It also gets a Recent-changes entry, and its page date moves to 20 October.
- One new source page, and an index line.

### What to weigh
The landing page has no publication date, so every derived line uses the ingest date, 20 October. ElevenLabs' docs page ingested on 19 October does not mention Realtime, so the launch probably falls between those days, but that is an inference. The page publishes no prices, so the tool page gives only the pricing structure.

## Intended changes

- [ ] **Create** `wiki/tools/eleven-realtime.md` — new tool page (subcategory `voice-models`, domains voice and agents)
- [ ] **Update** `wiki/state-of/voice.md` — add an Eleven Realtime line at the end of `### Real-time voice / interaction`; add one Recent-changes entry dated 2026-10-20 (no spill); merge source id `eleven-realtime-2026-10-20`; `as_of` → 2026-10-20
- [ ] **Update** `wiki/trends/voice-becomes-agent-interface.md` — add one Current-status bullet; add one Recent-changes entry dated 2026-10-20 (no spill); merge source id; `as_of` → 2026-10-20
- [ ] **Create** `wiki/sources/articles/eleven-realtime-2026-10-20.md` — source summary
- [ ] **Update** `wiki/index.md` — add the tool page line under tools, alphabetically after `tools/eleven-v3`, and bump the page count

## Page drafts

### wiki/tools/eleven-realtime.md (new)

```
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
```

### wiki/state-of/voice.md (updated)

Frontmatter: `as_of: 2026-10-20`; append `eleven-realtime-2026-10-20` to `sources:`.

Append to `### Real-time voice / interaction`:

```
- [Eleven Realtime](../tools/eleven-realtime.md) — ElevenLabs; speech-to-speech v1 Mini (conversation) and v1 Max (reasoning, tool calls), ~0.6 s to first audio; served through an OpenAI-compatible Realtime API as well as ElevenAgents *(as of 2026-10-20)*
```

New Recent-changes entry (newest first):

```
- [2026-10-20] ElevenLabs launches Eleven Realtime v1 Mini and v1 Max, speech-to-speech models with an OpenAI-compatible Realtime API.
```

### wiki/trends/voice-becomes-agent-interface.md (updated)

Frontmatter: `as_of: 2026-10-20`; append `eleven-realtime-2026-10-20` to `sources:`.

Append to `## Current status`:

```
- OpenAI's Realtime API protocol is becoming a common plug: ElevenLabs' Eleven Realtime (October 2026) serves its own speech-to-speech models through an OpenAI-compatible endpoint, so OpenAI's SDK and existing handlers work after an endpoint and model-name change. The voice layer of an agent becomes swappable between vendors.
```

New Recent-changes entry (newest first):

```
- [2026-10-20] ElevenLabs ships Eleven Realtime behind an OpenAI-compatible Realtime API, making voice vendors swappable at the protocol level.
```

Append to `## Sources`:

```
- [Eleven Realtime launch page](../sources/articles/eleven-realtime-2026-10-20.md)
```

### wiki/sources/articles/eleven-realtime-2026-10-20.md (new)

```
---
title: Eleven Realtime launch page (ElevenLabs)
type: source
source_type: article
source_file: raw/articles/2026-10-20-elevenlabsio-realtime.md
url: https://elevenlabs.io/realtime
ingested: 2026-10-20
domains: [voice, agents]
---

# Eleven Realtime launch page (ElevenLabs)

ElevenLabs' product page for Eleven Realtime, a speech-to-speech model family for voice agents with speech recognition, turn-taking, LLM and voice tuned as one system. Two models: v1 Mini for conversation and v1 Max for reasoning and tool calls. They are available in ElevenAgents and through a Realtime API compatible with OpenAI's. The page carries no publication date. The FAQ was expanded in a browser on 20 October.

## Influenced pages
- [Eleven Realtime](../../tools/eleven-realtime.md) — new page
- [State of Voice](../../state-of/voice.md) — new real-time voice line
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — OpenAI Realtime protocol as a cross-vendor plug

## Key claims extracted
- v1 Mini: Full-Duplex-Bench 95.8%, Speech Agent Arena Elo 988, 620 ms time to first audio
- v1 Max: Big Bench Audio 98.8%, task success 87.1%, 570 ms time to first audio
- Benchmarks run by Artificial Analysis; time to first audio averaged on Big Bench Audio
- Realtime API is OpenAI-compatible: same client/server events; OpenAI's SDK works after an endpoint and model-name change; migration skill `openai-realtime-migration`
- WebSocket only at launch, no WebRTC; ElevenAgents features (channels, knowledge base, guardrails, testing) not available via the API
- Pricing: per minute plus LLM tokens; no rates on the page
- 90+ languages, 17,500+ voices
```

### wiki/index.md (updated)

```
- [tools/eleven-realtime](tools/eleven-realtime.md) — ElevenLabs speech-to-speech voice-agent models (v1 Mini, v1 Max) with an OpenAI-compatible Realtime API *(as_of: 2026-10-20)*
```

## Schema / vocabulary additions

None.

## Open questions
- Should GPT-Realtime-2's page also note that ElevenLabs now serves a wire-compatible API, or is the Related link from the new page enough? Assumed: the link is enough.
	- Keep the assumption
