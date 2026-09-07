---
type: proposal
source: raw/newsletters/2026-07-28-ainews-much-ado-about-open-weights.md
status: pending
created: 2026-09-06
---

# Proposal: Kimi K3 weights ship, and Washington accuses Moonshot of distilling Fable

## Summary

### The source

Two AINews digests, dated 2026-07-23 and 2026-07-28, carry the next chapter of the Kimi K3 story this wiki has already been tracking as an announced-but-unreleased model. On the 28th, Moonshot followed through on its promised release window: full weights, tech report, and supporting infrastructure landed on Hugging Face under a "kimi-k3" license. The real specs are more precise than the announcement-era estimate — 2.8T total parameters, but 104B active per token across 896 experts with 16 active per token, not the flat "largest model" framing from launch. Moonshot also open-sourced three companion projects: FlashKDA (its Kimi Delta Attention kernels), MoonEP (an MoE communication library), and AgentENV (distributed agent-environment infrastructure) — practitioners read this as a fairly complete recipe for large-scale agentic post-training, not just a checkpoint drop. Distribution was immediate across a dozen providers (vLLM, Baseten, Modal, Fireworks, Nebius, Together, DigitalOcean, Cursor, Cognition, Ollama Cloud, Dell), and independent evals now confirm K3 beats Opus 4.8: #1 among open-weight models on Agent Arena (+9.75% net improvement), #1 overall in Frontend Code Arena, and the first open-weight model Cognition says "approaches frontier-level performance" on its FrontierCode 1.1 benchmark (58.2%, 63.6% pass rate). The license itself is notable: not OSI-style open source, but "open weights with carve-outs" — hosts over $20M/year revenue need a separate commercial agreement, and products above 100M MAU or $20M/month revenue must display "Kimi K3" in their UI.

The 23rd's digest carries a separate, more contentious thread: US Tech & Science Advisor Michael Kratsios publicly accused Moonshot of "large-scale, covert industrial distillation" of Anthropic's Fable to build K3, citing Moonshot's access to GB300 chips in Thailand as evidence. Treasury signaled the accusation could lead to Entity List sanctions. The claim drew immediate technical pushback: several commentators pointed out that only about 15 days separated Fable's release from K3's announcement, making a full distillation-driven capability jump implausible on that timeline, and legal commentators noted current copyright doctrine doesn't clearly support treating distillation as theft. Separately, the same digest logged fast-moving adoption data: Cline's usage share for K3 went from 0% to 16% in three days, making it the tool's #3 most-used open-weight model.

### What changes

The wiki currently has `models/kimi-k3.md` describing K3 as *announced* (2026-07-17) with weights only *promised* by 2026-07-27, and `trends/open-weight-momentum-broadens.md`'s Model-sovereignty section tracking the reversal of sovereignty pressure (US considering restricting Chinese open models) without a concrete sanctions threat yet named.

- **Kimi K3** moves from "announced" to "shipped": the intro and Current-status section are rewritten with the real architecture numbers (104B active / 896 experts / 16 active per token), the FlashKDA/MoonEP/AgentENV companion releases, day-0 multi-provider distribution, the license's commercial carve-outs, and the independent confirmation that K3 now beats Opus 4.8. A new caveat line notes the distillation accusation and sanctions threat, with the 15-day-gap counter-argument. Page date moves to 28 July.
- **Open-weight momentum broadens** gains a Model-sovereignty paragraph naming the Kratsios accusation and Treasury's sanctions signal as the concrete follow-through on the restriction pressure already being tracked, plus a new Recent-changes entry dated 28 July. The page is at its 10-entry Recent-changes cap, so the oldest entries will spill to history when this is applied.
- New source page for the 2026-07-28 AINews digest ("Much ado about Open Weights"), and a new source page for the 2026-07-23 digest's Kratsios/sanctions portion.

### What to weigh

Both sourcing threads are AINews aggregation digests (Twitter/Reddit recaps), not primary announcements — the specific architecture numbers (104B active, 896 experts) and the Cognition FrontierCode score are attributed to named practitioners quoted secondhand, not verified against Moonshot's own tech report or Cognition's own writeup. The distillation accusation is a live, contested claim with real pushback from technical commentators in the same source — it's presented here as "an accusation was made and disputed," not as an established fact, and that framing should be checked against the draft below.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/kimi-k3.md` — weights ship, real specs, distillation accusation
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — Model-sovereignty gains the distillation/sanctions thread
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-much-ado-about-open-weights-2026-07-28.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/ainews-laguna-kratsios-2026-07-23.md` — source summary (Kratsios/sanctions portion only; the Laguna S 2.1 model-release portion of this same newsletter is covered by a separate proposal)

## Page drafts

### wiki/models/kimi-k3.md (updated)

```md
---
title: Kimi K3
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [moonshot-ai, open-weights, agentic]
as_of: 2026-07-28
sources: [ainews-kimi-k3-2026-07-17, ainews-much-ado-about-open-weights-2026-07-28, ainews-laguna-kratsios-2026-07-23]
---

# Kimi K3

Moonshot AI's flagship, now shipped in full: weights, tech report, and supporting infrastructure released 2026-07-28 under a "kimi-k3" license. Supersedes [Kimi K2.7-Code](../history/models/kimi-k2-7-code.md) as Moonshot's current flagship; broader in scope than its coding-specialist predecessor.

## Current status (as of 2026-07-28)

- 2.8T total parameters, 104B active per token across 896 experts (16 active per token); 1M-token context; native text+image multimodal input
- Open-sourced alongside three companion projects: FlashKDA (Kimi Delta Attention kernels), MoonEP (MoE communication library), AgentENV (distributed agent-environment infrastructure) — a fairly complete recipe for large-scale agentic post-training, not just a checkpoint
- License is "open weights" with commercial carve-outs, not OSI-style open source: hosts over $20M/year revenue need a separate agreement; products above 100M MAU or $20M/month revenue must display "Kimi K3" in their UI
- Day-0 distribution across vLLM, Baseten, Modal, Fireworks, Nebius, Together, DigitalOcean, Cursor, Cognition, Ollama Cloud, and Dell Enterprise Hub
- Independent evals confirm K3 now beats Opus 4.8: #1 among open-weight models on Agent Arena (+9.75% net improvement), #1 overall in Frontend Code Arena, and Cognition reports it's the first open-weight model to "approach frontier-level performance" on FrontierCode 1.1 (58.2%, 63.6% pass rate)
- Reported ~2.5x scaling-efficiency improvement over K2, driven by numerical-stability choices at extreme scale (MXFP4 weights / MXFP8 activations); the tech report omits total training tokens

## Caveats

- Hallucination rate on Artificial Analysis's Omniscience eval regressed to 51% (from K2.6's 39%) despite the accuracy gain
- Disputed: US Tech & Science Advisor Michael Kratsios accused Moonshot of "large-scale, covert industrial distillation" of Anthropic's Fable, citing GB300 chip access in Thailand; Treasury has signaled possible Entity List sanctions. Technical critics note only ~15 days separated Fable's release from K3's announcement, making full distillation-driven capability transfer implausible on that timeline — unresolved as of this writing.
- At 104B active parameters, local deployment requires server-class or multi-GPU hardware; not practical on consumer GPUs

## Recent changes

- [2026-07-28] Weights, tech report, and FlashKDA/MoonEP/AgentENV shipped under a "kimi-k3" license; independent evals confirm it beats Opus 4.8; separately, Kratsios accuses Moonshot of distilling Fable, Treasury signals possible sanctions
- [2026-07-17] Announced: 2.8T params, Kimi Delta Attention, Intelligence Index 57, #1 Frontend Code Arena; supersedes Kimi K2.7-Code as Moonshot's flagship

## Sources

- [AINews — Kimi K3 (2.8T, largest open model)](../sources/newsletters/ainews-kimi-k3-2026-07-17.md)
- [AINews — Much ado about Open Weights](../sources/newsletters/ainews-much-ado-about-open-weights-2026-07-28.md)
- [AINews — Laguna S 2.1 / Kratsios distillation accusation](../sources/newsletters/ainews-laguna-kratsios-2026-07-23.md)
```

### wiki/trends/open-weight-momentum-broadens.md (updated)

```md
Add to the "## Model sovereignty as the latest driver (June 2026)" section, as a new paragraph after the existing final paragraph (the one ending "...pledging 5,000 AI-training slots to developing nations."):

The restriction pressure named its first concrete target on 2026-07-23: US Tech & Science Advisor Michael Kratsios publicly accused Moonshot AI of "large-scale, covert industrial distillation" of Anthropic's Fable to build Kimi K3, citing Moonshot's access to GB300 chips in Thailand, with Treasury signaling possible Entity List sanctions. The accusation drew immediate technical pushback — critics noted only about 15 days separated Fable's release from K3's announcement, making a full distillation-driven capability jump implausible on that timeline — and legal commentators flagged that current copyright doctrine doesn't clearly support treating distillation itself as theft. The dispute is unresolved, but it converts the sovereignty story from general policy pressure into a live sanctions threat against a specific, already-shipping model.

New "## Recent changes" entry (insert as the newest, before the existing [2026-07-21] entry):

- [2026-07-28] Kimi K3's weights ship in full (104B active/896 experts, FlashKDA/MoonEP/AgentENV infra open-sourced); separately, Kratsios accuses Moonshot of covertly distilling Fable to build it, Treasury signals possible Entity List sanctions, critics call the timeline technically implausible

Frontmatter `sources:` gains: ainews-much-ado-about-open-weights-2026-07-28, ainews-laguna-kratsios-2026-07-23

New "## Sources" list entries:
- [AINews — Much ado about Open Weights](../sources/newsletters/ainews-much-ado-about-open-weights-2026-07-28.md)
- [AINews — Laguna S 2.1 / Kratsios distillation accusation](../sources/newsletters/ainews-laguna-kratsios-2026-07-23.md)

This page is at its 10-entry Recent-changes cap; applying this addition spills the oldest entries (currently [2026-05-30] and, if still oldest at apply time, [2026-06-02]) to `wiki/history/trends/open-weight-momentum-broadens.md` under a new "## Archived from current page on <apply date>" block.
```

### wiki/sources/newsletters/ainews-much-ado-about-open-weights-2026-07-28.md (new)

```md
---
title: "AINews — Much ado about Open Weights"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-28-ainews-much-ado-about-open-weights.md
url: https://www.latent.space/p/ainews-much-ado-about-open-weights
published: 2026-07-28
ingested: 2026-09-06
domains: [models]
---

# AINews — Much ado about Open Weights

AINews digest covering the day's open-weight news: Kimi K3's full weight release and independent benchmark confirmation that it beats Opus 4.8, plus the parallel open-weight politics story (NVIDIA's Open Secure AI Alliance, Anthropic's position statement, and reported US/Anthropic lobbying against open models) — the politics portion is covered by a separate proposal.

## Influenced pages

- [Kimi K3](../../models/kimi-k3.md) — weights ship, real architecture specs, independent Opus-4.8-beating confirmation
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Recent-changes entry for the K3 ship date

## Key claims extracted

- Kimi K3: 2.8T total / 104B active parameters, 896 experts (16 active per token), FlashKDA/MoonEP/AgentENV open-sourced alongside the model
- License: "kimi-k3", hosts over $20M/year need a separate agreement, 100M+ MAU or $20M+/month products must display "Kimi K3" branding
- Independent evals: #1 open-weight on Agent Arena (+9.75%), #1 overall Frontend Code Arena, Cognition FrontierCode 1.1 58.2% (63.6% pass rate)
- Day-0 distribution across vLLM, Baseten, Modal, Fireworks, Nebius, Together, DigitalOcean, Cursor, Cognition, Ollama Cloud, Dell Enterprise Hub
```

### wiki/sources/newsletters/ainews-laguna-kratsios-2026-07-23.md (new)

```md
---
title: "AINews — Laguna S 2.1 / Kratsios distillation accusation"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-23-ainews-laguna-s-21-released-cheaper-than-deep.md
url: https://www.latent.space/p/ainews-laguna-s21-released-cheaper
published: 2026-07-23
ingested: 2026-09-06
domains: [models]
---

# AINews — Laguna S 2.1 / Kratsios distillation accusation

AINews digest covering two separate stories: Poolside's Laguna S 2.1 model release (covered by a separate proposal), and US Tech & Science Advisor Michael Kratsios's public accusation that Moonshot AI covertly distilled Anthropic's Fable to build Kimi K3, with Treasury signaling possible Entity List sanctions and technical commentators disputing the timeline.

## Influenced pages

- [Kimi K3](../../models/kimi-k3.md) — distillation-accusation caveat
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Model-sovereignty paragraph on the sanctions threat

## Key claims extracted

- Kratsios accuses Moonshot of "large-scale, covert industrial distillation" of Fable, citing GB300 chip access in Thailand
- Treasury signals possible Entity List sanctions over the accusation
- Critics note ~15 days between Fable's release and K3's announcement, calling full distillation technically implausible on that timeline
- Cline's K3 usage share went from 0% to 16% in 3 days, becoming its #3 most-used open-weight model
```

## Schema / vocabulary additions

None.

## Open questions

None beyond the sourcing caveat noted above.
