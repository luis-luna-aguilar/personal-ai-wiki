---
type: proposal
source: raw/tweets/2026-10-14-alexlavaee-2110521585623003572.md
status: pending
created: 2026-10-14
---

# Proposal: Alex Lavaee — "Agents Write the Code. Your System Has to Prove It."

## Summary

### In short
An agent saying "done" is only a claim. Work is done when checks the agent didn't write and can't change pass, and their output is saved. So tests take expected values from the acceptance criteria, never from running the new code, or they agree with the bug. Read the test diff first, block test edits in CI rather than in prompts, review in a fresh session, and combine judges with a mean plus a veto, since requiring five to agree rejects about 41% of good changes. Updates two eval and review pages. Hesitate: the evals page goes over its length limit.

[[#Open questions|Open questions: 2 to answer.]]

### The source
Alex Lavaee, who builds Atomic (an open-source coding-agent runtime forked from Pi), published a long X Article on 14 October that collects a series of his threads and a livestream on The Neuron. His thesis: when a coding agent says it is done, that is only a claim. Work is done when checks the agent didn't write and can't change show the acceptance criteria are met, and the output of those checks is saved. He opens with a familiar failure. CI goes green, and two days later the bug is back because the agent quietly changed an assertion to expect the wrong value.

He frames verification as a pyramid. At the base is an acceptance contract a person reviews before any code exists, then types and lint, unit tests, integration tests against real services, end-to-end tests, and a thin model judge on top. His key rules: tests must take their expected values from the criteria, not from running the new code, because LLM-written tests tend to encode what the code does rather than what it should do. Favour checks that are hard to game, such as property-based and mutation tests. Review from a fresh session that never saw the implementer's reasoning. Score with several judges using a mean plus a veto, since requiring all five judges to agree would bounce about 41% of good changes. He admits verification at scale is still unsolved.

### What changes
The wiki's eval page for coding agents already says to run deterministic gates first, use LLM judges with rubrics, and capture browser proof artifacts. It says nothing on where test expectations come from, which checks are hard to game, or how to combine several judges.

- **Evals for agentic software development** gains four guidance bullets (contract first, expectations from criteria, test diff first, deterministic blocking of test edits). It also gets a new "Oracles agents can't game" section, a multi-judge scoring paragraph in the LLM-as-judge section, a scenario-and-performance paragraph in browser verification, two failure modes and a Recent-changes line. Page date moves to 14 October.
- **AI PR and code review** gains a guidance bullet on fresh-session review (criteria before diff, two-reviewer quorum, capped rounds) and a "self-review" failure mode. Page date moves to 14 October.
- One new source page.

### What to weigh
The claim about how LLM-written tests set their expected values rests on two papers the article links, which were not read directly. The eval page is already about 2,400 body words. These additions of about 350 words push it past the 2,500-word limit for training pages, so the open questions offer a split.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/evals-for-agentic-software-development.md` — guidance bullets, new Oracles section, LLM-as-judge and browser additions, failure modes, one Recent-changes entry dated 2026-10-14, source id + link, `as_of` → 2026-10-14

- [ ] **Update** `wiki/workflows/ai-pr-code-review.md` — one guidance bullet, one failure mode, one Recent-changes entry dated 2026-10-14, source id + link, `as_of` → 2026-10-14

- [ ] **Update** `wiki/index.md` — as_of on both lines → 2026-10-14; append "test oracles, multi-judge scoring" to the evals page description

- [ ] **Create** `wiki/sources/tweets/lavaee-verification-pyramid-2026-10.md` — source summary

## Page drafts

### wiki/training/evals-for-agentic-software-development.md (updated)

Frontmatter: append `lavaee-verification-pyramid-2026-10` to `sources:`; `as_of: 2026-10-14`.

`## Current guidance` — append four bullets:

```
- Write the acceptance contract before the code: who acts, the starting state, the action, the checkable result on screen and in stored state, a numeric threshold where one applies, the oracle that checks it, and which dependencies must be real. A person reviews it before the agent starts.
- Take expected values from the criteria or a reference, never from running the new code. LLM-written tests tend to encode what the code does rather than what it should do, so a test whose expectation came from the implementation agrees with the bug.
- Read the test diff before the implementation diff. A weakened assertion, deleted case, or newly mocked dependency makes a green check meaningless.
- Block fixes that edit, skip, or delete a failing test with a hook or CI check, not a prompt rule, so "green" can't come from moving the goalposts.
```

New section, inserted after `## Layered eval stack`:

```
## Oracles agents can't game

An oracle is whatever decides pass/fail against something trusted. Fixed example asserts are the easiest for an agent to satisfy without being right. Harder to game:

- **Property-based tests** check an invariant over thousands of generated inputs ("output is always sorted").
- **Metamorphic tests** compare related runs (same inputs at 30 and 120 FPS must give the same outcome).
- **Differential tests** run old vs new, or yours vs a reference, on the same input.
- **Mutation tests** plant small faults; if tests still pass, they aren't testing what you think.
- **Approved snapshots** change only when a person approves the new snapshot.
- **Invariants and contracts** check pre/post-conditions on every run.
- **Seeded replays** re-run a recorded session deterministically.

The agent can write property tests; a person decides which matter. Treat coverage as a record of what ran, not of what was checked.
```

`## LLM-as-judge for code review` — append paragraph:

```
**Combining several judges.** Use the judge only for what code can't check, after deterministic gates. Give it a checklist with defined score meanings (e.g. 1 = broken, 20 = proven with evidence), and a fresh judge per item so a strong item can't lift a weak one. Average the scores but let any single confident "broken" veto the result. Unanimity sounds stricter but backfires: if each of K judges wrongly rejects a good change 10% of the time, a correct change is bounced 1 − 0.9^K of the time, about 41% at K = 5. Each extra judge is more model calls, so K is a budget choice. Before adding a judge, ask whether a test could check the thing instead.
```

`## Browser self-verification and proof artifacts` — append paragraph:

```
Write the user scenario in plain steps before the agent starts (log in → open settings → change X → see Y); that scenario is the test. Drive a real browser through it (e.g. Vercel Labs' agent-browser), assert against DOM and network requests rather than pixels alone, use a real test account, and rerun the same scenario after every repair. Performance claims need the same discipline: set the budget before the change (e.g. LCP under 2.5s on mobile), measure Core Web Vitals over several runs on main and on the branch, compare medians, and include a mobile viewport.
```

`## Failure modes` — append two bullets:

```
- Making an LLM verifier the foundation instead of the top layer — judges drift toward longer answers and whatever they read first, so checks get missed and regressions slip through
- Prompt-only guards on test integrity — an instruction not to suppress failing tests is not a runtime check; enforce it with a hook or CI step
```

`## Recent changes` — adds one entry at the top (list is at 3 of 10; no spill):

```
- [2026-10-14] Added Lavaee's verification-pyramid guidance: acceptance contract first, oracles agents can't game, test-diff-first review, multi-judge mean-plus-veto scoring, and scenario-driven browser and performance checks.
```

`## Sources` — append:

```
- [Agents Write the Code. Your System Has to Prove It. — Alex Lavaee](../sources/tweets/lavaee-verification-pyramid-2026-10.md)
```

### wiki/workflows/ai-pr-code-review.md (updated)

Frontmatter: append `lavaee-verification-pyramid-2026-10` to `sources:`; `as_of: 2026-10-14`.

`## Current guidance` — append one bullet:

```
- Review from a session that never saw the implementer's transcript, since a reviewer reading the implementer's reasoning tends to continue it. The reviewer picks its checks from the acceptance criteria before reading the diff, tags findings P0–P2, and approval is decided in code (e.g. two independent approvals, discarded if the same review lists a blocker), with a cap on review rounds and a hand-off to a person when it runs out. Before merge, map every change to the criterion it satisfies; a change that maps to nothing is scope creep.
```

`## Failure modes` — append one bullet:

```
- **Self-review:** "now review your changes" in the implementing session mostly produces agreement with itself.
```

`## Recent changes` — adds one entry at the top:

```
- [2026-10-14] Added fresh-session review guidance: criteria-first checks, P0–P2 findings, coded two-reviewer approval, capped review rounds, and change-to-criterion mapping.
```

`## Sources` — append:

```
- [Agents Write the Code. Your System Has to Prove It. — Alex Lavaee](../sources/tweets/lavaee-verification-pyramid-2026-10.md)
```

### wiki/index.md (updated)

```
- [workflows/ai-pr-code-review](workflows/ai-pr-code-review.md) — workflow for AI-assisted pull request analysis, code-review execution, historical PR replay, and understanding-preserving review artifacts *(as_of: 2026-10-14)*
- [training/evals-for-agentic-software-development](training/evals-for-agentic-software-development.md) — eval stack for coding agents: deterministic gates, sandboxed execution, historical PR replay, benchmark integrity, QA artifact capture, browser self-verification, MVES, trace mining, test oracles, and multi-judge scoring *(as_of: 2026-10-14)*
```

### wiki/sources/tweets/lavaee-verification-pyramid-2026-10.md (new)

```
---
title: 'Agents Write the Code. Your System Has to Prove It. — Alex Lavaee'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-14-alexlavaee-2110521585623003572.md
url: https://x.com/alexlavaee/status/2110521585623003572
published: 2026-10-14
ingested: 2026-10-14
domains: [coding, agents]
---

# Agents Write the Code. Your System Has to Prove It. — Alex Lavaee

X Article (also on alexlavaee.me) by the builder of Atomic, an open-source coding-agent runtime. Argues that an agent saying "done" is a claim, and done means checks the agent didn't write and can't change show the acceptance criteria are met, with the output saved. Lays out a verification pyramid: human-reviewed acceptance contract at the base, then types/lint, unit, integration against real services, end-to-end, and a thin model judge on top. Covers hard-to-game oracles, root-cause-first debugging, fresh-session review, multi-judge scoring, scenario-driven browser and performance checks, and small-blast-radius testing against real services. The author says verification at scale is still unsolved.

## Influenced pages
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — contract-first guidance, oracles section, multi-judge scoring, browser/performance checks
- [AI PR and code review](../../workflows/ai-pr-code-review.md) — fresh-session review, self-review failure mode

## Key claims extracted
- Done = checks the agent didn't write and can't change pass, with saved evidence
- Pyramid: acceptance contract → types/lint/static → unit → integration (real services) → E2E → thin model judge
- LLM test generators tend to write oracles capturing actual rather than expected behavior (cites Konstantinou et al.; Ruberto & Terragni)
- Hard-to-game oracles: property-based, metamorphic, differential, mutation, approved snapshots, invariants/contracts, seeded replays
- Read the test diff before the implementation diff; write tests one at a time
- Debugging: failing repro test first, separate debugger subagent, root cause as file:line + evidence, raw stack traces not summaries, block test-editing fixes via hook/CI
- Review: fresh session, criteria-first, P0–P2 tags, two-reviewer coded approval in Atomic's goal workflow, round cap (stop on same blocker 3 rounds running)
- Judges: per-item fresh judge, 1–20 scale, mean ≥14 accept with confident-failure veto; unanimity bounces ~41% of good changes at K=5 with 10% per-judge false-reject (arithmetic, not a measurement)
- Frontend: written user scenario, real browser (agent-browser), DOM/network asserts, real test account, rerun after every repair; Core Web Vitals medians main vs branch, budget set beforehand
- Real services in containers / dev environments, canary + test accounts, narrow agent CLI, human approval for fleet-wide commands
- Scale verification to the change; validation (are the criteria right?) stays with people
```

## Schema / vocabulary additions
None.

## Open questions
- Atomic (bastani-inc/atomic) and agent-browser (Vercel Labs) are named as implementations. Should either get a tool page? (Assumed no — mentioned inline only, no primary source read.)
	- No
- The eval page will cross the 2,500-word training-page ceiling after this. Should the oracles and judge-scoring material move into a separate page later?
	- Yes, we need to refactor this into more pages, but that should be part of these proposal changes.
