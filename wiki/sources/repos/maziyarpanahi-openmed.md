---
title: 'OpenMed GitHub repository (maziyarpanahi/openmed)'
type: source
source_type: repo
source_file: raw/repos/maziyarpanahi-openmed.md
url: https://github.com/maziyarpanahi/openmed
ingested: 2026-10-19
domains: [healthcare]
---

# OpenMed GitHub repository

README of Maziyar Panahi's OpenMed, an Apache-2.0 local-first SDK for clinical named-entity recognition and HIPAA-oriented PII de-identification, with Python, MLX/Swift, Android, browser, and REST runtimes. No release or commit date in the capture; the README cites a 9 October 2026 star snapshot; captured 2026-10-19.

## Influenced pages

- [OpenMed](../../tools/openmed.md) — new tool page
- [State of Healthcare](../../state-of/healthcare.md) — new Healthcare AI leader line
- [OpenAI Privacy Filter](../../models/openai-privacy-filter.md) — downstream packaging as three model families

## Key claims extracted

- 2,200+ medical models in a curated catalog; example NER models at 109M–434M parameters (disease, pharma, PII, anatomy, gene)
- De-identification methods: mask, replace (Faker), hash, shift_dates; smart entity merging; HIPAA/GDPR/research policy profiles, signed audit reports
- Safe Harbor-aligned configuration can target the 18 identifier categories; SDK use alone does not establish HIPAA compliance
- 42 supported PII language codes, 35 model-backed; Russian routes to a multilingual placeholder
- Privacy Filter family: `openai/privacy-filter`, `OpenMed/privacy-filter-nemotron` (NVIDIA Nemotron-PII data), `OpenMed/privacy-filter-mlx`; same API, only `model_name` changes
- MLX on Apple silicon: 24–33x faster than CPU PyTorch for the Privacy Filter (median latency per step); batch PII up to 3.3x throughput on CPU, 2.2x on MLX
- Runtimes: Python CPU/CUDA, MLX, Swift OpenMedKit (iOS), Kotlin + ONNX Runtime Mobile (Android), Transformers.js/WebGPU, FastAPI REST service with API-key/JWT auth, no-PHI logging, gRPC, async jobs, dynamic batching
- Agent Skills for Claude Code, Codex, OpenCode; MCP server; llms.txt index
- Clinical brief demo uses synthetic NER/NLI test doubles, not trained-model or clinical validation
- v3.0.0 release; 5,400+ stars (9 Oct 2026 snapshot); companion paper arXiv 2508.01630 (OpenMed NER, 2025)
