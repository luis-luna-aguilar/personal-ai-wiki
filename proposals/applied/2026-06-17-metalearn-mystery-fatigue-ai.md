---
type: proposal
source: raw/articles/2026-06-16-metalearn-mystery-fatigue-ai.md
status: pending
created: 2026-06-17
---

# Proposal: "I Solved My Mystery Fatigue with AI" — Amy Deng

## Summary

Amy Deng (AI researcher, formerly at METR) describes using frontier models and a systematic 4-step process (Track → Test → Analyze → Experiment) to solve her mystery episodic fatigue. Bold claim: an AI-literate patient running a good process with a frontier model can outperform most PCP visits for ambiguous, multi-system symptoms. The models surfaced nearly every hypothesis the specialist's NP offered and flagged the same niche ACTH stimulation test the NP independently ordered.

## Intended changes

- [x] **Create** `wiki/use-cases/ai-personal-health-investigation.md` — new use-case page for the 4-step patient health investigation process
    > See draft below

- [x] **Update** `wiki/state-of/healthcare.md` — add a "Patient-side AI" section noting emerging patient-empowerment pattern; bump `as_of`
    > See diff below

- [x] **Create** `wiki/sources/articles/2026-06-16-metalearn-mystery-fatigue-ai.md` — source summary

## Page drafts

### wiki/use-cases/ai-personal-health-investigation.md (new)

````md
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
````

### wiki/state-of/healthcare.md (updated diff)

> **Before** (after the "Speech to text" section, before `## Recent changes`):
> *(nothing — no patient-side section)*

> **After:** Add this section before `## Recent changes`:
> ```markdown
> ### Patient-side AI
>
> - Frontier models (Claude Opus 4.8, GPT 5.5) + a structured investigation process are documented to match or exceed PCP visits for ambiguous multi-system symptoms *(as of 2026-06-16)*
> - See use case: [AI-Assisted Personal Health Investigation](../use-cases/ai-personal-health-investigation.md)
> ```

> Also update frontmatter `as_of: 2026-04-22` → `as_of: 2026-06-16` and add `2026-06-16-metalearn-mystery-fatigue-ai` to `sources:`.

> Add to `## Recent changes`:
> ```
> - [2026-06-16] Added "Patient-side AI" subcategory — frontier models documented to match/exceed PCP visits for ambiguous symptoms (Amy Deng, MetaLearn)
> ```

### wiki/sources/articles/2026-06-16-metalearn-mystery-fatigue-ai.md (new)

````md
---
title: '"I Solved My Mystery Fatigue with AI" — Amy Deng'
type: source
source_type: article
source_file: raw/articles/2026-06-16-metalearn-mystery-fatigue-ai.md
url: https://metalearn.substack.com/p/i-solved-my-mystery-fatigue-with-ai
published: 2026-06-16
ingested: 2026-06-17
domains: [healthcare]
---

# "I Solved My Mystery Fatigue with AI" — Amy Deng

Amy Deng (AI researcher, METR) describes solving her episodic fatigue from a prolactinoma using a systematic AI-assisted process. She presents a 4-step framework (Track → Test → Analyze → Experiment) and argues that an AI-literate patient with a good process and a frontier model can outperform most PCP visits for ambiguous multi-system symptoms. Models surfaced nearly all the same hypotheses as her specialist's NP and flagged the same niche ACTH stimulation test. She has been symptom-free for one month.

## Influenced pages

- [use-cases/ai-personal-health-investigation](../../use-cases/ai-personal-health-investigation.md) — new page, full process documentation
- [state-of/healthcare](../../state-of/healthcare.md) — new "Patient-side AI" subcategory entry

## Key claims extracted

- Frontier models (Claude Opus 4.8, GPT 5.5) + structured process can outperform most PCP visits for ambiguous symptoms
- Models raised ~5/6 hypotheses the specialist NP offered; flagged the same niche ACTH stimulation test
- Always use reasoning models with high thinking effort for health work
- Coding agents (Claude Code, Codex) are superior for complex data (CT/MRI, Garmin exports, planning mode for unknown-unknowns)
- Most people have a significant "elicitation gap" — don't know how to use models for health effectively
- ChatGPT and Claude not HIPAA-compliant by default; users can opt out of training
- Published plug-and-play system prompt and Claude Code/Codex skill on GitHub
````

## Schema / vocabulary additions

- [x] No new schema additions required — `healthcare` domain and `agentic` tag already exist; `use-case` type doesn't require a subcategory.

## Open questions

- The "Patient-side AI" section in state-of/healthcare.md lists no specific tool (it references a use-case pattern with general-purpose models). Is that the right home, or should it stay purely in use-cases with no state-of update?
	- We can leave it as is
