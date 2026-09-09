---
type: proposal
source: raw/newsletters/2026-08-29-ainews-openai-shuts-off-cursor.md
status: pending
created: 2026-09-08
---

# Proposal: Artificial Analysis debuts a Search Index; Perplexity Search takes #1

## Summary

### The source

An AINews digest (2026-08-29) reports that Artificial Analysis launched a new "Search Index" benchmark and placed Perplexity Search on top across all three tested context variants. Perplexity's medium tier scored 80 versus a prior-leader ceiling of 75, while also carrying the lowest per-task inference cost among tested providers, due to smaller payloads. AINews reads this as evidence that search is becoming a benchmarked subsystem of its own — measured on action count, latency, and downstream token cost — rather than a hidden dependency buried inside agents.

### What changes

`tools/perplexity-computer.md` covers Perplexity's orchestration product but doesn't yet mention this benchmark result. This proposal adds a short bullet to Current status and a Recent-changes entry, bumping `as_of` to 2026-08-29.

### What to weigh

This is a thin, single-recap signal — no primary Artificial Analysis writeup was fetched, only AINews' tweet-recap coverage of the launch and results. Consistent with the page's existing sourcing depth, but worth noting given the specific numbers cited (score of 80, prior ceiling of 75) aren't independently verified against Artificial Analysis's own materials.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/perplexity-computer.md` — add Search Index bullet, bump `as_of`, add Recent-changes entry
    > See draft below

Note: `wiki/sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md` is created by the separate "OpenAI shuts off Cursor" proposal, which owns that source page; this proposal only references its slug.

## Page drafts

### wiki/tools/perplexity-computer.md (updated)

```md
---
as_of: 2026-08-29
sources:
  - perplexity-computer-plaid
  - perplexity-personal-computer
  - finance-agent-workflows-2026-05-06
  - ainews-openai-shuts-off-cursor-2026-08-29
---

## Current status (as of 2026-08-29)

(... existing bullets unchanged ...)

- **Perplexity Search tops a new Artificial Analysis Search Index (August 2026):** Artificial Analysis launched a dedicated benchmark for search-as-a-subsystem (measured on action count, latency, and downstream token cost, not just answer quality); Perplexity Search placed #1 across all three tested context variants, with its medium tier scoring 80 against a prior-leader ceiling of 75, and the lowest per-task inference cost among tested providers due to smaller payloads.

## Recent changes

- [2026-08-29] Perplexity Search took #1 on Artificial Analysis's new Search Index benchmark (score 80 vs. prior ceiling 75), with the lowest per-task inference cost among tested providers.
- (... existing entries follow ...)
```
