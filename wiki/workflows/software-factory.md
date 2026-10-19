---
title: Software factory
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-09-01
sources: [gas-city-software-factory-2026-05, aiewf-loops-debate-2026-07-03, software-factories-fde-2026-07, aiewf-2026-five-trends-latentspace, latent-space-pr-not-welcome-2026-09-01, ubereng-software-factory-2026-08-28]
---

# Software factory

A software factory is an agent pipeline that covers most of the software lifecycle (planning, design, coding, testing, review, deployment, maintenance, feedback) with long-running agents, while humans supervise interfaces, policies, escalation, and fit to the customer's workflow instead of editing every artifact. It is the destination many agentic-coding teams describe; the patterns below cover how to split the work, what has to exist before a factory is safe, and what changes when a project routes contributions through one. The general pattern catalog it builds on is [Agentic orchestration patterns](agentic-orchestration-patterns.md).

## Current patterns

### Structure

- **Software factory loop.** Long-running agents can cover planning, design, coding, testing, review, deployment, maintenance, and feedback, while humans supervise interfaces, policies, escalation, and customer-specific workflow fit rather than editing every artifact.
- **Dark factory / light factory.** Split agentic workflows into a **light** layer (planning, review, and human-agent interaction stay visible) and a **dark** layer (clearly defined execution runs in the background without human monitoring). As trust builds in the dark layer's output, more work moves out of the visible layer. Distinct from simple background execution: the light/dark split is a deliberate architectural boundary, not just async scheduling. *Source: Gas City workshop, Every (2026-05-19)*

### Prerequisites

- **Control layer before software factory.** The AI Engineer World's Fair loops debate sharpened the current constraint: loops are already useful, but the field has not settled the control layer for permissions, cost ceilings, review bottlenecks, and recovery. Treat "software factory" as a destination, not a starting architecture.

### Contribution model

- **PRs closed by default, software factories instead.** Several AI-native OSS projects now auto-close external human pull requests rather than reviewing them as code, routing incoming issues through their own agent pipelines instead: Vercel's AI SDK factory (20M+ weekly npm downloads) authors 25-35% of merged PRs and closes 70-80% of issues, four weeks after deployment; Astro's auto-triage system reversed years of unmanageable issue backlog into a routine weekly task; [Flue](../tools/flue.md) goes further, auto-converting every external PR into an issue or discussion. The framing from tldraw's Steve Ruiz and Ghostty's Mitchell Hashimoto: once agents can implement a well-specified issue, a human PR is no longer more valuable than the issue that specifies it — so large OSS projects increasingly limit community contribution to reporting, discussion, and perspective rather than code. *Source: Latent Space, "PRs Not Welcome" (2026-09-01)*

### Forward-deployed factories

- **FDE work is integration and ROI management.** AI Engineer World's Fair 2026 gave the software-factory/forward-deployed-engineer (FDE) pattern named examples: Sierra's Natalie Meurer described FDE work as managing "all the integrations and all the teams that contribute to the agent"; Cursor's Pauline Brunet framed FDE engagements around a "strict ROI" bar so customers don't turn the agents off after the engagement ends; Warp CEO Zach Lloyd described Oz, a software-factory platform where organizations choose which lifecycle stages to automate and where humans stay in the loop for high-risk changes.
- **Running a factory efficiently at scale.** Uber frames its internal agent stack as a software factory; its efficiency patterns (an AI Context Graph that grounds agents in a queryable graph of internal systems, and code-mode tool batching) are on [Agentic orchestration patterns](agentic-orchestration-patterns.md).

## Failure modes

- Building the factory before the control layer: unbounded cost, unreviewed changes, and no recovery path.
- Moving work into the dark layer before its output has earned trust.

## Recent changes

- [2026-10-19] Page created, split out of [Agentic orchestration patterns](agentic-orchestration-patterns.md): the dark/light factory, control-layer, software-factory-loop, and PRs-closed-by-default patterns, plus the AI Engineer World's Fair FDE examples.
- [2026-09-01] Added the "PRs closed by default" software-factory pattern with three named production examples (Vercel AI SDK, Astro/Flue, tldraw) and their concrete PR/issue-closure numbers.
- [2026-07-14] Added named AI Engineer World's Fair 2026 detail to the software-factory/FDE pattern: named FDE examples (Sierra, Cursor, Warp Oz).

## Related

- [Agentic orchestration patterns](agentic-orchestration-patterns.md) — the general pattern catalog (context, packaging, evaluation, cost) a factory is built from
- [Multi-agent coordination](multi-agent-coordination.md) — worker topologies such as Gas City's mayor-and-polecats split
- [Agent loop design](agent-loop-design.md) — the single-agent loops a factory chains together
- [Harness (agent)](../concepts/harness.md) — the control layer as part of harness design
- [Forward-deployed engineering](../training/forward-deployed-engineering.md) — the FDE model in depth
- [AI enablement — software development](../training/ai-enablement-software-development.md) — team rollout guidance, including Uber's Software Factory

## Sources

- [Inside the 100-agent Software Factory — Gas City](../sources/newsletters/gas-city-software-factory-2026-05.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Software factories and forward-deployed agent engineering](../sources/newsletters/software-factories-fde-2026-07.md)
- [5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space](../sources/newsletters/aiewf-2026-five-trends-latentspace.md)
- [Latent Space — PRs Not Welcome](../sources/newsletters/latent-space-pr-not-welcome-2026-09-01.md)
- [Uber Engineering — Running a Software Factory Efficiently at Uber Scale](../sources/tweets/ubereng-software-factory-2026-08-28.md)
