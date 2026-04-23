---
type: proposal
sources:
  - raw/newsletters/2026-04-23-openai-drops-a-privacy-focused-model.md
  - raw/newsletters/2026-04-23-anthropics-unreleased-model-got-hacked.md
  - raw/newsletters/2026-04-23-ainews-tasteful-tokenmaxxing.md
status: pending
created: 2026-04-23
---

# Proposal: OpenAI Privacy Filter

## Summary
OpenAI quietly released Privacy Filter: a 1.5B-total / 50M-active MoE token-classification model under Apache 2.0. It detects and masks PII (emails, API keys, personal data) locally on-device before data reaches the cloud, with a 128k context window for large-corpus redaction. Available on Hugging Face.

## Intended changes

- [x] **Create** `wiki/models/openai-privacy-filter.md` — new model page
- [x] **Update** `wiki/state-of/models.md` — add Privacy Filter under a new "Specialized utility models" subcategory; prepend Recent changes entry
- [x] **Schema** — propose new subcategory `utility-model` (see Schema section below)

*Note: Source pages `ainews-2026-04-23.md` and `the-code-2026-04-23.md` are created in proposal `2026-04-23-qwen-3-6-27b.md`. `superhuman-2026-04-23.md` is created in `2026-04-23-openai-workspace-agents.md`.*

## Page drafts

### wiki/models/openai-privacy-filter.md (new)

````md
---
title: OpenAI Privacy Filter
type: model
domains: [models, cybersecurity]
subcategory: utility-model
tags: [openai, open-weights]
as_of: 2026-04-23
sources: [ainews-2026-04-23, the-code-2026-04-23, superhuman-2026-04-23]
---

# OpenAI Privacy Filter

OpenAI's open-weight PII detection and redaction model. A 1.5B-total / 50M-active MoE token-classification model released under Apache 2.0. Intended to run on-device or on low-cost infrastructure to redact sensitive data before it reaches cloud AI systems — a targeted solution to a concrete enterprise and agent-pipeline compliance problem.

## Current status (as of 2026-04-23)

- 1.5B total parameters / 50M active (MoE token-classification architecture)
- Detects and masks: emails, API keys, names, and other PII categories
- 128k context window — practical for large log files and document corpora
- Apache 2.0 license; available on Hugging Face
- Designed for cheap, on-device preprocessing before data hits any cloud model

## Why it matters

Most enterprise AI pipelines face a real blocking question: "can we send this data to the cloud?" Privacy Filter offers a lightweight, deployable answer: redact PII locally first, then proceed. This is more operationally useful than a generic small open model — it solves one specific infrastructure problem.

## Weaknesses / caveats

- Quiet release with minimal official documentation at time of ingest
- MoE token-classification (not a generative model) — different usage pattern than general LLMs

## Recent changes

- [2026-04-23] Released by OpenAI; Apache 2.0; available on Hugging Face

## Sources

- [[sources/newsletters/ainews-2026-04-23]]
- [[sources/newsletters/the-code-2026-04-23]]
- [[sources/newsletters/superhuman-2026-04-23]]
````

### wiki/state-of/models.md (update — diff only)

> **Add new subcategory section after `Image generation` section:**
> ```markdown
> ### Specialized utility models
>
> Narrow-purpose models built for a specific infrastructure or pipeline task, rather than general-purpose generation or reasoning.
>
> - [[models/openai-privacy-filter]] — OpenAI; 1.5B-total / 50M-active MoE for on-device PII detection and masking; 128k context; Apache 2.0; designed for cheap on-device preprocessing before cloud API calls *(as of 2026-04-23)*
> ```

> **Add to `## Recent changes` (prepend):**
> `- [2026-04-23] Added 'Specialized utility models' subcategory; [[models/openai-privacy-filter]] is the first entry — on-device PII redaction, 1.5B MoE, Apache 2.0`

## Schema / vocabulary additions

- [x] **Add new subcategory `utility-model`** to `wiki/_schema/subcategories.md`:

```
### utility-model
- **Parent domain(s):** models
- **Applies to types:** model
- **Definition:** Small, narrow-purpose models built to solve a specific infrastructure or pipeline task (e.g. PII redaction, classification, embedding) rather than general-purpose generation or reasoning.
- **Examples:** [[models/openai-privacy-filter]]
```
