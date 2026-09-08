---
type: proposal
source: raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md
status: pending
created: 2026-09-07
---

# Proposal: Cost-normalized benchmarks and Fable's adoption gap both point toward "intelligence is outpacing the need for it"

## Summary

### The source

Two threads from the same week converge on one reading: frontier intelligence is outrunning how much of it typical work actually needs, and cost-normalized measurement is starting to show it directly rather than leaving it as a vibe. On the benchmark side, an AINews issue reports Together AI found GLM-5.3 completes 5x more DeepSWE work than Claude Fable 5 under a fixed $100 budget (roughly 17 solved tasks versus 3) despite similar first-try quality; GPT-5.6 Sol Max scored 72.7% on DeepSWE v1.1 for $6.47/task against Fable 5 Max's 69.7% for $21.63/task; and Cline found a stealth model, Ox Alpha, solving a real bugfix using roughly 3x fewer output tokens than Fable. On the adoption side, Every's own newsletter — reporting on a colleague's tech-consulting practice — cites Ramp/Anthropic spending data showing Fable, "the most capable model on the market," accounted for only 6% of Anthropic's own purchased tokens and 11% of model spend a month after its launch, hindered largely by the lack of a zero-data-retention option many enterprises require outright; Every's own head of tech consulting reports getting "no relative gain from Fable on 80 percent" of his knowledge-work tasks. Meanwhile, per Ramp/Vercel data cited in the same piece, open-weight models' share of tokens routed through Vercel's AI Gateway rose from 11% to 29% in two months, though still under 4% of spend — high-volume, low-stakes work is visibly migrating to cheaper models faster than dollars are.

### What changes

Two existing pages already track exactly this territory and both get incremental updates rather than new sections built from scratch.

- **Cost-aware AI task routing** gains a new evidence bullet with the cost-normalized DeepSWE/Cline numbers, reinforcing its existing routing-by-cost guidance with a third data point alongside the page's Databricks and Bridgewater cases. Page date moves to 26 August. This page has no Recent-changes section, so none is added.
- **Open-weight momentum broadens** gains a new Recent-changes entry and a matching Current-signal bullet on Fable's slow enterprise adoption and Vercel Gateway's open-weight share growth. Page date moves to 26 August. The page's Recent-changes list (10 entries) is at its cap, so the oldest entry (the July 22 Laguna S 2.1 note) spills to `wiki/history/trends/open-weight-momentum-broadens.md`.
- Reuses the AINews source page already drafted by a companion proposal (the harness-compounding proposal) for the DeepSWE/Cline data, rather than creating a duplicate; creates one new source page for the Every "Cloning Your Coworkers" newsletter (also referenced, for different content, by a separate self-improving-skills proposal).

### What to weigh

The DeepSWE/Cline cost figures are secondary Twitter-relayed benchmark comparisons, not primary published methodology papers — treated as directional evidence consistent with how this page already handles similar third-party comparisons. Every's Fable-adoption commentary is one company's own experience plus Ramp/Vercel spending data as reported by Every, not a broad market survey; it's presented as a data point, not a market-wide conclusion.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add cost-normalized benchmark evidence bullet, bump as_of
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — add Fable-adoption/open-weight-share bullet, Recent-changes entry, bump as_of
    > See draft below

- [ ] **Spill** `wiki/trends/open-weight-momentum-broadens.md` → `wiki/history/trends/open-weight-momentum-broadens.md` — oldest Recent-changes entry (2026-07-22) falls off the 10-entry cap
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-cloning-your-coworkers-2026-08-26.md` — source summary
    > See draft below

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

> **Frontmatter:** `as_of: 2026-08-21` → `as_of: 2026-08-26`; append `ainews-andrew-ng-ai-engineering-2026-08-25` and `every-cloning-your-coworkers-2026-08-26` to `sources:`.

> New bullet appended to `## Evidence from practice`:

```md
- **Cost-normalized agent benchmarks widen the gap between "most capable" and "best value."** Together AI found GLM-5.3 completes 5x more DeepSWE work than Fable 5 under a fixed $100 budget (~17 vs. ~3 solved tasks) despite similar first-try quality; GPT-5.6 Sol Max scored 72.7% on DeepSWE v1.1 for $6.47/task versus Fable 5 Max's 69.7% for $21.63/task; and Cline found a stealth model (Ox Alpha) solving a real bugfix using roughly 3x fewer output tokens than Fable. Separately, Every reports Fable — despite being "the most capable model on the market" — accounted for only 6% of Anthropic's purchased tokens and 11% of model spend a month after launch, largely because it lacks a zero-data-retention option many enterprises require outright; Every's own head of tech consulting reports "no relative gain from Fable on 80 percent" of his knowledge-work tasks. Read together, these argue for routing by cost-normalized task completion rather than raw capability score whenever a cheaper model clears the quality bar.
```

> **Sources** (append):
```md
- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
- [Every — The Case for Cloning Your Coworkers](../sources/newsletters/every-cloning-your-coworkers-2026-08-26.md)
```

### wiki/trends/open-weight-momentum-broadens.md (updated)

> **Frontmatter:** `as_of: 2026-08-20` → `as_of: 2026-08-26`; append `every-cloning-your-coworkers-2026-08-26` to `sources:`.

> New bullet appended to `## Current signal`:

```md
- **Fable's slow enterprise adoption widens the opening for open-weight models (August 2026):** per Ramp/Anthropic data cited by Every, Fable — despite being the market's most capable model — accounted for only 6% of Anthropic's purchased tokens and 11% of model spend a month after launch, hindered largely by the lack of a zero-data-retention option many enterprises require outright. Over the same window, open-weight models' share of tokens routed through Vercel's AI Gateway rose from 11% to 29% in two months (still under 4% of spend). Read alongside [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md)'s cost-normalized benchmark data, the pattern suggests routing pressure is shifting real workloads toward cheaper/open models even where a stronger closed model remains available.
```

> **Recent changes:** add as the newest entry (adds one entry; enforce the cap by spilling the current oldest, 2026-07-22):
```md
- [2026-08-26] Fable's low enterprise adoption (6% of Anthropic tokens purchased, 11% of model spend a month after launch — largely a zero-data-retention gap) and open-weight token share on Vercel's AI Gateway rising from 11% to 29% in two months both point toward a "diminishing returns on frontier intelligence for typical work" reading, reinforced by cost-normalized benchmark data on the routing page.
```

> **Sources** (append):
```md
- [Every — The Case for Cloning Your Coworkers](../sources/newsletters/every-cloning-your-coworkers-2026-08-26.md)
```

### wiki/history/trends/open-weight-momentum-broadens.md (updated)

> Adds a new archive block above the existing ones (spills the current oldest live entry):

```md
## Archived from current page on 2026-09-07

- [2026-07-22] Poolside released Laguna S 2.1 (118B/8B-active MoE, OpenMDW-1.1 license): a new non-Chinese open-weight coding entrant, strong on agentic-coding benchmarks, more prone to fabrication under pressure than Qwen3.5-122B per one independent eval.
```

### wiki/sources/newsletters/every-cloning-your-coworkers-2026-08-26.md (new)

```md
---
title: The Case for Cloning Your Coworkers
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md
url: https://every.to/context-window/the-case-for-cloning-your-coworkers
published: 2026-08-26
ingested: 2026-09-07
domains: [agents, training]
---

# The Case for Cloning Your Coworkers

Every's Context Window newsletter covering KateBench/DanLens (cloning specific colleagues' judgment into reusable skills), a self-improve Codex skill for correcting agent mistakes, Walleye Capital's mandatory AI-fluency policy, and Fable's slow enterprise adoption versus open-weight models' rising token share. Two companion proposals also draw on this issue.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — Fable adoption data
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Fable adoption data, Vercel Gateway open-weight share
- [Agent skill methodology](../../training/agent-skill-methodology.md) — self-improve Codex skill as a proven pattern

## Key claims extracted

- Fable accounted for 6% of Anthropic's purchased tokens and 11% of model spend a month after launch
- Fable lacks a zero-data-retention option, barring many enterprise customers outright
- Open-weight models' share of tokens routed through Vercel's AI Gateway rose from 11% to 29% in two months (under 4% of spend)
- Every's head of tech consulting reports "no relative gain from Fable on 80 percent" of his knowledge-work tasks
- Arielle Shipper (Every's head of operations) runs a self-improve Codex skill: feed the agent feedback on a mistake, then run the skill to propose a targeted edit to Codex's own instructions
- Walleye Capital ($10B hedge fund) has made AI use mandatory for all 400 employees
```

## Open questions

- None beyond the sourcing notes above.
