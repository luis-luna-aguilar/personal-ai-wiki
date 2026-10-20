---
type: proposal
source: raw/newsletters/2026-09-22-ainews-xiaomi-mimo-v26-pro-1t-a42b-the-new-top.md
sources:
  - raw/newsletters/2026-09-22-ainews-xiaomi-mimo-v26-pro-1t-a42b-the-new-top.md
  - raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Xiaomi MiMo-V2.6-Pro (1T-A42B, MIT, open RL environments)

## Summary

### In short
Open RL environments, not just open weights, are becoming the thing open labs compete on: Xiaomi shipped MiMo-V2.6-Pro, a 1T-total / 42B-active omnimodal model under MIT, together with its technical report, training code and the RL environments behind it, after an RL run reported at about $2.6M. Artificial Analysis scores it 46, at $0.13 per index task. The proposal creates a MiMo model page, adds it to the open-weight section of State of Models, and updates the open-weight trend and RL harness quality pages. Reason to hesitate: the "top open-weights model" headline uses an Artificial Analysis scale the wiki's older scores may not share.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Xiaomi, the Chinese phone maker that is not usually counted among China's leading AI labs, released the MiMo-V2.6 series around 21 September 2026: MiMo-V2.6-Pro, its most capable model, MiMo-V2.6-Flash, a cheaper balanced tier, and a Pro-UltraSpeed variant that Xiaomi says produces output up to 20 times faster at the same quality. Both models are "natively omnimodal", meaning one model takes in text, images, audio and video, and both ship with weights under the permissive MIT license. AINews' 22 September issue led with it. Artificial Analysis, the independent benchmarking firm, put Pro at the top of open-weight models on its Intelligence Index with a score of 46, at $0.435 per million input tokens and $0.87 per million output.

Most of the attention went to post-training. Fuli Luo, a former DeepSeek engineer now at Xiaomi, published the final reinforcement-learning (RL) runs live; RL means letting the model attempt tasks in training environments and rewarding success. Xiaomi scaled RL through bigger batches, a broader task mix across several harnesses, and more grading compute. One commentator put the run at 130 hours and about $2.6M. Xiaomi is open-sourcing the environment code and plans about 7,000 environments, though the task datasets are not out yet, and commentators argued open RL environments may now matter as much as open pretraining data did.

AINews' 25 September issue added the caveats: the RL gains reportedly do not carry over to harder math evals, users report the model overthinking, and its $0.13 per index task compares with $1.99 for GPT-5.6 Sol, which scores 47. Xiaomi also said MiMo-V3 will move to a new sparse-attention design, HySparse2, aimed at smaller key-value caches and cheaper processing of long prompts.

### What changes
The wiki has no MiMo page. Its open-weight section lists DeepSeek V4, whose Flash 0731 update scored 50 on the Artificial Analysis index in August, and the open-weight trend page stops at 1 September.

- New page `models/mimo-v2-6.md` covering Pro, Flash and UltraSpeed, the RL story, pricing and the caveats.
- **State of Models** gains a MiMo-V2.6 line under Open-weight models and a Recent-changes entry dated 22 September. The list is at its cap of 10, so the oldest entry (Grok 4.6, 13 August) moves to history. The page date stays at 20 October.
- **Open-weight momentum broadens** gains a bullet on MiMo and open RL environments, and a Recent-changes entry; the oldest entry (Kimi K3 deployment economics, 29 July) moves to history. Page date moves to 25 September.
- **RL harness quality** gains a bullet on open-sourced RL environments, including Xiaomi's agents-in-the-loop anti-cheating environment factory. Page date moves to 22 September.
- Two source pages, one per AINews issue.

### What to weigh
The "top open-weights model" claim is Artificial Analysis's, but the wiki's older index numbers look like a different scale: GPT-5.6 Sol is 47 in this source and 59 on the wiki's Sol line, so MiMo's 46 and DeepSeek V4-Flash 0731's 50 should not be compared directly. The drafts state the score without crowning MiMo as the open-weight leader. Flash and UltraSpeed get only a mention, because the source gives no numbers for them.

## Intended changes

- [ ] **Create** `wiki/models/mimo-v2-6.md` — new model page; index entry under Models: `- [models/mimo-v2-6](models/mimo-v2-6.md) — Xiaomi's 1T/42B-active omnimodal open-weight model (MIT); AA Intelligence Index 46 at $0.13/task; RL environments and training code open-sourced *(as_of: 2026-09-25)*`

- [ ] **Update** `wiki/state-of/models.md` — add one leader line under `### Open-weight models` (after DeepSeek V4); add one Recent-changes entry dated 2026-09-22 (live list has 10, cap 10); append source ids to frontmatter `sources:`; `as_of` stays 2026-10-20
    > See draft below

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — the oldest Recent-changes entry (expected: [2026-08-13] Grok 4.6) moves to history

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — add one bullet at the end of `### New entrants broaden the geography and scope` (before the Unsloth bullet); add one Recent-changes entry dated 2026-09-22 (live list has 10); append source ids and links; `as_of` 2026-09-01 → 2026-09-25
    > See draft below

- [ ] **Spill** `wiki/trends/open-weight-momentum-broadens.md` → `wiki/history/trends/open-weight-momentum-broadens.md` — the oldest Recent-changes entry (expected: [2026-07-29] Kimi K3 deployment economics) moves to history

- [ ] **Update** `wiki/concepts/rl-harness-quality.md` — add one bullet after the Miles bullet; add one Recent-changes entry dated 2026-09-22 (live list has 2); append source id and link; `as_of` 2026-09-09 → 2026-09-22
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-xiaomi-mimo-v26-pro-2026-09-22.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/ainews-mimo-aa-comparison-hysparse2-2026-09-25.md` — source summary (story-specific page for the 25 September issue)

## Page drafts

### wiki/models/mimo-v2-6.md (new)

```
---
title: Xiaomi MiMo-V2.6
type: model
domains: [models]
subcategory: open-weight-model
tags: [open-weights, multimodal]
as_of: 2026-09-25
sources: [ainews-xiaomi-mimo-v26-pro-2026-09-22, ainews-mimo-aa-comparison-hysparse2-2026-09-25]
---

# Xiaomi MiMo-V2.6

Xiaomi's open-weight model series, released around 2026-09-21: MiMo-V2.6-Pro (most capable), MiMo-V2.6-Flash (cost/efficiency tier) and Pro-UltraSpeed (Xiaomi claims up to 20x faster output at the same quality). Both models are natively omnimodal (one model for text, image, audio and video input) and ship under the MIT license with a technical report, training code and the RL environments used to post-train them.

## Current status (as of 2026-09-25)

- **Pro:** 1.02T total / 42B active parameters, 1M context; Artificial Analysis Intelligence Index 46 (GPT-5.6 Sol 47 on the same scale); $0.435 / $0.87 per 1M input/output tokens, about $0.13 per index task vs $1.99 for Sol
- **RL at scale, cheaply:** RL compute scaled along three axes (1,568 samples per update with up to 1M context; a multi-task mix across coding, agents, vision and cyber in several harnesses; more grader compute). One commentator puts the final RL run at 130 hours, 75B tokens and about $2.6M on JAX/TPU
- **Open RL environments:** environment code and recipes released for coding, cyber vulnerability reproduction, knowledge work, web development and music; about 7K environments planned, but the full task datasets are not yet out
- **Next:** MiMo-V3 will move to HySparse2, a sparse-attention design that cuts key-value cache size and long-prompt processing cost (tested on an 80B model so far)

## Why it matters

The release makes the post-training recipe, not only the weights, public. Commentators read it as a sign that open RL environments may become as strategic as open pretraining corpora were, and that RL is a cheaper route to frontier-adjacent scores than assumed. See [RL harness quality](../concepts/rl-harness-quality.md) and [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md).

## Weaknesses / caveats

- RL gains reportedly do not generalize to harder math evals
- Users report overthinking (long reasoning on simple prompts); a system-prompt mitigation circulates
- The Artificial Analysis score is on the index as of September 2026; older scores elsewhere in the wiki may sit on a different scale

## Recent changes

- [2026-09-25] Artificial Analysis cost comparison ($0.13 vs $1.99 per task against GPT-5.6 Sol); math-generalization and overthinking caveats; MiMo-V3 to use HySparse2.
- [2026-09-22] MiMo-V2.6-Pro, -Flash and Pro-UltraSpeed released under MIT with technical report, training code and RL environments; AA Intelligence Index 46 for Pro.

## Sources

- [AINews — Xiaomi MiMo-V2.6-Pro 1T-A42B](../sources/newsletters/ainews-xiaomi-mimo-v26-pro-2026-09-22.md)
- [AINews — MiMo-V2.6-Pro cost comparison and HySparse2](../sources/newsletters/ainews-mimo-aa-comparison-hysparse2-2026-09-25.md)
```

### wiki/state-of/models.md (updated)

Frontmatter `sources:` — append two ids to the live list:

```
ainews-xiaomi-mimo-v26-pro-2026-09-22, ainews-mimo-aa-comparison-hysparse2-2026-09-25
```

Under `### Open-weight models`, insert after the DeepSeek V4 line:

```
- [Xiaomi MiMo-V2.6](../models/mimo-v2-6.md) — Xiaomi; 1T/42B-active omnimodal MoE, MIT; AA Intelligence Index 46 at about $0.13 per task; RL environments and training code open-sourced *(as of 2026-09-25)*
```

`## Recent changes` — insert one entry in date order (below the 2026-10-19 entries, above the 2026-09-03 entries):

```
- [2026-09-22] Xiaomi MiMo-V2.6-Pro added to Open-weight models: 1T/42B-active omnimodal MoE under MIT, AA Intelligence Index 46 at $0.13 per task, shipped with its RL environments and training code.
```

Then spill the oldest entry to history (see below). Resulting list keeps 10 entries.

### wiki/history/state-of/models.md (updated)

Append at the end of the file:

```

## Archived from current page on <apply date>

- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

(If an archive block for the apply date already exists at the end of the file, append the entry to it instead of opening a new header. The entry spilled is whichever is oldest at apply time.)

### wiki/trends/open-weight-momentum-broadens.md (updated)

Frontmatter: `as_of: 2026-09-25`; append to `sources:`:

```
ainews-xiaomi-mimo-v26-pro-2026-09-22, ainews-mimo-aa-comparison-hysparse2-2026-09-25
```

Under `### New entrants broaden the geography and scope`, insert before the Unsloth Desktop bullet:

```
- **Xiaomi MiMo-V2.6-Pro (September 2026)** brought a lab outside China's usual leading group into the top tier: a 1T/42B-active omnimodal model under MIT, Artificial Analysis Intelligence Index 46 at about $0.13 per task. It shipped with its RL environments and training code, and commentators argued open RL environments may now matter as much as open pretraining data did. See [Xiaomi MiMo-V2.6](../models/mimo-v2-6.md).
```

`## Recent changes` — insert at the top (newest first):

```
- [2026-09-22] Xiaomi MiMo-V2.6-Pro released under MIT with RL environments and training code; AA Intelligence Index 46 at $0.13 per task; final RL run reported at about $2.6M.
```

Then spill the oldest entry (see below).

`## Sources` — append:

```
- [AINews — Xiaomi MiMo-V2.6-Pro 1T-A42B](../sources/newsletters/ainews-xiaomi-mimo-v26-pro-2026-09-22.md)
- [AINews — MiMo-V2.6-Pro cost comparison and HySparse2](../sources/newsletters/ainews-mimo-aa-comparison-hysparse2-2026-09-25.md)
```

### wiki/history/trends/open-weight-momentum-broadens.md (updated)

Append at the end of the file:

```

## Archived from current page on <apply date>

- [2026-07-29] Kimi K3 deployment economics documented: ~8×MI355X minimum to load, 64+ GPUs for production serving, six-figure entry cost; Composio's cross-harness comparison shows the same model performs similarly but at very different cost/speed depending on the agent harness used (Kimi Code, Hermes, Claude Code).
```

### wiki/concepts/rl-harness-quality.md (updated)

Frontmatter: `as_of: 2026-09-22`; append `ainews-xiaomi-mimo-v26-pro-2026-09-22` to `sources:`.

In `## Current status`, insert after the Miles bullet:

```
- **Open RL environments.** Xiaomi released the RL environments and recipes behind [MiMo-V2.6](../models/mimo-v2-6.md) (coding, cyber vulnerability reproduction, knowledge work, web development, music), with about 7K environments planned; its environment-factory paper generates tasks from open repositories with agents in the loop to check robustness and block cheating. Commentators argue environment quality is becoming the strategic asset that pretraining data was.
```

`## Recent changes` — insert at the top:

```
- [2026-09-22] Added open RL environments: Xiaomi open-sourced the environments behind MiMo-V2.6, including an agents-in-the-loop anti-cheating task factory.
```

`## Sources` — append:

```
- [AINews — Xiaomi MiMo-V2.6-Pro 1T-A42B](../sources/newsletters/ainews-xiaomi-mimo-v26-pro-2026-09-22.md)
```

### wiki/sources/newsletters/ainews-xiaomi-mimo-v26-pro-2026-09-22.md (new)

```
---
title: '[AINews] Xiaomi MiMo-V2.6-Pro 1T-A42B: the new top Open Weights model, trained for $3M'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-22-ainews-xiaomi-mimo-v26-pro-1t-a42b-the-new-top.md
url: https://www.latent.space/p/ainews-xiaomi-mimo-v26-pro-1t-a42b
published: 2026-09-22
ingested: 2026-10-20
domains: [models]
---

# AINews — Xiaomi MiMo-V2.6-Pro 1T-A42B

AINews' lead story for 19–21 September 2026: Xiaomi released MiMo-V2.6-Pro and -Flash, natively omnimodal open-weight models under MIT, with a technical report, training code and RL environments, plus a Pro-UltraSpeed variant. Artificial Analysis placed Pro at the top of open-weight models on its Intelligence Index. Commentary focused on the RL stack: live-published final RL runs, three-axis RL scaling, a cheap RL run, and the argument that open RL environments are now strategic.

## Influenced pages

- [Xiaomi MiMo-V2.6](../../models/mimo-v2-6.md) — new page
- [State of Models](../../state-of/models.md) — Open-weight models leader line
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new-entrant bullet
- [RL harness quality](../../concepts/rl-harness-quality.md) — open RL environments

## Key claims extracted

- MiMo-V2.6-Pro: 1.02T total / 42B active, natively omnimodal, MIT license; AA Intelligence Index 46 (top open-weights model per AA); $0.435 / $0.87 per 1M input/output tokens
- Pro-UltraSpeed: up to 20x faster output at the same quality (Xiaomi)
- RL scaled on three axes: 1,568 samples per update, up to 1M context, 3.5–3.7B tokens per step; multi-task suite across coding, agents, visual and cyber in several harnesses; more grader compute
- Final RL run: 130 hours, 75B tokens, about $2.6M (@zephyr_z9); JAX + TPU
- Environment code and recipes open-sourced; ~7K environments planned, full task datasets not yet released
- Environment/data-factory paper generates RL tasks from open repositories with agents in the loop for robustness and anti-cheating
```

### wiki/sources/newsletters/ainews-mimo-aa-comparison-hysparse2-2026-09-25.md (new)

```
---
title: 'AINews — MiMo-V2.6-Pro cost comparison and HySparse2 (The Future of Latent Space issue)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
url: https://www.latent.space/p/ainews-the-future-of-latent-space
published: 2026-09-25
ingested: 2026-10-20
domains: [models]
---

# AINews — MiMo-V2.6-Pro cost comparison and HySparse2

Story-specific page for the MiMo items in AINews' 25 September 2026 issue: an Artificial Analysis cost comparison against GPT-5.6 Sol, a caveat that MiMo's RL gains do not reach harder math, user reports of overthinking, and Xiaomi's announcement that MiMo-V3 will use the HySparse2 sparse-attention architecture.

## Influenced pages

- [Xiaomi MiMo-V2.6](../../models/mimo-v2-6.md) — cost comparison, caveats, MiMo-V3 architecture
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — per-task cost
- [State of Models](../../state-of/models.md) — per-task cost on the leader line

## Key claims extracted

- MiMo-V2.6-Pro: MIT, omnimodal, 1M context, AA index 46 vs GPT-5.6 Sol 47; $0.13 vs $1.99 per task
- RL gains do not generalize to harder math evals (@teortaxesTex)
- Users report MiMo 2.6 Pro overthinking; a system-prompt mitigation post circulates
- MiMo-V3 will adopt HySparse2 (arXiv:2609.26368): lower prefill FLOPs, smaller KV cache, better long-context retrieval; tested on an 80B model
```

## Schema / vocabulary additions

None.

## Open questions

- Should MiMo-V2.6 stay a challenger line under Open-weight models (as drafted), or should the section name a single open-weight leader once Artificial Analysis's current scores for DeepSeek V4-Flash and the other entries are re-checked on the same scale?
