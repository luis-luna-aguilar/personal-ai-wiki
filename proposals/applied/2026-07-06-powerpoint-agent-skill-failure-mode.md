---
type: proposal
sources:
  - raw/newsletters/2026-06-29-ai-could-do-anything-then-it-met-powerpoint.md
status: pending
created: 2026-07-06
---

# Proposal: PowerPoint remains hard for agents

## Summary
Every's presentation-automation piece is a useful training signal: polished decks require visual judgment, narrative structure, brand matching, research discipline, and extremely low defect rates. The strongest wiki update is to agent-skill methodology and anti-autopilot review guidance, not a new product page.

## Intended changes

- [x] **Update** `wiki/training/agent-skill-methodology.md` — add PowerPoint as evidence that serious skills need tools, references, scripts, and review loops.
    > **Add:** Presentation generation is a high-context skill, not a prompt trick. Every notes Anthropic's official PowerPoint skill includes dozens of files, Python scripts, a long skill file, and reference material, which makes it a good example of skill-as-software rather than skill-as-instruction.

- [x] **Update** `wiki/training/anti-autopilot-review-friction.md` — add near-correct deck generation as a failure mode.
    > **Add:** An 80% correct deck can be worse than no automation when defects are subtle, brand-sensitive, or costly to catch late; review friction must be part of the workflow design.

- [x] **Update** `wiki/state-of/creative.md` — add a caveat under slides/design workflows that mature presentation automation remains hard despite stronger creative agents.

- [x] **Create** `wiki/sources/newsletters/powerpoint-agent-skill-failure-mode-2026-06.md` — source summary.

## Updated Page Snippets

### `wiki/training/agent-skill-methodology.md`

> **Before:**
> `The core problem: skills written as long procedures become stale, redundant, or broken as the model improves or the task changes.`

> **After:**
> `The core problem: skills written as long procedures become stale, redundant, or broken as the model improves or the task changes. But thin skills are not enough for artifact-heavy work: polished presentation generation shows that serious skills may need supporting scripts, examples, references, validators, and review loops.`

### `wiki/training/anti-autopilot-review-friction.md`

> **Before:**
> `- Mistaking "I saw it" for "I reviewed it"`

> **After:**
> `- Mistaking "I saw it" for "I reviewed it"`
> `- Accepting near-correct polished artifacts too quickly. An 80% correct presentation can be worse than no automation when the defects are subtle, brand-sensitive, or expensive to catch late.`

### `wiki/state-of/creative.md`

> **Before:**
> `- [Genspark Slides](../tools/genspark-slides.md) — AI presentation generation inside Genspark's broader agent/content surface *(as of 2026-04-22)*`

> **After:**
> `- [Genspark Slides](../tools/genspark-slides.md) — AI presentation generation inside Genspark's broader agent/content surface; current training evidence still cautions that polished enterprise decks need deep skill/tooling support and human review, not a thin prompt *(as of 2026-06-29)*`

## Page Drafts

### `wiki/sources/newsletters/powerpoint-agent-skill-failure-mode-2026-06.md` (new)

```md
---
title: PowerPoint remains hard for agents
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-29-ai-could-do-anything-then-it-met-powerpoint.md
published: 2026-06-29
ingested: 2026-07-06
domains: [creative, training, agents]
---

# PowerPoint remains hard for agents

Every argues that enterprise presentation automation remains difficult because good decks require narrative cohesion, design precision, brand/style matching, research diligence, and near-zero defect rates. The piece uses Anthropic's PowerPoint skill as evidence that reliable presentation agents require substantial supporting files, scripts, references, and review loops.

## Influenced pages
- [Agent skill methodology](../../training/agent-skill-methodology.md) — skill-as-software example
- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — near-correct artifact failure mode
- [State of Creative](../../state-of/creative.md) — presentation automation caveat

## Key claims extracted
- Deck generation has a low tolerance for subtle errors.
- Thin prompting is insufficient for polished enterprise presentations.
- Review burden and over-trust make partially correct decks risky.
```
