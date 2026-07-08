---
type: proposal
sources:
  - raw/articles/2026-07-06-anthropiccom-news-claude-science-ai-workbench.md
  - raw/articles/2026-07-01-anthropiccom-newsclaude-science-ai-workbenc.md
  - raw/newsletters/2026-07-01-anthropic-releases-sonnet-5.md
status: pending
created: 2026-07-06
---

# Proposal: Claude Science official workbench details

## Summary
Anthropic's official Claude Science announcement adds concrete detail about the workbench: local/HPC execution, scientific artifact rendering, reviewer agents, 60+ scientific databases, BioNeMo integrations, reusable skills, and beta case studies. This should enrich the already-created Claude Science, science state-of, and AI-in-science trend pages.

## Intended changes

- [x] **Update** `wiki/tools/claude-science.md` — add local/HPC execution, scientific artifacts, reviewer agents, and beta availability.
    > **Add to Current status:** Beta for Claude Pro, Max, Team, and Enterprise; runs locally on macOS/Linux or over SSH/HPC login nodes; supports auditable artifacts including 3D protein structures, genome browser tracks, chemical structures, figures, manuscripts, exact code, environment details, and message history.

- [x] **Update** `wiki/state-of/science.md` — strengthen Claude Science's science-agent-platform entry with official beta and compute posture.

- [x] **Update** `wiki/trends/ai-in-science.md` — add case-study signal from Manifold Bio, Allen Institute, and UCSF.

- [x] **Create** `wiki/sources/articles/claude-science-workbench-2026-07.md` — official source summary.

## Updated Page Snippets

### `wiki/tools/claude-science.md`

> **Before:**
> `- Available for macOS and Linux in public beta.`
> `- Supports persistent Python and R kernels and can manage environments on laptops, Linux machines, or HPC login nodes.`

> **After:**
> `- Available in beta for Claude Pro, Max, Team, and Enterprise, with local macOS/Linux execution or remote access through SSH/HPC login nodes.`
> `- Supports persistent Python and R kernels, scientific artifact rendering, exact code/environment capture, message history, and reviewer agents that check citations, calculations, and code/figure consistency.`

### `wiki/state-of/science.md`

> **Before:**
> `- [Claude Science](../tools/claude-science.md) — Anthropic public beta app for scientific analysis, database search, reproducible artifact history, persistent Python/R kernels, scientific connectors, and HPC/local compute integration; Anthropic is dogfooding science tooling through internal preclinical drug programs *(as of 2026-07-06)*`

> **After:**
> `- [Claude Science](../tools/claude-science.md) — Anthropic beta science workbench for analysis, database search, reproducible artifacts, reviewer agents, scientific visualizations, 60+ databases, BioNeMo/Boltz/OpenFold-style integrations, and local/HPC compute; case studies now include Manifold Bio, Allen Institute, and UCSF workflows *(as of 2026-07-01)*`

### `wiki/trends/ai-in-science.md`

> **Before:**
> `- Anthropic's Claude Science signal reinforces a platform-first strategy in science AI: build tools for analysis, visualization, traceability, and verification, then dogfood them on real preclinical programs.`

> **After:**
> `- Anthropic's Claude Science signal reinforces a platform-first strategy in science AI: build tools for analysis, visualization, traceability, reviewer-agent verification, scientific databases, and lab/HPC compute, then dogfood them on real preclinical and partner research workflows.`

## Page Drafts

### `wiki/sources/articles/claude-science-workbench-2026-07.md` (new)

```md
---
title: Claude Science AI workbench announcement
type: source
source_type: article
source_file: raw/articles/2026-07-06-anthropiccom-news-claude-science-ai-workbench.md
url: https://www.anthropic.com/news/claude-science-ai-workbench
published: 2026-07-01
ingested: 2026-07-06
domains: [science, agents]
---

# Claude Science AI workbench announcement

Anthropic announced Claude Science as a beta workbench for scientific research workflows. The product combines Claude with scientific packages, artifacts, local or HPC execution, reusable skills/connectors, reviewer agents, and integrations across scientific databases and models.

## Influenced pages
- [Claude Science](../../tools/claude-science.md) — official beta details, execution model, artifact support, reviewer agents
- [State of Science](../../state-of/science.md) — science-agent-platform update
- [AI in Science](../../trends/ai-in-science.md) — case-study evidence

## Key claims extracted
- Claude Science can run locally on macOS/Linux or remotely through SSH/HPC login nodes.
- The workbench renders and preserves auditable scientific artifacts, code, environment details, and message history.
- Anthropic describes 60+ scientific databases plus NVIDIA BioNeMo, Evo 2, Boltz-2, and OpenFold3 integrations.
- Case studies include Manifold Bio target nomination, Allen Institute review workflows, and UCSF glioma molecular epidemiology.
```
