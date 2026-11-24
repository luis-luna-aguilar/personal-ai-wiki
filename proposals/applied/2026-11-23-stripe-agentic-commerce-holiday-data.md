---
type: proposal
source: raw/tweets/2026-11-20-ernietedeschi-2123852064027471901.md
status: pending
created: 2026-11-23
---

# Proposal: Stripe agentic commerce data ahead of the 2026 holiday season

## Summary

### In short
Consumer agent shopping has moved past novelty: spend through Stripe's Link Agent Wallet rose about 80-fold between early September and mid-November, doubled in the last month alone, and more than half of first-time agent buyers come back to buy again. Travel leads, with over 40% of volume, ahead of retail at about a third. The proposal adds one data bullet to the agent-commerce section of **State of Finance**, names the wallet on **Meta Muse**'s commerce line, and creates one source page. The reason to hesitate is scope: this is consumer shopping data filed on the finance dashboard, because the wiki has no agentic-commerce page.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 20 November 2026 Ernie Tedeschi, Stripe's chief economist, posted a one-minute X article with new Stripe data on consumer agentic commerce, meaning purchases that a personal AI agent completes on a person's behalf. He timed it to the week before the holiday season, which he calls the first one with agents doing the shopping. The data comes from Link Agent Wallet, the Stripe Link payment wallet that personal agents use to pay. Tedeschi names Meta's Muse, Instinct and Grok as agents that run on it.

Three findings stand out. First, growth: daily spend through the wallet, measured as a seven-day rolling average, was nearly 80 times higher in mid-November than at the start of September, and it doubled over the last month. Second, the category mix: last week more than 40% of volume went to airfare, travel and lodging, roughly a third to retail and a quarter to everything else. In a reply, Tedeschi explains why travel leads: flights are expensive, buyers know prices vary by seller, and an agent that compares fares saves money and earns points. Third, stickiness: more than half of consumers who make one agentic purchase make at least a second, usually in the same category. The post gives only relative growth with no dollar volumes, and its September baseline sits right at Muse's launch. Stripe says it will publish updates around Black Friday and Cyber Monday.

### What changes
The wiki has a short "Agent-native commerce and fraud" section on State of Finance, which says that agents are starting to buy things but gives no figures. The Meta Muse page records that Muse pays through Stripe Link.

- **State of Finance** gains one bullet in that section with the growth, category mix and repeat-purchase figures, a Recent-changes entry dated 20 November and the new source. The page date stays at 23 November.
- **Meta Muse** has its commerce line extended to name Link Agent Wallet and the wallet-wide growth, and gains a Recent-changes entry and the source. Page date moves to 20 November.
- One new source page for the Tedeschi post.

### What to weigh
The figures cover the whole wallet across Muse, Instinct and Grok, not Muse alone, so the Muse bullet says so and does not credit Muse with the 80x. Grok and Instinct pages get nothing: the wiki has no page for Instinct, and nothing in the wiki ties the Grok agent that Tedeschi names to its Grok Bot page.

## Intended changes

- [ ] **Update** `wiki/state-of/finance.md` — add one bullet to "Agent-native commerce and fraud"; adds one Recent-changes entry dated 2026-11-20 (list goes to 9 of 10, no spill); append `stripe-agentic-commerce-holiday-2026-11-20` to frontmatter `sources:` and one line to `## Sources`; `as_of` stays 2026-11-23
    > See draft below

- [ ] **Update** `wiki/tools/meta-muse.md` — extend the Commerce bullet; adds one Recent-changes entry dated 2026-11-20 (list goes to 5, no spill); append source id and Sources line; `as_of` and Current-status stamp 2026-10-13 → 2026-11-20
    > See draft below

- [ ] **Create** `wiki/sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md` — source summary

## Page drafts

### wiki/state-of/finance.md (updated)

Frontmatter `sources:` appends `stripe-agentic-commerce-holiday-2026-11-20`; `as_of` unchanged (2026-11-23).

In `### Agent-native commerce and fraud`, insert after the "Agents as purchasers" bullet:

```
- **Agent spend is ramping fast.** Stripe's Link Agent Wallet, which pays for personal agents including [Meta Muse](../tools/meta-muse.md), saw daily spend rise ~80x from early September to mid-November and double in the last month; travel takes >40% of volume, retail ~1/3, and over half of first-time agent buyers buy again *(as of 2026-11-20)*
```

In `## Recent changes`, insert directly below the 2026-11-23 entry:

```
- [2026-11-20] Stripe agentic commerce data (Ernie Tedeschi): Link Agent Wallet daily spend ~80x since early September and doubled in a month; travel >40% of volume, retail ~1/3; over half of first-time agent buyers return. Added to Agent-native commerce.
```

In `## Sources`, append:

```
- [Ernie Tedeschi (Stripe) — agentic commerce data ahead of the 2026 holiday season](../sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md)
```

### wiki/tools/meta-muse.md (updated)

Frontmatter changes:

```
as_of: 2026-11-20
sources: [ainews-navier-stokes-2026-09-09, ainews-muse-local-hijack-2026-09-22, ainews-meta-connect-2026-09-24, ainews-muse-wonder-launch-2026-10-13, stripe-agentic-commerce-holiday-2026-11-20]
```

Heading change: `## Current status (as of 2026-10-13)` → `## Current status (as of 2026-11-20)`

Commerce bullet, replaced:

```
- **Commerce:** pays through Stripe's Link Agent Wallet with an agentic payment-protection/refund guarantee; Shop Pay incoming. Day-one usage was 10x Meta's internal projections. Stripe reports wallet-wide daily spend (Muse, Instinct and Grok combined) up ~80x from early September to mid-November, led by travel ([State of Finance](../state-of/finance.md))
```

In `## Recent changes`, insert at the top:

```
- [2026-11-20] Stripe data: daily spend on Link Agent Wallet, the wallet behind Muse purchases, up ~80x since early September across all agents using it.
```

In `## Sources`, append:

```
- [Ernie Tedeschi (Stripe) — agentic commerce data ahead of the 2026 holiday season](../sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md)
```

### wiki/sources/tweets/stripe-agentic-commerce-holiday-2026-11-20.md (new)

```
---
title: Ernie Tedeschi (Stripe) — agentic commerce data ahead of the 2026 holiday season
type: source
source_type: tweet
source_file: raw/tweets/2026-11-20-ernietedeschi-2123852064027471901.md
url: https://x.com/ernietedeschi/status/2123852064027471901
published: 2026-11-20
ingested: 2026-11-23
domains: [finance, agents]
---

# Ernie Tedeschi (Stripe) — agentic commerce data ahead of the 2026 holiday season

Short X article by Stripe's chief economist releasing Stripe data on consumer agentic commerce (purchases completed by personal AI agents) the week before the 2026 holiday season. The data covers Link Agent Wallet, the Stripe Link wallet that pays for personal agents including Meta Muse, Instinct and Grok. It reports fast growth, a travel-led category mix and high repeat purchase. In a reply, Tedeschi attributes travel's lead to flights being big-ticket purchases where comparison shopping pays off in both savings and points.

## Influenced pages
- [State of Finance](../../state-of/finance.md) — new data bullet in Agent-native commerce and fraud
- [Meta Muse](../../tools/meta-muse.md) — commerce line names Link Agent Wallet and its growth

## Key claims extracted
- Link Agent Wallet daily spend (7-day rolling average) was nearly 80x higher in mid-November than at the start of September 2026; spend doubled in the last month
- Growth is relative only; no dollar volumes given
- Last week: >40% of Link agentic spend on airfare, travel and lodging; ~1/3 retail; ~1/4 other
- More than half of consumers who make one agentic purchase make at least a second, typically in the same category
- Stripe plans further updates around Black Friday/Cyber Monday
```

## Schema / vocabulary additions

None.

## Open questions
- Agentic-commerce material now sits in a State of Finance section plus scattered tool-page lines. When Stripe's promised Black Friday/Cyber Monday follow-up arrives, should it seed a dedicated `trends/` page on consumer agentic commerce (assumed: not yet, one data post is not enough)?
	- Yes, dedicated
