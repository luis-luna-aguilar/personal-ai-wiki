---
title: 'Sarah (@sarahfim) — How to build an anti-slop software factory for teams of 30+'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-19-sarahfim-2109736893198016898.md
url: https://x.com/sarahfim/status/2109736893198016898
published: 2026-10-12
ingested: 2026-10-19
domains: [coding, agents]
---

# Sarah (@sarahfim) — How to build an anti-slop software factory for teams of 30+

An X Article by Composio's product-engineering lead, written up from her 8 October video. Her thesis: a software factory is the repository, not the agents; the repo's own checks should make it nearly impossible for any contributor's agent to write bad code, because otherwise slop compounds across plan, implement, and self-review cycles. She lists seven repository practices in order, then a shared cloud agent, drawn from Composio's dashboard repo (built for agents from February 2026, ~50 contributors across engineering, product, and marketing).

## Influenced pages

- [Software factory](../../workflows/software-factory.md) — new "Repository as the factory" subsection and "slop compounds" failure mode
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — new "lint rules, not skills" Engineering-discipline bullet

## Key claims extracted

- Slop compounds: cloud agents in a messy repo plan, implement, and self-review from the mess, and the effect grows with scale; approvals slow down over time
- The factory is the repository (CI, lint rules, types, tests), not the agent, harness, or skills; contributors should be able to bring any agent
- Most changes to the Composio dashboard are now one-shot-able; ~50 contributors across engineering, marketing, and product
- Co-location (Next.js App Router; route owns components, helpers, tests); `lib` and `utils` folders banned
- End-to-end type safety via tRPC and OpenAPI so the compiler lists every place a schema change touches
- Duplication is acceptable because code generation is cheap; global primitives (buttons, style tokens) stay shared and lint-enforced
- Lint rules over skills: agents ignore instructions, skills go stale as models change; 38 custom lint rules; `useState`/`useEffect` banned without a justifying comment; React Doctor and anti-slop projects as off-the-shelf rule sources
- Global E2E tests: Meticulous (record-and-replay of staging/preview sessions for visual diffs), MCPJam (MCP server testing)
- Bugbots after deterministic checks: slower, more false positives, useful for non-deterministic bugs; `BUGBOT.md` of house practices
- Fast CI matters because non-engineers use preview deployments only; Blacksmith cut some checks by 50% and some by over 70%
- Zen, Composio's internal cloud agent (Slack, Linear, Datadog alert, or cron triggers; reads Datadog, PostHog, Linear via Composio managed auth), merged 1,300+ PRs since February 2026, 245 in September
- Author states the post is not sponsored by any tool mentioned
