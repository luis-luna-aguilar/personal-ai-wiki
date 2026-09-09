---
title: The Folder Is the Agent
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-04-the-folder-is-the-agent.md
url: https://every.to/source-code/the-folder-is-the-agent-rerun
published: 2026-09-04
ingested: 2026-09-09
domains: [agents, coding]
---

# The Folder Is the Agent

Every's Kieran Klaassen (Cora GM) describes running 44 specialized agents as durable folders, each with its own CLAUDE.md/AGENT.md, skills, and accumulated institutional knowledge, routed by a small file-based dispatch layer. Cites Anthropic's own multi-agent research (90% better / 15x tokens for Opus-lead + Sonnet-subagent research tasks) and closes on "you can't vibe orchestrate" — build and trust a flow before handing it to autonomous dispatch.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — extended folder-scoped-specialization pattern with dispatch-layer mechanics and the Anthropic citation

## Key claims extracted

- 44 agents run as folders, routed by a Ruby daemon dispatch layer
- Two slash commands: cross-project status briefing, and task-kickoff/orchestrate
- Anthropic: Opus lead + Sonnet sub-agents beat single Opus by 90% on research tasks, at 15x the token cost
- Most coding tasks parallelize worse than research tasks
- Rule of thumb: build a flow yourself, use it, trust it — only then hand it to autonomous dispatch
