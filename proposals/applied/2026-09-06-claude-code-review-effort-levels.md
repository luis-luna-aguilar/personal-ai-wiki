---
type: proposal
source: raw/newsletters/2026-07-17-chinese-model-rivals-fable-gpt-56.md
status: pending
created: 2026-09-06
---

# Proposal: Claude Code adds tiered effort levels to /code-review

## Summary

### The source
The Code newsletter (2026-07-17) reports Anthropic rolled out configurable effort levels for Claude Code's `/code-review` command. Previously the command ran one fixed prompt regardless of context. Now low effort runs a fast single pass meant to run before every push, while high effort spins up sub-agents that verify every individual finding. Anthropic says even the lowest tier outperforms rival code-review tools. The newsletter's coverage is a short product blurb — version number and exact rollout date beyond "2026-07-17" aren't given.

### What changes
`Claude Code`'s page already documents `/code-review` only implicitly, as part of its general command set — this is the first explicit entry for the command's effort-tiering.

- **Claude Code** gains a Current-status bullet describing the new low/high effort tiers for `/code-review`, plus a Recent-changes entry dated 2026-07-17. The page is at its 10-entry cap, so the oldest entry ([2026-05-13] /goal command) spills to `wiki/history/tools/claude-code.md`.
- New source page for this newsletter.

### What to weigh
Nothing beyond the sourcing noted above — this is a straightforward, well-attributed product update.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/claude-code.md` — adds a Current-status bullet on `/code-review` effort levels, adds one Recent-changes entry dated 2026-07-17, spills the oldest Recent-changes entry to history
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/thecode-claude-code-effort-levels-2026-07-17.md` — source summary

## Page drafts

### wiki/tools/claude-code.md (updated)

```md
- **Countermoves during OpenAI's GPT-5.6/Codex launch week (July 2026):** Anthropic reset Claude's 5-hour and weekly usage allowances, extended Claude Fable 5's promotional access on paid plans three times in ten days (July 7 → 12 → 19) while keeping Claude Code's weekly limits 50% higher than standard throughout the extension, added an in-app browser to Claude Code desktop so it can pull up docs and designs without leaving the terminal, and merged Chat and Cowork into a single "home" tab.
- `/code-review` now has configurable effort levels: low effort runs one fast pass suitable before every push, high effort spins up sub-agents that verify every individual finding; previously the command ran a single fixed prompt regardless of context. Anthropic says even the lowest tier outperforms rival review tools.
```

```md
## Recent changes

- [2026-07-17] `/code-review` gains configurable effort levels (low: fast single pass; high: sub-agents verify every finding), replacing the previous single fixed prompt.
- [2026-07-14] Anthropic countered OpenAI's Codex/ChatGPT merge week with a Claude Code in-app browser, a third extension of Fable 5's promotional access (through July 19) with 50%-higher Claude Code limits, and a Chat+Cowork "home" tab merge.
- [2026-07-08] Claude Code and Claude Design add bidirectional `/design-sync` between repo work and Claude Design canvases.
- [2026-07-01] Every frames Claude Code alongside Codex as a general-purpose agent harness spilling beyond software work when tasks can be represented as files, tools, and review artifacts.
- [2026-06-30] Anthropic published the official Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops, with guidance on matching loop primitive to task type and controlling token usage.
- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
- [2026-06-18] Every case studies show Dynamic Workflows replacing manual subagent coordination for reviewer agents and large Figma-to-code work.
- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify (with adversarial agents), and iterate to convergence on hours-to-days work; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens.
- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics
- [2026-05-18] Anthropic engineering best practices: context window as #1 constraint; verification-criteria pattern; explore-plan-code workflow (plan mode + Ctrl+G); Chrome extension for UI screenshot verification
```

Note this drops the current 10th entry ([2026-05-13] /goal command) to spill it; if a sibling proposal has already changed what's oldest by apply time, spill whatever is actually oldest instead.

Add `thecode-claude-code-effort-levels-2026-07-17` to the frontmatter `sources:` list.

### wiki/sources/newsletters/thecode-claude-code-effort-levels-2026-07-17.md (new)

```md
---
title: "Moonshot drops Kimi K3, Claude Code ships effort levels for /code-review"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-17-chinese-model-rivals-fable-gpt-56.md
url: https://codenewsletter.ai/p/moonshot-drops-kimi-k3-claude-code-ships-effort-levels-for-code-review
published: 2026-07-17
ingested: 2026-09-06
domains: [coding]
---

# Moonshot drops Kimi K3, Claude Code ships effort levels for /code-review

The Code newsletter (2026-07-17) reports Anthropic added configurable effort levels to Claude Code's `/code-review` command: low effort for a fast pre-push pass, high effort for sub-agent-verified findings. Anthropic says even the lowest tier beats rival review tools. (The newsletter's other lead story, Kimi K3, is covered by a separate proposal and source page.)

## Influenced pages
- [Claude Code](../../tools/claude-code.md) — Current-status bullet and Recent-changes entry for `/code-review` effort levels

## Key claims extracted
- `/code-review` previously ran one fixed prompt regardless of context
- Low effort: fast single pass, suitable before every push
- High effort: spins up sub-agents to verify every individual finding
- Anthropic claims even the lowest tier outperforms rival code-review tools
```

## Schema / vocabulary additions

None.

## Open questions

None.
