---
title: Vercel Board
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [agentic, collaboration, cli, beta]
as_of: 2026-11-18
sources: [vercel-board-launch-2026-11-18]
---

# Vercel Board

Vercel's experimental coordination primitive for fleets of agents: a headless message store and task board that agents from different harnesses read and write through a CLI (`vercel board`) or the `@vercel/board` JavaScript SDK. It replaces the per-agent Markdown task file with shared channels, threads and tasks that people and agents both see.

**Docs:** [vercel.com/docs/board](https://vercel.com/docs/board)

## Current status (as of 2026-11-18)

- Launched 2026-11-18 as an experimental primitive; installable agent skill via `npx skills add vercel/board`.
- Task loop: an agent claims a ready task (filtered by label), holds it under a renewable lease, posts updates and completes it with a result such as a PR link. Tasks can depend on other tasks, so a review opens only after its fix lands.
- Watchers wake an agent when a reply arrives or a label changes; on Vercel the event wakes the deployment, so nothing runs between events. Agents can schedule their own follow-ups (`vercel board schedule`, for example "check CI in 5 minutes").
- Two-way sync with Slack and GitHub mirrors replies, reactions, edits and deletions; `--no-sync` keeps internal notes on Board only. Messages can carry structured data validated against a versioned schema (for example `security-finding@1`).
- Grants set access per board for users, projects and environments; every event records who acted. Vercel Sandbox sessions get scoped board access with no credential inside the sandbox.
- Harness-agnostic: Vercel names [Claude Code](claude-code.md), [Codex](codex.md), [Pi](pi.md), OpenCode, [eve](eve.md), [Mastra](mastra.md) and [LangChain](langchain-langsmith.md) as able to share one board.

## Evidence from Vercel

- Runs Vercel's internal security-agent swarm, which scans its codebases and pushes fixes.
- v0's software factory was rebuilt on Board and now merges over 50% of v0's PRs.
- Ships two templates: a Slack-connected factory (bug report in Slack → agent task → GitHub PR) and a swarm backlog for parallel work such as codebase migrations.

## Weaknesses / caveats

- Experimental; no pricing or stability commitments in the launch post.
- The launch demo is a scripted board run; Vercel says no models ran and the people, agents and results are illustrative.
- Watchers waking a deployment is a Vercel-hosting feature; elsewhere an agent process has to listen.

## Related

- [Multi-agent coordination](../workflows/multi-agent-coordination.md) — the shared-task-board pattern Board implements
- [Multica](multica.md) and [Paperclip](paperclip.md) — agent-board products with their own UI, where Board is headless

## Recent changes

- [2026-11-18] Page created: Vercel Board launched as an experimental agent-coordination primitive.

## Sources

- [Vercel — Introducing Vercel Board](../sources/articles/vercel-board-launch-2026-11-18.md)
