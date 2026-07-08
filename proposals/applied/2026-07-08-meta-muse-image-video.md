---
type: proposal
source: raw/newsletters/2026-07-08-meta-debuts-muse-image-and-video.md
status: pending
created: 2026-07-08
---

# Proposal: Meta Muse Image and Muse Video

## Summary

Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp, and previewed Muse Video. AINews frames the release as notable because the generation loop includes planning, web search, tool use, code execution, and self-refinement before rendering.

## Intended changes

- [x] **Update** `wiki/models/muse-spark.md` — add Muse Image/Video section.
- [x] **Update** `wiki/state-of/creative.md` — add Muse Image/Video under image/video generation.
- [x] **Create** `wiki/sources/newsletters/meta-muse-image-video-2026-07.md` — source summary.

## Page drafts

### wiki/models/muse-spark.md (updated sections)

```md
---
title: Muse Spark
type: model
domains: [models, creative]
subcategory: frontier-model
tags: [closed-source, agentic, meta]
as_of: 2026-07-08
sources: [muse-spark, open-creative-workflows-2026-06, meta-muse-image-video-2026-07]
---

## Muse Image / Muse Video (as of 2026-07-08)

Meta Superintelligence Labs launched Muse Image inside Meta AI, Instagram Stories, and WhatsApp, with Facebook planned, and previewed Muse Video. Superhuman reports Muse Image reached #2 on Arena's text-to-image leaderboard behind GPT-Image-2.

The more important architecture signal is agentic generation: AINews describes Muse Image/Video as using planning, web search, tool use, code execution, and self-refinement before rendering, with Meta saying quality improves with scaled test-time compute.

## Recent changes

- [2026-07-08] Muse Image launches in Meta AI, Instagram Stories, and WhatsApp; Muse Video previewed; AINews describes an agentic planning/tool-use/self-refinement generation loop.
- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in; secondary coverage only.
- [2026-04-10] Page created from Meta's Muse Spark introduction post
```

### wiki/state-of/creative.md (updated sections)

```md
### AI video generation

- **Muse Video** — Meta Superintelligence Labs preview; paired with Muse Image and described in AINews as using agentic planning, tool use, code execution, and self-refinement before rendering *(as of 2026-07-08)*

### AI image generation

- [Muse Image](../models/muse-spark.md) — Meta; launched inside Meta AI, Instagram Stories, and WhatsApp; Superhuman reports #2 on Arena text-to-image behind GPT-Image-2; uses agentic planning/self-refinement loop per AINews *(as of 2026-07-08)*

## Recent changes

- [2026-07-08] Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp and previewed Muse Video; AINews describes an agentic generation loop with planning, tool use, code execution, and self-refinement.
- [2026-06-29] Every's PowerPoint analysis adds a caution for slide agents: polished enterprise decks require supporting skills, scripts, references, and review loops.
```

### wiki/sources/newsletters/meta-muse-image-video-2026-07.md (new)

```md
---
title: Meta Muse Image and Muse Video
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-08-meta-debuts-muse-image-and-video.md
url: https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/
published: 2026-07-08
ingested: 2026-07-08
domains: [creative, models]
tags: [meta]
---

# Meta Muse Image and Muse Video

Superhuman reports that Meta launched Muse Image inside Meta AI, Instagram Stories, and WhatsApp, with Facebook planned, and previewed Muse Video. AINews adds that the systems use an agentic generation loop with planning, web search, tool use, code execution, and self-refinement before rendering.

## Influenced pages

- [Muse Spark](../../models/muse-spark.md) — adds Muse Image/Video product section.
- [State of Creative](../../state-of/creative.md) — adds Muse entries under image/video generation.

## Key claims extracted

- Muse Image is rolling out inside Meta AI, Instagram Stories, and WhatsApp.
- Superhuman reports Muse Image ranked #2 on Arena text-to-image behind GPT-Image-2.
- Meta previewed Muse Video.
- AINews describes an agentic generation process involving planning, web search, tools, code execution, and self-refinement.
```

## Schema / vocabulary additions

None.
