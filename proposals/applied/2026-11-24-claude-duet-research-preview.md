---
type: proposal
source: raw/articles/2026-11-24-claudecom-resources-articles-claude-duet.md
sources:
  - raw/articles/2026-11-24-claudecom-resources-articles-claude-duet.md
  - raw/articles/2026-11-24-claudecom-product-claude-duet.md
  - raw/newsletters/2026-10-21-vibe-check-duetanthropics-always-on-agent.md
  - raw/newsletters/2026-10-25-anthropics-duet-gets-to-work.md
  - raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
status: pending
created: 2026-11-24
---

# Proposal: Claude Duet — Anthropic's always-on personal agent enters research preview

## Summary

### In short
Anthropic now has an always-on personal agent of its own. Claude Duet, launched 21 October on Opus 5.5, comes to the user with a morning brief, works in its own cloud computer while they are away, and waits for approval before it sends, pays or signs. Every's Dan Shipper calls it the first personal agent he would call a pro tool. The proposal creates a Duet tool page, adds it to State of Agents and cross-references it from ChatGPT dots. The reason to hesitate is a partial source: Every's full review is paywalled, so only its free preview and weekly recap were read.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 21 October 2026 Anthropic opened a waitlisted research preview of Claude Duet for US subscribers on the Pro, Max and Ultra plans. Duet is a standalone app for iOS and Android, also reachable on claude.ai. Anthropic built it for professionals and small-business owners with more than they can track. It carries over the user's memory, skills and connected apps from their Claude account and works in one ongoing message thread, typed or spoken. Each morning it sends a brief, then checks connected apps every few hours rather than constantly, to save plan usage. Tasks run in its own virtual machine with a browser, so the user's devices can be off. It can reach more than 6,000 connectors and plugins, from Gmail and Slack to QuickBooks, Stripe, Gusto, Docusign and Shopify. Purchases go through Stripe's Link wallet with a virtual card, or Shop Pay.

Anthropic stresses control. Duet shows exactly what it is about to do and waits for approval before sending a message, paying, signing or deleting anything. Some actions, such as trading securities or moving money between accounts, are blocked even with approval. It reuses safety pieces from Anthropic's other agents: credential handling from Managed Agents, so it never sees passwords or tokens, the auto-mode action classifier, and prompt-injection defenses from browser-use research. A new classifier refuses to pass on card numbers or government IDs. Anthropic lists the preview's limits plainly: it may misjudge urgency, it is weaker at personal errands, and it cannot yet show its browser.

Dan Shipper used Duet daily for two weeks next to his ChatGPT dot. It moved him to roughly an even split between ChatGPT and Claude. He found it unfinished: it can see the Claude sessions on his computers but not direct them, it lacks custom connectors and real voice mode, and its email drafts are worse than his dot's.

### What changes
State of Agents lists ChatGPT dots, Grok Bot, Devin Bots and Meta Muse as always-on agents, and Claude Tag as Anthropic's Slack team agent. Anthropic's personal agent is missing.

- New page `tools/claude-duet.md`: what it is, access and limits, the approval and safety model, Shipper's verdict and the preview's caveats.
- **State of Agents** adds Duet under Agent orchestration, after Claude Tag. Its Recent-changes list is at its cap, so the oldest entry (9 October, Harness²) moves to history. The page date stays 23 November.
- **ChatGPT dots** names Duet in its category sentence and adds Shipper's head-to-head note to his hands-on bullet. Page date moves to 21 October.
- Index entries, plus three source pages: Anthropic's announcement and two Every issues.

### What to weigh
Only Every's free preview and weekly recap were read, so the verdict appears as Every summarized it. It does not include the email failures or the side-by-side comparison with dots that sit behind the paywall.

## Intended changes

- [ ] **Create** `wiki/tools/claude-duet.md` — new tool page
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — one line under Agent orchestration after Claude Tag; adds one Recent-changes entry dated 2026-10-21, inserted between the 2026-10-23 and 2026-10-19 entries; append source id; `as_of` stays 2026-11-23
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — list is at its cap of 10, so the oldest entry (2026-10-09, Harness²) spills
    > See draft below

- [ ] **Update** `wiki/tools/chatgpt-dots.md` — Duet added to the category sentence; one sentence appended to the Shipper hands-on bullet; adds one Recent-changes entry dated 2026-10-21 at the top (list goes from 3 to 4, no spill); append source id and Sources line; `as_of` 2026-10-06 → 2026-10-21
    > See draft below

- [ ] **Update** `wiki/index.md` — add the claude-duet line; refresh the chatgpt-dots date
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-introducing-claude-duet-2026-10-21.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-claude-duet-2026-10-21.md` — source summary (Every Vibe Check, free preview)

- [ ] **Create** `wiki/sources/newsletters/every-duet-gets-to-work-2026-10-25.md` — source summary (Every weekly recap, Duet story)

## Page drafts

### wiki/tools/claude-duet.md (new)

```md
---
title: Claude Duet
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, agentic, closed-source]
as_of: 2026-10-25
sources: [anthropic-introducing-claude-duet-2026-10-21, every-vibe-check-claude-duet-2026-10-21, every-duet-gets-to-work-2026-10-25]
---

# Claude Duet

Anthropic's proactive personal agent, in research preview since 2026-10-21. Duet is a separate app (iOS, Android, and the web at claude.ai) that runs on [Claude Opus 5.5](../models/claude-opus-5-5.md) in one ongoing message thread. It sends a morning brief, watches connected apps, takes tasks by text or voice, keeps working in its own cloud virtual machine while the user is away, and asks before acting. It is Anthropic's entry in the always-on agent category alongside [ChatGPT dots](chatgpt-dots.md), [Meta Muse](meta-muse.md) and [Grok Bot](grok-bot.md). Anthropic's Slack team agent is [Claude Tag](claude-tag.md).

## Current status (as of 2026-10-25)

- Waitlisted research preview for US Pro, Max and Ultra subscribers. It shares the plan's usage limits with the rest of Claude, and its background checks count against them.
- Carries over memory, skills and connected apps from the user's Claude account, and can use 6,000+ Claude Marketplace connectors and plugins. It checks connected accounts every few hours, not continuously.
- Waits for approval before it sends a message, pays, signs or deletes anything. Some actions (trading securities, moving money between accounts) are blocked even with approval. Purchases use Stripe's Link wallet with a virtual card, or Shop Pay.
- Reuses Anthropic's agent safety stack: Managed Agents credential handling (it never sees passwords or tokens), the auto-mode action classifier and browser-use prompt-injection defenses. A new classifier blocks sharing card numbers and government IDs and passes health or financial details only on explicit instruction.

## Hands-on reports

- **Dan Shipper (Every), after two weeks:** the first personal agent he would call a pro tool. It sends suggestions he wants, gives recurring topics their own channels, keeps a visible list of its tasks and what it needs from him, and moved him to about 50/50 between ChatGPT and Claude. Gaps: it sees the Claude sessions on his computers but cannot direct them, it has no custom connectors or real voice mode, and its email drafts are worse than his ChatGPT dot's.

## Weaknesses / caveats

- Anthropic says it may misread a thread or misjudge urgency, can miss something that arrives between check-ins, is weaker at personal errands than at work, and cannot yet show its browser.
- Lives apart from the main Claude app for now; heavy tasks (financial models, decks) use more of the shared plan limits.

## Recent changes

- [2026-10-25] Every's weekly recap adds missing custom-connector support to the list of gaps.
- [2026-10-21] Research preview launched (waitlist, US Pro/Max/Ultra, Opus 5.5); Every's two-week review calls it the first pro-grade personal agent.

## Sources

- [Anthropic — Introducing Claude Duet](../sources/articles/anthropic-introducing-claude-duet-2026-10-21.md)
- [Every — Vibe Check: Duet, Anthropic's always-on agent](../sources/newsletters/every-vibe-check-claude-duet-2026-10-21.md)
- [Every — Anthropic's Duet gets to work](../sources/newsletters/every-duet-gets-to-work-2026-10-25.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter: append `anthropic-introducing-claude-duet-2026-10-21` to `sources:`. `as_of` unchanged.

Under `### Agent orchestration`, insert directly after the Claude Tag line:

```md
- [Claude Duet](../tools/claude-duet.md) — Anthropic; proactive personal agent app on Opus 5.5 (research preview, US Pro/Max/Ultra waitlist): morning brief, tasks run in its own cloud VM, approval before sending, paying or signing; 6,000+ connectors *(as of 2026-10-21)*
```

Recent changes: insert between the 2026-10-23 and 2026-10-19 entries:

```md
- [2026-10-21] Added [Claude Duet](../tools/claude-duet.md) to Agent orchestration: Anthropic's always-on personal agent (research preview on Opus 5.5), joining ChatGPT dots, Grok Bot and Meta Muse.
```

Remove the oldest entry (spilled, see below):

```md
- [2026-10-09] Added [Harness²](../tools/harness2.md) to Agent frameworks: Google's open-source recursive harnessing framework, frozen weights, up to +11.5 points on WorkBuddy-Bench.
```

### wiki/history/state-of/agents.md (updated)

Append at the end of the file (link re-pointed for the history path):

```md

## Archived from current page on <apply date>

- [2026-10-09] Added [Harness²](../../tools/harness2.md) to Agent frameworks: Google's open-source recursive harnessing framework, frozen weights, up to +11.5 points on WorkBuddy-Bench.
```

### wiki/tools/chatgpt-dots.md (updated)

Frontmatter: `as_of: 2026-10-06` → `as_of: 2026-10-21`; append `every-vibe-check-claude-duet-2026-10-21` to `sources:`.

In the intro paragraph:

> **Before:** `It is OpenAI's entry in the always-on agent category alongside [Grok Bot](grok-bot.md), [Meta Muse](meta-muse.md) and [Claude Tag](claude-tag.md).`
> **After:** `It is OpenAI's entry in the always-on agent category alongside [Grok Bot](grok-bot.md), [Meta Muse](meta-muse.md), [Claude Duet](claude-duet.md) and [Claude Tag](claude-tag.md).`

Append to the "Dan Shipper (Every)" hands-on bullet:

```md
In late October, after two weeks with [Claude Duet](claude-duet.md), he found Duet's email drafts worse than his dot's but moved to about 50/50 between ChatGPT and Claude.
```

Recent changes: insert at the top:

```md
- [2026-10-21] Anthropic launched Claude Duet, a direct rival; Shipper rates its email drafts below his dot's.
```

Sources: append:

```md
- [Every — Vibe Check: Duet, Anthropic's always-on agent](../sources/newsletters/every-vibe-check-claude-duet-2026-10-21.md)
```

### wiki/index.md (updated)

Add under Tools, directly after the claude-tag line:

```md
- [tools/claude-duet](tools/claude-duet.md) — Anthropic's always-on personal agent app (research preview, 2026-10-21) on Opus 5.5: morning brief, tasks in its own cloud VM, approval before sending, paying or signing, 6,000+ connectors; Every calls it the first pro-grade personal agent *(as_of: 2026-10-25)*
```

In the chatgpt-dots line, `as_of: 2026-10-06` → `as_of: 2026-10-21`.

### wiki/sources/articles/anthropic-introducing-claude-duet-2026-10-21.md (new)

```md
---
title: Anthropic — Introducing Claude Duet
type: source
source_type: article
source_file: raw/articles/2026-11-24-claudecom-resources-articles-claude-duet.md
url: https://claude.com/resources/articles/claude-duet
published: 2026-10-21
ingested: 2026-11-24
domains: [agents]
---

# Anthropic — Introducing Claude Duet

Anthropic's launch post for Claude Duet, a proactive agent app opened as a waitlisted research preview on 2026-10-21 (with a safety note added 2026-10-23). It covers who Duet is for, the morning brief and background tasks, the safety design, tester stories, how it works, connectors and purchasing, and preview limits. The product page (`raw/articles/2026-11-24-claudecom-product-claude-duet.md`) repeats the same facts in FAQ form.

## Influenced pages
- [Claude Duet](../../tools/claude-duet.md) — new tool page
- [State of Agents](../../state-of/agents.md) — Agent orchestration line

## Key claims extracted
- Research preview by waitlist for US Pro, Max and Ultra subscribers; standalone iOS/Android app and claude.ai; shares plan usage limits
- Designed around Claude Opus 5.5; morning brief; checks connected apps every few hours
- Carries over memory, skills and connected apps from the Claude account; one ongoing thread by typing or voice
- Own virtual machine with a browser; works while the user's devices are off
- Approval required before sending, paying, signing or deleting; trading securities and moving money between accounts blocked even with approval
- Credential handling follows Claude Managed Agents; actions approved by the auto-mode classifier; prompt-injection defenses from browser-use research; red-teamed and pen-tested; in the bug bounty
- New sensitive-information classifier and safety system prompt: rejects sharing card numbers and government IDs; health or financial data only on explicit instruction
- 6,000+ connectors and plugins (Gmail, Slack, QuickBooks, Stripe, Gusto, LinkedIn, Docusign, HubSpot, Canva, Shopify); purchases via Stripe Link virtual card or Shop Pay; 1Password sign-in coming
- Limits: may misread threads or misjudge urgency; weaker at personal errands; cannot yet show its browser; separate from the main Claude app
```

### wiki/sources/newsletters/every-vibe-check-claude-duet-2026-10-21.md (new)

```md
---
title: "Every — Vibe Check: Duet, Anthropic's always-on agent"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-vibe-check-duetanthropics-always-on-agent.md
url: https://every.to
published: 2026-10-21
ingested: 2026-11-24
domains: [agents]
---

# Every — Vibe Check: Duet, Anthropic's always-on agent

Free preview of Dan Shipper's subscriber-only review after two weeks of daily use alongside his ChatGPT dot. The full review (email failures, side-by-side with Dot, who should switch) is paywalled and was not read.

## Influenced pages
- [Claude Duet](../../tools/claude-duet.md) — hands-on verdict and gaps
- [ChatGPT dots](../../tools/chatgpt-dots.md) — head-to-head note

## Key claims extracted
- Duet launches in research preview in its own app, on Opus 5.5, pitched as a chief of staff for knowledge workers
- First personal agent Shipper would call a pro tool: useful suggestions, channels for recurring work, visible list of its tasks and what it needs
- Moved him to roughly 50/50 between ChatGPT and Claude
- Gaps: sees Claude sessions on his computers but cannot direct them; email drafts worse than Dot's; no real voice mode
```

### wiki/sources/newsletters/every-duet-gets-to-work-2026-10-25.md (new)

```md
---
title: "Every — Anthropic's Duet gets to work"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-25-anthropics-duet-gets-to-work.md
url: https://every.to
published: 2026-10-25
ingested: 2026-11-24
domains: [agents]
---

# Every — Anthropic's Duet gets to work

Every's Sunday recap; this page covers its Duet story only. It restates Shipper's Vibe Check verdict and adds one limitation.

## Influenced pages
- [Claude Duet](../../tools/claude-duet.md) — custom-connector gap

## Key claims extracted
- Shipper now closer to 50/50 between ChatGPT and Claude after two weeks with Duet
- Duet sorts recurring topics into channels, tracks its tasks and what it needs, keeps docs and dashboards up to date
- Cannot direct the Claude sessions it sees on the user's computer or use custom connections to other tools
```

## Schema / vocabulary additions

None.

## Open questions

None.
