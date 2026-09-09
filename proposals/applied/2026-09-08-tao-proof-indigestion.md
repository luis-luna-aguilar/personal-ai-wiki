---
type: proposal
source: raw/newsletters/2026-08-30-our-agents-ourselves.md
status: pending
created: 2026-09-08
---

# Proposal: Terence Tao on "proof indigestion"

## Summary

### The source

Every's Context Window newsletter (2026-08-30) summarizes a new problem Fields Medalist Terence Tao describes on his own blog: AI systems are now producing more apparently-correct mathematical proofs than the mathematics community has the bandwidth to verify or explain. Tao calls this "proof indigestion." His worked example: an AI-generated proof of Sendov's conjecture — a longstanding open problem about the roots of polynomials — formalized in Lean (software that machine-verifies mathematical proofs) by researcher Lech Mazur. The proof passed verification across all 90,000 lines, but was barely comprehensible to a human. Tao spent several days working through it with AI assistance, pen, and paper, and extracted the core idea into a roughly 15,000-line version he calls "remarkably elementary" for a problem that had resisted expert mathematicians for decades. His broader point: turning an AI-generated proof into something another human can understand, explain, and build on — not finding the proof in the first place — may become the primary human job in mathematics going forward.

### What changes

`trends/ai-in-mathematics.md` already tracks OpenAI's Erdős disproof and Anthropic's Riemann Hypothesis bound as the trend's two headline results. This proposal adds Tao's "proof indigestion" observation as a third, distinctly different kind of signal — not a new result, but a new bottleneck in how results get consumed — as a new Current-status bullet and Recent-changes entry, bumping `as_of` to 2026-08-30 (the date closest to the source's own dating; Tao's original post is dated 2026-08-12, but this proposal uses the newsletter's coverage date since that's the source actually being ingested).

### What to weigh

The `as_of` date choice is worth noting: Tao's own blog post is dated 2026-08-12, ahead of Every's 2026-08-30 coverage of it. Per the wiki's date rule, `as_of` should reflect the source's own publication date when available — this proposal uses 2026-08-12 (Tao's post date) rather than the newsletter's relay date, since that's the actual date of record for the claim. (See the corrected `as_of` in the draft below.)

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/ai-in-mathematics.md` — add "proof indigestion" bullet, bump `as_of`, add Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-our-agents-ourselves-2026-08-30.md` — source summary

## Page drafts

### wiki/trends/ai-in-mathematics.md (updated)

```md
---
as_of: 2026-08-12
sources: [openai-erdos-unit-distance-2026-05, anthropic-riemann-hypothesis-2026-08-11, every-our-agents-ourselves-2026-08-30]
---

## Current status (as of 2026-08-12)

(... existing bullets unchanged ...)

- **Terence Tao names a verification bottleneck: "proof indigestion" (2026-08-12):** Tao describes AI systems now producing more apparently-correct proofs than mathematicians can verify or explain. His worked example: an AI-generated, Lean-formalized proof of Sendov's conjecture (a longstanding polynomial-roots problem) that machine-verified across all 90,000 lines but was barely comprehensible to a human. Tao spent several days extracting the core idea with AI assistance into a ~15,000-line version he calls "remarkably elementary" for a problem that had resisted experts for decades. His framing: turning an AI-generated proof into something a human can understand, explain, and build on — not finding the proof — may become mathematics' primary human task going forward. Distinct from the Erdős and Riemann results above: this is not a new result, but a new bottleneck in how results get consumed.

## Why it matters

(... existing paragraph unchanged; append: ...) Tao's "proof indigestion" observation adds a third dimension to watch alongside the verification-gap point above: even a fully machine-verified proof can still be a bottleneck if no human can extract and communicate its reasoning.

## Recent changes

- [2026-08-12] Terence Tao names "proof indigestion": AI-generated proofs (his worked example: a 90,000-line Lean-verified proof of Sendov's conjecture) are outpacing the field's capacity to extract and communicate their reasoning, not just to generate results.
- (... existing entries follow ...)
```

### wiki/sources/newsletters/every-our-agents-ourselves-2026-08-30.md (new)

```md
---
title: "Our Agents, Ourselves"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-30-our-agents-ourselves.md
url: https://every.to/context-window/our-agents-ourselves
published: 2026-08-30
ingested: 2026-09-08
domains: [science]
---

# Our Agents, Ourselves

Every's Context Window roundup covering Terence Tao's "proof indigestion" observation on AI-generated mathematical proofs outpacing human verification capacity, alongside teasers for other Every posts (cloning coworkers, a writing-model review, executive Q&A).

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — "proof indigestion" bullet

## Key claims extracted

- Tao: AI is generating more apparently-correct math proofs than mathematicians can verify or explain ("proof indigestion")
- Worked example: AI-generated, Lean-formalized proof of Sendov's conjecture, 90,000 lines, machine-verified but barely human-comprehensible
- Tao's own ~15,000-line extracted version: "remarkably elementary" for a problem that resisted experts for decades
- Framing: extracting/communicating AI-found proofs, not finding them, may become mathematicians' primary job
```
