---
title: AI-Assisted Personal Health Investigation
type: use-case
domains: [healthcare]
tags: [agentic]
as_of: 2026-06-16
sources: [2026-06-16-metalearn-mystery-fatigue-ai]
---

# AI-Assisted Personal Health Investigation

Using frontier AI models to investigate ambiguous, multi-system symptoms through a structured 4-step loop. Documented to match or exceed PCP visits for ambiguous presentations when the patient is AI-literate and runs a good process.

**Bold claim (Amy Deng, METR researcher):** "An AI-literate patient running a good process with a frontier model can outperform most PCP visits for ambiguous, multi-system symptoms." Models surfaced nearly every hypothesis a specialist's NP offered on a phone visit and independently flagged the same niche ACTH stimulation test.

## The 4-step process

**Step 1 — Track:** Log symptoms and candidate causes longitudinally. Episodic symptoms have too many variables to hold in memory. Ask an LLM to suggest high-signal metrics given your symptoms and working hypothesis. Tools: spreadsheet (Notion), specialized apps (Garmin, Cronometer, CGM). Rule: as easy as possible + exportable format.

**Step 2 — Test:** Run blood work and specialized tests in parallel with tracking. Ask the model what additional tests might be worthwhile — they tend to be "just conservative enough." Avoid over-testing; it's emotionally costly.

**Step 3 — Analyze:** Feed all tracked data and test results to a frontier model. No PCP can sift through months of scattered notes; data-wrangling is exactly what these models do best. Sample questions:
- "Looking through all the data, can you find any patterns in what triggers my symptoms and what resolves them?"
- "What hypotheses might explain my symptoms, and where does each fail?"
- "What additional testing might help?"

**Step 3.5 — Build a supporting cast:** Specialist consultations (dietitian, PT, sleep coach) complement the AI analysis. Half of Amy's fatigue episodes improved after eating — a dietitian identified she was under-fueling ~300 cal/day, something the model missed.

**Step 4 — Experiment:** Implement behavioral, dietary, supplement, or medication changes. Categories: (1) definitely worth doing (iron when ferritin low — start now); (2) harmless but maybe useless (creatine — space out); (3) potentially risky (medication changes — consult physician, time-bound, one at a time).

## Prompting tips

- Use reasoning models with high thinking effort: Claude Opus 4.8 or GPT 5.5.
- Create a project; upload clinical records once and let the model build memory around your health concerns.
- For advanced users: coding agents (Claude Code, Codex) handle complex file formats (CT/MRI, Garmin exports), surface unknown-unknowns via planning mode, and can build custom trackers.
- Provide ALL context — medical history, all records, exact test values with reference ranges (not just "in range"). Models have infinite patience; use it.
- Be specific: severity, duration, what happened beforehand.
- Be critical: models can confidently be wrong. Cross-check by regenerating and comparing across models. Never take risky action without physician sign-off.

## Plug-and-play artifacts

Amy published a system prompt and a Claude Code / Codex skill for this process:
- System prompt: `github.com/amydeng2000/health-self-investigation-skill` (references/portable-core.md)
- Claude Code / Codex skill: `github.com/amydeng2000/health-self-investigation-skill`

## Limitations

- ChatGPT and Claude are not HIPAA-compliant by default (users can opt out of training data use).
- No model outperformed the author's neuroendocrinologist (top expert in her condition) — specialist context still wins for rare or complex conditions.
- Most people have a significant "elicitation gap"; the process matters as much as the model.

## Sources

- [I Solved My Mystery Fatigue with AI](../sources/articles/2026-06-16-metalearn-mystery-fatigue-ai.md) — Amy Deng, MetaLearn Substack
