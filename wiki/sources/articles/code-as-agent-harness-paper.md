---
title: "Code as Agent Harness"
type: source
source_type: article
source_file: raw/articles/2026-08-25-arxivorg-abs-260518747.md
url: https://arxiv.org/abs/2605.18747
published: 2026-05-18
ingested: 2026-08-25
domains: [agents]
---

# Code as Agent Harness

An arXiv survey (submitted 2026-05-18, cs.CL/cs.AI) arguing that code is becoming the operational substrate for agent systems rather than only a final output. The paper organizes harness design around three layers: the harness interface (where code connects agents to reasoning, action, and environment modeling), harness mechanisms (planning, memory, tool use for long-horizon execution, plus feedback-driven control), and scaling the harness from single-agent to multi-agent settings, where shared code artifacts support coordination, review, and verification. It surveys applications across coding assistants, GUI/OS automation, embodied agents, scientific discovery, and enterprise workflows, and names open challenges including evaluation beyond final task success and regression-free harness improvement.

## Influenced pages
- [Harness (agent)](../../concepts/harness.md) — added as a research framing reinforcing code-centered harness design

## Key claims extracted
- Frames "code as agent harness": code as the operational substrate for reasoning, acting, environment modeling, and execution-based verification, not just a target output
- Three-layer structure: harness interface, harness mechanisms (planning/memory/tool use/feedback control), and multi-agent scaling
- Open challenges named: evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across agents, human oversight for safety-critical actions
- This is a synthesis/survey paper, not a benchmark result — its framing is a useful vocabulary, not an empirical claim about any specific system
