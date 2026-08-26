---
title: Claude Design
type: tool
domains: [creative]
subcategory: visual-design-prototyping
tags: [anthropic, closed-source, beta]
as_of: 2026-07-08
sources: [claude-design-anthropic-labs, claude-creative-tool-connectors-2026-04-29, claude-code-design-sync-2026-07]
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
- **Pitch decks and presentations** — rough outline to on-brand deck; export to PPTX or Canva
- **Marketing collateral** — landing pages, social assets, campaign visuals
- **Frontier design** — code-powered prototypes with voice, video, shaders, 3D, and built-in AI

## Why it matters

Claude Design extends Anthropic into a domain previously owned by Figma, Canva, and Pitch. The brand-onboarding step (reading codebase + design files) eliminates the blank-slate setup cost and connects the design tool directly to engineering context. The combination with Claude Code (PM → prototype → handoff to Code) is a coherent end-to-end product workflow.

## Caveats

- Research preview — product shape and quality are still evolving
- Relies on Opus 4.7; early reports describe that model as more literal, which may affect design interpretation
- Brand onboarding quality depends on how well structured the codebase and design files are

## Creative tool connectors (as of 2026-04-29)

Anthropic added Claude connectors for professional creative production tools — reported by Superhuman AI (secondary source; verify availability against Anthropic documentation):

- **Adobe** (Creative Suite), **Affinity** (design suite alternative)
- **Blender** (3D modeling and animation), **Fusion** (compositing and VFX)
- **Ableton** (music production), **Splice** (sample library)
- **SketchUp** (architectural and product 3D modeling)
- **Resolume** (VJ/AV performance)

This extends Claude beyond artifact generation into direct integration with creative-production software workflows.

## Current status (as of 2026-07-08)

- Claude Design now syncs with Claude Code in both directions through `/design-sync`: design systems can be pulled into a repo for implementation work, and built work can be pushed back into the Claude Design canvas.

## Recent changes

- [2026-07-08] Claude Code / Claude Design bidirectional sync announced through `/design-sync`.
- [2026-04-29] Creative tool connectors reported: Claude integrations for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume; moves Claude from artifact generation toward in-workflow creative-production integration (secondary coverage)
- [2026-04-22] Full launch via Anthropic Labs; brand onboarding, PPTX/Canva export, group editing, web capture — replacing earlier thin stub

## Sources

- [Introducing Claude Design by Anthropic Labs](../sources/articles/claude-design-anthropic-labs.md)
- [Claude creative tool connectors](../sources/newsletters/claude-creative-tool-connectors-2026-04-29.md)
- [Claude Code and Claude Design sync](../sources/tweets/claude-code-design-sync-2026-07.md)
