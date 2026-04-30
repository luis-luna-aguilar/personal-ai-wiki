---
title: tau-bench
type: benchmark
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# tau-bench

tau-bench evaluates agents on their ability to navigate multi-turn dialogues with simulated users while adhering to strict corporate policies, handling real-world tasks like airline refunds and retail returns. Its core contribution is the **pass^k metric**, which measures reliability across multiple consecutive trials rather than single-attempt success.

## What tau-bench tests

Agents are evaluated on tasks with simulated users who:
- Have specific goals but may withhold information until asked
- Interact in natural language across multiple turns
- Trigger policy edge cases such as unusual refund requests or out-of-scope asks

Agents must query databases, follow policy rules, and handle the ambiguity of real human communication, not a clean single-turn input.

## The pass^k metric

tau-bench introduced **pass^k**: the probability that an agent succeeds on all `k` consecutive independent trials.

This is distinct from **pass@k** (`did at least one of k attempts succeed?`), which is appropriate when you can retry. In live customer service, there is no retry: the agent gets one interaction per customer.

**The results expose a severe reliability problem:** an agent with 60% single-attempt success (`pass^1`) can drop below 25% reliability when measured across eight consecutive runs (`pass^8`). Eval suites that only test single-shot success will massively overestimate production readiness for customer-facing workflow agents.

## Why it matters

tau-bench is the benchmark to watch for:
- Customer service and support agents
- Workflow agents operating under policy constraints
- Systems where consistency across repeated use matters more than demo quality

It is also relevant for coding-agent evaluation when the question is reliability of longer-running autonomous processes, not just single-task capability.

## Caveats

- The benchmark is designed around specific policy domains (airline, retail); generalization to other policy types requires separate evaluation
- LLM-driven user simulators have their own failure modes and may not fully represent real human variance

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
