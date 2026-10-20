---
title: ScaleDown
type: model
domains: [models]
subcategory: utility-model
tags: [closed-source]
as_of: 2026-10-19
sources: [scaledown-homepage-2026-10, scaledown-site-crawl-2026-10]
---

# ScaleDown

A family of four narrow, single-task models sold through one API by ScaleDown, a self-described applied research lab: **Classify** (calibrated label probabilities against labels and rubrics you write), **Extract** (schema-defined entities with confidence scores and character offsets), **Summarize** (length- and format-controlled abstractive summaries) and **Compress** (query-aware shortening of prompt context). Compress, Extract and Classify are encoder-only, which is why output tokens are free; Summarize has a generative step.

## Current status (as of 2026-10-19)

- Pricing, flat with no tiers: $0.05 per 1M text input tokens for all four models; $0.15 per 1M image input tokens (Classify, Extract, Summarize; Compress takes no images); output free. New accounts get 1M free tokens; 20% off via OpenRouter.
- Context: 1M tokens per request for Classify, Extract and Summarize; Compress is "unlimited" per the FAQ.
- Batch API (`POST /v1/batches`): JSONL of extract, summarize or classify requests (mixable in one batch), polled by batch ID, results in OpenAI ChatCompletion shape. Compress is not batchable.
- Classify also exposes a Decisions API that mirrors TypeSafe's Jev request/response shape (choice, yes/no, score questions), so Jev integrations can switch by base URL.
- Deployment: managed API, OpenRouter, or enterprise dedicated instance / self-hosted containers (VPC or air-gapped, per-deployment license; an L40 node serves all four for moderate load, per a 2026-06-03 blog). Zero data retention and no training on customer data are claimed.

## Integration pattern

ScaleDown sits in front of, or instead of, a frontier call. Compress goes between retrieval and the model call (RAG chunks, long documents, chat history, agent tool traces); `rate: "auto"` typically keeps 30–50% of prose, i.e. 50–70% compression, and the docs advise against it for prompts under ~500 tokens, code or JSON. Classify is pitched as the router upstream of model selection, and Extract/Summarize as drop-in replacements for LLM extraction and summarization calls. DietCode (a Claude Code / Codex CLI / Cursor plugin) and ScaleDown Agent (an MCP server that finds LLM call sites to migrate) package the same pattern.

## Benchmarks (vendor-run)

All figures are from the site's text tables; the homepage charts did not survive capture, so no number here was read from a chart.

- Method: Classify on CLINC OOS (accuracy), Extract on CUAD (F1), Summarize on QMSum (ROUGE-L), Compress end-to-end on FinanceBench (F1).
- Average accuracy gain over each provider's lineup: OpenAI +8.72%, Anthropic +8.0%, Gemini +9.0%, Grok +7.93%, DeepSeek +19.5%, Qwen +16.71%; 2.2–13.9× faster and 9–161× cheaper on provider averages.
- Classify: 90.53% vs 87.07% for GPT-5.4 Mini, at $0.0008 vs $0.16 for the run (blog, 2026-05-13).
- Compress + o4-mini on FinanceBench: F1 0.255 vs 0.199 uncompressed, $7.20 vs $18.50 per 1K calls.
- Against GLiNER2.5 (local, free, faster): +15.5 pp on classify, +0.2 pp on extract.

## Strengths

- Prices narrow pipeline tasks at near-zero marginal cost with large context.
- Calibrated probabilities and confidence scores make thresholding and human-review routing straightforward.

## Weaknesses / caveats

- Every benchmark is vendor-run and some comparisons name superseded models (Fable 5, Opus 4.8); the public GLiNER comparison page returns 404.
- Speed and cost headlines conflict: homepage "467× cheaper, 200× faster" (no methodology), FAQ "20× faster", docs tables 2.2–13.9×.
- Free-tier wording conflicts: pricing table says 1M free tokens; 2026 blog posts say 50M per agent.
- The FinanceBench compression study names o3, o4-mini and Claude 3.7 Sonnet, so it likely predates the current lineup.
- Proprietary weights; self-hosting is licensed, not open.

## Recent changes

- [2026-10-19] Page created from a crawl of scaledown.ai.

## Sources

- [ScaleDown AI — Task-specific SLMs (homepage)](../sources/articles/scaledown-homepage-2026-10.md)
- [ScaleDown website crawl (October 2026)](../sources/articles/scaledown-site-crawl-2026-10.md)
