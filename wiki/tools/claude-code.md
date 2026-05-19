---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-05-19
sources: [claude-code-monitor, claude-code-routines, claude-code-leak-architecture, claude-computer-use-late-march, anthropic-desktop-agent-expansion-late-march, coding-agents-review-and-orchestration-march, claude-code-scheduled-tasks-march, anthropic-persistent-workflow-surfaces-february, memory-vs-context-rot-february, thecode-april-22-2026, claude-code-worktree-autofix, claude-code-ultrareview, claude-code-one-time-scheduling, claude-code-product-management-2026-05-01, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, agent-native-product-management-2026-05-13, anthropic-claude-code-best-practices-2026-05, claude-code-fast-mode-default-2026-05]
---

# Claude Code

Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls, and is expanding toward supervised multi-session workflows.

## Current status (as of 2026-05-13)

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

- Paid plan limits doubled (May 2026) following SpaceX/Colossus 1 compute deal (220K+ NVIDIA GPUs)
- Built-in `--worktree` flag: run `claude --worktree` to give each Claude Code session its own isolated git worktree, enabling multiple agents to work in parallel without interfering with each other's file changes; Boris Cherny (Claude Code creator) announced; Matt Pocock calls it "my new default"
- `/autofix-pr` now triggerable from CLI: run `/autofix-pr` after finishing a PR, and it sends your session to the cloud so the PR autofixer has full context to address CI failures and reviewer comments
- Remote Control: `claude remote-control` spawns a new local Claude Code session from the mobile app (available on Max, Team, and Enterprise plans at version ≥2.1.74); lets you kick off sessions from your phone
- `/goal` command (May 2026, research preview): set a target (e.g. "pass all tests in this folder") and Claude loops autonomously until an evaluator model confirms it is met — analogous to the `/goals` command OpenAI added to Codex; the first native long-horizon success-criterion primitive in Claude Code
- Opus 4.7 fast mode (now default, as of 2026-05-19): was research preview; now the default mode for Claude Code; Cursor reports 2.5× faster output at approximately 6× the cost compared to standard Opus 4.7
- Claude Console prompt cache diagnostics (May 2026): developers can now see cache hit/miss rates for their Claude Code sessions in Claude Console; useful for debugging context reuse and cost efficiency in multi-agent setups
- Agent View (research preview, Claude Code v2.1.139+): `claude agents` opens one terminal screen for dispatching and supervising background Claude Code sessions. Sessions are grouped by state, can be peeked/replied to without opening the full transcript, attached/detached for full conversation, and launched from Agent View, `/bg`, or `claude --bg`; editable background sessions are isolated in git worktrees under `.claude/worktrees/` when possible.
- Every's product-management guide adds command-pack examples such as strategy interviews and product-pulse reviews, reinforcing Claude Code as a product workflow surface, not only a code editor.

## Monitor tool

The Monitor tool (announced 2026-04-10) lets Claude Code create background scripts that run independently and wake the agent only when a relevant event occurs. This replaces token-expensive polling loops with event-driven triggers. The agent can set monitors for:

- Dev server errors or crashes
- Test suite failures
- PR status changes (via script)
- Production launch health over extended periods

## Routines

Routines extend Claude Code from local terminal sessions into repeatable hosted workflows. A routine packages a prompt, repo, and connectors into a workflow that can run on a schedule, from an API call, or in response to an event on Anthropic's infrastructure.

## Best practices (Anthropic engineering, May 2026)

**Context window management**
- Context window is the #1 resource; performance degrades as it fills; the custom status line tracks context usage for exactly this reason
- Start a new session when context is full rather than continuing in a degraded state

**Verification criteria**
- Always give Claude a way to verify its own work before reporting done: run the tests, take a screenshot, execute a command and check the output
- Without a verification criterion, Claude marks tasks complete based on code inspection alone — missing runtime failures

**Explore-plan-code workflow**
- Step 1 (Explore): Claude reads relevant files in plan mode — no edits permitted
- Step 2 (Plan): Claude writes a plan doc; press Ctrl+G to open it in a text editor for review and editing before any code is written
- Step 3 (Code): Claude implements against the approved plan; commits after each logical unit
- Skip plan mode for small or clearly-scoped tasks — overhead is only worth it for multi-file or uncertain-approach work

**UI verification**
- The Claude Chrome extension lets Claude take screenshots of the running app to verify visual output
- Closes the loop between a code change and the rendered result without requiring a human to look

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
- As Claude Code broadens into goals, background sessions, remote control, worktrees, and product-management workflows, the product is increasingly a workflow container; the risk is surface sprawl unless teams standardize commands, skills, and review habits.

## Recent changes

- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics
- [2026-05-18] Anthropic engineering best practices: context window as #1 constraint; verification-criteria pattern; explore-plan-code workflow (plan mode + Ctrl+G); Chrome extension for UI screenshot verification
- [2026-05-13] /goal command added (research preview): autonomous loop until evaluator model confirms target met — first native long-horizon success-criterion primitive in Claude Code
- [2026-05-13] Opus 4.7 fast mode added (research preview): 2.5× faster, ~6× cost per Cursor benchmarks; new latency/price tier
- [2026-05-13] Agent View added (research preview, v2.1.139+): `claude agents` supervises background sessions with peek/reply, attach/detach, `/bg`, `--bg`, and worktree isolation.

## Sources

- [Claude Code Monitor tool announcement](../sources/articles/claude-code-monitor.md)
- [Claude Code routines launch](../sources/tweets/claude-code-routines.md)
- [Claude Code leak architecture lessons](../sources/newsletters/claude-code-leak-architecture.md)
- [Claude computer use in late March](../sources/newsletters/claude-computer-use-late-march.md)
- [Anthropic desktop-agent expansion in late March](../sources/newsletters/anthropic-desktop-agent-expansion-late-march.md)
- [Coding agents move toward review and concurrent supervision](../sources/newsletters/coding-agents-review-and-orchestration-march.md)
- [Claude Code scheduled tasks and `/loop`](../sources/newsletters/claude-code-scheduled-tasks-march.md)
- [Anthropic persistent workflow surfaces in late February](../sources/newsletters/anthropic-persistent-workflow-surfaces-february.md)
- [Memory versus context rot in late February](../sources/newsletters/memory-vs-context-rot-february.md)
- [The Code newsletter — 2026-04-22 (Cursor/SpaceX, Claude Code recap, CLI design)](../sources/newsletters/thecode-april-22-2026.md)
- [Claude Code — worktrees, /autofix-pr CLI, Remote Control](../sources/tweets/claude-code-worktree-autofix.md)
- [Claude Code one-time scheduling](../sources/tweets/claude-code-one-time-scheduling.md)
- [Claude Code for product-management workflows](../sources/newsletters/claude-code-product-management-2026-05-01.md)
- [Claude Code /goal, fast mode, and FleetView](../sources/newsletters/claude-code-goal-fastmode-fleetview-2026-05-13.md)
- [Claude Code Agent View docs](../sources/articles/claude-code-agent-view-2026-05-13.md)
- [Agent-native product management guide - Every](../sources/articles/agent-native-product-management-2026-05-13.md)
- [Claude Code Fast mode becomes default + spec-drift logging](../sources/newsletters/claude-code-fast-mode-default-2026-05.md)
