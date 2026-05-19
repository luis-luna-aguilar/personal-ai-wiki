---
type: proposal
source: raw/repos/multica-ai-multica.md
status: pending
created: 2026-05-18
---

# Proposal: Multica — open-source managed agents platform

## Summary

Multica is an open-source platform that turns coding agents (Claude Code, Codex, GitHub Copilot CLI, and nine others) into project-board teammates. Assign issues to an agent like you'd assign to a human colleague; the agent claims the task, executes it on a local or cloud runtime, posts comments, reports blockers, and compounds solutions into reusable skills. A Squads abstraction adds leader-agent delegation for stable routing across groups.

## Intended changes

- [x] **Create** `wiki/tools/multica.md` — new tool page
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add Multica to Agent orchestration section; add Recent changes entry
    > **Add to "Agent orchestration" section:**
    > `- [Multica](../tools/multica.md) — open-source; vendor-neutral managed agents platform; assign GitHub-style issues to agent CLIs (Claude Code, Codex, Copilot, and 8 others); Squads for leader-delegated routing; reusable skill compounding *(as of 2026-05-18)*`
    >
    > **Add to "Recent changes":**
    > `- [2026-05-18] Multica launches as open-source managed-agents platform: agents are first-class project-board members, not just CLI tools; Squads abstraction routes work through a leader agent; skills compound across sessions`

- [x] **Create** `wiki/sources/repos/multica-ai-multica.md` — source summary
    > See draft below

## Page drafts

### wiki/tools/multica.md (new)

```markdown
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

- [Multica GitHub repository](../sources/repos/multica-ai-multica.md)
```

### wiki/sources/repos/multica-ai-multica.md (new)

```markdown
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
```

## Open questions

- None — source is a well-structured README with enough detail to produce a clean page.
