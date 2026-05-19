---
type: proposal
sources:
  - raw/articles/2026-05-19-tco-8cvjj5fczp.md
  - raw/articles/2026-05-19-tco-8cvjj5fczp-1.md
status: pending
created: 2026-05-19
---

# Proposal: Shopify Claude Code fleet patterns — LLM proxy, CLAUDE.md discipline, permission config

## Summary

A synthesis of Shopify's internal Claude Code practices (from a Bessemer conference writeup, surfaced via @darkzodchi tweet). Five concrete patterns: (1) LLM proxy — tool-agnostic centralized gateway routing Claude Code, Copilot, and Cursor through one infrastructure layer for cost control and model swapping; (2) parallel agents in separate terminals; (3) critique loop before final answer; (4) CLAUDE.md committed to git, shared across all engineers, ~60-line limit; (5) permission config with explicit allow/deny lists. Reported outcome: 20% productivity gain and a 70%/30% strategy-to-execution ratio (was 30%/70% in 2024); Q3 target of 90% autonomous coding.

Note: primary source tweet content was not fetched (`fetched: false`). The triage signal description captures the key claims. The wiki already holds significant Shopify content from the April 2026 Latent Space podcast; these patterns are additive and complement existing evidence.

## Intended changes

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add new Shopify patterns under `## Proven patterns` (LLM proxy, CLAUDE.md discipline, explicit permission config) and update `## Evidence from practice` with productivity gain and strategy-to-execution ratio
    > See diff below

- [x] **Update** `wiki/concepts/harness.md` — add LLM proxy pattern as a fleet-management layer note
    > See diff below

- [x] **Create** `wiki/sources/articles/shopify-claude-code-bessemer-2026-05.md` — source summary

## Page drafts

### wiki/training/ai-enablement-software-development.md — additions

**Add to `## Proven patterns`:**

```md
- **LLM proxy as fleet infrastructure.** Shopify routes all AI coding tools (Claude Code, Copilot, Cursor) through a centralized LLM proxy gateway. Benefits: cost control from one layer, model swapping without reconfiguring every developer's tool, and tool-agnostic contracts. Prevents fragmented per-tool billing and enables org-wide model policy enforcement.
- **CLAUDE.md discipline: committed, shared, bounded.** Shopify commits CLAUDE.md to git and shares it across all 23,000 engineers. Hard length cap: ~60 lines. Key insight: "stuffing it makes performance worse." The quality of durable context decays with length — fewer, higher-quality instructions outperform comprehensive-but-diluted ones.
- **Explicit permission config as fleet policy.** Shopify deploys a standardized allow/deny list across all Claude Code instances: allow `read`, `write`, `test`, `lint`, `commit`; deny `push`, `deploy`, `drop`, `secrets`. This separates safe local work from risky external actions at the configuration layer, not per-session.
```

**Add to `## Evidence from practice`:**

```md
- Shopify (May 2026, Bessemer conference, @darkzodchi synthesis): LLM proxy, CLAUDE.md discipline, critique loop, permission config deployed fleet-wide across 23,000 engineers. Reported 20% productivity gain. Strategy-to-execution ratio flipped from 30%/70% (2024) to 70%/30% (2026). Q3 2026 target: 90% autonomous coding.
```

**Update `as_of`:** `2026-05-19`

### wiki/concepts/harness.md — addition to `## What good harness engineering looks like`

```md
- **LLM proxy as the fleet management layer.** At org scale (Shopify, 23K engineers), routing all AI coding-tool traffic through a centralized LLM proxy creates a control plane for cost, model choice, and policy enforcement without requiring per-tool reconfiguration. This positions the proxy as part of the enterprise harness boundary — above the individual tool harness, below the model.
```

### wiki/sources/articles/shopify-claude-code-bessemer-2026-05.md (new)

```md
---
title: Shopify Claude Code fleet patterns — Bessemer conference synthesis
type: source
source_type: article
url: https://x.com/zodchiii/status/2056319284641460626
published: 2026-05-19
ingested: 2026-05-19
domains: [coding]
---

# Shopify Claude Code fleet patterns — Bessemer conference synthesis

@darkzodchi synthesis of Shopify's internal Claude Code practices from a Bessemer conference writeup. Five fleet-wide patterns: LLM proxy, parallel terminals, critique loop, git-committed CLAUDE.md (~60-line cap), and explicit permission config (allow read/write/test/lint/commit; deny push/deploy/drop/secrets). Outcomes: 20% productivity gain; 70%/30% strategy-to-execution ratio; Q3 target 90% autonomous coding.

Note: primary source was a tweet pointing to the Bessemer writeup; content was not fetched. Key claims extracted from the triage signal description.

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — new Shopify patterns, productivity data, strategy-to-execution ratio
- [Harness (concept)](../../concepts/harness.md) — LLM proxy as fleet management layer

## Key claims extracted

- LLM proxy: centralized gateway for Claude Code + Copilot + Cursor; cost control + model swapping in one layer
- Parallel agents in separate terminals for independent tasks
- Critique loop: propose → critique → revise → critique before final answer
- CLAUDE.md committed to git; shared across 23,000 engineers; ~60-line hard cap ("stuffing it makes performance worse")
- Permission config: allow read/write/test/lint/commit; deny push/deploy/drop/secrets
- 20% productivity gain reported
- Strategy-to-execution ratio: 30%/70% (2024) → 70%/30% (2026)
- Q3 2026 target: 90% autonomous coding
```
