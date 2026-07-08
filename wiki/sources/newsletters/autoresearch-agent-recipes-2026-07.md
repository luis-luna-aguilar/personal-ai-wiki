---
title: Autoresearch and agent recipes
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-01-autoresearch-the-feedback-loop-behind-self-improv.md
published: 2026-07-01
ingested: 2026-07-06
domains: [agents, training]
---

# Autoresearch and agent recipes

Roland Gavrilescu describes autoresearch as an outer loop for improving agent systems: agents study traces, evals, failures, human feedback, and cost signals to maintain the primary system. The source introduces "agent recipes" as portable bundles that include harnesses, models, evals, judges, human expertise, failure history, and signal-processing logic.

## Influenced pages
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — autoresearch outer loop
- [Harness](../../concepts/harness.md) — agent recipe packaging pattern
- [Agent evals](../../concepts/agent-evals.md) — human signal as early eval source
- [Agent skill methodology](../../training/agent-skill-methodology.md) — reusable recipe/skill framing

## Key claims extracted
- Autoresearch makes agent improvement a continuous loop around the primary agent system.
- Recipes package the operational ingredients needed to reproduce or transfer an agent workflow.
- Provider-agnostic infrastructure, audit logs, secure deployment, and human feedback are central constraints.
