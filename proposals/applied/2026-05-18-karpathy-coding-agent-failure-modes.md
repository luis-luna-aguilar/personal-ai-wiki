---
type: proposal
source: raw/tweets/2026-05-18-technmak-2055712886790701226.md
status: pending
created: 2026-05-18
---

# Proposal: Karpathy coding-agent failure modes + CLAUDE.md remedy

## Summary

Andrej Karpathy articulated three failure modes in current coding agents that the community codified into a four-principle CLAUDE.md file. Core insight: give agents success criteria and let them loop — not instructions to execute step by step.

## Intended changes

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add Karpathy failure modes to Failure modes section; add success-criteria pattern; update `as_of` to `2026-05-18`; add source to frontmatter

    > **Add to Failure modes section** (alongside AI psychosis from the `ai-stack-fungibility` proposal):
    >
    > **Assumption runaway**
    > - Models "make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should." (Karpathy)
    > - Remedy: *think before coding* — state ambiguity explicitly, present multiple interpretations rather than silently picking one, stop and ask rather than guess
    >
    > **Over-engineering drift**
    > - Models "really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do." (Karpathy)
    > - Remedy: *simplicity first* — no features beyond what was asked, no abstractions for single-use code; test: would a senior engineer say this is overcomplicated?
    >
    > **Orthogonal side-effects**
    > - Models "sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task." (Karpathy)
    > - Remedy: *surgical changes* — don't improve adjacent code, match existing style, mention unrelated dead code rather than deleting it; every changed line must trace to the request
    >
    > **Add success-criteria pattern:**
    >
    > Transform "fix the bug" into "write a test that reproduces it, then make it pass." Transform "add validation" into "write tests for invalid inputs, then make them pass." Karpathy: "LLMs are exceptionally good at looping until they meet specific goals. Don't tell it what to do, give it success criteria and watch it go." This shifts the human role from directing steps → defining done.
    >
    > **Add to Recent changes:**
    > `- [2026-05-18] Karpathy failure modes: assumption runaway, over-engineering drift, orthogonal side-effects; success-criteria pattern: give agents verifiable done-conditions rather than step-by-step instructions`
    >
    > _Note: `proposals/2026-05-18-ai-stack-fungibility.md` also updates this page. Apply in either order._

- [ ] **Create** `wiki/sources/tweets/karpathy-coding-agent-failure-modes-2026-05.md`
    > See draft below

## Page drafts

### wiki/sources/tweets/karpathy-coding-agent-failure-modes-2026-05.md (new)

```md
---
title: Karpathy coding-agent failure modes + CLAUDE.md remedy — techNmak
type: source
source_type: tweet
source_file: raw/tweets/2026-05-18-technmak-2055712886790701226.md
url: https://x.com/techNmak/status/2055712886790701226
published: 2026-05-18
ingested: 2026-05-18
domains: [coding, training]
---

# Karpathy coding-agent failure modes + CLAUDE.md remedy — techNmak

TechNmak's summary of Andrej Karpathy's three critiques of current coding agents, paired with a community CLAUDE.md response. Karpathy's three failure modes: (1) assumption runaway — models run with wrong assumptions without checking or pushing back; (2) over-engineering drift — models overcomplicate code, bloat abstractions, ignore simplicity; (3) orthogonal side-effects — models change/remove code they don't fully understand as side effects of unrelated tasks. Community CLAUDE.md response: four principles — think before coding (state ambiguity), simplicity first (no unrequested features), surgical changes (every changed line traces to the request), goal-driven execution (give success criteria not steps). Karpathy's key insight: "LLMs are exceptionally good at looping until they meet specific goals. Don't tell it what to do, give it success criteria and watch it go."

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — Karpathy failure modes + success-criteria pattern

## Key claims extracted

- Assumption runaway: models don't seek clarifications, don't surface inconsistencies, don't push back
- Over-engineering drift: bloated abstractions, 1000 lines where 100 would do
- Orthogonal side-effects: modifying orthogonal code as side effects of a task
- CLAUDE.md remedy: think before coding, simplicity first, surgical changes, goal-driven execution
- Key insight: "Give agents success criteria and watch them loop" — shifts human role from directing steps to defining done
```
