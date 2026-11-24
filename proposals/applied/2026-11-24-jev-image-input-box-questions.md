---
type: proposal
source: raw/articles/2026-11-24-docstypesafeai-images.md
sources:
  - raw/articles/2026-11-24-docstypesafeai-images.md
  - raw/articles/2026-11-23-docstypesafeai-concepts-use-case-map.md
  - raw/articles/2026-11-24-docstypesafeai-primitives-box.md
status: pending
created: 2026-11-24
---

# Proposal: Jev reads images (experimental) and gains a Box question type

## Summary

### In short
Jev is no longer a text-only decision model: TypeSafe's docs now let Jev 1.13 and 1.14 take images anywhere text can go, and add a Box question that returns where something is in a picture, though only as an opt-in experiment TypeSafe says is not production-ready. The proposal corrects the "no image input" caveat on the **Jev** page and the "text only" note on **State of Models**, and adds two source pages. The reason to hesitate: the docs carry no release date, so the page date is the day they were read.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
TypeSafe makes Jev, an API model that answers typed questions (a yes/no probability, a pick from options, a score) instead of writing text. Its documentation, read on 23 and 24 November 2026, now has an Images page. An image can sit in the request's state, inside a question's instructions, or in the criteria a question is judged against, and every question type accepts it. A new Box question type returns the four edges of a rectangle around a named target, as fractions of the image's width and height, with a confidence score. Both Jev 1.13 and 1.14 accept images; Box needs 1.14.

The docs are explicit about the limits. Images and Box are labelled "Dreamer-ready": fine for prototypes, not yet up to TypeSafe's production standard, and the request format, answers and limits may change between releases. They are off by default and need a `TypeSafe-Danger-Zone-Images: true` header on each request. A Box question has no "not found" answer, so the docs advise pairing it with a yes/no question about whether the target is there at all.

The use-case map turns this into worked examples: reading a scanned vaccination record (locate each vaccine, read the year of each dose, flag doubtful readings for a nurse), checking OCR values on invoice photos against crops of their boxes, and logging bird species from feeder-camera frames. "Video" here means sending individual frames as images. The same page says a Jev workflow on its security-incidents evaluation takes 0.3 seconds per case, against 3.4 to 66 seconds for frontier models.

### What changes
The wiki currently says Jev handles text and structured data only, and lists image input as something rivals (Cloudflare's Clef, OpenAI's Decisions API, Liquid d1) have and Jev lacks.

- **Jev** describes experimental image input and the Box question type in its opening paragraph and Current status, replaces the "no image input" caveat with one about the feature's experimental status, and gains one Recent-changes entry. Page date moves to 24 November.
- **State of Models** swaps "text only" on the Jev line for "experimental image input and Box questions"; the line's date moves to 24 November. No Recent-changes entry, since no leader changes.
- **Index** refreshes the Jev line and its date.
- Two new source pages: `sources/articles/typesafe-docs-images-2026-11-24.md` and `sources/articles/typesafe-docs-use-case-map-2026-11-23.md`.

### What to weigh
The docs are undated, so nothing says when image support shipped; it could predate the wiki's October pages. The page date uses the day the docs were read (24 November), and the Recent-changes entry says "documented by" rather than "launched". The Box reference page was read as well and only backs claims the Images page also makes, so it gets no source page of its own and is listed only in this proposal's sources.

## Intended changes

- [ ] **Update** `wiki/models/jev.md` — opening paragraph, Current status bullet 1, Weaknesses bullet 3, `as_of` and Current-status date to 2026-11-24; adds one Recent-changes entry dated 2026-11-24 (no spill, list at 3); appends two source ids and two Sources links

- [ ] **Update** `wiki/state-of/models.md` — Jev line under Decision models
    > **Before:** `- [Jev](../models/jev.md) — TypeSafe; the reference model the category clones; $0.042/M input, output free; text only; second on Artificial Analysis's Decision Index (Jev 1.14: 57) *(as of 2026-10-17)*`
    > **After:** `- [Jev](../models/jev.md) — TypeSafe; the reference model the category clones; $0.042/M input, output free; experimental image input and Box (locate-in-image) questions; second on Artificial Analysis's Decision Index (Jev 1.14: 57) *(as of 2026-11-24)*`

- [ ] **Update** `wiki/index.md` — Jev line

- [ ] **Create** `wiki/sources/articles/typesafe-docs-images-2026-11-24.md` — source summary

- [ ] **Create** `wiki/sources/articles/typesafe-docs-use-case-map-2026-11-23.md` — source summary

## Page drafts

### wiki/models/jev.md (updated)

Frontmatter changes:

```
as_of: 2026-11-24
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17, tamaratran-fast-jev-compaction, typesafe-docs-images-2026-11-24, typesafe-docs-use-case-map-2026-11-23]
```

Opening paragraph (replaces the current one):

```
TypeSafe's API-only decision model, released 2026-09-15 and marketed as a "System One" model. Jev answers questions about text, structured input and (experimentally) images instead of generating text. A Noulli question returns the probability that a statement is true, a Choice question returns probabilities over a set of options, a Score question places the input on a scale, and a Box question returns where something is in an image. TypeSafe CEO Diogo Almeida, a co-author of InstructGPT, maps the first three to an if statement, a switch statement and a sort. It is the reference point for the [decision models](../concepts/decision-models.md) category.
```

Current status heading and first bullet (the other bullets are unchanged):

```
## Current status (as of 2026-11-24)

- Price: $0.042 per 1M input tokens, output free; 32K context per Cloudflare's comparison. Images are an opt-in experiment ("Dreamer-ready", behind a `TypeSafe-Danger-Zone-Images: true` header): Jev 1.13 and 1.14 accept them in the state, instructions or criteria of any question, and Jev 1.14 adds Box questions that return a bounding box with a confidence. TypeSafe's examples read scanned records, check OCR fields on invoice photos and label video frames one at a time.
```

Weaknesses / caveats, third bullet (replaces "No image input; Clef, OpenAI's Decisions API and Liquid d1 accept images."):

```
- Image input is not production-ready by TypeSafe's own label: the request format and limits may change between releases, and a Box question always returns a box, even when the target is absent, so it needs a companion yes/no question.
```

Recent changes (adds one entry at the top; the two existing entries stay):

```
## Recent changes

- [2026-11-24] TypeSafe's docs now document experimental image input on Jev 1.13 and 1.14 and a new Box question type (Jev 1.14) that locates a target in an image; the "no image input" caveat is replaced.
- [2026-10-26] Used as the keep-or-drop engine in [fast-jev-compaction](../tools/fast-jev-compaction.md), a Claude Code plugin that prunes stale tool calls and results instead of summarizing context; it calls `jev-latest` and splits requests to stay under Jev's 32K request limit.
- [2026-10-17] Page created: launch (2026-09-15), pricing, independent results, and its fall to second on Artificial Analysis's Decision Index.
```

Sources (appends two links):

```
- [TypeSafe docs — Images](../sources/articles/typesafe-docs-images-2026-11-24.md)
- [TypeSafe docs — Use cases](../sources/articles/typesafe-docs-use-case-map-2026-11-23.md)
```

### wiki/state-of/models.md (updated)

```
- [Jev](../models/jev.md) — TypeSafe; the reference model the category clones; $0.042/M input, output free; experimental image input and Box (locate-in-image) questions; second on Artificial Analysis's Decision Index (Jev 1.14: 57) *(as of 2026-11-24)*
```

### wiki/index.md (updated)

```
- [models/jev](models/jev.md) — TypeSafe's API-only decision model: calibrated yes/no, choice and score answers instead of text; $0.042/M input, output free; experimental image input and Box questions; second on Artificial Analysis's Decision Index; used for context compaction by fast-jev-compaction *(as_of: 2026-11-24)*
```

### wiki/sources/articles/typesafe-docs-images-2026-11-24.md (new)

```
---
title: TypeSafe docs — Images
type: source
source_type: article
source_file: raw/articles/2026-11-24-docstypesafeai-images.md
url: https://docs.typesafe.ai/images
ingested: 2026-11-24
domains: [models]
---

# TypeSafe docs — Images

TypeSafe's documentation page on sending images to Jev. An image can go anywhere text can in a System One request (the state, a question's instructions, its criteria), and every question type accepts it. Images are referenced by strings that point into a top-level `assets` map; the SDKs create these references automatically. The feature is labelled "Dreamer-ready": meant for prototypes, not yet production-ready, with format, answers and limits subject to change. The companion Box reference page (`raw/articles/2026-11-24-docstypesafeai-primitives-box.md`) describes the Box answer format. The page is undated; read 2026-11-24.

## Influenced pages
- [Jev](../../models/jev.md) — image input and Box questions; "no image input" caveat replaced
- [State of Models](../../state-of/models.md) — Jev line no longer says "text only"

## Key claims extracted
- Jev 1.13 and Jev 1.14 accept images; Box questions need Jev 1.14
- Images and Box questions are off by default; each request needs the `TypeSafe-Danger-Zone-Images: true` header
- A Box answer gives top, bottom, left and right edges as fractions of the image size, plus a confidence from 0 to 1
- A Box question has no "not found" answer; pair it with a Noul asking whether the target is present
- Each reference to an image adds another copy to what the model reads and counts toward the request limit
```

### wiki/sources/articles/typesafe-docs-use-case-map-2026-11-23.md (new)

```
---
title: TypeSafe docs — Use cases
type: source
source_type: article
source_file: raw/articles/2026-11-23-docstypesafeai-concepts-use-case-map.md
url: https://docs.typesafe.ai/concepts/use-case-map
ingested: 2026-11-24
domains: [models]
---

# TypeSafe docs — Use cases

TypeSafe's map of what to build with Jev, in five categories: business process automation, real-time apps, search and labeling at scale, agents and verification, and images and video. Each row names what Jev judges and what the application code does with the answer. The images-and-video category covers reading a scanned vaccination record and logging bird species from feeder-camera frames; an OCR bounding-box check on invoice photos sits under business process automation. The page is undated; read 2026-11-23.

## Influenced pages
- [Jev](../../models/jev.md) — image and video-frame use cases

## Key claims extracted
- "Images and video" is a use-case category: find, read and check what is in scans, photos and video frames
- Examples: scanned vaccination record (vaccine located, dose year read or marked unreadable, out-of-date doses flagged for a nurse); OCR values checked against crops of their bounding boxes; feeder-camera frames labelled by species and turned into a visit log
- On TypeSafe's security-incidents evaluation, a Jev workflow takes 0.3 s per case against 3.4–66 s for frontier models
- Across TypeSafe's four evaluations, every model was more accurate as a structured workflow than with the same rules in one prompt
```

## Schema / vocabulary additions

None.

## Open questions

None.
