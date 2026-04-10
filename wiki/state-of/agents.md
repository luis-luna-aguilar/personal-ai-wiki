---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-09
sources: [cursor-3-launch, advisor-strategy]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

## Subcategories

### Agent orchestration UIs

Surfaces (desktop, web, mobile, chat) where humans supervise, hand off, and review work across multiple AI agents running in parallel.

- [[tools/cursor]] — Cursor 3's desktop app surfaces local and cloud agents in one sidebar, with handoff between environments and demos/screenshots from cloud agents *(as of 2026-04-09)*

### Model orchestration

Patterns that combine models of different sizes or costs inside a single agentic task. Concerned with *how* agents are structured internally (which model runs the loop, which model steps in when), not with the user-facing surface.

- [[workflows/advisor-strategy]] — Anthropic: a small executor (Sonnet or Haiku) drives the loop and escalates to Opus as an *advisor* only when stuck. Shipped as a server-side `advisor_20260301` tool on the Claude API, making it a one-line change to a Messages request. Reported +2.7% on SWE-bench Multilingual *and* −11.9% cost for Sonnet+Opus-advisor vs Sonnet alone *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] Added `model-orchestration` subcategory with [[workflows/advisor-strategy]] after ingesting Anthropic's advisor-strategy launch post.
- [2026-04-09] First content for this page. Added `agent-orchestration-ui` subcategory with Cursor after ingesting the Cursor 3 launch post.
