---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-11-23
sources: [claude-code-monitor, claude-code-routines, claude-code-leak-architecture, claude-computer-use-late-march, anthropic-desktop-agent-expansion-late-march, coding-agents-review-and-orchestration-march, claude-code-scheduled-tasks-march, anthropic-persistent-workflow-surfaces-february, memory-vs-context-rot-february, thecode-april-22-2026, claude-code-worktree-autofix, claude-code-ultrareview, claude-code-one-time-scheduling, claude-code-product-management-2026-05-01, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, agent-native-product-management-2026-05-13, claude-code-fast-mode-default-2026-05, dynamic-workflows-claude-code, claude-code-getting-started-with-loops-2026-06-30, codex-general-work-agents-2026-07, ainews-opus-48-dynamic-workflows-2026-05, every-claude-dynamic-workflows-reliability-2026-06, claude-code-design-sync-2026-07, claude-sonnet-5-official-2026-06-30, every-urge-to-merge-2026-07-14, thecode-claude-code-effort-levels-2026-07-17, zawinskis-law-multiagents-2026-08-08, every-copilot-studio-microsoft-2026-08-03, claude-security-product-page, latent-space-thariq-claude-code-next-era-2026-09-29, claudedevs-cloud-sessions-ga-2026-09-23, ainews-claude-code-cloud-sessions-projects-2026-09-24, claude-projects-redesigned-2026-09-17, claudeai-projects-one-conversation-2026-09-17, emollick-claude-projects-mysteries-2026-09-17, tamaratran-fast-jev-compaction, claude-ship-launch-2026-11-23, ainews-claude-code-agents-md-2026-09-19, latent-space-claude-mods-2026-10-21, claudedevs-code-mode-2026-11-17]
---

# Claude Code

Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls, and is expanding toward supervised multi-session workflows; users increasingly treat it as a general-purpose agent harness for product, research, and operational work when those workflows can be represented as files, commands, skills, and review artifacts.

## Current status (as of 2026-11-17)

- Terminal CLI agent with persistent project context via `CLAUDE.md` (or `AGENTS.md` when no CLAUDE.md exists) and project-local auto-memory (`MEMORY.md` plus topic files); most-used AI coding tool at 63% of respondents per Pragmatic Engineer's May 2025–Feb 2026 developer survey
- Supports subagents, hooks, and background/event-driven flows; `--worktree` gives each session its own isolated git worktree for parallel work
- Current model lineup: Claude Sonnet 5 and Claude Fable 5 (restored 2026-07-02) alongside Opus 4.8, selectable via fast mode
- Remote Control (`claude remote-control`) and Agent View (`claude agents`) extend supervision to mobile and multi-session dispatch; cloud sessions (GA 2026-09-23) keep work running on Anthropic's infrastructure with the laptop closed
- Auto mode is now the default permission mode for Pro/Max/Team, backed by a classifier plus per-session budgets and mid-session advisor models
- Dedicated subsystems below cover the rest: Monitor (event-driven wake), Routines (scheduled/hosted workflows), Dynamic workflows (parallel orchestration), and `/ultrareview` (cloud multi-agent review, detailed on [Claude Code practices](../workflows/claude-code-practices.md))
- **Code Mode (experimental, 2026-11-17):** Claude writes one script that chains its tool calls instead of one call per round trip, and can answer while long commands still run. Opt in with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1` (v2.1.323+); compare `/cost` with it off and on. The general pattern is on [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md).

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

Anthropic's turn-based / goal-based / time-based / proactive loop taxonomy maps onto Claude Code primitives (normal prompts, `/goal`, `/loop`, `/schedule`, routines); the table and guidance live on [Agent loop design](../workflows/agent-loop-design.md).

## Mods, Projects, and cloud sessions

- **Cloud sessions (GA 2026-09-23):** start from claude.ai/code, the mobile Code tab, the desktop app, or `claude --cloud`; GitHub connection required; billed to normal plan usage, with a one-time promotional credit ($100 Pro, $250 Max) spent first.
- **Projects:** a coordinator chat that routes a goal to parallel threads, each a cloud session on its own branch, with shared project memory and a library (beta since 2026-09-17). Details on [Claude Code Projects](claude-code-projects.md).
- **Claude Mods:** in-process function hooks (early access from 2.1.274) that let plugins observe and change prompts, tool calls and the UI. Anthropic now ships parts of Claude Code itself as built-in mods, the AGENTS.md loader among them, and mods are not sandboxed. The mechanics, the built-in list, token costs and the trust caveat are on [Claude Code Mods](claude-code-mods.md).
- **Direction:** "cloud brain, local hands" — one cloud-resident agent that works in cloud sandboxes or on your machine when it is online (see [Agent runtime platforms](../concepts/agent-runtime-platforms.md)).
- **CLAUDE.md:** Thariq Shihipar expects it to disappear in the limit and suggests starting new projects without one, adding only repeated failure modes, since those are model-specific. Since v2.1.277 (September 2026) Claude Code reads AGENTS.md when no CLAUDE.md is present, with a config toggle, which removes shim files that only point one format at the other; the built-in `agents-md` mod ([Claude Code Mods](claude-code-mods.md)) now does the loading.

## Best practices (Anthropic engineering)

Context-window management, verification criteria, the explore-plan-code workflow, and UI verification now live on [Claude Code practices](../workflows/claude-code-practices.md).

## /ultrareview

Cloud multi-agent code review (research preview since v2.1.86, $5–$20 per run as extra usage); details and when to use it over `/review` are on [Claude Code practices](../workflows/claude-code-practices.md).

## Claude Ship (/ship)

`/ship` (beta, 2026-11-23) hands a finished change to [Claude Ship](claude-ship.md): Claude pushes it, opens the PR, reviews it, and works on feedback and failing checks until it is ready to merge, within the developer's permissions and the repository's branch rules.

## Claude Security

Anthropic's security-review product, in public beta for Claude Enterprise per Anthropic's product page: it scans a codebase with Anthropic's most capable models, now including Claude Mythos 5.2 (as of 2026-11-09; earlier Mythos 5.1, not Opus 4.7 as early secondary coverage reported), traces data flows across files, adversarially self-verifies each finding, and proposes a reviewable patch per finding. A Claude Code plugin, also in beta, runs the same pipeline locally. *(as of 2026-09-09)*

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

- [2026-11-24] Split: Claude Mods (function hooks, built-in mods, the unsandboxed-mods caveat) moved to [Claude Code Mods](claude-code-mods.md) and Projects to [Claude Code Projects](claude-code-projects.md); short pointers remain.
- [2026-11-23] `/ship` command added (beta): pushes the change, opens the PR, and hands it to [Claude Ship](claude-ship.md) for review, fixes, and an approval decision.
- [2026-11-17] Experimental Code Mode (`CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1`): Claude chains tool calls in one script and can reply while long commands run.
- [2026-10-21] Split: the "Best practices (Anthropic engineering)" and "/ultrareview" sections moved to [Claude Code practices](../workflows/claude-code-practices.md); one-line pointers remain.
- [2026-10-19] Split: the loop-taxonomy table and loop guidance moved to [Agent loop design](../workflows/agent-loop-design.md) (one-line pointer remains); Claude Security detail (Enterprise public beta on Mythos 5.1, adversarial self-verification, per-finding patches, Claude Code plugin beta, as of 2026-09-09) moved here from the [State of Cybersecurity](../state-of/cybersecurity.md) leader line.
- [2026-09-29] Thariq Shihipar (Latent Space) details Claude Mods (in-process function hooks: forked cache-sharing subagents, UI changes, composable modes), Projects, the "cloud brain, local hands" direction, and advice to start new projects without a CLAUDE.md.
- [2026-09-23] Cloud sessions left research preview (`claude --cloud`, web, mobile, desktop): work continues with the laptop closed on normal plan usage, plus a one-time $100 Pro / $250 Max credit; Projects launched alongside and now also run locally.
- [2026-09-19] v2.1.277 reads AGENTS.md when no CLAUDE.md is present, with a config toggle.

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
- [Claude Security product page](../sources/articles/claude-security-product-page.md)
- [Latent Space — Claude Code's Next Era (Thariq Shihipar)](../sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md)
- [ClaudeDevs — Cloud sessions out of research preview](../sources/tweets/claudedevs-cloud-sessions-ga-2026-09-23.md)
- [AINews — Claude Code cloud sessions GA and local Projects](../sources/newsletters/ainews-claude-code-cloud-sessions-projects-2026-09-24.md)
- [Projects redesigned: from folder to conversation](../sources/articles/claude-projects-redesigned-2026-09-17.md)
- [Claude (@claudeai) — Projects now run from one conversation](../sources/tweets/claudeai-projects-one-conversation-2026-09-17.md)
- [Ethan Mollick — Claude Projects handles teams of agents](../sources/tweets/emollick-claude-projects-mysteries-2026-09-17.md)
- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
- [Introducing Claude Ship](../sources/articles/claude-ship-launch-2026-11-23.md)
- [AINews — Claude Code reads AGENTS.md (v2.1.277)](../sources/newsletters/ainews-claude-code-agents-md-2026-09-19.md)
- [Latent Space — Claude Mods: Flipping the Harness Inside Out](../sources/newsletters/latent-space-claude-mods-2026-10-21.md)
- [ClaudeDevs — Code Mode (experimental)](../sources/tweets/claudedevs-code-mode-2026-11-17.md)
