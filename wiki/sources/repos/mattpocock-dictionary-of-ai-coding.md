---
title: "mattpocock/dictionary-of-ai-coding"
type: source
source_type: repo
source_file: raw/repos/mattpocock-dictionary-of-ai-coding.md
url: https://github.com/mattpocock/dictionary-of-ai-coding
published: 2026-05-01
ingested: 2026-05-05
domains: [coding, agents]
---

# mattpocock/dictionary-of-ai-coding

Plain-English glossary of AI coding terms covering models, sessions, context windows, tools, environments, failure modes, handoffs, memory, steering, and patterns of work.

## Influenced pages

- [AI coding vocabulary](../../training/ai-coding-vocabulary.md) — new training page
- [Harness](../../concepts/harness.md) — reinforces model / harness / agent distinctions

## Key claims extracted

- Models are passthrough functions: they process input and return output, but retain no memory between calls and take no actions on their own. The harness wraps a model to give it memory, tools, a loop, and the ability to act.
- Context is finite, degrades, and differs from durable memory.
- Tools and environment define what an agent can actually act on.
- Shared vocabulary reduces confusion around cost, failure, handoff, and model selection.
