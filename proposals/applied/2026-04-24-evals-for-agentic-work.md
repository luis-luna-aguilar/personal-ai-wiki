---
type: proposal
source: raw/deep-research/2026-04-23 Agents Evals.md
status: pending
created: 2026-04-24
---

# Proposal: Evals for workflow and task agents (training page)

## Summary

Business agents (email, scheduling, customer support, sales, finance, document review, internal operations) need a completely different eval approach than coding agents. There's often no single correct answer. Success is probabilistic, policy-dependent, and conversational. This proposal creates a training page covering the core problem, the pass^k reliability issue, task-specific metrics across eight business task types, simulated user testing, and LLM-as-judge for qualitative grading.

The pass^k framing and tau-bench adversarial simulation are well-grounded. The "CLEAR framework" is attributed to the report rather than a specific well-known primary source; it's presented as a useful structure rather than a canonical standard.

## Intended changes

- [x] **Create** `wiki/training/evals-for-agentic-work.md` — new training page
    > See draft below

- [x] **Update** `wiki/index.md` — add entry under Training
    > **Add under Training:**
    > `- [[training/evals-for-agentic-work]] — eval patterns for workflow and task agents: pass^k reliability, CLEAR dimensions, task-specific metrics, simulated users *(as_of: 2026-04-23)*`

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add link in See also
    > **Add to See also (or create it if absent):**
    > `- [[training/evals-for-agentic-work]] — eval patterns for workflow and task agents: reliability metrics, task-specific patterns, simulated users`

## Page drafts

### wiki/training/evals-for-agentic-work.md (new)

````md
---
title: Evals for workflow and task agents
type: training
as_of: 2026-04-23
sources: [agents-evals-deep-research]
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

## Five evaluation dimensions

A useful multi-dimensional framework for enterprise workflow agents:

- **Cost** — optimizing only for task success can produce agents that are significantly more expensive than cost-aware alternatives. High-capability models may solve a simple scheduling task, but at an unacceptable API cost per interaction.
- **Latency** — for web-interactive agents, external environment latency (network fetches, API calls, HTML parsing) can dominate total execution time. Measure and bound this per task type.
- **Efficacy** — baseline task completion: did the agent do what was asked, route tool calls correctly, and provide factually accurate output?
- **Assurance** — safety, policy adherence, and security: does the agent resist prompt injection? Does it prevent PII leakage? Does it stay within its authorized boundaries?
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

## LLM-as-judge for qualitative dimensions

For dimensions like tone, helpfulness, and policy adherence — where there's no single correct answer — a capable secondary model can grade the primary agent's outputs at scale. Key safeguards:

- **Calibrated rubrics:** specific, scored criteria rather than general quality questions. "Score 1 if the agent explicitly acknowledged the customer's complaint before proposing a resolution. Score 0 if it jumped directly to a solution." Specificity is the reliability mechanism.
- **Reference answers (golden datasets):** provide the judge with known-correct examples so it compares against an ideal state, not abstract quality.
- **Human audits (IRA checks):** periodically sample 5–10% of LLM-judged evals for manual human review. Measure Inter-Rater Agreement between the LLM and human reviewers to detect when the judge has drifted.

Observability platforms (Braintrust, Langfuse) support trace ingestion and scored assertions. The judge grades the full interaction trace, not just the final output — important for workflow agents where intermediate steps determine whether the outcome is safe and correct.

## Proven patterns

- **Mandate pass^k early.** Single-attempt success rates feel good; multi-trial consistency exposes the real production reliability profile.
- **Adversarial simulation before real users.** If your agent can't reliably handle a simulated user withholding information, it will fail with real ones.
- **Separate correctness from compliance.** An agent can produce a helpful and accurate response that also violates a policy (leaks PII, approves an out-of-scope request). Eval these dimensions independently.
- **Calibrate rubrics with real cases.** Start by taking 20–30 real human-handled interactions, have domain experts judge them, then use those judgments to calibrate the rubric. If the LLM judge doesn't match the expert judgment on the calibration set, the rubric needs revision before it's used at scale.

## Failure modes

- Shipping a workflow agent based only on demo performance — demos are single-shot, production is multi-shot
- Using pass@k when you need pass^k — acceptable for coding tasks where you can retry, not for live customer interactions
- Optimizing only for accuracy — ignoring cost, latency, and policy adherence creates agents that technically "work" but are too expensive, too slow, or non-compliant
- Testing only happy-path flows — real users are inconsistent; the agent needs eval coverage of partial information, mid-conversation changes, and out-of-scope requests
- No online eval layer — without async monitoring of production traces, quality degradation is invisible until customers complain

## Open questions

- What is the right pass^k threshold before a workflow agent is deployed to real users? The answer depends on the stakes of the task and acceptable error rates per interaction volume.
- How do you evaluate emergent multi-agent behavior when a workflow agent hands off to another agent?

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

## Open questions

- The "CLEAR framework" as a named standard is uncertain — the draft presents the five dimensions (Cost, Latency, Efficacy, Assurance, Reliability) as a useful structure but doesn't treat it as a canonical named framework. If the user can find a primary source for CLEAR, the page should be updated to attribute it properly.
	- Lets not name it.
