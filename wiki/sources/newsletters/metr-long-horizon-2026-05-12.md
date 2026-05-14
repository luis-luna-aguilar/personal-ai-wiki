---
title: METR long-horizon benchmark update — May 2026
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-12-the-fallacy-of-the-16-hour-agent.md
published: 2026-05-12
ingested: 2026-05-13
domains: [models, agents]
---

# METR long-horizon benchmark update — May 2026

The newsletter "The Fallacy of the 16-Hour Agent" reports METR's update to its time-horizon task benchmark, focusing on Claude Mythos Preview's results and the interpretive nuances of the benchmark's "duration" metric.

## Influenced pages

- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — METR benchmark data added
- [State of Agents](../../state-of/agents.md) — long-horizon reliability note added to Recent changes

## Key claims extracted

- Claude Mythos Preview achieves 50% success on METR tasks rated as "16+ hours" human-equivalent — first model to reach the top of the current scale
- At 80% reliability, Mythos handles tasks worth ~3 human-hours of equivalent work
- Gemini 3.1 Pro is the nearest competitor at ~1.5 human-hours at the 80% threshold
- METR explicitly cautions: "duration" is a proxy for task difficulty (complexity, scope, number of steps), not literal wall-clock time — AI agents complete these tasks considerably faster than the human baseline
- The 80% threshold is the operationally relevant number: it represents reliable-enough performance to delegate without close supervision
- Perplexity's agent skill methodology is also covered in this newsletter (see separate proposal)
