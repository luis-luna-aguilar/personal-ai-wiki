---
title: Physical AI deployment curve
type: trend
domains: [agents]
tags: [agentic]
as_of: 2026-10-13
sources: [physical-ai-deployment-2026-05-13, ainews-gpt-56-price-cut-2026-07-31, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, latent-space-dyna-robotics-2026-10-13, latent-space-runway-worldprompt-2026-09-25, ainews-amd-buys-world-labs-2026-09-29]
---

# Physical AI deployment curve

Physical AI and robotics are developing alongside screen agents, but on a different deployment curve. The loop is not purely digital: validation, hardware reliability, environment variation, safety, logistics, and supply chains shape adoption as much as model capability.

## Current status

- Current sources cluster around robotics infrastructure, humanoid trials, construction/data-center robots, world models, and geopolitics of the robotics supply chain.
- Physical deployment requires stronger validation than screen agents because failures can damage property or harm people.
- World models and simulation environments may become more important for robotics than text-only task benchmarks.
- **World models as robotics simulators (September 2026):** video world-model companies are selling into robotics. [Runway](../tools/runway.md)'s GWM Robotics starts from its Gen-4.5 video model and is fine-tuned per partner embodiment on hundreds of hours of robot data, against the 100,000-plus hours robotics pre-training uses; Runway also pitches its interface world model as a training environment for computer-use agents. AMD bought World Labs for $8.2B; World Labs says its Atlas model predicts new camera views from 2D images, cites demand for robotics RL environments, and recently acquired SceniX for robotics simulation.
- Google DeepMind's Gemini Robotics 2 (July 2026) is the clearest embodied-generality jump so far: a single checkpoint now reportedly controls multiple robot hardware types, extending from tabletop manipulation to whole-body humanoid control and multi-robot coordination, with a companion embodied-reasoning model (Gemini Robotics ER 2) that plans, coordinates with a VLA model, tracks progress, and recovers from failed steps during multi-minute tasks. A variant, On-Device 2, reportedly adapts to a new two-arm robot from fewer than 200 examples.
- **Microduck (August 2026):** Pollen Robotics and Hugging Face launched a $399 open-source biped robot (25cm, 15 actuators, camera/speaker/LiDAR/NFC/Bluetooth/Wi-Fi), trainable in a public Hugging Face simulation Space and deployable to real hardware. Reaction was unusually strong for robotics: roughly one unit sold every 5 seconds at peak, over $2.6M in orders in the first 24 hours. Engineers highlighted deliberate simulator design (EMA-smoothed head tracking, modeled motor backlash) alongside the price point; the open sim quickly led to community experiments (AR placement, somersaults, headstands, breakdance).
- **[Dyna Robotics](../robotics/dyna-robotics.md) (October 2026):** the clearest pilot-to-production signal so far. Its Dyna-2 "world-action model" predicts future video together with robot actions and was pre-trained on over a million hours of human video; Dyna-2.1 adds an agentic harness for hour-long jobs. Reported: 99.4% success over 24 hours of napkin folding, new tasks from ~45 minutes of demonstrations, and a larger follow-on contract across multiple Din Tai Fung locations. Dexterous hands, which overheat quickly, remain the bottleneck.

## What to watch

- Evidence of robots moving from pilots into routine operations.
- Safety-case and validation practices for embodied agents.
- Whether world-model advances translate into reliable real-world control.

## Recent changes

- [2026-10-13] Dyna Robotics (Latent Space interview): Dyna-2 world-action model on 1M+ hours of human video; Dyna-2.1 agentic harness runs hour-long workflows; 99.4% over 24h napkin folding; multi-site Din Tai Fung expansion cited as pilot-to-scaled deployment.
- [2026-09-29] AMD acquired World Labs for $8.2B (Atlas new-view prediction, SceniX robotics simulation); Runway's GWM Robotics fine-tunes a general video model on hundreds of hours of robot data per embodiment.
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
- [Latent Space — Dyna-2 and hour-long physical agents (Jason Ma)](../sources/newsletters/latent-space-dyna-robotics-2026-10-13.md)
- [Latent Space — Runway's WorldPrompt and the engineering of real-time worlds](../sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md)
- [AINews — AMD buys World Labs for $8.2B](../sources/newsletters/ainews-amd-buys-world-labs-2026-09-29.md)
