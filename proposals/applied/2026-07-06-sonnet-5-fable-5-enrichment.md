---
type: proposal
sources:
  - raw/articles/2026-07-06-anthropiccom-news-claude-sonnet-5.md
  - raw/newsletters/2026-07-01-ainews-sonnet-5-today-and-fable-5-tomorrow.md
  - raw/newsletters/2026-07-01-anthropic-drops-claude-sonnet-5.md
  - raw/newsletters/2026-07-01-anthropic-releases-sonnet-5.md
status: pending
created: 2026-07-06
---

# Proposal: Claude Sonnet 5 and Fable 5 enrichment

## Summary
Anthropic's official Sonnet 5 launch gives stronger product, pricing, safety, and API detail than the existing July 2 summary. AINews adds benchmark and cost-context signals, while the same source cluster confirms Fable 5 access returned after the U.S. government freeze with some fallback routing still in place.

## Intended changes

- [x] **Update** `wiki/models/claude-sonnet-5.md` — add official availability, pricing, effort-level, safety, and benchmark/cost detail.
    > **Add to Current status:** Sonnet 5 is available across Claude plans, Claude Code, and the API as `claude-sonnet-5`; launch pricing is $2/M input and $10/M output through 2026-08-31, then $3/M input and $15/M output.
    > **Add caveat:** Third-party coverage reports higher benchmark scores than Sonnet 4.6 but also materially higher output-token cost per task.

- [x] **Update** `wiki/models/claude-fable-5.md` — clarify restored access and remove stale "access suspended" caveat.
    > **Replace stale caveat:** Fable 5 access has returned after the U.S. government freeze, but some routine coding/debugging work may still fall back to Opus under Anthropic's safety routing.

- [x] **Update** `wiki/state-of/models.md` — refresh Sonnet 5 and Fable 5 lines with restored-access and Sonnet 5 availability notes.

- [x] **Update** `wiki/state-of/coding.md` — note Sonnet 5's Claude Code availability and reported agentic coding improvements.

- [x] **Create** `wiki/sources/articles/claude-sonnet-5-official-2026-06-30.md` — official source summary.

## Updated Page Snippets

### `wiki/models/claude-sonnet-5.md`

> **Before:**
> `## Current status (as of 2026-07-02)`
>
> `- Every's Vibe Check found Sonnet 5 broadly competent at writing, structured knowledge work, and some coding tasks, but hard to prefer over Opus 4.8, Fable 5, or GPT-5.5 for many specific jobs.`

> **After:**
> `## Current status (as of 2026-06-30)`
>
> `- Anthropic's official launch positions Sonnet 5 as its most agentic Sonnet model yet, available across Claude plans, Claude Code, and the API as claude-sonnet-5.`
> `- Launch pricing is $2/M input and $10/M output through 2026-08-31, then $3/M input and $15/M output.`
> `- Every's Vibe Check and The Code still make the routing caveat important: Sonnet 5 is broadly competent, but high-effort runs can cost more per completed task than the nominal tier price implies.`

### `wiki/models/claude-fable-5.md`

> **Before:**
> `- All benchmark positions are pre-ban; no ongoing public evaluation is possible while access is suspended.`

> **After:**
> `- Benchmark positions mostly come from launch/pre-ban coverage, but Fable 5 access has returned. Anthropic now applies safety fallback routing, so some sensitive or routine tasks may route to Opus 4.8 instead of Fable 5.`

### `wiki/state-of/models.md`

> **Before:**
> `- [Claude Sonnet 5](../models/claude-sonnet-5.md) — Anthropic middle-tier default; competent but early testing flags unclear model fit and higher cost per finished task at high effort *(as of 2026-07-02)*`

> **After:**
> `- [Claude Sonnet 5](../models/claude-sonnet-5.md) — Anthropic middle-tier default and most agentic Sonnet; available in Claude, Claude Code, and API, with early testing still flagging cost-per-task sensitivity at high effort *(as of 2026-06-30)*`

### `wiki/state-of/coding.md`

> **Before:**
> `- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: /goal autonomous loops, Agent View multi-session supervision, dynamic workflows (ultracode), and an official four-level loop taxonomy; Fable 5 is available again but sensitive-domain requests may fall back to Opus 4.8, making model-routing resilience part of the coding-agent operating model *(as of 2026-07-02)*`

> **After:**
> `- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows; now supports Sonnet 5 as a broadly available agentic default while Fable 5 remains the high-capability but fallback-routed tier, making model-routing resilience part of the coding-agent operating model *(as of 2026-06-30)*`

## Page Drafts

### `wiki/sources/articles/claude-sonnet-5-official-2026-06-30.md` (new)

```md
---
title: Claude Sonnet 5 official launch
type: source
source_type: article
source_file: raw/articles/2026-07-06-anthropiccom-news-claude-sonnet-5.md
url: https://www.anthropic.com/news/claude-sonnet-5
published: 2026-06-30
ingested: 2026-07-06
domains: [models, coding, agents]
---

# Claude Sonnet 5 official launch

Anthropic launched Claude Sonnet 5 as its most agentic Sonnet model, emphasizing stronger planning, browser and terminal tool use, coding, reasoning, and knowledge-work performance. The model is available across Claude plans, Claude Code, and the Claude API as `claude-sonnet-5`; promotional pricing is $2/M input and $10/M output through 2026-08-31 before moving to $3/M input and $15/M output.

## Influenced pages
- [Claude Sonnet 5](../../models/claude-sonnet-5.md) — official availability, pricing, API name, safety notes, and effort-level detail
- [State of Models](../../state-of/models.md) — Sonnet 5 status refresh
- [State of Coding](../../state-of/coding.md) — Claude Code availability and agentic coding note

## Key claims extracted
- Sonnet 5 is available in Claude plans, Claude Code, and the Claude API.
- Anthropic positions it as the most agentic Sonnet model to date.
- High-effort settings can approach Opus 4.8 on some tasks, while medium effort improves cost efficiency.
- Anthropic reports lower hallucination and sycophancy than Sonnet 4.6 and lower malicious capability than current Opus models.
```

## Open Questions
- Should Fable 5 keep a separate "restricted deployment" section now that access has returned, or should that history live only in `trends/restricted-frontier-deployment.md`?
