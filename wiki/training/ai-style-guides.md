---
title: AI style guides
type: training
as_of: 2026-11-16
sources: [how-to-build-an-ai-style-guide, every-instruction-bloat-parrott-2026-10-05, every-write-like-me-optimized-skill-2026-11-16, every-writing-arena-2026-11-13]
---

# AI style guides

An AI style guide is a practical document that teaches a writing system how your organization actually sounds. The point is not only grammar consistency. It is to make tacit editorial judgment explicit enough that the model can reproduce it instead of defaulting to generic polished prose.

## Current guidance

- Treat the guide as an operating artifact, not a brand appendix
- Encode voice, argument shape, preferred structure, and anti-patterns, not just punctuation rules
- Build from real examples of your writing rather than inventing rules in the abstract, and test the result blind against held-out examples; a guide that only describes your style can make drafts worse
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

## Test the skill, don't just describe it

Every's head of evals Mike Taylor (November 2026) compared a Claude-written "write like me" guide with three optimizers on 185 of his posts, 54 held out. The written guide lost to all three on 80–95% of held-out posts: it read like a list of his "greatest hits" (one-line paragraphs, signature phrases) and produced a caricature. For Opus 5.5, no skill beat the written skill 61% of the time. His method:

1. **Gather one format.** 12–25 published pieces from one publication; his 30 most recent posts beat the full archive because his style had changed. Meeting transcripts work if you have no samples; tweets and emails do not.
2. **Turn each piece into a brief.** Thesis, outline, facts, sources and quotes, with no phrasing or jokes, so a draft that sounds like you can be credited to the skill.
3. **Build a judge you can trust.** The judge sees the real piece and two drafts from the same brief and picks the closer one, run twice with the order swapped to cancel position bias, and notes how each draft differs. Consistency on swapped order: Opus 5.5 86%, Sonnet 5.5 70%, Jev 50%.
4. **Optimize instead of writing.** An optimizer (DSPy's GEPA won, ahead of Karpathy's autoresearch and Every's ce-optimize) keeps a skill change only if it scores better; the surviving rules are corrections drawn from the judge's notes, not preferences. Cost: $27–53 per skill against $5 for a one-shot guide; most gains come in three rounds.
5. **Optimize for the model you draft with.** Opus 5.5 rose from 16% with no skill to 93% with its optimized skill; Sonnet 5.5 with an optimized skill beat Opus 5.5 with the written guide on 46 of 60 judgments. Re-optimize when you switch models.
6. **Draft from a full brief and feed edits back.** A one-line prompt makes the skill invent plausible content in your voice; your edits on each draft are the next round's data.

His "Writing Arena" benchmark found the same across five Every writers: a one-pass skill lost to just handing the model a folder of the writer's posts for all five, and only after 10+ optimization rounds did the skill win for four. Limit: the judge rewards resemblance to past work, so the skill sounds like the writer you were; hold out your newest pieces. Taylor's skill is on GitHub (everyinc/compound-writing).

## Failure modes

- Treating a style guide as only a punctuation sheet
- Asking the model to "sound like us" without showing it what "us" means
- Leaving anti-patterns implicit, which lets generic AI prose sneak back in
- Confusing one good prompt with a reusable writing system
- Codifying every correction into the guide until checkable rules crowd out judgment, so drafts get worse with each round of feedback
- Trusting a style description no one has tested: a guide of signature habits applied every time yields a caricature, and may score below no guide at all

## Why it matters

As more writing gets produced through AI, the real risk is not only factual error. It is homogenization. Teams that externalize their voice and standards into a maintainable guide get more leverage from AI without sounding like everyone else using the same models.

## Related

- [Managing chat context](chat-context-management.md) — the same over-context problem in everyday chat threads, with signs to watch for and fixes

## Recent changes

- [2026-11-16] Added "Test the skill, don't just describe it": Mike Taylor's brief + pairwise-judge + optimizer method (written guide lost on 80–95% of held-out posts; GEPA best; skills are model-specific) and the Writing Arena result.
- [2026-10-05] Added "Instruction bloat": Katie Parrott's 759 → 3,855-word style guide, why checkable rules crowd out judgment, and her three rebuild principles (guides cut from 6,109 to 513 words).

## Sources

- [How to build an AI style guide](../sources/newsletters/how-to-build-an-ai-style-guide.md)
- [Every — When Trying to Make AI Better Makes It Worse](../sources/newsletters/every-instruction-bloat-parrott-2026-10-05.md)
- [Every — How I Finally Got AI to Write Like Me](../sources/newsletters/every-write-like-me-optimized-skill-2026-11-16.md)
- [Every — Writing Arena (Your Attention Is AI's New Bottleneck)](../sources/newsletters/every-writing-arena-2026-11-13.md)
