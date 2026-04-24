---
type: proposal
source: raw/deep-research/2026-04-23 Agents Evals.md
status: applied
created: 2026-04-24
---

# Proposal: Evals for agentic software development (training page)

## Summary

There is no training page in the wiki on how to evaluate coding agents. This proposal creates one covering the layered eval stack, task-specific patterns across nine coding task types, the Minimum Viable Eval Suite, shadow mode, LLM-as-judge for code review, and how to convert real bugs/PRs into test cases. The Ramp "Inspect" case study grounds the guidance in a real production deployment.

The high-level architecture (deterministic gates first, then AI-specific evals) is well-grounded. The nine task-specific patterns vary: issue fixing, test generation, CI repair, and shadow mode are solid; Agentform and "Root Repos" are lightly sourced and are hedged accordingly.

## Intended changes

- [x] **Create** `wiki/training/evals-for-agentic-software-development.md` — new training page
    > See draft below

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add link in Current guidance and See also
    > **Add bullet in `## Current guidance`:**
    > `- Design an explicit eval suite before granting a coding agent permission to open PRs autonomously — see [[training/evals-for-agentic-software-development]]`
    >
    > **Add to end of file (before Sources):**
    > ```
    > ## See also
    >
    > - [[training/evals-for-agentic-software-development]] — eval stack for coding agents: MVES, task-specific patterns, shadow mode, trace mining
    > ```
    > *(If a See also section already exists, add the line there.)*

- [x] **Update** `wiki/index.md` — add entry under Training
    > **Add under Training:**
    > `- [[training/evals-for-agentic-software-development]] — eval stack for coding agents: deterministic gates, task-specific patterns, MVES, shadow mode, trace mining *(as_of: 2026-04-23)*`

## Page drafts

### wiki/training/evals-for-agentic-software-development.md (new)

````md
---
title: Evals for agentic software development
type: training
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Evals for agentic software development

Coding agents produce output that looks correct before it compiles, runs, or lands in a shared codebase. Without a structured eval suite, the default quality signal is "it seemed fine when I ran it" — which misses regressions, security issues, inefficient trajectories, and silent scope violations. An eval suite is not the same as a test suite: evals measure agent behavior across tasks over time, not just whether one patch passes today.

## Current guidance

- Run deterministic gates (CI, linters, type-checkers, unit tests) before any AI-specific eval. AI evals only proceed after hard gates pass.
- Define a Minimum Viable Eval Suite before granting a coding agent permission to open PRs autonomously.
- Different coding tasks require different eval patterns — a blanket strategy misses failures specific to each task type.
- Use shadow mode to evaluate agents safely against live production data before enabling real commits.
- Convert real bugs, PR comments, and postmortems into test cases systematically, not ad hoc.
- Use LLM-as-judge for qualitative code review (style, architecture, security anti-patterns) only after deterministic gates pass.
- Set cost and latency thresholds as hard limits to catch runaway recursive loops before they damage production.

## Layered eval stack

**Layer 1 — Deterministic gates (always first):**
Static analysis, type checkers (MyPy, TypeScript compiler), linters, and existing unit/integration tests. If any fail, the agent's trajectory is interrupted and the error logs are fed back for self-correction. This layer catches a large category of failures cheaply and reliably before any expensive AI-specific evaluation runs.

**Layer 2 — AI-specific evals by task type:**
Qualitative and trajectory-based evals that run only after Layer 1 passes. What these look like depends heavily on the specific coding task (see below).

**Layer 3 — Online monitoring:**
Asynchronous scoring of production traces to detect drift, cost spikes, or trajectory degradation in live deployments. This feeds the trace mining loop (see Proven patterns).

## Minimum Viable Eval Suite (MVES)

A practical starting point for teams deploying a coding agent that will open real PRs:

1. **Baseline deterministic tests** — the agent's output must compile, pass existing unit tests, and pass the syntax formatter
2. **File system impact checks** — verify the agent did not touch files outside its stated scope (e.g., core config manifests, unrelated modules)
3. **Cost and latency thresholds** — hard limits on token consumption and wall-clock time per task to prevent runaway loops
4. **LLM-as-judge for code review** — a capable secondary model prompted with a specific rubric (style guide, security anti-patterns, readability) to grade the output; useful for things unit tests cannot catch

As the agent matures: add visual regression checks for frontend changes (before/after screenshots), dynamic test generation (agent writes a failing test before writing the fix), and multi-repo impact checks.

## Task-specific eval patterns

A single evaluation strategy does not work across all coding tasks. Each task type has its own failure modes and signals:

| Task | Primary eval approach | Key failure mode to catch |
|---|---|---|
| Issue fixing | Trajectory check: did the agent localize the right code region before generating a fix? | Fix applied to the wrong location |
| Feature implementation | Scope check: did the agent touch only in-scope files? (Spec-Driven Development validation) | Silent scope creep |
| Refactoring | Structural integrity: does compilation succeed across all affected repos after mass changes? | Dependency breakage at scale |
| Test generation | Coverage metrics + edge-case coverage: are both standard paths and edge cases included? | Tests that pass trivially but miss real edge cases |
| Code review | Stacked tool evaluation: surface logic → deep static analysis → LLM architectural review | Shallow review missing deep bugs |
| Security review | Adversarial injection: does the agent detect prompt injection attempts? Does it integrate with vulnerability scanners? | Passing obviously insecure code |
| Dependency updates | File system impact check: did the agent only touch what it was supposed to? | Accidental modification of unrelated configs |
| Migration tasks | Multi-repo context check: did the agent maintain execution context across shared libraries without breaking changes? | Partial migration leaving inconsistent state |
| CI failure repair | Step efficiency check: did the agent resolve the issue without entering a runaway recursive loop? | Infinite retry loop on unfixable failures |

## Shadow mode

Shadow mode is the safest way to evaluate a capable coding agent on live production data. The agent operates in parallel with human engineers — proposing solutions, detailing what it *would* do — but is blocked from committing changes or executing destructive commands.

**Ramp "Inspect" case study:** Ramp's internal coding agent (Inspect) now initiates over 50% of merged PRs. Ramp runs it in isolated Modal VMs with a full-stack local environment (Postgres, Redis, Temporal, plus Sentry and Datadog for observability). In shadow mode, the eval marks success when the agent's proposed resolution matches the human-implemented fix and passes all sandbox tests. This sandbox-driven evaluation loop closes the "verification gap" that plagues standard AI coding assistants.

The shadow mode pattern is most useful when:
- The agent is capable enough to produce meaningful proposals but not yet trusted to commit
- You want to benchmark agent performance against historical human decisions
- You need to build a dataset of ground-truth agent behavior before switching to autonomous mode

## Converting real artifacts into eval cases

Production artifacts (bug reports, PR review comments, postmortems) are the highest-quality source of eval cases because they reflect real failures, not synthetic ones. A systematic pipeline:

1. **Ingest** the artifact (bug ticket, PR comment) and extract the core failure intent
2. **Define the golden state** — the exact patch or trajectory a human expert used to resolve it
3. **Write deterministic assertions** — hard-coded checks on output format, required fields, specific API calls
4. **Set trajectory boundaries** — max step count, token budget, allowed tools
5. **Convert to a dataset row** — observability tools (Braintrust, LangSmith) support "one-click" trace-to-dataset conversion
6. **Wire into CI/CD** — run the new eval case automatically to block merges if performance drops below threshold

When a production incident occurs, it should always yield a regression test. Use an LLM to generate synthetic variations of the failing interaction so the agent learns the underlying principle, not just the specific case.

## LLM-as-judge for code review

For qualitative review signals (readability, architectural coherence, security anti-patterns) that unit tests cannot catch, a capable secondary model can grade the primary agent's output. To prevent judge drift:

- **Calibrated rubrics** — instead of "is this code good?", specify: "Score 1 if the PR modifies only files within the stated feature scope. Score 0 if it touches unrelated modules."
- **Reference answers** — when a golden solution exists, give the judge the known-correct version to compare against
- **Human audits** — periodically sample 5–10% of LLM-judged evals for manual review; measure Inter-Rater Agreement (IRA) to detect when the judge has drifted

Observability platforms (Braintrust, Promptfoo, Langfuse) support trace ingestion and assertion-based grading. A concrete example: a `skill-used` assertion in Promptfoo can verify that the agent routed a query to the SQL tool rather than hallucinating data from its weights — grading internal reasoning, not just the final output.

## Proven patterns

- **Deterministic gates first, always.** AI-specific evals are expensive and noisy. Let cheap deterministic checks filter obvious failures before any LLM-as-judge or trajectory eval runs.
- **Shadow mode before autonomous mode.** Evaluate on real production data before granting commit rights.
- **Scope assertions as a category.** Did the agent touch files it wasn't supposed to? This is one of the most important and most commonly missed checks.
- **Incident-to-regression pipeline.** Every production failure should produce a new eval case. Without this, the eval suite drifts out of sync with real failure modes.
- **Red/green TDD for agent-written tests.** Prompt the agent to write a failing test first, then write the implementation to make it pass. The five-word prompt "use red/green TDD" encodes this workflow because agents recognize the jargon.

## Failure modes

- Skipping the MVES because "the agent seems to work" — without measurable eval coverage, there is no signal when behavior regresses
- Treating a high pass rate on a static test suite as proof of production readiness — the suite may have overfit to cases developers have already seen
- Running AI-specific evals before deterministic gates — wastes compute and produces noisy signal
- Shadow mode without a feedback loop — shadow proposals that don't convert into training data or eval cases add cost without compounding value

## Evidence from practice

- Ramp: Inspect coding agent initiates >50% of merged PRs; runs in isolated Modal VMs with full-stack environment; shadow mode + sandbox validation is the core safety mechanism
- Shopify (April 2026): built an internal PR review tool specifically because external tools do not spend enough compute on expensive models during review — review quality, not code generation, is the current frontier bottleneck
- See [[training/ai-enablement-software-development]] for broader Shopify and Ramp adoption patterns

## Open questions

- What is the right threshold for promoting a coding agent from shadow mode to autonomous mode? The research report suggests pass^k thresholds (e.g., 95% over 100 consecutive traces) but these specific numbers are report-normalized and should be calibrated per organization.
- How do you maintain eval suite coverage when the agent's task distribution shifts over time?

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
- [[sources/articles/ramp-ai-adoption-playbook]]
- [[sources/newsletters/shopify-latent-space-april-2026]]
````

## Open questions

- The `ai-enablement-software-development.md` page already mentions Ramp and Shopify; the new page adds a focused eval angle rather than duplicating adoption guidance.
	- Looks good.
- The task-specific patterns table hedges "Root Repos" and "Agentform" by not linking to tool pages — those specific tools need verification before wiki promotion.
	- ok
