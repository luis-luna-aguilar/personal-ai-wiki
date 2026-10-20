---
type: proposal
source: raw/newsletters/2026-09-25-runways-worldprompt-and-the-engineering-of-real-t.md
sources:
  - raw/newsletters/2026-09-25-runways-worldprompt-and-the-engineering-of-real-t.md
  - raw/newsletters/2026-09-29-ainews-amd-buys-world-labs-for-82b-as-atlas-s.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Real-time world models — Runway GWM Worlds 2 and AMD buying World Labs

## Summary

### In short
Video models are turning into real-time, steerable simulators, and their main buyers may be robotics and agent training rather than filmmakers. Runway's GWM Worlds 2 streams interactive 720p, 24fps worlds that users steer with timestamped prompts, and a sibling model renders software interfaces as pure pixels; AMD paid $8.2B for World Labs, whose Atlas model predicts new camera views from 2D images. The proposal adds a Runway line to State of Creative, a world-models-as-simulators bullet to Physical AI deployment, and one alias to the knowledge-architectures hub. Hesitation: neither company gets a page, and the AMD story rests on a short newsletter excerpt.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Latent Space's 25 September article interviews Runway's CTO Kamil Sindi and research scientist Robin Kahlow about GWM Worlds 2, a research preview released earlier that month, with extra comments from co-CEO Anastasis Germanidis from a podcast whose transcript is attached. GWM Worlds 2 streams interactive worlds as continuous 720p video at 24 frames per second with 48kHz audio. Its new input format, WorldPrompt, fixes parts of the world, including the first frame, and then lists timestamped events that can also be typed in live; it is a prompt, not a scripting language, so there is no game state to program. Runway built it by fine-tuning its base audio-video model on that format, retraining it to generate a few frames at a time instead of a whole clip, and then distilling it for speed, for example from about 50 denoising steps to four. The team names three open problems: small errors pile up as generated frames feed back in, the model has no reliable long-term memory, and training video over-represents successes (more goals than misses), so different actions do not yet produce equally realistic outcomes. Competitors named are Google DeepMind's Genie 3, Odyssey-2 Pro and World Labs' RTFM.

In the podcast Germanidis shows an "interface world model" that renders a software front end directly as pixels and predicts what a click, drag or scroll does, with behaviour described in the prompt, and calls a fully neural operating system its end point; he pitches it as synthetic data and a live training environment for computer-use agents. GWM Robotics starts from the Gen-4.5 video model and is fine-tuned on hundreds of hours of a partner's robot data, per embodiment.

AINews' 29 September issue reports AMD buying World Labs for $8.2B, a price known because AMD is public. World Labs says Atlas, trained from scratch, predicts new camera views from 2D images and has "essentially solved" sparse reconstruction; it cites demand from robotics RL environments, scene generation, and real-estate and construction reconstruction, and it recently bought SceniX for robotics simulation.

### What changes
The wiki mentions Runway only for its Aleph 2.0 editor and as a Cosmos 3 partner, and Physical AI deployment says only that world models "may become more important" for robotics.

- **State of Creative** gains a GWM Worlds 2 line under AI video generation; its oldest Recent-changes entry (22 May, Figma Agent and Aleph 2.0) moves to history because the list is at the cap. Page date moves to 25 September.
- **Physical AI deployment curve** gains a bullet on world models as robotics simulators (GWM Robotics, Atlas, the AMD deal) and one Recent-changes entry. Page date moves to 29 September.
- **Knowledge architectures** gets "interface world model" added to its world-model row, and one Recent-changes entry; its date stays 19 October.
- Two source pages, one per newsletter story.

### What to weigh
Neither Runway's world models nor World Labs gets a page; both stay as lines until there is more than one source each. The AMD story is a short excerpt from the acquisition post, and the $8.2B figure comes only from the newsletter's headline. The triage also listed Odyssey's Agora-2 multi-agent world model from a third newsletter; it is left out as a one-line mention.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/creative.md` — adds a Runway GWM Worlds 2 bullet under AI video generation; adds one Recent-changes entry dated 2026-09-25; `as_of` → 2026-09-25; appends one source id and link

- [ ] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — list is at the cap of 10; the oldest entry ([2026-05-22] Figma Agent / Runway Aleph 2.0) moves to history

- [ ] **Update** `wiki/trends/physical-ai-deployment.md` — adds one Current-status bullet; adds one Recent-changes entry dated 2026-09-29 (2 → 3); `as_of` → 2026-09-29; appends two source ids and links

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — world-model term-map row gains the "interface world model" alias; adds one Recent-changes entry dated 2026-09-25 (inserted below the 2026-10-19 entry); `as_of` unchanged; appends one source id and link

- [ ] **Create** `wiki/sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md` — source page

- [ ] **Create** `wiki/sources/newsletters/ainews-amd-buys-world-labs-2026-09-29.md` — source page (story-specific; the newsletter's other stories are not covered)

## Page drafts

### wiki/state-of/creative.md (updated)

Frontmatter: `as_of: 2026-09-25`; append `latent-space-runway-worldprompt-2026-09-25` to `sources:`.

New bullet under `### AI video generation`, after the Runway Aleph 2.0 bullet:

```
- **Runway GWM Worlds 2** — Runway; research preview streaming interactive worlds at 720p/24fps with 48kHz audio, steered by WorldPrompt (fixed first frame plus timestamped, live-promptable events). Open problems: error accumulation, long-term memory, realistic outcomes for unlikely actions. Competes with Genie 3, Odyssey-2 Pro and World Labs' RTFM *(as of 2026-09-25)*
```

Recent changes (adds one entry at the top; the oldest spills):

```
- [2026-09-25] Runway GWM Worlds 2 (research preview) turns its audio-video model into a real-time interactive world at 720p/24fps via WorldPrompt, autoregressive post-training and step distillation (about 50 → 4 denoising steps); Runway also showed an "interface world model" that renders software UIs as pixels.
```

Sources (appends one line):

```
- [Latent Space — Runway's WorldPrompt and the engineering of real-time worlds](../sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md)
```

### wiki/history/state-of/creative.md (updated)

Appends under a new `## Archived from current page on <apply date>` header:

```
- [2026-05-22] Figma released a native in-canvas design agent (Gemini Flash + Claude Sonnet + Figma fine-tuned models; Every hands-on: good for first drafts, weak on detail fidelity) and Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video (AINews recap); both newsletter-sourced, no primary announcement fetched, no dedicated pages yet.
```

### wiki/trends/physical-ai-deployment.md (updated)

Frontmatter: `as_of: 2026-09-29`; append `latent-space-runway-worldprompt-2026-09-25` and `ainews-amd-buys-world-labs-2026-09-29` to `sources:`.

New bullet in `## Current status`, after "World models and simulation environments may become more important…":

```
- **World models as robotics simulators (September 2026):** video world-model companies are selling into robotics. Runway's GWM Robotics starts from its Gen-4.5 video model and is fine-tuned per partner embodiment on hundreds of hours of robot data, against the 100,000-plus hours robotics pre-training uses; Runway also pitches its interface world model as a training environment for computer-use agents. AMD bought World Labs for $8.2B; World Labs says its Atlas model predicts new camera views from 2D images, cites demand for robotics RL environments, and recently acquired SceniX for robotics simulation.
```

Recent changes (adds one entry at the top; 2 → 3):

```
- [2026-09-29] AMD acquired World Labs for $8.2B (Atlas new-view prediction, SceniX robotics simulation); Runway's GWM Robotics fine-tunes a general video model on hundreds of hours of robot data per embodiment.
```

Sources (appends two lines):

```
- [Latent Space — Runway's WorldPrompt and the engineering of real-time worlds](../sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md)
- [AINews — AMD buys World Labs for $8.2B](../sources/newsletters/ainews-amd-buys-world-labs-2026-09-29.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter: append `latent-space-runway-worldprompt-2026-09-25` to `sources:`; `as_of` stays 2026-10-19.

World-model row of the term map:

> **Before:** `| world model | the physical or video-prediction sense | canonical on [LeWorldModel](leworldmodel.md), [Cosmos 3](../models/cosmos-3.md), and [Physical AI deployment](../trends/physical-ai-deployment.md). DeepLethe markets [Utopia](../tools/utopia.md) as an "enterprise world model"; that is a marketing alias for an ontology-backed bitemporal knowledge graph and maps to the ontology row, not to this sense |`

```
| world model, interface world model | the physical or video-prediction sense | canonical on [LeWorldModel](leworldmodel.md), [Cosmos 3](../models/cosmos-3.md), and [Physical AI deployment](../trends/physical-ai-deployment.md). Runway's "interface world model" is the same sense applied to software: a video model that renders a UI as pixels and predicts the result of each click. DeepLethe markets [Utopia](../tools/utopia.md) as an "enterprise world model"; that is a marketing alias for an ontology-backed bitemporal knowledge graph and maps to the ontology row, not to this sense |
```

Recent changes (adds one entry, placed after the 2026-10-19 entry; 5 → 6):

```
- [2026-09-25] Mapped Runway's "interface world model" (video-generated software UIs) to the world-model row's video-prediction sense.
```

Sources (appends one line):

```
- [Latent Space — Runway's WorldPrompt and the engineering of real-time worlds](../sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md)
```

### wiki/sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md (new)

```
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

- [State of Creative](../../state-of/creative.md) — GWM Worlds 2 line
- [Physical AI deployment curve](../../trends/physical-ai-deployment.md) — GWM Robotics and world models as robotics simulators
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "interface world model" alias on the world-model row

## Key claims extracted

- GWM Worlds 2: real-time interactive worlds, continuous 720p at 24fps with 48kHz audio; research preview; first GWM Worlds launched December 2025
- WorldPrompt: fix parts of the world including the first frame, then timestamped events that can be prompted live; a prompting mechanism, not a scripting language, no controllable state
- Recipe: fine-tune the base audio-video model to WorldPrompt, post-train to autoregressive frame-by-frame generation, distill to real time (e.g. ~50 → 4 denoising steps)
- Open problems: error accumulation, context/GPU-memory management for infinite generation, no reliable long-term memory, counterfactual realism (training video over-represents successes)
- Competitors named: Genie 3 (720p/24fps, a few minutes of interaction), Odyssey-2 Pro, World Labs RTFM; Runway reportedly valued at $5.3B after a $315M raise in February
- Interface world model: renders a software front end as pixels, takes clicks/drags/scrolls, behaviour described in the prompt; pitched as synthetic data and an online RL environment for computer-use agents; end point is a "fully neural operating system"
- GWM Robotics: starts from Gen-4.5, fine-tuned on hundreds of hours of robot data, post-trained per partner embodiment
```

### wiki/sources/newsletters/ainews-amd-buys-world-labs-2026-09-29.md (new)

```
---
title: AINews — AMD buys World Labs for $8.2B
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-29-ainews-amd-buys-world-labs-for-82b-as-atlas-s.md
url: https://www.latent.space/p/ainews-amd-buys-world-labs-for-82b
published: 2026-09-29
ingested: 2026-10-20
domains: [creative, agents]
---

# AINews — AMD buys World Labs for $8.2B

AINews' 29 September lead story: AMD acquired Fei-Fei Li's World Labs for $8.2B, shortly after World Labs released Atlas, a model it says solves sparse reconstruction. The issue quotes World Labs' announcement; the rest of the issue covers other stories.

## Influenced pages

- [Physical AI deployment curve](../../trends/physical-ai-deployment.md) — world models as robotics simulators

## Key claims extracted

- AMD acquired World Labs; price $8.2B (known because AMD is public)
- Atlas: trained from scratch, predicts the next camera view from 2D images, claimed to outperform specialized models and "essentially" solve sparse reconstruction
- Demand cited: RL environments for robotics, scene generation for therapy and entertainment, reconstruction for real estate, design and construction
- World Labs acquired SceniX, building toward robotics simulation
```

## Schema / vocabulary additions

None.

## Open questions

- Should Runway get a tool page now that it appears across creative (Aleph 2.0, GWM Worlds 2) and robotics (GWM Robotics), or stay as state-of lines (assumed: lines only)?
