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
