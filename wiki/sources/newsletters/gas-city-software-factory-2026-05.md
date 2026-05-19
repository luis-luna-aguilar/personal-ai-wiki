---
title: "Inside the 100-agent Software Factory — Gas City"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-19-inside-the-100-agent-software-factory.md
url: https://every.to/context-window/inside-the-100-agent-software-factory
published: 2026-05-19
ingested: 2026-05-19
domains: [agents, coding]
---

# Inside the 100-agent Software Factory — Gas City

Every (Mike Taylor) attended a Gas City workshop and wrote a detailed Vibe Check. Gas City is the open-source successor to Gas Town (Steve Yegge), rebuilt by Chris Sells and Julian Knutsen. Currently ~100 agents, ~50 PRs/day, ~1B tokens/day. Three architecture ideas worth internalizing: dark/light factory, mayor/polecats, and multi-model parallel review. Verdict: sharp ideas, not yet practical for most teams.

## Influenced pages

- [Harness (concept)](../../concepts/harness.md) — dark/light factory, mayor/polecats, multi-model review as named primitives
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — two new named patterns

## Key claims extracted

- Gas City: ~100 agents, ~50 PRs/day, ~1B tokens/day; uses Beads task tracker (agent-first, CLI-only)
- Dark/light factory: visible human-agent collaboration (light) vs background agent execution (dark)
- Mayor + polecats: one persistent named supervisor routes work to anonymous disposable workers
- Multi-model review: Claude + Codex + Kimi in parallel on the same code diff
- Limitations: per-agent sessions don't share memory; six-step jobs cost ~6× one session; requires a day of setup with expert support
- Verdict (Mike Taylor): "Learn from the ideas. Skip the toolkit for now."
- OpenAI Symphony cited as a more accessible enterprise-ready alternative for the same orchestration need
