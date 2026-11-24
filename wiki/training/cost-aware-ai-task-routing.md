---
title: Cost-aware AI task routing
type: training
domains: [agents, models]
tags: [agentic]
as_of: 2026-11-17
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07, ubereng-software-factory-2026-08-28, ainews-2026-04-23, every-33-questions-executives-2026-08-28, claudedev-spending-your-effort-2026-09-25, claude-platform-linked-billing-2026-11-17, anthropic-claude-fable-mythos-5-2, reasoning-effort-economics-2026-10, every-burn-more-tokens-2026-09-17, ainews-databricks-astra-sub-budget-2026-09-17]
---

# Cost-aware AI task routing

AI cost discipline is moving from token counting to routing work to the cheapest competent executor: deterministic code, small models, frontier models, agents, or humans. The goal is not to minimize model spend in isolation, but to minimize total task cost, including human review and failure recovery.

## Current guidance

- Use scripts for deterministic transformations and validations.
- Use smaller, local, or open-weight models for cheap classification, extraction, first drafts, private/low-latency processing, and low-risk routing; reserve frontier calls for ambiguous synthesis or high-stakes decisions.
- Use frontier models for ambiguous synthesis, high-stakes reasoning, and tasks where failure is expensive.
- Use humans for intent, taste, accountability, exceptions, and final review on consequential work.
- When a task has repeated domain-specific judgment and stable evaluation examples, compare three routes before defaulting to frontier models: expert prompt on a frontier model, expert prompt on a cheaper strong model, and fine-tuned/open-weight model with task-specific examples.
- Route by uncertainty, not only by task size. Use frontier models like Fable when the prompt, standard, or premise may be wrong; route settled, repeatable work to cheaper models, scripts, or task-specific fine-tunes.
- Route by task novelty. For a brand-new, high-stakes, or one-off task, use the best available model — it's often cheaper overall because it avoids costly mistakes and self-correction cycles. Only once a task becomes recurring and well-understood should it move to a smaller model via a framework like DSPy or prompt optimization.
- **Tasteful tokenmaxxing: depth over breadth.** The emerging leadership consensus (AIE Miami, April 2026) is not "burn more tokens" or "burn fewer tokens" but *how* you burn them. Shopify CTO Mikhail Parakhin: prefer serial autoresearch loops (depth) over kicking off 5, 10, 50 parallel LLM runs (breadth). Reid Hoffman's middle ground: track how people use AI, not just how much — team-wide experimentation plus regular check-ins to surface what's actually working. Dex Horthy (coiner of "Context Engineering") publicly retracted his earlier vibe-coding-only stance and encouraged engineers to read the code. The practical signal: measure the *quality* of token use, not the quantity.
- Treat "efficiencymaxxing" as routing discipline, not blanket cost cutting: decompose a workflow, decide which steps actually need frontier reasoning, and move stable low-risk steps to cheaper models, scripts, or fine-tuned specialists.
- Run token audits by stage for repeated agent workflows. Ask what each stage used, why it was necessary, and whether the difficulty of the step justifies the spend.
- Change one variable at a time: trim context, rewrite skill instructions, split a step into a subagent, or route a stage to a cheaper model, then rerun and compare quality plus cost.

## Evidence from practice

Named model and harness comparisons (Bridgewater and Thinking Machines, Spiral, OpenAI's stale-experiment audit, Anthropic's Haiku 5.5 tier split and effort analysis), routing built as infrastructure (eval data as the moat, Databricks, Arkadium, OpenRouter and Glean, AT&T, ScaleDown, decision models, the Every Agent), and cost-variance cases (Every's Sol spike, cost-normalized benchmarks, Cursor's agent swarm, Uber, Opus 5.5 and GPT-6.1 Sol per-task cost, Vals AI's agent-team study) now live on [Cost-aware routing: evidence from practice](cost-aware-routing-evidence.md).

## AI FinOps controls

AI cost discipline is becoming an operating function, not just a prompt-writing habit. Practical controls include:

- Treat access to expensive models as an allocation decision (token allocation as governance): set token budgets by role, team, workflow, or risk tier, route routine work to cheaper tools, and grant higher-cost access to workflows that can show returns in quality, speed, scope, or revenue impact.
- Reserve frontier or heavy-reasoning models for work where cheaper models, scripts, or humans are not sufficient.
- Require opt-in approval for long-running or high-effort agent modes.
- Track cache hit rates, prompt reuse, context length, and cost per successful task.
- Use cheaper defaults, model routing, warm-cache reuse, and lean context before restricting useful adoption.
- Measure shipped outcomes and human review burden, not raw token volume.
- Choose prompt-cache TTL by session idle-gap length, not a fixed default: Uber found its interactive sessions were frequently idle past the standard 5-minute cache window (forcing full-price prefix rebuilds), so it moved interactive sessions to a 1-hour TTL while keeping subagents — whose work is short-lived and focused — on 5 minutes.
- Cap context growth with a fixed auto-compaction threshold (e.g. 400K tokens) even on much larger context-window models, to control cache-burst and repeated-input costs rather than relying on the full window.
- Default reasoning effort to a middle tier (e.g. Medium) rather than maximum, since reasoning/output tokens bill at a multiple of input-token rates and a large share of tasks don't need top-tier reasoning to hit a good cost/quality balance. Raise it by how much checking the task needs, not by how hard it sounds. Anthropic's rule of thumb for Claude Code: low for in-the-loop sketching, medium for most feature work, high for verification-heavy work such as bugs in existing code, and max only for fully autonomous hard problems such as security audits. Where a reliable correctness check exists (tests, a verifier, a grader), a stricter policy beats any fixed tier: start at the lowest effort and retry at the highest only after a checked failure. A Johns Hopkins / Together AI study found this matched or beat fixed top effort on every model and benchmark it tested, usually at lower cost ([evidence](cost-aware-routing-evidence.md)).
- Pair spend visibility with staged behavioral nudges, not hard caps: a live per-session cost counter, a shared budget pool across interactive tools (separate tiers for managed agents), alerts at 50/80/100% of expected spend, and an on-demand dashboard that flags specific, named cost-anti-patterns (e.g. running simple sessions on an expensive model, stale-cache rebuilds after long idle gaps, 100K-token prompt-init overhead) each paired with its dollar impact — closer-to-real-time feedback than a single aggregate spend number.
- Without hard budgets, watch the payment rail and review after the fact: Every keeps a $500 automatic credit refill that posts a Slack alert at each top-up, treats a burst of top-ups as a cue to check the usage leaderboard, and asks three questions after any expensive run: what did it cost, what did it buy, what did we learn. A costly run that shows a new capability or limit is worth it; a modest result earns more spend only if it can be reproduced more cheaply. Every is turning this into a skill that gives each employee a personal AI-spending profit-and-loss statement.
- Give a premium model tier its own sub-budget. When Databricks gave about 3,500 engineers its top tier, it helped on complex long-range work, not routine coding, and coding spend rose about 60%; a separate allocation steers that tier to the work that benefits instead of making it everyone's default.
- Bring third-party AI tool spend under the company's own model account instead of handing each tool an API key: Anthropic's linked billing (beta, November 2026) links the organization once, with a monthly spend limit and spend visibility per tool. Requests run in the tool's organization, so the customer's IP allowlists, encryption keys, and retention settings do not apply. Details on [Claude Platform](../tools/claude-platform.md).

## Failure modes

- Spending frontier-model tokens on work a script could do exactly.
- Saving model cost while increasing human review burden.
- Letting flat-rate subscriptions hide runaway agent workloads until pricing or limits change.
- Treating model prestige as a routing rule. The Bridgewater case suggests expert data and task-specific tuning can matter more than using the newest frontier model.
- Treating local AI as just a model download. Local/open routing needs surrounding infrastructure: search, documents, agents, harnesses, deployment tooling, and clear escalation to frontier models when needed.
- Cutting model spend in a way that increases hidden human review cost.
- Treating token volume as adoption success after the organization has moved into a per-token or usage-based pricing regime.
- Calling a workflow "optimized" after reducing token spend without rechecking output quality, human review time, or failure-recovery cost.
- Letting the agent self-assess its own token inefficiency without human review; Every notes models are still poor judges of when their own spend is disproportionate.
- Treating maximum effort as the safe setting. Higher effort can fail tasks a lower setting solved, costs many times more on easy tasks, and turning reasoning off is no reliable saving in agent loops, since agents then run longer.
- Letting an orchestrator spawn agents "as needed" toward an open-ended goal ("until it is done extremely well"). Cap the number of subagents, cut coordination layers that only relay work, add human checkpoints, and give any judge a concrete target such as a reference image; Every's uncapped version burned 4.5 billion tokens in a day and a half, much of it on context passed between layers.

## Recent changes

- [2026-11-23] Split the three evidence groups (model and harness selection wins, routing as infrastructure, cost variance and budgeting tradeoffs) out to [Cost-aware routing: evidence from practice](cost-aware-routing-evidence.md); this page keeps the guidance, AI FinOps controls, and failure modes.
- [2026-11-17] Added a FinOps control for third-party tool spend: Anthropic's linked billing replaces shared API keys with an organization link, per-platform monthly spend limits, and spend visible per platform; the customer's own IP allowlists, encryption keys, and retention settings do not apply to those requests.
- [2026-10-25] Added escalate-on-checked-failure ("laddering") to the effort control and a max-effort failure mode, from a study showing higher effort loses tasks lower effort solved.
- [2026-10-19] Merged the "Cost and model routing" proven-patterns group from [Company-wide AI enablement](company-wide-ai-enablement.md): tasteful tokenmaxxing (depth over breadth), route by task novelty, and token allocation as governance (folded into AI FinOps controls); its efficiencymaxxing bullet duplicated this page's Current guidance and was not repeated.
- [2026-09-25] Added Anthropic's per-task effort rule of thumb (low for in-the-loop sketching, medium for most feature work, high for verification-heavy work, max for fully autonomous hard problems) to the middle-tier FinOps control.
- [2026-09-17] Added two FinOps controls (refill alerts plus three post-run questions; a premium-tier sub-budget, from Databricks' +60% coding spend) and the uncapped-swarm failure mode.

## Related

- [Cost-aware routing: evidence from practice](cost-aware-routing-evidence.md) - the case studies and cost data behind this page's guidance.
- [Company-wide AI enablement](company-wide-ai-enablement.md) - the broader adoption playbook; its tokenmaxxing and spend-shock failure modes are the problems this page's routing answers.
- [Agent autonomy and governance](agent-autonomy-and-governance.md) - "exploration budget, then governance" sequencing for when token allocation should start.

- [AI work delegation modes](ai-work-delegation-modes.md) - task-shape framework for choosing autonomous delegation versus close collaboration.
- [OpenAI discounted async processing](../workflows/async-discounted-processing.md) - lower-cost asynchronous execution for non-urgent OpenAI workloads (Flex on older models, discounted background windows on new ones).
- [Claude Fable 5.2 / Mythos 5.2](../models/claude-fable-5-2.md) - Anthropic's top tier; Anthropic advises starting most work on Opus 5.5 and moving up to Fable only for the most ambitious open-ended jobs, or using Fable as an advisor or orchestrator over cheaper models.
- [Claude Platform](../tools/claude-platform.md) - Anthropic's developer platform; linked billing and per-platform spend limits.
- [Claude Haiku 5.5](../models/claude-haiku-5-5.md) - Anthropic's current cheap/fast tier, pitched for subagent, compaction and high-volume routing slots.
- [Decision models](../concepts/decision-models.md) - non-generative models that return calibrated yes/no, choice and score answers; the cheapest tier for classification steps.

## Sources

- [Task routing and cost discipline - May 2026](../sources/newsletters/task-routing-cost-discipline-2026-05-13.md)
- [Thinking Machines - Learning to Replicate Expert Judgment in Financial Tasks](../sources/articles/thinking-machines-financial-expert-judgment-2026-07-02.md)
- [Superhuman - A $5B startup emerges from stealth](../sources/newsletters/superhuman-bridgewater-thinking-machines-2026-07-02.md)
- [Local AI as open-weight infrastructure](../sources/newsletters/local-ai-infrastructure-2026-06.md)
- [Token tightening and AI FinOps](../sources/newsletters/token-tightening-ai-finops-2026-06.md)
- [Efficiencymaxxing and model-routing discipline](../sources/newsletters/efficiencymaxxing-model-routing-2026-07.md)
- [Fable for unknowns and cheaper specialists for settled work](../sources/newsletters/fable-unknowns-routing-2026-07.md)
- [Uber Engineering — Running a Software Factory Efficiently at Uber Scale](../sources/tweets/ubereng-software-factory-2026-08-28.md)
- [AINews — Tasteful Tokenmaxxing](../sources/newsletters/ainews-2026-04-23.md)
- [Every — 33 Questions Executives Ask About AI—Answered](../sources/newsletters/every-33-questions-executives-2026-08-28.md)
- [Anthropic — Using Claude Code: Spending your effort](../sources/articles/claudedev-spending-your-effort-2026-09-25.md)
- [Linked billing on the Claude Platform](../sources/articles/claude-platform-linked-billing-2026-11-17.md)
- [Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2](../sources/articles/anthropic-claude-fable-mythos-5-2.md)
- [What Effort Level Should I Choose? — Johns Hopkins, Together AI, Cornell (arXiv)](../sources/papers/reasoning-effort-economics-2026-10.md)
- [Every — Why You Should Burn More Tokens](../sources/newsletters/every-burn-more-tokens-2026-09-17.md)
- [AINews — Databricks' Astra rollout and sub-budget](../sources/newsletters/ainews-databricks-astra-sub-budget-2026-09-17.md)
