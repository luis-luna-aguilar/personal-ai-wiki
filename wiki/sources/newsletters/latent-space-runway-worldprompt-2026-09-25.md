---
title: 'Latent Space — Runway''s WorldPrompt and the engineering of real-time worlds'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-runways-worldprompt-and-the-engineering-of-real-t.md
url: https://www.latent.space/p/runway
published: 2026-09-25
ingested: 2026-10-20
domains: [creative, agents]
---

# Latent Space — Runway's WorldPrompt and the engineering of real-time worlds

Latent Space article plus podcast transcript with Runway (CTO Kamil Sindi, research scientist Robin Kahlow, co-CEO Anastasis Germanidis) on GWM Worlds 2, a research preview that turns Runway's audio-video generation model into a real-time interactive world, steered by a new WorldPrompt format. The podcast adds interface world models (software UIs rendered as pixels), the fully-neural-OS end point, and GWM Robotics.

## Influenced pages

- [Runway](../../tools/runway.md) — new tool page: GWM Worlds 2, interface world model, GWM Robotics, valuation
- [State of Creative](../../state-of/creative.md) — GWM Worlds 2 line
- [Physical AI deployment curve](../../trends/physical-ai-deployment.md) — GWM Robotics and world models as robotics simulators
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "interface world model" alias on the world-model row

## Key claims extracted

- GWM Worlds 2: real-time interactive worlds, continuous 720p at 24fps with 48kHz audio; research preview; first GWM Worlds launched December 2025
- WorldPrompt: fix parts of the world including the first frame, then timestamped events that can be prompted live; a prompting mechanism, not a scripting language, no controllable state
- Recipe: fine-tune the base audio-video model to WorldPrompt, post-train to autoregressive frame-by-frame generation, distill to real time (e.g. ~50 → 4 denoising steps)
- Open problems: error accumulation, context/GPU-memory management for infinite generation, no reliable long-term memory, counterfactual realism (training video over-represents successes)
- Competitors named: Genie 3 (720p/24fps, a few minutes of interaction), Odyssey-2 Pro, World Labs RTFM; Runway reportedly valued at $5.3B after a $315M raise in February
- Interface world model: renders a software front end as pixels, takes clicks/drags/scrolls, behaviour described in the prompt; pitched as synthetic data and an online RL environment for computer-use agents; end point is a "fully neural operating system"
- GWM Robotics: starts from Gen-4.5, fine-tuned on hundreds of hours of robot data, post-trained per partner embodiment
