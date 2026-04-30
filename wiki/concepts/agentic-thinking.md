---
title: Agentic thinking
type: concept
domains: [agents, models]
tags: [agentic]
as_of: 2026-04-10
sources: [agentic-thinking-lin]
---

# Agentic thinking

A proposed successor to "reasoning thinking" (the o1/R1 wave). Where reasoning models optimize for longer internal deliberation before answering, agentic thinking optimizes for sustained effective action within an environment — thinking in order to act, with continuous feedback from the world.

## Current status (as of 2026-04-10)

- Framed by Junyang Lin (ex-Qwen tech lead) in a post-departure essay as the next phase after the reasoning wave
- The central question shifts from "can the model think long enough?" to "can it execute effectively over multiple turns?"
- Environments (browsers, terminals, APIs, sandboxes) become first-class training artifacts — environment-building is becoming its own startup category
- Harness engineering and train-serve integration replace RL algorithms as the primary competitive edge

## Reasoning thinking vs agentic thinking

| | Reasoning thinking | Agentic thinking |
|---|---|---|
| **Optimizes for** | Quality of internal deliberation | Sustained effective action |
| **Judged by** | Final answer correctness | Progress over multi-turn interaction |
| **Environment** | Static verifier | Live tools, browsers, terminals, APIs |
| **RL challenge** | Scaling rollouts | Environment quality, reward hacking with tool access |
| **Competitive edge** | Better RL algorithms, stronger feedback signals | Better environments, harness engineering, closed-loop integration |

## Why it matters

- More thinking doesn't mean more intelligence — excess visible reasoning can signal weak allocation
- Agentic RL infrastructure is harder: the policy is embedded in a harness with tool servers, sandboxes, and API layers, not a static verifier
- Reward hacking becomes more dangerous with tool access (models can search for answers, exploit logs, discover shortcuts)
- The competitive moat shifts from model training to environment design and harness engineering

## Sources

- [From 'Reasoning' Thinking to 'Agentic' Thinking by Junyang Lin](../sources/articles/agentic-thinking-lin.md)
