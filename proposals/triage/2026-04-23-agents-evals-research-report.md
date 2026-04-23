---
type: triage
source: raw/deep-research/2026-04-23 Agents Evals.md
status: pending
---

# Triage: Agent Evals Research Report — 2026-04-23

## Signals

- [ ] **[agents]** Agent eval taxonomy, trajectories, and the harness boundary

    **What it is:** The report proposes a practical taxonomy for agent evaluation: capability, regression, trajectory, unit-level, and online evals, plus a framing that agents must be evaluated as `model + harness + tools + environment`, not as single-turn models.

    **Why it matters:** Strong fit for `wiki/concepts/harness.md` and `wiki/concepts/agent-improvement-loop.md`. Could also justify a new concept page on agent evals or task evals.

    **Source shape:** Mostly synthesis. The framing looks directionally strong, but the taxonomy and language are likely normalized by the report rather than copied from one canonical source.

    **Likely impact:** new concept page or major concept-page update; supports later training pages.
    **Verification:** verify before proposal using primary docs and stronger technical sources.
    **Recommended:** verify-first

- [ ] **[coding]** Evals for agentic software development

    **What it is:** A practical stack for coding-agent evaluation: deterministic gates first, then AI-specific evals; coding-task-specific eval patterns across issue fixing, implementation, refactoring, test generation, code review, security review, dependency updates, migration tasks, and CI repair; plus guidance on converting bugs, PR comments, and incidents into eval cases.

    **Why it matters:** This is the clearest gap in the wiki and the strongest candidate for a new `wiki/training/` page.

    **Source shape:** Mixed. The high-level architecture looks plausible and useful. Some specific named methods, tools, and pipelines may be over-compressed or weakly sourced.

    **Likely impact:** new training page `evals-for-agentic-software-development`; possible updates to `concepts/harness.md` and `concepts/agent-improvement-loop.md`.
    **Verification:** verify before proposal, especially named tools/frameworks and any task-specific prescriptions.
    **Recommended:** verify-first

- [ ] **[agents]** Autonomy ladder, escalation evals, and permission gating

    **What it is:** A staged autonomy model from read-only assistant to high/full autonomy, tied to eval evidence, escalation behavior, cost throttles, and permission boundaries.

    **Why it matters:** Strong fit for `wiki/training/company-wide-ai-enablement.md`, `wiki/training/anti-autopilot-review-friction.md`, and possibly a future evals concept page.

    **Source shape:** Useful as a managerial framing, but several named abstractions and thresholds look especially synthesis-heavy.

    **Likely impact:** updates to training pages; maybe folded into a broader evals concept rather than a standalone page.
    **Verification:** required before proposal. Do not trust `Authority Graph`, threshold examples, or governance language without stronger sources.
    **Recommended:** verify-first

- [ ] **[agents]** General task and workflow agent evals

    **What it is:** A parallel eval framework for non-coding agents covering email, scheduling, research, support, sales ops, finance, document review, and internal operations; includes task-specific metrics, simulated users, and policy-adherence concerns.

    **Why it matters:** Direct fit for a second training page on evals for normal business/knowledge-work agents.

    **Source shape:** Mixed but valuable. The task split is useful. Some metric names and frameworks may be vendor-specific or report-invented.

    **Likely impact:** new training page `evals-for-agentic-work`; updates to `company-wide-ai-enablement.md`.
    **Verification:** verify before proposal, especially metric names and enterprise-framework claims.
    **Recommended:** verify-first

- [ ] **[agents]** LLM-as-judge, rubric design, trace auditing, and observability

    **What it is:** The report argues that scaled agent evals require LLM-as-judge, calibrated rubrics, periodic human audits, trace review, and observability tooling such as Promptfoo, Braintrust, Langfuse, and MLflow-style stacks.

    **Why it matters:** High practical value. This can strengthen both the coding-agent and workflow-agent eval guidance and may justify selected tool updates.

    **Source shape:** Promising but tool-heavy and noisy. Some tooling is clearly relevant; some may be weak or peripheral.

    **Likely impact:** updates folded into the two training pages; selected tool pages if a tool proves durable and important enough.
    **Verification:** verify before proposal, with emphasis on official docs and real product scope.
    **Recommended:** verify-first

- [ ] **[agents]** Benchmark map for agent evaluation

    **What it is:** A benchmark cluster spanning SWE-bench-family, SWE-PolyBench, Terminal-Bench, OSWorld, WebArena, ToolBench, tau-bench, and GAIA, with a warning that public benchmarks are necessary but insufficient for deployment decisions.

    **Why it matters:** This is likely the cleanest route to benchmark-page expansion and to a clearer benchmark map for the wiki.

    **Source shape:** Stronger than many other sections because several benchmark names are already familiar and likely grounded in papers or benchmark sites. Still needs verification of reported roles, limitations, and framing.

    **Likely impact:** updates to `wiki/benchmarks/swe-polybench.md`; possible new benchmark pages; supporting updates to future eval pages.
    **Verification:** verify before proposal via benchmark papers and benchmark sites.
    **Recommended:** verify-first

- [ ] **[tools]** Eval tools and supporting infrastructure landscape

    **What it is:** A large set of tools and vendors appear across the report: Braintrust, Promptfoo, Langfuse, DeepEval, Galileo, Arize, benchmark runners, simulator frameworks, and adjacent engineering verification tools like SonarQube and Snyk.

    **Why it matters:** Tool discovery was an explicit research goal. This cluster can produce important `tools/` entries or enrich eval training pages with practical toolchain recommendations.

    **Source shape:** Noisy. The report is useful as a discovery map, but not enough to justify tool pages directly. Some mentioned tools are core; others are incidental, SEO-sourced, or not durable enough for the wiki.

    **Likely impact:** selected tool proposals only after verification; otherwise folded into training/concept pages as examples.
    **Verification:** required. Promote only tools with strong official docs, clear relevance, and durable importance to eval practice.
    **Recommended:** verify-first

- [ ] **[agents]** Eval lifecycle, trace mining, holdouts, and overfitting prevention

    **What it is:** Guidance on treating eval suites as living systems: continuous trace mining, incident-to-regression conversion, hidden holdouts, periodic refreshes, and retiring stale tests.

    **Why it matters:** Very strong fit for the wiki's existing `agent-improvement-loop` framing and likely one of the most reusable concepts in practice.

    **Source shape:** Synthesis-heavy but operationally coherent. Less dependent on exotic named frameworks than some other sections.

    **Likely impact:** update to `wiki/concepts/agent-improvement-loop.md`; likely folded into the future evals concept and training pages.
    **Verification:** moderate verification required; likely easier to ground than the autonomy/governance abstractions.
    **Recommended:** verify-first
