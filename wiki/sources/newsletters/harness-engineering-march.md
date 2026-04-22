---
title: Harness engineering in mid-March
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-10-ainews-autoresearch-sparks-of-recursive-self-im.md
published: 2026-03-10
ingested: 2026-04-22
domains: [coding, agents]
---

# Harness engineering in mid-March

This source summary groups a mid-March cluster on harness engineering before the idea became more mainstream in April. The shared takeaway is that reliable agents depend on systems design around the model: loop controls, eval craft, context structure, and safe separation between shared context and isolated execution.

## Influenced pages

- [[concepts/harness]] — adds concrete operational lessons on loop primitives and storage/compute separation
- [[workflows/agentic-orchestration-patterns]] — adds reusable patterns for isolated execution and long-running loop control

## Key claims extracted

- Long-running agent performance depends heavily on harness affordances such as looping, interruption, rewind, and transparent sessions
- Practical teams increasingly separate durable shared context from execution sandboxes so multiple agents can collaborate through repos or filesystems
- Eval design and harness iteration were already being framed as more important than raw model quality for reliable autonomous work
- OpenAI's first-party harness-engineering post reinforced that software leverage was moving into scaffolding, feedback loops, and control systems
