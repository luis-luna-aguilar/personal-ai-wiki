---
type: proposal
source: raw/deep-research/2026-04-23 Agents Evals.md
status: pending
created: 2026-04-24
---

# Proposal: Eval observability tool pages (Braintrust, Promptfoo, Langfuse)

## Summary

Three eval/observability tools appear prominently enough in the report — and are verifiable real products — to justify lightweight tool pages: Braintrust (trace ingestion + dataset management), Promptfoo (assertion-based eval framework), and Langfuse (open-source LLM observability). The remaining tools mentioned in the report (DeepEval, Galileo, Arize, Agentform) are either lightly sourced or not prominent enough to warrant standalone pages yet.

A new subcategory `agent-eval-tooling` is proposed for tools whose primary purpose is agent evaluation, tracing, and observability.

## Intended changes

- [x] **Schema** Add subcategory `agent-eval-tooling` to `wiki/_schema/subcategories.md`
    > See draft below

- [x] **Create** `wiki/tools/braintrust.md` — eval dataset management and trace-to-dataset platform
    > See draft below

- [x] **Create** `wiki/tools/promptfoo.md` — assertion-based agent eval framework
    > See draft below

- [x] **Create** `wiki/tools/langfuse.md` — open-source LLM observability and eval platform
    > See draft below

- [x] **Update** `wiki/index.md` — add three tool entries
    > **Add under Tools:**
    > ```
    > - [[tools/braintrust]] — eval dataset management and trace-to-dataset conversion for agent pipelines *(as_of: 2026-04-23)*
    > - [[tools/promptfoo]] — assertion-based CLI eval framework for LLM outputs and agent tool routing *(as_of: 2026-04-23)*
    > - [[tools/langfuse]] — open-source LLM observability and eval tracing platform *(as_of: 2026-04-23)*
    > ```

## Schema / vocabulary additions

- [x] Add new subcategory `agent-eval-tooling` to `wiki/_schema/subcategories.md`:
    ```
    ### agent-eval-tooling
    - **Parent domain(s):** agents
    - **Applies to types:** tool
    - **Definition:** Platforms and frameworks specialized for evaluating, tracing, and monitoring AI agent and LLM pipeline behavior — covering dataset management, assertion-based testing, LLM-as-judge scoring, and production observability.
    - **Examples:** [[tools/braintrust]], [[tools/promptfoo]], [[tools/langfuse]]
    ```

## Page drafts

### wiki/tools/braintrust.md (new)

````md
---
title: Braintrust
type: tool
domains: [agents]
subcategory: agent-eval-tooling
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Braintrust

Braintrust is an AI eval platform focused on dataset management, trace ingestion, and converting production agent traces into eval datasets. Its core pattern is "trace-to-dataset": capturing what an agent actually did in production and turning that record into a structured test case without manual reformatting.

## Current status (as of 2026-04-23)

- Supports trace ingestion and assertion-based scoring on those traces
- "One-click" trace-to-dataset conversion: an agent's full execution trace (input, tool calls, output) can be dropped directly into a dataset row for use in future evals
- Used alongside LLM-as-judge setups: the trace is ingested, a judge model is applied, and the scores are stored against the dataset
- Works with LangGraph, LangChain, and similar multi-agent orchestration frameworks

## Strengths

- The trace-to-dataset workflow closes the gap between production behavior and offline eval coverage
- Dataset versioning and logging allow teams to track how agent behavior changes over time across harness or model updates
- Integrates with the incident-to-regression pipeline: failures discovered in production can be immediately captured and converted into test cases

## Weaknesses / caveats

- Primary source here is a research synthesis report (April 2026); verify current feature scope at braintrust.dev
- As of training data, Braintrust is primarily a dataset management and logging platform — evaluation scoring is done by the user-defined judge, not by Braintrust itself

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/tools/promptfoo.md (new)

````md
---
title: Promptfoo
type: tool
domains: [agents]
subcategory: agent-eval-tooling
tags: [agentic, cli, open-source]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Promptfoo

Promptfoo is an open-source, CLI-based framework for evaluating LLM outputs and agent behavior through declarative assertions. It lets teams write specific, structured checks on what an agent said or did — for example, verifying that the agent called the correct tool rather than hallucinating a response.

## Current status (as of 2026-04-23)

- CLI-first, open-source eval framework
- Supports assertion-based testing: write structured predicates against agent outputs and tool calls
- `skill-used` assertion example: verify that an agent routed a query to the SQL execution tool rather than fabricating data from its weights — this grades internal routing behavior, not just final output quality
- Works with LangGraph multi-agent workflows and other orchestration frameworks
- Can be wired into CI/CD pipelines as an automated quality gate

## Strengths

- Declarative assertion syntax makes eval cases easy to write and review without custom test harness code
- The focus on *internal* agent behavior (tool routing, tool call sequences) fills a gap that output-only evaluators miss
- Open-source and CLI-native; integrates with developer workflows directly

## Weaknesses / caveats

- Verify current feature set at promptfoo.dev — the specific features described are from a research synthesis report (April 2026)
- Qualitative scoring (tone, helpfulness) requires LLM-as-judge configuration; Promptfoo provides the framework, the rubric is user-defined

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/tools/langfuse.md (new)

````md
---
title: Langfuse
type: tool
domains: [agents]
subcategory: agent-eval-tooling
tags: [agentic, open-source]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Langfuse

Langfuse is an open-source LLM observability and tracing platform. It captures the full execution trace of agent runs — model calls, tool invocations, intermediate outputs, latencies, and costs — and provides a UI and API for reviewing, scoring, and monitoring that trace data.

## Current status (as of 2026-04-23)

- Open-source; self-hostable or available as a managed cloud service
- Captures full LLM and agent execution traces including prompt, response, tool calls, and latency at each step
- Supports human review and LLM-as-judge scoring applied against stored traces
- Provides production monitoring with dataset management for building offline eval suites from production traces
- Positioned as the open-source alternative to proprietary observability platforms in the LLM eval toolchain

## Strengths

- Open-source and self-hostable — relevant for teams with data residency or privacy requirements
- Full trace capture (not just input/output) makes it possible to audit intermediate agent steps
- Works as both a development debugging tool and a production monitoring system

## Weaknesses / caveats

- As an observability platform, it captures and stores traces but the evaluation logic (rubrics, scoring) is user-defined or requires integration with an LLM-as-judge setup
- Verify current feature set and SDK compatibility at langfuse.com — the research report is from April 2026 and features may have changed

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

## Open questions

- Braintrust, Promptfoo, and Langfuse are all real products, but these pages are seeded primarily from the research report. They should be enriched from official docs when those sources are fetched.
	- Lets keep it as is
- DeepEval is also a real product worth considering for a future page; skipping for now because it's more lightly sourced in the report.
	- Lets keep it as is
