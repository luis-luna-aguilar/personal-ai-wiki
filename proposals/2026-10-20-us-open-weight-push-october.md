---
type: proposal
source: raw/newsletters/2026-10-17-ainews-high-taste-testers-ep-1.md
sources:
  - raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
  - raw/newsletters/2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishe.md
  - raw/newsletters/2026-10-16-ainews-agents-disprove-polysemanticity-greatly.md
  - raw/newsletters/2026-10-17-ainews-high-taste-testers-ep-1.md
  - raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
  - raw/newsletters/2026-10-01-getting-started-with-open-models.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: The October open-weight wave — Reflection Beam, Muse Spark Open, Mistral Large 4

## Summary

### In short
US labs are finally shipping big open weights, but they still trail the Chinese open leaders: Meta's Muse Spark Open (816B, 42B active) and Reflection's Beam (501B, 23B active) both shipped in mid-October, scoring 39 and 30 on Artificial Analysis's index against 45 for GLM-5.3. Europe's Mistral Large 4 (1T) scores 38 but its weights are still pending. The proposal creates a Reflection Beam page, adds both models to State of Models, records Spark's open weights and Glimmer's training report, and updates the open-weight trend. Reason to hesitate: Every's open-models guide was read only as a paywalled preview.

[[#Open questions|Open questions: 1 to answer.]]

### The source
AINews tracked the wave across five issues. On 6 October it covered Reflection, a US lab that had stayed in stealth for over a year, announcing Beam: a text-only mixture-of-experts model (only 23B of its 501B parameters active per token) trained from scratch in the US on 23.8T tokens, with RL on about 10,500 GB300 GPUs. Reflection claimed 80.9 on SWE-bench Verified; observers placed it around GLM-5.2 and below DeepSeek's newer Flash. Beam 1.0 shipped around 16 October under Apache 2.0 with the Mirror CLI harness it was trained in and a safety report. Artificial Analysis scored it 30, the #2 US open model, with 48.5% on AutomationBench but 3.0% on Terminal-Bench 4.0 and a 47% hallucination rate.

On 16 October Meta released Muse Spark Open, fulfilling the "coming soon" promise made since Spark 1.2, though observers place it near Spark 1.2 rather than the current 1.3. It takes text, image, video and audio, has a 1M-token context and ships under a custom Muse Model License requiring attribution and a separate deal for model-hosting businesses above $20M revenue. Artificial Analysis gives it 39, the best US open-weight score, ahead of Beam but behind GLM-5.3 (45) and Kimi K3 (44). It is the most token-frugal and least hallucination-prone of the top open models but ranks last of the top nine on agentic tests. A compressed checkpoint runs on two 512GB Mac Studios. Meta also published a report on Muse Glimmer, its 30B open model, trained by distilling from Spark's outputs while Spark itself was still training.

Mistral previewed Large 4 ("Le Chonk"), 1T total and 49B active, trained in Europe, with weights promised for end of October; it scores 38 but costs over four times similar open models per task. Smaller releases included Aleph Alpha's Kolibri, Ling 3.1 Flash, StepFun Step 5 Preview (non-commercial license) and EmbeddingGemma 2. Every's guide adds that 56% of Vercel AI Gateway tokens ran on open models in August, and open models handle 40% of AT&T's AI use.

### What changes
The wiki's open-weight trend stops at 1 September and Muse Spark's pages still say its weights are "coming soon".

- New page `models/reflection-beam.md`.
- **State of Models** adds Muse Spark Open and Reflection Beam to Open-weight models, removes "open weights still pending" from the Muse Spark frontier line, and adds a Recent-changes entry; the oldest entry (Grok 4.6, 13 August) moves to history.
- **Muse Spark** replaces the "coming soon" bullet with the Spark Open release. Page date moves to 17 October.
- **Muse Glimmer** gains the technical report's training recipe and its first Recent-changes section. Page date moves to 20 October.
- **Open-weight momentum broadens** gains a US-push bullet and updated adoption figures; the oldest Recent-changes entry (Kimi K3 economics, 29 July) moves to history. Page date moves to 17 October.
- Six story-specific source pages.

### What to weigh
Mistral Large 4, Kolibri, Ling, Step 5 and EmbeddingGemma 2 stay as trend mentions without pages until their weights ship or they show staying power. Spark Open goes on the existing Muse Spark page, not a page of its own.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/reflection-beam.md` — index entry under Models: `- [models/reflection-beam](models/reflection-beam.md) — Reflection's first model; 501B/23B-active text MoE trained from scratch in the US; Apache 2.0; AA Intelligence Index 30, #2 US open model *(as_of: 2026-10-17)*`

- [ ] **Update** `wiki/state-of/models.md` — edit the Muse Spark frontier line; add two lines under `### Open-weight models`; add one Recent-changes entry dated 2026-10-16 (live list has 10, cap 10); append source ids; `as_of` stays 2026-10-20

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest entry (expected: [2026-08-13] Grok 4.6)

- [ ] **Update** `wiki/models/muse-spark.md` — replace the open-weights bullet in Current status; one Recent-changes entry dated 2026-10-16 (live list has 9, becomes 10); append source ids and links; `as_of` 2026-09-08 → 2026-10-17

- [ ] **Update** `wiki/models/muse-glimmer.md` — one Current-status bullet; new `## Recent changes` section; append source id and link; index entry date; `as_of` 2026-08-11 → 2026-10-20

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — edit the access-risk bullet; add one bullet under `### New entrants broaden the geography and scope`; one Recent-changes entry dated 2026-10-16 (live list has 10); append source ids and links; `as_of` 2026-09-01 → 2026-10-17

- [ ] **Spill** `wiki/trends/open-weight-momentum-broadens.md` → `wiki/history/trends/open-weight-momentum-broadens.md` — oldest entry (expected: [2026-07-29] Kimi K3 deployment economics)

- [ ] **Create** six source pages under `wiki/sources/newsletters/` (drafts below)

## Page drafts

### wiki/models/reflection-beam.md (new)

```
---
title: Reflection Beam
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [open-weights, text]
as_of: 2026-10-17
sources: [ainews-reflection-beam-2026-10-06, ainews-reflection-beam-training-2026-10-07, ainews-us-open-weights-push-2026-10-17]
---

# Reflection Beam

Reflection's first model, after more than a year in stealth: a text-only 501B-total / 23B-active mixture-of-experts model for coding, agentic and scientific work, trained from scratch in the US. Beam 1.0 shipped around 2026-10-16 under Apache 2.0.

## Current status (as of 2026-10-17)

- 1M context; BF16, FP8 and NVFP4 weights, a DFlash2 speculative-decoding drafter, the open Mirror CLI harness Beam was trained in, and a safety report
- Artificial Analysis Intelligence Index 30, #2 among US open models (behind [Muse Spark Open](muse-spark.md)); ~26K tokens per task; 48.5% AutomationBench-AA but 3.0% Terminal-Bench 4.0; AA-Omniscience 33% correct, 47% hallucination
- Arena: #12 open model in Agent Arena; the only non-Chinese model in the top 25 open models on Code WebDev
- Reflection's claim: 80.9 on SWE-bench Verified and 3–4x GLM-5.2's inference efficiency; observers place it around GLM-5.2 and below DeepSeek V4.1 Flash
- Training: 23.8T pretraining tokens (partly OCR'd PDFs); four weeks each of pretraining and RL on ~10,500 GB300s, with over 100M rollouts across ~1M tasks; day-0 vLLM, SkyRL and Ollama support

## Why it matters

A credible US-trained, permissively licensed open model from a new lab, arriving the same week as Meta's Muse Spark Open. It still trails the Chinese open leaders (GLM-5.3, Kimi K3, DeepSeek V4.1 Flash). See [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md).

## Weaknesses / caveats

- Very weak on Terminal-Bench 4.0 and high hallucination rate
- Low estimated pretraining efficiency (~12% BF16 MFU); one commentator calls it an iso-FLOP replication of DeepSeek V3

## Recent changes

- [2026-10-16] Beam 1.0 weights shipped under Apache 2.0 with the Mirror harness and a safety report; AA Intelligence Index 30.
- [2026-10-05] Announced: 501B/23B text MoE trained from scratch in the US; weights due in October.

## Sources

- [AINews — Reflection Beam announcement](../sources/newsletters/ainews-reflection-beam-2026-10-06.md)
- [AINews — Beam training details and Mistral Large 4](../sources/newsletters/ainews-reflection-beam-training-2026-10-07.md)
- [AINews — US open-weights push: Spark Open and Beam 1.0](../sources/newsletters/ainews-us-open-weights-push-2026-10-17.md)
```

### wiki/state-of/models.md (updated)

Frontmatter `sources:` — append:

```
ainews-reflection-beam-2026-10-06, ainews-muse-spark-open-2026-10-16, ainews-us-open-weights-push-2026-10-17
```

Under `### Frontier models`, replace the Muse Spark line's ending `; open weights still promised "soon" *(as of 2026-09-03)*` with:

```
; open weights shipped 2026-10-16 as the separate, weaker Muse Spark Open *(as of 2026-10-16)*
```

Under `### Open-weight models`, append:

```
- [Muse Spark Open](../models/muse-spark.md) — Meta; 816B/42B-active multimodal MoE, 1M context, custom Muse Model License; AA Intelligence Index 39, top US open-weight model but behind GLM-5.3 and Kimi K3, last of the top nine open models on agentic evals *(as of 2026-10-17)*
- [Reflection Beam](../models/reflection-beam.md) — Reflection; 501B/23B-active text MoE trained from scratch in the US, Apache 2.0, ships with its Mirror training harness; AA Intelligence Index 30 *(as of 2026-10-17)*
```

`## Recent changes` — insert at the top:

```
- [2026-10-16] US open-weight push: Meta's Muse Spark Open (816B/42B, AA 39, top US open model) and Reflection Beam 1.0 (501B/23B, Apache 2.0, AA 30) added to Open-weight models; both trail GLM-5.3 (45) and Kimi K3 (44).
```

Then spill the oldest entry.

### wiki/history/state-of/models.md (updated)

Append at the end of the file:

```

## Archived from current page on <apply date>

- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

(If an archive block for the apply date already ends the file, append to it. The entry spilled is whichever is oldest at apply time.)

### wiki/models/muse-spark.md (updated)

Frontmatter: `as_of: 2026-10-17`; append to `sources:`:

```
ainews-muse-spark-open-2026-10-16, ainews-us-open-weights-push-2026-10-17
```

Rename `## Current status (as of 2026-09-08)` → `## Current status (as of 2026-10-17)`. Replace the bullet beginning `- Open weights promised "coming soon" since 1.2` with:

```
- **Muse Spark Open (2026-10-16):** the promised open weights, as a separate model rather than Spark 1.3: 816B total / 42B active MoE, 1M context, text/image/video/audio input, under a custom Muse Model License (attribution required; separate deal for model-hosting businesses above $20M revenue). Observers place it near Spark 1.2. AA Intelligence Index 39, top US open-weight model but behind GLM-5.3 (45) and Kimi K3 (44); fewest output tokens and lowest hallucination among the top nine open models, but last of them on agentic evals; $0.84 per index task on Together/Fireworks/Baseten. The NVFP4 checkpoint (~530GB) runs on two 512GB Mac Studios. The smaller [Muse Glimmer](muse-glimmer.md) (30B, Apache 2.0) shipped 2026-08-11
```

`## Recent changes` — insert at the top:

```
- [2026-10-16] Muse Spark Open released: 816B/42B open-weight MoE under a custom license, AA Intelligence Index 39 (top US open model), weaker than Spark 1.3.
```

`## Sources` — append:

```
- [AINews — Meta releases Muse Spark Open](../sources/newsletters/ainews-muse-spark-open-2026-10-16.md)
- [AINews — US open-weights push: Spark Open and Beam 1.0](../sources/newsletters/ainews-us-open-weights-push-2026-10-17.md)
```

### wiki/models/muse-glimmer.md (updated)

Frontmatter: `as_of: 2026-10-20`; `sources: [anthropic-riemann-hypothesis-2026-08-11, ainews-muse-glimmer-report-2026-10-20]`.

Rename `## Current status (as of 2026-08-11)` → `## Current status (as of 2026-10-20)` and append:

```
- **Technical report (2026-10-20):** trained by full-KL co-distillation from Muse Spark's in-training logits (the student learned from the teacher while the teacher was still training), switching to plain cross-entropy for the final 5%; training also used simulated multi-week "digital lives" as agent scenarios. Designed to run at 4-bit on a single consumer GPU
```

Insert before `## Sources`:

```
## Recent changes

- [2026-10-20] Technical report published: co-distillation from Muse Spark's in-training logits, simulated multi-week "digital lives".
- [2026-08-11] Released under Apache 2.0: 30B dense multimodal agent model; AA Intelligence Index 35.
```

`## Sources` — append:

```
- [AINews — Muse Glimmer technical report](../sources/newsletters/ainews-muse-glimmer-report-2026-10-20.md)
```

Index entry date for `models/muse-glimmer` moves to `2026-10-20`.

### wiki/trends/open-weight-momentum-broadens.md (updated)

Frontmatter: `as_of: 2026-10-17`; append to `sources:`:

```
ainews-reflection-beam-2026-10-06, ainews-reflection-beam-training-2026-10-07, ainews-muse-spark-open-2026-10-16, ainews-us-open-weights-push-2026-10-17, every-getting-started-open-models-2026-10-01
```

In `### Structural framing`, in the access-risk bullet, replace `open-weight models' share of Vercel AI Gateway tokens rising from 11% to 29% in two months` with:

```
open-weight models' share of Vercel AI Gateway tokens rising from 11% to 29% in two months, and to 56% by August; AT&T now runs 40% of its AI use on open models and expects up to 60%
```

Under `### New entrants broaden the geography and scope`, insert before the Unsloth Desktop bullet:

```
- **The US open-weight push (October 2026)** brought two large US releases in one week: Meta's [Muse Spark Open](../models/muse-spark.md) (816B/42B, custom license, AA Intelligence Index 39, top US open model) and Reflection's [Beam](../models/reflection-beam.md) (501B/23B, Apache 2.0, AA 30, shipped with its training harness). Both still trail GLM-5.3 (45) and Kimi K3 (44). Mistral previewed Large 4 (1T/49B, trained in Europe, AA 38, weights promised end of October), and smaller releases included Aleph Alpha Kolibri (German/English), Ling 3.1 Flash (AA 41), StepFun Step 5 Preview (600B/27B, non-commercial license) and Google's multimodal EmbeddingGemma 2.
```

`## Recent changes` — insert at the top:

```
- [2026-10-16] US open-weight push: Muse Spark Open (AA 39) and Reflection Beam 1.0 (AA 30) ship in the same week, both behind GLM-5.3 and Kimi K3; Mistral Large 4 previewed with weights pending; open models reach 56% of Vercel AI Gateway tokens in August.
```

Then spill the oldest entry.

`## Sources` — append:

```
- [AINews — Reflection Beam announcement](../sources/newsletters/ainews-reflection-beam-2026-10-06.md)
- [AINews — Beam training details and Mistral Large 4](../sources/newsletters/ainews-reflection-beam-training-2026-10-07.md)
- [AINews — Meta releases Muse Spark Open](../sources/newsletters/ainews-muse-spark-open-2026-10-16.md)
- [AINews — US open-weights push: Spark Open and Beam 1.0](../sources/newsletters/ainews-us-open-weights-push-2026-10-17.md)
- [Every — Getting Started With Open Models](../sources/newsletters/every-getting-started-open-models-2026-10-01.md)
```

### wiki/history/trends/open-weight-momentum-broadens.md (updated)

Append at the end of the file:

```

## Archived from current page on <apply date>

- [2026-07-29] Kimi K3 deployment economics documented: ~8×MI355X minimum to load, 64+ GPUs for production serving, six-figure entry cost; Composio's cross-harness comparison shows the same model performs similarly but at very different cost/speed depending on the agent harness used (Kimi Code, Hermes, Claude Code).
```

(If an archive block for the apply date already ends the file, append to it. The entry spilled is whichever is oldest at apply time.)

### wiki/sources/newsletters/ainews-reflection-beam-2026-10-06.md (new)

```
---
title: '[AINews] Reflection Beam - 501B-A23B American Open Model'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
url: https://www.latent.space/p/ainews-reflection-beam-501b-a23b
published: 2026-10-06
ingested: 2026-10-20
domains: [models]
---

# AINews — Reflection Beam announcement

AINews' lead story for 3–5 October 2026: Reflection announced Beam, a US-trained open model, alongside smaller open releases (Kolibri, Reka Rho-1, Solar Mini 4).

## Influenced pages

- [Reflection Beam](../../models/reflection-beam.md) — new page
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — US push, Kolibri
- [State of Models](../../state-of/models.md) — Open-weight models line

## Key claims extracted

- Beam: text-only 501B/23B MoE for coding, agentic and science work, trained from scratch; Apache 2.0 weights due in October
- 23.8T pretraining tokens; RL/OPD on 10K GB300s, 100M+ rollouts across ~1M tasks
- Claims 80.9 SWE-bench Verified, 3–4x GLM 5.2 inference efficiency
- Observers: around GLM-5.2 level, below DeepSeek V4 Flash on some benchmarks; ~12% BF16 MFU estimate; "iso-FLOP replication of DeepSeek V3"
- Aleph Alpha Kolibri: 78B/3.46B, Apache 2.0, German/English; agentic evals well below Qwen
```

### wiki/sources/newsletters/ainews-reflection-beam-training-2026-10-07.md (new)

```
---
title: AINews — Beam training details, Mistral Large 4 and other open releases (Quasi-Riemann issue)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishe.md
url: https://www.latent.space/p/ainews-quasi-riemann-hypothesis-openai
published: 2026-10-07
ingested: 2026-10-20
domains: [models]
---

# AINews — Beam training details and Mistral Large 4

Story-specific page for the open-model items in AINews' 7 October 2026 issue: Mistral Large 4 "Le Chonk" preview, EmbeddingGemma 2, Ling 3.1 Flash and a Reflection Beam training analysis.

## Influenced pages

- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Mistral Large 4, Ling 3.1 Flash, EmbeddingGemma 2
- [Reflection Beam](../../models/reflection-beam.md) — training details

## Key claims extracted

- Mistral Large 4 preview: 1T total / 49B active, multimodal, API now, open weights promised end of October; trained on ~3,800 Grace Blackwells in Europe; $1.36/$4.18 per M
- AA Intelligence Index 38, level with GPT-6 Luna (max), top score outside the US and China; $1.13 per task, over 4x similar open models; trails GLM-5.3
- EmbeddingGemma 2: Google's first natively multimodal open embedding model (text, code, image, video, audio), Apache 2.0
- Ling 3.1 Flash: 560B/25B, AA 41 (up from 20), weights coming
- Beam: RL on ~10,500 GB300s for four weeks; multi-teacher on-policy distillation
```

### wiki/sources/newsletters/ainews-muse-spark-open-2026-10-16.md (new)

```
---
title: AINews — Meta releases Muse Spark Open (Agents Disprove Polysemanticity issue)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-16-ainews-agents-disprove-polysemanticity-greatly.md
url: https://www.latent.space/p/ainews-agents-disprove-polysemanticity
published: 2026-10-16
ingested: 2026-10-20
domains: [models]
---

# AINews — Meta releases Muse Spark Open

Story-specific page for the Muse Spark Open release in AINews' 16 October 2026 issue.

## Influenced pages

- [Muse Spark](../../models/muse-spark.md) — open weights shipped
- [State of Models](../../state-of/models.md) — Open-weight models line, Muse Spark frontier line
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — US push

## Key claims extracted

- Muse Spark Open: 816B/42B MoE, 1M context, text/image/video/audio input; first base model trained under MSL; observers place it near Spark 1.2
- Custom Muse Model License: "Built with Muse Spark Open" attribution; separate agreement for MaaS businesses above $20M revenue
- AA Intelligence Index 39: first among US open-weight models, behind GLM-5.3 (45) and Kimi K3 (44); fewest output tokens (40K/task) of the top nine open models; leads open models on AA-Omniscience; last of the nine on agentic evals
- $1.25/$4.25 per M on Together/Fireworks/Baseten; $0.84 per index task vs $2.01 GLM-5.3, $0.27 DeepSeek V4.1 Flash
- NVFP4 checkpoint ~530GB; runs on 4× Blackwell Ultra, 8× H200 or two 512GB Mac Studios
```

### wiki/sources/newsletters/ainews-us-open-weights-push-2026-10-17.md (new)

```
---
title: '[AINews] High Taste Testers Ep. 1 — US open-weights push: Muse Spark Open and Reflection Beam 1.0'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-17-ainews-high-taste-testers-ep-1.md
url: https://www.latent.space/p/ainews-high-taste-testers-ep-1
published: 2026-10-17
ingested: 2026-10-20
domains: [models]
---

# AINews — US open-weights push: Spark Open and Beam 1.0

Story-specific page for the "US Open-Weights Push" section of AINews' 17 October 2026 issue.

## Influenced pages

- [Reflection Beam](../../models/reflection-beam.md) — 1.0 release and independent evals
- [Muse Spark](../../models/muse-spark.md) — Spark Open evals and footprint
- [State of Models](../../state-of/models.md) — Open-weight models lines
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — US push, Step 5 Preview

## Key claims extracted

- Muse Spark Open: AA 39, highest US open-weights score; last among top nine open models on AA's agentic evals; Vals #12 open / #38 overall; top US open model on Code Arena WebDev
- Reflection Beam 1.0: 501B/23B, 1M context, Apache 2.0; BF16/FP8/NVFP4 weights, DFlash2 drafter, open Mirror CLI harness, safety report
- Beam: AA 30 (#2 US open), ~26K tokens/task, AutomationBench-AA 48.5%, Terminal-Bench 4.0 3.0%, AA-Omniscience 33% correct / 47% hallucination; Agent Arena #12 open; only non-Chinese model in the top 25 open on Code WebDev
- StepFun released Step 5 Preview open weights
```

### wiki/sources/newsletters/ainews-muse-glimmer-report-2026-10-20.md (new)

```
---
title: AINews — Muse Glimmer technical report (not much happened today, 2026-10-20)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-f09
published: 2026-10-20
ingested: 2026-10-20
domains: [models]
---

# AINews — Muse Glimmer technical report

Story-specific page for the Muse Glimmer item in AINews' 20 October 2026 issue.

## Influenced pages

- [Muse Glimmer](../../models/muse-glimmer.md) — training recipe

## Key claims extracted

- Meta published a technical report on Muse Glimmer, a 30B open-weight agentic model designed to run at 4-bit on one consumer GPU
- Full-KL co-distillation from Muse Spark's in-training logits, then cross-entropy for the final 5%
- Training uses simulated multi-week "digital lives"
```

### wiki/sources/newsletters/every-getting-started-open-models-2026-10-01.md (new)

```
---
title: Every — Getting Started With Open Models
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-01-getting-started-with-open-models.md
published: 2026-10-01
ingested: 2026-10-20
domains: [models]
---

# Every — Getting Started With Open Models

Every's guide to adopting open models. Only the free preview was readable; the guide itself is paywalled.

## Influenced pages

- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — adoption figures

## Key claims extracted

- Vercel: 56% of tokens on its AI Gateway ran through open models in August 2026
- AT&T: open models handle 40% of its AI use, possibly rising to 60%
- On-device AI is the headline feature of Apple's latest Mac Studio and Mac Mini
```

## Schema / vocabulary additions

None.

## Open questions

- Should Mistral Large 4 get its own page now (it is #1 open-weight on Vals' HLAB and the strongest non-US, non-Chinese model) or wait until its weights actually ship (as drafted)?
