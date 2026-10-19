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
- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — CI test-impact-analysis case study (moved from AI enablement — software development)

## Key claims extracted

- Central point: with agents writing the code, overhauling infrastructure is now often cheaper than patching it, because writing the replacement is no longer the bottleneck
- Anthropic engineers ship ~8x as much code per quarter as 2021-2025; Claude authors ~80% of merged code and plays a large role in PR review
- Total tests grew 10x and CI jobs grew 25x over a six-month period
- Test-impact-analysis architecture: a "listener" records CI results, a "selector" reads history to decide which tests run per PR; originally a single-writer process
- Three sequential patches: bigger machine (70 days), package-level sharding (29 days), daily restarts (<1 day, caused stale-data selection when listener lag exceeded an hour)
- Redesign: external in-memory data store/journal makes listener workers stateless and horizontally scalable; took 3 weeks for one engineer vs. an estimated quarter a year earlier
- A long-running, service-dedicated Claude Tag session monitored the listener, paged the engineer, retained months of context, and repeatedly argued for the eventual overhaul
- Anthropic's PRs have gotten smaller/more granular over time because Claude prefers that shape, contributing to higher CI job counts
- Stated lessons: assume ~25x load within two quarters, keep state out of processes meant to scale, instrument services as "Claude's eyes and ears"
- Companion post referenced: "AI CI on-call using Claude Tag" (beta)
