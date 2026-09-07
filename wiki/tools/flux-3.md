---
title: FLUX 3
type: tool
domains: [creative]
subcategory: ai-video-generation
tags: [closed-source]
as_of: 2026-07-24
sources: [bfl-flux-3-2026-07-24]
---

# FLUX 3

Black Forest Labs' unified generative-media model, launched 2026-07-24 as FLUX 3 Video (early access), built on BFL's "Self Flow" research. Unlike a family of separate specialized generators, FLUX 3 is one architecture spanning image, video, audio, and — via a companion robotics release — action prediction. An open-weights "Dev" version is planned but not yet released.

## Current status (as of 2026-07-24)

- Capabilities (all with native audio generation): text-to-video, image-to-video (starting-frame continuation or reference-image driven), video-to-video carrying a source video's central elements (e.g. a character) into a new scene, video-audio continuation from an input clip, keyframe-to-video for controlled transitions, multilingual dialogue, wide style/aspect-ratio range, agentic multi-shot clip chaining, and strong typography/animated-design generation
- BFL claims this reproduces — independently, and possibly at state-of-the-art — capability sets previously shown separately by Seedance 2.0, Gemini Omni, and Grok Imagine
- Companion release **FLUX3-mimic** (from robotics startup mimic): a Video-Action Model built on FLUX 3, trained on robot and wearable data for general-purpose dexterity, deployable on a single on-prem GPU; already in testing with Audi, positioned as evidence FLUX 3's video world model transfers to real robot control and factory-impact prediction

## Strengths

- Broadest claimed capability span of any single generative-media model tracked in this wiki (image, video, audio, action prediction in one architecture)
- Character/scene continuity via video-to-video, and multi-shot agentic clip chaining — both aimed at longer-form, production-grade output rather than single clips

## Weaknesses / caveats

- The comparison against Seedance 2.0, Gemini Omni, and Grok Imagine is BFL's own launch framing, not an independent benchmark
- FLUX3-mimic's robotics-transfer claim is an early-stage startup partnership (Audi testing), not a published result
- Open-weights Dev version not yet released at time of writing

## Recent changes

- [2026-07-24] Initial page: FLUX 3 launch (Self Flow architecture, unified image/video/audio/action capabilities), FLUX3-mimic robotics companion release

## Sources

- [AINews — Black Forest Labs FLUX 3](../sources/newsletters/bfl-flux-3-2026-07-24.md)
