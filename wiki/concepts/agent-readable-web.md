---
title: Agent-readable web
type: concept
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
- Whether SEO and agent optimization converge or split into separate disciplines.
- Whether serving different human/agent experiences creates abuse, cloaking, or compliance concerns.

## Recent changes

- [2026-07-03] Vercel interview confirms production behavior: detect agent requests and serve Markdown directly.

## Sources

- [The website of the future may assemble itself for you](../sources/newsletters/website-future-agent-readable-2026-07-02.md)
- [Vercel's Andrew Qu on why agents are a new kind of software](../sources/newsletters/vercel-agents-new-software-2026-07-03.md)
