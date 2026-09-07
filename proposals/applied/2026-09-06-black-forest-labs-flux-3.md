---
type: proposal
source: raw/newsletters/2026-07-24-ainews-black-forest-labs-flux-3-multimodal-flo.md
status: pending
created: 2026-09-06
---

# Proposal: Black Forest Labs launches FLUX 3

## Summary

### The source

An AINews recap covers Black Forest Labs' launch of FLUX 3, two years after the company's original FLUX 1 image model first hinted at a video model to come. FLUX 3 is built on BFL's "Self Flow" research and is pitched as one unified architecture spanning image, video, audio, and — via a companion release — robot action prediction, rather than a family of separate specialized generators. Its claimed capabilities, all with native audio generation attached: text-to-video, image-to-video (continuing from a starting frame or using reference images), video-to-video that carries a source video's central elements (like a character) into a new scene, video-audio continuation from an input clip, keyframe-to-video for controlled transitions, multilingual dialogue, a wide range of visual styles and aspect ratios, agentic chaining of individual clips into longer multi-shot sequences, and strong typography/animated-design generation. BFL frames these as matching or beating capabilities shown separately by Seedance 2.0, Gemini Omni, and Grok Imagine — the first independent, and possibly state-of-the-art, reproduction of that full feature set in one model. An open-weights "Dev" version is planned but not yet released; FLUX 3 Video itself launched in early access.

The same announcement window included FLUX3-mimic from robotics startup mimic: a "Video-Action Model" built on top of FLUX 3, trained on robot and wearable data for general-purpose robot dexterity, deployable on a single on-prem GPU. mimic's claim is that FLUX 3's video world-modeling transfers directly into robot control quality and sample efficiency — they're already testing it with Audi. The newsletter frames this as proof that FLUX 3 is learning a "sufficient world model" to drive physical robots and predict their impact in real factory settings, not just generate media.

### What changes

No existing wiki page tracks Black Forest Labs, FLUX, or mimic — this is a new entrant to `state-of/creative.md`, which currently lists Seedance 2.0, Dream Machine, NVIDIA Cosmos 3, and others under its "AI video generation" subcategory.

- **New page** `tools/flux-3.md`: the unified image/video/audio/action-prediction architecture, its full capability list, the comparison claims against Seedance 2.0/Gemini Omni/Grok Imagine, and the FLUX3-mimic robotics extension.
- **State of Creative** gains a new line for FLUX 3 under "AI video generation" and a new Recent-changes entry dated 24 July.

### What to weigh

The "beats Seedance 2.0, Gemini Omni and Grok Imagine" framing is BFL's own launch positioning as relayed by AINews, not an independent benchmark — there's no third-party arena or eval score attached, unlike, say, Ideogram's Arena ranking on the same page. The robotics-transfer claim (FLUX3-mimic, the Audi testing) is a young startup's own characterization of an early partnership, not a published result either. Both are included because they're specific and notable, but should be read as launch claims rather than verified state-of-the-art.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/flux-3.md` — new page for Black Forest Labs' FLUX 3
    > See draft below

- [ ] **Update** `wiki/state-of/creative.md` — add FLUX 3 to AI video generation subcategory, new Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/bfl-flux-3-2026-07-24.md` — source summary

## Page drafts

### wiki/tools/flux-3.md (new)

````md
---
title: FLUX 3
type: tool
domains: [creative]
subcategory: ai-video-generation
tags: [black-forest-labs, closed-source]
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
````

### wiki/state-of/creative.md (updated)

````md
### AI video generation

<!-- new bullet appended to the existing list: -->

- [FLUX 3](../tools/flux-3.md) — Black Forest Labs; unified image/video/audio/action-prediction architecture ("Self Flow"); native audio generation, video-to-video character continuity, agentic multi-shot clip chaining; companion FLUX3-mimic extends it to robot control (testing with Audi); open-weights Dev version planned *(as of 2026-07-24)*

## Recent changes

<!-- insert as the newest entry, before the 2026-07-08 Muse Image/Video entry: -->
- [2026-07-24] Black Forest Labs launched FLUX 3: unified image/video/audio/action-prediction model, positioned against Seedance 2.0/Gemini Omni/Grok Imagine; companion FLUX3-mimic release extends it to robot control.
````

### wiki/sources/newsletters/bfl-flux-3-2026-07-24.md (new)

````md
---
title: AINews — Black Forest Labs FLUX 3
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-24-ainews-black-forest-labs-flux-3-multimodal-flo.md
url: https://www.latent.space/p/ainews-black-forest-labs-flux-3-multimodal
published: 2026-07-24
ingested: 2026-09-06
domains: [creative]
---

# AINews — Black Forest Labs FLUX 3

AINews recap of Black Forest Labs' FLUX 3 launch: a unified image/video/audio/action-prediction model built on "Self Flow" research, plus the companion FLUX3-mimic robotics release from startup mimic.

## Influenced pages

- [FLUX 3](../../tools/flux-3.md) — new page
- [State of Creative](../../state-of/creative.md) — new AI video generation line, Recent-changes entry

## Key claims extracted

- FLUX 3 (FLUX 3 Video, early access 2026-07-24): unified architecture for image, video, audio, and action prediction; open-weights Dev version planned
- Capabilities: text-to-video, image-to-video, video-to-video with character continuity, video-audio continuation, keyframe-to-video, multilingual dialogue, agentic clip chaining, typography generation
- BFL claims parity/superiority vs. Seedance 2.0, Gemini Omni, and Grok Imagine (launch framing, not independent benchmark)
- FLUX3-mimic (robotics startup mimic): Video-Action Model built on FLUX 3, robot/wearable training data, single on-prem GPU deployment, testing with Audi
````

## Schema / vocabulary additions

None.

## Open questions

None.
