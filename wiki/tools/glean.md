---
title: Glean
type: tool
domains: [agents, computer-use]
subcategory: ai-assistant
tags: [closed-source, agentic]
as_of: 2026-08-18
sources: [glean-model-routing-2026-08-18, ainews-stripe-openrouter-2026-08-17]
---

# Glean

Glean is an enterprise AI platform that co-founder Arvind Jain describes as "one really powerful personal co-worker" — a meta-harness combining the practical value of ChatGPT, Claude, Gemini, and Grok inside one product grounded in a company's own data, knowledge, and workflows.

## Current status (as of 2026-08-18)

- Valued at $7.2B after a $150M Series F; reached $300M ARR in 2026, a 3x increase over 15 months
- Three-tier model routing: employees can choose a model explicitly, admins can restrict or cap models, and an automatic mode routes per task — customers overwhelmingly pick automatic mode, for cost reasons
- Waldo, Glean's "agentic search model" (introduced April 2026), sits ahead of the LLM call: it decides how to break a query down, which tools to use, and when it has enough evidence, assembling the "raw materials" before handing off to a frontier model — saving tokens that would otherwise go to retrieval
- Claims roughly 4x cost-efficiency versus Claude Cowork ($0.45/task vs. $1.84), attributed to harness and routing design rather than a cheaper underlying model
- Evaluates its own router by running the chosen model in parallel with cheaper and pricier alternatives on a small sample of live traffic, scored by AI judges, feeding results back continuously
- Reports 80% adoption across 7,000 employees at Zillow; "first AI platform adopted company-wide" at Booking.com
- Jain: enterprise interest in open-weight models went from "minuscule" a year ago to "a key part of AI strategy" at most customers in the last three months, driven by cost

## Why it matters

Concrete, named-customer evidence that enterprise AI value is shifting toward the routing/orchestration layer sitting in front of models, not only which frontier model a company licenses. See [OpenRouter](openrouter.md) for a parallel consumer/developer-side routing business from the same week.

## Weaknesses / caveats

- Cost-efficiency and adoption figures are self-reported by Glean's co-founder in an interview, not independently benchmarked
- No independent leaderboard or benchmark of Glean's own product performance is captured here

## Recent changes

- [2026-08-18] Page created from a Latent Space interview with co-founder Arvind Jain covering Glean's model-routing architecture (Waldo, three-tier routing, cost claims vs. Claude Cowork), alongside the same week's Stripe–OpenRouter acquisition news.

## Sources

- [Frontier model cost and open-weights popularity is driving demand for model routing](../sources/newsletters/glean-model-routing-2026-08-18.md)
- [AINews — Stripe buys OpenRouter for $7B](../sources/newsletters/ainews-stripe-openrouter-2026-08-17.md)
