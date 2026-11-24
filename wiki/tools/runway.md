---
title: Runway
type: tool
domains: [creative]
subcategory: ai-video-generation
tags: []
as_of: 2026-09-25
sources: [ainews-new-ai-infra-unicorns-2026-05-22, ainews-cosmos-nemotron-june-2026, latent-space-runway-worldprompt-2026-09-25]
---

# Runway

Runway is a generative-video company that is stretching from video editing into real-time world models. Its products now span three markets: creative editing (Aleph 2.0 / Edit Studio), interactive worlds (GWM Worlds 2), and simulation for robots and computer-use agents (GWM Robotics and an "interface world model"). It is reportedly valued at $5.3B after a $315M raise in February 2026.

## Current status (as of 2026-09-25)

- **Aleph 2.0 / Edit Studio** (May 2026): edit a single frame and the edit propagates through the rest of the video
- **GWM Worlds 2** (research preview, September 2026): streams interactive worlds as continuous 720p video at 24fps with 48kHz audio, steered by WorldPrompt, a fixed first frame plus timestamped events that can also be typed in live. Built by fine-tuning the base audio-video model on that format, retraining it to generate a few frames at a time, then distilling it for speed (about 50 → 4 denoising steps). Competes with Genie 3, Odyssey-2 Pro and World Labs' RTFM
- **Interface world model** (demo): renders a software front end as pixels and predicts what each click, drag or scroll does; pitched as synthetic data and a live training environment for computer-use agents, with a "fully neural operating system" as the end point
- **GWM Robotics**: starts from the Gen-4.5 video model, fine-tuned on hundreds of hours of a partner's robot data per embodiment (see [Physical AI deployment](../trends/physical-ai-deployment.md))
- Partner in NVIDIA's Cosmos Coalition, the release vehicle for [Cosmos 3](../models/cosmos-3.md)

## Weaknesses / caveats

- WorldPrompt is a prompt, not a scripting language: there is no game state to program
- Runway's own list of open problems: small errors pile up as generated frames feed back in, no reliable long-term memory, and training video over-represents successes, so unlikely actions do not yet produce equally realistic outcomes

## Recent changes

- [2026-09-25] GWM Worlds 2 research preview (real-time 720p/24fps worlds via WorldPrompt); interface world model and GWM Robotics shown.
- [2026-06-02] Named as NVIDIA's Cosmos Coalition partner for Cosmos 3.
- [2026-05-22] Launched Aleph 2.0 / Edit Studio for single-frame edit propagation across video.

## Sources

- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer (Runway Aleph 2.0 recap)](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra (June)](../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
- [Latent Space — Runway's WorldPrompt and the engineering of real-time worlds](../sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md)
