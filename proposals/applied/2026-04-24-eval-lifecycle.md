---
type: proposal
source: raw/deep-research/2026-04-23 Agents Evals.md
status: applied
created: 2026-04-24
---

# Proposal: Eval lifecycle expansion — agent-improvement-loop update

## Summary

The `agent-improvement-loop.md` concept page covers trace collection and improvement iteration well, but is missing the practical eval suite hygiene that prevents the suite itself from becoming a liability: holdout sets, continuous trace mining from production incidents, periodic refresh, and retiring stale tests. The research report's coverage of this is the most synthesis-light section — these are standard eval engineering practices. This proposal adds them to the existing page as a new section.

## Intended changes

- [x] **Update** `wiki/concepts/agent-improvement-loop.md` — add `## Eval suite hygiene` section and one new `## Recent changes` entry; update `as_of` and `sources`
    > See diff below

## Diff

### wiki/concepts/agent-improvement-loop.md — new section

Add a new section after `## Self-improving skills` (before `## Caveats`):

````md
## Eval suite hygiene

An eval suite that isn't actively maintained will betray you. If you run the same 50 hand-authored test cases indefinitely, the agent optimizes for passing those exact cases — and starts failing on the real failure modes that didn't exist when the cases were written. The suite needs to evolve as fast as the agent and the environment do.

**Four practices that prevent eval rot:**

**1. Continuous trace mining.** Once an agent is deployed (even in shadow mode), monitor production logs actively. When a user reports a bad response, or when the agent triggers an error, extract that execution trace, anonymize it, and convert it into a new test case. Production failures are more valuable than synthetic cases because they reflect real failure modes, not imagined ones.

When a production incident occurs — say, an agent approved an action that violated a policy — that incident must yield a regression test. Prompt an LLM to generate 10 synthetic variations of the failing interaction so the agent learns the underlying principle, not just the specific case.

**2. Hidden holdout sets.** Maintain a separate set of eval cases that the development team cannot see during normal work. Periodically test against this blind holdout to get an unbiased measure of generalization. If you only test on cases that developers have seen, you're measuring memorization, not capability.

This applies in both directions: don't let holdout cases leak into training data, and don't let eval designers look at holdout cases when writing new ones.

**3. Periodic refresh.** The environment changes. APIs are updated. Company policies change. Support ticket formats shift. Eval cases built against deprecated documentation will falsely penalize a correct agent. Review and update cases regularly — weekly for fast-moving agent surfaces, monthly at minimum for stable ones.

**4. Retiring stale tests.** A test that achieves 100% pass rate for many consecutive model updates is no longer providing a useful signal. It's measuring something the agent has already mastered. Archive it and redirect compute to edge-case coverage and new failure modes instead.

**The meta-rule:** treat the eval suite as a product, not a one-time artifact. It has a maintenance burden, it goes stale, and it needs active curation to stay useful.
````

Add to `## Recent changes`:
- `[2026-04-24] Added eval suite hygiene section: holdout sets, trace mining, periodic refresh, and retiring stale tests`

Update frontmatter: `as_of: 2026-04-24`, add `agents-evals-deep-research` to sources.

## Open questions

- The "100% pass rate for six consecutive months" heuristic from the research report is intentionally omitted from the draft — it's a specific threshold that's likely calibrated to the report author's context. If the user wants a threshold example, add it with a clear "calibrate per your context" caveat.
- Should this also link to the new training pages (`evals-for-agentic-software-development` and `evals-for-agentic-work`) from Related? Probably yes once those pages are created.
	- Yes, please link them
