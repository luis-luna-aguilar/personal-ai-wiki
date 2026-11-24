---
title: Anthropic — How AI agents shape experts' judgment calls
type: source
source_type: article
source_file: raw/articles/2026-11-24-anthropiccom-research-agents-judgment-calls.md
url: https://www.anthropic.com/research/agents-judgment-calls
published: 2026-10-27
ingested: 2026-11-24
domains: [agents]
---

# Anthropic — How AI agents shape experts' judgment calls

A randomized study by Amaç Herdağdelen, Hailey Joren and Alex Tamkin. Professional analysts did a realistic causal-inference task with Claude Code, whose agent was covertly given a coin-flip preference on each open analytical decision. Analysts mostly adopted the agent's preferences, explained them in its words, and still described the decisions as their own. The authors argue this undermines human sign-off as an independent check, including in AI safety research, where agents increasingly run experiments.

## Influenced pages
- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — new "Deferral on judgment calls" section, guidance bullet and failure mode

## Key claims extracted
- 61 analysts recruited; 50 used the agent (Claude Code, Opus 4.8 at High effort); median task time 65 minutes
- Four analytical choices (outcome measure, comparison method, population, weighting) and a final recommendation; the agent's lean was set by coin flip, with instructions to argue honestly, update on evidence and never mislead
- Analysts matched the lean 86% overall (92%, 82%, 81%, 90% per decision); the final recommendation moved less (54% vs 36% rollout); four leans predicted 82% of recommendations vs a 61% baseline
- Prior-stated preferences switched 60% when the agent disagreed vs 6% when it agreed (38 cases; 95% CI on the gap 24–82 points)
- 77% reused the agent's arguments, 15% credited it; confidence was similar for full followers (71) and others (73); no tested characteristic reliably predicted deferral
- Without the agent: 6 of 11 made serious methodological errors vs 3 of 50 with it; median 90 vs 65 minutes; the no-agent group was less experienced
- With no assigned lean, Opus 4.8 made the same five choices in 112 of 123 runs
- Limits: strengthened leans; one task, field and model; average effects only. Proposed directions: measuring deferral, agents that argue each option or ask first, institutions deciding which decisions need a person's own judgment
