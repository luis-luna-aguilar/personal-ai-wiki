---
type: proposal
source: raw/newsletters/2026-04-22-ainews-openai-launches-gpt-image-2.md
status: pending
created: 2026-04-22
---

# Proposal: HF ml-intern — autonomous post-training research agent

## Summary

Hugging Face shipped ml-intern, an open-source agent that runs the complete post-training research loop end-to-end with minimal human intervention: reads papers, follows citations, collects datasets, launches training jobs, evaluates, and iterates on failures. Reported results: GPQA 10% → 32% on Qwen3-1.7B in under 10 hours; healthcare variant beats Codex on HealthBench by 60%. Represents the first publicly verified end-to-end autonomous ML research loop, distinct from coding demos.

## Intended changes

- [x] **Update** `wiki/state-of/agents.md` — add `Autonomous research agents` subcategory with ml-intern as the opening entry
    > **Add new subcategory section before `## Recent changes`:**
    > ```
    > ### Autonomous research agents
    >
    > Agents that close the full research loop end-to-end — reading literature, collecting data, running experiments, evaluating results, and iterating — with minimal human steering between steps.
    >
    > - [[tools/hf-ml-intern]] — Hugging Face; open-source ML post-training research loop agent; reads papers, collects datasets, launches training jobs, evaluates, and iterates; GPQA 10% → 32% in <10 hours on Qwen3-1.7B *(as of 2026-04-22)*
    > ```
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added `Autonomous research agents` subcategory; [[tools/hf-ml-intern]] is the first publicly verified agent to close the full ML post-training loop end-to-end
    > ```

- [x] **Create** `wiki/tools/hf-ml-intern.md` — new tool page
    > See draft below

## Schema / vocabulary additions

- [x] Add new subcategory `autonomous-research-agent` to `wiki/_schema/subcategories.md`
    > ```
    > ### autonomous-research-agent
    > - **Parent domain(s):** agents
    > - **Applies to types:** tool
    > - **Definition:** Agents that run a closed loop over a research or experimentation process — reading sources, designing experiments, executing jobs, evaluating results, and iterating — with minimal human steering.
    > - **Examples:** [[tools/hf-ml-intern]]
    > ```

## Page drafts

### wiki/tools/hf-ml-intern.md (new)

````md
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

- [[sources/newsletters/ainews-2026-04-22]]
````
