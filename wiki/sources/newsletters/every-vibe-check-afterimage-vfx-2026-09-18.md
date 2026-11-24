---
title: 'Every Vibe Check — "Is Astra a Breakthrough for Indie Filmmakers?" (Afterimage VFX test)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-18-vibe-check-is-astra-a-breakthrough-for-indie-film.md
url: https://every.to/p/vibe-check-is-astra-a-breakthrough-for-indie-filmmakers
published: 2026-09-18
ingested: 2026-11-24
domains: [creative, agents]
---

# Every Vibe Check — Afterimage VFX test

Cyrus Duff and Josh Lee of creative studio Afterimage tested GPT-6 Astra (since replaced) on VFX shots from real commercial footage. The agent wrote its own masking code around Robust Video Matting, tracked a moving pan behind hands and sleeves, composited in Nuke through its Python API without the humans touching Nuke, and modelled rigid objects in Blender (a building, a wineglass, a parade float, a gold sphere) matched to camera motion, grain and lighting. For the float shot it used Meta's SAM 3.1 for initial masks and Runway Aleph 2.0 for a texture pass. It failed on organic forms (cows, eyes on fingertips) and on elements that must physically interact with the scene.

## Influenced pages
- [Agent-scripted VFX](../../use-cases/agent-scripted-vfx.md) — new use-case page
- [State of Creative](../../state-of/creative.md) — agent-scripted VFX line and Recent-changes entry

## Key claims extracted
- Agent controlled Nuke via its Python scripting API; the studio never used Nuke directly
- Masking via self-written code around Robust Video Matting; SAM 3.1 for initial masks on the window shot
- Rigid, geometric 3D additions in Blender worked convincingly, including glass transparency
- Organic forms and scene interactions failed even after extensive iteration
- Every good shot needed close direction (annotated screenshots, repeated corrections)
