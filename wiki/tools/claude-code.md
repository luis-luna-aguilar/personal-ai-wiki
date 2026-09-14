---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-08-08
sources: [claude-code-monitor, claude-code-routines, claude-code-leak-architecture, claude-computer-use-late-march, anthropic-desktop-agent-expansion-late-march, coding-agents-review-and-orchestration-march, claude-code-scheduled-tasks-march, anthropic-persistent-workflow-surfaces-february, memory-vs-context-rot-february, thecode-april-22-2026, claude-code-worktree-autofix, claude-code-ultrareview, claude-code-one-time-scheduling, claude-code-product-management-2026-05-01, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, agent-native-product-management-2026-05-13, anthropic-claude-code-best-practices-2026-05, claude-code-fast-mode-default-2026-05, dynamic-workflows-claude-code, claude-code-getting-started-with-loops-2026-06-30, codex-general-work-agents-2026-07, ainews-opus-48-dynamic-workflows-2026-05, every-claude-dynamic-workflows-reliability-2026-06, claude-code-design-sync-2026-07, claude-sonnet-5-official-2026-06-30, every-urge-to-merge-2026-07-14, thecode-claude-code-effort-levels-2026-07-17, zawinskis-law-multiagents-2026-08-08, every-copilot-studio-microsoft-2026-08-03]
---

# Claude Code

Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls, and is expanding toward supervised multi-session workflows; users increasingly treat it as a general-purpose agent harness for product, research, and operational work when those workflows can be represented as files, commands, skills, and review artifacts.

## Current status (as of 2026-08-08)

- Terminal CLI agent with persistent project context via `CLAUDE.md` and project-local auto-memory (`MEMORY.md` plus topic files); most-used AI coding tool at 63% of respondents per Pragmatic Engineer's May 2025–Feb 2026 developer survey
- Supports subagents, hooks, and background/event-driven flows; `--worktree` gives each session its own isolated git worktree for parallel work
- Current model lineup: Claude Sonnet 5 and Claude Fable 5 (restored 2026-07-02) alongside Opus 4.8, selectable via fast mode
- Remote Control (`claude remote-control`) and Agent View (`claude agents`) extend supervision to mobile and multi-session dispatch
- Auto mode is now the default permission mode for Pro/Max/Team, backed by a classifier plus per-session budgets and mid-session advisor models (see Recent changes)
- Dedicated subsystems below cover the rest: Monitor (event-driven wake), Routines (scheduled/hosted workflows), Dynamic workflows (parallel orchestration), and `/ultrareview` (cloud multi-agent review)

## Monitor tool

The Monitor tool (announced 2026-04-10) lets Claude Code create background scripts that run independently and wake the agent only when a relevant event occurs. This replaces token-expensive polling loops with event-driven triggers. The agent can set monitors for:

- Dev server errors or crashes
- Test suite failures
- PR status changes (via script)
- Production launch health over extended periods

## Routines

Routines extend Claude Code from local terminal sessions into repeatable hosted workflows. A routine packages a prompt, repo, and connectors into a workflow that can run on a schedule, from an API call, or in response to an event on Anthropic's infrastructure.

## Dynamic workflows

Dynamic workflows (research preview, announced 2026-05-28) let Claude **dynamically write orchestration scripts** that run tens to hundreds of parallel subagents in a single session. Claude plans the task, breaks it into subtasks, fans them out, and verifies each result before folding it back in — agents attack the problem from independent angles while other agents try to refute their findings, and the run iterates until the answers converge, reaching results a single pass cannot.

- **Built for long-running, parallel work** — runs extend into hours or days, doing complex engineering work that previously took weeks.
- **Durable by default** — progress is checkpointed as the run proceeds, so an interrupted job resumes where it left off; coordination lives outside the conversation, so the plan stays on track as the task grows.
- **Typical use cases** — codebase-wide bug hunts, profiler-guided optimization audits, security/hardening passes, large migrations and language ports across thousands of files, and high-stakes work you want independently double-checked.
- **How to run** — turn on auto mode, then either ask Claude to "create a workflow" or enable the `ultracode` setting from the effort menu (sets effort to xhigh and lets Claude decide when a workflow is warranted).
- **Higher cost** — consumes substantially more tokens than a typical session; the first time a workflow triggers, Claude Code shows what is about to run and asks for confirmation. Org admins can disable workflows via managed settings.
- **Availability** — research preview in the Claude Code CLI, Desktop, and VS Code extension, and on the Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry. On by default for Max and Team (and the API); off by default for Enterprise at launch (admin can enable in settings).

- **Reliability pattern:** Every's June 18 case study frames Dynamic Workflows as the productized version of manually coordinating a lead agent plus reviewer subagents — Claude writes an orchestration script that instantiates subagents and verification steps instead of hoping a prompt reproduces that structure. Every also used it to split a large Figma redesign into 11 sections across dedicated subagents (extract, generate, compare to source).
- **Claude Design sync:** Claude Code and Claude Design now sync both directions through `/design-sync` — pull a design system into the repo, or push built work back into a Claude Design canvas.

**Flagship example — Bun rewrite:** Jarred Sumner used dynamic workflows to port Bun from Zig to Rust (~750,000 lines, 99.8% of the test suite passing, 11 days first-commit-to-merge): one workflow mapped Rust lifetimes per struct field, the next ported each file with hundreds of parallel agents and two reviewers each, then a fix loop and an overnight cleanup pass closed it out. (Not yet in production.)

## Loop taxonomy

Anthropic's June 30, 2026 "Getting started with loops" post defines a loop as an agent repeating cycles of work until a stop condition is met. The Claude Code team frames four levels:

| Loop type | Trigger | Stop condition | Claude Code primitive | Best fit |
| --- | --- | --- | --- | --- |
| Turn-based | User prompt | Claude judges the task done or asks for context | Normal prompt + verification skills | Short exploratory tasks |
| Goal-based | Manual prompt in real time | Goal achieved or turn cap hit | `/goal` | Tasks with deterministic exit criteria |
| Time-based | Interval or schedule | Cancelled, or external work completes | `/loop`, `/schedule` | Recurring checks, PR/CI monitoring, scheduled summaries |
| Proactive | Event or schedule, no human present | Each task exits when its goal is met; routine keeps running | `/schedule`, `/goal`, skills, dynamic workflows, auto mode | Recurring streams of well-defined work such as bug reports, triage, migrations, dependency upgrades |

The practical guidance is conservative: start with the simplest loop, define explicit success and stop criteria, pilot before large dynamic-workflow runs, use scripts for deterministic work, and review `/usage`, `/goal`, and `/workflows` token breakdowns to manage cost.

For code quality, Anthropic recommends encoding verification steps as skills, keeping project conventions clean, making docs easy to reach, and using a second agent or `/code-review` skill for review rather than letting the generator fully evaluate its own work.

## Best practices (Anthropic engineering)

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

**Pricing:** billed as extra usage, typically $5–$20 per run depending on change size; enable it via `/extra-usage`. Pro and Max got 3 free runs through May 5, 2026; Team and Enterprise never had a free tier. Use `/tasks` to monitor or stop a running review.

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

- Persistent context (auto-memory, `CLAUDE.md`) can decay through stale preferences and contradictory accumulated instructions if it is not inspectable and prunable
- Requires comfort with CLI workflows
- Product surface is broadening beyond a single terminal loop, so the clearest long-term interaction model is still evolving
- As Claude Code broadens into goals, background sessions, remote control, worktrees, and product-management workflows, the product is increasingly a workflow container; the risk is surface sprawl unless teams standardize commands, skills, and review habits.

## Recent changes

- [2026-08-08] Cross-session messaging shipped (one session summarizes to another on a different machine); auto mode becomes the default permission mode for Pro/Max/Team, gated by a classifier Anthropic says caught 89% of dangerous commands vs. 14% for manual approval; also added session budgets, automatic repo-skill loading, and mid-session advisor models.
- [2026-07-17] `/code-review` gains configurable effort levels (low: fast single pass; high: sub-agents verify every finding), replacing the previous single fixed prompt.
- [2026-07-14] Anthropic countered OpenAI's Codex/ChatGPT merge week with a Claude Code in-app browser, a third extension of Fable 5's promotional access (through July 19) with 50%-higher Claude Code limits, and a Chat+Cowork "home" tab merge.
- [2026-07-08] Claude Code and Claude Design add bidirectional `/design-sync` between repo work and Claude Design canvases.
- [2026-07-01] Every frames Claude Code alongside Codex as a general-purpose agent harness spilling beyond software work when tasks can be represented as files, tools, and review artifacts.
- [2026-06-30] Anthropic published the official Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops, with guidance on matching loop primitive to task type and controlling token usage.
- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
- [2026-06-18] Every case studies show Dynamic Workflows replacing manual subagent coordination for reviewer agents and large Figma-to-code work.
- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify (with adversarial agents), and iterate to convergence on hours-to-days work; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens.
- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics

## Sources

- [Claude Code Monitor tool announcement](../sources/tweets/claude-code-monitor.md)
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
- [Introducing dynamic workflows in Claude Code](../sources/articles/dynamic-workflows-claude-code.md)
- [Getting started with loops](../sources/articles/claude-code-getting-started-with-loops-2026-06-30.md)
- [Codex and Claude Code as general-purpose work agents](../sources/newsletters/codex-general-work-agents-2026-07.md)
- [AINews - Anthropic raises Series H, releases Opus 4.8 and Dynamic Workflows](../sources/newsletters/ainews-opus-48-dynamic-workflows-2026-05.md)
- [Every - How Anthropic makes Claude more reliable](../sources/newsletters/every-claude-dynamic-workflows-reliability-2026-06.md)
- [Claude Code and Claude Design sync](../sources/tweets/claude-code-design-sync-2026-07.md)
- [Claude Sonnet 5 — official launch](../sources/articles/claude-sonnet-5-official-2026-06-30.md)
- [Every — The Urge to Merge (ChatGPT and Codex)](../sources/newsletters/every-urge-to-merge-2026-07-14.md)
- [The Code — Moonshot drops Kimi K3, Claude Code ships effort levels for /code-review](../sources/newsletters/thecode-claude-code-effort-levels-2026-07-17.md)
- [AINews — Zawinski's Law of MultiAgents](../sources/newsletters/zawinskis-law-multiagents-2026-08-08.md)
- [Every — The Best AI Agent Builder Is Trapped Inside Microsoft](../sources/newsletters/every-copilot-studio-microsoft-2026-08-03.md)
