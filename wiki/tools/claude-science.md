---
title: Claude Science
type: tool
domains: [science, agents]
subcategory: science-agent-platform
tags: [anthropic, agentic]
as_of: 2026-07-06
sources: [claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07]
---

# Claude Science

Claude Science is Anthropic's public beta app for scientific workflows. It is not a new model; it wraps existing Claude models with scientific tools, database connections, compute integrations, and reproducible artifact history.

## Current status (as of 2026-07-06)

- Available in beta for Claude Pro, Max, Team, and Enterprise, with local macOS/Linux execution or remote access through SSH/HPC login nodes.
- Runs analyses, searches scientific databases, and traces steps from data wrangling to publication.
- Figures, tables, and notebooks preserve the code, environment, and conversation that produced them.
- Supports persistent Python and R kernels, scientific artifact rendering, exact code/environment capture, message history, and reviewer agents that check citations, calculations, and code/figure consistency.
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
- [2026-07-01] Official announcement adds beta plan availability, reviewer agents, scientific artifact rendering, BioNeMo/Boltz/OpenFold integrations, and case studies.
- [2026-07-05] Every reports Claude Science launch and Anthropic internal preclinical drug-program dogfooding.

## Sources

- [Claude Science beta](../sources/articles/claude-science-beta-2026-07-06.md)
- [Claude Science AI workbench announcement](../sources/articles/claude-science-workbench-2026-07.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
