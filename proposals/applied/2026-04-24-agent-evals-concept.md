---
type: proposal
source: raw/deep-research/2026-04-23 Agents Evals.md
status: pending
created: 2026-04-24
---

# Proposal: Agent eval taxonomy and trajectory framing

## Summary

Agent evaluation differs fundamentally from model evaluation because you are testing `model + harness + tools + environment` as one system. The core new idea: a trajectory eval measures the path an agent took to reach an answer, not just whether the answer was correct. This is the conceptual scaffolding that makes the rest of the eval signals coherent.

## Intended changes

- [x] **Create** `wiki/concepts/agent-evals.md` — new concept page on agent evaluation taxonomy and trajectory framing
    > See draft below

- [x] **Update** `wiki/concepts/harness.md` — add trajectory eval framing to the evaluation layer bullet; add wikilink to `agent-evals`
    > **Before (in `## What a harness includes`):**
    > `- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended`
    > **After:**
    > `- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended; see [[concepts/agent-evals]] for the taxonomy of eval categories and the trajectory-vs-result distinction`

- [x] **Create** `wiki/sources/deep-research/2026-04-23-agents-evals.md` — source summary for the research report
    > See draft below

- [x] **Update** `wiki/index.md` — add `[[concepts/agent-evals]]` entry under Concepts; add source type note
    > **Add under Concepts:**
    > `- [[concepts/agent-evals]] — taxonomy of agent evaluation categories and the trajectory-vs-result distinction *(as_of: 2026-04-23)*`

## Page drafts

### wiki/concepts/agent-evals.md (new)

````md
---
title: Agent evals
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Agent evals

Evaluating an AI agent is not the same as evaluating an AI model. When you run a coding agent, you are not testing the underlying model in isolation — you are testing the combined system: `model + harness (orchestration layer, prompts, tool schemas) + tools + environment`. A change to any of those layers can change agent behavior even when the model itself has not changed.

This means the field of "agent evals" is really about evaluating systems and behaviors — trajectories, tool use patterns, policy adherence — rather than output quality alone.

## Why trajectory matters

Two agents can reach the same correct answer via entirely different paths. One got there efficiently in three steps. The other hallucinated a tool call, self-corrected, read thirty irrelevant files, and eventually succeeded. A result-only check marks both as passing. A trajectory eval catches the broken one.

This is why trajectory evaluation is central to agent quality: the path an agent takes reveals its planning quality, tool efficiency, and failure risk — none of which are visible from the final answer alone.

## Five eval categories

A well-structured agent eval suite covers five distinct categories, each catching different kinds of failure:

- **Capability** — can the agent perform the task at all? Establishes the baseline intelligence of the system before worrying about efficiency or robustness.
- **Regression** — did a change to the prompt, tools, or underlying model break something that was previously working? Run after any harness or model update.
- **Trajectory** — did the agent take a logical, efficient path? Did it avoid redundant loops, call tools in the right order, and ask for clarification at the right moments rather than guessing?
- **Unit-level** — does each component of the agent architecture work correctly in isolation? Examples: does the routing logic select the right tool? Does the RAG pipeline retrieve the right document?
- **Online (production)** — asynchronous scoring of live traffic to detect quality degradation, cost explosions, or latency spikes before end users notice.

These categories are complementary. A failure in a unit-level eval suggests a routing or retrieval problem. A failure in a trajectory eval points to broken long-horizon planning. A capability failure means the agent cannot do the task at all.

## How this changes eval design

Because the harness, tools, and environment are all part of what you're evaluating:

- Eval results are not portable across harnesses. A benchmark score on one scaffold tells you little about the same model on a different scaffold.
- Small harness changes (reworded system prompt, new tool description) can shift eval results significantly without any model update.
- The eval suite must cover each layer: result quality (does the output make sense?), trajectory quality (was the path efficient and safe?), and component quality (does each piece work?).
- Eval-driven development becomes a first-class practice: iterating on the harness using evals as the signal, separate from any model update. This is the premise of [[concepts/agent-improvement-loop]].

## Caveats

- The five-category taxonomy used here is a synthesis of common practice, not a single canonical standard. Different teams and frameworks use slightly different names.
- The harness-as-unit-under-test framing is widely shared (Anthropic, LangChain, and others), but the precise vocabulary varies.

## Related

- [[concepts/harness]] — the scaffolding that is the primary unit under test in agent evals
- [[concepts/agent-improvement-loop]] — the operational loop that uses evals to iteratively improve a harness
- [[workflows/agentic-orchestration-patterns]] — orchestration patterns that good evals help validate

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/sources/deep-research/2026-04-23-agents-evals.md (new)

````md
---
title: Comprehensive Operational Framework for Agentic AI Evaluation
type: source
source_type: deep-research
source_file: raw/deep-research/2026-04-23 Agents Evals.md
ingested: 2026-04-24
domains: [agents, coding]
---

# Comprehensive Operational Framework for Agentic AI Evaluation

A deep-research report synthesizing current operational practices for evaluating AI agents across two domains: software-development agents and general task/workflow agents. The report covers taxonomies, metrics, toolchains, benchmarks, simulation patterns, and autonomy governance.

**Treat as synthesis, not primary source.** Claims involving specific frameworks (CLEAR, Authority Graph), vendor practices, and precise thresholds should be verified against primary sources before being cited as canonical.

## Influenced pages

- [[concepts/agent-evals]] — eval taxonomy and trajectory framing
- [[training/evals-for-agentic-software-development]] — coding-agent eval patterns
- [[training/evals-for-agentic-work]] — workflow-agent eval patterns
- [[training/company-wide-ai-enablement]] — autonomy ladder section
- [[concepts/agent-improvement-loop]] — eval lifecycle and trace mining expansion
- [[benchmarks/swe-bench]] — SWE-bench Pro / data contamination note
- [[benchmarks/swe-polybench]] — methodology detail update
- [[benchmarks/osworld]] — new page
- [[benchmarks/webarena]] — new page
- [[benchmarks/tau-bench]] — new page
- [[benchmarks/gaia]] — new page
- [[benchmarks/toolbench]] — new page
- [[benchmarks/terminal-bench]] — new page
- [[tools/braintrust]] — new page
- [[tools/promptfoo]] — new page
- [[tools/langfuse]] — new page

## Key claims extracted

- Agent evaluation requires assessing the full system: `model + harness + tools + environment`
- Five eval categories: Capability, Regression, Trajectory, Unit-level, Online
- Coding-agent evals: deterministic gates (CI, linters, type-checkers) must pass before AI-specific evals run
- Minimum Viable Eval Suite for coding: deterministic tests + file system impact checks + cost/latency thresholds + LLM-as-judge
- Ramp's "Inspect" coding agent: >50% of merged PRs, shadow mode in isolated Modal VMs
- pass^k metric (from tau-bench): probability of success across all k consecutive trials — drops sharply vs. single-trial success
- Autonomy Ladder: five levels from read-only (L0) to full autonomy (L4/5); level transitions require eval evidence
- LLM-as-judge requires calibrated rubrics, golden reference answers, and periodic IRA audits (5–10% sampling)
- Public benchmarks prove capability but should not be treated as proof of production readiness
````

## Open questions

- Should the source summary live in `wiki/sources/deep-research/` (matching the raw folder structure) or in `wiki/sources/articles/` since there's no `deep-research` source subdirectory yet? Creating `wiki/sources/deep-research/` is proposed here.
	- Please create the deep research one
- The harness.md update is a tiny patch — approve if the link is useful; skip if it's premature before the concept page is applied.
	- approved
