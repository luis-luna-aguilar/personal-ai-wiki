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
