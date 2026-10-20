---
title: OpenAI Privacy Filter
type: model
domains: [models, cybersecurity]
subcategory: utility-model
tags: [openai, open-weights]
as_of: 2026-10-19
sources: [ainews-2026-04-23, the-code-2026-04-23, maziyarpanahi-openmed]
---

# OpenAI Privacy Filter

OpenAI's open-weight PII detection and redaction model. A 1.5B-total / 50M-active MoE token-classification model released under Apache 2.0. Intended to run on-device or on low-cost infrastructure to redact sensitive data before it reaches cloud AI systems — a targeted solution to a concrete enterprise and agent-pipeline compliance problem.

## Current status (as of 2026-10-19)

- 1.5B total parameters / 50M active (MoE token-classification architecture)
- Detects and masks: emails, API keys, names, and other PII categories
- 128k context window — practical for large log files and document corpora
- Apache 2.0 license; available on Hugging Face
- Designed for cheap, on-device preprocessing before data hits any cloud model
- Packaged downstream by [OpenMed](../tools/openmed.md) as three model families on the same architecture (original weights, a Nemotron-PII-trained variant, an MLX build), all called through one `extract_pii()` / `deidentify()` API for clinical de-identification *(as of 2026-10-19)*

## Why it matters

Most enterprise AI pipelines face a real blocking question: "can we send this data to the cloud?" Privacy Filter offers a lightweight, deployable answer: redact PII locally first, then proceed. This is more operationally useful than a generic small open model — it solves one specific infrastructure problem.

## Weaknesses / caveats

- Quiet release with minimal official documentation at time of ingest
- MoE token-classification (not a generative model) — different usage pattern than general LLMs

## Recent changes

- [2026-10-19] OpenMed ships Privacy Filter-architecture variants (Nemotron-PII-trained and MLX) for on-device clinical de-identification.
- [2026-04-23] Released by OpenAI; Apache 2.0; available on Hugging Face

## Sources

- [AINews — Tasteful Tokenmaxxing](../sources/newsletters/ainews-2026-04-23.md)
- [The Code — OpenAI drops a privacy focused model](../sources/newsletters/the-code-2026-04-23.md)
- [OpenMed GitHub repository](../sources/repos/maziyarpanahi-openmed.md)
