---
type: proposal
source: raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
sources:
  - raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
  - raw/articles/2026-11-24-openaicom-index-introducing-chatgpt-wallet.md
  - raw/articles/2026-11-24-a16zcom-welcome-to-the-b2a-economy.md
  - raw/newsletters/2026-10-29-my-first-week-with-an-ai-coworker.md
  - raw/newsletters/2026-10-23-dots-a-guide-for-putting-openais-always-on-agent.md
  - raw/newsletters/2026-10-25-anthropics-duet-gets-to-work.md
status: pending
created: 2026-11-24
---

# Proposal: ChatGPT dots texting and Wallet, and a new Agentic commerce trend page

## Summary

### In short
Agents are becoming buyers, and payment is no longer what blocks them: ChatGPT Wallet lets a dot pay with a card token after a Face ID approval, Stripe's agent wallet spend grew about 80-fold in ten weeks, and agent browsing traffic grew eightfold. The open question is what people trust an agent to choose. The proposal creates `trends/agentic-commerce.md` for this material, moves the agent-buyer bullets out of **State of Finance**, and updates **ChatGPT dots** (texting, Wallet, Every's working patterns) and **Agent-readable web**. The reason to hesitate is scope: one new page, five updates and six source pages.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The story runs through four autumn updates on OpenAI's always-on personal agents, called dots, and one market report. In late October dots learned to text. A user can send a task by text, photo or voice note, and the dot texts back, over iMessage or RCS, when something needs attention. OpenAI's Nick Baumann routes his alerts by urgency: ChatGPT for updates, Slack for work, a text for anything urgent. Around the same time Every published a guide to dots with seven team workflows. They include a running list of what you owe people, cross-app consistency checks (one found launch emails describing an unshipped feature), inbox rules with an explicit "don't send anything without my approval" boundary, and jobs started from Slack threads. Every also reports silent failures, unreliable connections and dropped tasks.

On 13 November OpenAI launched ChatGPT Wallet with American Express, Chase, Mastercard and Visa, first for US Pro subscribers through dots. The user reviews the items, total and card, then approves each purchase with Face ID or a fingerprint. The payment network issues a token in place of the card number, so neither the agent nor the store sees the card, and card rewards and dispute protections still apply. OpenAI expects later to allow purchases pre-approved within spending limits, categories or time windows. A companion playbook tells merchants how to let agent purchases through.

On 10 November Andreessen Horowitz called this the start of the "B2A" (business-to-agent) economy. It cites Human Security data showing agent browser traffic up eightfold from August to October, with Meta's Muse at 60% of it, and Shopify orders from AI-powered search up nearly 13-fold year on year. Every's 19 November newsletter tied the threads together. Its team hands off purchases where the first reasonable option is fine (refills, rebookings, short flights) and keeps approving each one. Its head of evals found the same product sold to a simulated Claude shopper 4% of the time with hype copy written for people and 97% with copy written for agents.

### What changes
State of Finance's "Agent-native commerce and fraud" section says agents are starting to buy things and holds Stripe's spend data. The ChatGPT dots page stops at launch week.

- New page `trends/agentic-commerce.md`, dated 20 November, gathers the agent-as-buyer material: Stripe's spend data and the agents-as-purchasers point moved from State of Finance, plus Wallet, the B2A traffic figures, merchant responses and delegation patterns.
- **State of Finance** loses those two bullets and their 20 November Recent-changes entry, gains a one-line pointer and an entry recording the move, and keeps its fraud bullets. Page date stays 23 November.
- **ChatGPT dots** gains texting, Wallet and Every's working patterns, with three Recent-changes entries; page date moves from 6 October to 19 November.
- **Agent-readable web** gains the merchant playbook and the 4%-versus-97% copy test; page date moves from 14 October to 19 November.
- **Meta Muse**'s commerce link and the two Stripe source pages are re-pointed to the new page, and the index gains it.
- Six new source pages.

### What to weigh
The brief named which material moves; the drafts move the two buyer bullets and leave both fraud bullets on State of Finance, on the reading that fraud is a finance concern. The Every dots guide is paywalled, so its workflows come from the free preview and two recap newsletters. OpenAI's texting announcement on X was not fetched; texting rests on Every's newsletter.

## Intended changes

- [ ] **Create** `wiki/trends/agentic-commerce.md` — new trend page (`domains: [finance, agents]`, `tags: [agentic]`)
    > See draft below

- [ ] **Update** `wiki/state-of/finance.md` — in "Agent-native commerce and fraud", replace the "Agents as purchasers" and "Agent spend is ramping fast" bullets with one pointer line; move the 2026-11-20 Recent-changes entry to the new page and add one entry dated 2026-11-24 (list stays at 9); remove `stripe-agentic-commerce-holiday-2026-11-20` from frontmatter `sources:` and its `## Sources` line; `as_of` stays 2026-11-23
    > See draft below

- [ ] **Update** `wiki/tools/chatgpt-dots.md` — add texting and Wallet bullets to Current status and an Every working-patterns bullet to Hands-on reports; adds three Recent-changes entries dated 2026-11-13, 2026-10-29 and 2026-10-23 (list goes to 6, no spill); append five source ids and Sources lines; `as_of` and Current-status stamp 2026-10-06 → 2026-11-19
    > See draft below

- [ ] **Update** `wiki/concepts/agent-readable-web.md` — add one Current-status bullet and one What-to-watch bullet; adds one Recent-changes entry dated 2026-11-19 (list goes to 5); append two source ids and Sources lines; `as_of` 2026-10-14 → 2026-11-19
    > See draft below

- [ ] **Update** `wiki/tools/meta-muse.md` — re-point the Commerce bullet's link from State of Finance to Agentic commerce; no date change
    > **Before:** `... up ~80x from early September to mid-November, led by travel ([State of Finance](../state-of/finance.md))`
    > **After:** `... up ~80x from early September to mid-November, led by travel ([Agentic commerce](../trends/agentic-commerce.md))`

- [ ] **Update** `wiki/sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md` — re-point its State of Finance Influenced-pages line to the new page
    > See draft below

- [ ] **Update** `wiki/sources/newsletters/stripe-agent-native-commerce-fraud-2026-04-29.md` — add the new page to Influenced pages for the agents-as-purchasers point
    > See draft below

- [ ] **Update** `wiki/index.md` — add the new trend page under Trends
    > See draft below

- [ ] **Create** `wiki/sources/articles/openai-chatgpt-wallet-2026-11-13.md` — source summary

- [ ] **Create** `wiki/sources/articles/a16z-b2a-economy-2026-11-10.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-what-we-let-our-agents-buy-2026-11-19.md` — story-specific source summary (Wallet, B2A, team shopping practice)

- [ ] **Create** `wiki/sources/newsletters/every-dots-texting-2026-10-29.md` — story-specific source summary (dots texting and the commitments-list prompt in Every's 2026-10-29 newsletter)

- [ ] **Create** `wiki/sources/newsletters/every-dots-guide-2026-10-23.md` — source summary (paywalled guide preview)

- [ ] **Create** `wiki/sources/newsletters/every-put-your-dot-to-work-2026-10-25.md` — story-specific source summary (the "Put your Dot to work" list in Every's 2026-10-25 recap)

## Page drafts

### wiki/trends/agentic-commerce.md (new)

```
---
title: Agentic commerce
type: trend
domains: [finance, agents]
tags: [agentic]
as_of: 2026-11-20
sources: [stripe-agentic-commerce-holiday-2026-11-20, stripe-agent-native-commerce-fraud-2026-04-29, openai-chatgpt-wallet-2026-11-13, a16z-b2a-economy-2026-11-10, every-what-we-let-our-agents-buy-2026-11-19]
---

# Agentic commerce

Personal AI agents acting as buyers: they compare options, check out and pay on a person's behalf, so stores increasingly sell to software as well as to people. Andreessen Horowitz calls this the "B2A" (business-to-agent) economy. It is the step after [LLMs as commercial discovery channel](llm-as-discovery-channel.md), where a model recommends and a person still buys. The fraud side of the same shift (stolen compute, free-trial farming) stays on [State of Finance](../state-of/finance.md).

## Current status (as of 2026-11-20)

- **Spend is ramping.** Stripe's Link Agent Wallet, which pays for personal agents including [Meta Muse](../tools/meta-muse.md), Instinct and Grok, saw daily spend rise ~80x from early September to mid-November and double in the last month. Travel takes >40% of volume and retail ~1/3, and over half of first-time agent buyers buy again.
- **Traffic is ramping.** Agent browser traffic grew 8x from August to October (Human Security via a16z), with Muse driving 60% of it and OpenAI products 30%. Shopify reported orders from AI-powered searches up nearly 13x year on year in Q1 2026.
- **Wallets are the checkout layer.** ChatGPT Wallet (2026-11-13, with American Express, Chase, Mastercard and Visa) lets a [dot](../tools/chatgpt-dots.md) pay after the user reviews items, total and card and approves each purchase with Face ID or a fingerprint. The payment network issues a token in place of the card number, so neither agent nor merchant sees it, and card rewards and dispute protections stay. It launched for US Pro subscribers. OpenAI expects later to allow purchases pre-approved within spending limits, categories or time windows.
- **Merchants are splitting.** Some block agents (Amazon blocks Muse); a16z expects stores to "have to fight for bots' business". OpenAI's Commerce Partner Playbook asks merchants to publish product feeds, recognise signed agent requests (Web Bot Auth), work with fraud and payment providers so legitimate agent purchases are not declined, and add plugins or WebMCP tools. Copy written for agents sells: see [Agent-readable web](../concepts/agent-readable-web.md).

## Delegation patterns

- Payment is solved before choice: "ChatGPT Wallet fixes paying, not picking" (Every). Every's team hands agents purchases where the first reasonable option is fine and the agent already knows what you have (refills, rebookings, short flights, grocery runs), and keeps approving each purchase.
- Taste-dependent purchases such as gifts stay slow whether a person or an agent browses. Agents still miss common sense: one bought salt and olive oil the buyer already had and frozen shrimp instead of fresh.

## Why it matters

Payment, fraud and identity systems were built for human buyers. a16z reports strain on payments, fraud and identity at low agent volume, and says most enterprises still block agent traffic over fraud and chargeback concerns. The playbooks and wallets above are the first attempts to let agents through without losing those protections.

## What to watch

- Whether pre-approved, limit-bound purchases replace per-purchase approval
- Whether stores split into those that block agents and those that write for them
- Stripe's promised Black Friday and Cyber Monday update

## Related

- [State of Finance](../state-of/finance.md) — agent-native fraud patterns
- [LLMs as commercial discovery channel](llm-as-discovery-channel.md) — the step before: AI recommends, a person buys
- [Agent-readable web](../concepts/agent-readable-web.md) — serving and writing for agent visitors
- [ChatGPT dots](../tools/chatgpt-dots.md) and [Meta Muse](../tools/meta-muse.md) — the personal agents doing the buying

## Recent changes

- [2026-11-24] Page created: the agent-buyer bullets split out of [State of Finance](../state-of/finance.md)'s "Agent-native commerce and fraud" section, plus ChatGPT Wallet, the a16z B2A figures and Every's delegation patterns.
- [2026-11-20] Stripe agentic commerce data (Ernie Tedeschi): Link Agent Wallet daily spend ~80x since early September and doubled in a month; travel >40% of volume, retail ~1/3; over half of first-time agent buyers return.
- [2026-11-19] Every's team practice for agent purchases and Mike Taylor's simulated-shopper copy test (4% vs. 97%).
- [2026-11-13] ChatGPT Wallet: tokenized card payments by dots with per-purchase biometric approval; Commerce Partner Playbook for merchants.
- [2026-11-10] a16z "Welcome to the B2A economy": agent browser traffic 8x August–October; Shopify AI-search orders ~13x year on year.

## Sources

- [Ernie Tedeschi (Stripe) — agentic commerce data ahead of the 2026 holiday season](../sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md)
- [Stripe agent-native commerce and compute fraud](../sources/newsletters/stripe-agent-native-commerce-fraud-2026-04-29.md)
- [OpenAI — Introducing ChatGPT Wallet](../sources/articles/openai-chatgpt-wallet-2026-11-13.md)
- [a16z — Welcome to the B2A Economy](../sources/articles/a16z-b2a-economy-2026-11-10.md)
- [Every — What We Let Our Agents Buy](../sources/newsletters/every-what-we-let-our-agents-buy-2026-11-19.md)
```

### wiki/state-of/finance.md (updated)

Frontmatter `sources:` removes `stripe-agentic-commerce-holiday-2026-11-20`; `as_of` unchanged (2026-11-23).

In `### Agent-native commerce and fraud`, the "Agents as purchasers" and "Agent spend is ramping fast" bullets are replaced by one line, so the section reads:

```
### Agent-native commerce and fraud

AI is shifting the fraud attack surface and enabling agents as autonomous economic participants:

- **Stolen compute as the new stolen card.** Stripe's view (via Every newsletter): fraud is moving from payment credentials toward stolen API keys, tokens, credits, free-trial abuse, and unpaid compute bills. "Compute is the new cash."
- **Agents as buyers** — wallets, spend growth and merchant responses are tracked on [Agentic commerce](../trends/agentic-commerce.md).
- **Merchant implications.** Free-trial farming by automated agents, credit-consumption abuse, and unauthorized compute use are the emerging fraud patterns at the intersection of AI and commerce.
```

In `## Recent changes`, remove the 2026-11-20 entry (it moves to the new page):

```
- [2026-11-20] Stripe agentic commerce data (Ernie Tedeschi): Link Agent Wallet daily spend ~80x since early September and doubled in a month; travel >40% of volume, retail ~1/3; over half of first-time agent buyers return. Added to Agent-native commerce.
```

and insert at the top:

```
- [2026-11-24] Agent-buyer bullets (agents as purchasers, Stripe Link Agent Wallet spend) moved to the new [Agentic commerce](../trends/agentic-commerce.md) trend page; this section keeps the fraud bullets and a pointer.
```

In `## Sources`, remove:

```
- [Ernie Tedeschi (Stripe) — agentic commerce data ahead of the 2026 holiday season](../sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md)
```

### wiki/tools/chatgpt-dots.md (updated)

Frontmatter changes:

```
as_of: 2026-11-19
sources: [ainews-openai-devday-2026-dots-2026-09-30, every-vibe-check-openai-devday-2026-09-29, every-sam-altman-dots-ultrafast-2026-09-30, latent-space-openai-api-agents-api-2026-09-30, every-chatgpt-operating-system-dots-2026-10-04, ainews-openai-capacity-squeeze-codex-pledge-2026-10-06, every-dots-guide-2026-10-23, every-put-your-dot-to-work-2026-10-25, every-dots-texting-2026-10-29, openai-chatgpt-wallet-2026-11-13, every-what-we-let-our-agents-buy-2026-11-19]
```

Heading change: `## Current status (as of 2026-10-06)` → `## Current status (as of 2026-11-19)`

Insert after the plans bullet ("Available on Pro, Business Premium and Enterprise…"):

```
- **Texting (late October 2026):** a dot can send and receive text messages (iMessage or RCS). Users send a task by text, photo or voice note and get a text back when something needs attention. OpenAI's Nick Baumann routes alerts by urgency: ChatGPT for updates, Slack for work, a text for anything urgent.
- **ChatGPT Wallet (2026-11-13):** a dot can pay for purchases the user approves one by one with Face ID or a fingerprint, without the agent or merchant seeing the card number; US Pro subscribers at launch. See [Agentic commerce](../trends/agentic-commerce.md).
```

In `## Hands-on reports`, append:

```
- **Every's team (guide 2026-10-23, recaps through 2026-11-19):** a running list of commitments built from Slack and email, each with a link and a next step; checks for inconsistencies across apps (one caught launch emails describing an unshipped feature); inbox and scheduling rules with an explicit boundary ("Don't send anything without my approval, and save any corrections I give you for next time"); multistep jobs started from a Slack thread. Others add the dot to every channel, let it catch knock-on bugs in a colleague's automation, phone it for a briefing, and keep one ongoing conversation instead of new threads. For purchases they hand off only what any reasonable option would satisfy. Reported problems: silent failures, unreliable connections and dropped tasks.
```

In `## Recent changes`, insert at the top, in this order:

```
- [2026-11-13] ChatGPT Wallet: dots pay with tokenized cards after per-purchase Face ID or fingerprint approval; US Pro first.
- [2026-10-29] Dots can text (iMessage, RCS): tasks by text, photo or voice note, replies when attention is needed.
- [2026-10-23] Every's dots guide: seven team workflows (commitments list, cross-app consistency checks, inbox rules with an approval boundary, Slack-started jobs); silent failures and dropped tasks reported.
```

In `## Sources`, append:

```
- [Every — Dots: A Guide for Putting OpenAI's Always-on Agents to Work](../sources/newsletters/every-dots-guide-2026-10-23.md)
- [Every — Put your Dot to work (recap, 2026-10-25)](../sources/newsletters/every-put-your-dot-to-work-2026-10-25.md)
- [Every — Dots can text you (Context Window, 2026-10-29)](../sources/newsletters/every-dots-texting-2026-10-29.md)
- [OpenAI — Introducing ChatGPT Wallet](../sources/articles/openai-chatgpt-wallet-2026-11-13.md)
- [Every — What We Let Our Agents Buy](../sources/newsletters/every-what-we-let-our-agents-buy-2026-11-19.md)
```

### wiki/concepts/agent-readable-web.md (updated)

Frontmatter changes:

```
as_of: 2026-11-19
sources: [website-future-agent-readable-2026-07-02, vercel-agents-new-software-2026-07-03, agent-ready-saas-mcp-2026-06, cloudflare-agent-internet-monetization-2026-07, expand-fetch-launch-2026-10, openai-chatgpt-wallet-2026-11-13, every-what-we-let-our-agents-buy-2026-11-19]
```

In `## Current status`, append:

```
- Commerce is the sharpest case. OpenAI's Commerce Partner Playbook (2026-11-13) asks merchants to publish product feeds, recognise signed agent requests through Web Bot Auth rather than block them, and add plugins or WebMCP tools. Copy matters as much as format: in Every's simulated-shopper test the same product sold to a Claude Sonnet shopper 4% of the time with hype copy written for humans and 97% with copy written for AI shoppers. See [Agentic commerce](../trends/agentic-commerce.md).
```

In `## What to watch`, append:

```
- Whether stores split into those that block shopping agents and those that write product pages for them.
```

In `## Recent changes`, insert at the top:

```
- [2026-11-19] Commerce case added: OpenAI's merchant playbook (product feeds, Web Bot Auth, WebMCP) and Every's copy test (4% vs. 97% sales to a simulated Claude shopper).
```

In `## Sources`, append:

```
- [OpenAI — Introducing ChatGPT Wallet](../sources/articles/openai-chatgpt-wallet-2026-11-13.md)
- [Every — What We Let Our Agents Buy](../sources/newsletters/every-what-we-let-our-agents-buy-2026-11-19.md)
```

### wiki/tools/meta-muse.md (updated)

In `## Current status`, the Commerce bullet is replaced (only its closing link changes); `as_of` stays 2026-11-20:

```
- **Commerce:** pays through Stripe's Link Agent Wallet with an agentic payment-protection/refund guarantee; Shop Pay incoming. Day-one usage was 10x Meta's internal projections. Stripe reports wallet-wide daily spend (Muse, Instinct and Grok combined) up ~80x from early September to mid-November, led by travel ([Agentic commerce](../trends/agentic-commerce.md))
```

### wiki/sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md (updated)

In `## Influenced pages`, the State of Finance line is replaced:

```
- [Agentic commerce](../../trends/agentic-commerce.md) — spend data bullet (first added to State of Finance, moved on 2026-11-24)
```

### wiki/sources/newsletters/stripe-agent-native-commerce-fraud-2026-04-29.md (updated)

In `## Influenced pages`, append:

```
- `wiki/trends/agentic-commerce.md` — agents-as-purchasers point (moved from State of Finance on 2026-11-24)
```

### wiki/index.md (updated)

Under `## Trends`, insert in alphabetical position (after `trends/agent-native-compute`):

```
- [trends/agentic-commerce](trends/agentic-commerce.md) — personal agents as buyers ("B2A"): Stripe Link Agent Wallet spend ~80x Sep–Nov 2026, agent browser traffic 8x, ChatGPT Wallet's tokenized per-purchase approval, merchants blocking vs. writing for agents *(as_of: 2026-11-20)*
```

### wiki/sources/articles/openai-chatgpt-wallet-2026-11-13.md (new)

```
---
title: OpenAI — Introducing ChatGPT Wallet
type: source
source_type: article
source_file: raw/articles/2026-11-24-openaicom-index-introducing-chatgpt-wallet.md
url: https://openai.com/index/introducing-chatgpt-wallet/
published: 2026-11-13
ingested: 2026-11-24
domains: [finance, agents]
---

# OpenAI — Introducing ChatGPT Wallet

OpenAI's launch post for ChatGPT Wallet, a way for dots to pay on a user's behalf without seeing card details, built with American Express, Chase, Mastercard and Visa, plus a Commerce Partner Playbook telling merchants how to accept agent purchases.

## Influenced pages
- [Agentic commerce](../../trends/agentic-commerce.md) — wallet mechanics and the merchant playbook
- [ChatGPT dots](../../tools/chatgpt-dots.md) — Wallet bullet
- [Agent-readable web](../../concepts/agent-readable-web.md) — merchant playbook (product feeds, Web Bot Auth, WebMCP)

## Key claims extracted
- Users add a card once; before each purchase they review items, total and card and approve with a security check such as Face ID or a fingerprint; each approval is recorded
- The payment network issues a token (substitute card number, security code, expiry), so the card details are not shared with the business or the agent
- Card rewards and protections for eligible disputes remain; businesses keep pricing, fulfillment, returns and the customer relationship
- Rolling out in dots to US ChatGPT Pro subscribers aged 18+ with eligible US-issued cards
- Later, OpenAI expects users to pre-approve purchases within parameters such as spending limits, purchase categories or time periods
- Commerce Partner Playbook: claim the business in ChatGPT and upload a product feed; configure CDN/firewall to recognize signed requests via Web Bot Auth; work with risk providers to avoid declining legitimate agent purchases (fraud partners Forter, Riskified, Sardine, Signifyd; PSPs Adyen, Checkout.com, Stripe); build plugins or add WebMCP tools
- 1.2B people use ChatGPT each week
```

### wiki/sources/articles/a16z-b2a-economy-2026-11-10.md (new)

```
---
title: a16z — Welcome to the B2A Economy
type: source
source_type: article
source_file: raw/articles/2026-11-24-a16zcom-welcome-to-the-b2a-economy.md
url: https://a16z.com/welcome-to-the-b2a-economy/
published: 2026-11-10
ingested: 2026-11-24
domains: [finance, agents]
---

# a16z — Welcome to the B2A Economy

Andreessen Horowitz's first piece in a series on the agent economy, arguing that agents are becoming the main users of the internet and will decide which products people use and where they spend, a business-to-agent ("B2A") shift. Publication date taken from the page's metadata (modified 2026-11-17).

## Influenced pages
- [Agentic commerce](../../trends/agentic-commerce.md) — B2A framing, traffic figures, merchant and infrastructure strain

## Key claims extracted
- Human Security saw agentic browser traffic grow 8x between August and October 2026; Muse drove the largest share (60%), OpenAI products a combined 30%
- Shopify: AI-driven traffic to its stores up 8x year on year in Q1 2026; orders from AI-powered searches up nearly 13x
- Most agent traffic today is browser use; connectors, plugins and MCPs are emerging as an "App Store for agents"
- Retailers that built walls against bots "will have to fight for bots' business"; most enterprises still block agent traffic over fraud and chargeback concerns
- System strain already visible at low agent volume in payments, fraud and identity, and communication
- Coding agents as precedent: over 40% of GitHub PRs started from an agent draft as of September 2026
```

### wiki/sources/newsletters/every-what-we-let-our-agents-buy-2026-11-19.md (new)

```
---
title: Every — What We Let Our Agents Buy
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
url: https://every.to/context-window/what-we-let-our-agents-buy
published: 2026-11-19
ingested: 2026-11-24
domains: [finance, agents]
---

# Every — What We Let Our Agents Buy

The lead "Signal" and "Inside Every" items of Every's 2026-11-19 Context Window (Grant Harvey): what ChatGPT Wallet changes, a16z's B2A report, Mike Taylor's test of copy written for AI shoppers, and which purchases Every's staff let their agents make. This page covers only those items; the newsletter's other stories are separate.

## Influenced pages
- [Agentic commerce](../../trends/agentic-commerce.md) — delegation patterns, "fixes paying, not picking"
- [ChatGPT dots](../../tools/chatgpt-dots.md) — purchase hand-off practice in the Every team bullet
- [Agent-readable web](../../concepts/agent-readable-web.md) — the 4% vs. 97% copy test

## Key claims extracted
- ChatGPT Wallet launched the previous Friday for a small group of US Pro subscribers; dots shop and the user approves each purchase biometrically; the agent and merchant never see the card number
- "ChatGPT Wallet fixes paying, not picking": hand off purchases where you'd take the first reasonable option and the agent knows what you have (refills, rebookings), and keep approving each one
- a16z's B2A report: agent browsing traffic up 8x August–October; Shopify AI-search orders up nearly 13x year on year in Q1
- Amazon blocks Meta's Muse agent
- Mike Taylor's simulated-shopper test: the same product sold to Claude Sonnet 4% of the time with hype copy written for humans and 97% with copy written for AI shoppers
- Team practice: one staffer's agent buys groceries with a saved card; another has her dot fill an Amazon cart but presses buy herself; Dan Shipper's agent bought salt and olive oil he had and frozen shrimp instead of fresh ("still needs oversight in order to have common sense")
- Tyler Nishida uses Grok Bot to change flights and get refunds, but won't let it pick gifts: taste-dependent purchases take time whoever browses
- Every had not yet tested ChatGPT Wallet itself
```

### wiki/sources/newsletters/every-dots-texting-2026-10-29.md (new)

```
---
title: Every — Dots can text you (Context Window, 2026-10-29)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-29-my-first-week-with-an-ai-coworker.md
url: https://every.to/context-window/my-first-week-with-an-ai-coworker
published: 2026-10-29
ingested: 2026-11-24
domains: [agents]
---

# Every — Dots can text you (Context Window, 2026-10-29)

The dots items in Every's 2026-10-29 Context Window: the new texting channel with a routing tip from OpenAI's Nick Baumann, and Laura Entis's commitments-list prompt from Every's dots guide. This page covers only those items; the newsletter's other stories are separate.

## Influenced pages
- [ChatGPT dots](../../tools/chatgpt-dots.md) — texting bullet; commitments list in the Every team bullet

## Key claims extracted
- Dots can send text messages; users send a task by text, photo or voice note and the dot texts back when something needs attention
- Dots are rolling out gradually to eligible ChatGPT Pro, Business Premium and Enterprise users, varying by region and workspace settings
- Nick Baumann (OpenAI) routes alerts by urgency: ChatGPT for regular updates, Slack for work, text for urgent ("always prefer to send me a text via iMessage or RCS")
- Laura Entis's dot keeps a running list of what she owes people from Slack and email, with links, why each matters and next steps; a team dot caught a $5,700 error in a retreat budget unprompted
```

### wiki/sources/newsletters/every-dots-guide-2026-10-23.md (new)

```
---
title: "Every — Dots: A Guide for Putting OpenAI's Always-on Agents to Work"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-23-dots-a-guide-for-putting-openais-always-on-agent.md
url: https://every.to/guides/openai-dots-guide
published: 2026-10-23
ingested: 2026-11-24
domains: [agents]
---

# Every — Dots: A Guide for Putting OpenAI's Always-on Agents to Work

Laura Entis's guide to setting up a dot, with seven workflows Every's team uses and a prompt for each. Only the free preview was read; the guide itself is paywalled.

## Influenced pages
- [ChatGPT dots](../../tools/chatgpt-dots.md) — Every team working-patterns bullet

## Key claims extracted
- Workflows include: a running list of commitments from Slack and email with links and next steps; catching inconsistencies across apps (an outdated article summary, launch emails referencing an unshipped feature); inbox triage and scheduling rules with the boundary "Don't send anything without my approval, and save any corrections I give you for next time"; multistep projects run from Slack
- At publication, the guide says dots "currently requires ChatGPT Business Premium" (superseded by the Pro, Business Premium and Enterprise rollout Every reported on 2026-10-29)
- Most useful for people juggling teams, clients or projects; focused, linear work may offer fewer reasons to use it
- The team has hit silent failures, unreliable connections and dropped tasks, so progress needs checking
```

### wiki/sources/newsletters/every-put-your-dot-to-work-2026-10-25.md (new)

```
---
title: Every — Put your Dot to work (recap, 2026-10-25)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-25-anthropics-duet-gets-to-work.md
url: https://every.to/context-window/anthropic-s-duet-gets-to-work
published: 2026-10-25
ingested: 2026-11-24
domains: [agents]
---

# Every — Put your Dot to work (recap, 2026-10-25)

The "Put your Dot to work" section of Every's 2026-10-25 Sunday recap, which lists team workflows from Laura Entis's dots guide. This page covers only that section; the newsletter's other stories are separate.

## Influenced pages
- [ChatGPT dots](../../tools/chatgpt-dots.md) — Every team working-patterns bullet

## Key claims extracted
- Add the dot to every Slack channel and ask it to be "as proactive as possible" about what needs attention
- A dot watching one engineer's coding threads warned that a tool update would break a colleague's scheduled automation before it next ran
- Give it a habit you skip: one dot reviews meeting transcripts and sends communication feedback through the day
- Phone it for a briefing: it sent a settings link, confirmed an event was insured and drafted the reply
- Keep one ongoing conversation; the dot starts each request as its own task and messages when done
- Correct it once and save the rule (no evening meetings without asking); tag it in a Slack thread to watch a job and report back there
```

## Schema / vocabulary additions

None.

## Open questions

None.
