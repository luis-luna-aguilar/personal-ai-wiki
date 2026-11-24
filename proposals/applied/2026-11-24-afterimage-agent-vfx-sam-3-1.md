---
type: proposal
source: raw/newsletters/2026-09-18-vibe-check-is-astra-a-breakthrough-for-indie-film.md
sources:
  - raw/newsletters/2026-09-18-vibe-check-is-astra-a-breakthrough-for-indie-film.md
  - raw/articles/2026-11-23-developermetacom-ai-models-sam-3-1.md
status: pending
created: 2026-11-24
---

# Proposal: Agents doing professional VFX (Afterimage test) and SAM 3.1 on Meta Model API

## Summary

### In short
A general-purpose agent can now do real visual-effects work by writing code against the tools VFX artists already use (Blender, Nuke, open segmentation models), as long as what it adds is rigid. Organic forms and elements that touch the scene still fail. Afterimage, a small creative studio, showed this on its own footage, and Meta's SAM 3.1, the masking model in that pipeline, now sells at $2.50 per 1,000 images. The proposal adds a use-case page and two lines on State of Creative. One reason to hesitate: the test ran on GPT-6 Astra, since replaced, so it is filed as a pattern, not a model result.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 18 September 2026 Every published a Vibe Check by Cyrus Duff and Josh Lee, who run Afterimage, a studio that makes videos for tech companies. They wanted to know whether a frontier agent could handle effects they would normally do by hand or hire a VFX specialist for, on footage from real shoots.

The results were good wherever the work could be expressed as code and geometry. To cut a boxer out of grainy 16mm film, the agent wrote Python around Robust Video Matting, an open-source model for separating people from backgrounds. It tracked a moving pan behind the actor's hands and sleeves, then built the final composite in Nuke, the industry compositing tool, entirely through Nuke's Python scripting interface. The two founders never opened Nuke themselves. In Blender it modelled a building into a Brooklyn street, a wineglass with believable transparency, and a giant parade float outside a window in casual iPhone footage, matching camera shake, film grain and lighting. For that window shot it took first masks from Meta's SAM 3.1 (Segment Anything, a model that finds and outlines objects), refined them with its own code, and used Runway's Aleph 2.0 for a texture pass.

It failed in two places. Eyes grown out of fingertips never merged into the skin, and cows added to a field looked fake standing still and moved without weight. Meta's undated Model API page says SAM 3.1 detects, outlines and tracks objects through video in one zero-shot call, for $2.50 per 1,000 images and $0.20 per 1,000 video frames, behind the same OpenAI-SDK-compatible endpoint and billing as Meta's Muse models.

### What changes
The wiki tracks video generators and agent-driven editors such as Palmier on State of Creative, but nothing on agents operating professional VFX software, and it has no SAM entry.

- New page `use-cases/agent-scripted-vfx.md`: the pattern (masking, tracking and compositing as code, 3D work in Blender), what works, what fails, and SAM 3.1 as a priced masking step. Page date 24 November.
- **State of Creative** gains two lines under AI video generation, one for the pattern and one for SAM 3.1, plus two Recent-changes entries (18 September and 24 November). The list is at its cap, so the two oldest entries (19 and 24 June) move to history. Page date moves to 24 November.
- **Index** gains the use-case page; the use-case count goes from 4 to 5.
- Two new source pages, one for the Vibe Check and one for the SAM 3.1 page.

### What to weigh
The SAM 3.1 page carries no date, so its price lines use this ingest date, 24 November, which also moves State of Creative's date. The drafts name GPT-6 Astra only as the model the test happened to use, with no claims about the model itself; the comparison with Sol in the source is left out for the same reason. The open question asks whether SAM 3.1 should get its own model page instead of living on the use-case page and the state-of line.

## Intended changes

- [ ] **Create** `wiki/use-cases/agent-scripted-vfx.md` — new use-case page
    > See draft below

- [ ] **Update** `wiki/state-of/creative.md` — add two lines at the end of "AI video generation" (agent-scripted VFX, SAM 3.1); adds two Recent-changes entries dated 2026-11-24 and 2026-09-18; `as_of` 2026-10-20 → 2026-11-24; append source ids `every-vibe-check-afterimage-vfx-2026-09-18` and `meta-sam-3-1-model-api`; two Sources lines
    > See draft below

- [ ] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — list is at the cap of 10; the two oldest entries (2026-06-19 Palmier/Firefly, 2026-06-24 OpenArt/Krea) move to history
    > See draft below

- [ ] **Update** `wiki/index.md` — add the use-case page under Use Cases; update the state-of/creative date; use-cases count 4 → 5, total 295 → 296
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-afterimage-vfx-2026-09-18.md` — source summary

- [ ] **Create** `wiki/sources/articles/meta-sam-3-1-model-api.md` — source summary

## Page drafts

### wiki/use-cases/agent-scripted-vfx.md (new)

```md
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
```

### wiki/state-of/creative.md (updated)

Frontmatter changes:

```md
as_of: 2026-11-24
sources: [..., quiverai-arrow-2-announcement-2026-09-16, every-vibe-check-afterimage-vfx-2026-09-18, meta-sam-3-1-model-api]
```

Append to the end of `### AI video generation`:

```md
- [Agent-scripted VFX](../use-cases/agent-scripted-vfx.md) — general-purpose agents doing professional VFX by scripting Blender, Nuke and segmentation models (Afterimage test on real footage); works for rigid objects, fails on organic forms and scene interactions *(as of 2026-09-18)*
- **SAM 3.1** — Meta; detects, masks and tracks objects through video in one zero-shot call on Meta Model API, $2.50 per 1K images and $0.20 per 1K frames; used for initial masks in agent VFX pipelines *(as of 2026-11-24)*
```

`## Recent changes` — insert two entries (2026-11-24 at the top; 2026-09-18 between the 2026-09-25 and 2026-09-16 entries); then drop the two oldest (2026-06-19, 2026-06-24) per the Spill item. Resulting list:

```md
## Recent changes

- [2026-11-24] Meta lists SAM 3.1 (detect, segment and track in one call) on Meta Model API at $2.50 per 1K images and $0.20 per 1K video frames.
- [2026-10-20] Suno opened Speech (beta), billed as the first audio model that generates voice and music together as one track.
- [2026-09-25] Runway GWM Worlds 2 (research preview) turns its audio-video model into a real-time interactive world at 720p/24fps via WorldPrompt, autoregressive post-training and step distillation (about 50 → 4 denoising steps); Runway also showed an "interface world model" that renders software UIs as pixels.
- [2026-09-18] Afterimage's test shows an agent doing professional VFX on real footage by scripting Blender, Nuke and segmentation models; rigid objects work, organic forms and scene interactions do not.
- [2026-09-16] Claude Design moved into Claude conversations as Anthropic merged chat and Cowork, launching Claude Docs and Claude Slides beside it (all beta on paid plans).
- [2026-09-16] QuiverAI released [Arrow 2](../models/arrow-2.md) and Arrow 2 Telos, vector-graphics models that output editable SVGs, with a rebuilt app and a developer API platform.
- [2026-09-01] Fal's H3 Max Live crosses faster-than-realtime video generation (35x inference speedup over MiniMax H3's official endpoint), enabling a continuous, audience-steerable live-video product; Fal also launched Reference-to-Video for MiniMax H3 Max at up to real-time factor 1.
- [2026-07-24] Black Forest Labs launched FLUX 3: unified image/video/audio/action-prediction model, positioned against Seedance 2.0/Gemini Omni/Grok Imagine; companion FLUX3-mimic release extends it to robot control.
- [2026-07-08] Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp and previewed Muse Video; AINews describes an agentic generation loop with planning, tool use, code execution, and self-refinement.
- [2026-06-29] Every's PowerPoint analysis adds a caution for slide agents: polished enterprise decks require supporting skills, scripts, references, and review loops.
```

Append to `## Sources`:

```md
- [Every Vibe Check — Afterimage tests an agent on professional VFX](../sources/newsletters/every-vibe-check-afterimage-vfx-2026-09-18.md)
- [Meta — SAM 3.1 on Meta Model API](../sources/articles/meta-sam-3-1-model-api.md)
```

### wiki/history/state-of/creative.md (updated — spill)

Append at the end (ascending date order, as the file already uses):

```md
- [2026-06-19] Palmier and Adobe Firefly Assistant show creative tooling moving toward agentic desktop workflows: video editing and multi-app creative tasks executed from natural-language instructions.
- [2026-06-24] OpenArt Director and Krea 2 Raw/Turbo signal creative workflows splitting between conversational editing products and open fine-tuning ecosystems.
```

### wiki/index.md (updated)

State-of line date:

```md
- [state-of/creative](state-of/creative.md) — current state of AI creative tools across video, image, avatar, slides, UI generation, real-time world models, open models, AI music, and creative-agent caveats *(as_of: 2026-11-24)*
```

Add under `## Use Cases`:

```md
- [use-cases/agent-scripted-vfx](use-cases/agent-scripted-vfx.md) — general-purpose agents doing professional VFX by scripting Blender, Nuke and segmentation models (Afterimage test); rigid objects work, organic forms fail; SAM 3.1 pricing *(as_of: 2026-11-24)*
```

Page count: `- use-cases: 5`; `**Total content pages: 296.**`

### wiki/sources/newsletters/every-vibe-check-afterimage-vfx-2026-09-18.md (new)

```md
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
```

### wiki/sources/articles/meta-sam-3-1-model-api.md (new)

```md
---
title: Meta — Segment Anything Model (SAM) 3.1 on Meta Model API
type: source
source_type: article
source_file: raw/articles/2026-11-23-developermetacom-ai-models-sam-3-1.md
url: https://developer.meta.com/ai/models/sam-3-1/
ingested: 2026-11-24
domains: [creative]
---

# Meta — SAM 3.1 on Meta Model API

Meta's model page for SAM 3.1, its object detection, segmentation and tracking model, served on inference built for its DETR architecture. One zero-shot call returns boxes, pixel-precise masks and identity-preserving tracks through video, prompted by a short noun phrase. It shares keys, docs and billing with the Muse models on Meta Model API, through an OpenAI-SDK-compatible endpoint. The page is undated.

## Influenced pages
- [Agent-scripted VFX](../../use-cases/agent-scripted-vfx.md) — masking step and pricing
- [State of Creative](../../state-of/creative.md) — SAM 3.1 line

## Key claims extracted
- Price: $2.50 per 1K images, $0.20 per 1K video frames (model id `sam-3-1`)
- Detection, segmentation and tracking in one call; zero-shot, no fine-tuning
- Same envelope, keys and billing as Muse Spark and Muse Voice Transcribe on Meta Model API
```

## Schema / vocabulary additions

None.

## Open questions

- SAM 3.1 lives here as a state-of line and a cost note on the use-case page. Should it get its own `models/` page instead (it would need a subcategory; none of the current ones fits a segmentation model cleanly)?
	- Ok, only on the use case page
