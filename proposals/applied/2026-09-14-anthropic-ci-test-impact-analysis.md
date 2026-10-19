---
type: proposal
source: raw/articles/2026-09-14-claudecom-blog-agentic-coding-is-straining-ci-heres-how-we-s.md
status: pending
created: 2026-09-14
---

# Proposal: Anthropic — scaling test impact analysis for agentic-coding CI load

## Summary

### In short
With agents writing the code, rebuilding infrastructure properly is now often cheaper than patching it, because writing the replacement is no longer the bottleneck. Anthropic's redesign of its CI test-selection service took one engineer three weeks, against a quarter estimated a year earlier, after three quick patches each bought less time (70 days, 29 days, under one day). Other lessons: plan for about 25x CI load within two quarters, keep state out of anything meant to scale, and instrument services so an agent can monitor them. Adds this to **AI enablement — software development**. No red flags.

[[#Open questions|Open questions: none.]]

### The source

An Anthropic engineering blog post walks through what happened when agentic coding pushed the company's CI infrastructure past its limits, and how the team fixed it for good rather than patching around it again. The starting numbers set the scale of the problem: Anthropic engineers now ship roughly 8x as much code per quarter as in 2021-2025, Claude authors about 80% of that code and does a large share of PR review, and over six months the total test suite grew 10x while CI jobs grew 25x. All of that load hit a single service — a "test impact analysis" pipeline made of a "listener" (records every CI run's results) and a "selector" (decides which tests actually need to run on a given PR) — which had been built as a single-writer process because keeping one consistent history per test seemed to require it. As load climbed, the team tried three successive quick fixes: doubling the machine's cores (bought 70 days), sharding state by code package so each shard had its own writer (bought 29 days), and daily restarts once the process started hitting memory limits (bought less than a day, and quietly caused the selector to run on stale data whenever the listener fell behind). Notably, a long-running Claude Tag session dedicated to monitoring the service repeatedly argued for a full redesign during this period, paging the on-call engineer whenever listener lag crossed a threshold and holding months of context without needing to be re-briefed. The team eventually took that advice: they gave the service an external in-memory data store, so any listener worker could append a result to a shared journal and move on statelessly, with a separate small process rolling the journal into per-test history. The redesign took three weeks for one engineer, versus an estimated quarter a year earlier — the author's framing is that overhauling infrastructure is now often *cheaper* than patching it, because writing the replacement code is no longer the bottleneck. The stated lessons: assume roughly 25x load within two quarters when agents are involved, avoid single-instance stateful services for anything expected to scale, and instrument services well enough that an agent can act as their "eyes and ears" and drive incremental fixes.

### What changes

The wiki's [AI enablement — software development](../wiki/training/ai-enablement-software-development.md) page already flags "CI/CD is the real bottleneck, not code generation" as a failure mode (via GitHub's commit-volume data) and already cites Anthropic's high-level RSI numbers (80%+ Claude-authored code, 8x code/quarter); this proposal gives both of those a concrete, first-party engineering case study.

- **AI enablement — software development** gains one new Proven-patterns bullet (the generalizable lesson: plan CI/test infrastructure for exponential rather than linear growth, keep state out of anything meant to scale, instrument for agent monitoring) and one new Evidence-from-practice bullet under "Scale data and large-scale case studies" (the concrete Anthropic numbers: 25x CI job growth, the three patches and how long each lasted, the three-week redesign, and the dedicated Claude Tag monitoring session). One new Recent-changes entry is added; the page's list is at its 10-entry cap, so the oldest entry (2026-05-18, Karpathy's failure-mode trio) spills to history. Page date moves to 14 September.
- One new source page is created for the blog post.

### What to weigh

Nothing to weigh.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add 1 Proven-patterns bullet, 1 Evidence-from-practice bullet, 1 Recent-changes entry, bump `as_of` to 2026-09-14, add source id
    > See draft below

- [x] **Spill** `wiki/training/ai-enablement-software-development.md` → `wiki/history/training/ai-enablement-software-development.md` — oldest Recent-changes entry (2026-05-18, Karpathy failure-mode trio) falls off the 10-entry cap
    > See draft below

- [x] **Create** `wiki/sources/articles/anthropic-ci-test-impact-analysis-2026-09-14.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/training/ai-enablement-software-development.md (updated)

Frontmatter: bump `as_of: 2026-08-28` → `as_of: 2026-09-14`; append `anthropic-ci-test-impact-analysis-2026-09-14` to `sources:`.

Add to `## Proven patterns`, as a new bullet directly after the "Uber's 'Software Factory'" bullet:

```
- **Plan CI/test infrastructure for the exponential, not linear, growth curve.** As agents accelerate code generation and PR review, CI job volume can compound faster than intuition suggests; quick fixes (bigger machines, sharding, restarts) buy successively less time until the architecture itself is decoupled and made stateless. See Anthropic's test-impact-analysis case below for the concrete numbers. Anthropic's own rule of thumb: assume roughly 25x load within two quarters, keep state out of any process meant to scale, and instrument services well enough that an agent has the signal to monitor and help hill-climb the fix itself.
```

Add to `## Evidence from practice` → `### Scale data and large-scale case studies`, as a new bullet after the "Anthropic internal RSI data" bullet:

```
- Anthropic's test-impact-analysis (test-selection) service (September 2026): as Claude came to author 80%+ of merged code and engineers shipped 8x more code per quarter, total tests grew 10x and CI jobs grew 25x over six months, repeatedly overloading the "listener/selector" service that decides which tests run on each PR. Three sequential patches — a bigger machine, package-level sharding, then daily restarts — bought 70 days, then 29 days, then under a day, before the team redesigned the service around an external in-memory data store so listener workers could be stateless and horizontally scalable; the redesign took three weeks for one engineer versus an estimated quarter a year earlier. A long-running, service-dedicated Claude Tag session monitored the listener, paged the engineer, and retained context across months whenever lag crossed a threshold, repeatedly arguing for the eventual overhaul before the team acted on it. Anthropic's stated lesson: assume 25x load within two quarters, keep state out of any process meant to scale, and instrument services as "Claude's eyes and ears."
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-14] Added Anthropic's test-impact-analysis CI-scaling case study: 25x CI job growth over six months, three successive patches (70/29/<1 days), a three-week stateless redesign, and a dedicated Claude Tag monitoring session; new Proven-patterns bullet on planning CI/test infrastructure for exponential rather than linear growth.
```

The list is now 11 entries (was at the 10-entry cap); the oldest, `[2026-05-18] Karpathy failure modes: assumption runaway, over-engineering drift, orthogonal side-effects...`, is removed from this page and spilled below.

### wiki/history/training/ai-enablement-software-development.md (updated)

Append to the existing archive block (same apply-date header already present from an earlier spill):

```
## Archived from current page on 2026-09-14

- [2026-05-18] Karpathy failure modes: assumption runaway, over-engineering drift, orthogonal side-effects; success-criteria pattern: give agents verifiable done-conditions rather than step-by-step instructions
```

### wiki/sources/articles/anthropic-ci-test-impact-analysis-2026-09-14.md (new)

```md
---
title: "Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic"
type: source
source_type: article
source_file: raw/articles/2026-09-14-claudecom-blog-agentic-coding-is-straining-ci-heres-how-we-s.md
url: https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
ingested: 2026-09-14
domains: [coding, agents]
---

# "Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic"

An Anthropic engineering blog post on scaling its test-impact-analysis (test-selection) CI service under agentic-coding load: 25x CI job growth over six months, three successive stopgap patches, and a full redesign to a stateless, horizontally-scalable architecture built around an external in-memory data store. Includes a case of using a long-running, service-dedicated Claude Tag session as an infrastructure monitor.

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — new Proven-patterns bullet (plan for exponential CI growth) and Evidence-from-practice case study

## Key claims extracted

- Anthropic engineers ship ~8x as much code per quarter as 2021-2025; Claude authors ~80% of merged code and plays a large role in PR review
- Total tests grew 10x and CI jobs grew 25x over a six-month period
- Test-impact-analysis architecture: a "listener" records CI results, a "selector" reads history to decide which tests run per PR; originally a single-writer process
- Three sequential patches: bigger machine (70 days), package-level sharding (29 days), daily restarts (<1 day, caused stale-data selection when listener lag exceeded an hour)
- Redesign: external in-memory data store/journal makes listener workers stateless and horizontally scalable; took 3 weeks for one engineer vs. an estimated quarter a year earlier
- A long-running, service-dedicated Claude Tag session monitored the listener, paged the engineer, retained months of context, and repeatedly argued for the eventual overhaul
- Anthropic's PRs have gotten smaller/more granular over time because Claude prefers that shape, contributing to higher CI job counts
- Stated lessons: assume ~25x load within two quarters, keep state out of processes meant to scale, instrument services as "Claude's eyes and ears"
- Companion post referenced: "AI CI on-call using Claude Tag" (beta)
```

## Open questions

- None.
