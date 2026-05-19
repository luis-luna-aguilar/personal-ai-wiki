---
type: proposal
source: raw/tweets/2026-05-18-addyosmani-2056078124346228860.md
status: pending
created: 2026-05-18
---

# Proposal: Cognitive debt + AI learning posture (Addy Osmani)

## Summary

Addy Osmani's essay "Don't Outsource the Learning" introduces "cognitive debt" — the accumulated skill erosion from using AI without learning intent. Cites three studies (Anthropic, MIT, anchoring) all converging on the same finding: pure delegation posture degrades comprehension even when AI output is correct. Remedies are posture shifts inside the same tools, not different tools.

## Intended changes

- [x] **Update** `wiki/training/anti-autopilot-review-friction.md` — update `as_of`, add source to frontmatter, add Cognitive debt concept + three studies + learning-posture prescriptions, add Recent changes section
    > **`as_of`:** `2026-05-13` → `2026-05-18`
    >
    > **Sources frontmatter:** add `osmani-cognitive-debt-ai-learning-2026-05`
    >
    > **Add new section `## Cognitive debt` after `## Proven patterns`:**
    >
    > ```md
    > ## Cognitive debt
    >
    > Cognitive debt (Addy Osmani, May 2026): the accumulated deficit in comprehension and skill that results from using AI to close tasks without understanding what was produced. "Silently trading future capability for present-day speed, and the tools won't force us to do otherwise." Distinct from hallucination risk: cognitive debt accrues even when the AI output is correct.
    >
    > **Three empirical studies:**
    >
    > - **Anthropic comprehension study:** Engineers learned a new Python library — half with AI assistance, half without. Both groups finished tasks at the same speed. But the AI group scored 50% on the follow-up comprehension quiz vs 67% for the manual group; the gap widened on debugging tasks. Within the AI group: engineers who used AI for conceptual questions scored above 65%; engineers who copy-pasted generated code scored under 40%. **Finding: the tool didn't determine the outcome — the posture did.**
    >
    > - **MIT brain-connectivity study:** Essay writing across LLM, search-engine, and brain-only groups. EEG showed brain connectivity scaling down with every layer of external support; LLM group showed weakest coupling. After writing, 83% of LLM users couldn't quote a single line of what they had just produced. Researchers called this "cognitive debt."
    >
    > - **Anchoring study:** When participants had LLM access at the *start* of a task, the LLM framed the entire problem — even when humans did the rest of the work themselves, initial anchoring produced measurably worse decisions. Order of operations mattered more than total amount of AI used. Implication: defer AI until after you've formed your own initial frame.
    >
    > **Learning-posture prescriptions:**
    > - Form a hypothesis before asking: write 2–3 sentences on what you think the problem is; use the model's answer to test your theory, not replace it
    > - Ask for explanation before code: in unfamiliar territory, first prompt = "explain how this works, alternatives, and tradeoffs" — request code only after grasping concepts
    > - Treat AI output like a PR from a junior engineer: read it, critique it, push back; don't merge just because tests pass
    > - Re-derive by hand occasionally: recreate code the model wrote — calibration check for what you've quietly lost
    > - Ask the model to teach: after it writes a clever function, ask what concepts it used and what you'd read to understand the design choice
    > ```
    >
    > **Add `## Recent changes` section (page currently has none):**
    >
    > ```md
    > ## Recent changes
    >
    > - [2026-05-18] Cognitive debt (Osmani): three empirical studies confirm AI-without-learning-intent erodes comprehension (Anthropic: 50% vs 67% quiz; MIT EEG: 83% couldn't quote own AI-written text; anchoring: AI at task start produces worse decisions); learning-posture remedies added
    > ```

- [x] **Create** `wiki/sources/tweets/osmani-cognitive-debt-ai-learning-2026-05.md`
    > See draft below

## Page drafts

### wiki/sources/tweets/osmani-cognitive-debt-ai-learning-2026-05.md (new)

```md
---
title: '"Don''t Outsource the Learning" — Addy Osmani'
type: source
source_type: tweet
source_file: raw/tweets/2026-05-18-addyosmani-2056078124346228860.md
url: https://x.com/addyosmani/status/2056078124346228860
published: 2026-05-18
ingested: 2026-05-18
domains: [training]
---

# "Don't Outsource the Learning" — Addy Osmani

Addy Osmani's essay on cognitive debt: the accumulated skill degradation from using AI without learning intent. Cites three convergent studies. (1) Anthropic comprehension study: both AI-assisted and manual engineers finished tasks at same speed, but AI group scored 50% vs 67% on comprehension quiz; the gap widened on debugging; within AI group, posture determined outcome (conceptual questions → 65%+, copy-paste → under 40%). (2) MIT brain-connectivity study: EEG showed LLM group had weakest brain coupling; 83% of LLM users couldn't quote a line of what they had just written; researchers coined "cognitive debt." (3) Anchoring study: having LLM access at task start framed the entire problem; initial anchoring produced measurably worse decisions even when humans did the rest of the work. Prescriptions: form hypothesis before asking, request explanation before code, treat AI output as a junior PR, re-derive by hand occasionally, ask model to teach after it writes.

## Influenced pages

- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — Cognitive debt concept and three studies added

## Key claims extracted

- Cognitive debt: skill erosion from pure delegation, even when AI output is correct
- Anthropic study: same speed, AI group 50% vs 67% on comprehension; posture determines outcome within AI group
- MIT: 83% of LLM users couldn't quote their own AI-written text; LLM group weakest brain connectivity
- Anchoring: AI at task start → measurably worse decisions; order of operations matters more than total AI use
- Posture prescriptions: hypothesis first, explanation before code, re-derive by hand, ask model to teach
```
