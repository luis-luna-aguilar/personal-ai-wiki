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
