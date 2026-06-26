---
type: proposal
source: raw/newsletters/2026-06-04-ainews-reve-2-and-ideogram-4-layouts-in-imagege.md
status: pending
created: 2026-06-24
---

# Proposal: Harvey hybrid routing beats pure flagship at 60% the cost

## Summary

Harvey (legal AI) published benchmark results showing a hybrid routing strategy — GLM 5.1 as primary worker + Claude Opus 4.7 as advisor — achieves 18% all-pass accuracy vs 14% for pure Opus 4.7, at $368 vs $954 per 100 tasks. This is the first high-quality third-party validation of the multi-model advisor pattern in a real legal domain.

## Intended changes

- [ ] **Update** `wiki/tools/harvey.md` — major content update; add hybrid routing benchmark results, model strategy, SFT data point
    > See draft below

- [ ] **Update** `wiki/workflows/advisor-strategy.md` — add Harvey as third-party proof point for the advisor pattern; update Recent changes
    > **Add to Reported results section:**
    >
    > ### External replication: Harvey (legal domain, June 2026)
    > Harvey benchmarked the hybrid pattern on legal task completion. Results (vendor's own evals, not independent):
    > - **GLM 5.1 + Claude Opus 4.7 advisor** vs Opus 4.7 alone: **18% all-pass** vs **14%**, at **$368 vs $954** per 100 tasks
    > - SFT-tuned Kimi K2.6 achieved 15% accuracy at roughly 11× lower cost than Opus 4.7 alone
    > - This mirrors the Anthropic pattern: executor + frontier-advisor outperforms either alone; task accuracy and cost move in opposite directions
    >
    > **Add to Recent changes:**
    > `- [2026-06-04] Harvey external validation: GLM 5.1 + Opus 4.7 advisor achieves 18% vs 14% all-pass on legal tasks at $368 vs $954/100 tasks; SFT Kimi K2.6 reaches 15% at 11× lower cost`

- [ ] **Create** `wiki/sources/newsletters/ainews-ideogram-june-2026.md` — source summary for the June 4 AINews newsletter (also covers Ideogram 4 and enterprise spend signals)
    > See draft below

## Page drafts

### wiki/tools/harvey.md (updated)

````md
---
title: Harvey
type: tool
domains: [legal]
subcategory: legal-ai
tags: [closed-source, agentic]
as_of: 2026-06-04
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
  - SFT-tuned Kimi K2.6: 15% all-pass at roughly **11× lower cost** than Opus 4.7 alone
- Runs **Spectre** internally: autonomous agent handling engineering and non-engineering work triggered by incidents, bug reports, Slack messages — not a product

## Strengths

- Hybrid routing strategy validates multi-model orchestration at production legal-task scale
- Cost reduction (60%) alongside accuracy improvement is an unusual combination

## Weaknesses / caveats

- All benchmarks are Harvey's own evaluations; independent replication not yet available
- Source coverage remains limited — the April 2026 page creation and June 2026 benchmark are the only two ingested data points

## Recent changes

- [2026-06-04] Hybrid routing results disclosed: GLM 5.1 + Opus 4.7 advisor = 18% all-pass vs 14% pure Opus, at $368 vs $954/100 tasks; Kimi SFT at 15% for 11× lower cost
- [2026-04-02] Page created from Harvey's "Legal is Next" post — initial stub

## Sources

- [AINews — Ideogram 4 layouts, Harvey routing (June 4)](../../sources/newsletters/ainews-ideogram-june-2026.md)
- [Autonomous agents are transforming engineering. Legal is next. (Pereyra / Harvey)](../../sources/articles/harvey-legal-is-next.md)
````

### wiki/sources/newsletters/ainews-ideogram-june-2026.md (new)

````md
---
title: AINews — Ideogram 4 layouts, Harvey routing, enterprise spend (June 4)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-04-ainews-reve-2-and-ideogram-4-layouts-in-imagege.md
published: 2026-06-04
ingested: 2026-06-24
domains: [models, coding, creative]
---

# AINews — Ideogram 4 layouts, Harvey routing, enterprise spend (June 4)

AINews newsletter covering: Ideogram 4.0 Arena placement (#8 overall, #1 open image model); Harvey hybrid routing benchmark (GLM 5.1 + Opus 4.7 = 18% vs 14% legal all-pass at 60% cost); Uber $1,500/month AI spend cap; MACU multi-agent DAG results; Gemma 4 12B Apache 2.0 release; MAI-Thinking-1 Frontier Tuning detail.

## Influenced pages

- [Harvey](../../tools/harvey.md) — hybrid routing benchmark added
- [Advisor strategy](../../workflows/advisor-strategy.md) — Harvey as third-party proof point
- [Ideogram 4.0](../../models/ideogram-4.md) — Arena results (see cosmos-3-ideogram-4 proposal)
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — enterprise spend controls (see enterprise-spend proposal)

## Key claims extracted

- Harvey: GLM 5.1 + Opus 4.7 advisor → 18% legal all-pass vs 14% pure Opus; $368 vs $954/100 tasks
- SFT Kimi K2.6: 15% accuracy at 11× lower cost than Opus 4.7
- Ideogram 4.0 Arena: #8 overall, #1 open image model; strong text rendering + branding
- Uber: $1,500/month per-engineer AI spend cap
- MACU multi-agent DAG: 4.7–25.5% improvement, 1.5× faster on Odysseys benchmark
- Gemma 4 12B: Apache 2.0, encoder-free multimodal
- MAI-Thinking-1 Frontier Tuning: RL environments for workflow-specific adaptation; internal Excel-tuned models reach GPT-5.4-level at 10× efficiency
````
