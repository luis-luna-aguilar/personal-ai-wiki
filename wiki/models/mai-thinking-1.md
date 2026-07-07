---
title: MAI-Thinking-1
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [microsoft, closed-source]
as_of: 2026-06-03
sources: [ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026]
---

# MAI-Thinking-1

Microsoft's first frontier-class reasoning model, launched at Build 2026. The headline claim: trained from scratch with no synthetic data and no distillation, producing blind human preference over Claude Sonnet 4.6 and 97% AIME 2025. Signals a strategic shift — Microsoft as a model lab, not only a distributor of OpenAI models.

## Current status (as of 2026-06-03)

- **Architecture:** 35B active / 1T total MoE (Mixture of Experts); 256K context window
- **Pretraining:** 30T tokens; 8,192 NVIDIA GB200 GPUs; no synthetic data, no distillation from other models
- **Technical transparency:** 109-page technical report
- **Benchmarks:** 97% AIME 2025; 53% SWE-Bench Pro; blind human preference over Claude Sonnet 4.6 in side-by-side eval
- **Frontier Tuning:** RL environments for workflow-specific fine-tuning; internal Excel-tuned model reportedly reaches GPT-5.4-level at 10x efficiency
- **MAIA 200 silicon:** companion inference chip with 30% better performance/dollar vs NVIDIA GB200

## Strengths

- First credible evidence Microsoft can train frontier-class models independently of OpenAI
- "No synthetic data, no distillation" claim addresses enterprise IP concerns
- 109-page tech report level of transparency is above industry baseline
- MAIA 200 chip gives Microsoft deployment independence

## Weaknesses / caveats

- Claims are primarily from Microsoft's own sources; no independent third-party benchmark replication at time of writing
- Blind human preference over Sonnet 4.6 is a relatively low bar given Sonnet 4.6 is not the current Anthropic frontier
- SWE-Bench Pro 53% is competitive but below Claude Opus 4.8 and GPT-5.5 at their strongest

## MAI family members

| Model | Size | Benchmark | Use case |
|---|---|---|---|
| MAI-Thinking-1 | 35B active / 1T MoE | 97% AIME 2025, 53% SWE-Pro | Reasoning, flagship |
| MAI-Code-1-Flash | 5B active / 137B MoE | 51% SWE-Pro | GitHub Copilot, VS Code |
| MAI-Image-2.5 | — | #2 Image Edit Arena (1401) | Image editing |
| MAI-Transcribe-1.5 | — | 276x realtime, 2.4% AA-WER, 43 langs | Transcription |
| MAI-Voice-2 | — | — | Voice synthesis |

## Recent changes

- [2026-06-03] Launched at Microsoft Build 2026; initial benchmarks and tech report

## Sources

- [AINews — Microsoft Build, MAI-Thinking-1 (June 3)](../sources/newsletters/ainews-mai-build-june-2026.md)
- [Satya Nadella — No Priors x Latent Space (June 3)](../sources/newsletters/satya-nadella-no-priors-june-2026.md)
