---
type: proposal
source: raw/newsletters/2026-07-31-ainews-gpt-56-price-cut-by-20-80-cost-of-gpt.md
status: pending
created: 2026-09-07
---

# Proposal: Gemini Robotics 2 expands to whole-body, multi-robot control

## Summary

### The source

Tucked into AINews' 2026-07-31 roundup (mostly about GPT-5.6 pricing, covered in a separate proposal) is Google DeepMind's launch of Gemini Robotics 2, pitched as "one brain for any robot." The release extends the Robotics line from earlier tabletop-manipulation demos to whole-body humanoid control, fine dexterity, and multi-robot coordination. Alongside the control model, Google shipped Gemini Robotics ER 2, a higher-level embodied-reasoning model that observes a scene, plans a course of action, coordinates with a lower-level VLA (vision-language-action) model, tracks progress through a multi-minute task, and recovers when a step fails. Commentary emphasized that the same checkpoint reportedly drives multiple distinct robot hardware types, and that a variant called On-Device 2 can adapt to an entirely new two-arm robot from fewer than 200 examples. Demoed tasks included knot-tying, screwing in a light bulb, and a collaborative garage-cleanup task split across multiple robots.

### What changes

The wiki's physical-AI trend page currently has a single source from May 2026 and no Recent-changes section yet, since nothing substantive has landed on it since creation.

- **Physical AI deployment curve** gains a Current-status bullet describing Gemini Robotics 2 as the clearest embodied-generality jump tracked so far, a new `## Recent changes` section (this is its first dated entry), and a new source line. Page date moves to 31 July.
- Extends the shared AINews source page for this raw file (created by a sibling proposal in the same digest batch covering GPT-5.6 pricing) with this signal's Influenced-pages and Key-claims, rather than duplicating a source page for the same raw file.

### What to weigh

This is a single-source, lightweight signal — there's no independent verification beyond the one AINews recap, so the "same checkpoint controls multiple hardware types" and "fewer than 200 examples" claims are carried as reported rather than confirmed against Google's own technical documentation. This raw file is also cited by at least one other proposal from this same digest batch (the GPT-5.6 pricing/self-optimization signal); if that proposal's source page already exists by apply time, this proposal's source-page item should extend it instead of creating a second page for the same raw file — noted here so the apply step isn't surprised by the collision.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/physical-ai-deployment.md` — add Gemini Robotics 2 to Current status; add a new Recent-changes section (first entry); add source
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md` — source summary for this raw file (Gemini Robotics 2 angle only; if a sibling proposal already created a page for this same `source_file`, extend that page instead — see "What to weigh")

## Page drafts

### wiki/trends/physical-ai-deployment.md (updated)

Update frontmatter:

```md
---
title: Physical AI deployment curve
type: trend
domains: [agents]
tags: [agentic]
as_of: 2026-07-31
sources: [physical-ai-deployment-2026-05-13, ainews-gpt-56-price-cut-2026-07-31]
---
```

Add a new bullet to `## Current status`:

```md
- Google DeepMind's Gemini Robotics 2 (July 2026) is the clearest embodied-generality jump so far: a single checkpoint now reportedly controls multiple robot hardware types, extending from tabletop manipulation to whole-body humanoid control and multi-robot coordination, with a companion embodied-reasoning model (Gemini Robotics ER 2) that plans, coordinates with a VLA model, tracks progress, and recovers from failed steps during multi-minute tasks. A variant, On-Device 2, reportedly adapts to a new two-arm robot from fewer than 200 examples.
```

Add a new section after `## What to watch` (this page has no Recent-changes section yet — this is its first entry):

```md
## Recent changes

- [2026-07-31] Google DeepMind launched Gemini Robotics 2: one checkpoint reportedly controls multiple robot hardware types, whole-body humanoid control, multi-robot coordination; companion Gemini Robotics ER 2 embodied-reasoning model; On-Device 2 adapts to a new two-arm robot from fewer than 200 examples.
```

Add to `## Sources`:

```md
- [AINews — GPT-5.6 price cuts, Inkling-Small, Gemini Robotics 2](../sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md)
```

### wiki/sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md (new)

```md
---
title: AINews — GPT-5.6 price cuts, Inkling-Small, Gemini Robotics 2
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-31-ainews-gpt-56-price-cut-by-20-80-cost-of-gpt.md
url: https://www.latent.space/p/ainews-gpt-56-price-cut-by-20-80
published: 2026-07-31
ingested: 2026-09-07
domains: [models, agents]
---

# AINews — GPT-5.6 price cuts, Inkling-Small, Gemini Robotics 2

AINews recap covering three separate stories from the same issue: OpenAI's GPT-5.6 price cuts (Luna -80%, Terra -20%, new Sol Fast tier) tied to the ongoing "cost of constant intelligence" curve; Thinking Machines' Inkling-Small open-weight release (276B/12B active, AA Intelligence Index 40); and Google DeepMind's Gemini Robotics 2 launch (whole-body humanoid control, multi-robot coordination, Gemini Robotics ER 2 embodied reasoning). This page currently documents only the Gemini Robotics 2 angle in detail — sibling proposals processed from the same digest batch cover the GPT-5.6 and Inkling-Small stories and, if applied after this page exists, should extend this page's claims and Influenced-pages rather than creating a duplicate source page for the same raw file.

## Influenced pages

- [trends/physical-ai-deployment](../../trends/physical-ai-deployment.md) — added Gemini Robotics 2 as the clearest embodied-generality jump tracked so far

## Key claims extracted

- Gemini Robotics 2: "one brain for any robot" — whole-body humanoid control, dexterity, multi-robot coordination
- Gemini Robotics ER 2: embodied-reasoning model that observes, plans, coordinates with a VLA model, tracks progress, and recovers from failed steps during multi-minute tasks
- Same checkpoint reportedly controls multiple hardware types
- On-Device 2 can adapt to a new two-arm robot from fewer than 200 examples
- Demos: knot-tying, screwing in a bulb, collaborative garage cleanup
```

## Open questions

- None beyond the source-page collision risk noted above.
