---
type: triage
source: raw/deep-research/2026-04-23 Agents Evals.md
status: applied
---

# Triage: Agent Evals Research Report — 2026-04-23

## Signals

- [x] **[agents]** Agent eval taxonomy, trajectories, and the harness boundary

    **What it is:** The report's foundational argument is that evaluating an agent is fundamentally different from evaluating a model. When you run a coding agent, you are not testing Claude or GPT-4 in isolation — you are testing `model + harness (orchestration layer, prompts, tool schemas) + tools + environment` as one combined system. A change to any layer can break behavior even if the model itself hasn't changed.

    The second core idea is **trajectory evaluation**: two agents can reach the same correct final answer, but one got there in 3 steps while the other hallucinated a tool call, self-corrected, read 30 irrelevant files, and succeeded by accident. Both pass a result-only check. Only a trajectory eval catches the broken one.

    The report proposes five evaluation categories that map to different failure modes:
    - **Capability** — Can the agent do the task at all? (baseline intelligence check)
    - **Regression** — Did a prompt/tool/model change break something that was previously working?
    - **Trajectory** — Did it take a logical, efficient path? Did it ask for clarification when needed? Did it avoid redundant loops?
    - **Unit-level** — Does the routing layer pick the right tool? Does the RAG pipeline return the right document?
    - **Online (Production)** — Async scoring of live traffic to detect quality degradation, latency spikes, or cost explosions before users notice

    **Why it matters:** The wiki has `concepts/harness.md` and `concepts/agent-improvement-loop.md`, but neither likely has this taxonomy or the trajectory framing. This is the conceptual scaffolding that makes the rest of the eval guidance coherent — the coding and workflow eval signals below all build on it. Strong candidate for a new `wiki/concepts/agent-evals.md` or a substantial update to the harness page.

    **Source shape:** Mostly synthesis. The taxonomy language is normalized by the report author, not drawn verbatim from one canonical source. The core idea (evaluate the system, not just the model; evaluate the path, not just the result) is directionally strong and appears across multiple serious sources.
    **Verification:** moderate — the conceptual framing is solid; verify taxonomy names against Anthropic's eval docs or a benchmark paper before treating them as canonical.
    **Recommended:** verify-first

- [x] **[coding]** Evals for agentic software development

    **What it is:** A practical eval stack for coding agents, structured in two layers.

    **Layer 1 — Deterministic gates (always first):** Static analysis, type checkers (MyPy, TypeScript compiler), linters, and existing unit/integration tests run first. If any of these fail, the trajectory is interrupted and the error is fed back to the agent. AI-specific evals only run after deterministic gates pass. This is the "hard gate before soft gate" principle.

    **Layer 2 — AI-specific evals by task type.** The report argues that a single blanket eval strategy doesn't work — each coding task needs its own eval pattern. Nine specific patterns:
    1. **Issue fixing** — ReAct loop evaluation; agent must localize the correct AST node (using tree-sitter) before generating the fix
    2. **Feature implementation** — Spec-Driven Development validation; did the agent touch only in-scope files?
    3. **Refactoring** — Multi-repo trajectory analysis; tools like Moderne/Moddy use Lossless Semantic Trees to check mass dependency migrations across thousands of repos
    4. **Test generation** — Code coverage metrics + syntactic complexity checks to ensure edge cases are included
    5. **Code review** — Stacked tool evaluation: CodeRabbit (surface logic) → SonarQube (deep bugs) → custom LLM agent (architectural reasoning)
    6. **Security review** — Adversarial code injection to test prompt injection detection rates; integration with Snyk for vulnerability trapping
    7. **Dependency updates** — File system impact checks: did the agent accidentally touch core config manifests?
    8. **Migration tasks** — "Root Repo" coordination layer verification across micro-frontends and shared libraries
    9. **CI failure repair** — Step efficiency and trajectory analysis to prevent recursive runaway loops

    **Minimum Viable Eval Suite (MVES):** The report gives a concrete starting point for teams shipping a coding agent:
    - Baseline deterministic tests (compile, syntax, existing unit tests)
    - File system impact checks (did it touch files it shouldn't have?)
    - Cost/latency thresholds (hard token budget limits to catch runaway loops)
    - LLM-as-judge for code review (style, security anti-patterns, readability)

    **Case study — Ramp "Inspect":** Ramp's internal coding agent now initiates over 50% of merged PRs. They run it in shadow mode in isolated Modal VMs with a full-stack local environment (Postgres, Redis, Temporal, Sentry, Datadog). Shadow mode = agent proposes actions but cannot commit. The eval marks success when the agent's proposed fix matches the human-implemented fix and passes all sandbox tests.

    **Why it matters:** This is the clearest gap in the wiki. There's no training page on coding-agent eval practice. Strong candidate for a new `wiki/training/evals-for-agentic-software-development.md`. Also touches `concepts/harness.md` and `concepts/agent-improvement-loop.md`.

    **Source shape:** Mixed. The high-level architecture (deterministic gates first, then AI-specific evals) is sound and widely validated. The nine task-specific patterns vary in quality — issue fixing and CI repair are well-grounded; Agentform (IaC for agent orchestration) and "Root Repos" are lightly sourced and possibly report-normalized.
    **Verification:** verify the named tools (Agentform, Moderne/Moddy) and the Ramp case study specifically; the layered eval structure can likely be proposed with lighter verification.
    **Recommended:** verify-first

- [x] **[agents]** Autonomy ladder, escalation evals, and permission gating

    **What it is:** The report frames agent deployment as a ladder with five levels, where each step up requires passing an eval that proves the agent can handle the expanded authority:

    - **Level 0 — Read-only assistant:** No action capabilities. Synthesizes and proposes only. Human executes everything.
    - **Level 1 — Human-mediated:** Agent drafts artifacts (emails, code, notes). Human reviews and executes.
    - **Level 2 — Guarded actions:** Agent can autonomously take low-risk actions (update a CRM field, add internal notes). High-risk actions require human approval.
    - **Level 3 — Conditional autonomy:** Agent manages multi-step workflows autonomously but pauses at predefined high-risk checkpoints.
    - **Level 4/5 — High to full autonomy:** Agent executes end-to-end, self-diagnoses failures, and interacts with other agents. Reports to humans only on completion or unresolvable anomaly.

    **Escalation evals** are how you validate promotion between levels. To move an agent from Level 1 to Level 2, you inject adversarial examples and ambiguous out-of-scope tasks into the test suite and measure whether the agent reliably triggers a human handoff rather than hallucinating an action. The failure mode being tested is: does the agent know what it doesn't know?

    **Permission gating mechanics:** Transitions between levels are math-gated, not judgment-gated. The report describes an "Authority Graph" (a living permission map) governed by:
    - **pass^k thresholds** — e.g., 95% success rate over 100 consecutive traces before Level 2 → 3 promotion
    - **False Escalation Rate** — cases where the agent escalated but the human simply approved without changes (reviewer fatigue indicator)
    - **Token-bucket rate limits and cost-based throttling** — platforms like Fast.io enforce dollars-per-hour or monthly credit limits; if an eval detects a runaway recursive loop, the agent's spending is frozen

    **Why it matters:** This framing is directly applicable to `wiki/training/company-wide-ai-enablement.md` and `wiki/training/anti-autopilot-review-friction.md`. It gives a concrete governance model for the question "how do we safely expand what our agent is allowed to do?"

    **Source shape:** The five-level structure is useful and widely recognized in agentic governance contexts, but several named abstractions — "Authority Graph," "Boundary Violation Frequency," OIDC permission broadening — are report-synthesized and may not have strong primary source backing. The pass^k thresholds are grounded in the tau-bench paper (see benchmark signal below).
    **Verification:** required before proposal. The five-level ladder can be grounded via Anthropic's agent safety docs or similar. Do not trust the Authority Graph framing or specific threshold examples without a primary source.
    **Recommended:** verify-first

- [x] **[agents]** General task and workflow agent evals

    **What it is:** A parallel eval framework for non-coding agents — the ones managing email, calendar, customer support, sales ops, finance, document review, and internal operations.

    **The core problem:** For coding agents, "correct" is often deterministic (code compiles, tests pass). For business agents, there's rarely a single right answer. Success is probabilistic, conversational, and policy-dependent.

    **CLEAR framework** — the report's proposed multi-dimensional eval model for enterprise agents:
    - **Cost** — optimizing only for task success can produce agents 10x more expensive than cost-aware alternatives
    - **Latency** — for web-interactive agents, external environment latency (network fetches, HTML parsing) can consume over 50% of total execution time
    - **Efficacy** — baseline task completion, correct tool routing, factual accuracy
    - **Assurance** — safety, security, prompt injection resistance, no PII leakage
    - **Reliability** — consistent performance across repeated trials (this is the pass^k problem)

    **The pass^k problem (important):** Traditional benchmarks use pass@k — "did at least one of k attempts succeed?" That's fine when you can retry. But a customer service agent gets one shot per interaction. tau-bench introduced **pass^k** — "did the agent succeed on ALL k consecutive trials?" Results are sobering: an agent with 60% single-attempt success ($pass^1$) can drop below 25% reliability when measured across 8 consecutive runs ($pass^8$). This means eval suites that only test single-shot success will massively overestimate production readiness.

    **Task-specific metrics (8 business tasks):**
    1. Email automation — toxicity, hallucinations, tone consistency, formatting assertions
    2. Calendar/scheduling — PlanQualityMetric, StepEfficiencyMetric, temporal constraint navigation
    3. Research synthesis — retrieval relevance, summarization performance, Q&A factuality from retrieved data only
    4. Customer support — containment rate, error recovery on ambiguous queries, pass^k reliability
    5. Sales operations — latency vs SLA, CRM state machine mutation accuracy, PII leakage prevention
    6. Finance analysis — cost-per-task, deterministic mathematical accuracy, "Golden" workflow adherence
    7. Document review — contextual recall, long-context accuracy across buried clauses
    8. Internal operations — flow coverage, escalation routing accuracy, policy boundary adherence

    **Simulated users:** tau-bench and Shopify SimGym both use LLM-driven adversarial personas to test agents safely. In tau-bench, a simulator is instructed to withhold information ("change my flight but don't reveal your booking reference until asked") — the agent must navigate partial observability. Shopify SimGym deploys synthetic buyers on unpublished themes before real traffic.

    **Why it matters:** This would anchor a second training page (`wiki/training/evals-for-agentic-work.md`) covering business/knowledge-work agents specifically, parallel to the coding eval page. Also relevant to `company-wide-ai-enablement.md`.

    **Source shape:** Mixed. The CLEAR framework and pass^k are well-grounded (tau-bench paper is real). The eight task-specific metric names vary in quality — some (like containment rate for support, tone for email) are standard; others may be report-normalized. Shopify SimGym is a real product.
    **Verification:** verify CLEAR framework attribution and tau-bench pass^k before using those as primary claims; the task-metric breakdown can be used as structure with appropriate hedging.
    **Recommended:** verify-first

- [x] **[agents]** LLM-as-judge, rubric design, trace auditing, and observability

    **What it is:** Manual human review doesn't scale past a few hundred eval cases. The industry answer is LLM-as-judge — a secondary, capable model is given a calibrated rubric and asked to grade the primary agent's outputs and trajectories. This signal covers how to do it correctly and how to train non-engineers to participate.

    **Three safeguards to prevent judge drift:**
    1. **Calibrated rubrics** — instead of "is this answer good?", the rubric says: "Score 1 if the agent explicitly mentioned the 30-day return window. Score 0 if omitted." Specificity is the reliability mechanism.
    2. **Golden datasets** — provide the judge with human-verified reference answers so it's comparing against an ideal state, not abstract quality
    3. **Human audits (IRA checks)** — periodically sample 5–10% of LLM-judged evals for manual human review; measure Inter-Rater Agreement (IRA) between the LLM and the human experts to detect when the judge has drifted

    **Training non-experts to design rubrics and audit traces** (5-step curriculum):
    1. Agent foundations — routers, memory, tool schemas, Authority Graph boundaries
    2. Rubric design — 5 components: task framing, dimensional separation (3–6 axes like helpfulness/tone/safety), anchored scoring (explicit 0–4 point definitions), evidence rules, adjudication notes for edge cases
    3. Trace auditing — reading the "Prompt-Context-Action" loop in observability tools; distinguishing hallucination (reasoning failure) from privilege drift (tool/routing failure)
    4. Domain Expert Report — structured handoff format from domain expert to engineering team: failure-mode ontologies, benchmark datasets, calibrated examples
    5. Continuous loop integration — experts work with developers to translate tagged failure categories into automated LLM-judge prompts

    **Observability toolchain mentioned:** Promptfoo, Braintrust, Langfuse, Databricks MLflow. The report gives a concrete example: in a LangGraph multi-agent workflow, a `skill-used` assertion in Promptfoo verifies that the agent routed a query to the SQL execution tool rather than hallucinating the data from its weights. This is an example of grading internal reasoning, not just final output.

    **Why it matters:** This is cross-cutting — it strengthens both the coding eval and workflow eval training pages. The rubric design curriculum is especially valuable as a training page section. May also justify a tool update for Braintrust or Promptfoo if they prove durable enough for the wiki.

    **Source shape:** The LLM-as-judge pattern is well-established and widely documented. The five-step expert training curriculum reads as report synthesis. The IRA safeguard is standard eval practice. Tooling (Promptfoo, Braintrust, Langfuse) appears in real products.
    **Verification:** verify Promptfoo and Braintrust scope via official docs before creating tool pages; the rubric/IRA content can be proposed with lighter verification.
    **Recommended:** verify-first

- [x] **[agents]** Benchmark map for agent evaluation

    **What it is:** Eight benchmark families the report identifies as the most durable for tracking agentic capabilities. The report also includes an explicit warning: public benchmarks measure generalized capability but frequently fail to predict enterprise utility. Use them to select foundation models, not to make deployment decisions.

    **The eight benchmarks:**

    1. **SWE-bench / SWE-bench Verified** — gold standard for coding agents on real GitHub issues. Now largely deprecated by OpenAI due to data contamination (models absorbed the eval repo into pre-training data). The successor is **SWE-bench Pro**, which uses private/copyleft repos to prevent contamination.

    2. **SWE-PolyBench** — addresses SWE-bench's Python-only limitation. 2,110 real-world instances across Java, JavaScript, TypeScript, and Python. Uses Concrete Syntax Tree (CST) node-retrieval metrics alongside execution-based tests. Exposes deep multi-language gaps in frontier models.

    3. **Terminal-Bench** — 89 hard, multi-step tasks in isolated container environments covering system administration, compilation, and debugging via CLI. Frontier models currently score below 65%.

    4. **OSWorld** — computer use benchmark across Ubuntu, Windows, macOS. Human baseline: 72.36% task success. Top multimodal models: ~12%. The gap reveals how bad GUI grounding and layout navigation still are. Critical for teams evaluating RPA or desktop automation agents.

    5. **WebArena** — stateful web navigation benchmark (e-commerce, CMS, forums). Human baseline: 78%. Best systems (AWA 1.5): ~57%. Tests goal-directed behavior against web noise.

    6. **ToolBench** — 16,000+ real RESTful APIs from RapidAPI. Tests single-step, multi-step, and multi-tool planning using a Depth-First Search Decision Tree (DFSDT). The reference benchmark for enterprise API-chaining competence.

    7. **tau-bench** — policy adherence benchmark. Simulated users interact with agents on airline refund and retail return policies. Introduces pass^k (see workflow signal). Premier indicator of conversational reliability and enterprise policy compliance.

    8. **GAIA** — 466 multimodal questions testing fundamental reasoning, web browsing, and tool use. Human baseline: 92%. Frontier LLMs without scaffolding: ~15%. Designed to be un-gameable; useful for measuring the general autonomy gap.

    **Why it matters:** The wiki already has `wiki/benchmarks/swe-polybench.md`. This cluster would expand benchmark coverage and anchor the eval training pages with concrete capability reference points. The SWE-bench contamination/SWE-bench Pro transition is also a meaningful update to the coding state-of page.

    **Source shape:** Stronger than most of the report. SWE-bench, OSWorld, WebArena, GAIA, tau-bench, and ToolBench all have real papers or benchmark sites. The specific scores reported (OSWorld 12%, terminal-bench <65%, WebArena 57%) need verification against current leaderboards — they may be outdated.
    **Verification:** verify scores via benchmark sites or papers before committing to specific numbers; the benchmark landscape itself is well-grounded.
    **Recommended:** verify-first

- [x] **[tools]** Eval tools and supporting infrastructure landscape

    **What it is:** The report mentions a large set of tools across the eval workflow. Not all deserve wiki pages — this signal is mainly a discovery map. Grouped by function:

    **Observability / eval platforms (core mentions):**
    - **Braintrust** — trace ingestion, dataset management, "one-click" trace-to-dataset conversion; real product with clear eval focus
    - **Promptfoo** — assertion-based eval framework for LangGraph and similar; supports `skill-used` assertions for tool routing verification; real product
    - **Langfuse** — open-source LLM observability; mentioned alongside Braintrust as an alternative
    - **Databricks MLflow** — mentioned as an MLflow-style stack option; less eval-specific, more general observability

    **Evaluation libraries:**
    - **DeepEval** — Python eval library; primarily for LLM output quality
    - **Galileo** — eval and observability platform; less prominent in the report
    - **Arize** — ML observability; mentioned peripherally

    **Static analysis / security (existing tools being integrated into eval pipelines):**
    - **SonarQube** — deep bug detection; mentioned as the "deep layer" in the stacked code review eval pattern
    - **Snyk** — vulnerability scanning; integrated into security review evals
    - **CodeRabbit** — surface-level code review tool; mentioned as the first layer in the review stack

    **Simulation:**
    - **Shopify SimGym** — LLM-driven synthetic buyers for pre-launch agent testing; real product

    **Why it matters:** Braintrust and Promptfoo appear prominently enough and are real enough to justify tool pages if verification confirms their scope and durability. The rest are better folded into the training pages as toolchain examples rather than promoted to standalone pages.

    **Source shape:** Noisy. Braintrust, Promptfoo, Langfuse, SonarQube, Snyk, and Shopify SimGym are all real products with verifiable documentation. DeepEval, Galileo, and Arize are real but lightly mentioned. Agentform is cited as an IaC tool but is harder to verify independently.
    **Verification:** required. Use official docs to confirm scope and durability before creating any tool pages. Only promote tools that have clear eval-specific relevance, strong documentation, and visible adoption.
    **Recommended:** verify-first (selective promotion only)

- [x] **[agents]** Eval lifecycle, trace mining, holdouts, and overfitting prevention

    **What it is:** The problem this signal addresses: if you evaluate your agent against the same 50 hand-authored test cases over time, the agent will gradually overfit to passing those exact cases while failing in production. This is the same problem as overfitting in model training, applied to the eval suite itself.

    **The solution — treat the eval suite as a living system with four operational practices:**

    1. **Continuous trace mining:** Once an agent is deployed (even in shadow mode), monitor production logs actively. When a user downvotes a response or the agent triggers an error, extract that execution trace, anonymize it, and convert it into a new test case. When a production incident occurs (agent approves a refund that violated a temporal policy), the incident must yield a new regression test. Use an LLM to generate 10 synthetic variations of the failing interaction to ensure the agent learns the principle, not just the specific failure.

    2. **Hidden holdout sets:** Maintain a separate set of eval tasks that developers cannot see during normal development. Periodically test against this blind holdout to get an unbiased measure of generalization. If you only test on cases developers have seen, you're measuring memorization.

    3. **Periodic refreshes:** APIs change, company policies change, support ticket formats change. Evals built on deprecated documentation will falsely penalize a correct agent. Test cases need to be pruned and updated regularly (the report suggests weekly).

    4. **Retiring stale tests:** If an eval has achieved 100% pass rate for six consecutive months across multiple model updates, it's no longer providing a useful signal. Archive it and redirect compute to edge-case testing instead.

    **Why it matters:** This is the most directly applicable concept to the wiki's existing `wiki/concepts/agent-improvement-loop.md` — it gives the loop a concrete maintenance model. It also strengthens both training pages (coding and workflow evals) with a practical "how to keep your evals from becoming useless" section.

    **Source shape:** This is the most synthesis-light section of the report. The practices described (holdouts, trace mining, periodic refresh, retiring tests) are standard eval engineering practices that appear across multiple serious ML and AI safety contexts. Less dependent on exotic named frameworks than other sections.
    **Verification:** moderate — the practices are well-grounded; verify the "six months at 100%" heuristic specifically if it ends up quoted directly.
    **Recommended:** verify-first (lighter bar than other signals)
