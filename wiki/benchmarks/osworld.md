---
title: OSWorld
type: benchmark
domains: [agents, computer-use]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# OSWorld

OSWorld is a benchmark for evaluating multimodal agents capable of raw computer use, interacting with real operating system environments using mouse and keyboard actions. It tests agents across Ubuntu, Windows, and macOS in execution-based environments, where the agent must complete real GUI tasks rather than describe how it would.

## Current status (as of 2026-04-23)

- Human baseline task success: ~72.36%
- Top multimodal models: ~12% task success (as reported; verify against current leaderboard)
- The roughly 60-point gap reveals how far current frontier models still are from robust GUI grounding and layout navigation
- Evaluates agents as they actually interact with software: clicking buttons, navigating menus, and handling dynamic content

## Why it matters

OSWorld is the most important benchmark for teams evaluating autonomous desktop agents, RPA systems, and computer-use agents. The large human/model gap makes it a useful discriminator: high OSWorld scores indicate genuine GUI navigation ability rather than pattern matching against API-structured interfaces.

A model or system that performs well on text-based benchmarks but poorly on OSWorld is likely relying on text structure rather than genuine interface understanding.

## Caveats

- Specific scores are from a research synthesis report (April 2026); verify against the OSWorld leaderboard before citing numbers
- Task distribution may favor certain OS environments; verify per-platform breakdown for specific use cases
- GUI environments are updated over time; OSWorld scores may shift as apps change their interfaces

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
