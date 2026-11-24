---
type: proposal
source: raw/newsletters/2026-09-29-claude-codes-next-era-thariq-shihipar-anthropi.md
sources:
  - raw/newsletters/2026-09-29-claude-codes-next-era-thariq-shihipar-anthropi.md
  - raw/tweets/2026-09-23-claudedevs-2102871550974427462.md
  - raw/newsletters/2026-09-24-ainews-meta-connect-2026-muse-glasses-voice-v.md
  - raw/articles/2026-10-20-devinai-blog-devin-cloud-in-your-terminal.md
  - raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Claude Code's next era (Mods, Projects, cloud sessions) and cloud handoff across coding agents

## Summary

### In short

A coding agent that keeps working in the cloud after you close the laptop, and hands work back to your machine, is now the standard setup: Claude Code, Devin and Codex all shipped it within ten days in late September. Claude Code's cloud sessions left preview on 23 September. Anthropic's Thariq Shihipar also describes Claude Mods, which let users rewrite the harness itself, and Projects. The proposal updates Claude Code, Devin and Agent runtime platforms and adds five source pages. Reason to hesitate: Claude Code ends up at about 113% of its length ceiling.

[[#Open questions|Open questions: 2 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

The main source is a long Latent Space interview (29 September) with Thariq Shihipar, who teaches people how to use Claude Code at Anthropic. He says the harness is splitting into a "cloud brain" that reasons, "hands" that work in a cloud sandbox or on your computer when it is online, and artifacts (hosted pages with their own database) as the screen. **Projects** is the first step for individual users: you message one Claude, and it supervises subagents the way Claude Tag does in Slack, without Tag's admin setup. **Claude Mods** customise the harness itself. Ordinary hooks run a script when an event fires. A mod runs inside the harness, so it can see the messages and token counts, start a cheap "forked" subagent that reuses the prompt cache, change the interface, and register modes other mods use. His examples are an end-of-turn quiz, an assumption register and a model router. He also expects CLAUDE.md to fade away, because failure-mode lists are specific to one model and over-constrain the next.

The other sources date the launches. ClaudeDevs announced on 23 September that cloud sessions had left research preview. They run from the web, mobile, desktop or `claude --cloud`, use normal plan usage, and come with a one-time credit ($100 Pro, $250 Max). Cognition's 21 September post brings Devin Cloud to the terminal: `/handoff` sends a local task to a cloud VM and brings it back onto a local branch, and `devin ssh` opens that VM. AINews on 30 September reports Codex cloud environments that keep running with the laptop closed.

### What changes

The wiki's Claude Code page stops at the August auto-mode default, and its runtime page treats cloud-resident agents as a few scattered late-August moves.

- **Claude Code** gains a short "Mods, Projects, and cloud sessions" section and a current-status mention of cloud sessions. It adds two Recent-changes entries (23 and 29 September). The list is at its cap of ten, so the two oldest entries (19 May fast-mode default, 28 May dynamic workflows) move to history. Page date moves to 29 September.
- **Devin** gains a "Devin Cloud in the terminal" subsection and one Recent-changes entry dated 21 September (ten of ten, no spill). The page date stays 19 October.
- **Agent runtime platforms** gets a second paragraph under Cloud-resident agents covering the three launches and the "cloud brain, local hands" split. It also gets one current-status bullet and a Recent-changes entry. Page date moves to 30 September, and the body reaches about 1,230 words, 103% of its ceiling and inside the warning band.
- **Index** lines for Claude Code and Agent runtime platforms get new descriptions and dates.
- Five new source pages: the interview, the ClaudeDevs post, the Devin post, and one story page from each of the 24 and 30 September AINews issues.

### What to weigh

Claude Code already sits at its 1,500-word ceiling, so even this compact section takes it to about 1,690 words. A split is offered below rather than forced. Mods have no ship date in the sources, so they carry the interview date. The Codex fact is a single newsletter line. I used it only on the runtime page and left the Codex page alone. The interview's effort-level advice, its security half and its Claude Tag usage examples are not ingested here, so the Claude Tag page is left alone.

## Intended changes

- [ ] **Update** `wiki/tools/claude-code.md` — extend the Remote Control current-status bullet; insert new `## Mods, Projects, and cloud sessions` section after `## Loop taxonomy`; adds two Recent-changes entries dated 2026-09-29 and 2026-09-23 below the 2026-10-19 entry (list at cap of 10); append 3 source ids to frontmatter and 3 links to `## Sources`; `as_of` 2026-09-09 → 2026-09-29
- [ ] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — spills the two oldest Recent-changes entries (2026-05-28 dynamic workflows, 2026-05-19 fast mode default) under a new archive header
- [ ] **Update** `wiki/tools/devin.md` — insert `### Devin Cloud in the terminal` after `### Devin Outposts`; adds one Recent-changes entry dated 2026-09-21 below the 2026-10-19 entry (10 of 10, no spill); append 1 source id and 1 link; `as_of` stays 2026-10-19
- [ ] **Update** `wiki/concepts/agent-runtime-platforms.md` — add one current-status bullet; add a second paragraph to `## Cloud-resident agents`; adds one Recent-changes entry dated 2026-09-30 (4 of 10); append 4 source ids and 4 links; `as_of` 2026-09-07 → 2026-09-30
- [ ] **Update** `wiki/index.md` — refresh the `tools/claude-code` and `concepts/agent-runtime-platforms` lines
- [ ] **Create** `wiki/sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md`
- [ ] **Create** `wiki/sources/tweets/claudedevs-cloud-sessions-ga-2026-09-23.md`
- [ ] **Create** `wiki/sources/articles/devin-cloud-in-your-terminal-2026-09-21.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-claude-code-cloud-sessions-projects-2026-09-24.md` — story page for the Claude Code item in that issue
- [ ] **Create** `wiki/sources/newsletters/ainews-codex-cloud-environments-2026-09-30.md` — story page for the Codex item in that issue

## Page drafts

### wiki/tools/claude-code.md (updated)

Frontmatter changes:

```
as_of: 2026-09-29
sources: [...existing..., latent-space-thariq-claude-code-next-era-2026-09-29, claudedevs-cloud-sessions-ga-2026-09-23, ainews-claude-code-cloud-sessions-projects-2026-09-24]
```

Current status, header and one bullet replaced:

```
## Current status (as of 2026-09-29)
```

```
- Remote Control (`claude remote-control`) and Agent View (`claude agents`) extend supervision to mobile and multi-session dispatch; cloud sessions (GA 2026-09-23) keep work running on Anthropic's infrastructure with the laptop closed
```

New section, inserted after `## Loop taxonomy`:

```
## Mods, Projects, and cloud sessions

- **Cloud sessions (GA 2026-09-23):** start from claude.ai/code, the mobile Code tab, the desktop app, or `claude --cloud`; GitHub connection required; billed to normal plan usage, with a one-time promotional credit ($100 Pro, $250 Max) spent first.
- **Projects:** a Claude Tag-style supervising agent for individual users without Slack admin setup: message one Claude, it runs subagents and reports through artifacts (each with its own database several agents can read and write). Single-player at launch; also runs locally.
- **Claude Mods:** in-process "function hooks" for the CLI and desktop harness. Unlike shell hooks, a mod sees turn/token counts and messages, can spawn forked subagents that reuse the prompt cache, parse structured output, change the UI, and register modes other mods compose with. Examples: end-of-turn quiz, assumption register, model router, next-steps supervisor.
- **Direction:** "cloud brain, local hands" — one cloud-resident agent that works in cloud sandboxes or on your machine when it is online (see [Agent runtime platforms](../concepts/agent-runtime-platforms.md)).
- **CLAUDE.md:** Thariq Shihipar expects it to disappear in the limit and suggests starting new projects without one, adding only repeated failure modes, since those are model-specific; AGENTS.md support is coming.
```

Recent changes — two entries inserted directly below the 2026-10-19 entry; the 2026-05-28 and 2026-05-19 entries removed (spilled):

```
- [2026-09-29] Thariq Shihipar (Latent Space) details Claude Mods (in-process function hooks: forked cache-sharing subagents, UI changes, composable modes), Projects, the "cloud brain, local hands" direction, and advice to start new projects without a CLAUDE.md.
- [2026-09-23] Cloud sessions left research preview (`claude --cloud`, web, mobile, desktop): work continues with the laptop closed on normal plan usage, plus a one-time $100 Pro / $250 Max credit; Projects launched alongside and now also run locally.
```

Sources — three links appended:

```
- [Latent Space — Claude Code's Next Era (Thariq Shihipar)](../sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md)
- [ClaudeDevs — Cloud sessions out of research preview](../sources/tweets/claudedevs-cloud-sessions-ga-2026-09-23.md)
- [AINews — Claude Code cloud sessions GA and local Projects](../sources/newsletters/ainews-claude-code-cloud-sessions-projects-2026-09-24.md)
```

### wiki/history/tools/claude-code.md (updated)

Appended at the end of the file:

```

## Archived from current page on <apply date>

- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify (with adversarial agents), and iterate to convergence on hours-to-days work; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens.
- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics
```

### wiki/tools/devin.md (updated)

Frontmatter:

```
sources: [...existing..., devin-cloud-in-your-terminal-2026-09-21]
```

New subsection, inserted after `### Devin Outposts` (still under Current status):

```
### Devin Cloud in the terminal

- **Devin Cloud in the CLI (2026-09-21):** `devin --cloud` or `/cloud` creates, steers, resumes and watches cloud sessions from the terminal; sessions outlive the terminal that started them, and `devin --cloud --resume <url>` reopens one.
- **Two-way `/handoff`:** sends a local Devin CLI task to Devin on its own cloud VM; run in a cloud session, it fetches the session's PR branch, checks it out locally, and starts a local session on it. `/open web|desktop` switches the view to the web app or Devin Desktop.
- **`devin ssh`:** connects to the agent's VM to edit code, run dev servers with port forwarding, and copy files with scp.
```

Recent changes — one entry inserted directly below the 2026-10-19 entry:

```
- [2026-09-21] Devin Cloud in the terminal: `devin --cloud`, two-way `/handoff` between the local CLI and a cloud VM, `/open web|desktop`, `--resume`, and `devin ssh` into the agent's VM.
```

Sources — one link appended:

```
- [Cognition — Bringing Devin Cloud to your terminal](../sources/articles/devin-cloud-in-your-terminal-2026-09-21.md)
```

### wiki/concepts/agent-runtime-platforms.md (updated)

Frontmatter:

```
as_of: 2026-09-30
sources: [...existing..., latent-space-thariq-claude-code-next-era-2026-09-29, claudedevs-cloud-sessions-ga-2026-09-23, devin-cloud-in-your-terminal-2026-09-21, ainews-codex-cloud-environments-2026-09-30]
```

Current status — header updated and one bullet appended:

```
## Current status (as of 2026-09-30)
```

```
- Cloud sessions that outlive the laptop, with handoff back to a local checkout, became standard across Claude Code, Devin and Codex in late September 2026.
```

Cloud-resident agents — second paragraph appended after the existing one:

```
By late September 2026 this was the default shape for the leading coding agents. Claude Code cloud sessions left research preview on 23 September (`claude --cloud`, plus web, mobile and desktop). Devin Cloud reached the terminal on 21 September: `/handoff` moves a task from the local CLI to a dedicated cloud VM and back onto a local branch, and `devin ssh` opens the agent's VM as a dev environment. Codex added cloud environments that keep running with the laptop closed. Anthropic calls the next step "cloud brain, local hands": one cloud-resident agent holds the reasoning, does the work in a cloud sandbox or on the user's machine when it is online, and shows progress through hosted artifacts with their own database. [Devin Outposts](../tools/devin.md) already splits a cloud planning loop from execution on customer machines.
```

Recent changes — one entry inserted below the two 2026-10-19 entries:

```
- [2026-09-30] Cloud-resident agents: Claude Code cloud sessions GA, Devin Cloud in the terminal with two-way `/handoff` and `devin ssh`, Codex cloud environments; Anthropic's "cloud brain, local hands" direction.
```

Sources — four links appended:

```
- [Latent Space — Claude Code's Next Era (Thariq Shihipar)](../sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md)
- [ClaudeDevs — Cloud sessions out of research preview](../sources/tweets/claudedevs-cloud-sessions-ga-2026-09-23.md)
- [Cognition — Bringing Devin Cloud to your terminal](../sources/articles/devin-cloud-in-your-terminal-2026-09-21.md)
- [AINews — Codex cloud environments](../sources/newsletters/ainews-codex-cloud-environments-2026-09-30.md)
```

### wiki/index.md (updated)

```
- [tools/claude-code](tools/claude-code.md) — Anthropic's terminal-first AI coding agent; /goal, Agent View, dynamic workflows, cloud sessions (GA), Projects, Claude Mods harness customization, Claude Security plugin *(as_of: 2026-09-29)*
```

```
- [concepts/agent-runtime-platforms](concepts/agent-runtime-platforms.md) — infrastructure around the harness: managed-agent platforms, isolates vs containers, open vs managed cost, LLM-proxy fleet control, enterprise MCP auth, agent-friendly CLIs, plugin/cookbook distribution, cloud-resident agents and local/cloud handoff *(as_of: 2026-09-30)*
```

### wiki/sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md (new)

```
---
title: Latent Space — Claude Code's Next Era (Thariq Shihipar)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-29-claude-codes-next-era-thariq-shihipar-anthropi.md
url: https://www.latent.space/p/thariq
published: 2026-09-29
ingested: 2026-10-20
domains: [coding, agents]
---

# Latent Space — Claude Code's Next Era (Thariq Shihipar)

Interview with Anthropic's Thariq Shihipar on where the Claude Code harness is heading: artifacts as the interface, a cloud "brain" with local or remote "hands", Projects as single-user Claude Tag, and Claude Mods for rewriting the harness itself. This page covers the product half; the agent-security half of the episode is not ingested here.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — Mods, Projects, cloud-brain direction, CLAUDE.md guidance
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — "cloud brain, local hands"

## Key claims extracted

- Claude Mods customise both the execution loop and the UI of Claude Code (CLI and desktop); internally first called "function hooks"; run in-process with access to turn/token counts and messages
- Mods can spawn forked subagents that reuse the prompt cache, parse structured output, and register modes other mods compose with; built with someone from the Bun team
- Example mods: end-of-turn quiz, assumption register, model router, next-steps supervisor, dashboard mod
- Projects: Claude Tag-like supervising agent on Claude's own products, single-player first, without Tag's admin setup
- Direction: separate surface (artifact with its own database), inference (cloud), and hands (local or remote sandbox)
- CLAUDE.md "goes away in the limit"; start new projects without one and add only repeated failure modes; Anthropic will support AGENTS.md
```

### wiki/sources/tweets/claudedevs-cloud-sessions-ga-2026-09-23.md (new)

```
---
title: ClaudeDevs — Cloud sessions out of research preview
type: source
source_type: tweet
source_file: raw/tweets/2026-09-23-claudedevs-2102871550974427462.md
url: https://x.com/claudedevs/status/2102871550974427462
published: 2026-09-23
ingested: 2026-10-20
domains: [coding]
---

# ClaudeDevs — Cloud sessions out of research preview

Anthropic's developer account announces that Claude Code cloud sessions are generally available, with a one-time promotional credit for existing subscribers.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — cloud sessions GA
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — cloud-resident agents

## Key claims extracted

- Cloud sessions run on Anthropic-hosted infrastructure and keep working with the laptop closed
- Start from claude.ai/code, the mobile Code tab, the desktop app, or `claude --cloud`; GitHub connection required
- One-time credit: $100 Pro, $250 Max, separate from usage limits, claim by 7 October (`/claim-credit`)
- Anthropic's Lydia Hallie clarified cloud sessions use normal plan usage with no extra charge; the credit is spent first
```

### wiki/sources/articles/devin-cloud-in-your-terminal-2026-09-21.md (new)

```
---
title: Cognition — Bringing Devin Cloud to your terminal
type: source
source_type: article
source_file: raw/articles/2026-10-20-devinai-blog-devin-cloud-in-your-terminal.md
url: https://devin.ai/blog/devin-cloud-in-your-terminal
published: 2026-09-21
ingested: 2026-10-20
domains: [coding, agents]
---

# Cognition — Bringing Devin Cloud to your terminal

Cognition's launch post for running and steering Devin Cloud sessions from the Devin CLI, with two-way handoff between local and cloud work and SSH access to the agent's VM.

## Influenced pages

- [Devin](../../tools/devin.md) — new "Devin Cloud in the terminal" subsection
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — cloud-resident agents

## Key claims extracted

- `devin --cloud` or `/cloud` creates, steers, resumes and watches cloud sessions; sessions outlive the terminal
- `/handoff` sends a local task to Devin's cloud VM; in a cloud session it brings the PR branch back to a local checkout and local session
- `/open web|desktop` and `devin --cloud --resume <url>` move between views
- `devin ssh` connects to the agent's VM (edit code, forward ports, scp)
- Free SWE-2 sessions until 8 October
```

### wiki/sources/newsletters/ainews-claude-code-cloud-sessions-projects-2026-09-24.md (new)

```
---
title: AINews — Claude Code cloud sessions GA and local Projects
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-24-ainews-meta-connect-2026-muse-glasses-voice-v.md
published: 2026-09-24
ingested: 2026-10-20
domains: [coding]
---

# AINews — Claude Code cloud sessions GA and local Projects

Story page for the Claude Code item in the 24 September AINews issue (headlined on Meta Connect).

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — Projects now run locally

## Key claims extracted

- Claude Code cloud sessions are GA, with a one-time $100 Pro / $250 Max credit
- Projects now run locally
- Anthropic published how it made claude.ai 3x faster in two weeks using Claude for profiling and debugging
```

### wiki/sources/newsletters/ainews-codex-cloud-environments-2026-09-30.md (new)

```
---
title: AINews — Codex cloud environments
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
published: 2026-09-30
ingested: 2026-10-20
domains: [coding, agents]
---

# AINews — Codex cloud environments

Story page for the Codex item in the 30 September AINews issue (headlined on OpenAI DevDay 2026).

## Influenced pages

- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — cloud-resident agents

## Key claims extracted

- Codex gains cloud environments that keep running with the laptop closed
- Refreshed Codex CLI with worktrees and `/agents`, plus Security Cloud
```

## Schema / vocabulary additions

None.

## Open questions

- Claude Code would sit at about 1,690 body words (113% of the 1,500 ceiling). Split now? The cleanest cut is moving `## Best practices (Anthropic engineering)` and `## /ultrareview` (about 450 words together) to a new `workflows/claude-code-practices.md`, leaving one-line pointers.
- Should the Codex page also get a Recent-changes entry for cloud environments, or is the runtime-page mention enough for a one-line newsletter item?
