---
type: proposal
source: raw/articles/2026-11-23-cuaai-docs-spaces-guides-connect-your-agent.md
sources:
  - raw/articles/2026-11-23-cuaai-docs-spaces-guides-connect-your-agent.md
  - raw/repos/trycua-cua.md
  - raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
status: pending
created: 2026-11-24
---

# Proposal: Cua Spaces (agent-driven desktop VMs over MCP) and the CUA-S1-FORMS decision model

## Summary

### In short
Coding agents can now provision and drive their own full desktops, and even start nested Claude Code or Codex runs inside them, without the user's credential files ever entering the sandbox. Cua's Spaces app hands Claude Code, Codex, Cursor and others an MCP server for local macOS/Linux VMs, and its open CUA-S1-FORMS is the first decision model built for computer use. The proposal creates a `tools/cua.md` page and adds Cua to **State of Computer Use**, **Agent execution runtimes** and **Decision models**. One reason to hesitate: the Spaces docs carry no publication date, so the page is dated to ingest.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Cua (trycua on GitHub) builds open computer-use infrastructure. Its flagship today is Cua Spaces, a desktop app that gives agents full desktops: each "Space" is a macOS VM built locally on a Mac, or a Linux image, running on the user's own computers or their own AWS, Google Cloud or Modal account. Spaces is free for individuals and paid for Pro and Teams; a sibling tool, Cua Driver, operates native apps in the background.

The "Connect your agent" guide explains how it plugs into coding agents. Setup writes a `cua` MCP server and skills into the settings of each detected agent. The agent can then create a Space, run shell commands and upload a project to it, stream its desktop, move a signed-in Chrome session into it, or share it read-only with a teammate. It can also start long-lived Claude Code or Codex runs inside a Space that outlive the client. Credential handling is the careful part. Host credential files are never copied in; the daemon injects only the provider key a given harness reads, and agents cannot list or change keys at all. To reuse a Claude subscription, Cua copies only the short-lived access token and never refreshes it, because a refresh would sign the user's own Claude Code out. A `spaces:readonly` scope narrows what an agent may do.

Separately, around 19 September (per AINews) Cua open-sourced CUA-S1, a family of small "System 1" models for computer use. The first, CUA-S1-FORMS, scores bounded decisions in form filling, such as which value belongs in which field or which element to leave alone, from structured UI elements rather than by generating text. Application code orders the actions and Cua Driver executes them. Cua calls it an early research release.

### What changes
The wiki has no Cua page. Its computer-use leaders are hosted products and local action layers (Perplexity Computer, Pig, Codex, Peekaboo), and the decision-model page lists only text and audio models.

- New page `tools/cua.md`: Spaces, the MCP tool surface, nested agent runs, credential isolation, Cua Driver, CUA-S1-FORMS and pricing.
- **State of Computer Use** gains a Cua leader line under Computer use and one Recent-changes entry dated 24 November; the list is at its cap of 10, so the oldest entry (Gemini downloadable files, 5 May) spills to history. Page date moves to 24 November.
- **Agent execution runtimes** gains one bullet on nested agent runs with per-harness key injection and access-token-only subscription reuse, plus a Recent-changes entry. Page date moves to 24 November.
- **Decision models** names CUA-S1-FORMS as the first computer-use member, adds Cua's "System 1" to the Also-called line and a Related link, and gets a Recent-changes entry dated 19 September. Page date stays 8 November.
- Three source pages: the Spaces guide, the repo README, and the AINews CUA-S1 story.

### What to weigh
The Spaces guide and README are undated live pages fetched on 23 November, so Spaces claims are dated to ingest (24 November); CUA-S1's September date comes from the newsletter, not Cua. The other judgment call is scope: Cua could also fit the sandbox-provider subcategory, but the proposal files it under computer use, where its driver and desktop streaming sit.

## Intended changes

- [ ] **Create** `wiki/tools/cua.md` — new tool page (subcategory `computer-use`)
- [ ] **Update** `wiki/state-of/computer-use.md` — add Cua leader line under `### Computer use` (after Peekaboo); adds one Recent-changes entry dated 2026-11-24; append three ids to `sources:` and two links to `## Sources`; `as_of` 2026-10-14 → 2026-11-24
- [ ] **Spill** `wiki/state-of/computer-use.md` → `wiki/history/state-of/computer-use.md` — the list is at the cap of 10; spill the oldest-dated entry at apply time (expected: `[2026-05-05] Gemini now generates downloadable files…`)
- [ ] **Update** `wiki/concepts/agent-execution-runtimes.md` — add one bullet to `## Execution runtimes` (after "Real-session browsing"); adds one Recent-changes entry dated 2026-11-24 (8 entries after, no spill); append two ids to `sources:` and two links to `## Sources`; `as_of` 2026-11-23 → 2026-11-24
- [ ] **Update** `wiki/concepts/decision-models.md` — one sentence appended to the "Category formed in a month" bullet; Also-called line gains Cua's term; one Related line; adds one Recent-changes entry dated 2026-09-19 (oldest position); append two ids to `sources:` and two links to `## Sources`; `as_of` unchanged (2026-11-08)
- [ ] **Update** `wiki/index.md` — add `tools/cua` under Tools; tools count 126 → 127, total 305 → 306
- [ ] **Create** `wiki/sources/articles/cua-spaces-connect-your-agent-docs.md` — source summary
- [ ] **Create** `wiki/sources/repos/trycua-cua-repo-2026-11.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/ainews-cua-s1-forms-2026-09-19.md` — story-specific source summary (CUA-S1 item only)

## Page drafts

### wiki/tools/cua.md (new)

```
---
title: Cua
type: tool
domains: [computer-use, agents]
subcategory: computer-use
tags: [open-source, agentic, cli]
as_of: 2026-11-24
sources: [cua-spaces-connect-your-agent-docs, trycua-cua-repo-2026-11, ainews-cua-s1-forms-2026-09-19]
---

# Cua

Open computer-use infrastructure from Cua AI: a desktop app (Cua Spaces) that gives agents their own full desktops, a background driver for native apps (Cua Driver), a cross-language sandbox SDK and `cua` CLI, a benchmark suite (cua-bench), and small open decision models for computer use (CUA-S1).

## Current status (as of 2026-11-24)

- **Spaces.** Each Space is a macOS VM built locally on a Mac, or a Linux image, running on the user's own computers (reachable through a cua.ai relay) or in their own AWS, Google Cloud or Modal account. A signed-in app such as Chrome or Slack can be "teleported" into a Space and stays signed in; people and agents can share one desktop with separate cursors. Free for individuals, Pro $18/month, Teams $30/seat/month.
- **Driven by coding agents over MCP.** Setup adds a `cua` MCP server and skills to Claude Code, Codex, Cursor, Gemini CLI, Hermes, OpenClaw and others. Agents create Spaces, run commands (`space_bash`), upload files, stream the desktop, move a browser session in (`teleport_browser_session`) and share a Space read-only. A `spaces:readonly` permission scope limits agents that only need to look.
- **Nested agent runs.** An agent can start long-lived Claude Code or Codex runs inside a Space (`agent_start` / `agent_message`, or `startThread` in the TypeScript SDK); runs live in the guest and survive the client going away.
- **Credential isolation.** Host credential files are never copied into a Space. Each run gets only the saved provider key its harness reads, keys are written 0600 and redacted from logs, and key management is not exposed as MCP tools, so no agent can read or change keys. To reuse a Claude plan, Cua copies only the short-lived access token and never refreshes it, so the user's own Claude Code stays signed in.
- **CUA-S1-FORMS (September 2026).** First of Cua's small "System 1" [decision models](../concepts/decision-models.md) for computer use: it scores form-filling decisions (which value goes in which field, which elements to leave alone) from structured UI elements instead of generating tokens; application code orders the actions and Cua Driver executes them. MIT code; weights and a synthetic dataset on Hugging Face.

## Weaknesses / caveats

- Spaces itself is source-available (FSL-1.1-MIT, MIT after two years), not MIT like the rest of the repo.
- CUA-S1 is labelled an early research release, not a replacement for a general agent's planning.
- Several older Cua packages are deprecated; `cuabot` has known security issues and Cua says to uninstall it.

## Recent changes

- [2026-11-24] Page created: Cua Spaces 0.9.4 docs (agent-driven desktop VMs over MCP, nested runs, credential isolation) and the CUA-S1-FORMS decision model.

## Sources

- [Cua docs — Connect your agent](../sources/articles/cua-spaces-connect-your-agent-docs.md)
- [trycua/cua GitHub README](../sources/repos/trycua-cua-repo-2026-11.md)
- [AINews — Cua open-sources CUA-S1-FORMS](../sources/newsletters/ainews-cua-s1-forms-2026-09-19.md)
```

### wiki/state-of/computer-use.md (updated)

Frontmatter: `as_of: 2026-11-24`; append `cua-spaces-connect-your-agent-docs, trycua-cua-repo-2026-11, ainews-cua-s1-forms-2026-09-19` to `sources:`.

In `### Computer use`, insert after the Peekaboo line:

```
- [Cua](../tools/cua.md) — open stack that gives coding agents their own desktops: Cua Spaces runs local or self-hosted macOS/Linux VMs that Claude Code, Codex and Cursor drive over MCP, including nested agent runs with no host credentials copied in *(as of 2026-11-24)*
```

`## Recent changes` — insert at the top (then spill the oldest entry):

```
- [2026-11-24] Added [Cua](../tools/cua.md): Cua Spaces lets coding agents create and drive their own macOS/Linux desktops over MCP, and its open CUA-S1-FORMS model scores form-filling decisions for computer use.
```

`## Sources` — append:

```
- [Cua docs — Connect your agent](../sources/articles/cua-spaces-connect-your-agent-docs.md)
- [trycua/cua GitHub README](../sources/repos/trycua-cua-repo-2026-11.md)
```

### wiki/history/state-of/computer-use.md (updated — spill)

Append:

```

## Archived from current page on <apply date>

- [2026-05-05] Gemini now generates downloadable files from chat: Google Docs/Sheets/Slides, Microsoft Office formats, PDF, CSV, LaTeX, TXT, RTF, Markdown — artifact-producing assistant behavior
```

### wiki/concepts/agent-execution-runtimes.md (updated)

Frontmatter: `as_of: 2026-11-24`; append `cua-spaces-connect-your-agent-docs, trycua-cua-repo-2026-11` to `sources:`.

In `## Execution runtimes`, insert after the "Real-session browsing" bullet:

```
- **Nested agent runs on the user's own machines.** [Cua](../tools/cua.md) Spaces lets a coding agent start long-lived Claude Code or Codex runs inside a local or self-hosted VM (`agent_start` / `agent_message`, or `startThread` in TypeScript) that survive the client going away. Host credential files never enter the VM: the daemon injects only the key each harness reads (`ANTHROPIC_API_KEY` for Claude Code, `OPENAI_API_KEY` for Codex), a custom `base_url` gets no saved key unless named, and key management is not an MCP tool, so agents cannot read or change keys. To reuse a Claude subscription, Cua copies only the short-lived access token and never refreshes it, since refreshing would sign the user's own Claude Code out.
```

`## Recent changes` — insert at the top:

```
- [2026-11-24] Added nested agent runs on the user's own machines: Cua Spaces starts Claude Code or Codex inside local VMs with per-harness key injection and access-token-only subscription reuse.
```

`## Sources` — append:

```
- [Cua docs — Connect your agent](../sources/articles/cua-spaces-connect-your-agent-docs.md)
- [trycua/cua GitHub README](../sources/repos/trycua-cua-repo-2026-11.md)
```

### wiki/concepts/decision-models.md (updated)

Frontmatter: `as_of` unchanged (2026-11-08); append `trycua-cua-repo-2026-11, ainews-cua-s1-forms-2026-09-19` to `sources:`.

`## Also called` — replace the line with:

```
System One models (TypeSafe's term; Cua says "System 1"), Constrained Decoding Models (ScaleDown), Decisions API (OpenAI); critics call them zero-shot classifiers.
```

`## Current status` — append to the end of the "Category formed in a month" bullet:

```
Cua's open CUA-S1-FORMS (September) is the first built for computer use: it scores which value belongs in which form field, and which elements to leave alone, from structured UI elements, while application code orders the actions.
```

`## Related` — append:

```
- [Cua](../tools/cua.md) — computer-use infrastructure whose CUA-S1-FORMS scores form-filling decisions
```

`## Recent changes` — insert at the bottom (oldest-dated):

```
- [2026-09-19] Cua's CUA-S1-FORMS added as the first computer-use decision model.
```

`## Sources` — append:

```
- [trycua/cua GitHub README](../sources/repos/trycua-cua-repo-2026-11.md)
- [AINews — Cua open-sources CUA-S1-FORMS](../sources/newsletters/ainews-cua-s1-forms-2026-09-19.md)
```

### wiki/index.md (updated)

Under `## Tools`, insert after the `tools/cursor` line:

```
- [tools/cua](tools/cua.md) — open computer-use stack: Cua Spaces desktop VMs that coding agents drive over MCP (nested runs, no host credentials copied in), Cua Driver, and the CUA-S1-FORMS decision model *(as_of: 2026-11-24)*
```

`## Page count`: `tools: 127`; `**Total content pages: 306.**`

### wiki/sources/articles/cua-spaces-connect-your-agent-docs.md (new)

```
---
title: Cua docs — Connect your agent
type: source
source_type: article
source_file: raw/articles/2026-11-23-cuaai-docs-spaces-guides-connect-your-agent.md
url: https://cua.ai/docs/spaces/guides/connect-your-agent
ingested: 2026-11-24
domains: [computer-use, agents]
---

# Cua docs — Connect your agent

Cua's guide to connecting coding agents to Cua Spaces. Setup (app or `cua connect setup`) writes a `cua` MCP server and skills into each agent's settings; agents can then create Spaces, run commands, send files, stream the desktop, teleport a signed-in browser session, share Spaces read-only, and start nested Claude Code or Codex runs. Most of the page explains how credentials are kept out of Spaces. The page carries no publication date; it was fetched on 2026-11-23.

## Influenced pages
- [Cua](../../tools/cua.md) — new tool page
- [State of Computer Use](../../state-of/computer-use.md) — new Cua leader line
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — nested agent runs and credential isolation

## Key claims extracted
- Supported agents include Claude Code, Codex, Cursor, Gemini CLI, Hermes and OpenClaw; any other can add `cua daemon mcp` by hand.
- Main MCP tools: `list_spaces`/`create_space`, `space_bash`, `send_file`, `stream_endpoint`, `teleport_browser_session`, `share_space`, `delete_space`.
- `agent_start`, `agent_message`, `agent_status`, `agent_stop` run Claude Code or Codex inside a Space; runs survive the client going away. TypeScript: `startThread` from `@trycua/cua/spaces`.
- Host credential files are never copied into a Space; a run gets only the saved key its harness reads, or keys named in `env_from_host`; keys are written 0600 and redacted from the run log.
- Key management methods are daemon methods, not MCP tools: no agent can read, add or remove a key.
- Claude plan reuse: Cua copies only the access token, never the refresh token, and never refreshes, so the user's own Claude Code stays signed in; copying to other computers is off by default.
- `--permissions spaces:readonly` limits an agent to read-only use; `space_bash`, `send_file`, `teleport_app` and `hotspot_start` act with the user's authority.
```

### wiki/sources/repos/trycua-cua-repo-2026-11.md (new)

```
---
title: trycua/cua GitHub README
type: source
source_type: repo
source_file: raw/repos/trycua-cua.md
url: https://github.com/trycua/cua
ingested: 2026-11-24
domains: [computer-use, agents]
---

# trycua/cua GitHub README

The monorepo for Cua's computer-use stack: Cua Spaces (desktop app giving agents full macOS/Linux desktops), Cua Driver (background control of native apps on macOS, Windows and Linux), the `cua` SDK and CLI (Python, TypeScript, Rust), Lume (Apple-silicon VMs), cua-bench, and the CUA-S1 decision models. Fetched 2026-11-23 at Cua Spaces 0.9.4; the README carries no publication date.

## Influenced pages
- [Cua](../../tools/cua.md) — new tool page
- [State of Computer Use](../../state-of/computer-use.md) — Cua leader line
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — Spaces as a self-hosted agent runtime
- [Decision models](../../concepts/decision-models.md) — CUA-S1-FORMS

## Key claims extracted
- Spaces run locally on a Mac, on other computers the user owns, or in their own AWS, Google Cloud or Modal account; signed-in apps can be teleported in; people and agents share a desktop with separate cursors.
- Pricing: free for individuals; Pro $18/month; Teams $30/seat/month.
- Licensing: Spaces is FSL-1.1-MIT (MIT two years after each release); the rest of the repo is MIT.
- CUA-S1 is a family of small "System 1" models for bounded computer-use decisions; CUA-S1-FORMS scores form decisions from structured UI elements and document values; application code orders actions and Cua Driver executes them.
- CUA-S1 is an early, source-only research release; weights and a synthetic dataset are on Hugging Face.
- Several older packages are deprecated; `cuabot` has known security issues and should be uninstalled.
```

### wiki/sources/newsletters/ainews-cua-s1-forms-2026-09-19.md (new)

```
---
title: AINews — Cua open-sources CUA-S1-FORMS
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
published: 2026-09-19
ingested: 2026-11-24
domains: [computer-use, models]
---

# AINews — Cua open-sources CUA-S1-FORMS

Story-specific summary of one item in AINews "Here are 6 Clones of Jev in 2 days" (2026-09-19): Cua open-sourced CUA-S1-FORMS, the first in a family of small "System One" computer-use models, which AINews reads as a move toward fast, bounded action decisions rather than text-only planning.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — first computer-use member
- [Cua](../../tools/cua.md) — date for CUA-S1-FORMS

## Key claims extracted
- Cua open-sourced CUA-S1-FORMS around 2026-09-19, the first of a family of small System One computer-use models.
```

## Schema / vocabulary additions

None.

## Open questions

- Cua is filed under subcategory `computer-use`. It also sells self-hosted desktops for agents, which overlaps `agent-sandbox-infra` (E2B, Daytona). Keep `computer-use`, or switch?
	- Keep
