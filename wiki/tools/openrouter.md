---
title: OpenRouter
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [closed-source, agentic]
as_of: 2026-08-17
sources: [ainews-stripe-openrouter-2026-08-17]
---

# OpenRouter

OpenRouter is a model-routing and aggregation API: a single integration point that lets developers call many different LLM providers' models, with standardized request/response formats, fallback paths when a provider is unavailable, and an "Auto" mode that routes each request to a model automatically.

## Current status (as of 2026-08-17)

- Acquired by Stripe for a reported $7B, closing 90 days after OpenRouter's $1.3B Series B
- Revenue: ~$140M annualized, ~70% gross margin
- Volume: 250 trillion tokens/month routed, up 5x from 50 trillion in February 2026
- "Auto" mode routes requests to a model automatically; underlying router-training approach is comparable to Not Diamond's customer-specific trained routers (see [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md))
- Used in practice as a multi-model integration layer (e.g. Spiral routes prose through Sonnet 4.6, a top-edit pass through Gemini 2.5 Flash, and file summaries through a smaller OpenAI model, all via OpenRouter) for both cost and provider-outage resilience

## Why it matters

A striking monetization outcome for a layer that mostly takes a routing markup — evidence that model aggregation/routing has become valuable infrastructure in its own right, not just a developer convenience. See [Glean](glean.md) for a parallel enterprise-side routing architecture from the same week, and [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) for the broader routing-discipline pattern this page is one instance of.

## Weaknesses / caveats

- The acquisition is reported via AINews/press coverage, not a joint Stripe/OpenRouter press release
- Margin durability is an open question raised by outside commentary: OpenRouter's economics depend on a routing markup that could compress toward zero as zero-markup competitors (cloud-native routers, open-source routers) emerge

## Recent changes

- [2026-08-17] Page created: Stripe's reported $7B acquisition of OpenRouter, on ~$140M ARR and 250T tokens/month routed (up from 50T in February).

## Sources

- [AINews — Stripe buys OpenRouter for $7B](../sources/newsletters/ainews-stripe-openrouter-2026-08-17.md)
