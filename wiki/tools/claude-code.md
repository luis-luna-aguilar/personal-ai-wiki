---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-04-24
sources: [claude-code-monitor, claude-code-routines, claude-code-leak-architecture, claude-computer-use-late-march, anthropic-desktop-agent-expansion-late-march, coding-agents-review-and-orchestration-march, claude-code-scheduled-tasks-march, anthropic-persistent-workflow-surfaces-february, memory-vs-context-rot-february, thecode-april-22-2026, claude-code-worktree-autofix, claude-code-ultrareview, claude-code-one-time-scheduling]
---

# Claude Code

Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls, and is expanding toward supervised multi-session workflows.

## Current status (as of 2026-04-21)

- Terminal CLI agent with persistent project context via `CLAUDE.md`
- Late-February expanded Claude Code's persistence story further: auto-memory writes project-local `MEMORY.md` plus topic files, while Boris Cherny previewed `/batch` and `/simplify` as built-in commands for parallel migrations and post-change cleanup
- Auto-memory improved project-local recall, but the broader source cycle also introduced the counterpoint that persistent context can decay through stale preferences and contradictory accumulated instructions if it is not inspectable and prunable
- Early March introduced two practical automation primitives before the later routines/platform push: local scheduled tasks on desktop and `/loop`, a recurring-prompt command that could keep watching PRs, Slack notifications, or other long-running work for up to three days
- Supports subagents, hooks, and background/event-driven flows
- March 2026 already hinted at the later supervision direction: Code Review introduced a managed multi-agent PR-review system on Anthropic infrastructure, while `/btw` enabled side-chain conversations during active work instead of forcing users to interrupt the main thread
- Late-March rollout introduced cloud-following workflows from web/mobile sessions for PR auto-fix and comment-resolution tasks, a useful precursor to the later routines / multi-session-supervision story
- Claude Code Channels extended that direction: existing sessions could be messaged from Telegram or Discord, making the coding agent reachable from the phone without turning it into a separate product
- Monitor tool wakes the agent on external events instead of token-expensive polling
- Recurring tasks, announced alongside Channels, reinforced the shift from one-off terminal loops toward repeatable delegated workflows
- Routines let a workflow run on a schedule, from an API call, or in response to an event on Anthropic's infrastructure
- One-time scheduling is now available from the CLI and Routines UI via `Schedule -> Once`, extending the existing recurring-work story into delayed single-run tasks
- The early-April source leak made the product's underlying architecture more legible: layered memory, repo-state awareness, explicit permission modes, and cache-friendly subagent parallelism appear to be core design choices rather than implementation accidents
- Desktop redesign pushes the product toward multi-session supervision rather than a single terminal loop
- `/recap`: auto-generates a one-line summary of the last session after 3+ turns of inactivity — triggered only once per gap, never back-to-back, also available on demand via `/recap`
- `/fewer-permission-prompts` skill (Boris Cherny): scans session history to identify safe bash and MCP commands that repeatedly trigger permission prompts, then produces an allowlist to approve them once permanently; best run after a few days of work so there's enough history to pull from

- Built-in `--worktree` flag: run `claude --worktree` to give each Claude Code session its own isolated git worktree, enabling multiple agents to work in parallel without interfering with each other's file changes; Boris Cherny (Claude Code creator) announced; Matt Pocock calls it "my new default"
- `/autofix-pr` now triggerable from CLI: run `/autofix-pr` after finishing a PR, and it sends your session to the cloud so the PR autofixer has full context to address CI failures and reviewer comments
- Remote Control: `claude remote-control` spawns a new local Claude Code session from the mobile app (available on Max, Team, and Enterprise plans at version ≥2.1.74); lets you kick off sessions from your phone

## Monitor tool

The Monitor tool (announced 2026-04-10) lets Claude Code create background scripts that run independently and wake the agent only when a relevant event occurs. This replaces token-expensive polling loops with event-driven triggers. The agent can set monitors for:

- Dev server errors or crashes
- Test suite failures
- PR status changes (via script)
- Production launch health over extended periods

## Routines

Routines extend Claude Code from local terminal sessions into repeatable hosted workflows. A routine packages a prompt, repo, and connectors into a workflow that can run on a schedule, from an API call, or in response to an event on Anthropic's infrastructure.

## /ultrareview

Cloud multi-agent code review, introduced in v2.1.86 as a research preview. Unlike `/review` (single-pass, seconds, runs locally), ultrareview launches a fleet of reviewer agents in a remote sandbox that independently reproduces and verifies each finding before reporting it — so results focus on real bugs rather than style suggestions.

- Runs entirely in a remote cloud sandbox; terminal stays free while it runs
- Many reviewer agents explore the change in parallel, surfacing issues a single-pass review would miss
- Runs as a background task (~5-10 minutes); findings appear as a notification in your session
- Can review the diff between your current branch and the default branch (including uncommitted and staged changes), or a GitHub PR by number (`/ultrareview <PR-number>`)
- Requires authentication with a Claude.ai account — not available with API key only, and not available on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry
- Not available to organizations with Zero Data Retention enabled

**Pricing:**
| Plan | Included free runs | After free runs |
| --- | --- | --- |
| Pro | 3 free through May 5, 2026 | billed as extra usage |
| Max | 3 free through May 5, 2026 | billed as extra usage |
| Team and Enterprise | none | billed as extra usage |

Paid reviews typically cost $5–$20 depending on change size. Extra usage must be enabled on the account before launching a paid review; run `/extra-usage` to check or enable it. Use `/tasks` to monitor or stop a running review.

Use `/review` for fast feedback while iterating. Use `/ultrareview` before merging a substantial change when you want a deeper pass with independent verification.

## Architecture lessons from the leak

The April 1, 2026 Claude Code leak clarified what Anthropic had already decided mattered in frontier coding agents. The repeated takeaways across technical summaries were consistent: durable context is layered instead of dumped into one giant prompt; repo state and recent work are treated as first-class context; permission boundaries are explicit; and subagents are structured to reuse context efficiently instead of re-paying setup cost from scratch.

That matters because it shifts the product story away from "Anthropic has a strong coding model" toward "Anthropic has a strong coding-agent harness." The durable edge looks increasingly architectural rather than purely model-level.

## Strengths

- Terminal-native — fits into existing shell workflows
- Event-driven monitoring reduces token waste vs polling
- Routines add a path from one-off sessions to repeatable automation
- Extensible via hooks, MCPs, skills, and subagents

## Weaknesses / caveats

- Requires comfort with CLI workflows
- Product surface is broadening beyond a single terminal loop, so the clearest long-term interaction model is still evolving

## Recent changes

- [2026-04-24] Added one-time scheduling from CLI / Routines UI via `Schedule -> Once`, extending Claude Code's scheduled-workflow support beyond recurring runs
- [2026-04-23] /ultrareview added (v2.1.86+, research preview): cloud multi-agent code review with independent finding verification; 5-10 min background; 3 free runs for Pro/Max through May 5, 2026; then $5-20 extra usage; requires Claude.ai login; not on Bedrock/Vertex AI/Foundry
- [2026-04-22] Added --worktree flag (built-in parallel isolated git worktrees), /autofix-pr CLI trigger, and Remote Control mobile session spawning
- [2026-04-22] Added /recap (session gap summaries after inactivity) and /fewer-permission-prompts skill (history-based allowlist generator)
- [2026-02-27] Claude Code added auto-memory for project-local recall of commands, preferences, and architecture context
- [2026-02-28] Boris previewed `/batch` and `/simplify` as built-in primitives for parallel migrations and automated cleanup
- [2026-03-07] Claude Code added local scheduled tasks plus `/loop`, giving the terminal agent an explicit recurring-work primitive before the later hosted-routines layer
- [2026-04-21] Added late-March Channels / recurring-tasks context: phone-triggered continuation and scheduled workflows strengthen the multi-session supervision direction
- [2026-04-21] Added architecture note from the early-April leak cluster: layered memory, repo-state injection, explicit permissions, and cache-efficient subagent parallelism now read as core Claude Code design choices
- [2026-04-21] Routines announced — scheduled / event-driven Claude Code workflows on Anthropic-hosted infrastructure
- [2026-04-10] Monitor tool announced — event-driven background scripts for Claude Code
- [2026-03-10] Code Review and `/btw` made verified PR review plus side-thread supervision first-class parts of the Claude Code workflow
- [2026-03-27] Claude Code gained unattended cloud-following workflows from web/mobile sessions for PR fixes and comment resolution

## Sources

- [[sources/articles/claude-code-monitor]]
- [[sources/tweets/claude-code-routines]]
- [[sources/newsletters/claude-code-leak-architecture]]
- [[sources/newsletters/claude-computer-use-late-march]]
- [[sources/newsletters/anthropic-desktop-agent-expansion-late-march]]
- [[sources/newsletters/coding-agents-review-and-orchestration-march]]
- [[sources/newsletters/claude-code-scheduled-tasks-march]]
- [[sources/newsletters/anthropic-persistent-workflow-surfaces-february]]
- [[sources/newsletters/memory-vs-context-rot-february]]
- [[sources/newsletters/thecode-april-22-2026]]
- [[sources/tweets/claude-code-worktree-autofix]]
- [[sources/tweets/claude-code-one-time-scheduling]]
