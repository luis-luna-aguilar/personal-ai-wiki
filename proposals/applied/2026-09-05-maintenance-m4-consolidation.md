---
type: proposal
source: proposals/2026-09-05-maintenance-findings.md
status: pending
created: 2026-09-05
---

# Proposal: Maintenance M4 — concept/trend/training consolidation

## Summary

### The source

This is the third and most editorially delicate maintenance proposal. The maintenance report flagged that the wiki's concept, trend, and training pages — the ones that absorb newsletter clusters over months instead of getting one clean ingest — have sedimented: the same idea from the same source essay got written up on several pages instead of one, and two hub pages (harness/orchestration, company-wide enablement/agents-reshape-organizations) grew past 3,000 words each without ever linking to each other.

Before drafting, I re-read all twenty-six named pages in full rather than trusting the report's one-line summaries, since the report was itself a summary of a summary — and it overstated some of the duplication. The genuine verbatim overlaps were narrower than described: about a dozen pattern bullets shared between two pages, one framing and one mechanism duplicated near word-for-word between another two, and one concept (prompt injection's "lethal trifecta") fully explained on a training page while its own concept page sat as a stub. Two things the report called unresolved were already fixed by the prior maintenance proposal (the Fable-5-ban stale wording on five pages, and the 47%-vs-50/67% cognitive-debt figure) — dropped from this proposal entirely. Everywhere else — frame/framer on five pages, model neutrality on four, cost-routing on three — the prose turned out to be differentiated applications of the same idea to different contexts, not copies. Deleting it would lose content for no gain, so most of this proposal adds missing cross-links rather than cutting prose, reserving actual deletion for genuine near-duplicates.

### What changes

- **Harness ↔ orchestration patterns**: harness loses ~12 pattern bullets orchestration-patterns already states as well or better, keeps everything harness-specific (RL quality, security/permissions, CLI design, model-harness fit), and both pages get a `## Related` link to the other. The sidekick pattern, explained in full on three pages, keeps one full version (orchestration-patterns) and shrinks to a sentence on Devin and Advisor strategy.
- **Company-wide enablement ↔ agents-reshape-organizations**: reciprocal links added (currently zero either way despite nine shared sources); the two genuine duplicates — the McKinsey in-loop/above-the-loop framing and the Claudie trust-battery mechanism — each keep one full version and shrink to a linked sentence on the other page.
- **Agent Labs vs. Model Labs** gains its first `## Related` section (open-weight-momentum-broadens, harness, orchestration-patterns) — no prose cut, each page's treatment serves a different purpose.
- **Cost-aware AI task routing**, linked from nowhere today, gains inbound links from company-wide and orchestration-patterns; company-wide's "exploration budget" and "token governance" bullets get one clause resolving their apparent sequencing tension.
- **Frame/framer, cognitive debt, and skills-methodology** clusters each get the missing reciprocal links added, with no prose deleted — none of it was actually duplicated once read in full.
- **Prompt injection**, a 187-word stub, absorbs the "lethal trifecta" explanation (Willison's three-condition framework) that currently lives in full only on anti-autopilot-review-friction.md, which keeps a one-line pointer back; harness.md and evals-for-agentic-work.md get links to the concept page.
- **Three trend openers** (open-weight-momentum-broadens, voice-becomes-agent-interface, compute-infrastructure) get rewritten to match their own current content instead of their original ingest framing. Two Recent-changes entries about agent-execution infrastructure move from compute-infrastructure.md to agent-native-compute.md, the page split off from it in July.
- **A2A** gets its first inbound link, from mcp.md.
- **AI delegation management** (255 words, largely duplicates orchestration-patterns' loop-tempo material) is proposed for folding into ai-work-delegation-modes.md — left as an Open Question rather than drafted, since it implies deleting a page and AGENTS.md has no established convention for that.

### What to weigh

The compute-infrastructure entry split is my judgment call — of five tied `[2026-05-05]` entries, I moved only the two explicitly about sandbox/execution infrastructure and left three that didn't clearly fit; reasonable people could draw that line differently. The harness trim keeps every fact (the removed bullets are still on orchestration-patterns, just relocated), but the page reads noticeably shorter if you're used to its current length. The ai-delegation-management merge needs your call on mechanics — redirect stub, outright deletion, or just add a link and leave both pages.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/harness.md`, `wiki/workflows/agentic-orchestration-patterns.md` — trim ~12 pattern bullets from harness's "What good harness engineering looks like" that orchestration-patterns already states as well or better; move the narrow-scope-parallel-review point (Glasswing) to orchestration-patterns since harness's version is fuller; add a `## Related` line on harness pointing to the pattern catalog; add a `## Related` section to orchestration-patterns (currently has none) linking harness.md, agent-labs-vs-model-labs.md, and agent-skill-methodology.md
    > See draft below

- [ ] **Update** `wiki/tools/devin.md`, `wiki/workflows/advisor-strategy.md` — shrink the sidekick-pattern explanation on both pages to one sentence plus a link, since `agentic-orchestration-patterns.md` already carries the fullest version
    > See draft below

- [ ] **Update** `wiki/training/company-wide-ai-enablement.md`, `wiki/trends/agents-reshape-organizations.md` — add reciprocal `## See also`/`## Related concepts` links; trim the McKinsey in-loop/above-the-loop bullet on the trend page to one linked sentence (company-wide has the fuller section); trim the Claudie trust-battery bullet on company-wide to one linked sentence (the trend page's version is the fuller evidence-signal writeup)
    > See draft below

- [ ] **Update** `wiki/concepts/agent-labs-vs-model-labs.md` — add a `## Related` section (page currently has none)
    > See draft below

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md`, `wiki/training/company-wide-ai-enablement.md`, `wiki/workflows/agentic-orchestration-patterns.md` — add inbound links to cost-aware-ai-task-routing.md from the other two pages; resolve the unaddressed "exploration budget vs. token governance" sequencing tension on company-wide with one clause
    > See draft below

- [ ] **Update** `wiki/concepts/agent-evals.md`, `wiki/training/ai-work-delegation-modes.md`, `wiki/training/ai-native-product-building.md`, `wiki/training/company-wide-ai-enablement.md`, `wiki/trends/agents-reshape-organizations.md` — add the missing reciprocal links across the "frame vs. framer" cluster (agent-evals already links out; the other four don't link each other). No prose removed — each page's treatment is a distinct application of the idea, not a duplicate.
    > See draft below

- [ ] **Update** `wiki/workflows/ai-pr-code-review.md`, `wiki/training/ai-native-product-building.md` — add links from their one-line cognitive-debt mentions to the fuller treatment on `anti-autopilot-review-friction.md` (the number reconciliation itself was already added by the prior maintenance proposal)
    > See draft below

- [ ] **Update** `wiki/training/agent-skill-methodology.md`, `wiki/workflows/skillify-agent-reliability.md` — add a `## Related` section to agent-skill-methodology.md (currently has none) linking skillify-agent-reliability.md and agentic-orchestration-patterns.md; add agent-skill-methodology.md to skillify's existing `## Related` list
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md`, `wiki/trends/voice-becomes-agent-interface.md`, `wiki/trends/compute-infrastructure.md`, `wiki/trends/agent-native-compute.md`, `wiki/trends/agents-reshape-organizations.md` — rewrite three stale trend openers to match their own current content; move two agent-execution-layer Recent-changes entries from compute-infrastructure.md to agent-native-compute.md; tighten agents-reshape-organizations.md's first open question given the volume of independent evidence accumulated since it was written
    > See draft below

- [ ] **Update** `wiki/concepts/prompt-injection.md`, `wiki/training/anti-autopilot-review-friction.md`, `wiki/concepts/harness.md`, `wiki/training/evals-for-agentic-work.md` — expand the prompt-injection stub with the "lethal trifecta" framing currently duplicated in full on anti-autopilot-review-friction.md (which keeps a one-line pointer); add links from harness.md and evals-for-agentic-work.md's passing mentions of injection risk
    > See draft below

- [ ] **Update** `wiki/concepts/mcp.md` — add one sentence linking `wiki/concepts/a2a.md`, which currently has no inbound content links
    > See draft below

## Page drafts

### wiki/concepts/harness.md (updated)

Replace the `## What good harness engineering looks like` section in full:

```md
## What good harness engineering looks like

Most of the field's accumulated patterns for harness design — ambiguity gates, scoped context, failure-aware replanning, eval-driven simplification, skills as the reusable abstraction, hook-based reliability plumbing, externalized knowledge layers, robust loop primitives, decoupled shared context with isolated execution, the dark/light factory split, and the mayor-and-polecats worker topology — are cataloged with fuller detail on [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md). What follows are the points specific to harness *architecture* rather than orchestration *pattern*:

- **Layered memory** keeps durable knowledge, topic files, and live-session context separate instead of forcing everything into one rolling transcript.
- **Repo-state awareness** gives the agent current branch, recent commits, and file-level state so it acts on the real workspace instead of a stale abstract summary.
- **Permission boundaries** stay explicit. Good harnesses make it legible when the agent is allowed to act, when it must ask, and where risky execution is isolated.
- **Cache-efficient subagent parallelism** lets worker agents inherit enough shared context to be useful without rebuilding the full setup cost every time.
- **Critique-loop orchestration** over flat parallel dispatch: a generator agent + a separate critic model reviewing the output + the generator redoing the work based on the critique produces higher-quality output than equivalent compute spent on parallel independent agents. Observed by Shopify at scale; slower but more reliable for tasks with clear correctness signals.
- **CI/CD as part of the harness boundary**: at sufficient agent throughput (e.g. 30% MoM PR growth), deployment and verification infrastructure becomes the bottleneck. Harness design must account for the downstream pipeline, not only the generation loop.
- **Agent-friendly CLI design.** Tools built for human interactive use break agent pipelines: interactive prompts stall agents, undocumented flags require inference, and missing non-interactive modes force workarounds. Agent-facing CLI tools should be non-interactive by default, expose all behaviors through explicit flags, and document internal conventions. This applies equally to the tools the agent calls and to the CLIs agents themselves expose.
- **DSPy 3.2** (April 2026) as a harness engineering toolchain: adds Reinforced Language Model (RLM) improvements, optimizer chaining, and LiteLLM decoupling. Relevant for teams iterating on harness prompts and orchestration logic using programmatic optimization.
- **Model-harness fit.** Coding-agent performance depends on how well the surrounding harness matches the model's preferred edit format, action space, tool-call style, and failure recovery patterns. A strong model can underperform in a mismatched harness.
- **Measure effective feedback, not only activity.** Raw token counts, tool counts, and trace length are weak proxies for agent success. AINews coverage of Effective Feedback Compute argues that the useful signal is whether the harness gives the model actionable feedback that improves the next step.
- **Model-specific harness profiles.** LangChain Deep Agents coverage suggests that Qwen, Kimi, DeepSeek, and frontier closed models can require different prompts, tools, and memory layouts. A cheaper model can become viable when the harness matches its operating style.
- **LLM proxy as the fleet management layer.** At org scale (Shopify, 23K engineers), routing all AI coding-tool traffic through a centralized LLM proxy creates a control plane for cost, model choice, and policy enforcement without requiring per-tool reconfiguration. This positions the proxy as part of the enterprise harness boundary — above the individual tool harness, below the model.
- **Multi-model parallel code review.** Submitting the same code to Claude, Codex, and Kimi simultaneously in parallel finds different bugs than running one model three times. Three different models with different training distributions catch issues each would miss alone. Higher signal per review cycle at the cost of higher parallel token spend.
- **Model neutrality by design.** Build your harness so the underlying model is a configurable parameter, not a hardcoded dependency — routing, context packaging, and evaluation should live in the harness layer, not in model-specific prompt tricks. LangChain's LangSmith Engine, which automatically consumes production traces, clusters failures, identifies likely code issues, and proposes fixes and evals, demonstrates that the evaluation layer can also be decoupled from frontier access. See [Agent Labs vs Model Labs](agent-labs-vs-model-labs.md) for the competitive-moat argument this connects to.
- **Org-embedded identity and permissioning.** Slack-native and team-channel agents need a legible identity, scoped access to channels/tools/data, audit trails for actions, and memory boundaries that match how the organization actually partitions work. Without that, the harness becomes an organizational risk surface: unclear accountability, prompt-injection exposure, budget opacity, and channel noise.
- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution. Google adding these to the Gemini API is another sign that "harness" is becoming product infrastructure, not only application code. Anthropic's Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview) in May 2026: the agent loop that handles orchestration, context management, and error recovery stays on Anthropic's infrastructure, while tool execution and private MCP connectivity run on customer-controlled infrastructure or a supported sandbox provider (Cloudflare, Daytona, Modal, Vercel).
- **Security boundary as harness boundary.** Tool-using agents are not only productivity systems; they are software components that may read untrusted content, hold private context, and take actions. A production harness must define identity, permissions, data exfiltration boundaries, guardrails, red-team tests, and audit trails as part of the agent architecture — see [Prompt injection](prompt-injection.md) for the concrete attack pattern this defends against.
- **Code as the operational substrate, not just output.** A May 2026 survey ("Code as Agent Harness," arXiv:2605.18747) frames code as the shared medium connecting agent reasoning, acting, and environment modeling — not merely the artifact an agent produces. It organizes harness design around three layers: the interface where code links reasoning/action/environment; harness mechanisms (planning, memory, tool use, feedback-driven control); and scaling from single-agent to multi-agent settings, where shared code artifacts support coordination, review, and verification.
```

Add to `## Related` (full section):

```md
## Related

- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — the pattern catalog for agent loop design, escalation, and multi-agent topology; this page covers harness architecture, that page covers reusable operating patterns
- [Agent evals](agent-evals.md) — taxonomy of agent evaluation categories and why trajectory quality matters alongside final results
- [Agent improvement loop](agent-improvement-loop.md) — the loop for improving a harness systematically via traces, evals, and targeted changes
- [Skillify — Agent Reliability Pattern](../workflows/skillify-agent-reliability.md) — pattern for encoding agent failures as permanent tested skills; "thin harness / fat skills" architecture
- [Prompt injection](prompt-injection.md) — the concrete security attack the harness security boundary defends against
```

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Add one new pattern bullet to `## Current patterns` (after "Sandboxed executors for evidence-producing steps"):

```md
- **Narrow-scope parallel agents outperform exhaustive single agents in high-coverage tasks.** Cloudflare's Project Glasswing harness (8 stages, ~50 concurrent Mythos Preview agents) demonstrates this at security-research scale: each agent has one tightly scoped attack class + one target area; an independent adversarial agent validates but cannot emit new findings; root-cause deduplication collapses variant findings. The Trace stage further splits "is this buggy?" from "can an attacker reach this bug?" — a clean instance of decomposing a compound question into two separately answerable ones.
```

Add a new `## Related` section (page currently has none) directly before `## Sources`:

```md
## Related

- [Harness (agent)](../concepts/harness.md) — harness architecture; this page covers the reusable operating patterns built on top of it
- [Agent Labs vs Model Labs](../concepts/agent-labs-vs-model-labs.md) — the model-neutrality argument behind harness-level model routing
- [Agent skill methodology](../training/agent-skill-methodology.md) — how to author the skills referenced in the "share skills, not just code" and progressive-disclosure patterns above
```

### wiki/tools/devin.md (updated)

Replace the sidekick sentence in `## Current status` (the "Devin Fusion (preview)" bullet):

> **Before:** `- **Devin Fusion (preview):** a multi-model "sidekick" harness — a frontier model runs alongside a cheaper sidekick model, each a fully capable agent with its own tools and persistent, separately-cached context; the frontier model plans, interprets ambiguity, and reviews, while delegating mechanical or well-scoped work to the sidekick; a lightweight classifier can reassign which model leads mid-session, timed to coincide with context-compaction points so the switch doesn't cost an extra cache miss`
>
> **After:** `- **Devin Fusion (preview):** applies the [sidekick multi-model harness pattern](../workflows/agentic-orchestration-patterns.md) — a frontier model and a cheaper model run as two persistent, separately-cached agents, with the frontier model planning and reviewing while the sidekick handles mechanical work.`

### wiki/workflows/advisor-strategy.md (updated)

Replace `## Contrast with the sidekick pattern (2026-06-29)` in full:

```md
## Contrast with the sidekick pattern (2026-06-29)

Cognition's Devin Fusion critiques per-call escalation tools like this one: querying a second model per call means that model's context isn't shared in a cacheable way, so every advisor invocation pays a full, uncached price. The [sidekick pattern](../workflows/agentic-orchestration-patterns.md) avoids this by running both models as persistent, separately-cached agents for the whole session. The tradeoff: sidekick needs a harness built for two parallel long-running agents, while the advisor tool is a single API primitive addable to an existing single-agent loop.
```

### wiki/training/company-wide-ai-enablement.md (updated)

Replace the "Trust battery with judge agent" bullet in `## Proven patterns`:

> **Before:** `- **Trust battery with judge agent.** Grant autonomy incrementally rather than all at once. Implement a nightly judge agent that reviews interactions, scores behavior, adjusts a trust percentage, and lets the primary agent self-update memory from negative feedback. Start at a deliberately low trust level (Every's Claudie: 20% vs 50% for human new hires) and let the agent earn scope through demonstrated reliability rather than through time or configuration changes.`
>
> **After:** `- **Trust battery with judge agent.** Grant autonomy incrementally, tied to demonstrated reliability rather than elapsed time — see [Agents reshape organizations](../trends/agents-reshape-organizations.md) for the concrete Claudie mechanism (nightly judge agent, starting trust percentage, self-updating memory).`

Resolve the exploration-budget/token-governance sequencing tension by adding one clause to the "Exploration budget" bullet:

> **Before:** `- **Exploration budget.** Removing token caps and access restrictions gives people room to discover high-leverage use cases before ROI is obvious`
>
> **After:** `- **Exploration budget, then governance.** Removing token caps and access restrictions gives people room to discover high-leverage use cases before ROI is obvious — treat this as the deliberate first phase, with [token allocation as governance](#proven-patterns) (below) as the second phase once a workflow's value is established, not a contradiction to resolve.`

Add to `## See also` (full section):

```md
## See also

- [Agents reshape organizations](../trends/agents-reshape-organizations.md) — the trend-level evidence (GitHub commit growth, Stanford labor data, Ramp's internal numbers) that this page's guidance responds to
- [AI enablement — software development](ai-enablement-software-development.md) — engineering-specific patterns: critique loops, CI/CD as bottleneck, Shopify evidence, junior talent pipeline
- [Agentic infrastructure operations](agentic-infrastructure-operations.md) — practical guidance for safe agent use around production infrastructure, deployment safety, and post-action verification
- [Evals for workflow and task agents](evals-for-agentic-work.md) — eval patterns for workflow and task agents: reliability metrics, task-specific patterns, simulated users
- [Cost-aware AI task routing](cost-aware-ai-task-routing.md) — the mechanics behind the token-allocation and efficiencymaxxing guidance above
```

### wiki/trends/agents-reshape-organizations.md (updated)

Replace the McKinsey bullet in `## Concrete signals`:

> **Before:** `- **McKinsey names the bottleneck: workflow redesign, not technology.** "AI is Everywhere. The Agentic Organization Isn't Yet" (McKinsey, 2026) reports that 80%+ of companies are not seeing bottom-line impact from AI investments despite large spending. The diagnosis: companies are running pilots inside unchanged processes rather than redesigning workflows end-to-end. The unlock is "end-to-end workflow reimagination" — rethinking the entire process (e.g., insurance underwriting, hire-to-onboard) rather than speeding up individual tasks. McKinsey introduces the distinction between humans "in the loop" (executing parts of a workflow) vs. "above the loop" (providing judgment over an agent-run process) as the structural end state for knowledge work.`
>
> **After:** `- **McKinsey names the bottleneck: workflow redesign, not technology.** "AI is Everywhere. The Agentic Organization Isn't Yet" (McKinsey, 2026) reports that 80%+ of companies are not seeing bottom-line impact from AI investments despite large spending — see [Company-wide AI enablement](../training/company-wide-ai-enablement.md) for the full in-loop/above-the-loop framing and a worked example.`

Replace `## Related concepts` in full:

```md
## Related concepts

- [Agentic thinking](../concepts/agentic-thinking.md) — Junyang Lin argues the competitive edge is shifting from model training to environment design and harness engineering, reinforcing the thesis that organizational leverage matters more than individual model capability
- [Company-wide AI enablement](../training/company-wide-ai-enablement.md) — the operating guidance and proven patterns organizations are using to act on this trend
```

Replace the first `## Open questions` bullet:

> **Before:** `- Is this trend already happening in practice, or is it mostly Twitter / vendor-blog narrative? We now have a stronger first-party Ramp data point, but still need more independent or cross-company reporting before treating it as settled.`
>
> **After:** `- Is this trend already happening in practice, or is it mostly Twitter / vendor-blog narrative? The evidence base has broadened well beyond a single vendor claim — GitHub's own commit-volume data, Stanford's 25,000-firm labor study, and Cursor's internal PR data are now independent, first-party or academic sources rather than blog framing. What's still missing is reporting from outside the AI-tooling/big-tech cluster itself: no non-engineering, non-AI-lab company has yet published its own version of these numbers.`

### wiki/concepts/agent-labs-vs-model-labs.md (updated)

Add a new `## Related` section directly before `## Sources`:

```md
## Related

- [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md) — carries the model-sovereignty argument (open weights as the practical escape hatch from single-vendor dependence) that this page's "model neutrality becomes rational" point connects to
- [Harness (agent)](harness.md) — "model neutrality by design" as a concrete harness-architecture principle
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — where harness-level model routing shows up as an operating pattern
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

No content change — this page is the link target for the two additions below; nothing on it needs to change.

### wiki/training/company-wide-ai-enablement.md (updated, second edit)

Add one sentence to the "Efficiencymaxxing as model-routing practice" bullet in `## Proven patterns`:

> **Before:** `- **Efficiencymaxxing as model-routing practice.** Treat model selection like an operating system for work: use evals to identify which workflow stages can move to cheaper models, audit token use by step, and keep frontier access for ambiguous or high-risk stages. This is the practical middle ground between tokenmaxxing and blanket restriction.`
>
> **After:** `- **Efficiencymaxxing as model-routing practice.** Treat model selection like an operating system for work: use evals to identify which workflow stages can move to cheaper models, audit token use by step, and keep frontier access for ambiguous or high-risk stages. This is the practical middle ground between tokenmaxxing and blanket restriction. See [Cost-aware AI task routing](cost-aware-ai-task-routing.md) for the routing mechanics and FinOps controls this practice depends on.`

### wiki/workflows/agentic-orchestration-patterns.md (updated, second edit)

Add one sentence to the "Cost-aware loop primitives" bullet in `## Current patterns`:

> **Before:** `- **Cost-aware loop primitives.** Use scripts for deterministic work, run small pilots before dynamic workflows that may spawn many agents, choose cheaper/faster models for routine parts, and monitor \`/usage\`, \`/goal\`, and \`/workflows\` breakdowns.`
>
> **After:** `- **Cost-aware loop primitives.** Use scripts for deterministic work, run small pilots before dynamic workflows that may spawn many agents, choose cheaper/faster models for routine parts, and monitor \`/usage\`, \`/goal\`, and \`/workflows\` breakdowns. See [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) for the fuller routing framework.`

### wiki/concepts/agent-evals.md (updated)

No content change — already links to `ai-work-delegation-modes.md` in `## Related`; this page is the one place in the cluster that was already correctly cross-linked.

### wiki/training/ai-work-delegation-modes.md (updated)

Add a `## Related` section (page currently has none) before `## Sources`:

```md
## Related

- [Agent evals](../concepts/agent-evals.md) — the benchmark-framing half of Every's "After Automation" argument; this page covers the task-delegation half
- [AI-native product building](ai-native-product-building.md) — the "AI sandwich" pattern applied specifically to product-building work
- [Agents reshape organizations](../trends/agents-reshape-organizations.md) — the same framing applied at org-design scale
```

### wiki/training/ai-native-product-building.md (updated)

Add a link to the "AI sandwich for product work" bullet in `## Proven patterns`:

> **Before:** `- **AI sandwich for product work.** Humans supply the bread: intent, context, taste, and final judgment. AI handles much of the middle: drafting, coding, gathering, summarizing, and first-pass execution.`
>
> **After:** `- **AI sandwich for product work.** Humans supply the bread: intent, context, taste, and final judgment. AI handles much of the middle: drafting, coding, gathering, summarizing, and first-pass execution. See [AI work delegation modes](ai-work-delegation-modes.md) for the general task-level version of this split.`

Add a link to the "Fight cognitive debt deliberately" bullet:

> **Before:** `- **Fight cognitive debt deliberately.** Use walkthroughs, explanations, and other artifacts that make generated systems understandable enough to extend safely later`
>
> **After:** `- **Fight cognitive debt deliberately.** Use walkthroughs, explanations, and other artifacts that make generated systems understandable enough to extend safely later — see [Anti-autopilot review friction](anti-autopilot-review-friction.md) for the underlying research and prescriptions.`

### wiki/training/company-wide-ai-enablement.md (updated, third edit)

Add a link to the "Design for new frames" bullet in `## Proven patterns`:

> **Before:** `- **Design for new frames, not only task automation.** Cheap competence means more work can be done inside a given frame, but the higher-value organizational skill is creating better frames: what to investigate, what to ship, what tradeoff matters, and what "good" means.`
>
> **After:** `- **Design for new frames, not only task automation.** Cheap competence means more work can be done inside a given frame, but the higher-value organizational skill is creating better frames: what to investigate, what to ship, what tradeoff matters, and what "good" means. See [AI work delegation modes](ai-work-delegation-modes.md) for the task-level version of this argument.`

### wiki/workflows/ai-pr-code-review.md (updated)

Add a link to the "Cognitive debt" failure mode:

> **Before:** `- **Cognitive debt:** humans approve code they cannot explain, which weakens their ability to direct future agent work.`
>
> **After:** `- **Cognitive debt:** humans approve code they cannot explain, which weakens their ability to direct future agent work — see [Anti-autopilot review friction](../training/anti-autopilot-review-friction.md) for the underlying studies and remedies.`

### wiki/training/agent-skill-methodology.md (updated)

Add a `## Related` section (page currently has none) before `## Sources`:

```md
## Related

- [Skillify — Agent Reliability Pattern](../workflows/skillify-agent-reliability.md) — the 10-step checklist for turning a specific production failure into a tested skill; this page covers the general authoring method
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — where "share skills, not just code" and progressive disclosure show up as operating patterns
```

### wiki/workflows/skillify-agent-reliability.md (updated)

Add one line to `## Related`:

> **Before:** `- [Harness (agent)](../concepts/harness.md) — the thin harness is the other half of the "thin harness / fat skills" duality`
>
> **After:** `- [Harness (agent)](../concepts/harness.md) — the thin harness is the other half of the "thin harness / fat skills" duality
> - [Agent skill methodology](../training/agent-skill-methodology.md) — the general skill-authoring method this pattern's `SKILL.md` step draws on`

### wiki/trends/open-weight-momentum-broadens.md (updated)

Replace the opening paragraph:

> **Before:** `The trend: by early April 2026, open-weight momentum was no longer only a coding-model story. Gemma 4 supplied a stronger open multimodal signal with visible adoption, while Holo3 suggested that even computer-use models were entering the open-weight competition with concrete benchmark and price claims.`
>
> **After:** `The trend: open-weight momentum has broadened well past its original coding-model story. What started in early April 2026 with Gemma 4's multimodal signal and Holo3's computer-use claims has, by July, become a story about a structural split (Sarah Guo's Agent Labs vs. Model Labs framing), a new first-party US entrant (NVIDIA's Nemotron 3 Ultra), a previously-closed lab going fully open (Cohere), and open weights becoming explicit risk-management infrastructure after the Fable 5 export-control ban.`

Replace the "What to watch" section:

> **Before:**
> ```md
> ## What to watch
>
> - Whether Gemma 4 becomes a durable reference point in open multimodal deployment rather than only a popular release
> - Whether open computer-use models like Holo3 gain credible third-party validation beyond launch claims
> - Whether this broadening leads to new stable subcategories or simply stronger challenger entries inside existing ones
> ```
>
> **After:**
> ```md
> ## What to watch
>
> - Whether NVIDIA sustains Nemotron as a recurring open-weight release cadence or treats it as a one-off signal
> - Whether more previously-closed labs (following Cohere) ship fully open flagship models
> - Whether this broadening leads to new stable subcategories or simply stronger challenger entries inside existing ones
> ```

### wiki/trends/voice-becomes-agent-interface.md (updated)

Replace the opening paragraph:

> **Before:** `The late-March signal is that voice is no longer just an add-on to chat products. Texting your AI, smoother real-time voice agents, and open-weight TTS releases all point to conversational audio becoming part of the practical agent stack.`
>
> **After:** `Voice is becoming a practical agent interface rather than a chat add-on. What started in late March as texting-your-AI and open-weight TTS signals has, by July, produced GPT-Live's full-duplex voice layer with background task delegation — the clearest evidence yet that conversational audio and task execution are separating into distinct layers of the agent stack.`

### wiki/trends/compute-infrastructure.md (updated)

Replace the title-adjacent framing in the intro paragraph:

> **Before:** `Frontier AI labs are securing compute capacity at a scale that creates structural competitive advantages beyond what algorithm quality alone can overcome. As of 2026, access to multi-gigawatt compute is diverging rapidly between labs with strategic infrastructure partnerships and those without.`
>
> **After:** `Frontier AI labs are securing compute capacity at a scale that creates structural competitive advantages beyond what algorithm quality alone can overcome — but by mid-2026 the page's own evidence carries as many counterforces to that moat (open-weight models competing with far less disclosed infrastructure, runtime and inference-systems efficiency gains, hybrid local/cloud routing, and the "outputmaxxing" argument that utilization matters as much as cluster size) as signals reinforcing it. As of 2026, access to multi-gigawatt compute is diverging rapidly between labs with strategic infrastructure partnerships and those without, but the compute-moat thesis should be read alongside its limits, not in isolation.`

Remove two entries from `## Recent changes` (they move to `wiki/trends/agent-native-compute.md`, drafted below):

> **Before (two of the five `[2026-05-05]` entries, in context):**
> ```md
> - [2026-05-05] Manus Cloud Computer: persistent Ubuntu environments with SSH/web-terminal access and tool state that survives across agent sessions; durable-agent runtime as an infrastructure category distinct from ephemeral-per-task containers
> - [2026-05-05] Parallel Web Systems raised at a $2B valuation (secondary coverage) for internet/research APIs optimized for AI agents — market signal that agent-oriented web access infrastructure is becoming a standalone investable category
> - [2026-05-05] AINews "inference inflection" framing: inference throughput is the dominant current bottleneck, and agent systems add a compound requirement — CPU, sandbox, browser, and execution capacity matter alongside GPU for production agent workloads
> ```
>
> **After (Manus and the inference-inflection entry removed; Parallel Web Systems and the other two 05-05 entries stay unchanged):**
> ```md
> - [2026-05-05] Parallel Web Systems raised at a $2B valuation (secondary coverage) for internet/research APIs optimized for AI agents — market signal that agent-oriented web access infrastructure is becoming a standalone investable category
> ```

### wiki/trends/agent-native-compute.md (updated)

Add two entries to `## Recent changes`, in date order (both dated before the existing 2026-05-20 entry):

> **Before (top of the list):** `- [2026-07-08] Modal detailed its shift from developer experience to agent experience, its $355M Series C, and 100,000-sandbox RL rollout workloads.`
>
> **After (unchanged top entries, two new entries appended at the bottom in date order, after the existing 2026-05-20 entry):**
> ```md
> - [2026-05-20] Railway detailed its agent-native infrastructure thesis: bare-metal 3-month payback, Central Station, agent-safe production forks, and the "pull request is dying" argument for CLI-first agent interfaces.
> - [2026-05-05] AINews "inference inflection" framing: inference throughput is the dominant bottleneck for production agent workloads, and agent systems add a compound requirement — CPU, sandbox, browser, and execution capacity matter alongside GPU. Originally recorded on [Compute infrastructure](compute-infrastructure.md); relocated here as the execution-layer analog once this page split off from it.
> - [2026-05-05] Manus Cloud Computer: persistent Ubuntu environments with SSH/web-terminal access and tool state that survives across agent sessions — durable-agent runtime as an infrastructure category distinct from ephemeral-per-task containers. Originally recorded on [Compute infrastructure](compute-infrastructure.md); relocated here as the execution-layer analog once this page split off from it.
> ```

### wiki/concepts/prompt-injection.md (updated)

Replace the page body in full (frontmatter `sources:` gains `lennysan-simonw-interview`):

```md
---
title: Prompt injection
type: concept
domains: [cybersecurity, agents]
tags: [agentic]
as_of: 2026-06-22
sources: [gray-swan-ai-security-2026-06, lennysan-simonw-interview]
---

# Prompt injection

Prompt injection is an attack where instructions from untrusted content override or redirect an AI system's intended behavior. In agent systems, the most important variant is indirect prompt injection: the attacker does not prompt the model directly. They place malicious instructions in a webpage, file, ticket, email, repo, document, or other content the agent later reads.

## Current status

- The risk is highest when an agent combines untrusted content, private data, and authority to take actions or exfiltrate information.
- Coding agents and computer-use agents are especially exposed because they routinely read repos, webpages, logs, issues, browser state, and other externally controlled text.
- Prompt injection is not solved by asking the model to "ignore malicious instructions"; production systems need permissions, data boundaries, tool controls, guardrails, and adversarial tests.

## The lethal trifecta

Simon Willison's framing names the exact condition under which prompt injection becomes unfixable with current techniques: when an agent has **all three** of —

1. Access to private data
2. Exposure to untrusted content (incoming emails, scraped web pages, third-party documents)
3. The ability to send data externally (reply to email, post to an API, write to a public channel)

— a malicious instruction hidden in the untrusted content can override the agent's intended behavior and use its own access and authority to exfiltrate the private data. No prompt-level defense reliably closes this gap once all three conditions hold; Willison has predicted a "Challenger disaster" for AI security if a major exploit along these lines hasn't already happened quietly. The practical review question for any new agent design: does this agent have all three legs of the trifecta? If so, the fix is architectural (remove one leg) rather than a better system prompt.

## Why it matters

Prompt injection turns useful agent behavior into an attack surface. The same capability that lets an agent read context and act across tools also lets hostile context steer the agent unless the harness constrains what the model can see, do, and transmit. See [Harness (agent)](harness.md) for how the security boundary is meant to sit inside overall harness design.

## Sources

- [Gray Swan AI security interview](../sources/newsletters/gray-swan-ai-security-2026-06.md)
- [Lenny Rachitsky — Simon Willison interview takeaways](../sources/tweets/lennysan-simonw-interview.md)
```

### wiki/training/anti-autopilot-review-friction.md (updated)

Replace the "lethal trifecta" failure mode with a one-line pointer:

> **Before:** `- **The "lethal trifecta" of agent security (Simon Willison).** When an AI agent has access to private data AND exposure to untrusted content (incoming emails, scraped web pages) AND the ability to send data externally (reply to email, post to an API), prompt injection cannot be reliably prevented. Any malicious instruction in untrusted content can override the agent's intended behavior. This trifecta cannot be reliably solved with current techniques, and Willison predicts a "Challenger disaster" for AI security if it hasn't already happened. Review criteria for new agent designs: does this agent have all three legs of the trifecta?`
>
> **After:** `- **The "lethal trifecta" of agent security.** See [Prompt injection](../concepts/prompt-injection.md) for Simon Willison's three-condition framework — private data, untrusted content, and an external send channel together make prompt injection unfixable with current techniques.`

### wiki/concepts/harness.md (updated, second edit)

Already handled above — the "Org-embedded identity and permissioning" bullet in the rewritten `## What good harness engineering looks like` section keeps its existing reference to prompt-injection exposure in passing; the new "Security boundary as harness boundary" bullet (also in that same draft above) now links directly to `prompt-injection.md`.

### wiki/training/evals-for-agentic-work.md (updated)

Add a link to the "Assurance" dimension:

> **Before:** `- **Assurance** — safety, policy adherence, and security: does the agent resist prompt injection? Does it prevent PII leakage? Does it stay within its authorized boundaries?`
>
> **After:** `- **Assurance** — safety, policy adherence, and security: does the agent resist [prompt injection](../concepts/prompt-injection.md)? Does it prevent PII leakage? Does it stay within its authorized boundaries?`

### wiki/concepts/mcp.md (updated)

Add one sentence to `## Why it matters`:

> **Before:** `- Helps separate the agent harness problem from the underlying model problem`
>
> **After:** `- Helps separate the agent harness problem from the underlying model problem
> - Complements [Agent2Agent (A2A)](a2a.md): MCP is about how one agent reaches tools and context, A2A is about how one agent delegates and coordinates with another`

## Open questions

- **AI delegation management merge.** `wiki/training/ai-delegation-management.md` is 255 words on two sources and largely restates the loop-tempo material already on `agentic-orchestration-patterns.md` ("Loop tempo selection"). Its genuinely distinct content — delegation as a management skill, estimating success probability before delegating, writing delegation documents with explicit authority limits and checkpoints — would fit naturally as a new "Managing the handoff" section on `wiki/training/ai-work-delegation-modes.md`. I did not draft this merge because it implies deleting a live page, and AGENTS.md has no established convention for that (only for archiving superseded tool/model versions to `wiki/history/`). Options: (a) merge the content in and delete the source page, (b) merge the content in and leave the old page as a short redirect stub, or (c) leave both pages as they are and just add a cross-link in each direction — the lightest-touch option, and the one I'd default to if you'd rather not decide page-deletion mechanics right now. Let me know which and I'll draft it.
- **Compute-infrastructure entry split.** I moved the two `[2026-05-05]` Recent-changes entries that explicitly named sandbox/execution infrastructure (Manus Cloud Computer, the AINews inference-inflection framing) to `agent-native-compute.md`, and left three others (Stripe compute fraud, Parallel Web Systems, Big Tech capex) on `compute-infrastructure.md`. If you'd rather move Parallel Web Systems too (it's agent-facing infrastructure, just not sandbox-specific), say so and I'll adjust.
