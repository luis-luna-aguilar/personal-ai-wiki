---
type: proposal
sources:
  - raw/newsletters/2026-07-02-the-website-of-the-future-may-assemble-itself-for.md
  - raw/newsletters/2026-07-03-vercels-andrew-qu-on-why-agents-are-a-new-kind-of.md
status: pending
created: 2026-07-06
---

# Proposal: Agent-readable web

## Summary

The approved computer-use signal is that websites are starting to split into human visual experiences and machine-readable agent experiences. Vercel's interview is concrete: detect agent requests and serve Markdown directly; the companion newsletter frames future sites as assembling different surfaces for humans and agents.

## Intended changes

- [x] **Create** `wiki/trends/agent-readable-web.md` - current trend page.
- [x] **Update** `wiki/state-of/computer-use.md` - add agent-readable websites as an adjacent computer-use infrastructure pattern.
- [x] **Create** source summary `wiki/sources/newsletters/website-future-agent-readable-2026-07-02.md`.
- [x] **Update** `wiki/index.md` - add the new trend page.

## Page drafts

### wiki/trends/agent-readable-web.md (new)

```md
---
title: Agent-readable web
type: trend
domains: [agents, computer-use]
tags: [agentic]
as_of: 2026-07-03
sources: [website-future-agent-readable-2026-07-02, vercel-agents-new-software-2026-07-03]
---

# Agent-readable web

The agent-readable web is the shift from one website experience for everyone toward separate surfaces for humans and AI agents. Humans still get visual layouts; agents may receive Markdown, structured data, tool schemas, or task-specific representations that are easier to parse and act on.

## Current status
- Vercel already detects when an agent makes a request and serves Markdown directly instead of requiring the agent to parse visual HTML.
- Agent traffic and bot traffic are rising while human traffic is comparatively flatter, creating incentive to make product sites usable by non-human visitors.
- The design split is practical, not only aesthetic: agent-readable pages can reduce parsing cost, improve task completion, and make product documentation current inside agent workflows.

## Why it matters

Computer-use agents can operate through visual UIs, but that is often the most expensive and brittle path. If sites expose agent-native representations, web interaction becomes closer to API/tool use while preserving the public web as the discovery layer.

## What to watch
- Whether `llms.txt`, Markdown endpoints, MCP servers, or structured website manifests become the default agent surface.
- Whether SEO and "agent optimization" converge or split into separate disciplines.
- Whether serving different human/agent experiences creates abuse, cloaking, or compliance concerns.

## Recent changes
- [2026-07-03] Vercel interview confirms production behavior: detect agent requests and serve Markdown directly.

## Sources
- [The website of the future may assemble itself for you](../sources/newsletters/website-future-agent-readable-2026-07-02.md)
- [Vercel's Andrew Qu on why agents are a new kind of software](../sources/newsletters/vercel-agents-new-software-2026-07-03.md)
```

### wiki/state-of/computer-use.md (snippet)

```md
### Agent-readable web infrastructure

Web surfaces optimized for agents rather than only for humans.

- [Agent-readable web](../trends/agent-readable-web.md) - sites increasingly serve Markdown or structured machine-readable representations to agents while keeping visual pages for humans; Vercel reports doing this in production *(as of 2026-07-03)*

## Recent changes
- [2026-07-03] Added agent-readable web trend: Vercel reports serving Markdown directly to detected agent requests, signaling a split between human and machine website experiences.
```

### Source summary (new)

```md
---
title: The website of the future may assemble itself for you
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-02-the-website-of-the-future-may-assemble-itself-for.md
published: 2026-07-02
ingested: 2026-07-06
domains: [agents, computer-use]
---

# The website of the future may assemble itself for you

Newsletter coverage of how websites may become dynamic, agent-readable, and personalized as AI agents become a larger share of web traffic.

## Influenced pages
- [Agent-readable web](../../trends/agent-readable-web.md) - trend page
- [State of Computer Use](../../state-of/computer-use.md) - adjacent infrastructure category

## Key claims extracted
- Agent traffic changes the incentives for website structure.
- Sites may serve different representations for humans and agents.
- The web may shift from static pages toward generated or assembled experiences.
```

## Open questions

- Should this remain a trend, or later become a concept if the wiki needs a durable definition separate from current market movement?
	- Lets make it a concept, this is more than a trend.
