---
title: Devin
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: []
as_of: 2026-07-14
sources: [devin-auto-triage-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, cognitioncom-blog-ai-productivity]
---

# Devin

Cognition's autonomous coding agent, initially positioned as one of the first "fully autonomous software engineer" agents. Now expanding into persistent operational roles: Auto-Triage (May 2026) is the first always-on production deployment, monitoring Slack channels and triaging bugs without human initiation. Cognition valued at $25B (May 2026).

## Current status (as of 2026-07-14)

- **Auto-Triage:** always-on persistent Devin monitors Slack channels for bug reports, alerts, and incidents
- Parent Devin filters noise and dispatches focused sub-sessions to find root causes, post diagnoses, and tag code owners
- Shared long-term memory deduplicates repeat reports and builds team ownership map
- Generates PR candidates in addition to diagnoses
- Early adopter Modal: "more useful than homegrown triage automations"
- **Security Swarm:** parallel agents fan out across a codebase for vulnerability discovery, validation, patching, and PR generation
- Security Swarm aggregates findings, reproduces each issue in a sandbox, validates exploitability, then writes a patch for review
- **Agentic MapReduce (the architecture behind Security Swarm):** a Plan agent studies the repo and authors deterministic "selectors" (Tree-sitter queries, symbol/type queries, import-graph traversals, lexical patterns); the selectors run over every file with no model in the loop (Shard), producing a bounded, inspectable work queue instead of an open-ended search; one fresh Devin session per batch investigates its shard in parallel (Map); a Reducer session dedupes findings and composes cross-shard attack chains, e.g. an unauthenticated ID leak plus an ID-gated RCE becoming one P0 (Reduce); a final Verify stage reproduces each serious finding in a sandboxed session against a running build and marks it Confirmed, False Positive, or Inconclusive
- Benchmarked against a CVE-pinned ground-truth set (GitHub Advisory Database, each pinned to the commit before its fix, dozens of cases across 12+ languages and vulnerability classes): Security Swarm reports **72% recall**, ahead of other scanners tested in the same eval, at a fraction of their cost
- Cognition claims the system finds more verified vulnerabilities at 30% lower cost than rivals; treat both this and the 72% recall figure as vendor-reported until independently verified, though the CVE-pinned methodology is more rigorous than a bare cost claim
- **Devin Fusion (preview):** a multi-model "sidekick" harness — a frontier model runs alongside a cheaper sidekick model, each a fully capable agent with its own tools and persistent, separately-cached context; the frontier model plans, interprets ambiguity, and reviews, while delegating mechanical or well-scoped work to the sidekick; a lightweight classifier can reassign which model leads mid-session, timed to coincide with context-compaction points so the switch doesn't cost an extra cache miss
- On **FrontierCode Extended** (a cost-aware coding benchmark tracking both score and average cost per task), Fusion matches frontier-model performance at **35% lower cost** than running Opus 4.8 or GPT-5.5 alone, and **41% lower cost** when paired with Fable 5 (measured before Fable 5's access was suspended); internally, **88%** of Cognition's own merged PRs were driven entirely by the automated Fusion router
- **Session productivity estimator:** an automated system that reviews each completed Devin session, classifies whether it produced useful (typically merged) work, then estimates the equivalent human-engineering hours it saved; calibrated against 258 self-reported sessions from 126 users, reaching `r_log = 0.74` on held-out data, deliberately calibrated to underestimate rather than overestimate; now running in production with customers — Cognition frames this as the first automated system measuring AI engineering productivity in production

## Why it matters

Auto-Triage is Cognition's first persistent always-on production agent — distinct from session-scoped coding help. The parent/child Devin architecture (one manager filters noise, many focused workers investigate) is a concrete production instance of the [mayor + polecats orchestration pattern](../workflows/agentic-orchestration-patterns.md). Shared long-term memory across sessions gives it the deduplication capability that ephemeral agents lack.

Security Swarm extends the same architecture into enterprise security work, and Cognition has now named and documented the underlying pattern as [Agentic MapReduce](../workflows/agentic-orchestration-patterns.md): deterministic selection guarantees whole-repo coverage, parallel bounded workers keep cost proportional to relevant code rather than repo size, and a reasoning Reduce step connects findings that isolated workers couldn't see on their own. Devin Fusion applies a different multi-model idea — [sidekick harnesses](../workflows/agentic-orchestration-patterns.md), contrasted with the [Advisor strategy](../workflows/advisor-strategy.md) pattern by keeping both models' contexts persistently cached instead of paying a cache-miss cost per escalation. The productivity estimator is a production instance of [dollar/hours-denominated agent evals](../concepts/agent-evals.md).

## Recent changes

- [2026-07-14] Cognition detailed Agentic MapReduce (Plan/Shard/Map/Reduce/Verify) as the architecture behind Security Swarm; reported 72% recall on a CVE-pinned benchmark vs. rival scanners.
- [2026-07-14] Cognition's session-level productivity estimator (`r_log = 0.74`, human-hours-equivalent, calibrated conservative) is now running in production with customers.
- [2026-06-29] Devin Fusion (preview): multi-model "sidekick" harness matches frontier performance at 35% lower cost (41% with Fable 5) on FrontierCode Extended; 88% of Cognition's internal merged PRs driven by the automated router.
- [2026-07-02] Cognition shipped Devin Security Swarm for parallel vulnerability discovery, sandbox reproduction, exploitability validation, and fix PRs.
- [2026-05-19] Auto-Triage shipped: always-on Slack monitoring, parent/child Devin structure, shared long-term deduplication memory

## Sources

- [Devin Auto-Triage launch](../sources/articles/devin-auto-triage-2026-05.md)
- [The Code - Cognition ships Devin for Security](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Agentic MapReduce (Cognition/Devin blog)](../sources/articles/devinai-blog-agentic-map-reduce.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
- [Estimating the Productivity of an Autonomous AI Software Engineer](../sources/articles/cognitioncom-blog-ai-productivity.md)
