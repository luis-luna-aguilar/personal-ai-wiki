---
type: proposal
source: raw/newsletters/2026-09-21-jev-system-one-models-for-prod-not-god-with-di.md
sources:
  - raw/newsletters/2026-09-21-jev-system-one-models-for-prod-not-god-with-di.md
  - raw/newsletters/2026-09-23-how-to-get-the-most-out-of-jev.md
  - raw/tweets/2026-09-23-jackyk02-2102905335925424285.md
  - raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
  - raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
  - raw/articles/2026-10-02-cloudflare-clef-decision-models.md
  - raw/newsletters/2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishe.md
  - raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
  - raw/newsletters/2026-10-14-ainews-ai-engineer-nyc-gemini-4-argon-vals-ai.md
  - raw/newsletters/2026-10-17-ainews-high-taste-testers-ep-1.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Decision models become a product category (Jev and its rivals)

## Summary

### In short

A new model class now sits beside chat models: decision models, which return a calibrated probability for a yes/no question, a pick or a score instead of writing text, and are cheap enough to put on every step of a workflow. TypeSafe's Jev launched on 15 September at $0.042 per million input tokens with output free; within a month Cloudflare, OpenAI, Perplexity and Liquid shipped rivals and Artificial Analysis built an index for them. The proposal adds a concept page, a Jev page, a new state-of section and one routing bullet. Reason to hesitate: it needs a new subcategory.

[[#Open questions|Open questions: 2 to answer.]]

### The source

On 15 September TypeSafe, a lab that had spent two years in stealth, released Jev. CEO Diogo Almeida, an InstructGPT co-author, explained it in a long Latent Space interview. Jev does not generate text. You describe a situation and ask one of three kinds of question: a "Noulli" (the probability that something is true), a "Choice" (which of several options applies) or a "Score" (where it sits on a scale). It is trained to give honest probabilities rather than answers human raters like, and TypeSafe publishes no benchmark scores.

Every's how-to added practice: send Jev any call a person could make in under 10 seconds, and break a vague question ("is this email urgent?") into weighted yes/no checks tested against items you have already judged. Independent checks followed. A Jev-as-a-judge paper found it 277 times cheaper than GPT-6 and within 3 points on two judging benchmarks, though 14.5 points behind on JudgeBench. Vals found it matched GPT-6 Astra on claim verification but ranked last on LegalBench. A Reddit baseline using a small embedding model beat it on one standard intent dataset.

Rivals came fast. Cloudflare released open-weight Clef models that accept images and claim better scores at lower latency. OpenAI built its Decisions API on GPT-6 Luna in about a week. Perplexity, Microsoft and Liquid shipped their own. On 14 October Artificial Analysis launched a Decision Index, which Jev led at 58 until Liquid's d1-ultra reached 65 three days later. AA's verdict: these models are good at classification and routing, but weaker and overconfident on knowledge and reasoning.

### What changes

Today the wiki mentions Jev only in passing, as a point of comparison on the ScaleDown and MedDecider pages, and has no page for the category.

- New page `concepts/decision-models.md`: definition and aliases, the October rivals, the three benchmarks, where the class fits, and Every's method. Dated 17 October.
- New page `models/jev.md`, under a new `decision-model` subcategory: pricing, limits, independent results and funding. Dated 17 October.
- **State of Models** gains a "Decision models" section with Jev, Liquid d1-ultra, Clef, pplx-decider and OpenAI's Decisions API. It also gains one Recent-changes entry, and the oldest entry (Grok 4.6, 13 August) moves to history. Page date stays 20 October.
- **Cost-aware AI task routing** gains one evidence bullet on sending yes/no steps to decision models, with a related link. Page date stays 19 October.
- Ten new source pages: the interview, the Every how-to, the CLM thread, Cloudflare's launch post, OpenAI's Decisions API interview, and five AINews issues, one per story.

### What to weigh

The new subcategory is the main call. None of the existing ones fits a general-purpose model that decides rather than generates: `utility-model` covers single-task pipeline models and `domain-specialized-model` covers one profession. Of the twenty raw files in the triage signal, ten feed this proposal. The other ten repeat these claims or add single launches (Command Code Agr, Decision 3.0, vLLM's `/v1/systemone` endpoint, ScaleDown's "Constrained Decoding Models" rebrand), so they stay traced through the triage file only. The routing page ends at about 108% of its length ceiling, under the 110% warning line.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/concepts/decision-models.md` — category page
- [ ] **Create** `wiki/models/jev.md` — model page (subcategory `decision-model`)
- [ ] **Update** `wiki/state-of/models.md` — new "Decision models" subsection after "Domain-specialized models"; appends eight source ids to frontmatter `sources:`; adds one Recent-changes entry dated 2026-10-17 (inserted after the 2026-10-19 entries); list goes from 10 to 11, so the oldest entry spills
- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — the oldest Recent-changes entry ([2026-08-13] Grok 4.6) appended under the existing "Archived from current page on 2026-10-20" block
- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — one bullet appended to "Routing as infrastructure"; one Related line; three Sources links and three frontmatter ids appended; one Recent-changes entry dated 2026-10-17 (list 5 → 6, no spill); `as_of` 2026-10-19 stays (newer)
- [ ] **Create** `wiki/sources/newsletters/latent-space-jev-diogo-almeida-2026-09-21.md`
- [ ] **Create** `wiki/sources/newsletters/every-how-to-get-most-out-of-jev-2026-09-23.md`
- [ ] **Create** `wiki/sources/tweets/jackyk02-clm-contrastive-language-model-2026-09-23.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-jev-judge-clm-critique-2026-09-25.md`
- [ ] **Create** `wiki/sources/newsletters/latent-space-openai-decisions-api-2026-09-30.md`
- [ ] **Create** `wiki/sources/articles/cloudflare-clef-decision-models-2026-10-02.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-decisions-api-beta-vals-jev-2026-10-07.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-decision-models-product-category-2026-10-10.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-aa-decision-index-2026-10-14.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-liquid-d1-ultra-pplx-decider-2026-10-17.md`

## Page drafts

### wiki/concepts/decision-models.md (new)

```
---
title: Decision models
type: concept
domains: [models, agents]
subcategory: decision-model
tags: []
as_of: 2026-10-17
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, jackyk02-clm-contrastive-language-model-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, latent-space-openai-decisions-api-2026-09-30, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17]
---

# Decision models

Models that answer a typed question about a given input in one pass, without generating text: the probability that a statement is true, a pick from a fixed set of options, or a position on a scale. Because nothing is decoded token by token, many questions run in parallel within milliseconds and output is usually free. Code then branches, routes, sorts or thresholds on the result.

## Also called

System One models (TypeSafe's term), Constrained Decoding Models (ScaleDown), Decisions API (OpenAI); critics call them zero-shot classifiers.

## Current status (as of 2026-10-17)

- **Category formed in a month.** [Jev](../models/jev.md) launched on 2026-09-15; about 100 API clones followed within two weeks. By mid-October the field included Cloudflare's open-weight Clef and Clef-flash (2 October), OpenAI's Decisions API on GPT-6 Luna (public beta, $0.10/M input, no output charge), Perplexity's open pplx-decider (v1.1 27B, then v1.2 in 27B and 4B), Microsoft-Decision-1, Liquid d1 and vLLM Semantic Router's Decision 2.0. Unsloth published a notebook that turns Qwen3.5-4B into one on 8GB of VRAM.
- **Common build.** A frozen LLM backbone reads the input once (prefill only) and a small trained head scores each valid option. Cloudflare's Clef uses Qwen3.8-27B with a Brier-loss calibration step. CLM swaps the head for a contrastive pair of state and action encoders, so a fixed action set can be cached.
- **Benchmarks.** There are three competing indices: Cloudflare's "Jev Decision Index", Hugging Face's Decision Index v0.3 and Artificial Analysis's Decision Index (14 October). On AA's index, Liquid d1-ultra leads at 65 against Jev 1.14's 57. Claude Haiku 5.5 at low effort scores 61, but costs $184 against Jev's $42 per million tasks and takes 1.4 s against 0.13 s per task.
- **Where they fit.** Routing, approval gates, judging traces, tool selection, reranking, and real-time interfaces where an LLM's one-to-two-second turn breaks the feel. AA finds them competitive on classification and routing, but weaker and often overconfident on knowledge and reasoning. CLM's authors say Jev fails as a verifier on long-horizon coding tasks.
- **Skeptic view.** Critics call it standard zero-shot classification with better marketing. A small embedding model plus logistic regression beat Jev on Banking77 (93.3% vs 83.2%). The fair baseline is classifiers and rerankers, not LLMs emitting JSON.

## How to use one

Every's rule: if a person could make the call in under 10 seconds, send it to a decision model; slower calls go to an LLM. Break a fuzzy question ("is this urgent?") into separate yes/no checks ("did a person write it?", "is someone waiting on me?", "does ignoring it cost me?"), weight them in code, and test them on a sample you have already judged before running the full set. Almeida gives the same advice for production systems: ask many small independent questions rather than one compound instruction.

## Related

- [Jev](../models/jev.md) — the reference model the category formed around
- [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) — where decision models fit in a routing cascade
- [MedDecider-27B](../models/meddecider-27b.md) — a medical decision model, filed as domain-specialized
- [ScaleDown](../models/scaledown.md) — single-task classify/extract models with a Jev-compatible Decisions API

## Recent changes

- [2026-10-17] Page created: the category from Jev's launch (2026-09-15) to Artificial Analysis's Decision Index and Liquid d1-ultra taking its top spot.

## Sources

- [Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)](../sources/newsletters/latent-space-jev-diogo-almeida-2026-09-21.md)
- [Every — How to Get the Most Out of Jev](../sources/newsletters/every-how-to-get-most-out-of-jev-2026-09-23.md)
- [Jacky Kwok — Introducing Contrastive Language Model (CLM)](../sources/tweets/jackyk02-clm-contrastive-language-model-2026-09-23.md)
- [AINews — Jev as a judge, CLM, and the classifier critique](../sources/newsletters/ainews-jev-judge-clm-critique-2026-09-25.md)
- [Latent Space — How OpenAI shipped its Decisions API](../sources/newsletters/latent-space-openai-decisions-api-2026-09-30.md)
- [Cloudflare — Introducing Clef decision models](../sources/articles/cloudflare-clef-decision-models-2026-10-02.md)
- [AINews — Decisions API beta, pplx-decider, and Vals on Jev](../sources/newsletters/ainews-decisions-api-beta-vals-jev-2026-10-07.md)
- [AINews — Decision models become a product category](../sources/newsletters/ainews-decision-models-product-category-2026-10-10.md)
- [AINews — Artificial Analysis launches a Decision Index](../sources/newsletters/ainews-aa-decision-index-2026-10-14.md)
- [AINews — Liquid d1-ultra tops the Decision Index; pplx-decider v1.2](../sources/newsletters/ainews-liquid-d1-ultra-pplx-decider-2026-10-17.md)
```

### wiki/models/jev.md (new)

```
---
title: Jev
type: model
domains: [models]
subcategory: decision-model
tags: [closed-source]
as_of: 2026-10-17
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17]
---

# Jev

TypeSafe's API-only decision model, released 2026-09-15 and marketed as a "System One" model. Jev answers questions about text or structured input instead of generating text. A Noulli question returns the probability that a statement is true, a Choice question returns probabilities over a set of options, and a Score question places the input on a scale. TypeSafe CEO Diogo Almeida, a co-author of InstructGPT, maps them to an if statement, a switch statement and a sort. It is the reference point for the [decision models](../concepts/decision-models.md) category.

## Current status (as of 2026-10-17)

- Price: $0.042 per 1M input tokens, output free. Text and structured data only, no images; 32K context per Cloudflare's comparison.
- Trained with RLCD (reinforcement learning for calibrated decisions), an unpublished method that rewards honest probabilities rather than rater-preferred answers.
- TypeSafe publishes no benchmark scores, never refuses a request, and freezes each version once it ships (current versions 1.13 and 1.14).
- Artificial Analysis Decision Index: Jev 1.13 led at 58 at launch (2026-10-14); Liquid d1-ultra now leads at 65, with Jev 1.14 at 57.
- AINews reports TypeSafe passed $100M ARR at a $7.5B valuation three weeks after launch.

## Independent results

- Jev-as-a-judge paper: $0.044 per 1K judgments at 152 ms median, about 277x cheaper than GPT-6. Within 3 points on RewardBench and HaluEval, 14.5 points behind on JudgeBench. Escalating only low-confidence calls to GPT-6 Astra keeps 99% of accuracy at 57% of the cost.
- Vals: matched GPT-6 Astra's 97.5% on claim verification at about 1/500th the cost; ranked last on LegalBench.
- Cloudflare's own table: Jev leads Clef on When2Call and BRIGHT but trails on most other rows, at 524 ms median latency against Clef's 209 ms.
- A small-embedding-plus-logistic-regression baseline beat it on Banking77 (93.3% vs 83.2%).

## Weaknesses / caveats

- No public benchmarks from TypeSafe, so comparisons come from rivals and third parties that use different indices.
- Weaker and overconfident on knowledge and reasoning questions, per Artificial Analysis.
- No image input; Clef, OpenAI's Decisions API and Liquid d1 accept images.

## Recent changes

- [2026-10-17] Page created: launch (2026-09-15), pricing, independent results, and its fall to second on Artificial Analysis's Decision Index.

## Sources

- [Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)](../sources/newsletters/latent-space-jev-diogo-almeida-2026-09-21.md)
- [Every — How to Get the Most Out of Jev](../sources/newsletters/every-how-to-get-most-out-of-jev-2026-09-23.md)
- [AINews — Jev as a judge, CLM, and the classifier critique](../sources/newsletters/ainews-jev-judge-clm-critique-2026-09-25.md)
- [Cloudflare — Introducing Clef decision models](../sources/articles/cloudflare-clef-decision-models-2026-10-02.md)
- [AINews — Decisions API beta, pplx-decider, and Vals on Jev](../sources/newsletters/ainews-decisions-api-beta-vals-jev-2026-10-07.md)
- [AINews — Decision models become a product category](../sources/newsletters/ainews-decision-models-product-category-2026-10-10.md)
- [AINews — Artificial Analysis launches a Decision Index](../sources/newsletters/ainews-aa-decision-index-2026-10-14.md)
- [AINews — Liquid d1-ultra tops the Decision Index; pplx-decider v1.2](../sources/newsletters/ainews-liquid-d1-ultra-pplx-decider-2026-10-17.md)
```

### wiki/state-of/models.md (updated)

Frontmatter `sources:` — append (keep all existing ids):

```
latent-space-jev-diogo-almeida-2026-09-21, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17, ainews-jev-judge-clm-critique-2026-09-25, every-how-to-get-most-out-of-jev-2026-09-23
```

New subsection, inserted directly after the "Domain-specialized models" subsection (before "Real-time voice / interaction models"):

```
### Decision models

Models that return calibrated typed answers (a yes/no probability, a pick, a score) in one pass instead of generating text. See [Decision models](../concepts/decision-models.md).

- [Jev](../models/jev.md) — TypeSafe; the reference model the category clones; $0.042/M input, output free; text only; second on Artificial Analysis's Decision Index (Jev 1.14: 57) *(as of 2026-10-17)*
- **Liquid d1-ultra** — Liquid AI; tops Artificial Analysis's Decision Index at 65, at Jev's price and 92 ms per task *(as of 2026-10-17)*
- **Clef / Clef-flash** — Cloudflare; open weights (Apache 2.0), Jev-API compatible, image input, 64K context; beats Jev on most rows of Cloudflare's own table at lower latency *(as of 2026-10-02)*
- **pplx-decider v1.2** — Perplexity; open weights, 27B at $0.02/M and 4B at $0.01/M input; adds reranking and multi-question single-pass inference *(as of 2026-10-17)*
- **OpenAI Decisions API** — public beta on GPT-6 Luna; $0.10/M input, no output charge; accepts images *(as of 2026-10-10)*
```

`## Recent changes` — insert one entry after the two `[2026-10-19]` … Domain-specialized entry (i.e. before `[2026-09-03] GPT-6 Astra launched`):

```
- [2026-10-17] New Decision models section. Jev (TypeSafe, 2026-09-15) started a class of models that return calibrated typed answers instead of text; within a month Cloudflare, OpenAI, Perplexity and Liquid shipped rivals, and Liquid d1-ultra took the top of Artificial Analysis's new Decision Index (65 vs Jev 1.14's 57).
```

Then remove the oldest entry from the live list (it moves to history):

```
- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

`as_of` stays 2026-10-20 (live value is newer).

### wiki/history/state-of/models.md (updated)

Append under the existing `## Archived from current page on 2026-10-20` block (open a new block with that header if the apply date differs):

```
- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter `sources:` — append:

```
every-how-to-get-most-out-of-jev-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, ainews-decision-models-product-category-2026-10-10
```

Append as the last bullet of `### Routing as infrastructure`:

```
- **Decision models for the yes/no steps.** Many agent steps are classifications, not generation. [Decision models](../concepts/decision-models.md) such as [Jev](../models/jev.md) return a calibrated probability for about $0.04 per million input tokens, output free. A Jev-as-a-judge paper reports that escalating only low-confidence calls to GPT-6 Astra keeps 99% of accuracy at 57% of the cost. LangChain says routing each Open SWE step to the cheapest adequate model cut median cost per task by 64%. Every's rule for the split: if a person could make the call in under 10 seconds, it goes to the decision model.
```

`## Recent changes` — insert at the top (newest first):

```
- [2026-10-17] Added decision models (Jev and rivals) as the cheap tier for yes/no agent steps, with a confidence-based escalation result and LangChain's 64% cost cut.
```

`## Related` — append:

```
- [Decision models](../concepts/decision-models.md) - non-generative models that return calibrated yes/no, choice and score answers; the cheapest tier for classification steps.
```

`## Sources` — append:

```
- [Every — How to Get the Most Out of Jev](../sources/newsletters/every-how-to-get-most-out-of-jev-2026-09-23.md)
- [AINews — Jev as a judge, CLM, and the classifier critique](../sources/newsletters/ainews-jev-judge-clm-critique-2026-09-25.md)
- [AINews — Decision models become a product category](../sources/newsletters/ainews-decision-models-product-category-2026-10-10.md)
```

`as_of` stays 2026-10-19 (live value is newer).

### wiki/sources/newsletters/latent-space-jev-diogo-almeida-2026-09-21.md (new)

```
---
title: 'Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-21-jev-system-one-models-for-prod-not-god-with-di.md
url: https://www.latent.space/p/jev
published: 2026-09-21
ingested: 2026-10-20
domains: [models]
---

# Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)

Long interview with TypeSafe CEO Diogo Almeida, a co-author of InstructGPT, a week after Jev's launch. He explains Jev as a model built for software rather than chat: three question types instead of generated text, trained for calibrated probabilities instead of human preference. He also covers TypeSafe's refusal to publish benchmarks or refuse requests, and its practice of freezing each model version.

## Influenced pages
- [Jev](../../models/jev.md) — what it is, primitives, RLCD, product stance
- [Decision models](../../concepts/decision-models.md) — definition, "System One" alias, design advice
- [State of Models](../../state-of/models.md) — Decision models section

## Key claims extracted
- Three primitives: Noulli (from Bernoulli; probability a statement is true), Choice (pick among options), Score (position on a scale); mapped to if, switch and sort
- RLCD (reinforcement learning for calibrated decisions) is unpublished; Almeida argues RLHF causes mode collapse and miscalibration
- TypeSafe is "extremely anti-public benchmarks"; Jev does not refuse, because a refusal inside a software dependency breaks the software
- Deployed model versions are never changed
- Advice: ask many small independent questions in parallel rather than one compound instruction
```

### wiki/sources/newsletters/every-how-to-get-most-out-of-jev-2026-09-23.md (new)

```
---
title: Every — How to Get the Most Out of Jev
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-23-how-to-get-the-most-out-of-jev.md
url: https://every.to/context-window/how-to-get-the-most-out-of-jev
published: 2026-09-23
ingested: 2026-10-20
domains: [models, agents]
---

# Every — How to Get the Most Out of Jev

Every's practical guide to Jev (by Laura Entis, with Mike Taylor, Jack Cheng and Douglas Brundage). It gives a 10-second rule for when to use Jev, and a four-step workflow for turning a subjective question into checks Jev can score. It also includes a voice-and-gesture canvas demo, and a price comparison: Jev costs $0.042 per million input tokens with output free.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — "How to use one" section
- [Jev](../../models/jev.md) — price, text-only input
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — 10-second routing rule

## Key claims extracted
- TypeSafe released Jev on 2026-09-15 after two years in stealth
- Rule of thumb: tasks a person could do in under 10 seconds go to Jev; longer ones go to an LLM
- Workflow: install the TypeSafe skill, have an agent interview you to define the term, split it into weighted yes/no checks, test on items you have already judged, then run on the full set
- Jev takes no image input; Jack Cheng's canvas demo sends speech transcripts, fingertip coordinates and a shape list instead
- Douglas Brundage's news scan went from under 20 posts to more than 500 per run after switching to Jev
```

### wiki/sources/tweets/jackyk02-clm-contrastive-language-model-2026-09-23.md (new)

```
---
title: Jacky Kwok — Introducing Contrastive Language Model (CLM)
type: source
source_type: tweet
source_file: raw/tweets/2026-09-23-jackyk02-2102905335925424285.md
url: https://x.com/jackyk02/status/2102905335925424285
published: 2026-09-23
ingested: 2026-10-20
domains: [models, agents]
---

# Jacky Kwok — Introducing Contrastive Language Model (CLM)

Launch thread for CLM-8B, an open-weight decision model that embeds the situation and each candidate action separately and ranks them by similarity, instead of scoring options with a head on one LLM pass.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — contrastive variant, verifier claim

## Key claims extracted
- Up to 9x faster than Jev at comparable computer-use, gaming and tool-calling performance
- After light fine-tuning: DeepSWE 81.6%, Terminal-Bench 2.1 87.6% as a verifier; "Jev fails to serve as an effective verifier" on these long-horizon tasks
- State and action embeddings are cached independently, which helps when the state changes but the action set does not
- Trained on 60M Q&A pairs, 30M synthetic hard negatives and 1M agent trajectories; loss follows power-law scaling
```

### wiki/sources/newsletters/ainews-jev-judge-clm-critique-2026-09-25.md (new)

```
---
title: AINews — Jev as a judge, CLM, and the classifier critique
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
url: https://www.latent.space/p/ainews-the-future-of-latent-space
published: 2026-09-25
ingested: 2026-10-20
domains: [models]
---

# AINews — Jev as a judge, CLM, and the classifier critique

The decision-model story from the 2026-09-25 AINews issue. It covers TypeSafe's fundraise, a paper testing Jev as an LLM judge, ecosystem adoption, and two Reddit threads: one arguing Jev is standard zero-shot classification, one comparing it with CLM.

## Influenced pages
- [Jev](../../models/jev.md) — judge results, Banking77 baseline
- [Decision models](../../concepts/decision-models.md) — skeptic view
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — escalation cascade result

## Key claims extracted
- TypeSafe reportedly raising $1B+ at a $10B+ valuation, a week after a $200M round
- Jev-as-a-Judge paper: $0.044 per 1K judgments, 152 ms median, ~277x cheaper than GPT-6; within 3 points on RewardBench and HaluEval, 14.5 points behind on JudgeBench; escalating low-confidence calls to GPT-6 Astra keeps 99% accuracy at 57% of the cost
- turbopuffer native reranking includes Jev; Jev is the top OpenRouter model at 1K–10K context
- Reddit critique: BGE-small plus logistic regression scored 93.3% on Banking77 vs Jev's 83.2%; the fair baselines are zero-shot classifiers, cross-encoders and rerankers
```

### wiki/sources/newsletters/latent-space-openai-decisions-api-2026-09-30.md (new)

```
---
title: Latent Space — How OpenAI shipped its Decisions API
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
url: https://www.latent.space/
published: 2026-09-30
ingested: 2026-10-20
domains: [models]
---

# Latent Space — How OpenAI shipped its Decisions API

The decision-model segment of a DevDay interview with OpenAI's Nikunj Handa (API team). He describes the Decisions API as a direct, Jev-inspired response that runs zero-shot on GPT-6 Luna.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — OpenAI's entry, clone count

## Key claims extracted
- Built in about a week after Jev's launch; "zero-shotting this on top of Luna" for the first version, with model improvements to follow
- Early internal use: classifying support tickets; expected use with GPT Live for fast tool delegation
- Host swyx counts about 100 Jev API clones in the two weeks after launch
```

### wiki/sources/articles/cloudflare-clef-decision-models-2026-10-02.md (new)

```
---
title: 'Cloudflare — Introducing Clef: open-source decision models and RL fine-tuning'
type: source
source_type: article
source_file: raw/articles/2026-10-02-cloudflare-clef-decision-models.md
url: https://blog.cloudflare.com/clef-decision-models/
published: 2026-10-02
ingested: 2026-10-20
domains: [models]
---

# Cloudflare — Introducing Clef: open-source decision models and RL fine-tuning

Cloudflare's launch post for Clef and Clef-flash: Apache 2.0 decision models hosted on Workers AI, API-compatible with Jev. It also announces an RL fine-tuning service, first run by Cloudflare's forward-deployed engineers and later offered as a self-serve product.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — architecture, Clef entry
- [Jev](../../models/jev.md) — 32K context, latency, benchmark rows
- [State of Models](../../state-of/models.md) — Clef line

## Key claims extracted
- Clef freezes Qwen3.8-27B (Clef-flash: Qwen3.5-9B); one prefill pass, then a schema head scores valid options in parallel; LoRA rank 256, label-smoothed cross-entropy plus Brier loss, and Cloudflare's own RLCD stage
- Image input and 64K context (Jev: text only, 32K)
- Cloudflare's 10-benchmark table: Clef or Clef-flash top 7 rows; Jev tops When2Call (80.97) and BRIGHT (47.52)
- Median latency: Clef 209 ms, Clef-flash 39 ms, Jev 524 ms
- Threat-intelligence domain classification took 2.2 s with Clef vs 4.7 s with gpt-oss-120b
```

### wiki/sources/newsletters/ainews-decisions-api-beta-vals-jev-2026-10-07.md (new)

```
---
title: AINews — Decisions API beta, pplx-decider, and Vals on Jev
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishe.md
url: https://www.latent.space/
published: 2026-10-07
ingested: 2026-10-20
domains: [models]
---

# AINews — Decisions API beta, pplx-decider, and Vals on Jev

The decision-model items from the 2026-10-07 AINews issue: OpenAI's public beta, Perplexity's open model, and an independent Vals check on Jev.

## Influenced pages
- [Jev](../../models/jev.md) — Vals results
- [Decision models](../../concepts/decision-models.md) — OpenAI and Perplexity entries

## Key claims extracted
- OpenAI Decisions API public beta on GPT-6 Luna: predicates, choices or scores; "up to 10x faster" than the Responses API; from $0.10/M input, no output charge
- Perplexity pplx-decider-v1.1-27b: open weights, $0.02/M input, tops HF Decision Index v0.3
- Vals: Jev matched GPT-6 Astra's 97.5% on claim verification at about 1/500th the cost; Jev ranked last on LegalBench
```

### wiki/sources/newsletters/ainews-decision-models-product-category-2026-10-10.md (new)

```
---
title: AINews — Decision models become a product category
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
url: https://www.latent.space/
published: 2026-10-10
ingested: 2026-10-20
domains: [models, agents]
---

# AINews — Decision models become a product category

The 2026-10-10 AINews lead story: TypeSafe passes $100M ARR at a $7.5B valuation three weeks after launch, while several vendors ship decision models on the same day.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — vendor wave, Unsloth notebook
- [Jev](../../models/jev.md) — ARR and valuation
- [State of Models](../../state-of/models.md) — OpenAI Decisions API line
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — LangChain 64% cost cut

## Key claims extracted
- OpenAI Decisions API accepts text and images, runs on GPT-6 Luna, $0.10/M input, no output charge
- Also shipped: Microsoft-Decision-1, Perplexity pplx-decider-v1.1-27b (94.5% on Decision Bench, $0.017 per 1K decisions), Cloudflare clef-omni (audio, video, image, text), Liquid d1 on Vercel AI Gateway, vLLM Semantic Router Decision 2.0
- Unsloth notebook turns Qwen3.5-4B into a decision model on 8GB of VRAM
- LangChain: routing each task to the cheapest adequate model cut median Open SWE cost per task by 64%
```

### wiki/sources/newsletters/ainews-aa-decision-index-2026-10-14.md (new)

```
---
title: AINews — Artificial Analysis launches a Decision Index
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-14-ainews-ai-engineer-nyc-gemini-4-argon-vals-ai.md
url: https://www.latent.space/p/ainews-ai-engineer-nyc-gemini-4-argon
published: 2026-10-14
ingested: 2026-10-20
domains: [models]
---

# AINews — Artificial Analysis launches a Decision Index

The decision-model item from the 2026-10-14 AINews issue: Artificial Analysis's new index covering knowledge, reasoning, tool calling and safety classification.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — benchmark section
- [Jev](../../models/jev.md) — index score at launch

## Key claims extracted
- Jev 1.13 leads the published decision-model results at 58
- Claude Haiku 5.5 Low scores 61 but costs $184 vs $42 per million tasks and takes 1.4 s vs 0.13 s per task
- Decision models are competitive on classification and routing, weaker and often overconfident on knowledge and reasoning
```

### wiki/sources/newsletters/ainews-liquid-d1-ultra-pplx-decider-2026-10-17.md (new)

```
---
title: AINews — Liquid d1-ultra tops the Decision Index; pplx-decider v1.2
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-17-ainews-high-taste-testers-ep-1.md
url: https://www.latent.space/
published: 2026-10-17
ingested: 2026-10-20
domains: [models]
---

# AINews — Liquid d1-ultra tops the Decision Index; pplx-decider v1.2

The decision-model items from the 2026-10-17 AINews issue.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — current index leader
- [Jev](../../models/jev.md) — second place
- [State of Models](../../state-of/models.md) — Liquid d1-ultra and pplx-decider lines

## Key claims extracted
- Liquid d1-ultra tops Artificial Analysis's Decision Index at 65, ahead of Jev 1.14 at 57; 92 ms per task, $0.042/M input, output free; non-hallucination 85% (d1: 2%) but accuracy 32% (d1: 41%)
- Perplexity pplx-decider v1.2: open weights, 27B at 2¢/M and 4B Flash at 1¢/M; adds reranking and single-pass multi-question inference up to 5x faster
- OpenAI's Live API added the Decisions API for fast tool delegation
```

## Schema / vocabulary additions

- [ ] Add subcategory `decision-model` to `wiki/_schema/subcategories.md` (add the slug to the "Declared slugs" line and this block):

```
### decision-model
- **Parent domain(s):** models, agents
- **Applies to types:** model | concept
- **Definition:** General-purpose models that answer typed questions about an input (a yes/no probability, a pick from options, a score on a scale) in one pass without generating text, used as cheap programmable judgments inside software and agent loops. Distinct from `utility-model` (one fixed pipeline task) and `domain-specialized-model` (one profession's decisions).
- **Examples:** [Jev](../models/jev.md), [Decision models](../concepts/decision-models.md)
```

## Open questions

- Should ScaleDown (now marketed as "Constrained Decoding Models", with a Jev-compatible Decisions API) and MedDecider-27B move into the new Decision models section and subcategory? The proposal leaves them where they are, as a utility model and a domain-specialized model.
- Liquid d1-ultra, Clef and pplx-decider appear as unlinked lines on State of Models. Should any of them get its own model page now, or wait until a primary source is ingested?
