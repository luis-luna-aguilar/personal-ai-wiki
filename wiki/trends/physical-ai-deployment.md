---
title: Physical AI deployment curve
type: trend
domains: [agents]
tags: [agentic]
as_of: 2026-07-31
sources: [physical-ai-deployment-2026-05-13, ainews-gpt-56-price-cut-2026-07-31]
---

# Physical AI deployment curve

Physical AI and robotics are developing alongside screen agents, but on a different deployment curve. The loop is not purely digital: validation, hardware reliability, environment variation, safety, logistics, and supply chains shape adoption as much as model capability.

## Current status

- Current sources cluster around robotics infrastructure, humanoid trials, construction/data-center robots, world models, and geopolitics of the robotics supply chain.
- Physical deployment requires stronger validation than screen agents because failures can damage property or harm people.
- World models and simulation environments may become more important for robotics than text-only task benchmarks.
- Google DeepMind's Gemini Robotics 2 (July 2026) is the clearest embodied-generality jump so far: a single checkpoint now reportedly controls multiple robot hardware types, extending from tabletop manipulation to whole-body humanoid control and multi-robot coordination, with a companion embodied-reasoning model (Gemini Robotics ER 2) that plans, coordinates with a VLA model, tracks progress, and recovers from failed steps during multi-minute tasks. A variant, On-Device 2, reportedly adapts to a new two-arm robot from fewer than 200 examples.

## What to watch

- Evidence of robots moving from pilots into routine operations.
- Safety-case and validation practices for embodied agents.
- Whether world-model advances translate into reliable real-world control.

## Recent changes

- [2026-07-31] Google DeepMind launched Gemini Robotics 2: one checkpoint reportedly controls multiple robot hardware types, whole-body humanoid control, multi-robot coordination; companion Gemini Robotics ER 2 embodied-reasoning model; On-Device 2 adapts to a new two-arm robot from fewer than 200 examples.

## Related

- [LeWorldModel](../concepts/leworldmodel.md) - world-model research relevant to simulation and embodied-agent planning.
- [State of Agents](../state-of/agents.md) - broader agent runtime and orchestration landscape.

## Sources

- [Physical AI deployment signals - May 2026](../sources/newsletters/physical-ai-deployment-2026-05-13.md)
- [AINews — GPT-5.6 price cuts, Inkling-Small, Gemini Robotics 2](../sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md)
