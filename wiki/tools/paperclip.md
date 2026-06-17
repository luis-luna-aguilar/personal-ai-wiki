---
title: Paperclip
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [open-source, agentic, self-hosted]
as_of: 2026-06-10
sources: [papercliping]
---

# Paperclip

Open-source (MIT), self-hosted platform for managing AI agents as a company. The core framing: you are the board of directors; agents are employees with titles, reporting lines, monthly budgets, and scheduled heartbeats. You hire, approve strategy, set goals, and override at any time.

## Current status (as of 2026-06-10)

- 69.9k GitHub stars; installed via `npx paperclipai onboard --yes`
- Model-agnostic: Claude, Codex, Gemini, Cursor, Hermes, OpenClaw, and others can all be "hired" into the same org chart
- Core primitives: Org Chart (hierarchies, roles, titles), Goal Alignment (every task traces to a mission via SKILL.md), Heartbeats (agents wake on a schedule), Cost Control (hard monthly spend limits per agent), Ticket System (full tool-call trace + append-only audit log), Governance (board-approval for new hires and strategy)
- Self-hosted; no Paperclip account required to run; MIT licensed; supports Kubernetes for hosting the agents it orchestrates

## Strengths

- "Company of agents" mental model is well-designed and more opinionated than generic orchestration platforms — good for cross-functional work (dev + marketing + ops under one goal)
- Hard budget limits per agent are unusual and practically useful; prevent runaway spend without manual monitoring
- Complete audit trail: every tool call, decision, and conversation is immutable and traceable
- Kubernetes deployment: agents can be hosted inside Kubernetes clusters, making it a meaningful differentiator from Multica (issue-tracker model, no Kubernetes hosting) for teams with existing container infrastructure

## Weaknesses / caveats

- Source is the homepage only — no benchmark data, independent reviews, or post-launch coverage; testimonials are user-curated

## Recent changes

- [2026-06-10] Fetched from homepage; product in general availability with docs, blog, and Discord

## Sources

- [Paperclip homepage](../sources/articles/papercliping.md)
