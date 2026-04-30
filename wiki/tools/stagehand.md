---
title: Stagehand
type: tool
domains: [agents, computer-use, coding]
subcategory: agent-framework
tags: [open-source, agentic]
as_of: 2026-04-24
sources: [qa-tooling-for-software-agents-deep-research]
---

# Stagehand

Stagehand is an AI-era browser automation framework built by Browserbase. It sits between brittle selector-heavy browser tests and unconstrained browser agents, combining natural-language browser actions with explicit code and repeatable primitives.

## Current status (as of 2026-04-24)

- Official docs describe Stagehand as a browser automation framework using natural language and code
- Core primitives are `act`, `extract`, `observe`, and `agent`
- Docs explicitly position it as more reliable and repeatable than unconstrained browser agents
- Official integration docs show Stagehand working with Playwright directly
- Stagehand docs recommend Browserbase for cloud browser infrastructure, while also supporting local execution

## Strengths

- Useful for browser self-verification loops when coding agents need to prove a UI change actually works
- Sits in a practical middle ground between raw Playwright and fully autonomous computer-use agents
- The extract/observe primitives make it more suitable for proof-generation and verification than plain click-script automation alone

## Weaknesses / caveats

- AI-assisted browser actions are still slower and less deterministic than pure Playwright
- The wiki should treat Stagehand as a verification-enabling framework, not as proof that fully agentic browser testing is mature

## Sources

- [Practical tooling layer for evals in agentic software development](../sources/deep-research/2026-04-24-qa-tooling-for-software-agents.md)
