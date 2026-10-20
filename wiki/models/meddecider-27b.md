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
