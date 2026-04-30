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

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
