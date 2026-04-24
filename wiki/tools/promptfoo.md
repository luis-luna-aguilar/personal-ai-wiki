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
- The focus on internal agent behavior (tool routing, tool call sequences) fills a gap that output-only evaluators miss
- Open-source and CLI-native; integrates with developer workflows directly

## Weaknesses / caveats

- Verify current feature set at promptfoo.dev — the specific features described are from a research synthesis report (April 2026)
- Qualitative scoring (tone, helpfulness) requires LLM-as-judge configuration; Promptfoo provides the framework, the rubric is user-defined

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
