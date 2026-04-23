---
type: proposal
source: raw/articles/2026-04-22-anthropiccom-news-claude-design-anthropic-labs.md
status: pending
created: 2026-04-22
---

# Proposal: Claude Design — full product launch (Anthropic Labs)

## Summary

Anthropic Labs launched Claude Design, a collaborative visual design and prototyping tool powered by Claude Opus 4.7. The existing wiki page is a thin placeholder from the announcement. This proposal replaces it with full detail and adds Claude Design to `state-of/creative`.

## Intended changes

- [x] **Update** `wiki/tools/claude-design.md` — major content update; replace thin stub with full description
    > See full draft below (page is short enough that a full rewrite is cleaner than a diff)

- [x] **Update** `wiki/state-of/creative.md` — add Claude Design to a new `Visual design & prototyping` subcategory
    > **Add after `### UI generation`:**
    > ```
    > ### Visual design & prototyping
    >
    > - [[tools/claude-design]] — Anthropic; research preview for collaborative prototype, slide, one-pager, and marketing-asset creation; powered by Opus 4.7; brand onboarding from codebase + design files; Pro/Max/Team/Enterprise *(as of 2026-04-22)*
    > ```
    > **Update `as_of: 2026-04-22` in frontmatter.**
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added `Visual design & prototyping` subcategory; [[tools/claude-design]] full launch via Anthropic Labs
    > ```

- [x] **Create** `wiki/sources/articles/claude-design-anthropic-labs.md` — source summary
    > See draft below

## Page drafts

### wiki/tools/claude-design.md (full update)

```md
---
title: Claude Design
type: tool
domains: [creative, agents]
subcategory: ui-generation
tags: [anthropic, closed-source, beta]
as_of: 2026-04-22
sources: [claude-design-anthropic-labs]
---

# Claude Design

Anthropic Labs' collaborative visual design and prototyping tool. Powered by Claude Opus 4.7, it lets users build polished designs, prototypes, slides, one-pagers, and marketing assets through conversation and direct editing — without requiring a design background.

## Current status (as of 2026-04-22)

- Research preview launched 2026-04-22 via Anthropic Labs; rolling out gradually to Pro, Max, Team, and Enterprise subscribers
- Powered by Claude Opus 4.7 (Anthropic's most capable vision model)
- Brand onboarding: Claude reads your codebase and design files to build a team design system automatically; projects use your colors, typography, and components by default
- Import from: text prompt, images, DOCX/PPTX/XLSX, codebase, or web capture tool (scrapes your live site)
- Refinement via inline comments on specific elements, direct text edits, and adjustment knobs (spacing, color, layout live)
- Org-scoped sharing: private, view-link, or collaborative edit with group conversation + Claude
- Export: PPTX and Canva

## Use cases

- **Realistic interactive prototypes** — static mockups → shareable interactive prototypes without code review
- **PM wireframes** → hand off to Claude Code for implementation or to designers to polish
- **Design explorations** — explore many directions quickly before committing
- **Pitch decks and presentations** — rough outline to on-brand deck; export to PPTX or Canva
- **Marketing collateral** — landing pages, social assets, campaign visuals
- **Frontier design** — code-powered prototypes with voice, video, shaders, 3D, and built-in AI

## Why it matters

Claude Design extends Anthropic into a domain previously owned by Figma, Canva, and Pitch. The brand-onboarding step (reading codebase + design files) is a meaningful differentiator: it eliminates the blank-slate setup cost and connects the design tool directly to engineering context. The combination with Claude Code (PM → prototype → handoff to Code) is a coherent end-to-end product workflow.

## Caveats

- Research preview — product shape and quality are still evolving
- Relies on Opus 4.7; early reports describe that model as more literal, which may affect design interpretation
- Brand onboarding quality depends on how well structured the codebase and design files are

## Recent changes

- [2026-04-22] Full launch via Anthropic Labs; brand onboarding, PPTX/Canva export, group editing, web capture — replacing earlier thin stub

## Sources

- [[sources/articles/claude-design-anthropic-labs]]
```

### wiki/sources/articles/claude-design-anthropic-labs.md (new)

```md
---
title: Introducing Claude Design by Anthropic Labs
type: source
source_type: article
source_file: raw/articles/2026-04-22-anthropiccom-news-claude-design-anthropic-labs.md
url: https://www.anthropic.com/news/claude-design-anthropic-labs
published: 2026-04-22
ingested: 2026-04-22
domains: [creative, agents]
---

# Introducing Claude Design by Anthropic Labs

Anthropic's full launch post for Claude Design. Describes the product as a collaborative visual tool for prototypes, slides, one-pagers, and marketing assets powered by Opus 4.7. Key feature details: brand onboarding from codebase + design files, import from multiple sources, inline refinement controls, org-scoped sharing, PPTX/Canva export, group collaboration.

## Influenced pages

- [[tools/claude-design]] — major content update; thin stub replaced with full description
- [[state-of/creative]] — new `Visual design & prototyping` subcategory added

## Key claims extracted

- Research preview for Pro/Max/Team/Enterprise; rolling out 2026-04-22
- Powered by Claude Opus 4.7
- Brand onboarding reads codebase + design files to auto-build design system
- Import: text, image, DOCX/PPTX/XLSX, codebase, web capture
- Refinement: inline comments, direct edits, live adjustment knobs
- Export: PPTX, Canva
- Org-scoped sharing with group conversation + Claude
```

## Schema / vocabulary additions

- [x] Propose new subcategory `visual-design-prototyping` for `wiki/_schema/subcategories.md` if `ui-generation` feels too narrow for Claude Design's scope (slides, one-pagers, marketing collateral go beyond UI layouts)
    > Please add it, makes sense.

## Open questions

- Claude Design currently has `domains: [agents]` in the old page. This proposal updates it to `[creative, agents]`. The `agents` domain is kept because Claude Design uses Claude as an agent collaborator inside the workflow. Acceptable?
	- Ok
