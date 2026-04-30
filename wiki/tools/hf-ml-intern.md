---
title: HF ml-intern
type: tool
domains: [agents]
subcategory: autonomous-research-agent
tags: [open-source, agentic, huggingface]
as_of: 2026-04-22
sources: [ainews-2026-04-22]
---

# HF ml-intern

Hugging Face's open-source agent for autonomous ML post-training research. Closes the full loop: reads papers and follows citations, collects and reformats datasets, launches training jobs on the Hub, evaluates runs, and iterates on failures — with minimal human intervention between steps.

## Current status (as of 2026-04-22)

- Runs end-to-end post-training research loop autonomously
- GPQA scientific reasoning: 10% → 32% on Qwen3-1.7B in under 10 hours
- Healthcare variant beat Codex on HealthBench by 60%
- Math variant: wrote a full GRPO training script and recovered from reward collapse via ablations
- Community-verified: can autonomously fine-tune models and publish artifacts back to HuggingFace Hub
- Available and runnable on the HuggingFace Hub

## Why it matters

End-to-end autonomous research loops — not just coding demos — are the new frontier signal. The agent doesn't just write code; it reads literature, runs the science, evaluates the outputs, and publishes results back. Distinct from single-task code agents.

## Weaknesses / caveats

- Reported results come from community verification rather than a peer-reviewed benchmark — directionally credible but not formally audited
- Focused on ML post-training tasks specifically; scope beyond that is untested in captured sources

## Recent changes

- [2026-04-22] Initial page — HF ml-intern announced and community-verified

## Sources

- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
