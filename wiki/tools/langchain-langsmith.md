---
title: LangChain / LangSmith
type: tool
domains: [agents]
subcategory: agent-framework
tags: [open-source, agentic]
as_of: 2026-05-15
sources: [langchain-interrupt-may-2026]
---

# LangChain / LangSmith

LangChain is the leading open-source agent framework for building custom agents with tool use, multi-agent patterns, and runtime scaffolding. LangSmith is its observability and evaluation companion. Together they form the most widely used open-source stack for agent development and tracing.

## Current status (as of 2026-05-15)

- **LangSmith Engine** (May 2026): automatically consumes traces, clusters failures, identifies likely code issues, and proposes fixes and evals — converting passive observability into an active improvement loop; the system surfaces hypotheses for human confirmation rather than requiring manual trace review
- **SmithDB** (May 2026): purpose-built database for nested, long-running agent traces with large payloads; built on Apache DataFusion and Vortex; claims 12–15× faster access on key agent-trace workloads vs. general-purpose databases; architectural bet: agent traces are a different workload shape from standard application logs
- **LangChain Labs**: applied research arm focused on continual learning — production traces become training signal for targeted capability improvements; Prime Intellect partnership
- LangChain OSS also shipped: Managed Deep Agents, LLM Gateway, Context Hub, Deep Agents 0.6, streaming typed projections, checkpoint storage, and code interpreter at the same Interrupt conference release cluster

## Strengths

- The observability→improvement loop closes automatically (Engine clusters failures and proposes targeted changes)
- SmithDB is architecturally purpose-fit for agent traces rather than adapted from log-management databases
- Continual learning approach (Labs) targets the gap between offline eval improvement and production adaptation

## Weaknesses / caveats

- Engine efficiency claims are vendor-reported from the Interrupt conference; independent benchmarks pending
- LangChain Labs is early-stage applied research, not a shipped product

## Recent changes

- [2026-05-15] Interrupt conference: LangSmith Engine, SmithDB, LangChain Labs launched simultaneously — largest single LangChain infrastructure release cluster

## Sources

- [LangChain Interrupt conference — May 2026](../sources/newsletters/langchain-interrupt-may-2026.md)
