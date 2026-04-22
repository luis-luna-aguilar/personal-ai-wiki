---
type: proposal
source: raw/newsletters/2026-03-19-how-to-build-an-ai-style-guide.md
status: pending
created: 2026-04-21
---

# Proposal: AI style guides

## Summary

This source is a good fit for `training/` because it turns "write in our voice" from a vague prompting desire into an operational artifact. The durable lesson is that an AI style guide is not only a copy-editing nicety; it is a way to externalize tacit judgment so writing systems stop regressing toward generic polished prose.

## Intended changes

- [x] **Create** `wiki/training/ai-style-guides.md` — new training page
  > See full draft below.

- [x] **Create** `wiki/sources/newsletters/how-to-build-an-ai-style-guide.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/training/ai-style-guides.md (new)

```markdown
---
title: AI style guides
type: training
as_of: 2026-03-19
sources: [how-to-build-an-ai-style-guide]
---

# AI style guides

An AI style guide is a practical document that teaches a writing system how your organization actually sounds. The point is not only grammar consistency. It is to make tacit editorial judgment explicit enough that the model can reproduce it instead of defaulting to generic polished prose.

## Current guidance

- Treat the guide as an operating artifact, not a brand appendix
- Encode voice, argument shape, preferred structure, and anti-patterns, not just punctuation rules
- Build from real examples of your writing rather than inventing rules in the abstract
- Revise the guide by observing where outputs drift generic or miss your taste

## Proven patterns

- **Use real samples first.** Start from writing you already consider good
- **Capture rhythm, not only mechanics.** Note sentence length, pacing, preferred transitions, and what the prose avoids
- **List anti-patterns explicitly.** The model needs to know what "sounds wrong" as much as what sounds right
- **Turn taste into instructions.** If an editor can explain the difference, it can usually be codified
- **Iterate from failures.** Weak outputs reveal missing rules faster than brainstorming does

## Failure modes

- Treating a style guide as only a punctuation sheet
- Asking the model to "sound like us" without showing it what "us" means
- Leaving anti-patterns implicit, which lets generic AI prose sneak back in
- Confusing one good prompt with a reusable writing system

## Why it matters

As more writing gets produced through AI, the real risk is not only factual error. It is homogenization. Teams that externalize their voice and standards into a maintainable guide get more leverage from AI without sounding like everyone else using the same models.

## Sources

- [[sources/newsletters/how-to-build-an-ai-style-guide]]
```

### wiki/sources/newsletters/how-to-build-an-ai-style-guide.md (new)

```markdown
---
title: How to build an AI style guide
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-19-how-to-build-an-ai-style-guide.md
ingested: 2026-04-21
domains: [training]
---

# How to build an AI style guide

This source reframes style guides as machine-facing operating instructions rather than only editorial bureaucracy. The practical takeaway is that good AI writing depends on making your organization's taste and anti-patterns explicit enough for a model to follow.

## Influenced pages

- [[training/ai-style-guides]] — opens a dedicated practical page for writing-system guidance

## Key claims extracted

- Style guides historically solved a machine-consistency problem, not just a copy-editing problem
- The same logic now applies to language models: explicit rules help preserve consistent output across many generated drafts
- A useful AI style guide should encode voice, rhythm, structure, and anti-patterns, not only mechanical style rules
- The practical workflow is to derive rules from past writing, test outputs, and refine the guide where the model drifts generic
```
