---
title: Multica — GitHub repository
type: source
source_type: repo
source_file: raw/repos/multica-ai-multica.md
url: https://github.com/multica-ai/multica
ingested: 2026-05-18
domains: [agents, coding]
---

# Multica — GitHub repository

Open-source managed agents platform that positions coding agents (Claude Code, Codex, and 9 others) as first-class project-board teammates. Assign issues like you'd assign to a colleague; agents claim work, execute on a local or cloud runtime, post comments, and compound solutions into reusable team skills. Includes a Squads abstraction for stable multi-agent routing via a leader agent.

## Influenced pages

- [Multica](../../tools/multica.md) — new tool page created
- [State of Agents](../../state-of/agents.md) — added to Agent orchestration subcategory

## Key claims extracted

- Supports Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI
- Squads: leader agent routes work to sub-agents; stable `@TeamName` routing as team composition changes
- Skills compound across sessions: completed solutions become reusable team skills
- Full task lifecycle with WebSocket streaming; local daemon with cloud runtime support
- Stack: Next.js 16, Go (Chi + gorilla/websocket + sqlc), PostgreSQL 17 + pgvector
- Self-hostable (Docker) and cloud-hosted (multica.ai)
- Install: `brew install multica-ai/tap/multica` or install script
