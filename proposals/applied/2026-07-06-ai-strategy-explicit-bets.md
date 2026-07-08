---
type: proposal
sources:
  - raw/newsletters/2026-06-30-your-ai-strategy-is-making-bets-do-you-know-which.md
status: pending
created: 2026-07-06
---

# Proposal: AI strategy as explicit bets

## Summary
Every's strategy piece reframes AI strategy as a portfolio of explicit assumptions: token abundance, model-wrapper durability, provider lock-in, vertical specialization, and regulatory shocks. This is best handled as a training update rather than a factual product/model page.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add "make the bets explicit" strategy exercise.
    > **Add:** AI strategy should name the assumptions it depends on: cheap token supply, model-provider lock-in, wrapper durability, vertical specialization, data moat, regulatory exposure, and switching cost. Teams should write the failure condition for each bet before turning it into roadmap or vendor strategy.

- [x] **Update** `wiki/trends/proprietary-data-becomes-model-moat.md` — add vertical-app durability as a strategic bet, not a guarantee.

- [x] **Update** `wiki/trends/restricted-frontier-deployment.md` — cross-link regulatory and access shocks as assumptions every AI strategy should model.

- [x] **Create** `wiki/sources/newsletters/ai-strategy-explicit-bets-2026-06.md` — source summary.

## Updated Page Snippets

### `wiki/training/company-wide-ai-enablement.md`

> **Before:**
> `- Treat adoption as management and workflow design, not as software procurement`

> **After:**
> `- Treat adoption as management and workflow design, not as software procurement. Name the strategic bets behind the plan: cheap token supply, provider lock-in, wrapper durability, vertical specialization, data moat, regulatory exposure, and switching cost.`

### `wiki/trends/proprietary-data-becomes-model-moat.md`

> **Before:**
> `If this trend holds, "best model" stops being a single global ranking and becomes more local to a workflow or industry.`

> **After:**
> `If this trend holds, "best model" stops being a single global ranking and becomes more local to a workflow or industry. But vertical durability is a strategic bet, not a guarantee: teams should be explicit about whether their moat comes from proprietary data, workflow integration, distribution, regulation, or model-provider dependence.`

### `wiki/trends/restricted-frontier-deployment.md`

> **Before:**
> `If labs increasingly maintain a split between public-facing models and restricted internal or selective-access systems, state-of pages cannot assume that the most capable system is always the most publicly available one.`

> **After:**
> `If labs increasingly maintain a split between public-facing models and restricted internal or selective-access systems, state-of pages cannot assume that the most capable system is always the most publicly available one. AI strategies should treat regulatory and access shocks as explicit assumptions rather than background risk.`

## Page Drafts

### `wiki/sources/newsletters/ai-strategy-explicit-bets-2026-06.md` (new)

```md
---
title: AI strategy as explicit bets
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-30-your-ai-strategy-is-making-bets-do-you-know-which.md
published: 2026-06-30
ingested: 2026-07-06
domains: [training, agents, models]
---

# AI strategy as explicit bets

Every argues that AI strategies often hide their core assumptions. Token consumers rely on token abundance, wrapper companies rely on models not absorbing their orchestration layer, provider-specific products accept lock-in, vertical apps bet on workflow and data advantages, and regulation or access restrictions can shock any of these positions.

## Influenced pages
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — explicit-bets strategy exercise
- [Proprietary data becomes model moat](../../trends/proprietary-data-becomes-model-moat.md) — vertical durability as a bet
- [Restricted frontier deployment](../../trends/restricted-frontier-deployment.md) — regulation/access shock link

## Key claims extracted
- AI strategy should name its assumptions instead of treating them as background facts.
- Wrapper durability, provider lock-in, token abundance, and vertical specialization are all bets.
- Regulatory or access restrictions can change model availability and vendor strategy quickly.
```
