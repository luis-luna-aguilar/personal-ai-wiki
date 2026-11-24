---
type: proposal
source: raw/tweets/2026-10-22-xcom-elevencreativestatus2112911862.md
status: pending
created: 2026-11-24
---

# Proposal: ElevenCreative Chimera (Eleven v4 voice + Seedance 2.5 video)

## Summary

### In short
Talking-character video is now a packaged consumer template: ElevenLabs' Chimera turns one photo of a human, cartoon or pet plus a scripted line into a speaking clip, with Eleven v4 performing the voice and ByteDance's Seedance 2.5 animating the face. The proposal adds a Chimera bullet to **Eleven v4**, notes on **Seedance 2.0** that a 2.5 version exists, and creates one source page. The reason to hesitate is thin evidence on Seedance 2.5: this launch post is the wiki's only mention of it, too little to justify a new version page or to archive 2.0.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 21 October 2026, ElevenLabs' creative-app account, ElevenCreative, announced Chimera on X. Chimera pairs two models the post calls among "the world's leading": Eleven v4, ElevenLabs' current text-to-speech model, and Seedance 2.5, ByteDance's video model. The workflow is short. You create or upload a character, write the line it should say, and pick a library voice or design one. Inline audio tags such as [whispers], [laughs] and [yells] set the timing and mood of each word. In the post's words, "Eleven v4 puts the emotion in the voice. Seedance 2.5 carries it onto the face."

In replies, the account confirmed three practical details. Chimera accepts any character, including cartoons, anime-style art and pets. You can skip generated speech and upload your own audio under Speech. The tool sits on ElevenCreative's homepage under More Tools > Templates > Chimera. The post gives no pricing, length limit or resolution.

### What changes
The wiki already covers Eleven v4 as ElevenLabs' expressive TTS family with inline direction tags, and tracks ByteDance's video product only as Seedance 2.0, from an April product page.

- **Eleven v4** gains a status bullet on Chimera as the first packaged voice-plus-video use of v4's direction tags, and a Recent-changes entry dated 21 October. The page date stays 26 October, since that is newer.
- **Seedance 2.0** gains a status bullet saying ByteDance has shipped Seedance 2.5, with Chimera as the only evidence so far, and a new Recent-changes section with that entry. Page date moves to 21 October, and its index line follows.
- One new source page for the ElevenCreative launch post.

### What to weigh
The only judgment call is how to handle Seedance 2.5. Under the rule that superseded versions move to history, a new version would normally get its own page and push 2.0 into the archive. One launch post from a partner gives a version name and nothing else: no release date, no capabilities, no ByteDance source. The proposal therefore records 2.5 on the existing page and leaves the rename for when a ByteDance source arrives.

## Intended changes

- [ ] **Update** `wiki/tools/eleven-v4.md` — add a Chimera status bullet; adds one Recent-changes entry dated 2026-10-21 (list has 1 entry, no spill); append source id `elevencreative-chimera-2026-10-21`; `as_of` stays 2026-10-26
- [ ] **Update** `wiki/tools/seedance-2.md` — add a Seedance 2.5 status bullet; add a `## Recent changes` section with one entry dated 2026-10-21; append source; `as_of` 2026-04-22 → 2026-10-21
- [ ] **Update** `wiki/index.md` — Seedance 2.0 line `as_of` 2026-04-22 → 2026-10-21
- [ ] **Create** `wiki/sources/tweets/elevencreative-chimera-2026-10-21.md` — source summary

## Page drafts

### wiki/tools/eleven-v4.md (updated)

Frontmatter (only `sources:` changes):

```
sources: [elevenlabs-eleven-v4, ainews-eleven-v4-turbo-2026-10-06, elevencreative-chimera-2026-10-21]
```

Append to `## Current status (as of 2026-10-26)`:

```
- **Chimera (ElevenCreative, 2026-10-21):** a template that pairs Eleven v4 with ByteDance's Seedance 2.5 to make talking-character video. Upload or create a character (human, cartoon or pet), write the line, pick or design a voice, and direct it with audio tags ([whispers], [laughs], [yells]); v4 performs the voice and Seedance animates the face. Own audio can replace generated speech. Found under More Tools > Templates.
```

`## Recent changes` (adds one entry, newest first):

```
- [2026-10-26] Page created for Eleven v4 and v4 Turbo; supersedes [Eleven v3](../history/tools/eleven-v3.md), which moved to history.
- [2026-10-21] ElevenCreative launches Chimera, pairing Eleven v4 voices with Seedance 2.5 face animation for talking characters.
```

`## Sources` (append):

```
- [ElevenCreative — Chimera launch post](../sources/tweets/elevencreative-chimera-2026-10-21.md)
```

### wiki/tools/seedance-2.md (updated)

Frontmatter:

```
as_of: 2026-10-21
sources: [seedance-2, legacy-ai-tools-roadmap-xlsx, elevencreative-chimera-2026-10-21]
```

Append to `## Current status (as of 2026-04-22)`, retitled `## Current status (as of 2026-10-21)`:

```
- ByteDance has since shipped **Seedance 2.5**. The only evidence in the wiki is ElevenLabs' Chimera launch (2026-10-21), which uses Seedance 2.5 to animate faces in sync with Eleven v4 voices; no ByteDance source for 2.5 has been ingested yet, so this page still describes 2.0
```

New section, inserted before `## Sources`:

```
## Recent changes

- [2026-10-21] Seedance 2.5 appears as the video model in ElevenLabs' Chimera talking-character template.
```

`## Sources` (append):

```
- [ElevenCreative — Chimera launch post](../sources/tweets/elevencreative-chimera-2026-10-21.md)
```

### wiki/index.md (updated)

```
- [tools/seedance-2](tools/seedance-2.md) — ByteDance Seed's multimodal audio-video generation product *(as_of: 2026-10-21)*
```

### wiki/sources/tweets/elevencreative-chimera-2026-10-21.md (new)

```
---
title: ElevenCreative — Chimera launch post
type: source
source_type: tweet
source_file: raw/tweets/2026-10-22-xcom-elevencreativestatus2112911862.md
url: https://x.com/elevencreative/status/2112911862451048478
published: 2026-10-21
ingested: 2026-11-24
domains: [voice, creative]
---

# ElevenCreative — Chimera launch post

ElevenLabs' ElevenCreative account announced Chimera, a template that pairs Eleven v4 (voice) with ByteDance's Seedance 2.5 (video) to turn a character image and a scripted line into a talking clip. Audio tags direct the performance; replies confirm it works on cartoons and pets, accepts uploaded audio, and lives under More Tools > Templates. No pricing or limits given.

## Influenced pages
- [Eleven v4](../../tools/eleven-v4.md) — Chimera status bullet and Recent-changes entry
- [Seedance 2.0](../../tools/seedance-2.md) — first mention of Seedance 2.5

## Key claims extracted
- Chimera launched in ElevenCreative on 2026-10-21
- Pairs Eleven v4 (voice emotion) with Seedance 2.5 (face animation)
- Workflow: create or upload a character, write the line, pick or design a voice; direct with [whispers], [laughs], [yells]
- Works with humans, cartoons/anime and pets; "Upload Audio" replaces generated speech
- Location: ElevenCreative homepage > More Tools > Templates > Chimera
```

## Schema / vocabulary additions

None.

## Open questions

- Seedance 2.5 is named but undescribed. Keep it as a note on the Seedance 2.0 page (assumed), or create `tools/seedance-2-5.md` now and archive the 2.0 page to `wiki/history/tools/`?
	- Create the 2.5
