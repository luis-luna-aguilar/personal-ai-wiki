---
type: proposal
source: raw/articles/2026-04-10-justinlin610githubio-blog-from-reasoning-to-agentic-thinking.md
status: pending
created: 2026-04-10
---

# Proposal: Agentic thinking (Junyang Lin essay)

## Summary

Junyang Lin, former tech lead of Alibaba's Qwen models, argues that the reasoning-model wave (o1, R1) is winding down and being replaced by "agentic thinking" — models that reason in order to act within environments, not just produce longer internal monologues. The competitive edge shifts from RL algorithms to environment design and harness engineering.

## Intended changes

- [x] **Create** `wiki/concepts/agentic-thinking.md` — new concept page
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add recent change noting the concept
    > **Add to Recent changes:**
    > `- [2026-04-10] Added [[concepts/agentic-thinking]] — Junyang Lin's essay on the shift from reasoning to agentic thinking`

- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add cross-reference if relevant (light touch)
    > Only if the page mentions reasoning vs agentic framing. Otherwise skip.

- [x] **Create** `wiki/sources/articles/agentic-thinking-lin.md` — source summary

## Page drafts

### wiki/concepts/agentic-thinking.md (new)

```
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

- [[sources/articles/agentic-thinking-lin]]
```

### wiki/sources/articles/agentic-thinking-lin.md (new)

```
---
title: "From 'Reasoning' Thinking to 'Agentic' Thinking" — Junyang Lin
type: source
source_type: article
source_file: raw/articles/2026-04-10-justinlin610githubio-blog-from-reasoning-to-agentic-thinking.md
url: https://justinlin610.github.io/blog/from-reasoning-to-agentic-thinking/
published: 2026-04-10
ingested: 2026-04-10
domains: [agents, models]
---

# From 'Reasoning' Thinking to 'Agentic' Thinking — Junyang Lin

Junyang Lin (former Qwen tech lead, departed Alibaba March 2026) argues the reasoning wave sparked by o1 and R1 is giving way to agentic thinking: models that reason in order to act within environments. The essay covers the Qwen3 hybrid-thinking merge challenges, why Anthropic's integrated approach was a useful corrective, what agentic thinking actually means, and why environment/harness engineering is the new competitive frontier.

## Influenced pages

- [[concepts/agentic-thinking]] — new page created
- [[state-of/agents]] — recent change entry

## Key claims extracted

- The reasoning wave (o1, R1) is winding down; agentic thinking is replacing it
- Merging thinking and instruct modes is harder than described — Qwen3's hybrid approach had significant data-distribution tensions
- Agentic RL infrastructure is qualitatively harder: policy embedded in tool servers, browsers, terminals, sandboxes
- Environment-building is becoming a real startup category
- Reward hacking is much more dangerous when models have tool access
- Competitive edge shifts from RL algorithms to environment design and harness engineering
- "We are transitioning from an era focused on training models to one centered on training agents"
```
