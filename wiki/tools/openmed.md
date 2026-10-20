---
title: OpenMed
type: tool
domains: [healthcare]
subcategory: healthcare-ai
tags: [open-source]
as_of: 2026-10-19
sources: [maziyarpanahi-openmed]
---

# OpenMed

Open-source, local-first SDK for clinical text: named-entity recognition (diseases, drugs, anatomy, genes) and PII/PHI de-identification that run on hardware the user controls, so notes do not have to leave the building to be processed. Maintained by Maziyar Panahi; SDK under Apache-2.0, with model and dataset licenses varying per artifact.

## Current status (as of 2026-10-19)

- Curated catalog of 2,200+ medical models on Hugging Face, mostly specialized NER variants (e.g. disease, pharma, PII, anatomy, gene detection at 109M–434M parameters)
- De-identification by mask, replace (Faker-backed fake values), hash, or date shift; 42 supported PII language codes, 35 of them model-backed
- PII models include three families on the [OpenAI Privacy Filter](../models/openai-privacy-filter.md) architecture (original weights, Nemotron-PII-trained, MLX) behind the same `extract_pii()` / `deidentify()` API
- Runtimes: Python (CPU/CUDA), Apple MLX and a Swift package for iOS, Kotlin/ONNX Runtime Mobile for Android, browser via Transformers.js/WebGPU, and a Docker-ready REST service with auth, no-PHI logging, and batching
- Agent-facing surfaces: Agent Skills for Claude Code, Codex, and OpenCode, an MCP server, and an llms.txt docs index
- v3.0.0 release; 5,400+ GitHub stars as of 9 October 2026

## Why it matters

Most healthcare entries in the wiki are hosted products. OpenMed is the open, on-device counterpart for the step that usually blocks cloud AI in clinical settings: removing identifiers before any text reaches an external model. Its agent skills explicitly tell users to run the pipeline locally on real notes and not to paste PHI into a cloud-hosted agent.

## Weaknesses / caveats

- The README states that SDK use alone does not establish HIPAA compliance; Safe Harbor-aligned categories are implementation aids, and deployment owners must validate privacy behavior and clinical fitness
- Model and dataset terms vary across the catalog and must be checked per model
- The "clinical brief" demo runs on synthetic test doubles, not trained models, and is not clinical validation
- Network paths (model downloads, remote adapters, telemetry-enabled paths) sit outside the local-only boundary

## Recent changes

- [2026-10-19] Page created from the GitHub README (v3.0.0): clinical NER plus de-identification across Python, Apple, Android, browser, and REST runtimes.

## Sources

- [OpenMed GitHub repository](../sources/repos/maziyarpanahi-openmed.md)
