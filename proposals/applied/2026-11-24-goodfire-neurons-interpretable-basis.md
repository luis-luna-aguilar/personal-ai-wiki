---
type: proposal
source: raw/articles/2026-11-24-goodfirecom-research-neurons-as-an-interpretable-basis.md
sources:
  - raw/articles/2026-11-24-goodfirecom-research-neurons-as-an-interpretable-basis.md
  - raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md
status: pending
created: 2026-11-24
---

# Proposal: Goodfire's companion report — neurons as an interpretable basis

## Summary

### In short
Neurons in a real open-weight language model turn out to be readable units: Goodfire's companion report finds that most neurons in Qwen3.6-35B-A3B have one dominant job, and that agent-written descriptions let a judge model pick out when a neuron fires 95% of the time in its strongest range. Removing 92% of the weakest activations barely hurts the model. The proposal adds these results to **Mechanistic interpretability** and **Agent safety and alignment research**, replaces the caveat that the paper was unpublished, narrows the related watch item, and creates one source page. The reason to hesitate is the date: the page shows none, so 15 November comes from Every's "this week".

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
In October, Goodfire researcher Nick Cammarata published a long essay, "Neural Networks Are Already Clean". It argued that the field had misread its own evidence: the neurons of a neural network (the small computing units inside each layer) are mostly readable as they are, so researchers do not first need a second trained model to untangle them. The essay promised a technical companion with the language-model detail. In mid-November Goodfire published it as "Neurons as an Interpretable Basis", the first post in what it calls a series on "native interpretability": studying the network through its own units rather than through a learned stand-in.

The team studied the neurons of one open model, Qwen3.6-35B-A3B, and reports three findings. First, the model runs almost unchanged when the weakest 92.2% of neuron activations are switched off, and a light fine-tune restores full reasoning scores. What matters sits in the strongest few percent of firings, which is also where neurons are easiest to read. Second, in a sample of about 5,500 neurons, 69% are dominated by one "mode" (a coherent group of jobs): 47% have a single one, and others have one carrying at least 90% of their effect. Where there are several, they are few and can be told apart. Third, a frontier model working as a "Neuron Scientist" agent writes a plain-language description of each neuron. Given only that description, a judge model picks out the text that makes the neuron fire 95% of the time in the strong range (chance is 50%), and 89% against harder same-domain text. Activity simulated from the description recovers 73% of what a perfect reader could.

The authors list their own limits: one model family, weak activations left unexplained, and some neurons genuinely mixed.

### What changes
The wiki records Cammarata's essay on two pages, both noting that the companion paper had not yet appeared and asking whether it would support reading neurons directly.

- **Mechanistic interpretability** gains one current-status bullet with the report's three findings. Its caveat that the paper is unpublished is replaced with the report's own limits, and the page gains a Recent-changes entry. Page date moves to 15 November.
- **Agent safety and alignment research** has its Goodfire bullet extended with the report's headline result. The watch item about the companion paper is narrowed to outside replication and larger models, and the page gains a Recent-changes entry dated 15 November (8 of 10, no spill). Page date moves from 26 October to 15 November.
- One new source page for the report.

### What to weigh
The publication date is inferred. The report page carries no date, and Every's 15 November issue says Goodfire published it "this week", so 15 November is used as the date. The 95% figure is easy to over-read: Every says agents predict firing, but the paper reports a judge model working from agent-written descriptions, in the strongest activation range only, and the drafts keep that wording. The report runs to some 50,000 words; the abstract, findings, detection, mode statistics and conclusion were read in full, and most of the appendix was skimmed.

## Intended changes

- [ ] **Update** `wiki/concepts/mechanistic-interpretability.md` — one new Current-status bullet; Caveats rewritten for the published report; adds one Recent-changes entry dated 2026-11-15 (list goes to 2, no spill); append `goodfire-neurons-interpretable-basis-2026-11` to frontmatter `sources:` and one line to `## Sources`; `as_of` and Current-status stamp 2026-10-19 → 2026-11-15
    > See draft below

- [ ] **Update** `wiki/trends/agent-safety-and-alignment-research.md` — extend the Goodfire bullet; narrow the matching "What to watch" item; adds one Recent-changes entry dated 2026-11-15 (list goes to 8, no spill); append source id and Sources line; `as_of` 2026-10-26 → 2026-11-15
    > See draft below

- [ ] **Create** `wiki/sources/articles/goodfire-neurons-interpretable-basis-2026-11.md` — source summary

## Page drafts

### wiki/concepts/mechanistic-interpretability.md (updated)

Frontmatter changes:

```
as_of: 2026-11-15
sources: [goodfire-already-clean-2026-10, goodfire-neurons-interpretable-basis-2026-11]
```

Heading change: `## Current status (as of 2026-10-19)` → `## Current status (as of 2026-11-15)`

In `## Current status`, insert after the "~90% of neurons have one main job" bullet:

```
- **The companion report (November 2026)** tests the claim on the neurons of one open model, Qwen3.6-35B-A3B. Switching off the weakest 92.2% of activations costs 1.2–2.2 points on likelihood benchmarks, and a fine-tune of about 100M tokens restores reasoning. In a 5,468-pole sample, 69% are dominated by one mode (47% have a single one). Descriptions written by a "Neuron Scientist" agent let a judge model pick the text a neuron fires on 95% of the time in its strongest range (89% against same-domain text), and simulating a neuron from its description recovers 73% of a perfect reader's result.
```

`## Caveats`, replaced:

```
## Caveats
- The evidence comes from Goodfire alone, and the language-model results cover one model family (Qwen3.6-35B-A3B).
- Only strong activations are explained; the weak ones that make up most firings are left open, and some neurons are genuinely mixed.
- Contradicts the field's dominant SAE/dictionary-learning program; independent replication is pending.
- The step from "legible" to "solved" is labelled by the author as highly speculative.
```

In `## Recent changes`, insert above the 2026-10-19 entry:

```
- [2026-11-15] Goodfire's companion report, "Neurons as an Interpretable Basis": on Qwen3.6-35B-A3B, 92.2% of weak activations can be dropped, most neurons have one dominant mode, and agent-written descriptions predict firing 95% of the time in the strongest range.
```

In `## Sources`, append:

```
- [Neurons as an Interpretable Basis — Goodfire](../sources/articles/goodfire-neurons-interpretable-basis-2026-11.md)
```

### wiki/trends/agent-safety-and-alignment-research.md (updated)

Frontmatter changes: `sources:` appends `goodfire-neurons-interpretable-basis-2026-11`; `as_of: 2026-10-26` → `as_of: 2026-11-15`.

In `## Current signal`, the Goodfire bullet, replaced:

```
- **Goodfire: "networks are already clean" (2026):** Nick Cammarata argues the superposition evidence that pushed interpretability toward sparse-autoencoder decompositions was misread, that most neurons in modern models have one main job, and that agents acting as automated scientists could map frontier networks directly. He suggests alignment could then proceed through many small, targeted fixes. The November companion report backs this on one open model (Qwen3.6-35B-A3B): most neurons have one dominant mode, and agent-written descriptions predict when they fire 95% of the time in their strongest range. See [Mechanistic interpretability](../concepts/mechanistic-interpretability.md).
```

In `## What to watch`, the Goodfire item, replaced:

```
- Whether outside replications and larger models confirm Goodfire's single-model neuron results, or whether superposition holds up at scale
```

In `## Recent changes`, insert directly below the 2026-11-23 entry:

```
- [2026-11-15] Goodfire's companion report supports reading neurons directly on Qwen3.6-35B-A3B: most neurons have one dominant mode; agent-written descriptions predict firing 95% of the time in the strongest range.
```

In `## Sources`, append:

```
- [Neurons as an Interpretable Basis — Goodfire](../sources/articles/goodfire-neurons-interpretable-basis-2026-11.md)
```

### wiki/sources/articles/goodfire-neurons-interpretable-basis-2026-11.md (new)

```
---
title: Neurons as an Interpretable Basis — Goodfire
type: source
source_type: article
source_file: raw/articles/2026-11-24-goodfirecom-research-neurons-as-an-interpretable-basis.md
url: https://www.goodfire.com/research/neurons-as-an-interpretable-basis
published: 2026-11-15
ingested: 2026-11-24
domains: [models]
---

# Neurons as an Interpretable Basis — Goodfire

Goodfire's technical companion to Nick Cammarata's essay [Neural Networks Are Already Clean](goodfire-already-clean-2026-10.md), and the first post in its series on "native interpretability": studying a network through its own units instead of through a learned replacement such as a sparse autoencoder. The page carries no date. Every's 15 November 2026 newsletter says it came out that week, so `published` is inferred.

## The question
Can individual neurons (the hidden units of a transformer's MLP layers) be studied directly, or are they too mixed to read? The team tests three ways neurons could fail as units: rarely having a clear role, firing on too wide a range of inputs to describe briefly, or resisting descriptions precise enough to predict them.

## What they did
They ran 10 billion tokens through Qwen3.6-35B-A3B (an open mixture-of-experts model with about 5 million neurons), collected examples at many activation strengths, traced which neurons feed each neuron and which read its output, and had a frontier model (Claude Fable 5.0/5.1, Opus 5.5 or GPT-6 Sol) in a research harness, the "Neuron Scientist", write and test descriptions for samples of neurons (500 for the detection test). All scores are computed on held-out text.

## Findings
- **Sparse already.** Switching off the weakest 92.2% of activations leaves the model close to the original (1.2–2.2 points lower on likelihood benchmarks). About 91M tokens of fine-tuning and 9M of RL restore full reasoning scores. Most of a neuron's effect comes from its top and bottom 3% of firings.
- **Few jobs per neuron.** In a 5,468-pole sample, 69% are dominated by one "mode" (a coherent group of jobs): 47% have a single one, and in 46% of multi-mode poles the main mode does ≥90% of the damage. Where there are several, they are few and can be told apart by what feeds them and what reads them.
- **Predictable from a sentence.** Given the description, a judge model picks the snippet that makes a neuron fire 95% of the time in the strongest range against random text, and 89% against text from the same expert (chance 50%). Opus 5.5 scores 86% on the weakest band studied.
- **Simulatable.** Replacing a neuron's real activations with ones predicted from its description recovers 73% of what a perfect reader recovers in the top bands, with no model trained for the task.
- **Steerable.** For 94% of neurons the agent can write text that fires the neuron harder than anything in the 10B-token corpus.
- A popular counterexample, a Qwen3-32B "Colorado" neuron that also fires on the Tornado web framework, gets about 98.8% of its effect from place-related text; the Tornado link is a real association in the model (it wrongly places Tornado in Colorado), not storage noise.

## Limits (authors' own)
- One model family; generalization to other models and behaviors is untested.
- Weak activations, which make up most firings, are not explained.
- Some neurons are genuinely mixed, and some behavior remains unexplained.

## Influenced pages
- [Mechanistic interpretability](../../concepts/mechanistic-interpretability.md) — companion-report results; caveats updated
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Goodfire bullet extended; watch item narrowed

## Key claims extracted
- Up to 92.2% of the weakest neuron activations in Qwen3.6-35B-A3B can be ablated with 1.2–2.2 points of benchmark loss; light fine-tuning restores reasoning
- 69% of a 5,468-pole sample are dominated by one mode; 47% have a single mode
- Description-based detection: 95% vs random text, 89% vs same-expert text, strongest band
- Description-based simulation recovers 73% of a perfect-reader ceiling
- 94% of neurons can be driven past their corpus maximum by agent-written text
```

## Schema / vocabulary additions

None.

## Open questions

None.
