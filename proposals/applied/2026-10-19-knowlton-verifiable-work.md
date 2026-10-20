---
type: proposal
source: raw/tweets/2026-10-19-leeknowlton-2111469315220443345.md
status: pending
created: 2026-10-19
---

# Proposal: Lee Knowlton — sort work by whether AI can verify it

## Summary

### In short
How much AI you can throw at a task depends on whether AI can check the result, so the first job is sorting work into verifiable and not, and the second is building judges that turn "maybe" into "yes". Lee Knowlton's 17 October post adds the middle step the wiki lacks: build an AI judge, test it with evals, and if it is good enough the work becomes delegable. The proposal updates **AI work delegation modes** and **Evals for workflow and task agents**. Hesitation: the delegation page already says delegation needs a verifiable success criterion, so part of this overlaps.

[[#Open questions|Open questions: none.]]

### The source
Lee Knowlton posted a short list of "notes on using AI productively" on X on 17 October 2026. His organizing idea is that most work falls into two buckets, AI-verifiable and not, where verifiable means the AI can independently tell whether the work it just did is good. If the work is verifiable, he says, design a verifier or a system of verifiers and "let 'er rip": the human is no longer the bottleneck, so scaling the number of tasks costs no extra attention.

The interesting part is the middle. When work might be verifiable, you can try building an AI judge, a model that grades the output, but you need evals, a set of test cases with known answers, to prove the judge is competent. If the judge passes, the work has moved into the verifiable bucket. Sometimes such a judge is easy to build and sometimes so hard it is not worth trying. Work no AI can verify leaves a human as the judge, and there he recommends working the old way with AI help: one or two tasks at a time, no context switching, protected focus. Finally, large unverifiable jobs often contain verifiable sub-tasks; automating those frees attention for the parts only the human can judge. He points to the X account @hammer_mt as his reference for building judges well.

### What changes
The delegation page already sorts work into autonomous delegation and human-steered collaboration, using "a clear, verifiable success criterion" as the dividing test, and the evals page already explains how to calibrate an LLM judge against human ratings.

- **AI work delegation modes** gains a pattern that treats verifiability as something you can build (verifier, then a judge proven with evals), a working rule for the unverifiable bucket (one or two tasks, protected focus), and a pointer that carving out verifiable sub-tasks is one answer to its own open question about tasks that shift between modes. It opens a Recent-changes section with one entry; page date moves to 17 October.
- **Evals for workflow and task agents** gains a short framing at the top of its LLM-as-judge section: the judge's measured competence is what decides whether a task can be handed off at all, and some judges cost more to build than they save. One Recent-changes entry; page date moves to 17 October.
- One new source page for the post.

### What to weigh
The post includes an attached image that was not read; only its text is in the fetched copy. Beyond that, the reviewer should decide whether the overlap with the delegation page's existing "verifiable success criterion" line is worth a second bullet; the draft keeps the existing line and adds only the build-a-judge path and the unverifiable-bucket rule.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-work-delegation-modes.md` — add one Proven-patterns bullet (sort by AI-verifiability; build verifiers or eval-tested judges); add a new `## Recent changes` section (none exists today) with one entry dated 2026-10-17, placed before `## Related`; appends one id to frontmatter `sources:` and one link to `## Sources`; `as_of` to 2026-10-17
- [ ] **Update** `wiki/training/evals-for-agentic-work.md` — add a framing paragraph at the top of `## LLM-as-judge for qualitative dimensions`; adds one Recent-changes entry dated 2026-10-17 (live list has 1, no spill); appends one id to frontmatter `sources:` and one link to `## Sources`; `as_of` to 2026-10-17
- [ ] **Create** `wiki/sources/tweets/leeknowlton-verifiable-work-2026-10-17.md` — source summary

## Page drafts

### wiki/training/ai-work-delegation-modes.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-17
sources: [ai-work-splitting-2026-05-10, task-routing-cost-discipline-2026-05-13, every-after-automation-2026-05, every-chatgpt-openclaw-guides-2026-08-27, leeknowlton-verifiable-work-2026-10-17]
```

New bullet, appended to `## Proven patterns`:

```
- **Sort by AI-verifiability, and treat verifiability as something you can build.** The deciding question is whether an AI can independently tell if the work it just completed is good. If yes, design a verifier (or a set of them) and scale up freely: the human is no longer the bottleneck, so more tasks cost no more attention. If maybe, build an AI judge and test it with evals before trusting it; a judge that passes moves the work into delegation mode, but some judges are too hard to be worth building. If no, a human stays the judge: work one or two tasks at a time, avoid context switching, protect focus. Inside large unverifiable jobs, carve out the verifiable sub-tasks and delegate those, which is one practical answer to tasks that move between modes. (Lee Knowlton, Oct 2026)
```

New section, inserted after `## Open questions` and before `## Related`:

```
## Recent changes

- [2026-10-17] Added the verifiability sort: verifier for verifiable work, eval-tested AI judge for maybe-verifiable work, focused one-or-two-task human work otherwise, and carving out verifiable sub-tasks (Lee Knowlton).
```

`## Sources` — appends one link:

```
- [Lee Knowlton — notes on using AI productively](../sources/tweets/leeknowlton-verifiable-work-2026-10-17.md)
```

### wiki/training/evals-for-agentic-work.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-17
sources: [agents-evals-deep-research, every-benchmarks-dont-know-your-job-2026-08-25, leeknowlton-verifiable-work-2026-10-17]
```

New paragraph, inserted directly under the `## LLM-as-judge for qualitative dimensions` heading, before the existing first paragraph:

```
A judge is also what decides whether a task can be delegated at all. Work an AI can verify can be scaled with little human attention; work that might be verifiable becomes delegable only once an AI judge has been shown, through its own evals, to grade it competently. Some judges are easy to build and some are hard enough not to be worth the effort, so estimate that cost before committing (Lee Knowlton, Oct 2026). See [AI work delegation modes](ai-work-delegation-modes.md).
```

`## Recent changes` — adds one entry at the top (live list has 1 entry; no spill):

```
- [2026-10-17] Framed LLM-as-judge as the gate on delegation: a judge proven with evals turns maybe-verifiable work into delegable work (Lee Knowlton).
```

`## Sources` — appends one link:

```
- [Lee Knowlton — notes on using AI productively](../sources/tweets/leeknowlton-verifiable-work-2026-10-17.md)
```

### wiki/sources/tweets/leeknowlton-verifiable-work-2026-10-17.md (new)

```
---
title: 'Lee Knowlton (@leeknowlton) — notes on using AI productively'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-19-leeknowlton-2111469315220443345.md
url: https://x.com/leeknowlton/status/2111469315220443345
published: 2026-10-17
ingested: 2026-10-19
domains: [agents, training]
---

# Lee Knowlton — notes on using AI productively

Short X post sorting work into AI-verifiable and not, and prescribing a different way of working for each: verifiers and unlimited AI for verifiable work, an eval-tested AI judge for work that might be verifiable, and focused one-or-two-task human work for the rest. The attached image was not read; the text is complete in the raw file.

## Influenced pages

- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — verifiability sort and the build-a-judge path
- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — judge competence as the gate on delegation

## Key claims extracted

- Most work splits into AI-verifiable and not; "verifiable" means AI can independently tell whether its completed work is good
- Verifiable work: design a verifier or system of verifiers and use as much AI as possible; the human stops being the bottleneck, so no marginal attention is needed as tasks scale
- Possibly verifiable work: build an AI judge, but use evals to test the judge's competence; a good-enough judge makes the work verifiable
- Some judges are easy to build; some are so hard they are not worth it
- Unverifiable work: a human is the judge; one or two tasks at a time, avoid context switching, protect focus
- Larger work often contains verifiable sub-tasks; automating them frees attention for the parts the human is uniquely suited for
- Cites @hammer_mt as the author's reference on building judges well
```

## Schema / vocabulary additions

None.

## Open questions

None.
