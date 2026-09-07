---
title: Kimi K3
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [moonshot-ai, open-weights, agentic]
as_of: 2026-07-28
sources: [ainews-kimi-k3-2026-07-17, ainews-much-ado-about-open-weights-2026-07-28, ainews-laguna-kratsios-2026-07-23]
---

# Kimi K3

Moonshot AI's flagship, now shipped in full: weights, tech report, and supporting infrastructure released 2026-07-28 under a "kimi-k3" license. Supersedes [Kimi K2.7-Code](../history/models/kimi-k2-7-code.md) as Moonshot's current flagship; broader in scope than its coding-specialist predecessor.

## Current status (as of 2026-07-28)

- 2.8T total parameters, 104B active per token across 896 experts (16 active per token); 1M-token context; native text+image multimodal input
- Open-sourced alongside three companion projects: FlashKDA (Kimi Delta Attention kernels), MoonEP (MoE communication library), AgentENV (distributed agent-environment infrastructure) — a fairly complete recipe for large-scale agentic post-training, not just a checkpoint
- License is "open weights" with commercial carve-outs, not OSI-style open source: hosts over $20M/year revenue need a separate agreement; products above 100M MAU or $20M/month revenue must display "Kimi K3" in their UI
- Day-0 distribution across vLLM, Baseten, Modal, Fireworks, Nebius, Together, DigitalOcean, Cursor, Cognition, Ollama Cloud, and Dell Enterprise Hub
- Independent evals confirm K3 now beats Opus 4.8: #1 among open-weight models on Agent Arena (+9.75% net improvement), #1 overall in Frontend Code Arena, and Cognition reports it's the first open-weight model to "approach frontier-level performance" on FrontierCode 1.1 (58.2%, 63.6% pass rate)
- Reported ~2.5x scaling-efficiency improvement over K2, driven by numerical-stability choices at extreme scale (MXFP4 weights / MXFP8 activations); the tech report omits total training tokens

## Caveats

- Hallucination rate on Artificial Analysis's Omniscience eval regressed to 51% (from K2.6's 39%) despite the accuracy gain
- Disputed: US Tech & Science Advisor Michael Kratsios accused Moonshot of "large-scale, covert industrial distillation" of Anthropic's Fable, citing GB300 chip access in Thailand; Treasury has signaled possible Entity List sanctions. Technical critics note only ~15 days separated Fable's release from K3's announcement, making full distillation-driven capability transfer implausible on that timeline — unresolved as of this writing.
- At 104B active parameters, local deployment requires server-class or multi-GPU hardware; not practical on consumer GPUs

## Recent changes

- [2026-07-28] Weights, tech report, and FlashKDA/MoonEP/AgentENV shipped under a "kimi-k3" license; independent evals confirm it beats Opus 4.8; separately, Kratsios accuses Moonshot of distilling Fable, Treasury signals possible sanctions
- [2026-07-17] Announced: 2.8T params, Kimi Delta Attention, Intelligence Index 57, #1 Frontend Code Arena; supersedes Kimi K2.7-Code as Moonshot's flagship

## Sources

- [AINews — Kimi K3 (2.8T, largest open model)](../sources/newsletters/ainews-kimi-k3-2026-07-17.md)
- [AINews — Much ado about Open Weights](../sources/newsletters/ainews-much-ado-about-open-weights-2026-07-28.md)
- [AINews — Laguna S 2.1 / Kratsios distillation accusation](../sources/newsletters/ainews-laguna-kratsios-2026-07-23.md)
