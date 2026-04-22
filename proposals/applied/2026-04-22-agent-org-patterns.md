---
type: proposal
sources:
  - raw/newsletters/2026-04-22-youre-the-bread-in-the-ai-sandwich.md
  - raw/newsletters/2026-04-21-the-ai-coding-race-is-heating-up.md
status: pending
created: 2026-04-22
---

# Proposal: Agent org patterns — trust batteries, AI sandwich, tokenmaxxing

## Summary

Two signals from April 21-22 that both speak to the same underlying question: how organizations should structure AI use and measure it. (1) Every's "AI sandwich" and Claudie trust-battery pattern provides concrete architectural templates for agentic org design. (2) Meta's Claudeonomics leaderboard and the "tokenmaxxing" phenomenon shows what happens when the wrong metrics get institutionalized. Both update trends/agents-reshape-organizations and training/company-wide-ai-enablement.

## Intended changes

- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add trust battery pattern and AI sandwich architecture to Concrete signals; add org architecture prediction
    > **Append to `## Concrete signals`:**
    > ```
    > - **Trust batteries as a concrete autonomy-granting mechanism.** Every's reporting on Claudie (Every's internal AI employee) documents a "trust battery" model for agentic autonomy: a judge agent reviews Claudie's interactions nightly, adjusts a trust percentage, and Claudie self-updates her memory and behavior from negative feedback. Claudie started at 20% trust (vs 50% for human new hires) and earns higher autonomy over time. The trust battery is wired to observable behavior, not time-based promotion — a reusable design for any agent that needs to earn scope gradually.
    > - **The AI sandwich as a practical org architecture template.** Framing from Every's Dan Shipper: humans do the planning (framing the problem) and the review (taste and judgment), while AI does the execution in the middle. The human role is not eliminated — it moves to the two ends that require authentic intent and independent evaluation.
    > - **Org architecture prediction: two models will coexist, one will lose.** Dan Shipper's forecast: (a) personal AI assistants with rich, maintained relationships will work well for high-trust, customizable tasks; (b) company-wide super-agents with department plugins will win for low-maintenance, lower-customization use cases. A third model — fleets of single-purpose agents — is predicted to lose because they require high maintenance without the relationship depth that makes personal assistants valuable.
    > ```
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added trust-battery pattern (Claudie/Every) and AI sandwich org architecture; Dan Shipper prediction: two org models coexist, single-purpose fleet loses
    > ```

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add trust battery as a proven pattern; add tokenmaxxing as a failure mode
    > **Append to `## Proven patterns`:**
    > ```
    > - **Trust battery with judge agent.** Grant autonomy incrementally rather than all at once. Implement a nightly judge agent that reviews interactions, scores behavior, adjusts a trust percentage, and lets the primary agent self-update memory from negative feedback. Start at a deliberately low trust level (Every's Claudie: 20% vs 50% for human new hires) and let the agent earn scope through demonstrated reliability rather than through time or configuration changes.
    > ```
    >
    > **Append to `## Failure modes`:**
    > ```
    > - **Tokenmaxxing — measuring token spend as a productivity proxy.** Meta's internal "Claudeonomics" leaderboard ranked 85,000 employees by AI token usage; within weeks employees were leaving agents idle to climb the rankings. One OpenAI engineer processed 210 billion tokens in a single week (enough to fill Wikipedia 33 times). Dubbed "tokenmaxxing," this mirrors the early 2000s lines-of-code mistake exactly. Reasoning models compound the problem by generating inner-monologue tokens as a function of architecture, not work done. Reward outcomes and quality; token spend is a cost center, not a productivity signal.
    > ```

- [x] **Create** `wiki/sources/newsletters/every-ai-sandwich-april-2026.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/newsletters/every-ai-sandwich-april-2026.md (new)

````md
---
title: Every — "You're the Bread in the AI Sandwich" (April 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-22-youre-the-bread-in-the-ai-sandwich.md
url: https://every.to/context-window/you-re-the-bread-in-the-ai-sandwich
published: 2026-04-22
ingested: 2026-04-22
domains: [agents]
---

# Every — "You're the Bread in the AI Sandwich" (April 2026)

Every's Context Window newsletter from Dan Shipper. Introduces the AI sandwich org architecture (human planning → AI execution → human review), documents Claudie's trust battery system, and predicts two agentic org models will coexist while single-purpose agent fleets lose.

## Influenced pages

- [[trends/agents-reshape-organizations]] — trust battery, AI sandwich, org architecture prediction
- [[training/company-wide-ai-enablement]] — trust battery as proven pattern

## Key claims extracted

- AI sandwich: humans do planning + review (both ends), AI does execution (middle)
- Claudie trust battery: judge agent reviews nightly, adjusts trust %; started at 20% vs 50% for human new hires
- Two coexisting org models: (a) personal AI assistants (rich relationship, requires maintenance); (b) company-wide super-agents + dept plugins (lower maintenance)
- Predicted loser: fleet of single-purpose agents (high maintenance, no relationship depth)
````
