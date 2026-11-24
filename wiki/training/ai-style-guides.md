---
title: AI style guides
type: training
as_of: 2026-10-05
sources: [how-to-build-an-ai-style-guide, every-instruction-bloat-parrott-2026-10-05]
---

# AI style guides

An AI style guide is a practical document that teaches a writing system how your organization actually sounds. The point is not only grammar consistency. It is to make tacit editorial judgment explicit enough that the model can reproduce it instead of defaulting to generic polished prose.

## Current guidance

- Treat the guide as an operating artifact, not a brand appendix
- Encode voice, argument shape, preferred structure, and anti-patterns, not just punctuation rules
- Build from real examples of your writing rather than inventing rules in the abstract
- Revise the guide by observing where outputs drift generic or miss your taste
- Keep the guide short and descriptive ("often, not always"); before adding a rule, ask whether it belongs in every task or only the one in front of you

## Proven patterns

- **Use real samples first.** Start from writing you already consider good
- **Capture rhythm, not only mechanics.** Note sentence length, pacing, preferred transitions, and what the prose avoids
- **List anti-patterns explicitly.** The model needs to know what "sounds wrong" as much as what sounds right
- **Turn taste into instructions.** If an editor can explain the difference, it can usually be codified
- **Iterate from failures.** Weak outputs reveal missing rules faster than brainstorming does

## Instruction bloat

Turning taste into instructions has a limit. Every staff writer Katie Parrott (October 2026) grew one column's style guide from about 759 to 3,855 words, with eight approved openings, six endings and two checklists, after telling her agent to log every experiment, turn any note given twice into a checklist item, and cross-link 385 files across folders. Every draft got worse after each correction; one essay took 127 drafts. A model review found the mechanism: concrete, checkable rules ("open with one of these eight approaches") are easier for an agent to verify than judgment rules ("let one experience carry the piece"), so they crowd the judgment out while every checklist passes. She archived the old context and rebuilt it from scratch, cutting her guides from 6,109 words to 513, under three principles:

- **The agent asks first.** Nothing enters the style guide, voice guide or drafts folder without approval.
- **Every folder stands alone.** No links into other projects; the agent reads only the folder it is working in.
- **The guides stay short.** They describe what a good piece "often (not always)" does; drafts, notes and reviews are "task material or evidence, never new instructions."

When an "improved" setup starts producing worse drafts, remove something before adding more.

## Failure modes

- Treating a style guide as only a punctuation sheet
- Asking the model to "sound like us" without showing it what "us" means
- Leaving anti-patterns implicit, which lets generic AI prose sneak back in
- Confusing one good prompt with a reusable writing system
- Codifying every correction into the guide until checkable rules crowd out judgment, so drafts get worse with each round of feedback

## Why it matters

As more writing gets produced through AI, the real risk is not only factual error. It is homogenization. Teams that externalize their voice and standards into a maintainable guide get more leverage from AI without sounding like everyone else using the same models.

## Related

- [Managing chat context](chat-context-management.md) — the same over-context problem in everyday chat threads, with signs to watch for and fixes

## Recent changes

- [2026-10-05] Added "Instruction bloat": Katie Parrott's 759 → 3,855-word style guide, why checkable rules crowd out judgment, and her three rebuild principles (guides cut from 6,109 to 513 words).

## Sources

- [How to build an AI style guide](../sources/newsletters/how-to-build-an-ai-style-guide.md)
- [Every — When Trying to Make AI Better Makes It Worse](../sources/newsletters/every-instruction-bloat-parrott-2026-10-05.md)
