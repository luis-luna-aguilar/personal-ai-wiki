---
title: Composer 2
type: model
domains: [coding, models]
subcategory: coding-model
tags: [closed-source]
as_of: 2026-03-23
sources: [cursor-3-launch, late-march-small-coding-models]
---

# Composer 2

Composer 2 is Cursor's in-house coding model for complex long-horizon engineering work. It is no longer just a stub-level mention from the Cursor 3 launch: late-March sources add benchmark claims, pricing claims, and the now-disclosed fact that Cursor started from Moonshot's Kimi-k2.5 before doing continued pretraining and reinforcement learning.

## Current status (as of 2026-03-23)

- Cursor positions Composer 2 as its own model for complex, long-term coding tasks
- Reported benchmark claims: 61.7 on TerminalBench 2.0 and 73.7 on SWE-bench Multilingual
- Source coverage says it trails GPT-5.4 slightly, but beats Anthropic's Opus 4.6 on those cited coding benchmarks
- Launch pricing claim in the source set: about `$0.50` per million input tokens, roughly one-tenth of some frontier competitors
- Later source coverage says Cursor did not train it from scratch: the model reportedly starts from Moonshot's open Kimi-k2.5, then adds continued pretraining plus Cursor-specific finetuning / RL
- Available only inside Cursor products; no standalone API

## Strengths

- Clearer benchmark story than the original stub implied
- Integrated tightly into Cursor's agent workspace, so the model and product can co-evolve
- Low-cost positioning matters if the benchmark claims hold up in real usage

## Weaknesses / caveats

- Benchmarks and pricing come through secondary reporting in the captured source set
- The Kimi-k2.5 disclosure created credibility friction around the launch story
- Closed distribution makes independent evaluation harder than for open-weight peers

## Recent changes

- [2026-04-21] Late-March model coverage turned Composer 2 from a stub into a real current-state page with benchmark, pricing, and lineage claims
- [2026-04-02] Page created (stub) from a passing mention in the Cursor 3 launch post

## Sources

- [Meet the new Cursor (Cursor 3 launch)](../sources/articles/cursor-3-launch.md)
- [Late-March small coding models](../sources/newsletters/late-march-small-coding-models.md)
