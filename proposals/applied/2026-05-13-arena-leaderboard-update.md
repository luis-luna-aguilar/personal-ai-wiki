---
type: proposal
sources:
  - raw/newsletters/2026-05-13-googles-macbook-competitor.md
status: pending
created: 2026-05-13
---

# Proposal: Arena leaderboard update — Claude Opus 4.7 "most consistently dominant"

## Summary

Arena's latest leaderboard (May 2026) calls Claude Opus 4.7 "the most consistently dominant model," leading across nearly every category. Specialization pattern: Gemini 3.1 Pro close second with an edge in creative writing; Meta Spark leads coding; GPT-5.5 leads math; Grok 4.20 leads creative writing and hard prompts; GPT-Image-2 tops text-to-image; Veo 3.1 claims video generation.

## Intended changes

- [x] **Update** `wiki/state-of/models.md` — update Frontier multimodal models section and add Arena leaderboard note to Recent changes; update `as_of` and `sources`
    > See diff snippets below

- [x] **Create** `wiki/sources/newsletters/arena-leaderboard-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/state-of/models.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-05-05`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append:**
> Add `arena-leaderboard-2026-05-13`

**Frontier multimodal models section — update Claude Opus 4.7 line:**
> **Before:** `- [Claude Opus 4.7](../models/claude-opus-4-7.md) — Anthropic flagship; stronger on explicit coding, document, and visual artifact tasks, but early user reports describe more literal behavior and mixed long-context reliability *(as of 2026-04-21)*`
> **After:** `- [Claude Opus 4.7](../models/claude-opus-4-7.md) — Anthropic flagship; Arena (May 2026): "most consistently dominant model," leads nearly every category; *(as of 2026-05-13)*`

**Frontier multimodal models section — update GPT-5.5 line:**
> **Before:** `- [GPT-5.5](../models/gpt-5-5.md) — OpenAI's April 2026 frontier model; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench; Claude Opus 4.7 still leads on SWE-Bench Pro, MCP Atlas, FinanceAgent, and some planning-heavy work *(as of 2026-04-23)*`
> **After:** `- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench *(as of 2026-05-13)*`

**Add new models to Frontier multimodal models (if not already present):**
> If `Gemini 3.1 Pro` does not have an entry under Frontier multimodal models, add:
> `- **Gemini 3.1 Pro** — Google; Arena (May 2026): close second overall; leads creative writing *(as of 2026-05-13)*`
>
> If `Grok 4.20` does not have an entry, add:
> `- **Grok 4.20** — xAI; Arena (May 2026): leads creative writing and hard prompts *(as of 2026-05-13)*`

**Under Image generation — add Veo 3.1 if not present:**
> `- **Veo 3.1** — Google; Arena (May 2026): leads video generation category *(as of 2026-05-13)*`

**Under Coding models — update Meta Spark if not present:**
> Check if Meta Spark is listed under `Frontier multimodal models` or `Coding models`. If not present in either section, add:
> `- **Meta Spark** — Meta; Arena (May 2026): leads coding category *(as of 2026-05-13)*`

**Recent changes — prepend:**
```
- [2026-05-13] Arena leaderboard (May 2026): Claude Opus 4.7 "most consistently dominant" overall; Gemini 3.1 Pro close second/creative writing; Meta Spark leads coding; GPT-5.5 leads math; Grok 4.20 leads creative/hard prompts; GPT-Image-2 tops text-to-image; Veo 3.1 leads video
```

### wiki/sources/newsletters/arena-leaderboard-2026-05-13.md (new)

```markdown
---
title: Arena leaderboard — May 2026 update
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-13-googles-macbook-competitor.md
published: 2026-05-13
ingested: 2026-05-13
domains: [models]
---

# Arena leaderboard — May 2026 update

Newsletter "Google's MacBook Competitor" (May 13) includes an Arena leaderboard summary alongside the Googlebook announcement. Primary URL: https://arena.ai/leaderboard/text

## Influenced pages

- [State of Models](../../state-of/models.md) — Arena results added to Frontier multimodal models section and Recent changes

## Key claims extracted

- Overall: Claude Opus 4.7 described as "the most consistently dominant model"
- Creative writing: Gemini 3.1 Pro close second to Opus 4.7; Grok 4.20 also strong in creative writing and hard prompts
- Coding: Meta Spark leads the coding category
- Math: GPT-5.5 strongest in math
- Hard prompts: Grok 4.20 leads
- Text-to-image: GPT-Image-2 tops this category
- Video generation: Veo 3.1 claims the video generation category
- Coverage source: newsletter summary, not the Arena site directly; treat as secondary until verified against arena.ai/leaderboard/text
```

