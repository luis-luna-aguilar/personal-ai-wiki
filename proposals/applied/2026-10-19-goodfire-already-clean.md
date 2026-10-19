---
type: proposal
source: raw/articles/2026-10-19-already-cleangoodfirecom.md
status: pending
created: 2026-10-19
---

# Proposal: "Neural Networks Are Already Clean" — Nick Cammarata (Goodfire)

## Summary

### In short
Neural networks may already be mostly readable. Most neurons do one main job, and the famous "mixed" neurons were misread: the cat-and-car neuron actually detects V shapes. If that holds, the field's costly detour of training a second model just to untangle neurons is largely unnecessary, and agents acting as automated scientists could map frontier models directly. Nick Cammarata of Goodfire reports that about 90% of Qwen3-32B neurons do one job in preliminary audits. Creates `concepts/mechanistic-interpretability.md`, the wiki's first page on the field. Hesitate only if you'd rather not open a new concept page for interpretability yet.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Nick Cammarata co-authored some of the founding interpretability papers at OpenAI and on Distill, and now works at Goodfire. In 2026 he published a long interactive essay arguing that the field misread its own key evidence. Interpretability is the work of figuring out what the parts of a neural network actually do. Its core worry has been "superposition": the idea that a network short on room packs unrelated concepts into the same neuron because they rarely collide. If that were true, neurons would be meaningless knots. You would have to train a second model, such as a sparse autoencoder (SAE), to untangle the network before studying it, and that is where much of the field went.

Cammarata argues the knots were mostly misreadings. The field's most famous mixed neuron, which seemed to fire on both cats and cars, turns out on a second look to detect V shapes: pointed cat faces, car fronts, fox faces, flames. What looks like mixing is usually "recursive generalization". A neuron grows offshoots of related ideas, like a branch sprouting twigs; one that detected "iy" grew into "diy" and then "do it yourself". With ordinary architecture fixes, 99–100% of neurons in the last layer of an old vision model become readable, up from almost none. In preliminary audits of Qwen3-32B, about 90% of neurons have one main job, ~7% two related jobs, and ~2–4% are unexplained; he says the numbers depend on where thresholds are set. His conclusion is that agents working as automated scientists could map frontier networks directly and make interpretability far more tractable than assumed. He calls that last step highly speculative.

### What changes
The wiki has no page on interpretability as a field. The only neighbour is **Model internal workspace**, which covers Anthropic's J-space finding.

- New page `concepts/mechanistic-interpretability.md`: plain-language definition, the superposition vs recursive-generalization disagreement, current claims, why it matters for safety, and caveats.
- **Agent safety and alignment research** gains one current-signal bullet and one watch item on the automated-scientist approach, plus a Recent-changes line. Page date moves to 19 October.
- **Model internal workspace** gains a Related line to the new page (no date change; nothing about J-space changes).
- **Index** gains the concept line; concepts count goes from 28 to 29. One new source page, written to explain the essay.

### What to weigh
The main call is scope. This opens the wiki's first page on interpretability as a field, rather than adding to **Model internal workspace**, which covers a single Anthropic finding. The essay runs to about 41,000 words, and the core argument and key sections were read, not every appendix. The page gives only the year, so 19 October (the ingest date) stands in.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/concepts/mechanistic-interpretability.md` — new concept page

- [ ] **Update** `wiki/trends/agent-safety-and-alignment-research.md` — one Current-signal bullet, one What-to-watch bullet, one Related line, one Recent-changes entry dated 2026-10-19 (list at 5; no spill), source id + link, `as_of` → 2026-10-19

- [ ] **Update** `wiki/concepts/model-internal-workspace.md` — add `## Related` section with a link to the new page

- [ ] **Update** `wiki/index.md` — add concept line; `concepts: 28` → `29`; `as_of` → 2026-10-19 on the agent-safety line

- [ ] **Create** `wiki/sources/articles/goodfire-already-clean-2026-10.md` — source summary

## Page drafts

### wiki/concepts/mechanistic-interpretability.md (new)

```
---
title: Mechanistic interpretability
type: concept
domains: [models]
tags: []
as_of: 2026-10-19
sources: [goodfire-already-clean-2026-10]
---

# Mechanistic interpretability

Mechanistic interpretability tries to explain how a neural network works from the inside: what individual neurons respond to, how they connect into circuits, and how information flows from input to output. It is the "read the source code" approach to AI safety, as opposed to judging a model only by what it says.

## Current status (as of 2026-10-19)
- The field's working assumption since Zoom In (2020) has been **superposition**: networks short on room pack unrelated concepts into the same neuron, so neurons are unreadable and must first be untangled with a second trained model, usually a sparse autoencoder (SAE).
- Nick Cammarata (Goodfire, 2026), a co-author of the original evidence, argues that evidence was misread and that networks are "already clean". The canonical cat-and-car neuron is a V-shape detector. With ordinary architecture fixes, 99–100% of InceptionV1's last-layer neurons become readable, up from almost none.
- He reports that in preliminary audits of Qwen3-32B, ~90% of neurons have one main job, ~7% two related jobs, and ~2–4% are unexplained. Results look similar in trillion-parameter MoE models (Kimi K3). He flags that these numbers depend on thresholds.
- In his vision-model tests, 88% of SAE activity was near-copies of single neurons, and removing the rest left accuracy unchanged. He argues SAEs and probes belong at the end of an analysis, not the start.
- [Model internal workspace](model-internal-workspace.md) (Anthropic's J-space) is a separate line of work on a reportable internal representation.

## The disagreement in plain terms
**Superposition** says a neuron firing on "floppy dog ears + Latin poetry" is a storage trick: the pairing means nothing, so you must unfold the network before you can study it. **Recursive generalization** says neurons group *related* things and then sprout related offshoots. One neuron that detected "iy" grew into "diy" and then "do it yourself". Under this view, the odd extra activations are clues to follow. The two predict opposite things, and Cammarata says watching neurons grow during training settles it in favour of generalization.

## Why it matters
If networks are mostly legible as they are, interpretability becomes ordinary science that agents can run at scale: label neurons, find recurring patterns, test explanations, repeat. It stops being a search for a cleverer decomposition. Cammarata's safety claim is that deception has no reason to hide from the model's own circuitry, so the risk is not a hidden activation but failing to read what is in plain sight.

## Caveats
- One author's essay; the technical companion paper is not yet published.
- Contradicts the field's dominant SAE/dictionary-learning program; independent replication is pending.
- The step from "legible" to "solved" is labelled by the author as highly speculative.

## Recent changes
- [2026-10-19] Page created from Cammarata's "Neural Networks Are Already Clean" (Goodfire): challenges superposition as the explanation for messy neurons.

## Sources
- [Neural Networks Are Already Clean — Nick Cammarata (Goodfire)](../sources/articles/goodfire-already-clean-2026-10.md)
```

### wiki/trends/agent-safety-and-alignment-research.md (updated)

Frontmatter: append `goodfire-already-clean-2026-10` to `sources:`; `as_of: 2026-10-19`.

`## Current signal` — append bullet:

```
- **Goodfire: "networks are already clean" (2026):** Nick Cammarata argues the superposition evidence that pushed interpretability toward sparse-autoencoder decompositions was misread, that most neurons in modern models have one main job, and that agents acting as automated scientists could map frontier networks directly. He suggests alignment could then proceed through many small, targeted fixes. Single-author essay; companion paper pending. See [Mechanistic interpretability](../concepts/mechanistic-interpretability.md).
```

`## What to watch` — append bullet:

```
- Whether Goodfire's companion paper and outside replications support reading frontier-model neurons directly, or whether superposition holds up at scale
```

`## Related` — append:

```
- [Mechanistic interpretability](../concepts/mechanistic-interpretability.md) — the inside-the-model research line behind several of these safety bets
```

`## Recent changes` — adds one entry at the top:

```
- [2026-10-19] Goodfire's Cammarata argues networks are "already clean": superposition evidence misread, ~90% of Qwen3-32B neurons have one main job, and agent-run interpretability may be tractable soon.
```

`## Sources` — append:

```
- [Neural Networks Are Already Clean — Nick Cammarata (Goodfire)](../sources/articles/goodfire-already-clean-2026-10.md)
```

### wiki/concepts/model-internal-workspace.md (updated)

New section, inserted before `## Sources`:

```
## Related

- [Mechanistic interpretability](mechanistic-interpretability.md) — the broader field of reading model internals, including the superposition debate
```

### wiki/index.md (updated)

Under `## Concepts`, in alphabetical position:

```
- [concepts/mechanistic-interpretability](concepts/mechanistic-interpretability.md) — reading neural networks from the inside; superposition vs "networks are already clean" (Goodfire) debate *(as_of: 2026-10-19)*
```

Set `as_of: 2026-10-19` on the `trends/agent-safety-and-alignment-research` line. Page count: `- concepts: 28` → `- concepts: 29`.

### wiki/sources/articles/goodfire-already-clean-2026-10.md (new)

```
---
title: 'Neural Networks Are Already Clean — Nick Cammarata (Goodfire)'
type: source
source_type: article
source_file: raw/articles/2026-10-19-already-cleangoodfirecom.md
url: https://already-clean.goodfire.com/
ingested: 2026-10-19
domains: [models]
---

# Neural Networks Are Already Clean — Nick Cammarata (Goodfire)

Long interactive essay (~40K words with appendices), Goodfire, 2026; the page gives the year only. The author co-wrote Zoom In, Multimodal Neurons and OpenAI's 2023 automated-interpretability project, so he is revisiting his own earlier evidence.

## The problem
To check what an AI model is doing, interpretability researchers try to read its parts. Neurons that seemed to respond to unrelated things ("polysemantic" neurons) made that look hopeless. The accepted explanation, **superposition**, said networks short on room pack unrelated concepts together because they rarely collide. If so, you can't read neurons directly. You first train a second model (a sparse autoencoder, or "dictionary") to unpack them, and study that instead.

## The claim
Most of that apparent mixing is **recursive generalization**: a neuron groups related things and then sprouts related offshoots, like a branch growing twigs. Example: a neuron detecting "iy" grew to "diy", then "do it yourself". Under this view the extra activations are leads, not noise, and the network can be studied as it is.

## Four-step argument (author's own)
1. Networks use one learning principle (generalization), not two, so ordinary science on them can start now.
2. With modern models and tools, that science goes much better than expected.
3. Understanding compounds like a crossword: each explained neuron constrains its neighbours, so the map fills in faster as it goes.
4. Highly speculative: this might be most of what interpretability needs, possibly soon.

## Evidence highlights
- **Cat-and-car neuron (InceptionV1 4e:55)** is a V-shape detector: its inputs and readers include pointed snouts, flames and fireboat jets, and its negative side responds to round O shapes.
- The canonical superposition circuit from Zoom In (a car feature spreading into dog neurons) has no downstream reader. He reads it as ordinary generalization, not hidden storage.
- InceptionV1's messy last layer was an architecture problem. With modern architecture fixes (no change to size or data), 99–100% of last-layer neurons are readable, at every scale across a 300× size range. Smaller models get coarser neurons, not mixed ones.
- Language models: preliminary Qwen3-32B audits find ~90% of neuron poles with one main job, ~7% with two related jobs, and ~2–4% not understood. Thresholds matter, and dense and MoE models look similar. A GPT-2 XL re-audit puts ~70% at roughly one thing, against <2% in 2023.
- SAEs on ConvNeXt: 88% of last-layer SAE activity is near-copies of single neurons. Removing the non-matching directions leaves accuracy unchanged, and what the SAE adds is loose groupings of existing neurons.
- First published attribution graph of a multi-trillion-parameter model (Kimi K3) using only neurons.
- Why the field missed it: 2023 explainer models couldn't run conjecture-and-test loops, metrics rewarded simulating activations over being right, nobody knew which language-neuron patterns to expect, and most studies used small models.

## What a solution might look like
A lab of automated scientist agents watching the network through training and inference, following a "mechanistic constitution": label neurons, find motifs, test explanations at many scales. Alignment might then proceed through many simple, targeted fixes, such as removing a toxic RL environment. Deception, he argues, can't hide from the model's own circuitry; the risk is failing to read what is in plain sight.

## Limits
- Single author; the companion paper with language-model detail is forthcoming
- Headline percentages depend on author-chosen thresholds and small audited samples
- Contradicts the field's dominant decomposition program; independent replication pending
- Step 4 is explicitly speculative

## Influenced pages
- [Mechanistic interpretability](../../concepts/mechanistic-interpretability.md) — new concept page
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — current-signal and watch bullets
- [Model internal workspace](../../concepts/model-internal-workspace.md) — Related link

## Key claims extracted
- Superposition was the wrong explanation for InceptionV1; the polysemantic examples in the vision literature were misread
- Recursive generalization explains most remaining apparent polysemanticity
- Qwen3-32B: ~90% one job / ~7% two related / ~2–4% unexplained (preliminary)
- SAE activity on ConvNeXt is 88% near-copies of single neurons
- Bigger models learn narrower, easier-to-recognize neurons
- Agents at scale can map vision models; language models "so far" similar up to trillions of parameters
```

## Schema / vocabulary additions
None.

## Open questions
- Should the concept page carry a short history (Distill circuits era → Anthropic dictionary learning → this challenge) once a second source on the SAE side is ingested? (Assumed: not from this source alone.)
	- No, we are trying to keep track of the edge of this tech, not its archive.
