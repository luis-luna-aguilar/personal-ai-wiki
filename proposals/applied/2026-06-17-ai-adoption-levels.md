---
type: proposal
source: raw/newsletters/2026-06-07-ai-is-ready-organizations-arent.md
status: pending
created: 2026-06-17
---

# Proposal: 8 levels of AI adoption (Every/Mike Taylor)

## Summary

Every (via Mike Taylor and Laura Entis) published "The Eight Levels of AI Adoption" on June 7 — a practical framework mapping L1 (ask-and-answer chatbot) through L8 (orchestrator agent running a team of sub-agents), with sample prompts and signals for when to level up. Key insight: a higher level is not automatically better — the right level depends on how much you trust the AI and how costly a mistake would be. Companion piece: Natalia Quintero (Every Consulting, 100+ company interviews) published a 5-step 60-day executive implementation guide.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add 8-levels framework as a named Proven Pattern and the 5-step executive plan structure
    > See diff below

- [x] **Create** `wiki/sources/newsletters/every-ai-adoption-levels.md` — source summary
    > See draft below

## Page drafts

### wiki/training/company-wide-ai-enablement.md (diff)

Add a new `## AI adoption maturity model` section after `## Current guidance` (before `## Proven patterns`). Also add source entry and recent-changes entry.

**New section to insert:**
```md
## AI adoption maturity model

Every (Mike Taylor / Laura Entis, June 2026) published an 8-level framework for AI adoption maturity. Central insight: **higher level is not automatically better.** The right level depends on how much you trust the AI and how costly a mistake is.

| Level | Name | What the AI does |
|---|---|---|
| 1 | Chatbot | You ask, it answers. Single turn. No memory. |
| 2 | Conversational assistant | Multi-turn, context-aware. Still human-initiated every turn. |
| 3 | Tool user | AI calls external tools (search, calculator, APIs) inside a conversation. |
| 4 | Autonomous task executor | Completes multi-step tasks with minimal steering. Human reviews output. |
| 5 | Background agent | Runs unsupervised; triggers on schedule or event; reports results. |
| 6 | Goal-directed agent | Given an objective and constraints; plans and executes independently. |
| 7 | Multi-tool orchestrator | Combines tools, agents, and APIs across a pipeline to complete complex work. |
| 8 | Sub-agent orchestrator | Runs a team of specialized sub-agents under a master orchestrator. |

**Practical rules from the framework:**
- Match level to task risk and trust. High-stakes tasks with hard-to-verify outputs belong at lower levels with more human review.
- The signal to move up: consistent performance at the current level with no meaningful error rate — not just enthusiasm or capability.
- Levels 5-8 require investing in evals, verification, and guardrails before promotion.

**5-step executive implementation (Natalia Quintero, Every Consulting):**
1. Identify a high-ROI anchor workflow (narrow scope, measurable output, high volume)
2. Pick a tool and stand it up with SSO, pre-connected data, and a preconfigured agent surface
3. Run a 30-day internal pilot with a small self-selected group; surface wins publicly
4. Roll out with a visible social loop (demos, leaderboards, shared channels)
5. Expand to second and third workflows only after the first is stable and the social loop is active

Source: "AI Is Ready. Organizations Aren't." (Every, June 2026) — based on interviews with 100+ leadership teams.
```

**Update `## Recent changes` (add entry):**
> No existing Recent changes section visible in current page — if the page has one, prepend:
> `- [2026-06-07] Added 8-level AI adoption maturity model (Every/Mike Taylor) and 5-step executive plan (Natalia Quintero/Every Consulting); source: 100+ leadership team interviews`

**Update frontmatter sources list** (add `every-ai-adoption-levels`).

**Update `as_of` to 2026-06-17** (or keep current date if it's already 2026-06-17).

### wiki/sources/newsletters/every-ai-adoption-levels.md (new)

```md
---
title: '"AI Is Ready. Organizations Aren''t." — Every (June 7)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-07-ai-is-ready-organizations-arent.md
published: 2026-06-07
ingested: 2026-06-17
domains: []
---

# "AI Is Ready. Organizations Aren't." — Every (June 7)

Every weekly digest that surfaced two practical guides: Mike Taylor's 8-level AI adoption framework (with sample prompts and level-up signals) and Natalia Quintero's 5-step 60-day executive implementation plan. Quintero heads Every Consulting and bases the guide on interviews with 100+ leadership teams.

## Influenced pages
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — 8-level framework and 5-step plan added

## Key claims extracted
- 8 levels of AI adoption: L1 (chatbot) → L8 (orchestrator with sub-agents); higher is not automatically better
- Level selection depends on trust and cost of mistakes, not just capability
- Signal to level up: consistent performance at current level; build evals before promoting to L5+
- 5-step executive plan: anchor workflow → tool + SSO → 30-day pilot → social loop → expand
- "AI adoption is being held back by organizations, not the models" (Natalia Quintero)
```
