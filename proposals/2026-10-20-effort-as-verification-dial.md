---
type: proposal
source: raw/articles/2026-10-20-claudedev-blog-spending-your-effort.md
sources:
  - raw/articles/2026-10-20-claudedev-blog-spending-your-effort.md
  - raw/tweets/2026-09-25-trq212-2103576349499855160.md
  - raw/newsletters/2026-09-29-claude-codes-next-era-thariq-shihipar-anthropi.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Effort is a verification dial (Anthropic's guide to choosing effort levels)

## Summary

### In short
Effort is a verification dial, not an intelligence dial: raising it makes Claude test more and make more choices on your behalf, but it rarely rescues a wrong approach. On Terminal-Bench 3.0, Fable 5.1 went from 140 to 214 passes out of 370 attempts between low and max effort, with the largest gains in security and hardware. The proposal adds an evidence bullet and a rule of thumb to Cost-aware AI task routing, a spec-implement-verify loop to the software-development enablement page, and two source pages. One reason to hesitate: the routing page ends just over its 110% length warning.

[[#Open questions|Open questions: 1 to answer.]]

### The source
On 25 September 2026 Thariq Shihipar, who works on Claude Code at Anthropic, published "Spending your effort" on claude.dev (an X Article carried the same text). Effort is the setting that tells the model roughly how much compute to spend. His answer to "which level when" comes from two kinds of evidence: his own runs of the same tasks at several levels, and a pass through every Terminal-Bench 3.0 result, a community benchmark of about 70 hard terminal tasks.

On toy builds, effort mostly changed how much Claude decided for him. A vague "fitness tracker app" request produced a log and a graph at low effort in 1.5 minutes and a far richer app at max in 67 minutes. Given a detailed spec, the levels converged. On the benchmark, higher effort mostly bought testing. An HTML sanitizer task went from 1 of 5 at low to 5 of 5 at xhigh, where the run reviewed its own draft adversarially, read the parser's source and wrote a fuzzer. A storage-engine bug fix went from 0 of 5 to 4 of 5 because the high run reproduced the crash first. Failures from missed edge cases fell sharply between low and max, while "made the wrong call" failures barely moved. Gains by area ran from security (64% to 87%) to operations (12% to 22%). The numbers come from Anthropic's internal runs, five attempts per task, with safety interventions off.

In a Latent Space interview four days later he added a tip: ask for implementation notes, because most high-effort failures he read were cases where the model considered the right fix and rejected it.

### What changes
The wiki has one generic FinOps line telling teams to default effort to a middle tier, and one mention of comparing effort levels in a maintenance recipe. Nothing says when to raise it.

- **Cost-aware AI task routing** extends the middle-tier FinOps line with Anthropic's per-task rule of thumb and gains one evidence bullet with the Terminal-Bench numbers. One Recent-changes entry dated 25 September (6 entries, no spill). Page date stays at 19 October.
- **AI enablement — software development** gains an Engineering-discipline bullet: spec and interview, implement at low or medium, verify at high, and ask for implementation notes. One Recent-changes entry dated 25 September; the list is at its cap, so the 1 July entry spills to history. Page date stays at 19 October.
- Two new source pages: the claude.dev post, and a story-specific page for the effort part of the Latent Space interview.

### What to weigh
The routing page sits at 104% of its training-page ceiling; with these additions it reaches about 111%, just past the warning band. The proposal adds the content instead of compressing it and offers a split as an open question. The X Article version gets no source page of its own because the claude.dev post is the fuller copy of the same text; the tweet file is listed only in this proposal's frontmatter.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — extend the middle-tier effort FinOps bullet; add one evidence bullet under "Model and harness selection wins"; add one Recent-changes entry dated 2026-09-25 (list goes 5 → 6, no spill); append source id and link
    > **Before:** `- Default reasoning effort to a middle tier (e.g. Medium) rather than maximum, since reasoning/output tokens bill at a multiple of input-token rates and a large share of tasks don't need top-tier reasoning to hit a good cost/quality balance.`
    > **After:** see draft below

- [ ] **Update** `wiki/training/ai-enablement-software-development.md` — new Engineering-discipline bullet; add one Recent-changes entry dated 2026-09-25; append two source ids and links

- [ ] **Spill** `wiki/training/ai-enablement-software-development.md` → `wiki/history/training/ai-enablement-software-development.md` — the list is at its cap of 10, so the oldest entry (2026-07-01, software-factory/FDE rollout pattern) moves to history

- [ ] **Create** `wiki/sources/articles/claudedev-spending-your-effort-2026-09-25.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/latent-space-thariq-effort-implementation-notes-2026-09-29.md` — story-specific source summary (effort and implementation notes only)

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter: append `claudedev-spending-your-effort-2026-09-25` to `sources:`. `as_of` stays 2026-10-19.

New bullet, placed at the end of `### Model and harness selection wins` (after the Haiku 5.5 bullet):

```
- **Anthropic: effort buys verification, not a better approach.** Thariq Shihipar's pass through every Terminal-Bench 3.0 result found that higher effort mostly adds testing and edge-case checking. Moving Fable 5.1 from low to max raised passes from 140 to 214 of 370 attempts, at a median of 222k tokens per attempt against 73k, and cut "missed a case" failures from 59 to 24, while "made the wrong call" failures only fell from 133 to 107. Gains were largest in security (64% to 87%) and hardware (34% to 75%) and smallest in operations (12% to 22%). With a detailed spec the levels converge, so pay for effort where checking is the work. The working loop is on [AI enablement — software development](ai-enablement-software-development.md).
```

Replaced bullet in `## AI FinOps controls`:

```
- Default reasoning effort to a middle tier (e.g. Medium) rather than maximum, since reasoning/output tokens bill at a multiple of input-token rates and a large share of tasks don't need top-tier reasoning to hit a good cost/quality balance. Raise it by how much checking the task needs, not by how hard it sounds. Anthropic's rule of thumb for Claude Code: low for in-the-loop sketching, medium for most feature work, high for verification-heavy work such as bugs in existing code, and max only for fully autonomous hard problems such as security audits.
```

`## Recent changes` — adds one entry dated 2026-09-25, inserted in date order below the 2026-10-19 entries (list goes from 5 to 6, no spill):

```
- [2026-09-25] Added Anthropic's effort analysis (Terminal-Bench 3.0: effort buys edge-case verification, not a better approach) and its per-task effort rule of thumb to the middle-tier FinOps control.
```

`## Sources` — append:

```
- [Anthropic — Using Claude Code: Spending your effort](../sources/articles/claudedev-spending-your-effort-2026-09-25.md)
```

### wiki/training/ai-enablement-software-development.md (updated)

Frontmatter: append `claudedev-spending-your-effort-2026-09-25` and `latent-space-thariq-effort-implementation-notes-2026-09-29` to `sources:`. `as_of` stays 2026-10-19.

New bullet at the end of `### Engineering discipline` (after "Agent-driven maintenance"):

```
- **Spend effort on verification, and ask for implementation notes.** In Claude Code, the effort setting mostly changes how much the agent tests and how many choices it makes for you, not whether it finds the right approach. Thariq Shihipar's feature loop: give Claude a spec and have it interview you about missing details, implement at low or medium effort, review that it got the gist, then verify and test at high effort. On an underspecified build, higher effort means more assumptions made on your behalf; with a detailed spec the levels converge. Ask for implementation or decision notes as well: in his reading of eval transcripts, most high-effort failures were cases where the model considered the right fix and rejected it, and notes let a reviewer catch that. Benchmark numbers are on [Cost-aware AI task routing](cost-aware-ai-task-routing.md).
```

`## Recent changes` — adds one entry dated 2026-09-25, inserted between the 2026-10-12 and 2026-09-14 entries; then spills the oldest entry (2026-07-01) to history so the list stays at 10:

```
- [2026-10-19] Split "Evidence from practice" out to [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md) and grouped Proven patterns under `###` subheads.
- [2026-10-19] Split "Hiring AI-native engineers" and "The junior talent problem" out to [AI-native hiring and the junior talent pipeline](ai-native-hiring-and-junior-talent.md), a separate audience (hiring managers and talent leads).
- [2026-10-19] Added the agent-driven maintenance pattern (start small, compare model/effort, feed review back into the prompt, then widen) from OpenAI Core Experimentation's GPT-6 cleanup work.
- [2026-10-15] Added "Expect human-scale developer infrastructure, not code, to be the next bottleneck" (Anthropic's Scion source-control rebuild) and a caveat on Adversarial review: it can be myopic and push over-engineering, so engineers say "no" and review intent rather than every line.
- [2026-10-12] Added "Enforce conventions with lint rules, not skills" (Composio: 38 custom lint rules across a ~50-contributor repo; fast CI for preview-only contributors).
- [2026-09-25] Added "Spend effort on verification, and ask for implementation notes" (Anthropic's spec → low/medium implement → high verify loop).
- [2026-09-14] Added Anthropic's test-impact-analysis CI-scaling case study: 25x CI job growth over six months, three successive patches (70/29/<1 days), a three-week stateless redesign (rebuilding now often cheaper than patching), and a dedicated Claude Tag monitoring session; new Proven-patterns bullet on planning CI/test infrastructure for exponential rather than linear growth.
- [2026-08-28] Added Uber's Software Factory adoption numbers (70%+ PRs agent-attributed, 3,600+ agent skills, 30K executions/day, 7x WAU growth) and its core strategic argument: eliminating wasted token consumption, not just cheaper unit prices, is what let usage scale 7x while unit costs fell.
- [2026-07-16] Corrected the Bun Zig→Rust rewrite figures in the Stack-fungibility bullet (535,496 lines, 11 days, ~$165K in tokens) and added a full case study of its one-implementer/two-adversarial-reviewer methodology, plus a new "Adversarial review" pattern generalizing the technique.
- [2026-07-08] Added AI PR/code-review workflow as a first-class enablement concern: historical PR replay, local review standards, and understanding-preserving review artifacts.
```

`## Sources` — append:

```
- [Anthropic — Using Claude Code: Spending your effort](../sources/articles/claudedev-spending-your-effort-2026-09-25.md)
- [Latent Space — Thariq Shihipar on effort and implementation notes](../sources/newsletters/latent-space-thariq-effort-implementation-notes-2026-09-29.md)
```

### wiki/history/training/ai-enablement-software-development.md (updated)

Append at the end of the file (new archive block):

```
## Archived from current page on <apply date>

- [2026-07-01] Added software-factory/FDE rollout pattern: enterprise agent adoption needs workflow integration capacity, not only developer tooling.
```

### wiki/sources/articles/claudedev-spending-your-effort-2026-09-25.md (new)

```
---
title: 'Anthropic — Using Claude Code: Spending your effort'
type: source
source_type: article
source_file: raw/articles/2026-10-20-claudedev-blog-spending-your-effort.md
url: https://claude.dev/blog/spending-your-effort/
published: 2026-09-25
ingested: 2026-10-20
domains: [coding, models]
---

# Anthropic — Using Claude Code: Spending your effort

Thariq Shihipar (Anthropic, Claude Code) explains what the effort setting does and when to use each level, from his own runs of the same tasks at several levels on Opus 5.5 and a pass through every Terminal-Bench 3.0 result for Fable 5.1, Opus 5 and Fable 5. His conclusion: effort mainly changes how much verification and edge-case testing Claude does and how many judgment calls it makes on its own, so it pays off on edge-case-heavy work (security, hardware, code review) and matters little once a detailed spec is given. The same text was posted as an X Article (`raw/tweets/2026-09-25-trq212-2103576349499855160.md`); this page covers both.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — Terminal-Bench evidence bullet; effort rule of thumb added to the middle-tier FinOps control
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — spec → implement low/medium → verify high loop

## Key claims extracted

- Effort approximates how much compute the user wants spent; higher effort means more independent verification and judgment calls
- Underspecified build ("fitness tracker app"): low 1.5 min (log plus graph) vs max 67 min (much richer app); with a detailed spec from an interview, levels converge (16 to 79 min, similar designs)
- Terminal-Bench 3.0, Fable 5.1, 370 attempts per level: passes 140 at low (median 73k tokens) vs 214 at max (median 222k); "missed a case" failures 59 → 24; "made the wrong call" 133 → 107
- Pass rate low → top effort by area (Fable 5.1): security 64% → 87%, hardware 34% → 75%, ML 54% → 73%, science 41% → 61%, software 43% → 56%, media 18% → 30%, operations 12% → 22%
- Worked examples: `html-js-filter` 1/5 at low → 5/5 at xhigh (Fable 5.1); `mvcc-lsm-compaction` 0/5 → 4/5, `cli-2ph-simplex` 0/5 → 5/5, `gsea-proteomics` 0/5 → 4/5 (Opus 5.5)
- Rule of thumb: low for in-the-loop brainstorming and easy changes; medium for most feature work; high for verification-heavy work such as brownfield bugs; max for fully autonomous hard problems such as security audits
- Recommended loop: spec plus interview, implement at low effort, review, verify and test at high effort
- Numbers are internal runs, 5 attempts per task, production safety interventions off for Fable 5.1, security tasks without internet; they will not match the public leaderboard
```

### wiki/sources/newsletters/latent-space-thariq-effort-implementation-notes-2026-09-29.md (new)

```
---
title: 'Latent Space — Thariq Shihipar on effort and implementation notes'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-29-claude-codes-next-era-thariq-shihipar-anthropi.md
url: https://www.latent.space/p/thariq
published: 2026-09-29
ingested: 2026-10-20
domains: [coding]
---

# Latent Space — Thariq Shihipar on effort and implementation notes

The effort segment of Latent Space's interview with Anthropic's Thariq Shihipar ("Claude Code's next era"). He previews his effort blog post and adds a prompting tip the post does not carry: ask Claude for implementation or decision notes, because most failures he read in high-effort eval transcripts were cases where the model considered the correct solution and decided against it. The interview's other stories (Claude Mods, agent security, Pacing the Frontier) are covered by other source pages.

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — implementation-notes tip in the effort bullet

## Key claims extracted

- Effort is mostly spent on verification and edge-case testing, so it changes security evals a lot and ordinary software engineering much less
- Spending more time on the initial prompt and context avoids expensive redo cycles that eat usage
- Most high-effort eval failures are the model considering the right fix and rejecting it; implementation notes let the user catch and reverse those decisions
- Thariq expects frontier models to become cheaper than small models on many simple tasks because they need less verification
```

## Schema / vocabulary additions

None.

## Open questions

- Cost-aware AI task routing would sit at about 111% of the 2,500-word training ceiling. Split now? The natural seam is its three `###` evidence groups (model and harness selection wins, routing as infrastructure, cost variance) moving to a `training/cost-aware-routing-evidence.md` page, as was done for engineering adoption evidence. Default: no split in this proposal.
