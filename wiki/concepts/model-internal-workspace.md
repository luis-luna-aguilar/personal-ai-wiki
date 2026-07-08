---
title: Model internal workspace
type: concept
domains: [models]
tags: []
as_of: 2026-07-07
sources: [anthropic-jspace-global-workspace-2026-07]
---

# Model internal workspace

A model internal workspace is a privileged internal representation that appears to support flexible reasoning, reportable concepts, and modulation of later behavior. Anthropic's July 2026 global-workspace research calls Claude's version `J-space`.

## Current status

- Anthropic reports that Claude has a global-workspace-like internal structure centered on a small subset of activations called J-space.
- The claim is not ordinary chain-of-thought extraction; it is about a representational substrate that may be available for report, modulation, and flexible reasoning.
- Interpretability researchers treated the result as evidence for working-memory-like model structure, while disagreeing about the framing.
- The practical safety angle is auditability: if hidden concepts, prompt injections, or sabotage-related features can be surfaced before they are verbalized, J-space-like tools may become a model-monitoring surface.

## Caveats

- This should not be read as proof of model consciousness. The safer interpretation is mechanistic: a possible internal workspace that helps explain and audit behavior.
- The strongest current source is newsletter synthesis of Anthropic's research and reactions; the primary paper/page should be fetched before adding deeper technical claims.

## Sources

- [Anthropic J-space / global workspace research](../sources/newsletters/anthropic-jspace-global-workspace-2026-07.md)
