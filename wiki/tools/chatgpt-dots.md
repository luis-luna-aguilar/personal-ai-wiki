---
title: ChatGPT dots
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [openai, agentic, closed-source]
as_of: 2026-11-19
sources: [ainews-openai-devday-2026-dots-2026-09-30, every-vibe-check-openai-devday-2026-09-29, every-sam-altman-dots-ultrafast-2026-09-30, latent-space-openai-api-agents-api-2026-09-30, every-chatgpt-operating-system-dots-2026-10-04, ainews-openai-capacity-squeeze-codex-pledge-2026-10-06, every-dots-guide-2026-10-23, every-put-your-dot-to-work-2026-10-25, every-dots-texting-2026-10-29, openai-chatgpt-wallet-2026-11-13, every-what-we-let-our-agents-buy-2026-11-19, every-vibe-check-claude-duet-2026-10-21]
---

# ChatGPT dots

OpenAI's always-on personal agents inside ChatGPT, launched at DevDay on 2026-09-29. Each dot runs on [GPT-6 Astra](../history/models/gpt-6-astra.md) and has its own Linux virtual computer in the cloud, so it can run desktop applications and a browser, not only call APIs. It is OpenAI's entry in the always-on agent category alongside [Grok Bot](grok-bot.md), [Meta Muse](meta-muse.md), [Claude Duet](claude-duet.md) and [Claude Tag](claude-tag.md).

## Current status (as of 2026-11-19)

- Connects to 4,000+ apps and sits in Slack and Teams; connecting the user's own machine is optional
- The user sets three boundaries: what the dot may do on its own, what needs approval, and what it must never do
- Available on Pro, Business Premium and Enterprise. The primary dot's own work does not draw on plan usage, but Codex tasks it spawns (bug triage, failing builds, PRs) do. Critics note it starts at the $100 Pro plan.
- **Texting (late October 2026):** a dot can send and receive text messages (iMessage or RCS). Users send a task by text, photo or voice note and get a text back when something needs attention. OpenAI's Nick Baumann routes alerts by urgency: ChatGPT for updates, Slack for work, a text for anything urgent.
- **ChatGPT Wallet (2026-11-13):** a dot can pay for purchases the user approves one by one with Face ID or a fingerprint, without the agent or merchant seeing the card number; US Pro subscribers at launch. See [Agentic commerce](../trends/agentic-commerce.md).
- Launched with two companion shared human/agent surfaces, [ChatGPT Space](chatgpt-space.md) (where a dot can be tagged in a comment) and [ChatGPT Pages](chatgpt-pages.md).

## Hands-on reports

- **Dan Shipper (Every):** his dot became his main way of using ChatGPT. It caught a flight change that clashed with a meeting proposed in a Slack thread he had not read. It also dropped messages, tripped over permissions, often could not reach its browser and made him log in to services twice. His verdict: try it if you live in ChatGPT; users happy with Grok Bot, Muse or Instinct should wait a week or two. In late October, after two weeks with [Claude Duet](claude-duet.md), he found Duet's email drafts worse than his dot's but moved to about 50/50 between ChatGPT and Claude.
- **Sam Altman:** his dot triages urgent issues each morning and alerts him only when something matters. He leaves it voice notes at night and it builds several versions of a feature for him to review.
- **Early testers:** proactive errands such as negotiating with customer service to cut about $500 a year in charges. OpenAI's computer-use lead describes a two-hour meal-prep order done in 15 minutes.
- **Every's team (guide 2026-10-23, recaps through 2026-11-19):** a running list of commitments built from Slack and email, each with a link and a next step; checks for inconsistencies across apps (one caught launch emails describing an unshipped feature); inbox and scheduling rules with an explicit boundary ("Don't send anything without my approval, and save any corrections I give you for next time"); multistep jobs started from a Slack thread. Others add the dot to every channel, let it catch knock-on bugs in a colleague's automation, phone it for a briefing, and keep one ongoing conversation instead of new threads. For purchases they hand off only what any reasonable option would satisfy. Reported problems: silent failures, unreliable connections and dropped tasks.

## Why it matters

OpenAI's framing is ChatGPT as the operating system for work: agents, documents and partner apps all running inside it. Dots move the always-on agent from a startup and second-tier product category into ChatGPT itself. The reliability gap reported in week one is the open question.

## Recent changes

- [2026-11-13] ChatGPT Wallet: dots pay with tokenized cards after per-purchase Face ID or fingerprint approval; US Pro first.
- [2026-10-29] Dots can text (iMessage, RCS): tasks by text, photo or voice note, replies when attention is needed.
- [2026-10-23] Every's dots guide: seven team workflows (commitments list, cross-app consistency checks, inbox rules with an approval boundary, Slack-started jobs); silent failures and dropped tasks reported.
- [2026-10-21] Anthropic launched Claude Duet, a direct rival; Shipper rates its email drafts below his dot's.
- [2026-10-05] Capacity squeeze after DevDay; critics note dots require the $100+ Pro plan.
- [2026-10-04] Every's Dots vibe check: main way Shipper uses ChatGPT, but drops messages and loses its computer connection.
- [2026-09-29] Launched at OpenAI DevDay with Space and Pages; GPT-6 Astra, own Linux cloud computer, 4,000+ connectors, three-tier permission rules.

## Sources

- [AINews — OpenAI DevDay 2026: dots and platform changes](../sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md)
- [Every — Vibe Check: OpenAI DevDay 2026](../sources/newsletters/every-vibe-check-openai-devday-2026-09-29.md)
- [Every — How Sam Altman uses dots to take back his time](../sources/newsletters/every-sam-altman-dots-ultrafast-2026-09-30.md)
- [Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)](../sources/newsletters/latent-space-openai-api-agents-api-2026-09-30.md)
- [Every — ChatGPT wants to be your operating system](../sources/newsletters/every-chatgpt-operating-system-dots-2026-10-04.md)
- [AINews — OpenAI capacity squeeze and the Codex 28-day pledge](../sources/newsletters/ainews-openai-capacity-squeeze-codex-pledge-2026-10-06.md)
- [Every — Dots: A Guide for Putting OpenAI's Always-on Agents to Work](../sources/newsletters/every-dots-guide-2026-10-23.md)
- [Every — Put your Dot to work (recap, 2026-10-25)](../sources/newsletters/every-put-your-dot-to-work-2026-10-25.md)
- [Every — Dots can text you (Context Window, 2026-10-29)](../sources/newsletters/every-dots-texting-2026-10-29.md)
- [OpenAI — Introducing ChatGPT Wallet](../sources/articles/openai-chatgpt-wallet-2026-11-13.md)
- [Every — What We Let Our Agents Buy](../sources/newsletters/every-what-we-let-our-agents-buy-2026-11-19.md)
- [Every — Vibe Check: Duet, Anthropic's always-on agent](../sources/newsletters/every-vibe-check-claude-duet-2026-10-21.md)
