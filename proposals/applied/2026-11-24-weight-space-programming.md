---
type: proposal
source: raw/articles/2026-11-24-rikiyatgithubio-blog-weight-space-programming.md
sources:
  - raw/articles/2026-11-24-rikiyatgithubio-blog-weight-space-programming.md
  - raw/articles/2026-11-24-cmpndai-blog-weight-space-programming-dspyhtml.md
  - raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md
status: pending
created: 2026-11-24
---

# Proposal: Weight-space programming — frontier models edit small models' weights directly

## Summary

### In short
A frontier model can now improve a small model by reading and rewriting its weights directly, with no training run. GPT-6 Astra edited 0.016% of Qwen3.5-0.8B's weights to stop its reasoning loops, raising MATH-500 from 7.9% to 48.1%. Cmpnd's open DSPy optimizer applies the method to small decision models, improving all five it tested for about $5–10 each. The proposal creates a concept page, `concepts/weight-space-programming.md`, adds pointers on **Agent improvement loop** and **Decision models**, and creates two source pages. The reason to hesitate is the new page: the wiki has no concept for this yet.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
By 3 November 2026, Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab (whom Every describes as MIT researchers) had published a blog post called "Sparks of Weight-Space Programming". Its claim is that frontier models can treat a neural network's weights, the millions of numbers that make up a trained model, the way a programmer treats code. They can read the weights to work out what the network does, then edit them by reasoning instead of by training. No gradients or training loops were allowed. GPT-6 Astra got the weights, sometimes a Python sandbox, and at most a small budget of test runs.

The results are uneven but striking. From raw weights alone, Astra could tell which game a small network had been trained on. It wrote small game-playing networks from scratch that beat networks trained with PPO, a standard reinforcement-learning method, for 100 million steps. With 50 test runs, its Go network beat an equal-sized one trained on 20 million games. On Qwen3.5-0.8B, a small model that its own model card warns gets stuck in thinking loops, Astra found the cause and fixed it, which also tripled the IFEval score. The limits are stated plainly. Astra could not improve Gemma 3 270M, which rarely loops, because its errors were ordinary reasoning mistakes. It also could not tell a sycophantic model from an honest one by weights alone; it needed to see the attention patterns. The authors say this is a capability, not a method, and that context length and harnesses still hold it back. Within days others had replicated it and built a benchmark, IWIBench.

On 13 November Drew Breunig's company Cmpnd released `dspy-wsp`, an experimental DSPy optimizer built on the idea. A "writer" model inspects and edits a small model's weights over 25 test runs. On five open decision models (0.6B to 9B parameters) it added 1.9 to 16.1 accuracy points, and 6.5 to 20.0 when combined with Cmpnd's ReAnchor threshold optimizer. The edited models run locally, on a Mac or an NVIDIA GPU.

### What changes
The wiki covers improving a model's weights only through training runs, via Palantir's AutoResearch, and records no way to tune a decision model after release.

- New concept page `concepts/weight-space-programming.md` defines the idea and gives the main results, Cmpnd's tool and the stated limits. It is added to the index.
- **Agent improvement loop** gains one sentence in its "Autoresearch over model weights" section contrasting direct weight edits with training runs, plus a Related link and a Recent-changes entry. Page date moves to 13 November.
- **Decision models** gains one current-status bullet on tuning a released decision model with `dspy-wsp`, plus a Related link and a Recent-changes entry. Page date moves to 13 November.
- Two new source pages, one for the research post and one for Cmpnd's release.

### What to weigh
The triage recommended a lightweight ingest; this proposal goes further with a new concept page, because the idea spans model improvement, decision models and interpretability and would not fit on any one existing page. The research post shows no publication date; Simon Willison's replication shows it was public by 3 November, which is the only date the drafts give it. Cmpnd's release date of 13 November comes from Every's "last Friday" in its 15 November issue. The research post (about 9,500 words) was read for its summary, the language-model experiments and the authors' responses, and the small-network experiments were skimmed. Every's framing of "artisanal models" is left out as commentary.

## Intended changes

- [ ] **Create** `wiki/concepts/weight-space-programming.md` — new concept page; add to `wiki/index.md` under concepts (concepts count 40 → 41, total 311 → 312)
    > See draft below

- [ ] **Update** `wiki/concepts/agent-improvement-loop.md` — one sentence appended to "Autoresearch over model weights"; one Related line; adds one Recent-changes entry dated 2026-11-13 (list goes to 9 of 10, no spill); append `weight-space-programming-takehi-2026-11` and `cmpnd-dspy-wsp-2026-11-13` to frontmatter `sources:` and two lines to `## Sources`; `as_of` and Current-status stamp 2026-10-24 → 2026-11-13
    > See draft below

- [ ] **Update** `wiki/concepts/decision-models.md` — one new Current-status bullet; one Related line; adds one Recent-changes entry dated 2026-11-13 (list goes from 3 to 4, no spill); append `cmpnd-dspy-wsp-2026-11-13` to frontmatter `sources:` and one line to `## Sources`; `as_of` and Current-status stamp 2026-11-08 → 2026-11-13
    > See draft below

- [ ] **Create** `wiki/sources/articles/weight-space-programming-takehi-2026-11.md` — source summary for the research post

- [ ] **Create** `wiki/sources/articles/cmpnd-dspy-wsp-2026-11-13.md` — source summary for Cmpnd's release

## Page drafts

### wiki/concepts/weight-space-programming.md (new)

```
---
title: Weight-space programming
type: concept
domains: [models, agents]
tags: []
as_of: 2026-11-13
sources: [weight-space-programming-takehi-2026-11, cmpnd-dspy-wsp-2026-11-13]
---

# Weight-space programming

Weight-space programming treats a neural network's weights like a program: a frontier model reads them to work out what the network computes, then edits them directly to change it, by reasoning instead of by training. The term comes from a research post by Takehi, Teoh, Zhang and Khattab (public by 3 November 2026), who stress that it names an emerging model capability, not a method.

## Current status (as of 2026-11-13)
- **Reading.** From raw weights alone, GPT-6 Astra told which game a small network was trained on. It could not tell a sycophantic Gemma 3 270M from an honest one by weights alone, but did once shown attention patterns.
- **Fixing.** With no gradients and 10–50 test runs, Astra edited 0.016% of Qwen3.5-0.8B's weights to remove a known thinking-loop fault: MATH-500 rose from 7.9% to 48.1% and IFEval roughly tripled. It could not improve Gemma 3 270M, whose errors were ordinary reasoning mistakes rather than one faulty component.
- **Writing.** Astra wrote small game-playing networks from scratch that beat PPO trained for 100M steps; with 50 test runs, its 1.5M-parameter Go network beat an equal-sized one trained on 20M games.
- **Tooling.** Cmpnd's experimental [`dspy-wsp`](https://github.com/cmpnd-ai/dspy-wsp) DSPy optimizer applies it to small [decision models](decision-models.md): 25 test runs of GPT-6 Astra (about $5–10) added 1.9–16.1 accuracy points on five open models from 0.6B to 9B, and the edited model runs locally (Mac via MLX, or PyTorch/vLLM on NVIDIA).
- **Uptake.** Within days the post was replicated (Simon Willison, Hugging Face) and extended to robot policies and quantum circuits, and a benchmark (IWIBench) appeared; the authors are building their own benchmark and harness.

## Why it matters
Until now the wiki's model-improvement loops change weights only through training runs ([Agent improvement loop](agent-improvement-loop.md), Palantir AutoResearch). Direct edits touch a tiny share of weights, so in principle they avoid the forgetting that fine-tuning causes and need no dataset. The authors also see it as a new route for auditing models from their weights and for [mechanistic interpretability](mechanistic-interpretability.md).

## Caveats
- Results are on small models (under 1B parameters for language models); the authors say context length and harnesses limit it today.
- Fixing a known fault is not the same as adding skill: the large Qwen gain came from removing loops, and the non-looping Gemma did not improve.
- Cmpnd calls `dspy-wsp` very experimental; runs on text-generating LLMs are long, costly and may not help.

## Recent changes
- [2026-11-13] Page created: the weight-space programming research post (public by 3 November) and Cmpnd's `dspy-wsp` optimizer for decision models.

## Related
- [Agent improvement loop](agent-improvement-loop.md) — model improvement through training runs, which this skips
- [Decision models](decision-models.md) — the small models `dspy-wsp` targets
- [Mechanistic interpretability](mechanistic-interpretability.md) — reading networks from the inside with purpose-built tools

## Sources
- [Sparks of Weight-Space Programming — Takehi, Teoh, Zhang, Khattab](../sources/articles/weight-space-programming-takehi-2026-11.md)
- [Cmpnd — Weight-Space Programming with DSPy](../sources/articles/cmpnd-dspy-wsp-2026-11-13.md)
```

Index line (under concepts, after `concepts/agent-improvement-loop` group as alphabetical/position allows):

```
- [concepts/weight-space-programming](concepts/weight-space-programming.md) — frontier models reading and editing a small model's weights directly, without training: Astra's Qwen3.5-0.8B loop fix (MATH-500 7.9%→48.1%) and Cmpnd's dspy-wsp optimizer for decision models *(as_of: 2026-11-13)*
```

Page count: `- concepts: 41` and `**Total content pages: 312.**`

### wiki/concepts/agent-improvement-loop.md (updated)

Frontmatter changes:

```
as_of: 2026-11-13
sources: [trace-agent-improvement-loop, langchain-better-harness, cursor-bugbot-learning, self-improving-skills, agents-evals-deep-research, langchain-interrupt-may-2026, autoresearch-agent-recipes-2026-07, agent-memory-systems-layer-2026-06, ainews-eating-finance-aie-nyc-2026-07-29, palantir-autoresearch-fine-tuning-ontology-2026-10-24, weight-space-programming-takehi-2026-11, cmpnd-dspy-wsp-2026-11-13]
```

Heading change: `## Current status (as of 2026-10-24)` → `## Current status (as of 2026-11-13)`

In `## Autoresearch over model weights`, append at the end of the paragraph (after the HF ml-intern sentence):

```
A newer alternative (November 2026) skips training entirely: in [weight-space programming](weight-space-programming.md), a frontier model reads a small model's weights and edits a few of them directly between short test runs, and Cmpnd's `dspy-wsp` packages this as a DSPy optimizer.
```

In `## Recent changes`, insert above the 2026-10-24 entry:

```
- [2026-11-13] Added weight-space programming to autoresearch over weights: a frontier model edits a small model's weights directly instead of running training.
```

In `## Related`, append:

```
- [Weight-space programming](weight-space-programming.md) — improving a model by editing its weights directly, with no training run
```

In `## Sources`, append:

```
- [Sparks of Weight-Space Programming — Takehi, Teoh, Zhang, Khattab](../sources/articles/weight-space-programming-takehi-2026-11.md)
- [Cmpnd — Weight-Space Programming with DSPy](../sources/articles/cmpnd-dspy-wsp-2026-11-13.md)
```

### wiki/concepts/decision-models.md (updated)

Frontmatter changes:

```
as_of: 2026-11-13
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, jackyk02-clm-contrastive-language-model-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, latent-space-openai-decisions-api-2026-09-30, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17, hume-audio-decision-model-api-2026-11-08, trycua-cua-repo-2026-11, ainews-cua-s1-forms-2026-09-19, cmpnd-dspy-wsp-2026-11-13]
```

Heading change: `## Current status (as of 2026-11-08)` → `## Current status (as of 2026-11-13)`

In `## Current status`, insert after the "Where they fit" bullet:

```
- **Tuning after release.** Cmpnd's experimental `dspy-wsp` optimizer has GPT-6 Astra edit an open decision model's weights directly ([weight-space programming](weight-space-programming.md)) over 25 test runs for about $5–10. On five models from 0.6B to 9B (including d1 and Clef-Flash models) it added 1.9–16.1 accuracy points on 400 held-out cases, and 6.5–20.0 with Cmpnd's ReAnchor threshold refit; the edited model runs locally.
```

In `## Related`, append:

```
- [Weight-space programming](weight-space-programming.md) — tuning an open decision model by editing its weights directly
```

In `## Recent changes`, insert above the 2026-11-08 entry:

```
- [2026-11-13] Cmpnd's `dspy-wsp` added: direct weight edits improved all five open decision models it tested by 1.9–16.1 points for about $5–10 each.
```

In `## Sources`, append:

```
- [Cmpnd — Weight-Space Programming with DSPy](../sources/articles/cmpnd-dspy-wsp-2026-11-13.md)
```

### wiki/sources/articles/weight-space-programming-takehi-2026-11.md (new)

```
---
title: 'Sparks of Weight-Space Programming — Takehi, Teoh, Zhang, Khattab'
type: source
source_type: article
source_file: raw/articles/2026-11-24-rikiyatgithubio-blog-weight-space-programming.md
url: https://rikiyat.github.io/blog/weight-space-programming/
ingested: 2026-11-24
domains: [models]
---

# Sparks of Weight-Space Programming — Takehi, Teoh, Zhang, Khattab

Research blog post by Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab (described by Every as MIT researchers), arguing that frontier LLMs can natively read and write neural network weights. The post shows no publication date; a replication dated 3 November 2026 shows it was public by then, and a "Response to Comments" section was added on 12 November.

## The idea
Treat weights like code: read them to understand what a network computes, edit them to change it. The "programmer" is GPT-6 Astra working from a plain-language request, with no gradients and no training loops; some experiments allow a Python kernel and a small budget of forward passes. The authors call it a capability, not a method.

## Results
- **Read:** identified which game a small network was trained on from its weights; could not identify a sycophantic Gemma 3 270M from weights alone, but did from attention patterns on texts it wrote.
- **Fix:** edited 0.016% of Qwen3.5-0.8B's weights to remove its known thinking-loop fault; MATH-500 7.9% → 48.1%, IFEval about 3×, on held-out benchmarks. Could not improve Gemma 3 270M, which rarely loops.
- **Write:** small MinAtar game networks written from scratch outplayed PPO trained for 100M steps; a 1.5M-parameter Go network beat an equal-sized PPO network trained on 20M games when given 50 forward passes.
- Full logs and the edited Qwen model are public; replications and extensions (robot policies, quantum circuits, IWIBench) followed within days.

## Limits (authors' own)
- Capabilities are "exciting but still limited", mainly by context length and harnesses.
- Baselines test narrow claims, not a method ranking; no comparison with human interpretability researchers.

## Influenced pages
- [Weight-space programming](../../concepts/weight-space-programming.md) — new concept page
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — direct weight edits as an alternative to training runs

## Key claims extracted
- GPT-6 Astra edited 0.016% of Qwen3.5-0.8B's weights; MATH-500 7.9% → 48.1%
- No gradients or training loops were used
- Gemma 3 270M could not be improved; sycophancy not detectable from weights alone
- Weight-space programming is a concept and capability, not a method
```

### wiki/sources/articles/cmpnd-dspy-wsp-2026-11-13.md (new)

```
---
title: Cmpnd — Weight-Space Programming with DSPy
type: source
source_type: article
source_file: raw/articles/2026-11-24-cmpndai-blog-weight-space-programming-dspyhtml.md
url: https://cmpnd.ai/blog/weight-space-programming-dspy.html
published: 2026-11-13
ingested: 2026-11-24
domains: [models, agents]
---

# Cmpnd — Weight-Space Programming with DSPy

Drew Breunig's company Cmpnd releases `dspy-wsp`, a prototype DSPy optimizer that brings weight-space programming to existing DSPy programs. The post has no date; Every's 15 November 2026 newsletter says it was released "last Friday", 13 November.

## What it does
The `WeightSpace` optimizer hands a small model's weights to a "writer" LLM (GPT-6 Astra at maximum reasoning effort in the tests). In turns, the writer runs the program on practice examples, looks at layer activity, edits weights in a sandboxed Python kernel with no GPU, network or gradients, and re-tests. When a fixed budget of forward passes runs out, it keeps the best edit as a patch or full checkpoint. Works with DSPy 3.5; `pip install dspy-wsp`.

## Results
- Five open decision models from 0.6B to 9B, Typed Decisions benchmark, 400 held-out cases, 25 forward passes, about $5–10 per model.
- WeightSpace alone: +1.9 to +16.1 points; with Cmpnd's ReAnchor (refits each question's decision thresholds): +6.5 to +20.0. Examples: d1-omni-600M 50.9% → 69.1%; d1-2B 60.6% → 77.9%; Clef-Flash 68.8% → 75.3%.
- Edited models run locally: MLX on Apple silicon, PyTorch on Linux; 2B models used about 6 GB. A Mac or a GPU with 4 GB can run optimizations on d1-omni-600M.

## Caveats
- "Very experimental", tested in a handful of environments and model families; editing runs on text-generating LLMs are long, costly and may not help.

## Influenced pages
- [Weight-space programming](../../concepts/weight-space-programming.md) — tooling bullet
- [Decision models](../../concepts/decision-models.md) — tuning-after-release bullet
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — named as the packaged tool

## Key claims extracted
- `dspy-wsp` improved every one of five open decision models tested
- Cost about $5–10 of GPT-6 Astra usage per model
- Combines with ReAnchor for +6.5 to +20.0 points
```

## Schema / vocabulary additions

None.

## Open questions

- Should weight-space programming get its own concept page (assumed yes, since it spans optimization, decision models and interpretability), or only a short section on **Agent improvement loop**? That page is already just over its 1,200-word ceiling (101%; about 105% with this proposal's one sentence), so folding the full material in would make it a split candidate.
	- Yes, new concept page
