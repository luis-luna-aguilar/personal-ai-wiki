---
type: proposal
source: raw/tweets/2026-09-09-vasuman-2095999742031675738.md
status: pending
created: 2026-09-09
---

# Proposal: "Applied AI Doesn't Work" — Vas, CEO of Varick Agents (2026-09-04)

## Summary

### The source

On September 4, 2026, Vas — CEO of Varick Agents, an AI-transformation consultancy that works with $500M-$100B revenue companies — posted a long-form X Article arguing that most enterprise AI spend is being wasted for a very specific, very old reason: it's being "applied" onto broken processes instead of used to redesign them. He roots the argument in Michael Hammer's 1990 Harvard Business Review critique of 1990s IT spending — "heavy investments in information technology have delivered disappointing results... they leave existing processes intact and use computers simply to speed them up" — and argues the line reads as though it were written about AI yesterday. His illustrative case, borrowed from Hammer: an insurance application that took 22 days to move through a business contained only 17 minutes of actual work; even doubling every step's speed only saves 8 minutes, because the time was never in the work, it was in the queues and handoffs between people. He backs the general claim with a concrete, checkable data point: the UK's Department for Business and Trade ran a 1,000-license, 3-month Microsoft 365 Copilot trial and published results showing just 1.14 Copilot actions per user per day, faster-but-lower-quality PowerPoint and Excel output, and its own conclusion that it found no robust evidence that time savings translated into productivity — yet 72% of users were satisfied anyway. From there he lays out a concrete methodology: map a business at the department level (happy path, exceptions, upstream/downstream dependencies, systems of record, touch time vs. elapsed time) using both process mining and operator interviews, then sort every step into one of three buckets — deterministic (plain code), agentic (LLM judgment where labeled history exists), or human-in-the-loop (agent-assembled evidence, human decides) — before building anything. He illustrates it with a bank-reconciliation case study (a 12-step, month-long process across 300+ accounts collapsed to 3 steps) and closes with a set of results Varick reports across its own deployments: month-end close cut from 18-22 days to 7-9, AP exceptions from 600-800/month to under 50, payroll corrections down 90%, and over $100M in total reported value delivered across clients.

### What changes

The wiki's company-wide AI enablement page already has a "move from point solutions to end-to-end workflow re-imagination" guidance bullet; this proposal gives that idea its historical grounding and a concrete operating method.

- **Company-wide AI enablement** gains three new Current-guidance bullets (the Hammer/process-reengineering framing with the 17-minute/22-day illustration, the department-level mapping method, and the three-bucket step-sorting framework, cross-linked to the existing model/human cost-routing page) plus two evidence entries — the independently-checkable UK DBT trial numbers, and Varick's own reported deployment results, explicitly labeled as vendor-reported. The page's Recent-changes list is at its 10-entry cap, so its oldest entry (2026-05-27, the cheap-competence/after-automation framing) spills to history. Page date moves to 4 September.
- One new source page is created for the X Article.

### What to weigh

This is a consultancy CEO's pitch for the exact service he's describing — Varick Agents sells AI-driven process re-engineering, and the framework here is also his sales pitch. The Hammer/BPR framing and the three-bucket sorting method are useful and stand on their own regardless of who's telling the story; the UK DBT trial is independently published and checkable. But the outcome numbers he attributes to his own firm's deployments (month-end close, AP exceptions, the $100M+ total) are self-reported and not independently audited — the draft below attributes them to Varick explicitly throughout rather than stating them as neutral fact, and separates them from the UK trial data in their own bullet.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/company-wide-ai-enablement.md` — add 3 Current-guidance bullets, 2 evidence entries, 1 Recent-changes entry, bump `as_of` to 2026-09-04, add source id
    > See draft below

- [ ] **Spill** `wiki/training/company-wide-ai-enablement.md` → `wiki/history/training/company-wide-ai-enablement.md` — oldest Recent-changes entry (2026-05-27, cheap-competence/after-automation framing) falls off the 10-entry cap
    > See draft below

- [ ] **Create** `wiki/sources/tweets/vasuman-applied-ai-doesnt-work-2026-09-04.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/training/company-wide-ai-enablement.md (updated)

Frontmatter: bump `as_of: 2026-08-28` → `as_of: 2026-09-04`; append `vasuman-applied-ai-doesnt-work-2026-09-04` to `sources:`.

Add to `## Current guidance`, as new bullets placed directly after the existing "Move from point solutions to end-to-end workflow re-imagination..." bullet:

```
- Treat AI adoption as process re-engineering, not a paint layer: Michael Hammer's 1990 HBR critique of 1990s IT investment — "heavy investments in information technology have delivered disappointing results... they leave existing processes intact and use computers simply to speed them up" — applies to AI adoption near-verbatim today. Speeding up the wrong step doesn't help: if a step takes 17 minutes of real work inside a 22-day end-to-end process (the classic Hammer example), doubling that step's speed only saves 8 minutes — the value was in the queues and handoffs, not the work itself.
- Map before building, at the department level, not the whole company or a single workflow in isolation: identify the happy path, the exceptions (share of volume, cycle time, cost of error), upstream/downstream dependencies, systems of record and tie-breaking rules, regional/entity variation, touch time vs. elapsed time, and per-person AI-readiness — via both process mining against systems of record and operator interviews (neither alone is sufficient).
- Sort every process step into one of three buckets before choosing a build approach: **deterministic** (plain code — cheap, auditable, no hallucination risk), **agentic** (LLM judgment where historical labeled examples exist and the step is low-risk — measure every output), or **human-in-the-loop** (evidence assembled by an agent, final call by a human). See [Cost-aware AI task routing](cost-aware-ai-task-routing.md) for the parallel model/human routing framework applied at the execution-model level rather than the process-step level.
```

Add to `## Evidence from practice`, as new entries near the other consumption/adoption-pricing evidence:

```
- **UK Dept for Business and Trade M365 Copilot trial (2025, published 2026):** 1,000 licenses over 3 months produced only 1.14 Copilot actions per user per day; PowerPoint generation got 7 minutes faster (18→11 min) but at lower quality, Excel analysis got slower and lower-quality, and email time savings were "extremely small." The department's own conclusion: "We did not find robust evidence to suggest that time savings are leading to improved productivity" — yet 72% of users reported being satisfied or very satisfied. A concrete illustration of AI adoption improving individual sentiment without moving organizational output.
- **Varick Agents' reported process-redesign results** (vendor-reported, not independently audited): across enterprise deployments (~$500M-$100B revenue clients), month-end close fell from 18-22 days to 7-9 days, AP exception volume fell from 600-800/month to under 50, payroll corrections fell 90%, and reported total value delivered exceeded $100M. Treat these as one AI-transformation vendor's own case-study numbers, not independently verified — the UK DBT trial above is the independently checkable data point in this entry.
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-04] Added process-re-engineering framing for AI adoption (Michael Hammer's 1990 BPR critique, touch-time-vs-elapsed-time, department-level mapping method, Deterministic/Agentic/HITL step-sorting) plus two evidence points: the UK DBT's M365 Copilot trial (1.14 actions/user/day, no measurable productivity gain, 72% satisfied anyway) and Varick Agents' vendor-reported enterprise deployment results.
```

The list is now 11 entries (was at the 10-entry cap); the oldest, `[2026-05-27] Added cheap-competence / after-automation framing...`, is removed from this page and spilled below.

### wiki/history/training/company-wide-ai-enablement.md (updated)

Append a new archive block:

```
## Archived from current page on 2026-09-09

- [2026-05-27] Added cheap-competence / after-automation framing: AI expands the frontier of human work by shifting scarcity toward framing and judgment.
```

### wiki/sources/tweets/vasuman-applied-ai-doesnt-work-2026-09-04.md (new)

```md
---
title: "Applied AI Doesn't Work"
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-vasuman-2095999742031675738.md
url: https://x.com/vasuman/status/2095999742031675738
published: 2026-09-04
ingested: 2026-09-09
---

# "Applied AI Doesn't Work"

A long-form X Article (resolved URL: x.com/i/article/2095378321588826112) by Vas, CEO of AI-transformation consultancy Varick Agents. Argues that most enterprise AI spend fails because it's applied on top of unchanged, often broken processes rather than used to redesign them — grounding the argument in Michael Hammer's 1990 business-process-reengineering critique — and lays out a department-level mapping method plus a three-bucket (deterministic/agentic/human-in-the-loop) step-sorting framework, illustrated with a bank-reconciliation case study and Varick's own reported deployment results.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — process-re-engineering framing, mapping method, three-bucket sort, UK DBT trial and Varick evidence entries

## Key claims extracted

- Michael Hammer's 1990 HBR quote on IT investment applied near-verbatim to AI adoption today
- Illustrative example: a 22-day process containing 17 minutes of real work; doubling step speed only saves 8 minutes
- UK Dept for Business and Trade M365 Copilot trial: 1,000 licenses, 3 months, 1.14 actions/user/day, no robust productivity evidence found, 72% user satisfaction anyway
- $1T AI infrastructure capex (2025) vs. $37B enterprise usage spend
- Department-level mapping method: happy path, exceptions, upstream/downstream, systems of record, regional variation, touch-vs-elapsed time, per-person AI-readiness; via process mining + operator interviews
- Three-bucket step sort: Deterministic (code) / Agentic (LLM judgment, measured) / Human-in-the-Loop (evidence-assisted human decision)
- Bank-reconciliation case study: 12-step, month-long process across 300+ accounts collapsed to 3 steps
- Varick's reported results: month-end close 18-22→7-9 days, AP exceptions 600-800→<50/month, payroll corrections -90%, $100M+ total reported value (vendor-reported, unaudited)
- Author's critique of both traditional consultancies (process-capable, AI-judgment-blind) and AI labs/vendors (agent-capable, process-blind, single-provider lock-in risk)
```
