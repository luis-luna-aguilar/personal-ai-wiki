---
title: Agent autonomy and governance
type: training
domains: [agents]
tags: [agentic]
as_of: 2026-11-12
sources: [agents-evals-deep-research, mckinsey-agentic-org, ramp-ai-adoption-playbook, ai-for-boring-businesses, token-tightening-ai-finops-2026-06, every-ai-sandwich-april-2026, every-cheap-competence-after-automation-2026-05, every-33-questions-executives-2026-08-28, every-ai-adoption-levels, karpathy-capability-funnel-2026-10-11, satyanadella-models-as-insider-risks-2026-10-10, latent-space-crossing-the-threshold-2026-10-14, anthropic-human-agent-teams-2026-10, claude-for-manufacturing-2026-11-12, latent-space-aiuc-rune-kvist-2026-09-16, every-next-two-adoption-levels-2026-11-12]
---

# Agent autonomy and governance

How an organization decides what its agents are allowed to do, and who owns that decision. The core idea: autonomy is not a binary switch but a staged ladder, and each step up is earned with eval evidence rather than granted because a demo looked good. This page is for the people who govern agent rollouts — AI platform leads, risk owners, and the managers deciding when a workflow can move humans from inside the loop to above it.

## Autonomy ladder

A practical governance model for expanding what an agent is allowed to do: each step up requires eval evidence that the agent can handle the broader authority safely.

| Level | Name | What the agent can do |
|---|---|---|
| 0 | Read-only assistant | Synthesizes, proposes, retrieves. Human executes everything. |
| 1 | Human-mediated actions | Drafts artifacts such as emails, code, and notes. Human reviews and executes. |
| 2 | Guarded actions | Executes low-risk actions autonomously. High-risk actions require explicit human approval. |
| 3 | Conditional autonomy | Manages multi-step workflows autonomously but pauses at predefined high-risk checkpoints. |
| 4/5 | High to full autonomy | Executes end to end within strict policy boundaries. Reports to humans only on completion or unresolvable anomaly. |

**Promoting between levels requires eval evidence, not just elapsed time.** To move an agent from Level 1 to Level 2, the eval suite must prove the agent reliably adheres to role-based access controls and policy boundaries. To move to Level 3, the agent must pass escalation evals: inject adversarial and out-of-scope queries into the test suite and measure whether the agent triggers a human handoff rather than hallucinating an action. The failure mode being tested is simple: does the agent know what it does not know?

**Practical permission controls:** transitions should be enforced mechanically, not by judgment alone. Common mechanisms include pass-rate thresholds over a rolling window of consecutive traces, cost-based throttling that freezes spending when a runaway loop is detected, and tracking how often the agent escalates cases that humans later approve unchanged. Specific thresholds should be calibrated per organization; the values cited in the research report are directional, not universal.

**The practical implication for enablement:** do not deploy a new agent at Level 3 or 4 because the vendor demo looked good. Start at Level 1, build an eval suite, and promote based on measured evidence. The enablement question becomes: what eval evidence would make us comfortable giving this agent more authority?

## AI adoption and fluency levels

Every (Mike Taylor / Laura Entis, June 2026) published an 8-level framework for AI adoption maturity, which its consulting practice also uses as an AI-fluency ladder; Taylor added Levels 9 and 10 in November 2026. Central insight: **higher level is not automatically better.** The right level depends on how much you trust the AI and how costly a mistake is.

| Level | Name | What the AI does |
|---|---|---|
| 1 | Chatbot | You ask, it answers. Single turn. No memory. |
| 2 | Conversational assistant | Multi-turn, context-aware. Still human-initiated every turn. |
| 3 | Tool user | AI calls external tools (search, calculator, APIs) inside a conversation. |
| 4 | Autonomous task executor | Completes multi-step tasks with minimal steering. Human reviews output. |
| 5 | Background agent | Runs unsupervised; triggers on schedule or event; reports results. |
| 6 | Goal-directed agent | Given an objective and constraints; plans and executes independently. |
| 7 | Multi-tool orchestrator | Combines tools, agents, and APIs across a pipeline to complete complex work. |
| 8 | Sub-agent orchestrator | Runs a team of specialized sub-agents under a master orchestrator. |
| 9 | Simulation | Several orchestrated agent teams pursue the same goal with different strategies and compete under a scoring rule you set. |
| 10 | Multiverse | The same competition is rerun many times to separate strategies that win reliably from ones that won by luck. |

**Practical rules from the framework:**
- Match level to task risk and trust. High-stakes tasks with hard-to-verify outputs belong at lower levels with more human review.
- The signal to move up: consistent performance at the current level with no meaningful error rate — not just enthusiasm or capability.
- Levels 5-8 require investing in evals, verification, and guardrails before promotion.

**Levels 9 and 10 (Every, November 2026).** Levels 1–8 hand off more work and autonomy; 9 and 10 change how agents explore strategies once orchestration is routine. At Level 9 your job becomes defining the goal, the scoring and the rules of competition, for problems where trying several approaches is cheaper than guessing wrong (growth, pricing, content strategy, engineering problems with more than one solution); diverse teams can be seeded with persona prompts built from colleagues' past messages. At Level 10 you rerun that competition with the same starting conditions and trust only what wins across runs: Taylor's simulator of ~2,000 cloned Hacker News commenters predicted front-page headlines 60% of the time, and its misses came from chance (one extra early upvote sent identical posts down different paths), not from bad personas. Limits he states: both levels are experimental and burn far more tokens; each competing team needs reliable orchestration and its own share of human attention; a bad simulation averaged 50 times gives "a very confident wrong answer," so for now this works on narrow systems such as a single feed or focus group. Check a winning plan with real people before acting on it.

**Where people sit (Every consulting, August 2026):** most people are at levels 1–2 (chatbot use, co-working with AI in Docs or Excel). The level knowledge workers are actively moving to is "agentic" work (Codex, Claude Cowork, Claude Code, adopting skills and running several tasks at once). Everything above that is still largely experimental, up to level 8, where a manager AI orchestrates other AIs. Use the ladder to calibrate expectations rather than pushing every team toward the top.

**The population-scale view (Andrej Karpathy, October 2026).** Karpathy describes the same spread across everyone as a funnel: about 75% of people have barely used an LLM, about 20% are casual free-tier users (including many professionals outside math and code, and executives who know the shift mostly second-hand), about 0.2% use frontier agents professionally in math and code, and a few thousand people see unreleased systems inside the labs. His three drivers double as enablement levers. Impact scales with the size and horizon of the problems people bring, so a team needs real, large problems to see the upside. Capability is jagged, peaking where work is digital, checkable and commercially valuable, so functions outside engineering should expect smaller gains. And access tier caps what anyone can see: views formed on last year's free chatbot understate what current paid agents do.

This ladder measures how people and teams use AI; the autonomy ladder above measures how much an individual agent is trusted to act alone.

## Humans in the loop vs. above the loop

A useful distinction for planning workflow redesign:

- **In the loop**: agents do parts of the process, then hand off to a human who does other parts. The human is a step in the workflow.
- **Above the loop**: agents do most or all of the core process; the human's role is judgment on top — reviewing the output, making the call, catching edge cases. The human supervises the workflow.

Both will coexist. "Above the loop" represents the higher-value state for most knowledge work: not eliminating human judgment, but elevating what humans are doing to where judgment actually matters.

**Example (American Arbitration Association):** Agents trained on closed case files to build timelines, review fact bases, examine both sides of an argument, and produce summary decisions — in some cases doing it better than the traditional manual process. A human reviews and approves. The judgment layer remains critical, but the execution work is done end-to-end by agents.

## Governance patterns

- **Promotion only after reliability.** Expand an agent from one bounded workflow to broader responsibility only after it is stable in the narrower role.
- **Exploration budget, then governance.** Removing token caps and access restrictions gives people room to discover high-leverage use cases before ROI is obvious — treat this as the deliberate first phase, with token allocation as governance (see [Cost-aware AI task routing](cost-aware-ai-task-routing.md)) as the second phase once a workflow's value is established, not a contradiction to resolve.
- **Reward outcomes, not AI usage.** Teams stall or drift when "used AI" becomes the goal; quality and throughput improvements are the only metrics that matter.
- **Trust battery with judge agent.** Grant autonomy incrementally, tied to demonstrated reliability rather than elapsed time — see [AI adoption: evidence from practice](ai-adoption-evidence.md) for the concrete Claudie mechanism (nightly judge agent, starting trust percentage, self-updating memory).
- **Widen autonomy per task type, with verification built in.** Anthropic's teams (Oct 2026) track which kinds of task each agent has earned autonomy on and widen scope one type at a time after repeated successes. They review all agent work by hand at first and turn that feedback into verification checklists, have a separate verifier agent check the doer's work, and ask agents for a weekly "lessons & missteps" report. As agents grow more independent, they are coached to treat human attention as scarce: batch questions into one pass, restate key context, limit how many items a person sees at once; some teams cap agent output per day so review stays sustainable. Retest tasks when models change, since old guardrails can hold a stronger model back. One engineering team reached agents handling 500 bug fixes independently this way.
- **Keep looking up separate from changing, and let write access follow the user's own permissions.** Anthropic's Claude for Manufacturing (November 2026) ends every skill with the responsible person's review: the estimator checks and releases the quote, the quality engineer verifies the fix. Its Infor connector only looks records up. Changes in Infor go through Infor's own plugin and run only after the user approves (for example, releasing a purchase order to another supplier and rescheduling production when a steel shipment slips), within that user's existing Infor permissions. Claude links figures and claims back to the underlying data and documents so the reviewer can check them.
- **Keep humans at the judgment boundary.** As AI fills in the middle of workflows, employees need stronger habits for framing, taste, coordination, and review rather than only faster execution tactics.
- **Split governance ownership explicitly.** A central AI team should own standards, security and vendor decisions, shared infrastructure, and the first few working examples; individual business teams should own their own workflows. Centralizing everything creates a bottleneck; leaving every team to build alone creates sprawl.
- **Measure at the workflow level, never by a single metric.** Track cycle time, output quality, error/rework rate, user satisfaction (e.g. NPS), and traditional cost-benefit business impact — and track reuse of shared skills as a leading indicator. Establish a pre-AI baseline (time, quality standard, cost, common mistakes) before claiming a workflow improved.

### Place controls where they enable autonomy

Finance practitioners at AI Engineer New York (October 2026) argued that safe autonomy depends on where controls and human judgment sit, not on how many approvals are added.

- **Approval fatigue is a risk, not a safeguard.** A person asked to approve everything slows the work and stops paying attention to the decisions that matter (John Feminella, Two Sigma).
- **Route by case type.** Classifiers settle routine calls and escalate only consequential or ambiguous ones to a person; deterministic rules handle clear-cut cases. Two Sigma runs this as one of five composable controls, each doing one job.
- **Propose, don't act, at the boundary.** Anthropic's trade-break investigation agent proposes order amendments for a human to approve and never writes them itself.
- **Build one trust layer, then deploy many agents.** Anthropic's three parts: identity and permissions (whom the agent acts as), a sandbox and approval layer (who signs off before it acts), and regression checks (does it still work when variables change).
- **Keep enforcement outside the model.** Bloomberg's incident list, including an agent that obeyed instructions hidden in a marketplace review and stocked a product, leads to scoped credentials, tool-call checks, egress limits, audit logs, budgets, and kill switches, plus input validation and provenance tracking. This is the practitioner form of the insider-risk principles below.
- **Treat human-in-the-loop as product design.** OpenAI's Joseph Kim: decide what the user must still control, review, or approve, and build traceability (where each number came from) into the interface.

### Treat the model as an insider risk

Satya Nadella (October 2026) argues agent governance should reuse the enterprise playbook for powerful insiders: establish identity, limit privileges, log activity, draw containment boundaries. Models are not assumed malicious, but any capable actor with access to important systems can err or be compromised. The central rule: the controls that decide what a model can access and do sit outside the model, separate from the [harness](../concepts/harness.md) that orchestrates it and from its action space (the set of actions it is allowed to take).

- **Model diversity.** No single model is the sole dependency for an important outcome, or verifies its own work.
- **Observe everything.** Every meaningful action leaves tamper-proof, human-readable evidence, so an outcome can be reproduced without the model attesting to it.
- **Verifiability.** Test the whole system continuously, including failures, attacks, edge cases, and system changes, not only successful tasks.
- **Independent controls and audit.** The organization sets access and permitted actions itself; validation is independent of the model being validated.
- **Containment.** Assume compromise from the start; an authorized person can always pause or stop a model mid-task.
- **Incident disclosure.** Failures are disclosed to those affected, with what failed and which controls broke, and lessons are shared across the industry.

This complements the autonomy ladder above: the ladder decides how much authority an agent has earned; these controls make sure that authority is enforced and observable from outside the model. Nadella's summary: the most trustworthy system is the one that lets you trust the model least.

### Certify and insure agents externally

Enterprise buyers increasingly ask who pays when an agent fails; the Air Canada ruling, which held the airline to a refund policy its chatbot invented, made that a legal question, not a hypothetical. [AIUC](../tools/aiuc.md) (cofounder Rune Kvist; $40M Series A, September 2026) sells the answer as one package of standard, testing and insurance. Its AIUC-1 standard for agent security, safety and reliability has six categories and about 51 requirements and 130 controls of three kinds: technical controls (for example, configure a groundedness filter), test controls (an independent party measures whether the control works), and policy controls (a named person accountable for failures, a plan for telling customers). Auditors such as KPMG and Schellman check that the evidence exists; AIUC runs the effectiveness tests itself, thousands of simulated jailbreak, hallucination and data-leak attempts every quarter. Certification takes 3–10 weeks and lasts a year. A consortium of Fortune 1000 risk leaders meets twice a quarter, so the standard is revised quarterly (recent additions: MCP and agent-to-agent risks). Certification pairs with liability cover: ElevenLabs bought an agent insurance policy underwritten with Lloyd's of London, which carries most of the financial risk. Lovable, ElevenLabs and Intercom are certified.

The practical lesson for builders: most teams already have guardrails, but few have stress-tested them against an adversary. This is the outside-assurance counterpart to the insider-risk controls above.

## Open questions

- When does "above the loop" become viable for a given workflow? What's the minimum agent reliability threshold before removing humans from execution entirely?

## Recent changes

- [2026-11-12] Added "Keep looking up separate from changing" from Anthropic's Claude for Manufacturing launch: skills end in the responsible person's review, Infor changes go through Infor's own plugin after approval and within the user's Infor permissions, and figures link back to source data.
- [2026-11-12] Extended Every's adoption ladder with Level 9 (Simulation: competing agent teams under a scoring rule) and Level 10 (Multiverse: rerun to filter out luck), with Mike Taylor's limits.
- [2026-10-19] Added Every's 8-level adoption maturity model from [Company-wide AI enablement](company-wide-ai-enablement.md), merged with the AI-fluency ladder that described the same framework.
- [2026-10-19] Page created, split out of [Company-wide AI enablement](company-wide-ai-enablement.md): its "Autonomy ladder" and "Humans in the loop vs. above the loop" sections and the "Governance, autonomy, and reliability" proven-patterns group.
- [2026-10-14] Added "Place controls where they enable autonomy" from AIE NYC finance keynotes: approval fatigue, classifier-versus-rule routing (Two Sigma), propose-not-act and a three-part trust layer (Anthropic), deterministic controls outside the model (Bloomberg), HITL as product design (OpenAI).
- [2026-10-11] Added Karpathy's capability funnel (≈75% barely touched LLMs, ≈20% casual free-tier, ≈0.2% professional frontier-agent users) and its three drivers as the population-scale counterpart to Every's "where people sit".
- [2026-10-10] Added "Widen autonomy per task type, with verification built in" from Anthropic's lessons on human-agent teams (verifier agents, weekly lessons-and-missteps reports, human-attention budgets).
- [2026-10-10] Added "Treat the model as an insider risk": Satya Nadella's external-control principles (model diversity, observe everything, verifiability, independent controls and audit, containment, incident disclosure).
- [2026-09-16] Added "Certify and insure agents externally": AIUC's AIUC-1 standard (technical, test and policy controls; quarterly adversarial testing by AIUC and quarterly revisions with Fortune 1000 risk leaders) paired with Lloyd's-backed agent liability insurance.

## Related

- [Company-wide AI enablement](company-wide-ai-enablement.md) — the broader adoption playbook this governance layer sits inside
- [AI delegation management](ai-delegation-management.md) — the individual-manager view: bounding an agent's authority one delegation at a time, and layered access control for always-on agents
- [AI work delegation modes](ai-work-delegation-modes.md) — task-level choice between autonomous delegation and close collaboration
- [Evals for workflow and task agents](evals-for-agentic-work.md) — the eval suites that supply the promotion evidence
- [Agentic infrastructure operations](agentic-infrastructure-operations.md) — staged autonomy (read-only, propose-only, mutate-with-approval) for production infrastructure

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [McKinsey — "AI is Everywhere. The Agentic Organization Isn't Yet."](../sources/articles/mckinsey-agentic-org.md)
- [Ramp AI adoption playbook](../sources/articles/ramp-ai-adoption-playbook.md)
- [AI for boring businesses](../sources/newsletters/ai-for-boring-businesses.md)
- [Token tightening and AI FinOps](../sources/newsletters/token-tightening-ai-finops-2026-06.md)
- [Every — "You're the Bread in the AI Sandwich" (April 2026)](../sources/newsletters/every-ai-sandwich-april-2026.md)
- [Every - Cheap competence and after automation](../sources/newsletters/every-cheap-competence-after-automation-2026-05.md)
- [Every — 33 Questions Executives Ask About AI—Answered](../sources/newsletters/every-33-questions-executives-2026-08-28.md)
- [AI Is Ready. Organizations Aren''t." — Every (June 7)](../sources/newsletters/every-ai-adoption-levels.md)
- [Andrej Karpathy on X — the LLM capability funnel](../sources/tweets/karpathy-capability-funnel-2026-10-11.md)
- [Satya Nadella — Models as Insider Risks in the Super Intelligence Era](../sources/tweets/satyanadella-models-as-insider-risks-2026-10-10.md)
- [Latent Space — Crossing the Threshold: autonomy and safety in financial agents](../sources/newsletters/latent-space-crossing-the-threshold-2026-10-14.md)
- [Lessons from Anthropic on building effective human-agent teams](../sources/articles/anthropic-human-agent-teams-2026-10.md)
- [Claude for Manufacturing: AI plugin for plant teams](../sources/articles/claude-for-manufacturing-2026-11-12.md)
- [Latent Space — Underwriting Superintelligence: Rune Kvist on AIUC-1 and agent insurance](../sources/newsletters/latent-space-aiuc-rune-kvist-2026-09-16.md)
- [Every — The Next Two Levels of AI Adoption](../sources/newsletters/every-next-two-adoption-levels-2026-11-12.md)
