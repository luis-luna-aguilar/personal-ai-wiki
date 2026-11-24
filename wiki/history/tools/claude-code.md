# Claude Code History

Older recent-change entries spilled from [Claude Code](../../tools/claude-code.md).

## Archived from current page on 2026-09-09

- [2026-05-19] Paid plan limits doubled following the SpaceX/Colossus 1 compute deal (220K+ NVIDIA GPUs)
- [2026-05-19] Claude Console added prompt cache diagnostics (hit/miss rates per session) for debugging context reuse and cost in multi-agent setups

## Archived from current page on 2026-09-07

- [2026-05-18] Anthropic engineering best practices: context window as #1 constraint; verification-criteria pattern; explore-plan-code workflow (plan mode + Ctrl+G); Chrome extension for UI screenshot verification

## Archived from current page on 2026-09-06

- [2026-05-13] Agent View added (research preview, v2.1.139+): `claude agents` supervises background sessions with peek/reply, attach/detach, `/bg`, `--bg`, and worktree isolation.

## Archived from current page on 2026-09-05

- [2026-05-13] Opus 4.7 fast mode added (research preview): 2.5× faster, ~6× cost per Cursor benchmarks; new latency/price tier

## Archived from current page on 2026-09-06

- [2026-05-13] /goal command added (research preview): autonomous loop until evaluator model confirms target met — first native long-horizon success-criterion primitive in Claude Code

## Recent changes

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

## Archived from current page on 2026-05-19

- [2026-05-01] Claude Code as a product-management environment: Every profiles PM workflows inside Claude Code — roadmaps, PRDs, tickets, strategy docs, GitHub Projects tracking, and Compound Engineering skills; extends the tool beyond engineering into product operations
- [2026-04-24] Added one-time scheduling from CLI / Routines UI via `Schedule -> Once`, extending Claude Code's scheduled-workflow support beyond recurring runs
- [2026-04-23] /ultrareview added (v2.1.86+, research preview): cloud multi-agent code review with independent finding verification; 5-10 min background; 3 free runs for Pro/Max through May 5, 2026; then $5-20 extra usage; requires Claude.ai login; not on Bedrock/Vertex AI/Foundry
- [2026-04-22] Added --worktree flag (built-in parallel isolated git worktrees), /autofix-pr CLI trigger, and Remote Control mobile session spawning

## Archived from current page on 2026-10-21

- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify (with adversarial agents), and iterate to convergence on hours-to-days work; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens.
- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics
- [2026-06-18] Every case studies show Dynamic Workflows replacing manual subagent coordination for reviewer agents and large Figma-to-code work.

## Archived from current page on 2026-11-23

- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
- [2026-07-01] Every frames Claude Code alongside Codex as a general-purpose agent harness spilling beyond software work when tasks can be represented as files, tools, and review artifacts.
- [2026-07-08] Claude Code and Claude Design add bidirectional `/design-sync` between repo work and Claude Design canvases.

## Archived from current page on 2026-11-24

- [2026-07-14] Anthropic countered OpenAI's Codex/ChatGPT merge week with a Claude Code in-app browser, a third extension of Fable 5's promotional access (through July 19) with 50%-higher Claude Code limits, and a Chat+Cowork "home" tab merge.
- [2026-07-17] `/code-review` gains configurable effort levels (low: fast single pass; high: sub-agents verify every finding), replacing the previous single fixed prompt.
- [2026-08-08] Cross-session messaging shipped (one session summarizes to another on a different machine); auto mode becomes the default permission mode for Pro/Max/Team, gated by a classifier Anthropic says caught 89% of dangerous commands vs. 14% for manual approval; also added session budgets, automatic repo-skill loading, and mid-session advisor models.
