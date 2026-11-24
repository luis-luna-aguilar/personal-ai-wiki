---
title: Harvey
type: tool
domains: [legal]
subcategory: legal-ai
tags: [closed-source, agentic]
as_of: 2026-09-17
sources: [harvey-legal-is-next, ainews-ideogram-june-2026, openai-astra-for-law-2026-09-17, harvey-astra-for-law-plugin-2026-09-17]
---

# Harvey

Harvey is a legal AI platform aimed at law firms and in-house legal teams. June 2026 benchmark disclosure shows meaningful evidence of the hybrid model routing strategy working in production legal work. Since September 2026 it also sits on top of, and inside, OpenAI's legal stack: a Harvey plugin runs in ChatGPT Enterprise, and Harvey builds on OpenAI's [Astra for Law](astra-for-law.md) configuration.

## Current status (as of 2026-09-17)

- Active company; raised at $11B valuation (prior)
- Marketed surfaces: **Assistant**, **Vault**, **Knowledge**, **Workflow Agents**
- Solution areas: Innovation, In-House, Transactional, Litigation, Mid-Sized Firms, Collaboration
- **Hybrid routing benchmark (June 2026):**
  - GLM 5.1 (main worker) + Claude Opus 4.7 (advisor): **18% all-pass rate** vs 14% for pure Opus 4.7
  - Cost: **$368 vs $954 per 100 tasks** (~60% cost reduction with better accuracy)
  - SFT-tuned Kimi K2.6: 15% all-pass at roughly **11x lower cost** than Opus 4.7 alone
- Runs **Spectre** internally: autonomous agent handling engineering and non-engineering work triggered by incidents, bug reports, Slack messages — not a product
- **OpenAI partnership (2026-09-17):** Harvey's plugin inside ChatGPT Enterprise lets lawyers reach Harvey from ChatGPT, and Harvey will build on [Astra for Law](astra-for-law.md) in its own products. Harvey's Head of Applied Research, Niko Grupen, said early Astra for Law testing showed strength in grounding answers in on-point authorities, precise citation, and practical advisory guidance.

## Strengths

- Hybrid routing strategy validates multi-model orchestration at production legal-task scale
- Cost reduction (60%) alongside accuracy improvement is an unusual combination

## Weaknesses / caveats

- All benchmarks are Harvey's own evaluations; independent replication not yet available
- Source coverage remains limited: the April 2026 post, the June 2026 benchmark, and the September 2026 OpenAI partnership are the ingested data points

## Recent changes

- [2026-09-17] Launched a Harvey plugin inside ChatGPT Enterprise and said it will build on OpenAI's Astra for Law configuration in its own products.
- [2026-06-04] Hybrid routing results disclosed: GLM 5.1 + Opus 4.7 advisor = 18% all-pass vs 14% pure Opus, at $368 vs $954/100 tasks; Kimi SFT at 15% for 11x lower cost
- [2026-04-02] Page created from Harvey's "Legal is Next" post — initial stub

## Sources

- [AINews — Ideogram 4, Reve 2 (June)](../sources/newsletters/ainews-ideogram-june-2026.md)
- [Autonomous agents are transforming engineering. Legal is next. (Pereyra / Harvey)](../sources/articles/harvey-legal-is-next.md)
- [Introducing Astra for Law (OpenAI)](../sources/articles/openai-astra-for-law-2026-09-17.md)
- [Harvey (@harvey) — Harvey plugin for Astra for Law in ChatGPT Enterprise](../sources/tweets/harvey-astra-for-law-plugin-2026-09-17.md)
