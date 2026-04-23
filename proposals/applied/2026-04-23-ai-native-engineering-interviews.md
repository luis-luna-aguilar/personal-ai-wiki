---
type: proposal
source: raw/newsletters/2026-04-23-openai-drops-a-privacy-focused-model.md
status: applied
created: 2026-04-23
---

# Proposal: AI is rewriting engineering interviews

## Summary
Multiple companies (Sierra, Augment Code, Karat) report that traditional coding interviews are now obsolete — Claude Code and Codex pass them trivially. The emerging replacement: two-hour, open-ended sessions where candidates use their AI of choice to build a real product, evaluated on product taste and architectural judgment rather than syntax recall. Directly relevant to the wiki's software development training coverage.

## Intended changes

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add a "Hiring AI-native engineers" section; prepend Recent changes entry if page has one (it currently does not have a Recent changes section); update as_of; add source

*Note: Source page `the-code-2026-04-23.md` is created in proposal `2026-04-23-qwen-3-6-27b.md`.*

## Page drafts

### wiki/training/ai-enablement-software-development.md (update — diff only)

> **Add new section before `## The junior talent problem`:**
> ```markdown
> ## Hiring AI-native engineers
>
> Traditional coding interviews became obsolete the moment Claude Code and Codex started passing them automatically. The failure mode: pre-LLM rubrics measure syntax recall and framework knowledge — things LLMs now handle in seconds. Karat, which has run 600,000+ interviews for Atlassian and PayPal, confirmed the shift is industry-wide.
>
> **What's replacing them:**
> - **Live AI-assisted builds.** Give candidates two hours, their AI of choice, and a real product to build. Sierra (founded by ex-Salesforce co-CEO Bret Taylor) published the most detailed write-up; Augment Code shipped a similar model in March 2026.
> - **Evaluate product taste and architectural judgment.** The real signal is what candidates build, what they prioritize, and why — not whether they remembered the right API syntax.
> - **Calibration is harder.** Open-ended interviews are more difficult to grade and often spark debrief debates. The payoff: hiring for standout strengths rather than filtering for absence of weaknesses.
>
> **Practical implications for teams:**
> - Update interview rubrics: move from "can they write code?" to "can they direct AI, make architectural calls, and ship something coherent?"
> - Invest in debrief calibration: reviewers need shared vocabulary for "good product taste" and "strong architectural judgment"
> - The shift is already happening at companies hiring at scale; waiting to update means your rubrics are testing AI proficiency, not engineering judgment
> ```

> **Update `sources` frontmatter** to add: `the-code-2026-04-23`

> **Update `as_of`:** `as_of: 2026-04-23`
