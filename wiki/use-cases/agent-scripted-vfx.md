---
title: Agent-scripted VFX
type: use-case
domains: [creative, agents]
tags: [agentic, vision]
as_of: 2026-11-24
sources: [every-vibe-check-afterimage-vfx-2026-09-18, meta-sam-3-1-model-api]
---

# Agent-scripted VFX

A general-purpose coding agent does visual-effects work on live-action footage by writing code against the tools VFX artists already use: open segmentation and matting models for masks, Python for tracking and compositing, Nuke's scripting API for the final composite, and Blender for 3D elements. The humans direct; the agent operates the software. Studio Afterimage's September 2026 test on real commercial footage is the reference case.

## Current guidance

- Expect it to work for **rigid, geometric additions**: buildings, glassware, product-like objects, set replacements. Afterimage added a building to a street, a wineglass with believable transparency and a float outside a window in handheld iPhone footage.
- Masking and tracking come first. The agent chose Robust Video Matting for people and [SAM 3.1](../sources/articles/meta-sam-3-1-model-api.md) for initial object masks, then refined both with its own code.
- Keep everything editable. The value over pure generative video is control: each fix is a code or scene change, not a re-roll.
- Budget for close direction. Annotated screenshots and repeated, specific corrections were needed on every good shot.

## Failure modes

- **Organic forms.** Animals and body parts looked wrong even when still and moved without weight.
- **Scene interaction.** New elements did not deform or affect the scene: eyelids did not merge into skin, grass did not react to hooves.

## Costs

SAM 3.1 on Meta Model API: $2.50 per 1,000 images, $0.20 per 1,000 video frames; one zero-shot call detects, masks and tracks objects, through an OpenAI-SDK-compatible endpoint shared with Meta's Muse models *(as of 2026-11-24)*.

## Why it matters

Small effects that used to require hiring a specialist become something a small studio can prototype without up-front budgeting. Afterimage also reports a new aesthetic: maximal VFX added to casual footage it would never have treated before. The test ran on GPT-6 Astra, since replaced; the pattern, not the model, is what carries forward.

## Related

- [State of Creative](../state-of/creative.md)
- [Runway](../tools/runway.md) — Aleph 2.0 was used for a texture pass
- [Video agents next frontier](../trends/video-agents-next-frontier.md) — agents using generators as tools; this page is agents using professional VFX software

## Sources

- [Every Vibe Check — Afterimage tests an agent on professional VFX](../sources/newsletters/every-vibe-check-afterimage-vfx-2026-09-18.md)
- [Meta — SAM 3.1 on Meta Model API](../sources/articles/meta-sam-3-1-model-api.md)
