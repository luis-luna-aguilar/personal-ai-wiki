---
type: proposal
source: raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
status: pending
created: 2026-11-24
---

# Proposal: Bria Fibo 2.0 and Krea 3 Ultra image editing

## Summary

### In short
Image editing now has a credible open-weight option, Bria's 8B Fibo 2.0, which Artificial Analysis rates the best open-weight editing model, while Krea 3 Ultra sits in the top tier of closed editing models but with arena ranks that swing from #4 to #8. The proposal adds both as unlinked lines under AI image generation on **State of Creative**, plus one source page. Reason to hesitate: the facts come from an AINews recap, not from Bria's, Krea's or Artificial Analysis's own pages, and Fibo's weights are non-commercial, which limits its practical value.

[[#Open questions|Open questions: 2 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
AINews, the daily AI-news digest from Latent Space, ran a short "speech and image releases" block in its 21 October 2026 edition. Two items concern image editing, meaning changing an existing picture from an instruction rather than generating one from scratch.

The first is Fibo 2.0 from Bria, an Israeli image-model company known for training on licensed data. Fibo 2.0 is an 8-billion-parameter family whose weights anyone can download: a Dev model for text-to-image and a distilled, faster Edit Turbo model for editing. Artificial Analysis, an independent benchmarking firm, ranks it the leading open-weight editing model and statistically tied with Alibaba's Qwen-Image-2.1 for text-to-image. The catch, which AINews stresses, is that the weights are licensed for non-commercial use only; commercial deployment needs a separate agreement with Bria, and licensed training data does not mean free commercial rights. Bria's own API costs $32 per 1,000 images, and the model is already in Hugging Face Diffusers and on fal.

The second is Krea 3 Ultra, a closed model. AINews warns its rank depends on the leaderboard: Artificial Analysis places it #5, earlier posts said #4, and LMArena has it #4 for multi-image editing but #8 for single-image editing. Ultra outputs 2K images only; a 2K edit with one reference image costs $0.27.

### What changes
State of Creative today tracks image generation (Ideogram 4.0, Muse Image, Nano Banana 2, Krea 2 Raw/Turbo, Arrow 2) but names no editing leader and no open-weight editing model.

- **State of Creative** gains two lines under AI image generation: Bria Fibo 2.0 as the leading open-weight editing model with its licence caveat, and Krea 3 Ultra as a competitive closed editor with the rank spread and price. One Recent-changes entry dated 21 October is added; the list is at its cap, so the oldest entry (24 June, OpenArt Director and Krea 2) moves to history. Page date moves to 21 October.
- One new source page for this AINews story.

### What to weigh
The primary pages (Bria's release, Krea's announcement, the Artificial Analysis and LMArena boards) were not read; their links in the newsletter are Substack redirects, so ranks and prices are as AINews reported them. Neither model gets its own page, matching how the wiki treats Krea 2. The Krea 2 Raw/Turbo line is kept because Krea 3 Ultra is an API product, not a new release of those open checkpoints.

## Intended changes

- [ ] **Update** `wiki/state-of/creative.md` — add Bria Fibo 2.0 and Krea 3 Ultra lines under "AI image generation"; add one Recent-changes entry dated 2026-10-21; add source id to frontmatter `sources:` and a link under `## Sources`; `as_of` 2026-10-20 → 2026-10-21
- [ ] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — the list is at its cap of 10, so the oldest entry (2026-06-24, OpenArt Director and Krea 2 Raw/Turbo) moves to history; the 2026-06-19 entry already spilled today
- [ ] **Create** `wiki/sources/newsletters/ainews-bria-fibo-krea-3-image-editing-2026-10-21.md` — source summary for this story

## Page drafts

### wiki/state-of/creative.md (updated)

Frontmatter changes only:

```yaml
as_of: 2026-10-21
sources: [... existing ids ..., ainews-bria-fibo-krea-3-image-editing-2026-10-21]
```

Section `### AI image generation`: append two lines after the Krea 2 Raw / Turbo line:

```markdown
- **Bria Fibo 2.0** — Bria; 8B open-weight family (Dev for text-to-image, distilled Edit Turbo for editing); Artificial Analysis rates it the leading open-weight image-editing model and statistically tied with Qwen-Image-2.1 on text-to-image; weights are non-commercial (commercial use needs a Bria agreement); API $32 per 1,000 images; in Diffusers and on fal. Current evidence is newsletter coverage only *(as of 2026-10-21)*
- **Krea 3 Ultra** — Krea; closed image-editing model ranked #4–#8 depending on board (Artificial Analysis #5; LMArena #4 multi-image, #8 single-image editing); 2K output only, $0.27 for a 2K edit with one reference image. Current evidence is newsletter coverage only *(as of 2026-10-21)*
```

`## Recent changes`: insert at the top (newest first) and drop the oldest entry (2026-06-24):

```markdown
- [2026-10-21] Image editing gets an open-weight leader: Bria's Fibo 2.0 (8B, non-commercial weights) tops Artificial Analysis's open-weight editing board; Krea 3 Ultra joins the closed editing top tier at #4–#8 depending on the arena.
```

`## Sources`: append:

```markdown
- [AINews — Bria Fibo 2.0 and Krea 3 Ultra image editing](../sources/newsletters/ainews-bria-fibo-krea-3-image-editing-2026-10-21.md)
```

### wiki/history/state-of/creative.md (updated)

Append to the existing `## Archived from current page on 2026-11-24` block at the end of the file (the apply step uses the actual oldest entry at apply time, and a new block if the apply date differs):

```markdown
- [2026-06-24] OpenArt Director and Krea 2 Raw/Turbo signal creative workflows splitting between conversational editing products and open fine-tuning ecosystems.
```

### wiki/sources/newsletters/ainews-bria-fibo-krea-3-image-editing-2026-10-21.md (new)

```markdown
---
title: AINews — Bria Fibo 2.0 and Krea 3 Ultra image editing
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
published: 2026-10-21
ingested: 2026-11-24
domains: [creative]
---

# AINews — Bria Fibo 2.0 and Krea 3 Ultra image editing

Story from the AINews edition of 2026-10-21 ("On-Device Models, Speech and Image Releases" block). Bria released Fibo 2.0, an 8B open-weight image family that Artificial Analysis rates the leading open-weight editing model, under a non-commercial weights licence. Krea 3 Ultra, a closed editing model, ranks between #4 and #8 depending on the leaderboard. Primary announcements and leaderboards were not fetched; links in the newsletter are Substack redirects.

## Influenced pages
- [State of Creative](../../state-of/creative.md) — added Bria Fibo 2.0 and Krea 3 Ultra lines under AI image generation

## Key claims extracted
- Fibo 2.0: Bria's 8B open-weight family; Dev for text-to-image, distilled Edit Turbo for editing
- Artificial Analysis: leading open-weight editing performance; statistical tie with Qwen-Image-2.1 on text-to-image
- Weights are non-commercial; commercial deployment requires a separate Bria agreement
- Bria API: $32 per 1,000 images; Diffusers support and fal availability announced
- Krea 3 Ultra: Artificial Analysis #5 (earlier posts said #4); LMArena #4 multi-image editing, #8 single-image editing
- Krea 3 Ultra outputs 2K only; a 2K edit with one 1K reference image costs $0.27
- Krea 3 Fast: $0.03 per 1K output image plus $0.02 per 1K reference image
```

## Schema / vocabulary additions

None.

## Open questions
- Should image editing get its own `### AI image editing` section on State of Creative (with GPT-Image-2.5 and MAI-Image-2.5, which already have editing ranks elsewhere in the wiki), or stay inside "AI image generation" as drafted?
	- New section
- Krea now has Krea 2 Raw/Turbo (open checkpoints) and Krea 3 Ultra (API) as separate lines. Merge them into one Krea line, or keep them apart as drafted?
	- Merge
