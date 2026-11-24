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
