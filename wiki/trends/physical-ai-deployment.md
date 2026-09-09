---
title: Physical AI deployment curve
type: trend
domains: [agents]
tags: [agentic]
as_of: 2026-08-29
sources: [physical-ai-deployment-2026-05-13, ainews-gpt-56-price-cut-2026-07-31, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29]
---

# Physical AI deployment curve

Physical AI and robotics are developing alongside screen agents, but on a different deployment curve. The loop is not purely digital: validation, hardware reliability, environment variation, safety, logistics, and supply chains shape adoption as much as model capability.

## Current status

- Current sources cluster around robotics infrastructure, humanoid trials, construction/data-center robots, world models, and geopolitics of the robotics supply chain.
- Physical deployment requires stronger validation than screen agents because failures can damage property or harm people.
- World models and simulation environments may become more important for robotics than text-only task benchmarks.
- Google DeepMind's Gemini Robotics 2 (July 2026) is the clearest embodied-generality jump so far: a single checkpoint now reportedly controls multiple robot hardware types, extending from tabletop manipulation to whole-body humanoid control and multi-robot coordination, with a companion embodied-reasoning model (Gemini Robotics ER 2) that plans, coordinates with a VLA model, tracks progress, and recovers from failed steps during multi-minute tasks. A variant, On-Device 2, reportedly adapts to a new two-arm robot from fewer than 200 examples.
- **Microduck (August 2026):** Pollen Robotics and Hugging Face launched a $399 open-source biped robot (25cm, 15 actuators, camera/speaker/LiDAR/NFC/Bluetooth/Wi-Fi), trainable in a public Hugging Face simulation Space and deployable to real hardware. Reaction was unusually strong for robotics: roughly one unit sold every 5 seconds at peak, over $2.6M in orders in the first 24 hours. Engineers highlighted deliberate simulator design (EMA-smoothed head tracking, modeled motor backlash) alongside the price point; the open sim quickly led to community experiments (AR placement, somersaults, headstands, breakdance).

## What to watch

- Evidence of robots moving from pilots into routine operations.
- Safety-case and validation practices for embodied agents.
- Whether world-model advances translate into reliable real-world control.

## Recent changes

- [2026-08-29] Microduck ($399 open-source biped, Pollen Robotics + Hugging Face) sells roughly one unit every 5 seconds at peak, $2.6M in orders in 24 hours; open Hugging Face simulation Space enables community-trained policies.
- [2026-07-31] Google DeepMind launched Gemini Robotics 2: one checkpoint reportedly controls multiple robot hardware types, whole-body humanoid control, multi-robot coordination; companion Gemini Robotics ER 2 embodied-reasoning model; On-Device 2 adapts to a new two-arm robot from fewer than 200 examples.

## Related

- [LeWorldModel](../concepts/leworldmodel.md) - world-model research relevant to simulation and embodied-agent planning.
- [State of Agents](../state-of/agents.md) - broader agent runtime and orchestration landscape.

## Sources

- [Physical AI deployment signals - May 2026](../sources/newsletters/physical-ai-deployment-2026-05-13.md)
- [AINews — GPT-5.6 price cuts, Inkling-Small, Gemini Robotics 2](../sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
