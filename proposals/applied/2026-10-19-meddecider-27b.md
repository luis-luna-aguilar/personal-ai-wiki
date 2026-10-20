---
type: proposal
source: raw/repos/lion-ai-meddecider-27b.md
status: pending
created: 2026-10-19
---

# Proposal: MedDecider-27B (calibrated medical decision model)

## Summary

### In short

Narrow clinical decisions, such as whether a drug in a note is a current medication or whether a patient meets a trial criterion, can now go to a mid-size open-weight model that returns a calibrated probability per answer in one pass, without writing text. MedDecider-27B, a small adapter on Qwen 3.8 27B, scores 88.3% on robustness tests against 79.5% for TypeSafe's Jev 1.13, and passes every Polish medical licensing exam session from 2008 to 2026. The proposal adds a model page and lines on both State of Models and State of Healthcare. Reason to hesitate: it needs a new subcategory.

[[#Open questions|Open questions: 2 to answer.]]

### The source

MedDecider-27B is a Hugging Face model card from thelion.ai, released in October 2026. The model does one kind of job. It reads a clinical state (a note, a trial record or any JSON), receives a question with 2 to 10 answer options, and returns a probability for every option in a single scoring pass. It never generates text: it reads how likely the model is to pick each option letter, scores the question twice with the options in opposite order, and averages the two. A temperature fitted per question type calibrates the result, meaning a 0.8 should be right about 80% of the time. The card says to refit that calibration on a few hundred local labelled examples before treating the numbers as risks.

Technically it is a LoRA adapter, a small set of extra weights (234 MB), on Alibaba's Qwen3.8-27B. It was trained for one epoch on 35,800 decisions in 85 minutes on one NVIDIA H200. The training mix covers medical exams, differential diagnosis, code-generated clinical notes with near-identical twin cases, trial eligibility, evidence inference, and robustness items such as planted instructions. On 9,849 held-out items it leads the 27B-class comparison on robustness (88.3%), unseen clinical problem types (89.7%) and trial criteria (85.4%). It follows an instruction hidden in a note 3.0% of the time, against 13.7% for Jev 1.13. On unseen medical exams Jev leads, 65.4% to 64.4%. Over 4,722 questions of the Polish final medical exam it scores 87.1%, and on 286 new 2025–2026 questions 89.2%, where the average examinee scored 71.3%. The card itself notes that two rows favour MedDecider because their datasets were split between training and test. It calls the model a research model, not a medical device. It was trained on English only and released under CC BY-NC 4.0, non-commercial. Sibling models range from 4B to 31B, plus a Duo ensemble.

### What changes

The wiki has no medical models. Its only narrow-task model is OpenAI Privacy Filter, under "Specialized utility models", and State of Healthcare lists only products and use cases.

- New page `wiki/models/meddecider-27b.md` explaining the scoring mechanism, results, and the card's own limits.
- **State of Models** gains a "Domain-specialized models" section with one line, and one Recent-changes entry. The list is at its cap of ten, so the oldest entry (31 July, Inkling-Small) moves to history. Page date moves from 8 September to 19 October.
- **State of Healthcare** gains the same section with one line, plus one Recent-changes entry (six become seven, no spill). Page date moves from 13 August to 19 October.
- New subcategory `domain-specialized-model`.
- One new source page for the model card.

### What to weigh

The card gives only "October 2026" as the release date, so 19 October, the capture date, is used. The main decision is the subcategory. `utility-model` covers small models for pipeline tasks such as PII redaction, and a 27.8B model built for clinical judgment fits it badly. I propose `domain-specialized-model` for models tuned to one profession's decisions or knowledge, which legal or finance models could later join. The non-commercial license limits who can use the model, so it is on the page and the dashboard lines.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/meddecider-27b.md` — new model page (subcategory `domain-specialized-model`)
- [ ] **Update** `wiki/state-of/models.md` — add new `### Domain-specialized models` section after `### Specialized utility models`; adds one Recent-changes entry dated 2026-10-19 at the top (list is at the cap of 10); append `lion-ai-meddecider-27b` to frontmatter `sources:`; `as_of` 2026-09-08 → 2026-10-19
- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — spills the oldest Recent-changes entry (2026-07-31, Inkling-Small) under a new archive header
- [ ] **Update** `wiki/state-of/healthcare.md` — add new `### Domain-specialized models` section after `### Healthcare AI`; adds one Recent-changes entry dated 2026-10-19 (7 of 10, no spill); append `lion-ai-meddecider-27b` to frontmatter `sources:` and one link to `## Sources`; `as_of` 2026-08-13 → 2026-10-19
- [ ] **Create** `wiki/sources/repos/lion-ai-meddecider-27b.md` — source summary

## Page drafts

### wiki/models/meddecider-27b.md (new)

```
---
title: MedDecider-27B
type: model
domains: [models, healthcare]
subcategory: domain-specialized-model
tags: [open-weights]
as_of: 2026-10-19
sources: [lion-ai-meddecider-27b]
---

# MedDecider-27B

thelion.ai's 27.8B medical decision model: given a clinical state (note, trial record, or JSON) and a question with 2–10 answer options, it returns a calibrated probability for every option in one scoring pass, without generating text. Built for high-volume decision steps such as medication and diagnosis checks in notes, trial-eligibility screening, evidence classification, and medical knowledge questions.

## Current status (as of 2026-10-19)

- LoRA adapter (rank 16, 234 MB) on Alibaba's [Qwen3.8-27B](qwen-3-8-27b.md); one epoch over 35,800 decisions (7.5M tokens) in 85 minutes on one H200; released October 2026
- Readout: option-letter logits with reasoning off, scored in both option orders and averaged; one calibration temperature per question type (choice, yes/no, ordered scale)
- On 9,849 held-out items, leads its 27B-class comparison on robustness (88.3% vs 79.5% for TypeSafe's Jev 1.13 and 76.0% for Clef 27B), unseen clinical problem types (89.7%), and trial criteria (85.4%); follows a planted instruction 3.0% of the time (Jev 1.13: 13.7%)
- Jev 1.13 leads on unseen medical exams (65.4% vs 64.4%); pplx-decider-v1-27b leads NLI4CT macro-F1 (0.848 vs 0.827)
- Polish final medical exam (LEK), 2008–2026: 87.1% over 4,722 questions, every session passed; 89.2% on 286 new 2025–2026 questions vs 71.3% for the average examinee
- License CC BY-NC 4.0 (non-commercial); family runs from 4B to 31B, plus a Duo ensemble of the 31B and 27B

## Why it matters

It turns a class of clinical judgments into a cheap, scorable primitive: a probability per option that code can threshold, rank, or route, instead of free text that has to be parsed and trusted. Its strongest result is resistance to instructions planted in records, which matters when notes or trial documents come from untrusted sources.

## Weaknesses / caveats

- Research model, not a medical device; outputs must not drive care without local validation and clinical oversight
- Trained on English only; Polish results are evaluation-only
- The trial-criteria and in-distribution rows use test halves of datasets whose training halves were in its training data, so those rows favour it; NLI4CT figures for the other models are their published scores
- Knowledge-heavy exam questions remain the weak spot (55–70% across the family)
- Training and quickstart notes are synthetic; calibration should be refit on a few hundred local labelled examples before probabilities are used as risks
- Non-commercial license; the base model keeps its own license

## Recent changes

- [2026-10-19] Page created from the Hugging Face model card (October 2026 release).

## Sources

- [MedDecider-27B model card](../sources/repos/lion-ai-meddecider-27b.md)
```

### wiki/state-of/models.md (updated)

Frontmatter (changed fields only; `sources:` appends `lion-ai-meddecider-27b` to the end of the live list):

```
as_of: 2026-10-19
sources: [ainews-death-of-params-glm-53-2026-08-20, ainews-claude-opus-5-launch-2026-07-25, every-taming-opus-5-2026-07-28, muse-spark, kimi-k2-6-blog, ainews-kimi-k3-2026-07-17, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25, qwen-3-6-27b-aa-2026-05-01, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, anthropic-spacex-dreams-2026-05-07, arena-leaderboard-2026-05-13, end-of-finetuning-debate-2026-05-13, thinking-machines-interaction-2026-05-12, gpt-5-5-instant-default-2026-05-06, qwen-3-7-arena-2026-05, fable-ban-june-2026, ainews-glm-52-june-2026, kimi-k27-code-june-2026, openai-economics-june-2026, ainews-fable5-june-2026, ainews-open-models-june-2026, every-fable5-vibe-check, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, every-opus-48-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, ainews-june-05-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30, gpt-56-sol-restricted-preview-2026-06, metr-gpt-5-6-sol-eval-2026-06, glm-52-frontier-adjacent-2026-06, open-weight-adoption-access-risk-2026-05, ainews-opus-48-dynamic-workflows-2026-05, outputmaxxing-amp-compute-utilization-2026-06, cohere-command-a-plus-launch, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-all-model-labs-are-now-agent-labs, google-io-2026-search-blog, ainews-google-io-2026, cursor-blog-grok-4-5-launch-2026-07, ainews-spacexai-grok-45-2026-07-09, ainews-gpt-56-launch-benchmarks-2026-07-10, ainews-thinkys-inkling-2026-07-16, ainews-not-much-happened-2026-08-01, ainews-qwen38-max-launch-2026-08-04, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, unsloth-desktop-chatgpt-linux-2026-08-12, every-vibe-check-gpt-6-astra-2026-09-03, latent-space-gpt-6-astra-ai-engineer-2026-09-03, ainews-gpt-6-astra-launch-2026-09-04, every-split-verdict-fable-astra-2026-09-06, lion-ai-meddecider-27b]
```

New section, inserted after `### Specialized utility models` and before `### Real-time voice / interaction models`:

```
### Domain-specialized models

Models fine-tuned for one profession's decisions or knowledge, evaluated on that domain's tasks rather than general benchmarks.

- [MedDecider-27B](../models/meddecider-27b.md) — thelion.ai; calibrated per-option probabilities for clinical decisions in one scoring pass; LoRA on Qwen3.8-27B; leads its 27B-class comparison on robustness (88.3%); CC BY-NC *(as of 2026-10-19)*
```

`## Recent changes` (adds one entry dated 2026-10-19 at the top; the list is at its cap of 10, so the oldest entry, dated 2026-07-31, spills):

```
- [2026-10-19] Added the "Domain-specialized models" section with MedDecider-27B, a medical decision model that returns calibrated option probabilities without generating text.
```

Entry removed from the bottom of the live list:

```
- [2026-07-31] Thinking Machines shipped Inkling-Small (276B/12B MoE, Intelligence Index 40), a near-flagship-capability sibling to Inkling at roughly a quarter the active footprint.
```

### wiki/history/state-of/models.md (updated)

Appended at the end of the file (spills whatever is oldest at apply time; at proposal time that is the entry below):

```

## Archived from current page on 2026-10-19 (1)

- [2026-07-31] Thinking Machines shipped Inkling-Small (276B/12B MoE, Intelligence Index 40), a near-flagship-capability sibling to Inkling at roughly a quarter the active footprint.
```

### wiki/state-of/healthcare.md (updated)

Frontmatter (changed fields only; `sources:` appends `lion-ai-meddecider-27b`):

```
as_of: 2026-10-19
sources: [legacy-ai-tools-roadmap-xlsx, dragon-copilot-launch, hippocratic-ai-homepage, tempus-homepage, zocdoc-zo, open-evidence-homepage, konko-kora-homepage, elevenlabs-scribe, 2026-06-16-metalearn-mystery-fatigue-ai, midjourney-medical-scanner-2026-06, ai-healthcare-triage-doctronic-2026-05, mistral-document-ai, bfl-flux-3-2026-07-24, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, lion-ai-meddecider-27b]
```

New section, inserted after `### Healthcare AI` and before `### Document intelligence`:

```
### Domain-specialized models

- [MedDecider-27B](../models/meddecider-27b.md) — open-weight medical decision model returning calibrated probabilities for note checks, trial eligibility, and exam questions; passes every Polish medical licensing exam session 2008–2026; research use, CC BY-NC *(as of 2026-10-19)*
```

`## Recent changes` (adds one entry dated 2026-10-19 at the top; 7 of 10, no spill):

```
- [2026-10-19] Added MedDecider-27B, the first medical-specialized model on the dashboard: calibrated per-option probabilities for clinical decisions, strongest on robustness and planted-instruction resistance.
```

`## Sources` (appends one link):

```
- [MedDecider-27B model card](../sources/repos/lion-ai-meddecider-27b.md)
```

### wiki/sources/repos/lion-ai-meddecider-27b.md (new)

```
---
title: 'MedDecider-27B model card (lion-ai/MedDecider-27B)'
type: source
source_type: repo
source_file: raw/repos/lion-ai-meddecider-27b.md
url: https://huggingface.co/lion-ai/MedDecider-27B
ingested: 2026-10-19
domains: [models, healthcare]
---

# MedDecider-27B model card

Hugging Face model card from thelion.ai for MedDecider-27B, a LoRA adapter on Qwen3.8-27B that scores clinical choice, yes/no, and ordered-scale questions and returns a calibrated probability per option without generating text. Released October 2026 (no day given); captured 2026-10-19.

## Influenced pages

- [MedDecider-27B](../../models/meddecider-27b.md) — new model page
- [State of Models](../../state-of/models.md) — new "Domain-specialized models" section
- [State of Healthcare](../../state-of/healthcare.md) — new "Domain-specialized models" section

## Key claims extracted

- 27.8B parameters; LoRA rank 16 on all linear layers (234 MB) on `Qwen/Qwen3.8-27B`, merged at load time
- Fine-tuning: 35,800 decisions, 7.5M tokens, one epoch, 85 minutes on one H200; English training data
- Readout from option-letter logits with reasoning off; both option orders averaged; temperatures per question type (choice 1.23, yes/no 1.0, score 1.0) fitted on in-distribution calibration data
- 9,849 held-out items; competitors run through their authors' inference code, Jev through TypeSafe's API
- Unseen medical exams: 64.4% (Jev 1.13 65.4%, Clef 27B 60.3%, pplx-decider-v1-27b 58.4%)
- Unseen clinical problem types: 89.7% (Jev 87.7%, Clef 89.0%, pplx 89.4%)
- Robustness: 88.3% (Jev 79.5%, Clef 76.0%, pplx 57.8%); follows planted instruction 3.0% (Jev 13.7%, Clef 17.7%, pplx 62.3%)
- NLI4CT macro-F1 0.827 (pplx 0.848 best); TrialGPT trial criteria 85.4% and in-distribution halves 88.1% (rows favour MedDecider)
- Polish LEK 2008–2026: 87.1% over 4,722 questions, all 26 sessions passed (pass mark 56%); 89.2% on 286 new 2025–2026 questions vs 71.3% average examinee
- Family: Duo (31B + 27B) 59.1B, 31B, 27B, 9B, 4B; 31B leads unseen exams at 70.2%
- Research model, not a medical device; CC BY-NC 4.0
```

## Schema / vocabulary additions

- [ ] Add new subcategory `domain-specialized-model` to `wiki/_schema/subcategories.md` (and to the "Declared slugs" line):

```
### domain-specialized-model
- **Parent domain(s):** models, healthcare
- **Applies to types:** model
- **Definition:** Models fine-tuned for one profession's decisions or knowledge (clinical, legal, financial) and evaluated on that domain's tasks rather than general benchmarks; distinct from `utility-model`, which covers small models for a generic pipeline task such as PII redaction or embedding.
- **Examples:** [MedDecider-27B](../models/meddecider-27b.md)
```

## Open questions

- If the new subcategory is declined, should the page fall back to `utility-model` and its dashboard line move under "Specialized utility models" on State of Models (with no healthcare section)?
	- Yes
- Should the [Qwen 3.8 27B](../wiki/models/qwen-3-8-27b.md) page gain a one-line note that MedDecider-27B is a downstream medical fine-tune of it? I left that page untouched.
	- Yes
