---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-04-21
sources: [claude-code-monitor, claude-code-routines, claude-code-leak-architecture, claude-computer-use-late-march]
---

# Claude Code

Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls, and is expanding toward supervised multi-session workflows.

## Current status (as of 2026-04-21)

- Terminal CLI agent with persistent project context via `CLAUDE.md`
- Supports subagents, hooks, and background/event-driven flows
- Late-March rollout introduced cloud-following workflows from web/mobile sessions for PR auto-fix and comment-resolution tasks, a useful precursor to the later routines / multi-session-supervision story
- Monitor tool wakes the agent on external events instead of token-expensive polling
- Routines let a workflow run on a schedule, from an API call, or in response to an event on Anthropic's infrastructure
- The early-April source leak made the product's underlying architecture more legible: layered memory, repo-state awareness, explicit permission modes, and cache-friendly subagent parallelism appear to be core design choices rather than implementation accidents
- Desktop redesign pushes the product toward multi-session supervision rather than a single terminal loop

## Monitor tool

The Monitor tool (announced 2026-04-10) lets Claude Code create background scripts that run independently and wake the agent only when a relevant event occurs. This replaces token-expensive polling loops with event-driven triggers. The agent can set monitors for:

- Dev server errors or crashes
- Test suite failures
- PR status changes (via script)
- Production launch health over extended periods

## Routines

Routines extend Claude Code from local terminal sessions into repeatable hosted workflows. A routine packages a prompt, repo, and connectors into a workflow that can run on a schedule, from an API call, or in response to an event on Anthropic's infrastructure.

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

- [2026-04-21] Added architecture note from the early-April leak cluster: layered memory, repo-state injection, explicit permissions, and cache-efficient subagent parallelism now read as core Claude Code design choices
- [2026-04-21] Routines announced — scheduled / event-driven Claude Code workflows on Anthropic-hosted infrastructure
- [2026-04-10] Monitor tool announced — event-driven background scripts for Claude Code
- [2026-03-27] Claude Code gained unattended cloud-following workflows from web/mobile sessions for PR fixes and comment resolution

## Sources

- [[sources/articles/claude-code-monitor]]
- [[sources/tweets/claude-code-routines]]
- [[sources/newsletters/claude-code-leak-architecture]]
- [[sources/newsletters/claude-computer-use-late-march]]
