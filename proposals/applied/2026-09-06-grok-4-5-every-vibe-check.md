---
type: proposal
source: raw/newsletters/2026-07-12-from-doing-to-tending.md
status: pending
created: 2026-09-06
---

# Proposal: Every's mini vibe-check on Grok 4.5

## Summary

### The source

A year after Every panned Grok 4 as strong on benchmarks but not useful enough to use daily, the team ran a mini vibe-check on Grok 4.5 and reached a different verdict: "fast, cheap, and finally useful." Their internal evals put it roughly at Opus 4.8 level — one tester's benchmark actually ranked it slightly above Opus 4.8, since Grok completed assignments end-to-end that Opus abandoned partway through. A second tester, running it through Every's own compound-engineering workflow, placed it more conservatively in the Opus-4.5-to-4.6 range: "not state of the art, but pretty good for a lot of things, and very fast." Every's own read of xAI's efficiency claims (~80 tok/s, roughly 2x the token efficiency of leading models) checks out against pricing — Grok 4.5's $2/$6 per million tokens undercuts both Opus 4.8 ($5/$25) and GPT-5.6 Sol ($5/$30). In hands-on tests it did well at vibe-coded UI work and PowerPoint-style slide generation (rated near Opus 4.6/4.7), though the team still prefers GPT-5.6 Sol for writing.

### What changes

`models/grok-4-5.md` currently sources its benchmark picture entirely from Artificial Analysis via AINews. This adds independent, hands-on corroboration from a different evaluator:

- **Grok 4.5** gains one new bullet under Current status citing Every's internal placement (Opus-4.5-to-4.8 range depending on the tester) and one Recent-changes entry. Page moves to 12 July.
- One new source page.

### What to weigh

This is Every's own non-public internal benchmark, not an independently reproducible one — the draft attributes it as such throughout, consistent with how the page already treats its existing (also non-independent) AINews/Artificial-Analysis figures.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/grok-4-5.md` — add one Current-status bullet citing Every's mini vibe-check placement; bump `as_of` to 2026-07-12; add a Recent-changes entry; add the new source
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-grok-4-5-mini-vibe-check-2026-07.md` — source summary

## Page drafts

### wiki/models/grok-4-5.md (updated)

Frontmatter:

```yaml
as_of: 2026-07-12
sources: [cursor-blog-grok-4-5-launch-2026-07, ainews-spacexai-grok-45-2026-07-09, every-grok-4-5-mini-vibe-check-2026-07]
```

`## Current status` — add a bullet after the existing benchmark bullet:

```md
- Every's mini vibe-check (internal, non-public evals) placed Grok 4.5 roughly at Claude Opus 4.8 level — one tester ranked it slightly above Opus 4.8 since it completed assignments end-to-end that Opus abandoned partway, while another placed it in the Opus-4.5-to-4.6 range on Every's compound-engineering workflow ("not state of the art, but pretty good for a lot of things, and very fast"); rated near Opus 4.6/4.7 on PowerPoint-style slide generation; Every still prefers GPT-5.6 Sol for writing
```

Updated `## Recent changes` (full section):

```md
## Recent changes

- [2026-07-12] Every's mini vibe-check rates it roughly Opus-4.8-level on internal evals; strong at vibe-coded UI work and slide generation, cheaper than both Opus 4.8 and GPT-5.6 Sol.
- [2026-07-08] Launched: 1.5T MoE co-trained with Cursor, $2/$6 pricing, available across all Cursor surfaces plus Grok Build and API
```

Updated `## Sources` (full section):

```md
## Sources

- [Cursor — Introducing Grok 4.5](../sources/articles/cursor-blog-grok-4-5-launch-2026-07.md)
- [AINews — SpaceXAI launches Grok 4.5](../sources/newsletters/ainews-spacexai-grok-45-2026-07-09.md)
- [Every — mini vibe-check on Grok 4.5](../sources/newsletters/every-grok-4-5-mini-vibe-check-2026-07.md)
```

### wiki/sources/newsletters/every-grok-4-5-mini-vibe-check-2026-07.md (new)

```md
---
title: "Every — From Doing to Tending (Grok 4.5 mini vibe-check)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-12-from-doing-to-tending.md
url: https://every.to/context-window/from-doing-to-tending
published: 2026-07-12
ingested: 2026-09-06
domains: [models]
---

# Every — From Doing to Tending (Grok 4.5 mini vibe-check)

Every's newsletter, whose main content is unrelated (AI scribes and clinical cognitive offloading), but which opens with a mini vibe-check of Grok 4.5 — the first output of the SpaceX/Cursor co-training tie-up. Only the Grok 4.5 portion is used here.

## Influenced pages
- [Grok 4.5](../../models/grok-4-5.md) — added Every's internal benchmark placement

## Key claims extracted
- Every's internal evals place Grok 4.5 roughly at Claude Opus 4.8 level
- Mike Taylor's benchmark ranked it slightly above Opus 4.8: Grok completed a full assignment Opus stopped partway through
- Kieran Klaassen, running it through Every's `/LFG` compound-engineering workflow, placed it in the Opus-4.5-to-4.6 range: "not state of the art, but pretty good for a lot of things, and very fast"
- xAI claims ~80 tok/s and roughly 2x the token efficiency of leading models; pricing $2/$6 per million input/output tokens, versus Opus 4.8's $5/$25 and GPT-5.6 Sol's $5/$30
- Rated well on vibe-coded UI generation (voice-interview form, neighborhood map app) and PowerPoint-style slides (rated near Opus 4.6/4.7); Every still prefers Sol for writing; Grok avoids some of Claude's writing tics but produces short, sharp sentences
