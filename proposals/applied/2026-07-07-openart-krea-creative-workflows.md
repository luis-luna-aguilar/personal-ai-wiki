---
type: proposal
sources:
  - raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md
  - raw/newsletters/2026-06-24-anthropic-drops-claude-tag.md
  - raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md
status: pending
created: 2026-07-07
---

# Proposal: Open creative workflows and vibe directing

## Summary

The creative signal is that generative media workflows are moving in two directions at once: more editable, conversational products like OpenArt Director, and more open/fine-tunable ecosystems like Krea 2 Raw/Turbo. The proposed update should stay lightweight because the source cluster is newsletter-heavy and primary pages were not fetched during triage.

## Intended changes

- [x] **Update** `wiki/state-of/creative.md` — add lightweight OpenArt Director and Krea 2 notes.
    > Under `AI video generation`, add: `OpenArt Director — conversational "vibe directing" product for generating/editing clips up to five minutes with consistent characters, voiceover, music, and captions; secondary coverage only *(as of 2026-06-24)*`.
    >
    > Under `AI image generation`, add: `Krea 2 Raw/Turbo — open-weight image models; Raw is an undistilled fine-tuning checkpoint, Turbo is distilled for fast inference; day-0 diffusers/LoRA ecosystem support reported; secondary coverage only *(as of 2026-06-24)*`.

- [x] **Update** `models/muse-spark.md` — optional lightweight recent-change entry for Meta smart glasses only if user wants consumer-device surface tracked there.
    > `- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in; secondary coverage only.`

- [x] **Create** `wiki/sources/newsletters/open-creative-workflows-2026-06.md` — source summary.
    > See draft below.

## Page drafts

### wiki/state-of/creative.md (updated snippets)

```markdown
---
as_of: 2026-06-24
sources: [..., open-creative-workflows-2026-06]
---

### AI video generation

- **OpenArt Director** — conversational "vibe directing" product for generating and editing clips up to five minutes with consistent characters, voiceover, music, and captions; current evidence is newsletter coverage pending primary-source fetch *(as of 2026-06-24)*

### AI image generation

- **Krea 2 Raw / Turbo** — open-weight image model pair; Raw is positioned as an undistilled fine-tuning checkpoint, while Turbo is a distilled fast-inference checkpoint with reported day-0 diffusers, LoRA, and training-tool support *(as of 2026-06-24)*

## Recent changes

- [2026-06-24] OpenArt Director and Krea 2 Raw/Turbo signal creative workflows splitting between conversational editing products and open fine-tuning ecosystems.
```

### wiki/models/muse-spark.md (optional updated snippet)

```markdown
---
as_of: 2026-06-24
sources: [..., open-creative-workflows-2026-06]
---

## Recent changes

- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in; secondary coverage only.
```

### wiki/sources/newsletters/open-creative-workflows-2026-06.md (new)

```markdown
---
title: Open creative workflows and vibe directing
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md
url: https://openart.ai/director
published: 2026-06-24
ingested: 2026-07-07
domains: [creative]
---

# Open creative workflows and vibe directing

Superhuman reports OpenArt launched Director, a conversational video product for generating and editing clips up to five minutes with consistent characters, voiceover, music, and captions. The same source cluster reports Krea 2 Raw and Krea 2 Turbo open weights, with Raw positioned for fine-tuning and Turbo for fast inference, plus day-0 ecosystem support for diffusers and LoRA workflows.

## Influenced pages

- [State of Creative](../../state-of/creative.md) — adds lightweight entries for OpenArt Director and Krea 2 Raw/Turbo.
- [Muse Spark](../../models/muse-spark.md) — optional secondary note that Meta Glasses reportedly ship with Muse Spark built in.

## Key claims extracted

- OpenArt Director is described as a conversational "vibe directing" surface for generating and editing short-form videos.
- Reported Director features include consistent characters, voiceover, music, and captions.
- Krea 2 Raw is described as an undistilled open-weight checkpoint intended for custom styles and LoRAs.
- Krea 2 Turbo is described as a fast distilled inference checkpoint.
- AINews reports day-0 diffusers, LoRA, and training-tool support around the Krea release.
```

## Schema / vocabulary additions

None.
