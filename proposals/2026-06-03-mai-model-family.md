---
type: proposal
sources:
  - raw/newsletters/2026-06-03-ainews-microsoft-build-mai-thinking-1-and-mai-f.md
  - raw/newsletters/2026-06-03-satya-nadella-no-priors-x-latent-space-crossove.md
status: pending
created: 2026-06-24
---

# Proposal: Microsoft MAI model family — Microsoft Build 2026

## Summary

Microsoft launched 7 new MAI (Microsoft AI) models at Build 2026, all trained from scratch with no distillation or synthetic data. MAI-Thinking-1 (35B active / 1T total MoE) shows blind human preference over Claude Sonnet 4.6 and 53% SWE-Bench Pro — the first evidence Microsoft can train frontier-class models independently. MAI-Code-1-Flash (5B active / 137B MoE) ships inside GitHub Copilot and VS Code.

## Intended changes

- [x] **Create** `wiki/models/mai-thinking-1.md` — new model page for the flagship
    > See draft below

- [x] **Update** `wiki/state-of/models.md` — add MAI-Thinking-1 to frontier multimodal section, MAI-Code-1-Flash to coding models; add Recent changes entry
    > **Add to frontier multimodal section:**
    > `- [MAI-Thinking-1](../models/mai-thinking-1.md) — Microsoft; 35B active / 1T total MoE; 256K context; 97% AIME 2025, 53% SWE-Bench Pro; blind human preference over Claude Sonnet 4.6; trained from scratch (no synthetic data, no distillation); 109-page tech report; Frontier Tuning for workflow-specific RL adaptation *(as of 2026-06-03)*`
    >
    > **Add to coding models section:**
    > `- **MAI-Code-1-Flash** — Microsoft; 5B active / 137B MoE; 51% SWE-Bench Pro; powers GitHub Copilot and VS Code; designed for high-throughput coding inference *(as of 2026-06-03)*`
    >
    > **Add to Recent changes:**
    > `- [2026-06-03] Microsoft Build: MAI model family launched (7 models, all from scratch): MAI-Thinking-1 (35B/1T MoE, 97% AIME 2025, 53% SWE-Pro, beats Sonnet 4.6 in blind human eval), MAI-Code-1-Flash (5B/137B, 51% SWE-Pro, in GitHub Copilot/VS Code), MAI-Image-2.5 (#2 Image Edit Arena), MAI-Transcribe-1.5 (276× realtime, 43 languages)`

- [x] **Update** `wiki/tools/microsoft-copilot.md` — add MAI-Code-1-Flash and Microsoft Autopilot agent context from Build
    > **Add to Current status section:**
    > `- **MAI-Code-1-Flash** powers GitHub Copilot and VS Code at Build launch — Microsoft's first-party 5B active / 137B MoE coding model replaces external model dependency for Copilot's core coding feature (as of 2026-06-03)`
    > `- **Microsoft Autopilot**: hosted long-running agent runtime launched at Build; OpenClaw and Hermes Agent as early examples; Scout is the first consumer-facing always-on agent; long-running agent substrate positioning`
    >
    > **Update Recent changes (add at top):**
    > `- [2026-06-03] Build 2026: MAI-Code-1-Flash in Copilot/VS Code; Microsoft Autopilot hosted agent runtime; Scout (always-on personal agent across M365)`
    >
    > **Update sources frontmatter:** add `ainews-mai-build-june-2026`

- [x] **Create** `wiki/sources/newsletters/ainews-mai-build-june-2026.md` — source summary for the Build 2026 MAI AINews newsletter
    > See draft below

- [x] **Create** `wiki/sources/newsletters/satya-nadella-no-priors-june-2026.md` — source summary for Satya Nadella No Priors × Latent Space podcast
    > See draft below

## Page drafts

### wiki/models/mai-thinking-1.md (new)

````md
---
title: MAI-Thinking-1
type: model
domains: [models, coding]
subcategory: frontier-multimodal-model
tags: [microsoft, closed-source]
as_of: 2026-06-03
sources: [ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026]
---

# MAI-Thinking-1

Microsoft's first frontier-class reasoning model, launched at Build 2026. The headline claim: trained from scratch with no synthetic data and no distillation, producing blind human preference over Claude Sonnet 4.6 and 97% AIME 2025. Signals a strategic shift — Microsoft as a model lab, not only a distributor of OpenAI models.

## Current status (as of 2026-06-03)

- **Architecture:** 35B active / 1T total MoE (Mixture of Experts); 256K context window
- **Pretraining:** 30T tokens; 8,192 NVIDIA GB200 GPUs; no synthetic data, no distillation from other models
- **Technical transparency:** 109-page technical report (praised by researchers as unusually detailed)
- **Benchmarks:**
  - 97% AIME 2025 (math olympiad reasoning)
  - 53% SWE-Bench Pro (coding/software engineering)
  - Blind human preference: beats Claude Sonnet 4.6 in side-by-side eval
- **Frontier Tuning:** RL environments for workflow-specific fine-tuning; internal Excel-tuned model reportedly reaches GPT-5.4-level at 10× efficiency
- **MAIA 200 silicon:** companion inference chip with 30% better performance/dollar vs. NVIDIA GB200; provides deployment independence

## Strengths

- First credible evidence Microsoft can train frontier-class models independently of OpenAI
- "No synthetic data, no distillation" claim addresses enterprise IP concerns
- 109-page tech report level of transparency is above industry baseline
- MAIA 200 chip gives Microsoft deployment independence

## Weaknesses / caveats

- Claims are primarily from Microsoft's own sources (Build keynote + AINews relay); no independent third-party benchmark replication at time of writing
- Blind human preference over Sonnet 4.6 is a relatively low bar given Sonnet 4.6 is not the current Anthropic frontier
- SWE-Bench Pro 53% is competitive but below Claude Opus 4.8 and GPT-5.5 at their strongest

## MAI family members

| Model | Size | Benchmark | Use case |
|---|---|---|---|
| MAI-Thinking-1 | 35B active / 1T MoE | 97% AIME 2025, 53% SWE-Pro | Reasoning, flagship |
| MAI-Code-1-Flash | 5B active / 137B MoE | 51% SWE-Pro | GitHub Copilot, VS Code |
| MAI-Image-2.5 | — | #2 Image Edit Arena (1401) | Image editing |
| MAI-Transcribe-1.5 | — | 276× realtime, 2.4% AA-WER, 43 langs | Transcription |
| MAI-Voice-2 | — | — | Voice synthesis |

## Recent changes

- [2026-06-03] Launched at Microsoft Build 2026; initial benchmarks and tech report

## Sources

- [AINews — Microsoft Build, MAI-Thinking-1 (June 3)](../../sources/newsletters/ainews-mai-build-june-2026.md)
- [Satya Nadella — No Priors × Latent Space (June 3)](../../sources/newsletters/satya-nadella-no-priors-june-2026.md)
````

### wiki/sources/newsletters/ainews-mai-build-june-2026.md (new)

````md
---
title: AINews — Microsoft Build 2026, MAI-Thinking-1 and MAI family (June 3)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-03-ainews-microsoft-build-mai-thinking-1-and-mai-f.md
published: 2026-06-03
ingested: 2026-06-24
domains: [models, coding]
---

# AINews — Microsoft Build 2026, MAI-Thinking-1 and MAI family (June 3)

AINews deep-dive on Microsoft Build 2026. Covers the full MAI model family, MAIA 200 silicon, Microsoft Autopilot (hosted long-running agents), Scout (always-on M365 personal agent), and MDash (multi-agent code review that caught bugs Anthropic Mythos missed).

## Influenced pages

- [MAI-Thinking-1](../../models/mai-thinking-1.md) — new page
- [Microsoft Copilot](../../tools/microsoft-copilot.md) — MAI-Code-1-Flash, Autopilot, Scout
- [State of Models](../../state-of/models.md) — MAI entries added

## Key claims extracted

- MAI-Thinking-1: 35B active / 1T MoE; 30T tokens, 8,192 GB200; 256K context; 97% AIME 2025; 53% SWE-Bench Pro; blind human preference vs Sonnet 4.6; no synthetic data/distillation; 109-page tech report; Frontier Tuning
- MAI-Code-1-Flash: 5B active / 137B MoE; 51% SWE-Bench Pro; powers GitHub Copilot/VS Code
- MAI-Image-2.5: #2 Image Edit Arena (score 1401)
- MAI-Transcribe-1.5: 276× realtime, 2.4% AA-WER, 43 languages, $6/1000min
- MAIA 200: Microsoft's inference silicon; 30% better perf/dollar vs GB200
- Microsoft Autopilot: hosted long-running agent runtime (OpenClaw and Hermes as early examples)
- MDash: multi-agent code review system that caught bugs Anthropic Mythos missed
- Microsoft Scout: always-on personal agent integrated across M365 apps
````

### wiki/sources/newsletters/satya-nadella-no-priors-june-2026.md (new)

````md
---
title: '"Satya Nadella on No Priors × Latent Space" — June 3'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-03-satya-nadella-no-priors-x-latent-space-crossove.md
published: 2026-06-03
ingested: 2026-06-24
domains: [models, coding]
---

# "Satya Nadella on No Priors × Latent Space" — June 3

Transcript of Satya Nadella (Microsoft CEO) crossover interview at Build 2026. Covers Microsoft AI strategy, the MAI model family, consumption pricing philosophy, and the MXC (Microsoft eXecution Containers) for OS-level agent sandboxing.

## Influenced pages

- [Microsoft Copilot](../../tools/microsoft-copilot.md) — strategy and pricing context
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — consumption pricing framing

## Key claims extracted

- Private evals are "the biggest IP" — Satya frames proprietary eval infrastructure as more durable moat than model weights
- Consumption/per-token pricing is the inevitable dominant enterprise model ("per-seat was a mistake in retrospect")
- GitHub Copilot evolving: Sessions app; engineers become "full-stack builders" not specialists
- RTX Spark laptop: runs 128B-parameter model locally; MXC for OS-level agent sandboxing on Windows
- MXC (Microsoft eXecution Containers): gives agents isolated OS sandbox without full VM; lighter than VM, safer than bare OS
- Microsoft Autopilot: Scout as first consumer agent; long-horizon hosted agent substrate
````
