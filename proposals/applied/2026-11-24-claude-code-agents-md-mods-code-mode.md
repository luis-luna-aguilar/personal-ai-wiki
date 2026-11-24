---
type: proposal
source: raw/newsletters/2026-10-21-claude-mods-flipping-the-harness-inside-out.md
sources:
  - raw/newsletters/2026-10-21-claude-mods-flipping-the-harness-inside-out.md
  - raw/tweets/2026-11-24-xcom-claudedevs-2122801681939234950.md
  - raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
  - raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
status: pending
created: 2026-11-24
---

# Proposal: Claude Code — AGENTS.md fallback, built-in mods, and Code Mode

## Summary

### In short
Claude Code now builds its own features as mods, the plugin layer it opened to users, and that changes what "trusting a mod" means. Six built-in mods ship with it, among them the AGENTS.md loader and an opt-in side agent called you-should-know. Mods are not sandboxed, and the built-in ones keep running under `--safe-mode`. The proposal updates **Claude Code** with the AGENTS.md fallback (replacing the stale "support is coming" line), the built-in mods, the trust caveat and experimental Code Mode, and adds three source pages. The reason to hesitate is length: the page already sits at its word ceiling and this pushes it past 110%.

[[#Open questions|Open questions: 2 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The core is a Latent Space essay from 21 October on Claude Mods. Mods are TypeScript or JavaScript functions that run inside Claude Code and react to prompts, tool calls and screen renders. The author calls them middleware that turns the harness toward the human's attention. Typing /plugin and opening Installed shows six mods Anthropic ships built in. **agents-md** loads AGENTS.md as project instructions. **diff** draws the /diff pane. **plugin-authoring** gives Claude the skill to write mods. **sec-default** guards organization-managed settings from user-installed mods. **telemetry** sends analytics. **you-should-know** is the only one off by default. It is a side agent that watches the main agent and posts a note when something important is buried in the trace. In the author's example, it noticed that about 45 files held uncommitted work that a planned discard would have destroyed. The essay also counts the costs. The author's open-source Next Steps Supervisor mod (in ModSmith) fired on 99 of 111 turns. Its README estimates 5–6k input-equivalent tokens per check on a 50k-token session. Anthropic's docs warn that a loaded mod can read and write files, see every prompt and spend your usage.

Two shorter items fill in the dates. On 19 September AINews relayed Thariq Shihipar's announcement that Claude Code v2.1.277 reads AGENTS.md when no CLAUDE.md exists, with a config toggle. Simon Willison noted this ends the need for shim files that only point one format at the other. On 17 November the ClaudeDevs account introduced Code Mode, fetched for this proposal. It is an experimental setting in which Claude writes scripts that chain tool calls together and can reply while long commands are still running. It is turned on with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1`, and a community note on a related post puts it at v2.1.323 or later. Every's newsletter suggests comparing `/cost` on one task with it off and on.

### What changes
The page still says AGENTS.md support "is coming". It describes mods only through their September preview, with no built-in list, no safety caveat and no Code Mode.

- **Claude Code** replaces the AGENTS.md line with the fallback and names the `agents-md` mod that now carries it. It gains a "Built-in mods" bullet, a Code Mode bullet in Current status (which is dated 17 November) and a trust caveat under Weaknesses. Three Recent-changes entries are added, dated 17 November, 21 October and 19 September. The three oldest entries (14 July, 17 July, 8 August) spill to history. The page date stays 23 November.
- Three new source pages: the Code Mode post, the mods essay, and an AGENTS.md story page for the 19 September AINews issue.

### What to weigh
The v2.1.323 version for Code Mode comes from a community note, not from Anthropic's post. The Every tip gets no source page of its own because it only repeats the announcement. The essay's comparisons with ChatGPT Intelligent UI and Cursor PR Routing are left out (see Open questions).

## Intended changes

- [ ] **Update** `wiki/tools/claude-code.md` — Current status: date 2026-10-26 → 2026-11-17, first bullet mentions the AGENTS.md fallback, new Code Mode bullet; Mods section: new "Built-in mods" bullet, CLAUDE.md bullet's "AGENTS.md support is coming" replaced; Weaknesses: one mod-trust bullet; Recent changes: adds three entries dated 2026-11-17, 2026-10-21, 2026-09-19 in date order (10 → 13), spills the three oldest; `sources:` and `## Sources` gain three ids/links; `as_of` stays 2026-11-23
- [ ] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — the three oldest Recent-changes entries (at draft time 2026-07-14, 2026-07-17, 2026-08-08)
- [ ] **Create** `wiki/sources/tweets/claudedevs-code-mode-2026-11-17.md`
- [ ] **Create** `wiki/sources/newsletters/latent-space-claude-mods-2026-10-21.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-claude-code-agents-md-2026-09-19.md` — story-specific page for that AINews issue (no source page exists for its raw file)

## Page drafts

### wiki/tools/claude-code.md (updated)

Frontmatter (`as_of` unchanged; `sources:` appends three ids at the end of the live list):

```
sources: [...live list..., claude-ship-launch-2026-11-23, ainews-claude-code-agents-md-2026-09-19, latent-space-claude-mods-2026-10-21, claudedevs-code-mode-2026-11-17]
```

`## Current status` heading and first bullet (replace), plus one new bullet appended at the end of the section:

```
## Current status (as of 2026-11-17)

- Terminal CLI agent with persistent project context via `CLAUDE.md` (or `AGENTS.md` when no CLAUDE.md exists) and project-local auto-memory (`MEMORY.md` plus topic files); most-used AI coding tool at 63% of respondents per Pragmatic Engineer's May 2025–Feb 2026 developer survey
...
- **Code Mode (experimental, 2026-11-17):** Claude writes one script that chains its tool calls instead of one call per round trip, and can answer while long commands still run. Opt in with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1` (v2.1.323+); compare `/cost` with it off and on. The general pattern is on [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md).
```

`## Mods, Projects, and cloud sessions` — new bullet inserted directly after the **Claude Mods** bullet:

```
- **Built-in mods:** Anthropic now builds parts of Claude Code as mods, listed under /plugin → Installed → Built-in: `agents-md` (loads AGENTS.md as project instructions), `diff` (the /diff pane), `plugin-authoring` (the skill Claude uses to write mods for you), `sec-default` (guards organization-managed settings from user-installed mods), `telemetry`, and `you-should-know`, the only one off by default: a side agent that flags things buried in the trace, such as about 45 files of uncommitted work before a discard. Third-party supervisor mods cost tokens: ModSmith's Next Steps Supervisor fired on 99 of 111 turns at about 5–6k input-equivalent tokens per check on a 50k-token session.
```

`## Mods, Projects, and cloud sessions` — **CLAUDE.md** bullet (replace):

```
- **CLAUDE.md:** Thariq Shihipar expects it to disappear in the limit and suggests starting new projects without one, adding only repeated failure modes, since those are model-specific. Since v2.1.277 (September 2026) Claude Code reads AGENTS.md when no CLAUDE.md is present, with a config toggle, which removes shim files that only point one format at the other; the built-in `agents-md` mod now does the loading.
```

`## Weaknesses / caveats` — one bullet appended:

```
- Mods are not sandboxed: a loaded mod can read and write files, see every prompt, and spend usage, and built-in mods keep running under `--safe-mode`, so third-party mods need a code read before install
```

`## Recent changes` (adds three entries in date order; list goes 10 → 13, then the three oldest spill):

```
- [2026-11-23] `/ship` command added (beta): pushes the change, opens the PR, and hands it to [Claude Ship](claude-ship.md) for review, fixes, and an approval decision.
- [2026-11-17] Experimental Code Mode (`CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1`): Claude chains tool calls in one script and can reply while long commands run.
- [2026-10-26] Function hooks confirmed as early access (2.1.274+, opt-in env flag); the third-party [fast-jev-compaction](fast-jev-compaction.md) plugin uses them to replace the `/compact` summary with pruning.
- [2026-10-21] Six built-in mods documented (agents-md, diff, plugin-authoring, sec-default, telemetry, opt-in you-should-know side agent); mods are unsandboxed and built-ins run under `--safe-mode`.
- [2026-10-21] Split: the "Best practices (Anthropic engineering)" and "/ultrareview" sections moved to [Claude Code practices](../workflows/claude-code-practices.md); one-line pointers remain.
- [2026-10-19] Split: the loop-taxonomy table and loop guidance moved to [Agent loop design](../workflows/agent-loop-design.md) (one-line pointer remains); Claude Security detail (Enterprise public beta on Mythos 5.1, adversarial self-verification, per-finding patches, Claude Code plugin beta, as of 2026-09-09) moved here from the [State of Cybersecurity](../state-of/cybersecurity.md) leader line.
- [2026-09-29] Thariq Shihipar (Latent Space) details Claude Mods (in-process function hooks: forked cache-sharing subagents, UI changes, composable modes), Projects, the "cloud brain, local hands" direction, and advice to start new projects without a CLAUDE.md.
- [2026-09-23] Cloud sessions left research preview (`claude --cloud`, web, mobile, desktop): work continues with the laptop closed on normal plan usage, plus a one-time $100 Pro / $250 Max credit; Projects launched alongside and now also run locally.
- [2026-09-19] v2.1.277 reads AGENTS.md when no CLAUDE.md is present, with a config toggle.
- [2026-09-17] Projects redesigned (beta, select Pro/Max cloud-session users): one coordinator chat routes work to parallel threads, each a cloud session on its own branch; shared project memory and a file/artifact library; model and effort set separately for coordinator and workers.
```

`## Sources` (appends three links at the end):

```
- [AINews — Claude Code reads AGENTS.md (v2.1.277)](../sources/newsletters/ainews-claude-code-agents-md-2026-09-19.md)
- [Latent Space — Claude Mods: Flipping the Harness Inside Out](../sources/newsletters/latent-space-claude-mods-2026-10-21.md)
- [ClaudeDevs — Code Mode (experimental)](../sources/tweets/claudedevs-code-mode-2026-11-17.md)
```

### wiki/history/tools/claude-code.md (updated — spill)

Appended at the end of the file (entries kept in ascending date order, as in the existing archive blocks):

```

## Archived from current page on <apply date>

- [2026-07-14] Anthropic countered OpenAI's Codex/ChatGPT merge week with a Claude Code in-app browser, a third extension of Fable 5's promotional access (through July 19) with 50%-higher Claude Code limits, and a Chat+Cowork "home" tab merge.
- [2026-07-17] `/code-review` gains configurable effort levels (low: fast single pass; high: sub-agents verify every finding), replacing the previous single fixed prompt.
- [2026-08-08] Cross-session messaging shipped (one session summarizes to another on a different machine); auto mode becomes the default permission mode for Pro/Max/Team, gated by a classifier Anthropic says caught 89% of dangerous commands vs. 14% for manual approval; also added session budgets, automatic repo-skill loading, and mid-session advisor models.
```

### wiki/sources/tweets/claudedevs-code-mode-2026-11-17.md (new)

```
---
title: ClaudeDevs — Code Mode (experimental) in Claude Code
type: source
source_type: tweet
source_file: raw/tweets/2026-11-24-xcom-claudedevs-2122801681939234950.md
url: https://x.com/ClaudeDevs/status/2122801681939234950
published: 2026-11-17
ingested: 2026-11-24
domains: [coding, agents]
---

# ClaudeDevs — Code Mode (experimental) in Claude Code

Anthropic's ClaudeDevs account introduces Code Mode, an experimental way for Claude Code to use tools: Claude writes scripts that chain tools together and can answer while long commands are still running. Rendered via aside. Every's 2026-11-18 newsletter (`raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md`) relays it with a tip to compare `/cost` on one multistep task with Code Mode off and on.

## Influenced pages
- [Claude Code](../../tools/claude-code.md) — Code Mode bullet in Current status and a Recent-changes entry

## Key claims extracted
- Code Mode is experimental; opt in with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1`
- Claude writes scripts that chain tool calls instead of one call per round trip, and can reply while long commands still run
- Docs page: "Run tool calls from code with Code Mode" on code.claude.com
- A community note on a related post says it is official and available from v2.1.323
```

### wiki/sources/newsletters/latent-space-claude-mods-2026-10-21.md (new)

```
---
title: 'Latent Space — Claude Mods: Flipping the Harness Inside Out'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-claude-mods-flipping-the-harness-inside-out.md
url: https://www.latent.space/p/claude-mods
published: 2026-10-21
ingested: 2026-11-24
domains: [coding, agents]
---

# Latent Space — Claude Mods: Flipping the Harness Inside Out

An essay arguing that Claude Mods turn the harness from an agent-to-machine interface into an "Attention Interface" toward the human. It lists the mods Anthropic ships built in, walks through you-should-know and the author's open-source Next Steps Supervisor (ModSmith), and counts the costs. It also contrasts mods with ChatGPT's Intelligent UI and Cursor's PR Routing & Approval.

## Influenced pages
- [Claude Code](../../tools/claude-code.md) — built-in mods bullet, AGENTS.md loader, mod-trust caveat, Recent-changes entry

## Key claims extracted
- A mod is a Claude Code plugin of TypeScript/JavaScript functions that run inside Claude Code (CLI and Desktop), react to events such as prompts, tool calls and renders, and can observe, re-render or replace the default handling
- Six built-in mods under /plugin → Installed → Built-in: agents-md (loads AGENTS.md as project instructions), diff, plugin-authoring, sec-default, telemetry, you-should-know (the only one off by default)
- you-should-know is a side agent that flags important things buried in the trace. In the author's example it caught about 45 files of uncommitted work before a discard
- Next Steps Supervisor (ModSmith) runs after turns that edit files, run commands or make 8+ tool calls: 99 of 111 turns since 2026-10-15. Its README estimates about 5–6k input-equivalent tokens per check on a 50k-token session
- Per Anthropic's docs, mods aren't sandboxed: a loaded mod can read and write files, see every prompt and spend usage. Built-in mods keep running under `--safe-mode`
- Comparisons: ChatGPT Intelligent UI (generative UI shipped with GPT-6 on 2026-10-07) and Cursor PR Routing & Approval (reviewer assignment, auto-approval of low-risk PRs, approval policy read from the base branch so an agent can't relax review on its own PR)
```

### wiki/sources/newsletters/ainews-claude-code-agents-md-2026-09-19.md (new)

```
---
title: AINews — Claude Code reads AGENTS.md (v2.1.277)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
published: 2026-09-19
ingested: 2026-11-24
domains: [coding]
---

# AINews — Claude Code reads AGENTS.md (v2.1.277)

Story-specific source page for one item in the 2026-09-19 AINews issue: "AGENTS.md gained real momentum as a cross-tool convention."

## Influenced pages
- [Claude Code](../../tools/claude-code.md) — AGENTS.md fallback replaces "support is coming"; Recent-changes entry

## Key claims extracted
- Per @trq212 (Thariq Shihipar), Claude Code v2.1.277 checks for AGENTS.md when no CLAUDE.md is present, with a config-level toggle
- AINews reads this as acknowledging AGENTS.md as an emerging cross-tool standard
- Simon Willison: the practical payoff is fewer shim files that just point one format to the other
```

## Schema / vocabulary additions

None.

## Open questions

- **Claude Code** goes from about its 1,500-word body ceiling to roughly 115% with these additions. Should a later refactor split "Mods, Projects, and cloud sessions" into its own page? Below 150% this is optional.
	- Yes, but keep them as sub-pages except when they are features of many AI coding tools
- The essay names two products the wiki lacks: ChatGPT Intelligent UI (generative charts, forms and tools inside answers, shipped with GPT-6 on 2026-10-07) and Cursor PR Routing & Approval (auto-approves low-risk PRs and reads the approval policy from the base branch). Should either get a line on its tool page from this essay, or wait for a primary source?
	- Wait
