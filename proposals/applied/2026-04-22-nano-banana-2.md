---
type: proposal
source: raw/tweets/2026-04-22-sundarpichai-2027057726170509724.md
status: pending
created: 2026-04-22
---

# Proposal: Google Nano Banana 2 — image generation model stub

## Summary

Sundar Pichai announced "Nano Banana 2," Google's latest image generation model. It uses Gemini's world understanding plus real-time web search imagery to reflect real-world conditions in generated images. Thin source (tweet only), but warrants a stub since we have a `models/gpt-image-2` page and this is a direct competitor in the image-generation subcategory.

## Intended changes

- [x] **Create** `wiki/models/nano-banana-2.md` — new model stub
    > See draft below

- [x] **Update** `wiki/state-of/models.md` — add to `Image generation` subcategory
    > **Add after existing gpt-image-2 line:**
    > ```
    > - [[models/nano-banana-2]] — Google; powered by Gemini world understanding + real-time web search imagery; can reflect real-world conditions (current events, weather) in generated images *(as of 2026-04-22)*
    > ```
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added [[models/nano-banana-2]] to `Image generation` subcategory; Google enters the arena with Gemini+web-search-grounded image generation
    > ```

- [x] **Create** `wiki/sources/tweets/nano-banana-2.md` — source summary
    > See draft below

## Page drafts

### wiki/models/nano-banana-2.md (new)

```md
---
title: Nano Banana 2
type: model
domains: [models, creative]
subcategory: image-generation-model
tags: [google, closed-source]
as_of: 2026-04-22
sources: [nano-banana-2-tweet]
---

# Nano Banana 2

Google's image generation model. Uses Gemini's understanding of the world plus real-time information and images from web search to generate images that can reflect current real-world conditions.

## Current status (as of 2026-04-22)

- Announced by Sundar Pichai
- Powered by Gemini world understanding + real-time web search imagery
- Differentiator: can ground generated images in current real-world information (weather, events, locations)
- Demo: "Window Seat" — generates images reflecting real current conditions

## Caveats

- Source is a single CEO tweet; no benchmarks, pricing, or access details available
- Competitive position vs. gpt-image-2 unknown without independent testing

## Sources

- [[sources/tweets/nano-banana-2]]
```

### wiki/sources/tweets/nano-banana-2.md (new)

```md
---
title: Sundar Pichai — Nano Banana 2 image model announcement
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-sundarpichai-2027057726170509724.md
url: https://x.com/sundarpichai/status/2027057726170509724
published: 2026-04-22
ingested: 2026-04-22
domains: [models, creative]
---

# Sundar Pichai — Nano Banana 2

Brief CEO announcement tweet for Google's Nano Banana 2 image model. Gemini world understanding + real-time web search grounding for image generation. "Window Seat" demo.

## Influenced pages

- [[models/nano-banana-2]] — new stub created
- [[state-of/models]] — added to Image generation subcategory

## Key claims extracted

- Gemini world understanding + real-time web search imagery
- Can reflect real-world conditions in high-fidelity
- Demo: "Window Seat"
```
