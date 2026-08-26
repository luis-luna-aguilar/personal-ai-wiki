---
title: Windsurf
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [closed-source, agentic]
as_of: 2026-07-14
sources: [devinai-blog-windsurf-adaptive]
---

# Windsurf

Windsurf is Cognition's AI coding workspace — this announcement was published on Devin's (Cognition's) blog, reflecting Windsurf's integration under the same company. On 2026-07-14, Cognition shipped an **Adaptive** model router, a redesigned model picker with pricing transparency, and removed daily usage limits for Max subscribers, in direct response to user complaints that the product's newer token-based pricing was too opaque and too restrictive.

## Current status (as of 2026-07-14)

- **Adaptive router:** automatically selects the best underlying model per task to avoid overusing premium models and make quota last longer; billed at a flat per-token rate — $0.50/M input, $2.00/M output, $0.10/M cache read as a promotional rate for the first two weeks; rolling out to all self-serve tiers (Pro, Max, Teams)
- **Model picker redesign:** shows live token pricing per model (e.g. Claude Opus 4.6), a prompt-cache timer integrated into the context window indicator, and post-message token/cost breakdowns
- **Max plan daily limits removed:** only the weekly quota remains for Max users, aimed at bursty power-user workflows; daily limits remain on other tiers as a spend safety net
- Cognition says it is building a more efficient harness for Windsurf with a multi-model architecture and subagents, to be detailed later

## Why it matters

The changes are a direct response to backlash over Windsurf's token-based pricing model: opaque billing and daily caps that especially penalized heavy users. Adaptive routing and transparent per-token pricing mirror a broader industry pattern — cost-aware model routing — now applied to a per-seat coding product rather than an API.

## Recent changes

- [2026-07-14] Launched Adaptive model router, transparent model-picker pricing (with prompt-cache timer), and removed Max-plan daily limits.

## Sources

- [Introducing Adaptive: a smarter way to use Windsurf](../sources/articles/devinai-blog-windsurf-adaptive.md)
