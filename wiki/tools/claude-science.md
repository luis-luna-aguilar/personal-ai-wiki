---
title: Claude Science
type: tool
domains: [science, agents]
subcategory: science-agent-platform
tags: [anthropic, agentic]
as_of: 2026-07-06
sources: [claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05]
---

# Claude Science

Claude Science is Anthropic's public beta app for scientific workflows. It is not a new model; it wraps existing Claude models with scientific tools, database connections, compute integrations, and reproducible artifact history.

## Current status (as of 2026-07-06)

- Available for macOS and Linux in public beta.
- Runs analyses, searches scientific databases, and traces steps from data wrangling to publication.
- Figures, tables, and notebooks preserve the code, environment, and conversation that produced them.
- Supports persistent Python and R kernels and can manage environments on laptops, Linux machines, or HPC login nodes.
- Preconfigured for genomics, single-cell, proteomics, structural biology, cheminformatics, and related domains; Anthropic says it can query 60+ scientific databases.
- Every reports that Anthropic is also running internal preclinical drug programs to dogfood and improve its science tooling.

## Strengths

- Strong fit for workflows where verification, provenance, and reproducibility matter.
- Connectors can bring internal APIs, ELNs, bespoke pipelines, protein/structure models, HPC, and MCP-accessible tools into one workflow.
- Anthropic's internal drug programs may create a real feedback loop for evaluating the platform on hard biological problems.

## Weaknesses / caveats

- Public beta; product surface and availability may change.
- Drug discovery feedback loops are slow, so success cannot be inferred from launch alone.

## Recent changes

- [2026-07-06] Anthropic product page confirms Claude Science public beta, reproducible artifacts, persistent kernels, 60+ scientific databases, and scientific-tool/compute integrations.
- [2026-07-05] Every reports Claude Science launch and Anthropic internal preclinical drug-program dogfooding.

## Sources

- [Claude Science beta](../sources/articles/claude-science-beta-2026-07-06.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
