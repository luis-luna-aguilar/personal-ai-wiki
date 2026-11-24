---
title: Evals for workflow and task agents
type: training
as_of: 2026-10-26
sources: [agents-evals-deep-research, every-benchmarks-dont-know-your-job-2026-08-25, leeknowlton-verifiable-work-2026-10-17, every-copilot-seat-in-org-chart-2026-09-25, every-personal-ai-benchmark-2026-09-21, every-evals-go-mainstream-2026-09-24, paper-instruments-ultramarine-1-flash-2026-10-14, claude-api-build-eval-hillclimb]
---

# Evals for workflow and task agents

Coding agents have a clear correctness signal: the code compiles, the tests pass, or they don't. Business agents — the ones handling email, scheduling, customer support, sales operations, financial analysis, document review, or internal coordination — rarely do. Success is often probabilistic, highly context-dependent, and governed by policy rules that don't reduce to a compiler check.

This makes eval design for workflow agents fundamentally harder than for coding agents, and it also makes the failure modes less obvious. An agent can appear to be performing well in single-shot demos while systematically failing at the reliability and policy adherence that production requires.

## The core problem: reliability degrades over repeated trials

The deepest and most commonly missed problem in workflow agent evaluation is reliability degradation over repeated interactions.

Traditional benchmarks use **pass@k**: "did at least one of k attempts succeed?" In coding, this is acceptable — you generate five patches, run the tests, keep what works. But in customer service, a sales workflow, or a scheduling agent, the agent gets one shot per live interaction. There is no retry.

**pass^k** (from the tau-bench research benchmark) asks the harder question: "did the agent succeed on ALL k consecutive trials?" The results are sobering. An agent with 60% single-attempt success ($pass^1$) can drop below 25% reliability when measured across eight consecutive runs ($pass^8$). This means eval suites that only test single-shot success will massively overestimate production readiness for workflow agents.

Practically: mandate pass^k testing for any customer-facing or high-stakes internal workflow agent. Single-trial success rates are interesting; multi-trial consistency is what matters for production.

## Current guidance

- Measure multi-trial consistency (pass^k) from the start — single-attempt success rates mislead on production readiness
- Evaluate across five dimensions, not just accuracy: cost, latency, task completion, safety/policy adherence, and reliability
- Apply task-specific metrics for each business workflow type — blanket accuracy measures miss domain-specific failure modes
- Use simulated adversarial users to evaluate how agents handle partial information, policy ambiguity, and out-of-scope requests before they encounter real users
- Use LLM-as-judge with calibrated rubrics for qualitative dimensions (tone, policy adherence, helpfulness) that don't reduce to deterministic checks
- Monitor for PII leakage and policy boundary violations in production with async online evals

## Designing an eval you can hill-climb

Before tuning prompts, skills or model choice against an eval, check that the eval can tell a better setup from a worse one. Anthropic's four checks:

1. **Tasks mirror production.** Sample what the system will actually face, not what is easy to generate or grade.
2. **Stronger models and more effort score higher.** If they don't, suspect ambiguous tasks or a miscalibrated grader.
3. **Headroom at the frontier.** The best model at max effort should sit well below 100%, and not because of impossible tasks: a task that fails every replicate usually means a broken task. A good task is one where two domain experts would agree on the verdict and everything the grader checks is stated in the task.
4. **Low run-to-run variance.** Noise often comes from vague tasks, an unstable grader, inconsistently applied effort settings, or leftover environment state (a file, a git history) that hands the agent the answer.

**Sampling.** Pick hard cases because a person can say why they are hard, not because today's model fails them; failure-picked cases measure one model's blind spots. Order of preference: production transcripts, bug reports and tickets, five to ten hand-written cases, then synthetic cases anchored on real ones. Raw user traffic can skew easy, because users try what they expect to work.

**Grader.** Use the cheapest grader that fits: a code check (exact match, fixed label set, schema, tests) when outputs are constrained, otherwise an LLM judge from a different model than the one under test, with a rubric of checkable claims rather than a 1-to-5 scale, or a blind, order-randomized comparison against a baseline. Grade a handful of cases by hand and compare, then run the grader twice on the same output to catch drift. Check that timeouts, API errors and truncated answers aren't counted as model variance. If the baseline already scores ~95%, aim the work at cost or latency instead.

The `/claude-api build-eval` command in Claude Code walks through these steps, pausing for approval of the inputs and grader. The hill-climbing side is on [Automated harness optimization](../concepts/automated-harness-optimization.md).

## Five evaluation dimensions

A useful structure for enterprise workflow agent evals:

- **Cost** — optimizing only for task success can produce agents that are significantly more expensive than cost-aware alternatives. High-capability models may solve a simple scheduling task, but at an unacceptable API cost per interaction.
- **Latency** — for web-interactive agents, external environment latency (network fetches, API calls, HTML parsing) can dominate total execution time. Measure and bound this per task type.
- **Efficacy** — baseline task completion: did the agent do what was asked, route tool calls correctly, and provide factually accurate output?
- **Assurance** — safety, policy adherence, and security: does the agent resist [prompt injection](../concepts/prompt-injection.md)? Does it prevent PII leakage? Does it stay within its authorized boundaries?
- **Reliability** — consistent performance across repeated trials; this is the pass^k problem.

These are trade-offs, not independent goals. An agent optimized only for efficacy may solve tasks correctly but at 10× the cost of a more constrained alternative.

## Task-specific metrics (eight business workflows)

Different business tasks have distinct primary failure modes. Apply task-specific metrics rather than relying on a single cross-domain measure:

| Task | Primary eval focus | Key failure modes |
|---|---|---|
| Email automation | Tone consistency, hallucinations, toxicity, formatting | Wrong tone for audience; fabricated facts; inappropriate content |
| Calendar/scheduling | Plan quality, step efficiency, temporal constraint adherence | Double-booking; ignoring time zones; unnecessary tool calls |
| Research synthesis | Retrieval relevance, summarization fidelity, factuality against retrieved data | Hallucinating facts not in retrieved sources; missing key findings |
| Customer support | Containment rate, error recovery on ambiguous queries, pass^k reliability | Escalating when unnecessary; failing on ambiguous refund/return policies |
| Sales operations | CRM state mutation accuracy, latency vs. SLA, PII leakage prevention | Incorrect CRM updates; slow response; leaking prospect data |
| Finance analysis | Mathematical accuracy, cost-per-task, golden workflow adherence | Calculation errors; expensive tool chains; deviation from approved workflows |
| Document review | Contextual recall, long-context reasoning, clause-level accuracy | Missing critical clauses buried deep in long documents |
| Internal operations | Flow coverage, escalation routing, policy boundary adherence | Wrong routing; unauthorized actions; dialogue paths that dead-end |

## Simulated users for safe pre-deployment testing

Testing experimental customer-facing agents on real users carries significant reputational and compliance risk. The alternative: adversarial user simulation.

**How it works:** An LLM is prompted to act as a user with a specific goal, but instructed to withhold information, be inconsistent, or behave ambiguously. Example: "You need to change your flight. Your booking reference is AA123. Do not reveal your booking reference until the agent specifically asks for it." The agent must navigate partial observability, ask clarifying questions, and complete the task.

This pattern (used in the tau-bench evaluation framework) exposes failure modes that clean test inputs miss: how does the agent handle incomplete information? What happens when the user changes their request mid-conversation? Does it know when to escalate?

**Shopify SimGym** extends this to e-commerce: synthetic buyer personas navigate unpublished product themes and interact with the layout before real traffic is routed. The simulation identifies navigational friction points without any real user exposure.

Use simulation for:
- Pre-deployment stress testing of edge cases
- Adversarial testing of policy boundaries (what happens when a user asks for something the agent isn't authorized to do?)
- Measuring how the agent handles out-of-scope requests (does it escalate? hallucinate? refuse cleanly?)

## Evidence from practice

- **Public benchmarks can't answer a buying decision.** Mercor CEO Brendan Foody and Box CEO Aaron Levie both argue companies spending tens of millions of dollars a year on AI frequently do so without offline evals — a fixed set of real internal tasks used to compare models before they touch live work — leaving them unable to say whether a model actually does the job they bought it for, or whether a cheaper model would do it just as well.
- **KateBench: a high acceptance rate that looked finished but wasn't.** Every's internal AI copyeditor (trained on ~30,000 of its editor-in-chief's past edits, run inside Google Docs) showed an apparently strong 85-90% acceptance rate — until the engineer who owns it found the number was inflated by a silent cap that discarded any suggestion past the 40th on long essays, quietly dropping good edits before an editor ever saw them. The acceptance rate is also noisy run-to-run, since the model doesn't produce identical edits twice, so a single high-scoring run doesn't prove improvement.
- **CentaurBench: the best solo performer isn't always the best helper.** On 5 of 7 tasks tested, the model best at completing a task alone was not the model best at improving a weaker model's first attempt — a distinct failure mode from the reliability problem above, relevant whenever an eval setup assumes "the strongest model" is interchangeable across roles.
- **Thinkingbox: reliability collapses under repetition, echoing this page's pass^k thesis with a fresh number.** The strongest coding model tested passed 65% of single attempts, but its success rate fell to 25% when required to perform reliably across 20 consecutive attempts — an independent data point for the same pass@k-vs-pass^k gap this page already documents.
- **Microsoft: thousands of workflow evals, built by the people who do the work.** At the September 2026 Copilot relaunch, Microsoft said it runs about 16,000 internal evals, each a common task found in usage data and built by domain experts, and builds more with customers. Charles Lamanna's pattern for customers who succeed: the person who does the job daily builds the eval; they "embrace the red", treating a failing test as the to-do list and writing a harder one once it passes; and they measure the current human baseline (error rate, contract turnaround time) before the agent tries, so it has a real number to beat.
- **Evals become a job requirement and an engineering routine.** Nearly half of 25 product-manager openings Lenny Rachitsky shared in September 2026 asked for experience writing evals, and at Sentry proposed code changes triggered about 1,800 eval runs in a month, up from near zero in May, catching cases such as revised instructions that break tasks an agent used to handle. The individual version of the practice is under "Personal benchmarks for picking a model" below.
- **Hill-climbing for cost on a support eval (Anthropic).** On 44 support tickets (30 searched, 14 held out), `/claude-api hillclimb` first removed mandatory tool-call rituals, a scratchpad step and contradictory rules from the prompt, then moved from Opus 4.8 at high effort to Opus 5.5 at low effort, then stepped down to Sonnet 5 at low effort, which scored the same at about half the cost. Routing rules and a refund-cap cross-reference took search accuracy from 74.4% to 98.9% and cost per ticket from 4.6¢ to 1¢. On the held-out tickets the final setup scored 90.5% against 78.6% at roughly a fifth of the cost. That gap is why the held-out number is the one to report.

## LLM-as-judge for qualitative dimensions

A judge is also what decides whether a task can be delegated at all. Work an AI can verify can be scaled with little human attention; work that might be verifiable becomes delegable only once an AI judge has been shown, through its own evals, to grade it competently. Some judges are easy to build and some are hard enough not to be worth the effort, so estimate that cost before committing (Lee Knowlton, Oct 2026). See [AI work delegation modes](ai-work-delegation-modes.md).

For dimensions like tone, helpfulness, and policy adherence — where there's no single correct answer — a capable secondary model can grade the primary agent's outputs at scale. Key safeguards:

- **Calibrated rubrics:** specific, scored criteria rather than general quality questions. "Score 1 if the agent explicitly acknowledged the customer's complaint before proposing a resolution. Score 0 if it jumped directly to a solution." Specificity is the reliability mechanism.
- **One proposition per criterion:** a criterion copied from one golden answer rejects valid alternatives, and a vague one passes plausible errors; state the one checkable condition that earns credit (Paper Instruments, Oct 2026). See [Non-verifiable RL](../concepts/non-verifiable-rl.md).
- **Reference answers (golden datasets):** provide the judge with known-correct examples so it compares against an ideal state, not abstract quality.
- **Human audits (IRA checks):** periodically sample 5–10% of LLM-judged evals for manual human review. Measure Inter-Rater Agreement between the LLM and human reviewers to detect when the judge has drifted.

Observability platforms (Braintrust, Langfuse) support trace ingestion and scored assertions. The judge grades the full interaction trace, not just the final output — important for workflow agents where intermediate steps determine whether the outcome is safe and correct.

## Proven patterns

- **Mandate pass^k early.** Single-attempt success rates feel good; multi-trial consistency exposes the real production reliability profile.
- **Adversarial simulation before real users.** If your agent can't reliably handle a simulated user withholding information, it will fail with real ones.
- **Separate correctness from compliance.** An agent can produce a helpful and accurate response that also violates a policy (leaks PII, approves an out-of-scope request). Eval these dimensions independently.
- **Calibrate rubrics with real cases.** Start by taking 20–30 real human-handled interactions, have domain experts judge them, then use those judgments to calibrate the rubric. If the LLM judge doesn't match the expert judgment on the calibration set, the rubric needs revision before it's used at scale.

## Personal benchmarks for picking a model

The same discipline at the scale of one person choosing a daily model. Public benchmarks cannot say whether a model helps with your job, or whether a cheaper one would do as well; with frontier models exceeding most everyday needs, speed, price and taste decide. Mike Taylor's three levels (Every, Sep 2026):

1. **Collect failures.** Have your coding or desktop agent mine the past month of sessions for about ten tasks that needed heavy back-and-forth or were abandoned ("back-pocket evals", Steve Yegge's term). Run them in parallel across models in a side-by-side viewer: a large and a small model, two providers, and one model three times.
2. **Turn taste into yes/no checks.** Dictate likes and dislikes, have a model convert them into three to ten pass/fail checks, and let a second model grade. Avoid 100-point scores: ratings cluster around 70/100 and imply precision they lack.
3. **Scale up.** Turn each task into a skill that files brief, output and feedback until it holds 20+ cases, each with a gold example and an eval script.

Include hard tasks: easy ones sit below the "discernment horizon", where every model passes. On Taylor's consulting benchmark OpenAI's cheapest model, Luna, came within a few points of Fable, so routine work can go to the cheap model (see [Cost-aware AI task routing](cost-aware-ai-task-routing.md)). Benchmarks saturate; make the tasks harder as models improve. Every is helping all its staff build one.

## Failure modes

- Shipping a workflow agent based only on demo performance — demos are single-shot, production is multi-shot
- Using pass@k when you need pass^k — acceptable for coding tasks where you can retry, not for live customer interactions
- Optimizing only for accuracy — ignoring cost, latency, and policy adherence creates agents that technically "work" but are too expensive, too slow, or non-compliant
- Testing only happy-path flows — real users are inconsistent; the agent needs eval coverage of partial information, mid-conversation changes, and out-of-scope requests
- No online eval layer — without async monitoring of production traces, quality degradation is invisible until customers complain

## Open questions

- What is the right pass^k threshold before a workflow agent is deployed to real users? The answer depends on the stakes of the task and acceptable error rates per interaction volume.
- How do you evaluate emergent multi-agent behavior when a workflow agent hands off to another agent?

## Recent changes

- [2026-10-26] Added Anthropic's checks for an eval you can hill-climb (production-like tasks, scores rising with model and effort, headroom, low variance), plus case sampling, grader validation, and a support-ticket cost hill-climb (held-out 78.6% → 90.5% at ~1/5 the cost).
- [2026-10-17] Framed LLM-as-judge as the gate on delegation: a judge proven with evals turns maybe-verifiable work into delegable work (Lee Knowlton).
- [2026-10-14] Added "one proposition per criterion" rubric guidance from Paper Instruments' Ultramarine RL report, linked to the new Non-verifiable RL page.
- [2026-09-25] Added Microsoft's eval practice from the Copilot relaunch: ~16,000 internal workflow evals, practitioner-built evals, "embrace the red", and measuring the human baseline first.
- [2026-09-24] Added a compact personal-benchmark method for individuals picking a model (Mike Taylor's three levels) and evidence that evals are going mainstream (about half of 25 PM openings ask for eval experience; Sentry at ~1,800 eval runs a month).
- [2026-08-25] Added Evidence from practice: Mercor/Box CEO case for task-specific offline evals over leaderboard-chasing; KateBench's inflated acceptance rate (silent 40-suggestion cap, run-to-run noise); CentaurBench (best solo model ≠ best helper model, 5/7 tasks); Thinkingbox (65% single-attempt pass rate falls to 25% across 20 consecutive attempts).

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [Every — Benchmarks Don't Know Your Job](../sources/newsletters/every-benchmarks-dont-know-your-job-2026-08-25.md)
- [Lee Knowlton — notes on using AI productively](../sources/tweets/leeknowlton-verifiable-work-2026-10-17.md)
- [Every — Copilot Gets a Seat in the Org Chart](../sources/newsletters/every-copilot-seat-in-org-chart-2026-09-25.md)
- [Every — How to Create Your Own Personal AI Benchmark](../sources/newsletters/every-personal-ai-benchmark-2026-09-21.md)
- [Every — Evals go mainstream](../sources/newsletters/every-evals-go-mainstream-2026-09-24.md)
- [Paper Instruments — Ultramarine 1 Flash: Scaling Non-Verifiable RL](../sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md)
- [Anthropic — Automating eval design and hillclimbing with Claude](../sources/articles/claude-api-build-eval-hillclimb.md)
