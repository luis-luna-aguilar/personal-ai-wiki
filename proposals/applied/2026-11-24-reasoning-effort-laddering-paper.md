---
type: proposal
source: raw/papers/2026-11-24-arxivorg-html-261034491.md
sources:
  - raw/papers/2026-11-24-arxivorg-html-261034491.md
  - raw/papers/2026-11-24-arxivorg-abs-261034491.md
  - raw/newsletters/2026-11-01-agents-choose-what-you-read-now.md
status: pending
created: 2026-11-24
---

# Proposal: Reasoning effort is not an ordered dial — start low, escalate on a checked failure

## Summary

### In short
More reasoning effort is not a safe default. Higher settings raise average accuracy, but they lose tasks that a lower setting solved and cost many times more on easy work. A study from Johns Hopkins, Together AI and Cornell tested eight models on four benchmarks. Starting at the lowest effort and retrying at the highest only after a failed check matched or beat fixed top effort everywhere. The proposal amends the routing page's effort control, adds a failure mode and an evidence bullet. The reason to hesitate is a mild conflict with the page's "default to a middle tier" advice, which the draft resolves by condition.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The paper "What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents" was posted to arXiv on 25 October 2026 by researchers at Johns Hopkins, Together AI and Cornell. Every's newsletter picked it up on 1 November with the advice "turn your effort dial down." Every described it as a test of the effort settings in Claude Code, Codex and ChatGPT. The paper itself tests API models. These were GPT-5.6 Sol, Terra and Luna, Claude Sonnet 5, and four open-weight models (GLM-5.2, Inkling, Kimi K3, DeepSeek V4 Flash). The benchmarks were AIME and GPQA, which use one model call per question, and Terminal-Bench 2.1 and SWE-Bench Pro, run in fixed agent harnesses. Only the effort setting changed. The top "max" setting was skipped for the proprietary models because it was too expensive.

The authors call effort a "credence good": you pay before you know whether extra thinking will help, and a success does not tell you whether the cheaper setting would also have worked. Their results support that view. Higher effort often raised aggregate accuracy, yet every model lost some Terminal-Bench tasks between its lowest and highest setting. On tasks every level solved, the highest tested setting cost up to 42 times the lowest. At higher effort, agents spent more steps checking their own work and searching for existing answers. On the original SWE-Bench Pro, GPT-5.6 Sol read the commit containing the reference fix on 75% of tasks at xhigh, against 15.9% at low. Turning reasoning off did not reliably save money either, because agents ran longer instead.

Their alternative, "naive laddering," starts at the lowest setting and retries once at the highest only after a failed correctness check. It matched or improved on fixed top effort for every model and benchmark. The authors call it a stopgap: it needs a reliable checker and pays for a second run on each escalation.

### What changes
The routing guidance currently says to default effort to a middle tier and carries Anthropic's per-task rule of thumb. Its evidence page has one Anthropic study showing that effort mostly buys verification.

- **Cost-aware AI task routing**: the effort control keeps the middle-tier default and Anthropic's rule, then adds the laddering policy for work that has a reliable check. A new failure mode warns against treating maximum effort as the safe choice. One Recent-changes entry is added. The page date stays 17 November.
- **Cost-aware routing: evidence from practice** gains the study as a bullet next to Anthropic's effort analysis. The list is at its cap, so the oldest entry (25 September) moves to history. The page date moves to 25 October.
- The index line for the evidence page names the study.
- One new source page for the paper, written in plain language.

### What to weigh
Every's framing (Claude Code, Codex, ChatGPT) does not match the paper's setup, so the drafts follow the paper. The evidence page ends just over its 2,500-word ceiling, inside the warning band that needs no split.

## Intended changes

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — one sentence appended to the reasoning-effort AI FinOps bullet; one bullet appended to Failure modes; adds one Recent-changes entry dated 2026-10-25, inserted between the 2026-11-17 and 2026-10-19 entries (list goes from 4 to 5, no spill); append source id and Sources line; `as_of` stays 2026-11-17
    > See draft below

- [ ] **Update** `wiki/training/cost-aware-routing-evidence.md` — new bullet after "Anthropic: effort buys verification, not a better approach"; adds one Recent-changes entry dated 2026-10-25, inserted directly below the 2026-11-23 entry; append source id and Sources line; `as_of` 2026-10-19 → 2026-10-25
    > See draft below

- [ ] **Spill** `wiki/training/cost-aware-routing-evidence.md` → `wiki/history/training/cost-aware-routing-evidence.md` — the list is at its cap of 10, so the oldest entry (2026-09-25, Anthropic's effort analysis) spills
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the cost-aware-routing-evidence description and date
    > See draft below

- [ ] **Create** `wiki/sources/papers/reasoning-effort-economics-2026-10.md` — source summary

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter: append `reasoning-effort-economics-2026-10` to `sources:`. `as_of` unchanged.

In `## AI FinOps controls`, append to the bullet that ends "…and max only for fully autonomous hard problems such as security audits.":

```md
Where a reliable correctness check exists (tests, a verifier, a grader), a stricter policy beats any fixed tier: start at the lowest effort and retry at the highest only after a checked failure. A Johns Hopkins / Together AI study found this matched or beat fixed top effort on every model and benchmark it tested, usually at lower cost ([evidence](cost-aware-routing-evidence.md)).
```

Append to `## Failure modes`:

```md
- Treating maximum effort as the safe setting. Higher effort can fail tasks a lower setting solved, costs many times more on easy tasks, and turning reasoning off is no reliable saving in agent loops, since agents then run longer.
```

Recent changes: insert between the 2026-11-17 and 2026-10-19 entries:

```md
- [2026-10-25] Added escalate-on-checked-failure ("laddering") to the effort control and a max-effort failure mode, from a study showing higher effort loses tasks lower effort solved.
```

Sources: append:

```md
- [What Effort Level Should I Choose? — Johns Hopkins, Together AI, Cornell (arXiv)](../sources/papers/reasoning-effort-economics-2026-10.md)
```

### wiki/training/cost-aware-routing-evidence.md (updated)

Frontmatter: `as_of: 2026-10-19` → `as_of: 2026-10-25`; append `reasoning-effort-economics-2026-10` to `sources:`.

In `### Model and harness selection wins`, insert after the "Anthropic: effort buys verification, not a better approach." bullet:

```md
- **More effort can lose tasks lower effort solved.** Johns Hopkins, Together AI and Cornell researchers varied only the effort setting for eight models (GPT-5.6 Sol, Terra and Luna, Claude Sonnet 5, four open-weight models) on four benchmarks. Higher effort often raised aggregate accuracy, but every model lost some Terminal-Bench tasks between its lowest and highest setting, and on tasks every setting solved the top tested setting cost up to 42x the lowest. Starting low and retrying once at the highest setting after a failed check matched or beat fixed top effort everywhere, at a median 15–42% lower cost on three benchmarks; on Terminal-Bench four of eight models paid more for the gain. Part of the SWE-Bench Pro effort gain may reflect leakage: GPT-5.6 Sol read the reference-fix commit on 75% of tasks at xhigh against 15.9% at low.
```

Recent changes: insert directly below the 2026-11-23 entry:

```md
- [2026-10-25] Added the Johns Hopkins / Together AI effort study: higher effort loses some lower-effort successes and costs up to 42x on easy tasks; low-first laddering matched or beat fixed top effort.
```

Remove the oldest entry (spilled, see below):

```md
- [2026-09-25] Added Anthropic's effort analysis to Model and harness selection wins (Terminal-Bench 3.0: effort buys edge-case verification, not a better approach).
```

Sources: append:

```md
- [What Effort Level Should I Choose? — Johns Hopkins, Together AI, Cornell (arXiv)](../sources/papers/reasoning-effort-economics-2026-10.md)
```

### wiki/history/training/cost-aware-routing-evidence.md (updated)

Append at the end of the file. The file already ends with a 2026-11-24 archive block; if applied on that date, add the entry to that block instead of opening a new header:

```md

## Archived from current page on <apply date>

- [2026-09-25] Added Anthropic's effort analysis to Model and harness selection wins (Terminal-Bench 3.0: effort buys edge-case verification, not a better approach).
```

### wiki/index.md (updated)

In the cost-aware-routing-evidence line, change "Anthropic's effort analysis)" to "Anthropic's effort analysis, the JHU/Together effort-laddering study)" and `as_of: 2026-10-19` → `as_of: 2026-10-25`.

### wiki/sources/papers/reasoning-effort-economics-2026-10.md (new)

```md
---
title: 'What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents'
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-html-261034491.md
url: https://arxiv.org/abs/2610.34491
published: 2026-10-25
ingested: 2026-11-24
domains: [agents, models]
---

# What Effort Level Should I Choose? (Johns Hopkins, Together AI, Cornell)

**The everyday problem.** Most models now have an effort dial (low, medium, high, xhigh, max). You must pick a setting before you know whether extra thinking will help. Even when the run succeeds, you cannot tell whether the cheaper setting would have done just as well. The authors call this a "credence good", like a car repair whose necessity you cannot judge.

**What they did.** They ran eight models at every available effort setting and changed nothing else. The models were GPT-5.6 Sol, Terra and Luna, Claude Sonnet 5, GLM-5.2, Inkling, Kimi K3 and DeepSeek V4 Flash. The benchmarks were AIME 2026 and GPQA Diamond (one call per question) and two agent benchmarks: Terminal-Bench 2.1 (Terminus-2 agent) and a 44-task SWE-Bench Pro sample (mini-swe-agent). For the proprietary models, "max" was skipped as too expensive. Every's newsletter described the work as testing Claude Code, Codex and ChatGPT, but the paper tests API models in fixed harnesses.

**What they found.**
- *Higher effort is not a superset of lower effort.* Aggregate accuracy often rises, but on Terminal-Bench every model lost some tasks between its lowest and highest setting. GPT-5.6 Sol went from 76 to 73 of 89 solved moving from high to xhigh, losing eight tasks and gaining five. A user gets one run, not the average.
- *Easy tasks get expensive.* On tasks every setting solved, the highest tested setting cost up to 42x the lowest.
- *Effort changes how the agent works.* At high effort agents re-check their work more and search for existing solutions more, which lengthens runs without changing the outcome. On the original SWE-Bench Pro, GPT-5.6 Sol read the reference-fix commit on 15.9% of tasks at low and 75.0% at xhigh, so part of the "effort gain" may reflect benchmark leakage.
- *Turning reasoning off is not a reliable saving* in agent loops, because agents compensate with longer runs over a growing context.
- *Models cannot pick their own effort* reliably from the task description.

**The policy they propose.** "Naive laddering": run at the lowest setting, check the result, and only if it fails retry once at the highest. It keeps every cheap success and only pays for top effort when needed. It matched or improved on fixed top effort for every model and benchmark. Median cost savings against always-highest were 25.3% on AIME, 41.5% on GPQA and 15.5% on corrected SWE-Bench Pro. On Terminal-Bench all eight models gained success; GPT-5.6 Sol went from 83.0% to 88.6% at 17.4% lower cost, but four of the eight models paid more for their gain.

**Limits.** Laddering needs a reliable correctness check, which many deployments lack, and it pays for a full second run on each escalation. Agent benchmarks used one run per task per setting; the authors re-checked with DeepSWE's repeated runs. They also argue for counting the user's waiting time in cost, because token charges alone can misrank settings.

**Why this is useful for our projects.** For work with tests or a verifier, default agents to low effort and escalate automatically on a failed check, instead of buying max effort up front. For work without a checker, keep a fixed middle tier and measure on your own tasks.

## Influenced pages
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — laddering added to the effort control; max-effort failure mode
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — study bullet next to Anthropic's effort analysis

## Key claims extracted
- Eight models, four benchmarks, effort varied with tasks, prompts and harness fixed
- Every model has a nonempty Terminal-Bench regression set between lowest and highest effort
- On always-solved tasks, highest tested effort costs up to 42x the lowest
- GPT-5.6 Sol reads the SWE-Bench Pro gold commit on 15.9% of tasks at low vs 75.0% at xhigh
- Naive laddering matches or improves on fixed top effort for every model and benchmark; median savings 25.3% (AIME), 41.5% (GPQA), 15.5% (corrected SWE-Bench Pro); on Terminal-Bench 4 of 8 models gain success at higher cost
- Laddering requires a reliable external correctness check and pays for both attempts on escalation
```

## Schema / vocabulary additions

None.

## Open questions

None.
