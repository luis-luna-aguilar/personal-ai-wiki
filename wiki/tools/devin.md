---
title: Devin
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: []
as_of: 2026-05-19
sources: [devin-auto-triage-2026-05]
---

# Devin

Cognition's autonomous coding agent, initially positioned as one of the first "fully autonomous software engineer" agents. Now expanding into persistent operational roles: Auto-Triage (May 2026) is the first always-on production deployment, monitoring Slack channels and triaging bugs without human initiation. Cognition valued at $25B (May 2026).

## Current status (as of 2026-05-19)

- **Auto-Triage:** always-on persistent Devin monitors Slack channels for bug reports, alerts, and incidents
- Parent Devin filters noise and dispatches focused sub-sessions to find root causes, post diagnoses, and tag code owners
- Shared long-term memory deduplicates repeat reports and builds team ownership map
- Generates PR candidates in addition to diagnoses
- Early adopter Modal: "more useful than homegrown triage automations"

## Why it matters

Auto-Triage is Cognition's first persistent always-on production agent — distinct from session-scoped coding help. The parent/child Devin architecture (one manager filters noise, many focused workers investigate) is a concrete production instance of the [mayor + polecats orchestration pattern](../workflows/agentic-orchestration-patterns.md). Shared long-term memory across sessions gives it the deduplication capability that ephemeral agents lack.

## Recent changes

- [2026-05-19] Auto-Triage shipped: always-on Slack monitoring, parent/child Devin structure, shared long-term deduplication memory

## Sources

- [Devin Auto-Triage launch](../sources/articles/devin-auto-triage-2026-05.md)
