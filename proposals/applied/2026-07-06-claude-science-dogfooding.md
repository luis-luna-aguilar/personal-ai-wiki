---
type: proposal
sources:
  - raw/newsletters/2026-07-05-a-tale-of-two-models.md
status: pending
created: 2026-07-06
---

# Proposal: Claude Science and Anthropic drug-program dogfooding

## Summary

Every reports that Anthropic launched Claude Science as a desktop research tool for analysis, molecular/genomic visualization, and transparent code/step traces, while also running internal preclinical drug programs to dogfood the platform. The wiki should add Claude Science as a science-agent platform and update the science state page.

## Intended changes

- [x] **Create** `wiki/tools/claude-science.md` - Anthropic science workflow platform.
- [x] **Update** `wiki/state-of/science.md` - add Claude Science under science agent platforms.
- [x] **Update** `wiki/trends/ai-in-science.md` - add dogfooding/evaluation loop in drug discovery.
- [x] **Update** `wiki/index.md` - add `tools/claude-science.md`.

## Page drafts

### wiki/tools/claude-science.md (new)

```md
---
title: Claude Science
type: tool
domains: [science, agents]
subcategory: science-agent-platform
tags: [anthropic, agentic]
as_of: 2026-07-05
sources: [every-tale-of-two-models-2026-07-05]
---

# Claude Science

Claude Science is Anthropic's desktop research tool for scientific workflows. Every describes it as a tool for running analyses, visualizing molecular and genomic data, and showing the exact code and steps behind results.

## Current status (as of 2026-07-05)
- Built for scientific research workflows, especially analysis and visualization.
- Emphasizes traceability: scientists can see the code and steps behind results.
- Anthropic is also running internal preclinical drug programs, apparently to dogfood and improve its science tooling rather than to become a full-stack drug company.

## Strengths
- Strong fit for workflows where verification and reproducibility matter.
- Anthropic's internal drug programs may create a real feedback loop for evaluating the platform on hard biological problems.

## Weaknesses / caveats
- Current evidence is Every newsletter coverage; fetch Anthropic's primary product page before applying deep product claims.
- Drug discovery feedback loops are slow, so success cannot be inferred from launch alone.

## Recent changes
- [2026-07-05] Every reports Claude Science launch and Anthropic internal preclinical drug-program dogfooding.

## Sources
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
```

### wiki/state-of/science.md (snippet)

```md
### Science agent platforms
- [Claude Science](../tools/claude-science.md) - Anthropic desktop research tool for analysis, molecular/genomic visualization, and traceable code/step outputs; Anthropic is dogfooding it through internal preclinical drug programs *(as of 2026-07-05)*

## Recent changes
- [2026-07-05] Claude Science entered the science-agent-platform set; Anthropic's internal drug programs make evaluation/verification feedback loops the strategic point to watch.
```

### wiki/trends/ai-in-science.md (snippet)

```md
## Current status (as of 2026-07-05)
- Anthropic's Claude Science signal reinforces a platform-first strategy in science AI: build tools for analysis, visualization, traceability, and verification, then dogfood them on real preclinical programs.
- The hard part is not only hypothesis generation. Biological feedback is slow and expensive, so evaluation and verification workflows become the bottleneck the platform must solve.

## Recent changes
- [2026-07-05] Claude Science and Anthropic's internal drug programs reframed science agents as dogfooded workflow platforms, not only model demos.
```

## Open questions

- Fetch and ingest Anthropic's Claude Science primary product page before applying, or apply this as a lightweight source-backed note from Every first?
	- Fetch and ingest please.
