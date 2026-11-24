---
type: proposal
source: raw/newsletters/2026-10-13-dyna-2-general-purpose-physical-agents-with-hour.md
triage: proposals/triage/2026-10-11-to-2026-10-20-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Dyna Robotics — world-action model and multi-site deployment (Latent Space)

## Summary

### In short
General-purpose robots are starting to cross from pilots into repeat, multi-site contracts. Dyna Robotics says its robots, driven by a world-action model pre-trained on over a million hours of human video, fold thousands of napkins a day across several Din Tai Fung locations, held 99.4% success over 24 hours straight, and pick up new tasks from about 45 minutes of demonstrations. The proposal adds one status bullet and one Recent-changes entry to Physical AI deployment curve, plus a source page. The only hesitation is scope: Dyna stays a trend bullet rather than getting its own page.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 13 October 2026 Latent Space published a podcast episode, with a full transcript, in which swyx and Vibhu interview Jason Ma, co-founder and chief scientist of Dyna Robotics. The month before, Dyna had announced Dyna-2, which it calls a "world-action model": instead of only predicting the robot's next movements, it predicts future video of the scene together with the actions. Ma's argument is that a vision-language-action model (a chat-style vision model adapted to output robot commands) bakes in human choices about what matters, while predicting the raw camera future removes that bias. Dyna-2 was pre-trained on more than a million hours of mostly first-person human video, and Dyna claims scaling laws for transfer from human footage to robots across four orders of magnitude.

The follow-up, Dyna-2.1, wraps that model in an agentic harness: a higher-level planner that sequences skills, so a robot can run a laundry loop of about an hour (start the washer, do something else, move towels to the dryer when it finishes). Ma's commercial claim is the sharper one. Many robotics firms run single-site pilots; Dyna's biggest customer, Din Tai Fung, signed a larger contract after the first sites and now wants food-cutting too, which Ma says is at human parity. Best Western uses the robots for towel folding. Dyna builds its own wheeled semi-humanoid hardware rather than buying bipeds, runs inference on the device, and names dexterous hands as the current bottleneck: the best ones overheat quickly. Ma also concedes that robotics is still "very demo-oriented" as an industry.

### What changes
The Physical AI deployment curve page tracks robotics through Gemini Robotics 2 (one checkpoint across robot types) and the Microduck hobby robot, and its watch list asks for "evidence of robots moving from pilots into routine operations." Dyna is the first entry that speaks directly to that question.

- **Physical AI deployment curve** gains one status bullet on Dyna: world-action model versus vision-language-action framing, the agentic-harness layer for hour-long jobs, the Din Tai Fung multi-site expansion, the 99.4% / 24-hour and 45-minute figures, and the overheating-hands bottleneck. It adds one Recent-changes entry dated 13 October (three entries total, under the cap), one source, and the page date moves to 13 October.
- One new source page for the episode.

### What to weigh
Scope is the only call. The episode is detailed enough to justify a `tools/` or `models/` page for Dyna, but the wiki tracks robotics at trend level and has no robotics model pages, so this proposal keeps Dyna as a trend bullet. The broader "world models for agents" thread (Runway, World Labs, LeWorldModel) is also not unified here.

## Intended changes

- [ ] **Update** `wiki/trends/physical-ai-deployment.md` — add Dyna status bullet, add one Recent-changes entry dated 2026-10-13 (list goes from 2 to 3, no spill), append source `latent-space-dyna-robotics-2026-10-13` to frontmatter and `## Sources`, `as_of` 2026-08-29 → 2026-10-13
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-dyna-robotics-2026-10-13.md` — source summary

## Page drafts

### wiki/trends/physical-ai-deployment.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-13
sources: [physical-ai-deployment-2026-05-13, ainews-gpt-56-price-cut-2026-07-31, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, latent-space-dyna-robotics-2026-10-13]
```

`## Current status` — append this bullet after the Microduck bullet:

```
- **Dyna Robotics (October 2026):** the clearest pilot-to-production signal so far. Dyna-2 is a "world-action model" that predicts future video together with robot actions, pre-trained on over a million hours of mostly egocentric human video; Dyna argues this beats vision-language-action models because it predicts the raw world instead of a human-chosen abstraction. Dyna-2.1 wraps it in an agentic harness that sequences skills into hour-long jobs (a full laundry loop). Reported results: 99.4% success folding napkins for 24 hours straight, new tasks learned from ~45 minutes of demonstrations, and thousands of napkins folded daily across multiple Din Tai Fung locations after a larger follow-on contract (Best Western is another customer). Hardware is a wheeled semi-humanoid with on-device inference; dexterous hands remain the bottleneck because they overheat quickly.
```

`## Recent changes` — insert at top:

```
- [2026-10-13] Dyna Robotics (Latent Space interview): Dyna-2 world-action model on 1M+ hours of human video; Dyna-2.1 agentic harness runs hour-long workflows; 99.4% over 24h napkin folding; multi-site Din Tai Fung expansion cited as pilot-to-scaled deployment.
```

`## Sources` — append:

```
- [Latent Space — Dyna-2 and hour-long physical agents (Jason Ma)](../sources/newsletters/latent-space-dyna-robotics-2026-10-13.md)
```

### wiki/sources/newsletters/latent-space-dyna-robotics-2026-10-13.md (new)

```
---
title: 'Latent Space — Dyna-2: General Purpose Physical Agents with Hour-Long Autonomy (Jason Ma)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-13-dyna-2-general-purpose-physical-agents-with-hour.md
url: https://www.latent.space/p/dyna
published: 2026-10-13
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — Dyna-2: General Purpose Physical Agents with Hour-Long Autonomy (Jason Ma)

Podcast episode with full transcript. Dyna Robotics co-founder and chief scientist Jason Ma explains Dyna-2, a world-action model that predicts future video together with robot actions, pre-trained on over a million hours of human video, and Dyna-2.1, which puts an agentic harness around it for hour-long physical workflows. Ma separates single-site pilots from scaled deployments and cites Din Tai Fung's multi-site expansion as Dyna's proof point.

## Influenced pages
- [Physical AI deployment curve](../../trends/physical-ai-deployment.md) — Dyna status bullet and Recent-changes entry

## Key claims extracted
- Dyna-2 is pre-trained on 1M+ hours of mostly egocentric human video; Dyna claims human-to-robot scaling laws across four orders of magnitude.
- World-action models predict future video plus actions; Ma argues VLAs encode human bias by predicting only actions or abstract representations.
- Dyna-2.1 uses a hierarchical agentic harness to compose skills into hour-long tasks (e.g. a full laundry loop).
- 99.4% success folding napkins for 24 hours straight, including recovery after knocking over the stack.
- New tasks learned from ~45 minutes of demonstration data (e.g. vegetable chopping).
- Robots fold thousands of napkins per day across multiple US Din Tai Fung locations; Din Tai Fung signed a larger contract and wants food cutting next. Best Western uses them for towel folding.
- Hardware is built in-house: wheeled semi-humanoid with 4-DoF waist; on-device inference; distillation expected to become standard.
- Dexterous hands overheat quickly and are a current bottleneck.
```

## Schema / vocabulary additions

None.

## Open questions
- Should Dyna get its own page (`tools/` or `models/`), or stay as a trend bullet until a second source covers it (assumed: stay as a bullet)?
