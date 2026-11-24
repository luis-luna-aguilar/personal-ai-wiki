---
title: Reflection Beam
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [open-weights, text]
as_of: 2026-10-17
sources: [ainews-reflection-beam-2026-10-06, ainews-reflection-beam-training-2026-10-07, ainews-us-open-weights-push-2026-10-17]
---

# Reflection Beam

Reflection's first model, after more than a year in stealth: a text-only 501B-total / 23B-active mixture-of-experts model for coding, agentic and scientific work, trained from scratch in the US. Beam 1.0 shipped around 2026-10-16 under Apache 2.0.

## Current status (as of 2026-10-17)

- 1M context; BF16, FP8 and NVFP4 weights, a DFlash2 speculative-decoding drafter, the open Mirror CLI harness Beam was trained in, and a safety report
- Artificial Analysis Intelligence Index 30, #2 among US open models (behind [Muse Spark Open](muse-spark.md)); ~26K tokens per task; 48.5% AutomationBench-AA but 3.0% Terminal-Bench 4.0; AA-Omniscience 33% correct, 47% hallucination
- Arena: #12 open model in Agent Arena; the only non-Chinese model in the top 25 open models on Code WebDev
- Reflection's claim: 80.9 on SWE-bench Verified and 3–4x GLM-5.2's inference efficiency; observers place it around GLM-5.2 and below [DeepSeek V4.1 Flash](deepseek-v4-1-flash.md)
- Training: 23.8T pretraining tokens (partly OCR'd PDFs); four weeks each of pretraining and RL on ~10,500 GB300s, with over 100M rollouts across ~1M tasks; day-0 vLLM, SkyRL and Ollama support

## Why it matters

A credible US-trained, permissively licensed open model from a new lab, arriving the same week as Meta's Muse Spark Open. It still trails the Chinese open leaders (GLM-5.3, Kimi K3, DeepSeek V4.1 Flash). See [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md).

## Weaknesses / caveats

- Very weak on Terminal-Bench 4.0 and high hallucination rate
- Low estimated pretraining efficiency (~12% BF16 MFU); one commentator calls it an iso-FLOP replication of DeepSeek V3

## Recent changes

- [2026-10-16] Beam 1.0 weights shipped under Apache 2.0 with the Mirror harness and a safety report; AA Intelligence Index 30.
- [2026-10-05] Announced: 501B/23B text MoE trained from scratch in the US; weights due in October.

## Sources

- [AINews — Reflection Beam announcement](../sources/newsletters/ainews-reflection-beam-2026-10-06.md)
- [AINews — Beam training details and Mistral Large 4](../sources/newsletters/ainews-reflection-beam-training-2026-10-07.md)
- [AINews — US open-weights push: Spark Open and Beam 1.0](../sources/newsletters/ainews-us-open-weights-push-2026-10-17.md)
