---
type: proposal
sources:
  - raw/newsletters/2026-07-14-the-urge-to-merge-chatgpt-and-codex.md
  - raw/newsletters/2026-07-14-ainews-codex-usage-up-10x-in-6-months-to-7m-use.md
  - raw/newsletters/2026-07-11-ainews-not-much-happened-today.md
  - raw/newsletters/2026-07-13-apple-just-sued-openai.md
status: pending
created: 2026-09-06
---

# Proposal: OpenAI folds Codex into a ChatGPT "superapp"; Anthropic and Cursor counter

## Summary

### The source

Five days after GPT-5.6 launched, OpenAI merged its standalone Codex app into a new ChatGPT desktop app — three modes (Chat, Work, Codex) in one window, with the old ChatGPT app relabeled "ChatGPT Classic." It did not land well. Theo Browne called it a "generational fumble"; Reddit threads described "mayhem" — duplicate apps, buried chats and projects, broken plugins, unclear usage limits. OpenAI course-corrected in public: multiple usage-limit resets, and (per Codex lead Thibault Sottiaux) a rollback of the context limit from 372K back down to 272K after it caused billing and usage side effects. None of that stopped growth. AINews' own estimate, chaining Fidji Simo's March disclosure (2M Codex users, ~550-700K on January 1) with a July tweet reporting 6M users on July 12 and 7M a day later, puts Codex at roughly 10x year-over-year growth — against Claude Code's last public figure of ~2M weekly users and $2.5B ARR from February.

Anthropic didn't sit still. It reset Claude's own 5-hour and weekly usage allowances, extended Claude Fable 5's promotional access on paid plans three times in ten days (July 7 → 12 → 19, with Claude Code's weekly limits kept 50% higher throughout), shipped an in-app browser for Claude Code desktop, and merged Chat and Cowork into a single "home" tab. Cursor made its own smaller move in the same window: version 3.11 added "side chats" — a parallel conversation (`/side` or `/btw`) that inherits the main session's context so you can research something or double-check a decision without derailing the agent that's actively working.

### What changes

The wiki's coding-tool pages currently treat Codex, Claude Code, and Cursor as separate, steadily-evolving products. This is the first source describing them as active competitors reacting to each other in real time, with real (if noisy) usage numbers attached.

- **Codex** gains the merge, the backlash, the usage-limit fixes, and the growth estimate — with its sourcing chain spelled out, since it's an estimate built from two different disclosures, not a single confirmed number. Page moves to 14 July.
- **Claude Code** gains Anthropic's specific countermoves: the browser, the third Fable 5 extension, the Chat+Cowork merge. Page moves to 14 July; Recent changes is at the 10-entry cap, so the oldest entry spills to history.
- **Cursor** gains the side-chats feature. Page moves to 13 July.
- **State of Coding** gets one combined Recent-changes entry for the whole episode, and its Codex/Cursor lines pick up a short mention each. Its Recent-changes list is also at the cap and was already slightly out of order, so this pass reorders it and spills the oldest entry.
- No new source page is created for the AINews "not much happened today" (2026-07-11) newsletter cited above beyond what's already drawn from it here — its content is folded into the Codex/Claude Code updates rather than given its own page, since nothing in it stands alone as a distinct claim outside this merge story.

### What to weigh

The "10x growth" figure is AINews' own construction — a March disclosure chained to a July tweet, not a single OpenAI-published number — and I've kept that chain visible in the draft rather than stating it as a flat fact. Everything else here (the merge, the backlash quotes, Anthropic's specific countermoves, Cursor's side chats) is corroborated across at least two of the four sources.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/codex.md` — add the ChatGPT-desktop merge (Chat/Work/Codex modes), the power-user backlash, OpenAI's usage-limit resets and context-limit rollback, and the ~10x-growth estimate with its sourcing chain; bump `as_of` 2026-07-01 → 2026-07-14; add 2 Recent-changes entries; add 2 sources
    > See draft below

- [ ] **Update** `wiki/tools/claude-code.md` — add Anthropic's countermoves during the same window (in-app browser, third Fable 5 extension through July 19, Chat+Cowork "home" tab merge); bump `as_of` 2026-07-08 → 2026-07-14; add 1 Recent-changes entry (page is at the 10-entry cap — **spill required**); add 1 source
    > See draft below

- [ ] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — oldest-by-date Recent-changes entry (`[2026-05-13]` Agent View, the later of two tied entries) falls off the cap
    > See draft below

- [ ] **Update** `wiki/tools/cursor.md` — add the Cursor 3.11 "side chats" feature; bump `as_of` 2026-07-08 → 2026-07-13; add 1 Recent-changes entry; add 1 source
    > See draft below

- [ ] **Update** `wiki/state-of/coding.md` — add one combined Recent-changes entry for the merge/backlash/growth-race episode and reorder the section into strict newest-first order (fixes a pre-existing `[2026-06-29]`-before-`[2026-07-02]` inversion); short mentions added to the Codex and Cursor lines; page is at the 10-entry cap — **spill required**
    > See draft below

- [ ] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — oldest-by-date Recent-changes entry (`[2026-05-28]` Claude Code dynamic workflows) falls off the cap
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-urge-to-merge-2026-07-14.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/ainews-codex-usage-growth-2026-07-14.md` — source summary (scoped to the Codex/ChatGPT usage-growth and rollout-friction portion of this newsletter issue; the same issue's Prime Intellect Verifiers v1, the Grok Build CLI privacy incident, and the eval-data-as-moat items are separate signals not covered here)
- [ ] **Create** `wiki/sources/newsletters/the-code-cursor-sidechats-2026-07-13.md` — source summary (scoped to Cursor's side-chats release and developer reaction to the ChatGPT/Codex merge; the same issue's Apple/OpenAI lawsuit and the model-router/eval-moat items are separate signals not covered here)

## Page drafts

### wiki/tools/codex.md (updated)

Frontmatter — bump `as_of`, add two source ids:

```yaml
as_of: 2026-07-14
sources: [..., every-urge-to-merge-2026-07-14, ainews-codex-usage-growth-2026-07-14]
```
(append both ids to the existing `sources:` list)

Add to `## Current status`, as a new bullet near the top (this supersedes the framing of the "broader computer-work system" opening paragraph without replacing it):

```md
- **Folded into a ChatGPT "superapp" (July 2026):** OpenAI merged the standalone Codex app into a new ChatGPT desktop app with three modes — Chat (questions), Work (longer cross-tool assignments), and Codex (developer workflows); the previous ChatGPT app was relabeled "ChatGPT Classic." The move drew immediate backlash from power users (Theo Browne called it a "generational fumble"; Reddit threads described "mayhem" — duplicate apps, buried chats and projects, broken plugins, unclear usage limits). OpenAI course-corrected publicly with multiple usage-limit resets and, per Codex lead Thibault Sottiaux, a rollback of the context limit from 372K back down to 272K after it caused billing/usage side effects. Despite the rocky rollout, usage grew fast: chaining Fidji Simo's March disclosure (2M Codex users, an estimated 550K-700K on January 1) with a July tweet reporting 6M users on July 12 and 7M roughly a day later, AINews estimates Codex has grown around 10x year-to-date — compared with Claude Code's last public figure of roughly 2M weekly users and $2.5B ARR from February.
```

Add to `## Recent changes` (top, newest-first):

```md
## Recent changes

- [2026-07-14] OpenAI folded Codex into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes); power users pushed back hard, but usage estimates put Codex around 6-7M users by mid-July, roughly 10x growth year-to-date.
- [2026-07-11] Rollout friction: 36-plus model/effort configuration combinations drew complaints; OpenAI ran multiple usage-limit resets and rolled the context limit back from 372K to 272K.
- [2026-07-01] Every frames Codex as a general-purpose workspace agent for inbox, CRM, healthcare coordination, writing, meeting-note, and personal knowledge workflows.
- [2026-05-19] Zoom plugin (meeting-to-task context handoffs), keep-Mac-awake for long-running remote sessions, additional mobile remote-execution improvements
- [2026-05-10] Codex-maxxing usage patterns (jxnl): durable threads, Heartbeats (thread-local scheduling), Goals with verification criteria, memory as files (vault + AGENTS.md), $browser/@chrome/@computer, side panel as live work surface
- [2026-05-16] 4M+ WAU, 5× messages/user, 1M+ app downloads; Ollama Codex support; MagicPath canvas; /goal as portable MCP; Zed subscription parity; VS Code/Copilot team confirms harness-over-model thesis
- [2026-05-15] Mobile preview in ChatGPT app: steer Codex sessions from iOS/Android while agent runs on devbox; Remote SSH GA; CI/CD hooks; scoped tokens; 30-day enterprise switch promo (2 months free)
- [2026-04-28] OpenAI Symphony: described as an open-source Codex orchestration spec for defining, invoking, and coordinating Codex subagents; issue-tracker integration as the primary input surface; secondary coverage from The Code newsletter — verify spec details against primary OpenAI documentation
```

(no spill needed here — the page had 6 entries before this update and gains 2, landing at 8, under the 10-entry cap)

Add to `## Sources`:

```md
- [Every — The Urge to Merge (ChatGPT and Codex)](../sources/newsletters/every-urge-to-merge-2026-07-14.md)
- [AINews — Codex usage up >10x in 6 months to 7M users](../sources/newsletters/ainews-codex-usage-growth-2026-07-14.md)
```

### wiki/tools/claude-code.md (updated)

Frontmatter — bump `as_of`, add one source id:

```yaml
as_of: 2026-07-14
sources: [..., the-code-cursor-sidechats-2026-07-13]
```
(note: this page's countermove content is drawn from `every-urge-to-merge-2026-07-14`, already added to `codex.md`'s sources above — since the same source id can be cited from multiple pages, add `every-urge-to-merge-2026-07-14` to this page's `sources:` list too, not `the-code-cursor-sidechats-2026-07-13` — corrected below)

```yaml
sources: [..., every-urge-to-merge-2026-07-14]
```

Add to `## Current status`, as a new bullet:

```md
- **Countermoves during OpenAI's GPT-5.6/Codex launch week (July 2026):** Anthropic reset Claude's 5-hour and weekly usage allowances, extended Claude Fable 5's promotional access on paid plans three times in ten days (July 7 → 12 → 19) while keeping Claude Code's weekly limits 50% higher than standard throughout the extension, added an in-app browser to Claude Code desktop so it can pull up docs and designs without leaving the terminal, and merged Chat and Cowork into a single "home" tab.
```

Add to `## Recent changes` (top, newest-first; oldest tied entry removed for the spill):

```md
## Recent changes

- [2026-07-14] Anthropic countered OpenAI's Codex/ChatGPT merge week with a Claude Code in-app browser, a third extension of Fable 5's promotional access (through July 19) with 50%-higher Claude Code limits, and a Chat+Cowork "home" tab merge.
- [2026-07-08] Claude Code and Claude Design add bidirectional `/design-sync` between repo work and Claude Design canvases.
- [2026-07-01] Every frames Claude Code alongside Codex as a general-purpose agent harness spilling beyond software work when tasks can be represented as files, tools, and review artifacts.
- [2026-06-30] Anthropic published the official Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops, with guidance on matching loop primitive to task type and controlling token usage.
- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
- [2026-06-18] Every case studies show Dynamic Workflows replacing manual subagent coordination for reviewer agents and large Figma-to-code work.
- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify (with adversarial agents), and iterate to convergence on hours-to-days work; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens.
- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics
- [2026-05-18] Anthropic engineering best practices: context window as #1 constraint; verification-criteria pattern; explore-plan-code workflow (plan mode + Ctrl+G); Chrome extension for UI screenshot verification
- [2026-05-13] /goal command added (research preview): autonomous loop until evaluator model confirms target met — first native long-horizon success-criterion primitive in Claude Code
```

(the removed entry — `[2026-05-13] Agent View added (research preview, v2.1.139+)...` — is the oldest by date, tied with the `/goal` entry directly above it and positioned last in the file; it is spilled to history below)

Add to `## Sources`:

```md
- [Every — The Urge to Merge (ChatGPT and Codex)](../sources/newsletters/every-urge-to-merge-2026-07-14.md)
```

### wiki/history/tools/claude-code.md (updated — new spill block)

Insert a new block at the top of the file, immediately after the introductory line and above the existing `## Archived from current page on 2026-09-05` block:

```md
## Archived from current page on 2026-09-06

- [2026-05-13] Agent View added (research preview, v2.1.139+): `claude agents` supervises background sessions with peek/reply, attach/detach, `/bg`, `--bg`, and worktree isolation.
```

### wiki/tools/cursor.md (updated)

Frontmatter — bump `as_of`, add one source id:

```yaml
as_of: 2026-07-13
sources: [..., the-code-cursor-sidechats-2026-07-13]
```

Add to `## Current status`, as a new bullet:

```md
- **Side chats (Cursor 3.11, July 2026):** `/side` or `/btw` opens a parallel conversation thread that inherits the main session's context, for researching a library or double-checking a decision without interrupting the agent that's actively working; the same release adds transcript search and cloud-agent hooks.
```

Add to `## Recent changes` (top, newest-first):

```md
## Recent changes

- [2026-07-13] Cursor 3.11 ships side chats (`/side` / `/btw`), transcript search, and cloud-agent hooks.
- [2026-07-08] Grok 4.5 launched: jointly trained with SpaceXAI, 1.5T MoE, available across all Cursor surfaces with double usage for the first week; also available in Grok Build and via API.
- [2026-06-30] Cursor for iOS public beta: launch always-on cloud agents, control desktop agents remotely, voice/slash commands, push notifications, Live Activities, diff review, follow-up, and PR merge from mobile.
- [2026-06-17] SpaceX acquires Cursor in $60B all-stock deal; Cursor Origin launched (agent-native git/code hosting); jointly trained model with xAI coming to Cursor and Grok Build
- [2026-05-18] Composer 2.5: targeted RL with textual hints + KL distillation; 25× synthetic tasks; fast-tier pricing ($3/$15 per M); next model in training at SpaceX/Colossus 2 scale
- [2026-05-14] Cloud development environments: multi-repo agent work with full env config, Dockerfile support, version history, rollback, isolated secrets, 70% faster cached builds; agents can cross-repo trace Slack issues → PRs
- [2026-05-01] Cursor Security Review reported: always-on PR review and scheduled codebase scans; source is AINews secondary coverage, primary Cursor page not yet fetched
- [2026-04-30] Cursor SDK released: TypeScript SDK exposes the Cursor agent runtime headlessly for CI, automations, cloud VMs, MCP servers, model swapping, and embedded product agents; marks transition from IDE seat product toward agent infrastructure platform
- [2026-04-22] Added Truell's third-era data: 35% of Cursor internal PRs from cloud agents; 2:1 agent-to-Tab user ratio; 15× agent usage growth YoY
```

(no spill needed — 8 existing entries plus 1 new lands at 9, under the 10-entry cap)

Add to `## Sources`:

```md
- [The Code — OpenAI's GPT-5.6 Sol wins over developers, Cursor drops side chat](../sources/newsletters/the-code-cursor-sidechats-2026-07-13.md)
```

### wiki/state-of/coding.md (updated)

Frontmatter — no `as_of` change (2026-07-14 remains the newest source-backed claim on the page); no new source ids needed (this page's own Sources section links tool pages, not raw newsletters directly, per its existing convention)

Terminal coding agent — update the Codex line:

> **Before:**
> `- [Codex](../tools/codex.md) — OpenAI; cloud coding agent via CLI, ChatGPT, and now mobile (iOS/Android preview); remote SSH GA; parallel subagents keep the main context clean on independent task parts; direction increasingly spills into broader computer-work workflows — Every now frames it as a general-purpose workspace agent beyond coding (inbox, CRM, writing) *(as of 2026-07-01)*`
>
> **After:**
> `- [Codex](../tools/codex.md) — OpenAI; folded into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes) in July 2026, drawing power-user backlash but reaching an estimated 6-7M users; remote SSH GA; parallel subagents keep the main context clean on independent task parts *(as of 2026-07-14)*`

Agentic coding workspace — update the Cursor line:

> **Before:**
> `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; iOS beta adds mobile launch/control for always-on cloud and desktop agents; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting; Grok 4.5, the jointly trained SpaceXAI/Cursor model, launched July 2026 and is available across all Cursor surfaces *(as of 2026-07-08)*`
>
> **After:**
> `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; iOS beta adds mobile launch/control for always-on cloud and desktop agents; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting; Grok 4.5, the jointly trained SpaceXAI/Cursor model, launched July 2026 and is available across all Cursor surfaces; version 3.11 adds side chats for parallel research without interrupting the main agent *(as of 2026-07-13)*`

`## Recent changes` — full section, reordered into strict newest-first (fixes the pre-existing `[2026-06-29]`-before-`[2026-07-02]` inversion), new entry inserted at top, oldest-by-date entry removed for the spill:

```md
## Recent changes

- [2026-07-14] OpenAI folded Codex into a ChatGPT "superapp" (Chat/Work/Codex modes), drawing power-user backlash but reaching an estimated 6-7M users, ~10x growth year-to-date; Anthropic countered with a Claude Code browser, a third Fable 5 access extension, and higher Claude Code limits; Cursor 3.11 added side chats.
- [2026-07-14] Windsurf (Cognition) shipped Adaptive model router, transparent per-token pricing in the model picker, and removed daily quota limits for Max users.
- [2026-07-02] Fable 5 returned to coding-tool surfaces; Sonnet 5 testing reinforced cost-per-completed-task as a better routing metric than token list price.
- [2026-07-02] Z.ai launched ZCode for GLM-5.2, a signal that open coding models are building product ecosystems around long-context workflows rather than competing only as checkpoints.
- [2026-06-30] Cursor iOS beta adds mobile launch/control for always-on cloud agents and desktop agents.
- [2026-06-30] Official Sonnet 5 launch confirms Claude Code availability and `claude-sonnet-5` API access.
- [2026-06-30] Anthropic published a Claude Code loop taxonomy tying task type to primitives: turn-based prompts, `/goal`, `/loop` or `/schedule`, and proactive routines composed with skills, dynamic workflows, and auto mode.
- [2026-06-29] Devin Fusion (preview): multi-model "sidekick" harness matches frontier performance at 35% lower cost on FrontierCode Extended; Devin added to the Terminal coding agent subcategory alongside the newly documented Agentic MapReduce architecture.
- [2026-06-17] SpaceX acquires Cursor ($60B all-stock); Cursor Origin launched (agent-native git/code hosting); jointly trained xAI model coming to both Cursor and Grok Build — completes a model + IDE + hosting vertical stack
- [2026-06-17] Claude Fable 5 suspended under US export controls; had reached #1 on DeepSWE/FrontierSWE; Claude Code + Fable 5 [max] scored 77 on DeepSWE before ban; Claude Code + Opus 4.8 is now the accessible Anthropic coding stack
```

(the removed entry — `[2026-05-28] Claude Code adds dynamic workflows (research preview)...` — is the oldest by date on the page; it is spilled to history below)

### wiki/history/state-of/coding.md (updated — new spill block)

Insert a new block at the very top of the file, above the existing flat entries (this file predates the `## Archived from current page on <date>` header convention used elsewhere and has not been reformatted — only a new block is added, nothing below it is touched):

```md
# State of Coding — History

## Archived from current page on 2026-09-06

- [2026-05-28] Claude Code adds dynamic workflows (research preview): the `ultracode` effort setting lets Claude write orchestration scripts that fan tens-to-hundreds of parallel subagents, verify findings (with adversarial agents) before folding them in, and iterate to convergence across hours-to-days; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens. Bun's Zig→Rust port (~750K LOC Rust, 99.8% tests passing, 11 days) is the flagship case.

- [2025-10-15] First content for this page. Added `spec-driven-development` subcategory with Kiro, spec-kit, Tessl after ingesting Fowler's SDD survey.
```

(everything from `- [2025-10-15] First content for this page...` onward is the file's existing, unchanged content, reproduced here only so the insertion point is unambiguous)

### wiki/sources/newsletters/every-urge-to-merge-2026-07-14.md (new)

```md
---
title: "The Urge to Merge (ChatGPT and Codex)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-14-the-urge-to-merge-chatgpt-and-codex.md
url: https://every.to/context-window/the-urge-to-merge-chatgpt-and-codex
published: 2026-07-14
ingested: 2026-09-06
domains: [coding, agents]
---

# The Urge to Merge (ChatGPT and Codex)

Every's Katie Parrott on the ChatGPT/Codex merge backlash and Anthropic's countermoves during the same week — plus a practical workflow for using an expensive model (Fable 5) as the planner/reviewer over a cheaper model (Sonnet, or GPT-5.6 Sol across labs) as the executor. The `url` above is inferred from Every's "Context Window" column naming pattern; a distinct "view online" permalink was not present in the plain-text capture.

## Influenced pages
- [Codex](../../tools/codex.md) — the ChatGPT-desktop merge and backlash
- [Claude Code](../../tools/claude-code.md) — Anthropic's countermoves

## Key claims extracted
- OpenAI merged the standalone Codex app into the new ChatGPT desktop app (three modes: Chat, Work, Codex); the previous ChatGPT app was relabeled "ChatGPT Classic"
- Developer/YouTuber Theo Browne called the merge a "generational fumble"; Reddit threads described "mayhem" — duplicate apps, buried chats/projects, broken plugins, unclear limits
- ChatGPT has 800M+ weekly users vs. Codex's ~5M weekly users at the time of the merge — OpenAI is betting the merge trades some power-user alienation for a much larger audience
- Anthropic reset Claude's 5-hour and weekly usage allowances; pushed Fable 5's paid-plan promotional cutoff from July 7 → 12 → 19 while keeping Claude Code's weekly limits 50% higher throughout; added an in-app browser to Claude Code desktop; merged Chat and Cowork into one "home" tab
- Workflow: use an expensive model (Fable 5) as planner/reviewer delegating bounded implementation work to a cheaper model (Sonnet inside Claude Code, or GPT-5.6 Sol via Codex) — includes concrete `.claude/agents/` and `.claude/skills/` setup snippets
- A cited paper (arXiv 2607.08010) reported a 53% agent error-rate drop after the agent stopped rewriting code from scratch and instead saved and reused working solutions as tools
```

### wiki/sources/newsletters/ainews-codex-usage-growth-2026-07-14.md (new)

```md
---
title: "[AINews] Codex usage up >10x in 6 months to 7M users, +1M in the past ~day"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-14-ainews-codex-usage-up-10x-in-6-months-to-7m-use.md
url: https://www.latent.space/p/ainews-codex-usage-up-10x-in-6-months
published: 2026-07-14
ingested: 2026-09-06
domains: [coding, agents]
---

# AINews — Codex usage up >10x in 6 months to 7M users

AINews' own estimate of Codex's growth trajectory, built by chaining Fidji Simo's March disclosure of 2M Codex users (implying ~550K-700K on January 1) with a July 12 tweet reporting 6M users and a July 13 follow-up reporting 7M — set against Claude Code's last public figure of ~2M weekly users and $2.5B ARR from February. This page is scoped to the usage-growth and rollout-friction portion of the issue; the same issue's Prime Intellect Verifiers v1 release, the Grok Build CLI privacy incident, and the "eval data as the real moat" discussion are separate, unrelated signals covered by other proposals from this digest, not this one.

## Influenced pages
- [Codex](../../tools/codex.md) — usage-growth estimate and its sourcing chain

## Key claims extracted
- GPT-5.6 launched July 9; a July 12 tweet reported 6M Codex/ChatGPT-Work users in the prior 48 hours; a follow-up ~24.5 hours later reported 7M
- Fidji Simo's March disclosure put Codex at 2M users, implying roughly 550K-700K users on January 1 — used to derive an approximate 10x year-to-date growth estimate
- Claude Code's last public figure is ~2M weekly active users and $2.5B ARR, reported in February; Anthropic has not published a comparably recent number, possibly because coding usage has shifted partly to Claude Tag/Slack surfaces with different, harder-to-compare usage statistics
- OpenAI's Thibault Sottiaux described several fixes for GPT-5.6 Sol in ChatGPT Work/Codex: ~10% more usage from inference optimizations, a context-limit rollback from 372K to 272K after billing/usage side effects, reversion of some experimental reasoning-effort ("juice") changes, and fixes for overactive multi-agent spawning at high/xhigh settings
```

### wiki/sources/newsletters/the-code-cursor-sidechats-2026-07-13.md (new)

```md
---
title: "OpenAI's GPT-5.6 Sol wins over developers, Cursor drops side chat"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-13-apple-just-sued-openai.md
url: https://codenewsletter.ai/p/openai-s-gpt-5-6-sol-wins-over-developers-cursor-drops-side-chat
published: 2026-07-13
ingested: 2026-09-06
domains: [coding]
---

# OpenAI's GPT-5.6 Sol wins over developers, Cursor drops side chat

The Code's 2026-07-13 issue on GPT-5.6 Sol's strong opening weekend and Cursor's 3.11 release. This page is scoped to the Cursor side-chats feature and developer reaction to the merge; the same issue's Apple-v-OpenAI trade-secret lawsuit and the "eval data is the real moat" model-router discussion are separate, unrelated signals covered by other proposals from this digest, not this one.

## Influenced pages
- [Cursor](../../tools/cursor.md) — side chats, transcript search, cloud-agent hooks

## Key claims extracted
- Cursor shipped "side chats" in its 3.11 release: `/side` or `/btw` starts a parallel conversation that inherits the main chat's context, for researching libraries or double-checking decisions while the main agent keeps working; @-mention the side chat later to bring its answers back into the main thread
- The same release adds transcript search and cloud-agent hooks
- GPT-5.6 Sol went public on Thursday (July 9); developers praised its long agentic runs and subagent orchestration over the launch weekend; usage hit double the previous record, and OpenAI temporarily removed its five-hour usage cap in response to demand
- Codex and ChatGPT Work had 6M active users combined at the time of writing, per Codex lead Thibault Sottiaux
```

## Schema / vocabulary additions

None needed — all domains used here (`coding`, `agents`) already exist in the controlled vocabulary.

## Open questions

- The canonical URL for `every-urge-to-merge-2026-07-14` is inferred from Every's "Context Window" column naming pattern, not a captured "view online" footer. Swap in the real permalink if you have it.
- `the-code-cursor-sidechats-2026-07-13`'s `source_file` points at `raw/newsletters/2026-07-13-apple-just-sued-openai.md` — that file's headline story is the Apple/OpenAI lawsuit, but this proposal only uses its Cursor side-chats section. If a sibling proposal from this same digest batch also creates a source page for this raw file (for the lawsuit or the eval-moat content), the two should be merged into one page at apply time per the wiki's usual one-page-per-raw-file rule, rather than left as two.
