---
type: proposal
source: raw/newsletters/2026-10-20-the-programmable-data-center-evan-conrad-sf-com.md
status: pending
created: 2026-11-24
---

# Proposal: SF Compute's GPU order book and the inference-versus-rental price gap

## Summary

### In short
GPU time is becoming a traded commodity, and its prices are badly out of line: SF Compute's CEO says a B300 earns about $40 an hour selling inference but rents for $5–6. SF Compute runs a GPU exchange that delivers working compute rather than cash, matching orders by chip generation, interruptibility and time window, from one hour to three years ahead. The proposal adds a short "Compute markets" section to the compute-infrastructure trend page and one source page. The reason to hesitate is length: you kept the page whole at 119% of its ceiling, and this section takes it to about 137%.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 20 October 2026, Latent Space published an interview with Evan Conrad, CEO of SF Compute. SF Compute runs a market where companies buy and sell GPU time, now or in the future. Its key design choice is physical settlement, a futures-market term: the buyer receives usable compute, not a cash payment tied to a price index. Delivering compute forced the company to build most of a cloud's operations, though it owns no hardware, so that it cannot move its own forward prices.

Rather than wait for standard contracts, the order book matches orders that carry constraints: GPU generation, storage, whether a running job may be interrupted, and start and end times from one hour to three years out. The cost is wider gaps between buy and sell prices. Only about 5% of its capacity is on the order book so far. His headline number: a B300 earns about $40 an hour selling inference at full use, about $25 at 50% use, yet rents for $5–6 an hour, and "one of these numbers has to change." He also warns that price indices built on thin data can be manipulated, as LIBOR was, and argues that NVIDIA or any large hardware or inference business cannot run a neutral exchange.

### What changes
The compute-infrastructure trend page treats compute as a moat and quotes a framing of future infrastructure as "grid-like", with market coordination as a core problem, but has no material on how compute is actually bought, sold or priced.

- **Compute infrastructure as decisive competitive moat** gains a short "Compute markets" section after "Outputmaxxing": physical versus cash settlement, constraint-matching order books, the $40-versus-$5–6 gap, and the index-manipulation and neutrality arguments. It gains one Recent-changes entry dated 20 October; the list is at its cap of ten, so the oldest entry (5 May, Stripe's stolen-compute framing) moves to the page's history file. The page date stays 20 November.
- The index line for the page adds compute markets; its date stays 20 November.
- One new source page for the interview.

### What to weigh
The judgment call is placement against length. Compute markets sit awkwardly on a page whose thesis is that compute is a moat, but a separate trend page would be thin today, so the proposal files them as a section. That takes the page from about 1,425 to about 1,640 body words, roughly 137% of its 1,200-word ceiling. You already chose to keep this page whole, so no split is offered; the open question asks only whether compute markets should go to their own page instead.

## Intended changes

- [ ] **Update** `wiki/trends/compute-infrastructure.md` — insert a new `## Compute markets` section after `## Outputmaxxing`; add one Recent-changes entry dated 2026-10-20 between the 2026-10-22 and 2026-08-19 entries (list is at the 10-entry cap, so the oldest entry spills); `as_of` stays 2026-11-20 (newer than this source); append source id `latent-space-sf-compute-order-book-2026-10-20` to frontmatter and one line to `## Sources`
    > See draft below

- [ ] **Spill** `wiki/trends/compute-infrastructure.md` → `wiki/history/trends/compute-infrastructure.md` — the oldest Recent-changes entry (currently the 2026-05-05 Stripe stolen-compute entry; the Superhuman and Parallel Web Systems entries already spilled today) moves to history
    > See draft below

- [ ] **Update** `wiki/index.md` — add compute markets to the compute-infrastructure description; date stays 2026-11-20
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-sf-compute-order-book-2026-10-20.md` — source summary

## Page drafts

### wiki/trends/compute-infrastructure.md (updated)

Frontmatter: append `latent-space-sf-compute-order-book-2026-10-20` to `sources:`. `as_of` unchanged (2026-11-20).

New section, inserted after `## Outputmaxxing` and before `## Lab and subscription economics`:

```md
## Compute markets

GPU time is starting to trade like a commodity, and the grid-like framing above now has a working market behind it. SF Compute (CEO Evan Conrad, Latent Space, October 2026) runs a physically settled exchange: the buyer receives working compute, not a cash payment against an index. Delivering it meant building most of a cloud's operations, down to InfiniBand partitions customers can redraw on the fly. Instead of standard contracts, its order book matches orders that carry constraints (GPU generation, storage, whether a running job may be interrupted, start and end times from one hour to three years ahead), which trades concentrated liquidity for wider spreads. About 5% of its capacity is on the book; Conrad says buyers recover about $25 of every $100 by reselling unused time.

- **Inference versus rental gap:** by Conrad's numbers a B300 earns about $40/hr selling inference at full use (about $25 at 50%) but rents for $5–6/hr; one of the two prices has to move.
- **Index risk:** cash-settled compute indices built on thin data can be manipulated, as LIBOR was.
- **Neutrality:** Conrad argues no chip maker, cloud or large inference business can run a trusted exchange, because it could move the forward price; SF Compute owns no hardware for that reason.
```

Recent changes: adds one entry dated 2026-10-20, inserted between the 2026-10-22 and 2026-08-19 entries; then spills the oldest-dated entry to history (expected: the 2026-05-05 Stripe stolen-compute entry).

```md
- [2026-10-20] Added a Compute markets section: SF Compute's physically settled GPU order book, a B300 earning ~$40/hr on inference against $5–6/hr rental, and the index-manipulation and neutrality arguments.
```

Sources (appends one line):

```md
- [Latent Space — The Programmable Data Center (Evan Conrad, SF Compute)](../sources/newsletters/latent-space-sf-compute-order-book-2026-10-20.md)
```

### wiki/history/trends/compute-infrastructure.md (updated)

Appended at the end of the file (the entry is whichever is oldest at apply time; expected). The file already ends with a 2026-11-24 archive block; if applied on that date, add the entry to that block instead of opening a new header:

```md

## Archived from current page on <apply date>

- [2026-05-05] Stripe frames stolen compute (API keys, tokens, credits, free trials) as the emerging AI fraud surface — "compute is the new cash"; agents as autonomous purchasers create new commerce and payment-flow design challenges
```

### wiki/index.md (updated)

```md
- [trends/compute-infrastructure](trends/compute-infrastructure.md) — frontier compute scale plus inference-system efficiency as competitive moats; lab economics including Anthropic's S-1 and IPO; open inference serving (DeepInfer economics, TorchTPU, EAGLE-4); compute markets (SF Compute's physically settled GPU order book, inference-versus-rental price gap) *(as_of: 2026-11-20)*
```

### wiki/sources/newsletters/latent-space-sf-compute-order-book-2026-10-20.md (new)

```md
---
title: Latent Space — The Programmable Data Center (Evan Conrad, SF Compute)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-20-the-programmable-data-center-evan-conrad-sf-com.md
url: https://www.latent.space/p/sfcompute2
published: 2026-10-20
ingested: 2026-11-24
domains: [models]
---

# Latent Space — The Programmable Data Center (Evan Conrad, SF Compute)

Latent Space interview with SF Compute CEO Evan Conrad, recorded at AI Engineer New York's Compute Trading track. SF Compute runs a market for buying and selling GPU time now or in the future, settled physically: the buyer gets working compute. Conrad explains why that required building a cloud's operations, how the order book matches orders with different constraints instead of standard contracts, and why he thinks compute prices and indices are still far from settled.

## Influenced pages

- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — new Compute markets section

## Key claims extracted

- Physical settlement: buyers receive usable compute, not a cash payment against an index; delivering it required site visits, bill-of-materials design, backplane operation and supply-chain work
- SF Compute does not own hardware, so it cannot manipulate the forward market; customers can redraw InfiniBand partitions on the fly
- The order book matches orders carrying constraints (GPU generation, storage, interruptibility, start and end time from one hour to three years ahead) rather than waiting for standardized contracts; the trade-off is wider buy-sell spreads
- Interrupting a batch job and interrupting a live inference service are priced differently, since a live service owes its own customers an SLA
- About 5% of SF Compute's capacity is on the order book; a customer spending $100 on capacity recovers about $25 on average by reselling unused time
- A B300 earns about $40/hr selling inference at full use (about $25/hr at 50% use) but rents for $5–6/hr
- Compute indices built on small amounts of data can be manipulated, as LIBOR was
- NVIDIA, clouds and large inference businesses cannot run a neutral exchange; Silicon Data and Compute Exchange are named as fellow early players
```

## Schema / vocabulary additions

None.

## Open questions

- You kept this page whole at 119% of its ceiling; the new section takes it to about 1,640 body words, roughly 137%. File compute markets as a section here (assumed), or as a short trend page of their own with a one-line pointer from this page, which would leave this page at 119%?
