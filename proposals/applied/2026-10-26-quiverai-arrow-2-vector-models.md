---
type: proposal
source: raw/articles/2026-10-26-quiverai-blog-introducing-arrow-2-0.md
sources:
  - raw/articles/2026-10-26-quiverai-blog-introducing-arrow-2-0.md
  - raw/tweets/2026-10-26-quiverai-2100295136261349802.md
status: pending
created: 2026-10-26
---

# Proposal: QuiverAI Arrow 2 and Arrow 2 Telos

## Summary

### In short
Generative image models are splitting by output format: QuiverAI's Arrow 2 produces editable SVG vector graphics written as code, not pixels, so the result can be scaled, edited and animated in ordinary design tools. Released 16 September 2026, it comes in a fast tier and a Telos tier with frontier-model refinement, plus a new app and developer API. The proposal creates an Arrow 2 model page, adds it to State of Creative, and adds two source pages. Reason to hesitate: the image-generation subcategory is a loose fit for a vector model.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
QuiverAI, which describes itself as "frontier AI for design", announced Arrow 2 on 16 September 2026 in an X thread (2.3M views) and a launch post on its blog. Its premise is that vectors should be "intentionally crafted through code": instead of painting pixels, the model writes SVG, the format designers use for logos, icons and diagrams, so every output can be opened, adjusted and reused.

The post claims faster generation and better taste. Geometry is cleaner, with fewer and more precise control points and fewer messy overlapping paths, and layouts respect spacing, padding and alignment without exhaustive prompting. It shows four kinds of work: new illustrations that keep a reference's palette and shape language, anatomical diagrams with the target muscles highlighted, fashion line drawings that keep seams and closures consistent across variations, and vectorization of a hand-drawn sketch into a clean editable SVG. It also adds micro-animations, which animate the shapes and groups already in an SVG and suit logo reveals, loading states and animated icons rather than illustrative motion. No benchmark numbers are given.

Arrow 2 Telos is the second tier, which QuiverAI says combines Arrow's speed with "the refinement capabilities of frontier models" for harder briefs; plain Arrow 2 is the choice when speed and cost per asset matter. The thread adds a rebuilt app that puts conversational generation and direct canvas editing in one workspace, and a new API platform at platform.quiver.ai for credentials, usage and billing.

### What changes
The wiki has no page for QuiverAI or Arrow, and its image-generation leaders are all raster models.

- New page `models/arrow-2.md` covering both tiers, the four task types, animation, and availability.
- **State of Creative** gains an Arrow 2 line under AI image generation and a Recent-changes entry. The list is at its cap, so its oldest entry (Figma's in-canvas agent and Runway Aleph 2.0, 22 May) moves to history. Page date moves to 16 September.
- Two new source pages, one for the blog post and one for the announcement thread.

### What to weigh
The `image-generation-model` subcategory is defined around text-to-image and image editing, and Arrow's output is code, not pixels; it is used here as the closest existing fit rather than proposing a vector-graphics subcategory from one launch. The blog post carries no date, so it takes the thread's 16 September date, since the thread links to it as the same launch.

## Intended changes

- [ ] **Create** `wiki/models/arrow-2.md` — new model page, subcategory `image-generation-model`
    > See draft below

- [ ] **Update** `wiki/state-of/creative.md` — add one leader line at the end of `### AI image generation`; `as_of` moves to 2026-09-16; adds one Recent-changes entry dated 2026-09-16 (live list has 10, at the cap); append two source ids
    > See draft below

- [ ] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — the oldest Recent-changes entry (expected: [2026-05-22] Figma in-canvas agent / Runway Aleph 2.0) moves to history
    > See draft below

- [ ] **Create** `wiki/sources/articles/quiverai-arrow-2-launch-2026-09-16.md` — source summary for the blog post

- [ ] **Create** `wiki/sources/tweets/quiverai-arrow-2-announcement-2026-09-16.md` — source summary for the X thread

## Page drafts

### wiki/models/arrow-2.md (new)

```
---
title: Arrow 2
type: model
domains: [models, creative]
subcategory: image-generation-model
tags: []
as_of: 2026-09-16
sources: [quiverai-arrow-2-launch-2026-09-16, quiverai-arrow-2-announcement-2026-09-16]
---

# Arrow 2

QuiverAI's model family for generating editable vector graphics. Instead of producing pixels, Arrow writes SVG ("vectors should be intentionally crafted through code"), so every output can be scaled, edited, and reused in ordinary design tools. Arrow 2 was released on 16 September 2026 together with a higher-end tier, Arrow 2 Telos.

## Current status (as of 2026-09-16)

- **Two tiers:** Arrow 2 when speed and cost per asset come first; Arrow 2 Telos, which QuiverAI says combines Arrow's speed with "the refinement capabilities of frontier models", for harder briefs, complex styles, and demanding compositions.
- **Tasks shown at launch:** illustration variations that keep a reference's palette and shape language; illustrative and anatomical diagrams with selective emphasis; technical line drawings that stay consistent across variations; vectorization of raster images and sketches into editable SVGs.
- **Micro-animations:** animates the shapes and groups already present in an SVG into web-ready motion (logo reveals, loading states, animated icons), suited to flat, structured artwork.
- **Claimed upgrades over the previous Arrow:** faster generation; cleaner geometry with fewer, more precise control points and fewer overlapping paths; composition that respects spacing, padding, and alignment without heavy prompting. No benchmark figures were published.
- **Availability:** all users, in a rebuilt app that combines conversational generation with direct canvas editing, and through a new developer API platform (credentials, usage, billing) at platform.quiver.ai.

## Recent changes

- [2026-09-16] Arrow 2 and Arrow 2 Telos released, with a rebuilt app workspace and a developer API platform.

## Related

- [State of Creative](../state-of/creative.md) — listed under AI image generation
- [GPT-Image-2](gpt-image-2.md) — the raster image-generation leader, for contrast with vector output

## Sources

- [QuiverAI — Introducing Arrow 2 and Arrow 2 Telos](../sources/articles/quiverai-arrow-2-launch-2026-09-16.md)
- [QuiverAI on X — Introducing Arrow 2](../sources/tweets/quiverai-arrow-2-announcement-2026-09-16.md)
```

### wiki/state-of/creative.md (updated)

Frontmatter: `as_of: 2026-09-16`; append two ids (`quiverai-arrow-2-launch-2026-09-16`, `quiverai-arrow-2-announcement-2026-09-16`) to the live `sources:` list.

`### AI image generation` — append after the Krea 2 Raw / Turbo line:

```
- [Arrow 2](../models/arrow-2.md) — QuiverAI; writes editable SVG vector graphics rather than raster images: illustrations, diagrams, vectorization, and micro-animations; the Arrow 2 Telos tier adds frontier-model refinement for harder briefs *(as of 2026-09-16)*
```

`## Recent changes` — insert one entry above the 2026-09-01 entry, then remove the oldest entry (see Spill):

```
- [2026-09-16] QuiverAI released Arrow 2 and Arrow 2 Telos, vector-graphics models that output editable SVGs, with a rebuilt app and a developer API platform.
```

### wiki/history/state-of/creative.md (updated — spill)

Append at the end of the file:

```

## Archived from current page on 2026-10-26

- [2026-05-22] Figma released a native in-canvas design agent (Gemini Flash + Claude Sonnet + Figma fine-tuned models; Every hands-on: good for first drafts, weak on detail fidelity) and Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video (AINews recap); both newsletter-sourced, no primary announcement fetched, no dedicated pages yet.
```

### wiki/sources/articles/quiverai-arrow-2-launch-2026-09-16.md (new)

```
---
title: QuiverAI — Introducing Arrow 2 and Arrow 2 Telos
type: source
source_type: article
source_file: raw/articles/2026-10-26-quiverai-blog-introducing-arrow-2-0.md
url: https://quiver.ai/blog/introducing-arrow-2-0
published: 2026-09-16
ingested: 2026-10-26
domains: [creative, models]
---

# QuiverAI — Introducing Arrow 2 and Arrow 2 Telos

QuiverAI's launch post for Arrow 2, its vector-graphics model, and the higher-end Arrow 2 Telos. Claims faster generation, cleaner SVG geometry, and better composition; shows illustration variations, illustrative diagrams, technical line drawings, vectorization, and micro-animations of existing SVG shapes. Positions Arrow 2 for speed and cost per asset and Telos for harder briefs. The post is undated; its date is taken from the same-day announcement thread that links to it.

## Influenced pages
- [Arrow 2](../../models/arrow-2.md) — new model page
- [State of Creative](../../state-of/creative.md) — new line under AI image generation

## Key claims extracted
- Arrow 2 is QuiverAI's "most significant update yet": faster generation and better visual quality for animation, vectorization, and asset creation
- Philosophy: vectors should be intentionally crafted through code
- Cleaner geometry: fewer, more precise control points; fewer overlapping paths
- Stronger composition: respects spacing, padding, and alignment without exhaustive prompt engineering
- Use cases: reference-consistent illustration variations, illustrative diagrams, technical drawings, raster-to-SVG vectorization
- Micro-animations animate the shapes and groups already present in an SVG; suited to interface motion and flat, structured artwork
- Arrow 2 Telos combines Arrow's speed with the refinement capabilities of frontier models; choose Arrow 2 for speed and cost per asset, Telos for harder briefs
- Available now for all users
```

### wiki/sources/tweets/quiverai-arrow-2-announcement-2026-09-16.md (new)

```
---
title: QuiverAI on X — Introducing Arrow 2
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-quiverai-2100295136261349802.md
url: https://x.com/QuiverAI/status/2100295136261349802
published: 2026-09-16
ingested: 2026-10-26
domains: [creative, models]
---

# QuiverAI on X — Introducing Arrow 2

QuiverAI's announcement thread (2.3M views) for Arrow 2, "our latest and most advanced models for generating precise, editable vector graphics", available in the app and API. Follow-up posts introduce Arrow 2 Telos, a rebuilt app combining generation and canvas editing in one workspace, and a new developer API platform, and link the launch blog post.

## Influenced pages
- [Arrow 2](../../models/arrow-2.md) — release date, app and API availability, Telos tier
- [State of Creative](../../state-of/creative.md) — new line under AI image generation

## Key claims extracted
- Arrow 2 released 2026-09-16: higher quality, faster outputs, available in app and API
- Arrow 2 Telos combines Arrow's infrastructure, taste, and speed with the depth of frontier models
- New app: describe, iterate through conversation, and make precise adjustments on the canvas; every creation is an editable SVG usable outside the app
- New API platform (platform.quiver.ai) for credentials, usage, and billing
```

## Schema / vocabulary additions

None.

## Open questions

- Should vector-graphics models get their own subcategory (for example `vector-graphics-model`) once a second one appears, or stay under `image-generation-model`?
	- yes, subcategory
