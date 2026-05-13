---
type: proposal
source: raw/repos/mattpocock-dictionary-of-ai-coding.md
sources:
  - raw/repos/mattpocock-dictionary-of-ai-coding.md
  - raw/articles/2026-05-01-githubcom-mattpocockdictionary-of-ai-cod.md
status: pending
created: 2026-05-05
---

# Proposal: AI coding dictionary for training vocabulary

## Summary

Matt Pocock's AI coding dictionary is not a product launch, but it is useful training material: it gives practitioners plain-English definitions for models, harnesses, sessions, context windows, tools, failure modes, handoffs, memory, steering, and work patterns. The wiki should ingest this as training support and lightly cross-link the existing harness concept rather than duplicate the entire glossary.

## Intended changes

- [x] **Create** `wiki/training/ai-coding-vocabulary.md` — concise training page for shared agentic-coding language.

- [x] **Update** `wiki/concepts/harness.md` — add source link and a short note that practitioner vocabulary increasingly distinguishes model, harness, agent, context, session, and environment.

- [x] **Update** `wiki/index.md` — add the new training page and bump training/page counts when applying.

- [x] **Create** `wiki/sources/repos/mattpocock-dictionary-of-ai-coding.md` — source summary.

## Page drafts

### wiki/training/ai-coding-vocabulary.md (new)

```markdown
---
title: AI coding vocabulary
type: training
domains: [coding, agents]
tags: [agentic]
as_of: 2026-05-01
sources: [mattpocock-dictionary-of-ai-coding]
---

# AI coding vocabulary

Teams using coding agents need shared language for the things that actually determine outcomes: the model, the harness, the session, the context window, the tools, the environment, and the handoff between runs.

## Current guidance

- Use **model** for the stateless parameters served by a provider, not for the whole product experience.
- Use **agent** for the harnessed system a person interacts with: model plus tools, system prompt, environment, permissions, and loop behavior.
- Use **context** for the information the agent has available right now; distinguish it from durable memory and from the finite context window sent to the model.
- Use **session** for the bounded run that accumulates tool results and conversation history until it is cleared, compacted, or handed off.
- Use **harness** for the scaffolding around the model: tools, prompts, orchestration, context management, permission layers, and environment access.

## Teaching pattern

Start with the operational distinction: if two products use the same model but behave differently, the harness and environment explain the difference. This prevents teams from over-attributing success or failure to model choice alone.

## Failure modes

- Calling every behavior "the model" and missing harness, tool, or context problems
- Treating a long session as memory instead of a context window slowly filling up
- Letting handoffs depend on chat history instead of durable artifacts

## Sources

- [Matt Pocock — Dictionary of AI Coding](../sources/repos/mattpocock-dictionary-of-ai-coding.md)
```

### wiki/sources/repos/mattpocock-dictionary-of-ai-coding.md (new)

```markdown
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

- Models are stateless and require a harness to become agents.
- Context is finite, degrades, and differs from durable memory.
- Tools and environment define what an agent can actually act on.
- Shared vocabulary reduces confusion around cost, failure, handoff, and model selection.
```

## Feedback:

- "stateless parameters" what do you mean with that?