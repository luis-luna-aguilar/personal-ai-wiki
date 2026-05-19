---
title: Multica
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [open-source, agentic]
as_of: 2026-05-18
sources: [multica-repo]
---

# Multica

Open-source managed agents platform. Multica treats coding agents as project-board teammates: assign a GitHub-style issue to an agent (Claude Code, Codex, Copilot CLI, etc.), and the agent claims it, executes it on your runtime, posts comments, raises blockers, and ships code — all visible on a shared board alongside human teammates. Vendor-neutral and self-hostable.

**GitHub:** [multica-ai/multica](https://github.com/multica-ai/multica)

## Current status (as of 2026-05-18)

- Supports 11 agent CLIs out of the box: Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI
- **Squads:** group agents (and humans) under a leader agent; assign work to `@FrontendTeam` instead of an individual — the leader routes to the right member autonomously
- **Reusable skills:** every completed solution is stored as a team skill; deployments, migrations, and code reviews compound over time rather than being re-solved from scratch
- **Autonomous execution:** full task lifecycle (enqueue → claim → start → complete/fail) with real-time WebSocket progress streaming
- **Unified runtimes dashboard:** local daemon auto-detects installed agent CLIs; cloud runtimes also supported; both visible in one UI
- Self-hostable via Docker; cloud offering at multica.ai; CLI via Homebrew

## Stack

Next.js 16 frontend · Go backend (Chi, sqlc, gorilla/websocket) · PostgreSQL 17 with pgvector · local daemon

## Strengths

- First-class "agent as teammate" UX: agents show up in the assignee picker, post comments, and update issue statuses rather than just printing output in a terminal
- Vendor-neutral: switching or mixing agent CLIs requires no code changes
- Squads as a stable routing abstraction — `@TeamName` stays stable as members change

## Weaknesses / caveats

- Early-stage / no public benchmark data
- Skill compounding quality depends on agent and task diversity over time
- Self-hosting requires Docker; cloud offering has no public pricing yet

## Recent changes

- [2026-05-18] First ingest from GitHub repo; initial stable release

## Sources

- [Multica GitHub repository](../sources/repos/multica-repo.md)
