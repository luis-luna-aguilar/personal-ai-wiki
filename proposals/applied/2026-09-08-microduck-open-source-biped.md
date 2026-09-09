---
type: proposal
sources:
  - raw/newsletters/2026-08-28-ainews-openai-to-reach-agi-bar-by-end-2026.md
  - raw/newsletters/2026-08-29-ainews-openai-shuts-off-cursor.md
status: pending
created: 2026-09-08
---

# Proposal: Microduck — a $399 open-source biped robot

## Summary

### The source

Two consecutive AINews digests (2026-08-28 and 2026-08-29) cover the launch and aftermath of **Microduck**, a 25cm open-source biped robot from Pollen Robotics and Hugging Face, priced at $399 and slated to ship before Christmas. The robot carries 15 actuators and a notably rich sensor stack — camera, speaker, LiDAR, NFC, Bluetooth, Wi-Fi — and can be trained in a public Hugging Face simulation Space before deployment to the real hardware. Reaction was unusually strong for a robotics launch: units reportedly sold at a rate of roughly one every 5 seconds at peak, with over $2.6M in orders in the first 24 hours. Engineers highlighted deliberate simulator design choices as much as the price point — EMA-smoothed head tracking (the head is 38% of the robot's body weight) and explicit modeling of motor backlash via an unactuated hinge — and the open simulator quickly led to community experiments: AR placement, somersaults, headstands, breakdance-style behaviors.

### What changes

`trends/physical-ai-deployment.md` currently centers on Google DeepMind's Gemini Robotics 2 and hasn't yet covered a low-cost, community-trainable consumer robot. This proposal adds Microduck as a new Current-status bullet and Recent-changes entry, bumping the page's `as_of` to 2026-08-29 (the newer of the two source dates) and merging both source citations.

### What to weigh

Nothing beyond the sourcing already noted — both figures ($2.6M in 24h, one-every-5-seconds) come from AINews' tweet-recap coverage rather than a Pollen Robotics/Hugging Face primary sales statement, consistent with how most of this page's other entries are already sourced.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/physical-ai-deployment.md` — add Microduck bullet, bump `as_of`, add Recent-changes entry, merge 2 source citations
    > See draft below

Note: both source pages referenced here (`ainews-openai-agi-bar-2026-08-28.md`, `ainews-openai-shuts-off-cursor-2026-08-29.md`) are created by other proposals in this batch, which own them; this proposal only references their slugs.

## Page drafts

### wiki/trends/physical-ai-deployment.md (updated)

```md
---
as_of: 2026-08-29
sources: [physical-ai-deployment-2026-05-13, ainews-gpt-56-price-cut-2026-07-31, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29]
---

## Current status

(... existing bullets unchanged ...)

- **Microduck (August 2026):** Pollen Robotics and Hugging Face launched a $399 open-source biped robot (25cm, 15 actuators, camera/speaker/LiDAR/NFC/Bluetooth/Wi-Fi), trainable in a public Hugging Face simulation Space and deployable to real hardware. Reaction was unusually strong for robotics: roughly one unit sold every 5 seconds at peak, over $2.6M in orders in the first 24 hours. Engineers highlighted deliberate simulator design (EMA-smoothed head tracking, modeled motor backlash) alongside the price point; the open sim quickly led to community experiments (AR placement, somersaults, headstands, breakdance).

## Recent changes

- [2026-08-29] Microduck ($399 open-source biped, Pollen Robotics + Hugging Face) sells roughly one unit every 5 seconds at peak, $2.6M in orders in 24 hours; open Hugging Face simulation Space enables community-trained policies.
- (... existing entries follow ...)
```
