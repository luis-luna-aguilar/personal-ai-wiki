---
title: Software factory
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-10-19
sources: [gas-city-software-factory-2026-05, aiewf-loops-debate-2026-07-03, software-factories-fde-2026-07, aiewf-2026-five-trends-latentspace, latent-space-pr-not-welcome-2026-09-01, ubereng-software-factory-2026-08-28, composio-anti-slop-software-factory-2026-10-12, rauchg-gdp-ts-2026-10]
---

# Software factory

A software factory is an agent pipeline that covers most of the software lifecycle (planning, design, coding, testing, review, deployment, maintenance, feedback) with long-running agents, while humans supervise interfaces, policies, escalation, and fit to the customer's workflow instead of editing every artifact. It is the destination many agentic-coding teams describe; the patterns below cover how to split the work, what has to exist before a factory is safe, and what changes when a project routes contributions through one. The general pattern catalog it builds on is [Agentic orchestration patterns](agentic-orchestration-patterns.md).

## Current patterns

### Structure

- **Software factory loop.** Long-running agents can cover planning, design, coding, testing, review, deployment, maintenance, and feedback, while humans supervise interfaces, policies, escalation, and customer-specific workflow fit rather than editing every artifact.
- **Dark factory / light factory.** Split agentic workflows into a **light** layer (planning, review, and human-agent interaction stay visible) and a **dark** layer (clearly defined execution runs in the background without human monitoring). As trust builds in the dark layer's output, more work moves out of the visible layer. Distinct from simple background execution: the light/dark split is a deliberate architectural boundary, not just async scheduling. *Source: Gas City workshop, Every (2026-05-19)*

### Prerequisites

- **Control layer before software factory.** The AI Engineer World's Fair loops debate sharpened the current constraint: loops are already useful, but the field has not settled the control layer for permissions, cost ceilings, review bottlenecks, and recovery. Treat "software factory" as a destination, not a starting architecture.
- **Make unsafe agent code fail to compile.** Rules an agent must follow at every call site, such as running the authorization check before a sensitive write, hold up better as type and lint errors than as review comments. [gdp-ts](../tools/gdp-ts.md) has data-layer functions demand a proof, minted only by a trusted module, that the check ran on those exact values; a bundled agent skill steers coding agents toward the pattern and a lint preset blocks forged proofs. It adds about 0.3 ms of type-check time per authorized call site and almost no runtime cost. *Source: gdp-ts README (2026-10-19)*

### Repository as the factory

- **The factory is the repository, not the agent.** Composio's product-engineering lead argues that a factory's quality lives in the repo's own machinery (CI, lint rules, types, tests), so that anyone can bring their own agent, harness, and model and still find it nearly impossible to write bad code. Without it, slop compounds: a cloud agent in a messy repo plans from the mess, implements that plan, then self-reviews its own output, and each round degrades the next. Her Composio dashboard repo, designed for agents from February 2026 and now worked on by ~50 contributors across engineering, product, and marketing, reports most changes as one-shot-able. Her layering, in order:
  1. **Co-location.** Everything a feature needs (components, helpers, tests) lives in one folder, as with the Next.js App Router, so agents find it with little searching and reviewers see a PR's real scope. Shared `lib` and `utils` folders are banned.
  2. **End-to-end types** (tRPC, OpenAPI), so the compiler names every place a schema change touches.
  3. **Duplication over shared abstractions**, since generating a helper twice is cheap; the exception is global primitives (buttons, style tokens), which lint rules enforce.
  4. **Lint rules instead of skills.** Agents ignore written instructions, and skills go stale as models change; a lint rule fails immediately, says how to fix it, and binds every contributor's agent. Composio runs 38 custom rules, including a ban on `useState`/`useEffect` without a justifying comment: "every time an agent gets something wrong, you lint it away."
  5. **Global end-to-end tests**: Meticulous replays recorded staging and preview sessions for visual diffs; MCPJam tests MCP servers.
  6. **Review bots last among checks**, only for bugs no deterministic check can catch, because their loop is slower and noisier than a lint rule's; a `BUGBOT.md` of house practices turns the bot into an enforced self-review on every PR.
  7. **Fast CI**, because non-engineers work only through preview deployments, so the build is their whole loop (moving to Blacksmith cut some checks by 50-70%).
- **Then a shared cloud agent.** Only once the repo enforces its own standards does Composio point its internal cloud agent, Zen, at it. Zen is triggered from a Slack message, a Linear issue, a Datadog alert, or a cron job, reads logs, session replays, and tickets through Composio's managed auth, and has merged 1,300+ PRs across Composio's repos since February 2026 (245 in September). *Source: Sarah (@sarahfim), Composio (2026-10-12)*

### Contribution model

- **PRs closed by default, software factories instead.** Several AI-native OSS projects now auto-close external human pull requests rather than reviewing them as code, routing incoming issues through their own agent pipelines instead: Vercel's AI SDK factory (20M+ weekly npm downloads) authors 25-35% of merged PRs and closes 70-80% of issues, four weeks after deployment; Astro's auto-triage system reversed years of unmanageable issue backlog into a routine weekly task; [Flue](../tools/flue.md) goes further, auto-converting every external PR into an issue or discussion. The framing from tldraw's Steve Ruiz and Ghostty's Mitchell Hashimoto: once agents can implement a well-specified issue, a human PR is no longer more valuable than the issue that specifies it — so large OSS projects increasingly limit community contribution to reporting, discussion, and perspective rather than code. *Source: Latent Space, "PRs Not Welcome" (2026-09-01)*

### Forward-deployed factories

- **FDE work is integration and ROI management.** AI Engineer World's Fair 2026 gave the software-factory/forward-deployed-engineer (FDE) pattern named examples: Sierra's Natalie Meurer described FDE work as managing "all the integrations and all the teams that contribute to the agent"; Cursor's Pauline Brunet framed FDE engagements around a "strict ROI" bar so customers don't turn the agents off after the engagement ends; Warp CEO Zach Lloyd described Oz, a software-factory platform where organizations choose which lifecycle stages to automate and where humans stay in the loop for high-risk changes.
- **Running a factory efficiently at scale.** Uber frames its internal agent stack as a software factory; its efficiency patterns (an AI Context Graph that grounds agents in a queryable graph of internal systems, and code-mode tool batching) are on [Agentic orchestration patterns](agentic-orchestration-patterns.md).

## Failure modes

- Building the factory before the control layer: unbounded cost, unreviewed changes, and no recovery path.
- Moving work into the dark layer before its output has earned trust.
- Letting slop compound: running agents at scale in a repo whose conventions live only in instructions rather than enforced checks, so every plan-implement-self-review round builds on the previous round's slop and approvals slow down over time.

## Recent changes

- [2026-10-19] Added the "make unsafe agent code fail to compile" prerequisite, with gdp-ts as the example.
- [2026-10-19] Page created, split out of [Agentic orchestration patterns](agentic-orchestration-patterns.md): the dark/light factory, control-layer, software-factory-loop, and PRs-closed-by-default patterns, plus the AI Engineer World's Fair FDE examples.
- [2026-10-12] Added "Repository as the factory": Composio's seven-step ordering (co-location, end-to-end types, duplication, 38 lint rules instead of skills, global E2E tests, review bots last, fast CI) before a shared cloud agent (Zen, 1,300+ merged PRs since February), plus the "slop compounds" failure mode.
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
- [Sarah (@sarahfim) — How to build an anti-slop software factory for teams of 30+](../sources/tweets/composio-anti-slop-software-factory-2026-10-12.md)
- [rauchg/gdp-ts — Ghosts of Departed Proofs for TypeScript (GitHub)](../sources/repos/rauchg-gdp-ts-2026-10.md)
