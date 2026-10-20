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
- [Qwen 3.8 27B](../../models/qwen-3-8-27b.md) — downstream fine-tune note

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
