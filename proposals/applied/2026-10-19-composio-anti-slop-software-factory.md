---
type: proposal
source: raw/tweets/2026-10-19-sarahfim-2109736893198016898.md
status: pending
created: 2026-10-19
---

# Proposal: Composio's anti-slop software factory

## Summary

### In short
A software factory's quality lives in the repository, not in the agents: if the repo's own checks make bad code fail immediately, anyone's agent can contribute, and if they don't, slop compounds with every agent pass. Composio backs this with a dashboard repo of about 50 contributors, 38 custom lint rules, and an internal cloud agent that has merged 1,300+ PRs since February. The proposal adds a "repository as the factory" section to Software factory and one lint-over-skills bullet to the engineering enablement page. One reason to hesitate: its "skills get ignored" claim cuts against the wiki's skill-friendly guidance.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Sarah, who leads product engineering at Composio (a company that sells managed tool access and authentication for agents), published an X Article on 12 October 2026 expanding a video from four days earlier. In February she built Composio's dashboard repository from scratch for agents; it now has almost 50 contributors across engineering, product and marketing, each using a personal agent,, and she says most changes are now one-shot-able.

Her starting point: slop compounds. A cloud agent working in a messy repository plans from the mess, implements that plan, then reviews its own output, and at scale each round makes the next worse. So the factory is the repository, not the agent, harness or skills. She lists the machinery in a deliberate order. Co-location comes first: everything a feature needs sits in one folder, so agents search less and reviewers see a PR's scope, and she banned shared `lib` and `utils` folders outright. Then end-to-end types, so the compiler names every place a schema change touches; duplication over shared components, except global primitives such as buttons and style tokens; and lint rules instead of skills, because agents ignore written instructions and skills go stale as models change, while a lint rule fails at once and explains the fix. Global end-to-end tests follow (Meticulous session replay, MCPJam for MCP servers), then code-review bots only for bugs no deterministic check can catch, then fast CI, because marketers work only through preview deployments. Only after all that comes a shared cloud agent: Composio's internal Zen, triggered from Slack, Linear, Datadog alerts or cron.

### What changes
Software factory currently covers how to split a factory's work and why a control layer comes first, but not what inside the repository keeps agent output clean.

- **Software factory** gains a "Repository as the factory" subsection with Composio's seven-step ordering and Zen as the worked example, plus a "letting slop compound" failure mode. One Recent-changes entry dated 12 October; page date moves from 1 September to 12 October.
- **AI enablement — software development** gains one Engineering-discipline bullet, "enforce conventions with lint rules, not skills," pointing to Software factory. One Recent-changes entry, bringing the list to the cap of 10 with no spill; page date moves to 12 October.
- The **index** line for Software factory mentions the new section.
- One new source page for the article.

### What to weigh
The lint-over-skills claim sits awkwardly beside the wiki's existing advice to build skill marketplaces and micro-skills; the drafts record it as a claim about convention enforcement in shared repos rather than overturning that guidance; adjust the framing if you read it as broader. The evals page for coding agents was left untouched because it already sits at its length ceiling and already says deterministic gates come first.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/workflows/software-factory.md` — new `### Repository as the factory` subsection under Current patterns, one new Failure-modes bullet, frontmatter `as_of` 2026-09-01 → 2026-10-12 and one source id appended, adds one Recent-changes entry dated 2026-10-12 (list goes 3 → 4, no spill), appends one Sources link
    > See draft below

- [ ] **Update** `wiki/training/ai-enablement-software-development.md` — one new bullet under `### Engineering discipline`, frontmatter `as_of` 2026-09-14 → 2026-10-12 and one source id appended, adds one Recent-changes entry dated 2026-10-12 (list goes 9 → 10, at cap, no spill), appends one Sources link
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the `workflows/software-factory` line and its as_of
    > See draft below

- [ ] **Create** `wiki/sources/tweets/composio-anti-slop-software-factory-2026-10-12.md` — source summary

## Page drafts

### wiki/workflows/software-factory.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-12
sources: [gas-city-software-factory-2026-05, aiewf-loops-debate-2026-07-03, software-factories-fde-2026-07, aiewf-2026-five-trends-latentspace, latent-space-pr-not-welcome-2026-09-01, ubereng-software-factory-2026-08-28, composio-anti-slop-software-factory-2026-10-12]
```

New subsection, inserted under `## Current patterns` directly after `### Prerequisites`:

```
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
```

`## Failure modes` (full section):

```
## Failure modes

- Building the factory before the control layer: unbounded cost, unreviewed changes, and no recovery path.
- Moving work into the dark layer before its output has earned trust.
- Letting slop compound: running agents at scale in a repo whose conventions live only in instructions rather than enforced checks, so every plan-implement-self-review round builds on the previous round's slop and approvals slow down over time.
```

`## Recent changes` — adds one entry dated 2026-10-12, placed below the 2026-10-19 entry (full section):

```
## Recent changes

- [2026-10-19] Page created, split out of [Agentic orchestration patterns](agentic-orchestration-patterns.md): the dark/light factory, control-layer, software-factory-loop, and PRs-closed-by-default patterns, plus the AI Engineer World's Fair FDE examples.
- [2026-10-12] Added "Repository as the factory": Composio's seven-step ordering (co-location, end-to-end types, duplication, 38 lint rules instead of skills, global E2E tests, review bots last, fast CI) before a shared cloud agent (Zen, 1,300+ merged PRs since February), plus the "slop compounds" failure mode.
- [2026-09-01] Added the "PRs closed by default" software-factory pattern with three named production examples (Vercel AI SDK, Astro/Flue, tldraw) and their concrete PR/issue-closure numbers.
- [2026-07-14] Added named AI Engineer World's Fair 2026 detail to the software-factory/FDE pattern: named FDE examples (Sierra, Cursor, Warp Oz).
```

`## Sources` — appends one link:

```
- [Sarah (@sarahfim) — How to build an anti-slop software factory for teams of 30+](../sources/tweets/composio-anti-slop-software-factory-2026-10-12.md)
```

### wiki/training/ai-enablement-software-development.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-12
sources: [ramp-ai-adoption-playbook, shopify-latent-space-april-2026, lennysan-simonw-interview, agentic-cognitive-overhead, the-code-2026-04-23, qa-tooling-for-software-agents-deep-research, agent-review-artifacts-2026-05-13, agentic-coding-trap-may-2026, ai-stack-fungibility-hashimoto-2026-05, shopify-claude-code-bessemer-2026-05, github-kyle-daigle-june-2026, software-factories-fde-2026-07, dashbench-code-review-understanding-2026-07, openais-new-model-for-cyber-attacks-2026-07-16, bun-rust-rewrite-2026-07-16, ubereng-software-factory-2026-08-28, anthropic-ci-test-impact-analysis-2026-09-14, composio-anti-slop-software-factory-2026-10-12]
```

`### Engineering discipline` — appends one bullet after "Stack fungibility":

```
- **Enforce conventions with lint rules, not skills.** When many people bring their own agents to one repository, written instructions (skills, rules files) will be ignored by someone's agent and go stale as models change; a custom lint rule fails at once, tells the agent how to fix it, and binds every contributor's harness equally. Composio's dashboard repo (~50 contributors across engineering, product, and marketing) runs 38 custom rules and adds one whenever an agent repeats a mistake. Keep CI fast for the same reason: contributors who work only through preview deployments get the build as their whole feedback loop. The full repository-as-factory ordering is on [Software factory](../workflows/software-factory.md).
```

`## Recent changes` — adds one entry dated 2026-10-12, placed below the two 2026-10-19 entries (list goes 9 → 10, at cap, no spill). Full section:

```
## Recent changes

- [2026-10-19] Split "Evidence from practice" out to [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md) and grouped Proven patterns under `###` subheads.
- [2026-10-19] Split "Hiring AI-native engineers" and "The junior talent problem" out to [AI-native hiring and the junior talent pipeline](ai-native-hiring-and-junior-talent.md), a separate audience (hiring managers and talent leads).
- [2026-10-12] Added "Enforce conventions with lint rules, not skills" (Composio: 38 custom lint rules across a ~50-contributor repo; fast CI for preview-only contributors).
- [2026-09-14] Added Anthropic's test-impact-analysis CI-scaling case study: 25x CI job growth over six months, three successive patches (70/29/<1 days), a three-week stateless redesign (rebuilding now often cheaper than patching), and a dedicated Claude Tag monitoring session; new Proven-patterns bullet on planning CI/test infrastructure for exponential rather than linear growth.
- [2026-08-28] Added Uber's Software Factory adoption numbers (70%+ PRs agent-attributed, 3,600+ agent skills, 30K executions/day, 7x WAU growth) and its core strategic argument: eliminating wasted token consumption, not just cheaper unit prices, is what let usage scale 7x while unit costs fell.
- [2026-07-16] Corrected the Bun Zig→Rust rewrite figures in the Stack-fungibility bullet (535,496 lines, 11 days, ~$165K in tokens) and added a full case study of its one-implementer/two-adversarial-reviewer methodology, plus a new "Adversarial review" pattern generalizing the technique.
- [2026-07-08] Added AI PR/code-review workflow as a first-class enablement concern: historical PR replay, local review standards, and understanding-preserving review artifacts.
- [2026-07-01] Added software-factory/FDE rollout pattern: enterprise agent adoption needs workflow integration capacity, not only developer tooling.
- [2026-06-02] GitHub 14x agent commit growth added: 275M AI-generated commits/week in April 2026; CI/CD CPU capacity becomes bottleneck; micro-skills pattern added
- [2026-05-19] Shopify fleet patterns (Bessemer): LLM proxy, CLAUDE.md ~60-line cap, explicit allow/deny permission config; 20% productivity gain; strategy-to-execution ratio 70%/30% (was 30%/70%); Q3 target 90% autonomous coding
```

`## Sources` — appends one link:

```
- [Sarah (@sarahfim) — How to build an anti-slop software factory for teams of 30+](../sources/tweets/composio-anti-slop-software-factory-2026-10-12.md)
```

### wiki/index.md (updated)

Replaces the `workflows/software-factory` line:

```
- [workflows/software-factory](workflows/software-factory.md) — end-to-end agent pipelines across the software lifecycle: software-factory loop, dark/light factory split, control layer first, repository as the factory (Composio: co-location, lint rules over skills, fast CI before cloud agents), PRs closed by default in AI-native OSS (Vercel AI SDK, Astro/Flue, tldraw), FDE examples (Sierra, Cursor, Warp Oz) *(as_of: 2026-10-12)*
```

### wiki/sources/tweets/composio-anti-slop-software-factory-2026-10-12.md (new)

```
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
```

## Schema / vocabulary additions

None.

## Open questions

- Should [Evals for agentic software development](../wiki/training/evals-for-agentic-software-development.md) also get a one-line pointer to the Composio ordering (deterministic checks before review bots)? Left out because that page already sits at its length ceiling and already states the same "deterministic gates first" order.
	- Leave it out.
