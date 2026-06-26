---
title: Kimi K2.7-Code
type: model
domains: [models, coding]
subcategory: coding-model
tags: [moonshot-ai, open-weights, agentic]
as_of: 2026-06-13
sources: [kimi-k27-code-june-2026]
---

# Kimi K2.7-Code

Moonshot AI's June 2026 open-source coding model. Successor to Kimi K2.6. 1T total / 32B active MoE with MLA attention, 256K context. Claims strong improvements in coding task efficiency — 30% fewer reasoning tokens than K2.6 on the same tasks.

## Current status (as of 2026-06-13)

- 1T total / 32B active MoE; MLA attention; 256K context
- Open-source; vLLM and SGLang support on day of release
- **Benchmark claims (Moonshot-reported):**
  - +21.8% on Kimi Code Bench v2
  - +11.0% on Program Bench
  - +31.5% on MLS Bench Lite
  - 30% fewer reasoning tokens than K2.6
  - KernelBench-Hard: more authentic Triton kernels than K2.6 (qualitative community signal)
- Community reception: honest benchmark behavior, solid step up from K2.6; several benchmarks are Moonshot's own

## Caveats

- Primary benchmark comparisons are Moonshot-reported; independent leaderboard positions not yet available
- Released the same week as GLM-5.2, which received more community attention
- K2.6's long-horizon execution demos (12+ hour runs, 4K+ tool calls) have not been replicated publicly for K2.7-Code yet

## Recent changes

- [2026-06-13] Released as open-source; supersedes Kimi K2.6

## Sources

- [Kimi K2.7-Code release — AINews June 2026](../sources/newsletters/kimi-k27-code-june-2026.md)
