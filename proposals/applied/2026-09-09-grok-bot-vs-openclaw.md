---
type: proposal
source: raw/newsletters/2026-09-05-openclaw-power-macbook-simplicity-five-days-with.md
status: pending
created: 2026-09-09
---

# Proposal: Grok Bot vs. OpenClaw 2.0

## Summary

### The source

Latent Space published a five-day hands-on comparison of xAI's Grok Bot against OpenClaw 2.0, released the same week. Grok Bot's pitch is near-zero setup: open the plugin catalog, find a service, sign in through a normal browser login, and it's connected — no MCP server JSON, no pasted API credentials. The author connected it to X and to Freshdesk (via a virtual browser session, not a native connector) this way in minutes. Under the hood, Grok Bot runs on an always-on hosted cloud computer per Bot, so state and sessions persist across devices without the user ever standing up or maintaining a server. The programmable unit is the "Bot" itself, not code or a config file: each Bot gets a name, role, and identity, and multiple Bots compose into a "group chat" — the author's Agentic Engineer Bot routes visual/design work to Claude Code, debugging to Codex, and simpler tasks to Grok Build CLI, without the author manually choosing a tool each time. The tradeoffs are real: there's no model picker (Grok Bot routes behind the scenes), no manual context or compaction control the way Claude Code or Codex expose, and — the one flagged as a genuine security-relevant caveat rather than just a UX one — every Bot on an account shares the same underlying computer, files, browser sessions, and logins, so separate Bots are an organizational boundary, not a security boundary. OpenClaw 2.0 narrows the gap from the other direction: its Quick Start can reuse an existing Claude Code or Codex login rather than requiring fresh credentials, it now ships a native Codex runtime, and it offers one-click managed deployment through Hostinger for people who don't want to run their own server. But the fundamental difference holds: OpenClaw gives the user an owned Gateway they choose how and where to run, while Grok Bot supplies and operates the computer as part of the product — a "Mac vs. Linux" split, more optionality and lower-level control on one side, more convenience and less friction on the other. The author's verdict after a week: Grok Bot is genuinely useful as a low-setup "digital chief of staff" for admin, summarizing, and project tracking, but he doubts it will be authoring the majority of his pull requests any time soon — deep implementation work still goes to Claude Code or Codex directly.

### What changes

The wiki already has a page for **Grok Bot** (created at its 2026-08-13 launch, currently thin — just launch framing) but no page for **OpenClaw**, which so far only appears in passing elsewhere in the wiki (as a named example in the cybersecurity dashboard's indirect-prompt-injection entry, and inside a third-party plugin's install instructions).

- **Grok Bot** gains its first substantive hands-on review content: the connector-login mechanics, the Bot-as-atomic-unit design, and the shared-computer security caveat. Page date moves to 5 September.
- New page `wiki/tools/openclaw.md`: OpenClaw 2.0's Quick Start, native Codex runtime, Hostinger managed deployment option, and the user-owned-Gateway framing that distinguishes it from Grok Bot.
- One new source page for the Latent Space review.

### What to weigh

Nothing beyond the sourcing noted above — this is one practitioner's five-day review from a single outlet, not a benchmarked comparison, and both product pages are written to reflect that (framed as one reviewer's read, not settled fact).

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/tools/grok-bot.md` — adds hands-on review findings and a new Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/tools/openclaw.md` — new tool page
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-grok-bot-openclaw-2026-09-05.md` — source summary

## Page drafts

### wiki/tools/grok-bot.md (updated)

Frontmatter `as_of` moves from `2026-08-13` to `2026-09-05`; append `latent-space-grok-bot-openclaw-2026-09-05` to `sources:`.

New `## Hands-on review (as of 2026-09-05)` section, inserted after the existing `## Current status` section and before `## Why it matters`:

```md
## Hands-on review (as of 2026-09-05)

A five-day Latent Space review (against OpenClaw 2.0, see [OpenClaw](openclaw.md)) found:

- Near-zero setup for connectors: open the plugin catalog, sign in through a normal browser login, done — no MCP server JSON, no pasted API credentials
- Runs on an always-on hosted cloud computer per Bot; state and sessions persist across devices with no server for the user to maintain
- "Bots," not code, are the programmable unit: each gets a name, role, and identity, and multiple Bots compose into a "group chat" that can route work between them (e.g. an Agentic Engineer Bot routing design work to Claude Code, debugging to Codex)
- Tradeoffs: no model picker (routing happens behind the scenes), no manual context/compaction control the way Claude Code or Codex expose
- Security-relevant caveat: every Bot on an account shares the same underlying computer, files, browser sessions, and logins — separate Bots are an organizational boundary, not a security boundary
- Reviewer's verdict: strong as a low-setup "digital chief of staff" for admin, summarizing, and project tracking; not yet a replacement for direct-control tools on deep implementation work
```

New entry at the top of `## Recent changes`:

```md
- [2026-09-05] Latent Space's five-day hands-on review: near-zero-setup connectors, Bot-as-atomic-unit design, shared-computer/session caveat (org boundary, not security boundary), and a "useful for shallow work, not deep implementation" verdict.
```

### wiki/tools/openclaw.md (new)

````md
---
title: OpenClaw
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [agentic, open-source]
as_of: 2026-09-05
sources: [latent-space-grok-bot-openclaw-2026-09-05]
---

# OpenClaw

A user-owned agent gateway platform, contrasted this week against xAI's fully-managed [Grok Bot](grok-bot.md) in a five-day Latent Space review. Where Grok Bot supplies and operates the computer as part of the product, OpenClaw gives the user a Gateway they choose how and where to run — described as a "Mac vs. Linux" split: more optionality and lower-level control, at the cost of more setup and operating overhead. OpenClaw is already referenced elsewhere in the wiki as a named example system in the cybersecurity dashboard's indirect-prompt-injection entry; see [State of Cybersecurity](../state-of/cybersecurity.md).

## Current status (as of 2026-09-05)

- OpenClaw 2.0 released the week of 2026-09-05
- Quick Start can now reuse an existing Claude Code or Codex login rather than requiring fresh credentials
- Ships a native Codex runtime and supported routes for other coding-agent harnesses
- One-click managed deployment available through Hostinger, for users who don't want to run their own server
- Its browser app moves much of setup, plugin management, and automation into a graphical or conversational interface
- Reviewer's framing: still requires more setup and closer engagement with code/configuration/tools/skills/plugins/infrastructure than Grok Bot, but 2.0 narrows that gap substantially versus earlier versions

## Weaknesses / caveats

- More setup overhead than fully-managed alternatives like Grok Bot, even after 2.0's improvements
- Single-source coverage (one practitioner's review) so far

## Recent changes

- [2026-09-05] OpenClaw 2.0 released: Claude Code/Codex login reuse in Quick Start, native Codex runtime, one-click Hostinger managed deployment.

## Sources

- [Latent Space — OpenClaw Power, MacBook Simplicity: Five Days With Grok Bot](../sources/newsletters/latent-space-grok-bot-openclaw-2026-09-05.md)
````

### wiki/sources/newsletters/latent-space-grok-bot-openclaw-2026-09-05.md (new)

```md
---
title: "OpenClaw Power, MacBook Simplicity: Five Days With Grok Bot"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-05-openclaw-power-macbook-simplicity-five-days-with.md
url: https://www.latent.space/p/grok-bot
published: 2026-09-05
ingested: 2026-09-09
domains: [agents]
---

# OpenClaw Power, MacBook Simplicity: Five Days With Grok Bot

A five-day hands-on comparison of xAI's Grok Bot against OpenClaw 2.0: Grok Bot's near-zero-setup connector login and Bot-as-atomic-unit design versus OpenClaw's user-owned-Gateway model, now with a lower-friction Quick Start and native Codex runtime.

## Influenced pages

- [Grok Bot](../../tools/grok-bot.md) — hands-on review findings
- [OpenClaw](../../tools/openclaw.md) — new page

## Key claims extracted

- Grok Bot: browser-login connector setup, always-on hosted computer per Bot, "Bots" as the atomic programmable unit
- Grok Bot caveat: all Bots on an account share one computer/session — an organizational boundary, not a security boundary
- OpenClaw 2.0: Quick Start reuses Claude Code/Codex login, native Codex runtime, one-click Hostinger managed deployment
- Framing: Grok Bot is a managed agent computer; OpenClaw is a user-owned agent platform
```

## Schema / vocabulary additions

None.

## Open questions

None beyond the sourcing noted above.
