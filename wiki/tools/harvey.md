---
title: Harvey
type: tool
domains: [legal]
subcategory: legal-ai
tags: [closed-source, agentic]
as_of: 2026-04-02
sources: [harvey-legal-is-next, ainews-ideogram-june-2026]
---

# Harvey

Harvey is a legal AI platform aimed at law firms and in-house legal teams. June 2026 benchmark disclosure shows meaningful evidence of the hybrid model routing strategy working in production legal work.

## Current status (as of 2026-06-04)

- Active company; raised at $11B valuation (prior)
- Marketed surfaces: **Assistant**, **Vault**, **Knowledge**, **Workflow Agents**
- Solution areas: Innovation, In-House, Transactional, Litigation, Mid-Sized Firms, Collaboration
- **Hybrid routing benchmark (June 2026):**
  - GLM 5.1 (main worker) + Claude Opus 4.7 (advisor): **18% all-pass rate** vs 14% for pure Opus 4.7
  - Cost: **$368 vs $954 per 100 tasks** (~60% cost reduction with better accuracy)
  - SFT-tuned Kimi K2.6: 15% all-pass at roughly **11x lower cost** than Opus 4.7 alone
- Runs **Spectre** internally: autonomous agent handling engineering and non-engineering work triggered by incidents, bug reports, Slack messages — not a product

## Strengths

- Hybrid routing strategy validates multi-model orchestration at production legal-task scale
- Cost reduction (60%) alongside accuracy improvement is an unusual combination

## Weaknesses / caveats

- All benchmarks are Harvey's own evaluations; independent replication not yet available
- Source coverage remains limited — the April 2026 page creation and June 2026 benchmark are the only two ingested data points

## Recent changes

- [2026-06-04] Hybrid routing results disclosed: GLM 5.1 + Opus 4.7 advisor = 18% all-pass vs 14% pure Opus, at $368 vs $954/100 tasks; Kimi SFT at 15% for 11x lower cost
- [2026-04-02] Page created from Harvey's "Legal is Next" post — initial stub

## Sources

- [AINews — Ideogram 4, Reve 2 (June)](../sources/newsletters/ainews-ideogram-june-2026.md)
- [Autonomous agents are transforming engineering. Legal is next. (Pereyra / Harvey)](../sources/articles/harvey-legal-is-next.md)
