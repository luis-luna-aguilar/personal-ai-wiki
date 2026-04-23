---
type: proposal
sources:
  - raw/newsletters/2026-04-23-ainews-tasteful-tokenmaxxing.md
  - raw/newsletters/2026-04-23-anthropics-unreleased-model-got-hacked.md
status: pending
created: 2026-04-23
---

# Proposal: Tokenmaxxing — Tasteful vs. Wasteful

## Summary
The tokenmaxxing debate matured with new voices this week. AIE Miami leadership conversations and the AINews "Tasteful Tokenmaxxing" issue add: Jensen Huang's "deeply alarmed" quote, Reid Hoffman's middle-ground framing, and Shopify CTO Parakhin's operational guidance (depth/serial loops > breadth/parallel runs). The wiki's company-wide-ai-enablement page already has a tokenmaxxing failure-mode entry; this proposal expands it with the new voices and adds a nuanced "proven pattern" entry for the depth-vs-breadth heuristic.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — expand the Tokenmaxxing failure mode entry with new quotes; add "Tasteful tokenmaxxing" to Proven patterns

*Note: Source pages `ainews-2026-04-23.md` and `superhuman-2026-04-23.md` are created in proposals `2026-04-23-qwen-3-6-27b.md` and `2026-04-23-openai-workspace-agents.md` respectively.*

## Page drafts

### wiki/training/company-wide-ai-enablement.md (update — diff only)

> **Before** (Failure modes — Tokenmaxxing entry):
> ```
> - **Tokenmaxxing — measuring token spend as a productivity proxy.** Meta's internal "Claudeonomics" leaderboard ranked 85,000 employees by AI token usage; within weeks employees were leaving agents idle to climb the rankings. One OpenAI engineer processed 210 billion tokens in a single week (enough to fill Wikipedia 33 times). Dubbed "tokenmaxxing," this mirrors the early 2000s lines-of-code mistake exactly. Reasoning models compound the problem by generating inner-monologue tokens as a function of architecture, not work done. Reward outcomes and quality; token spend is a cost center, not a productivity signal.
> ```
>
> **After:**
> ```
> - **Tokenmaxxing — measuring token spend as a productivity proxy.** Meta's internal "Claudeonomics" leaderboard ranked 85,000 employees by AI token usage; within weeks employees were leaving agents idle to climb the rankings. One OpenAI engineer processed 210 billion tokens in a single week (enough to fill Wikipedia 33 times). Dubbed "tokenmaxxing," this mirrors the early 2000s lines-of-code mistake exactly. Reasoning models compound the problem by generating inner-monologue tokens as a function of architecture, not work done. Jensen Huang publicly said he'd be "deeply alarmed" if engineers weren't burning tokens worth half their annual salary — amplifying the leaderboard pressure. Reward outcomes and quality; token spend is a cost center, not a productivity signal. (See also: "Tasteful tokenmaxxing" in Proven patterns for the emerging middle-ground guidance.)
> ```

> **Add to `## Proven patterns` section (append new entry):**
> ```markdown
> - **Tasteful tokenmaxxing: depth over breadth.** The emerging leadership consensus (AIE Miami, April 2026) is not "burn more tokens" or "burn fewer tokens" but *how* you burn them. Shopify CTO Mikhail Parakhin: prefer serial autoresearch loops (depth) over kicking off 5, 10, 50 parallel LLM runs (breadth). Reid Hoffman's middle ground: track how people use AI, not just how much — team-wide experimentation plus regular check-ins to surface what's actually working. Dex Horthy (coiner of "Context Engineering") publicly retracted his earlier vibe-coding-only stance and encouraged engineers to read the code. The practical signal: measure the *quality* of token use, not the quantity.
> ```

> **Update `sources` frontmatter** to add: `ainews-2026-04-23, superhuman-2026-04-23`

> **Update `as_of`:** `as_of: 2026-04-23`
