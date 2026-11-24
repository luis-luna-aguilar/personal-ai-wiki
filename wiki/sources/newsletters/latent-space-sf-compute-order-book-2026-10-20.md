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
