---
type: proposal
source: raw/articles/2026-10-20-tco-bq3ymfajqh.md
sources:
  - raw/articles/2026-10-20-tco-bq3ymfajqh.md
  - raw/tweets/2026-10-14-bertgodel-2110400987622265232.md
  - raw/newsletters/2026-10-15-ainews-modals-1b-arr-16b-series-d-makes-it-n.md
triage: proposals/triage/2026-10-11-to-2026-10-20-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Ultramarine 1 Flash, RL for work with no single right answer

## Summary

### In short

Reinforcement learning now works on professional work that has no single right answer, as long as the grading rubric is written with the task and each criterion tests one checkable claim. Paper Instruments shows it with Ultramarine 1 Flash, a GLM-5.3 Flash post-train that gains 4.1 points across six knowledge-work benchmarks, costs $0.13 per task, and was trained by five people for about $300k. The proposal adds a model page, a Domain-specialized models line, rubric guidance on the workflow-evals page, and RL-environment lessons. One hesitation: weights are not out yet, and the model only loosely fits a one-profession category.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

Paper Instruments, a small lab that sells to AI companies serving banks and law firms, published a long technical report on 14 October 2026 alongside a launch thread from co-founder Daanish Khazi. Ultramarine 1 Flash is Z.ai's open GLM-5.3 Flash with a large reinforcement-learning stage on top (RL here means letting the model attempt thousands of tasks and nudging it toward the attempts that score well). Coding RL is easy to score with tests; diligence memos and board pre-reads are not. The report's answer is to synthesise each task together with its rubric. A criterion copied from one golden answer rejects valid alternatives; a vague one ("provides a useful update") rewards plausible errors. Good criteria state one substantive proposition, with the facts and thresholds needed to check it, and are judged met or unmet.

The curriculum is fully synthetic: 88 environment types across finance, law, consulting and operations, each a mounted workspace with real filings, synthetic documents, and live CRM or ledger systems behind MCP. Training ran in Feather, the lab's own minimal harness, with a 50-token system prompt so that prescriptive production instructions would not narrow exploration. Sandbox crashes are dropped from training instead of scored as zero, and the agent loop runs outside the sandbox so the model cannot touch its grader. The thread claims Fable 5-level performance at 60x lower cost; the report itself says Ultramarine beats Fable 5 and GPT-5.6 Sol on the lab's internal suite and trails Opus 5.5 and GPT-6 Sol by two to three points, while losing on DiligenceBench and APEX-Agents and slipping slightly on coding. API access is live; weights and training code were promised within two weeks.

### What changes

The wiki has no page on RL for non-verifiable work. Rubric advice exists only as a short "calibrated rubrics" bullet, and the Domain-specialized models section holds one medical model.

- New page `models/ultramarine-1-flash.md` with the recipe, results, and caveats, dated 14 October.
- **State of Models** gains an Ultramarine line under Domain-specialized models and a Recent-changes entry; the oldest entry (Grok 4.6, 13 August) spills to history.
- **Evals for workflow and task agents** gains a "one proposition per criterion" safeguard in its LLM-as-judge section and a Recent-changes entry; its date stays 17 October.
- **RL harness quality** gains a short section on three environment-design choices from the report; date moves to 14 October.
- Two source pages, one for the report and one for the launch thread.

### What to weigh

The domain-specialized subcategory is defined as "one profession"; Ultramarine spans four professional domains, and it belongs in Open-weight models once weights ship. The headline "60x cheaper than Fable 5" is the thread's framing; the drafts use the report's own per-task numbers. The AINews item only repeats the thread, so it gets no source page.

## Intended changes

- [ ] **Create** `wiki/models/ultramarine-1-flash.md` — new model page
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — adds one line under "Domain-specialized models"; adds one Recent-changes entry dated 2026-10-14; merges two source ids into `sources:`; `as_of` stays 2026-10-20
    > **After (new line):** `- [Ultramarine 1 Flash](../models/ultramarine-1-flash.md) — Paper Instruments; RL post-train of GLM-5.3 Flash for finance, legal, and consulting deliverables; 59.3 on its internal suite at $0.13/task (Fable 5: 57.8 at $8.19); weights promised *(as of 2026-10-14)*`

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — list is at the cap of 10; spills the oldest entry (2026-08-13 Grok 4.6) under a new archive header

- [ ] **Update** `wiki/training/evals-for-agentic-work.md` — adds one safeguard bullet to "LLM-as-judge for qualitative dimensions"; adds one Recent-changes entry dated 2026-10-14; merges one source; `as_of` stays 2026-10-17

- [ ] **Update** `wiki/concepts/rl-harness-quality.md` — adds a "Design choices from a non-verifiable RL run" section; adds one Recent-changes entry dated 2026-10-14; merges one source; `as_of` 2026-09-09 → 2026-10-14

- [ ] **Create** `wiki/sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md` — source summary for the tech report

- [ ] **Create** `wiki/sources/tweets/bertgodel-ultramarine-launch-2026-10-14.md` — source summary for the launch thread

## Page drafts

### wiki/models/ultramarine-1-flash.md (new)

```
---
title: Ultramarine 1 Flash
type: model
domains: [models, finance, legal]
subcategory: domain-specialized-model
tags: [agentic]
as_of: 2026-10-14
sources: [paper-instruments-ultramarine-1-flash-2026-10-14, bertgodel-ultramarine-launch-2026-10-14]
---

# Ultramarine 1 Flash

Paper Instruments' agentic model for professional knowledge work (finance, law, consulting, operations): Z.ai's open GLM-5.3 Flash (see [GLM-5.3](glm-5-3.md)) with a large reinforcement-learning stage on synthetic tasks graded by rubrics. Its main contribution is a recipe for RL on work that has no single right answer, such as diligence memos and board pre-reads.

## Current status (as of 2026-10-14)

- Released 2026-10-14 on API; weights, training code, and tech report promised within two weeks. Post-trained by a team of five for about $300k all-in
- Beats its base on all six knowledge-work benchmarks reported (+4.1 points on average) with 6.5% fewer output tokens
- Internal PI Knowledge Work suite: 59.3 at $0.13 per task, vs Claude Fable 5 57.8 at $8.19 and GPT-5.6 Sol 55.1 at $2.09; trails Claude Opus 5.5 by 2.6 points ($6.96) and GPT-6 Sol by 2.0 ($1.26)
- Leads JobBench (62.9) and FrontierFinance (53.3) in its comparison set; behind Gemini 3.8 Flash and Fable 5 on DiligenceBench and APEX-Agents 1.1 (57.0 vs 64.3)
- Coding slips slightly below the base: Terminal-Bench 2.1 83.2 (base 84.3), DeepSWE 61.5 (base 63.4)

## How it was trained

- **Task and rubric co-design.** Each task is synthesised with its rubric; each criterion tests one proposition with the facts needed to check it, so it neither copies one golden answer nor rewards plausible errors (see [Evals for workflow and task agents](../training/evals-for-agentic-work.md))
- **Synthetic curriculum.** 88 environment types across 19 practice areas, each a workspace of real filings and synthetic documents plus live CRM, ERP, and ticketing systems behind MCP; production traces were rejected because they bake one user's unstated assumptions into the reward
- **Minimal harness.** Its own Feather harness with a 50-token system prompt; production instructions added only at the end (see [RL harness quality](../concepts/rl-harness-quality.md))

## Weaknesses / caveats

- The "Fable 5-level at 60x cheaper" headline comes from the launch thread; the report's strongest comparison is its own internal suite, and DiligenceBench is also the lab's own benchmark
- No vision training
- Weights not yet released as of the launch date

## Recent changes

- [2026-10-14] Released on API with a technical report; weights promised within two weeks.

## Sources

- [Ultramarine 1 Flash: Scaling Non-Verifiable RL](../sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md)
- [Daanish Khazi — Ultramarine 1 Flash launch thread](../sources/tweets/bertgodel-ultramarine-launch-2026-10-14.md)
```

### wiki/state-of/models.md (updated)

Frontmatter: append `paper-instruments-ultramarine-1-flash-2026-10-14, bertgodel-ultramarine-launch-2026-10-14` to `sources:`. `as_of` unchanged (2026-10-20).

Domain-specialized models section (one line added after MedDecider-27B):

```
### Domain-specialized models

Models fine-tuned for one profession's decisions or knowledge, evaluated on that domain's tasks rather than general benchmarks.

- [MedDecider-27B](../models/meddecider-27b.md) — thelion.ai; calibrated per-option probabilities for clinical decisions in one scoring pass; LoRA on Qwen3.8-27B; leads its 27B-class comparison on robustness (88.3%); CC BY-NC *(as of 2026-10-19)*
- [Ultramarine 1 Flash](../models/ultramarine-1-flash.md) — Paper Instruments; RL post-train of GLM-5.3 Flash for finance, legal, and consulting deliverables; 59.3 on its internal suite at $0.13/task (Fable 5: 57.8 at $8.19); weights promised *(as of 2026-10-14)*
```

Recent changes: insert one entry in date order (after the 2026-10-19 entries, before 2026-09-03), then drop the oldest (2026-08-13 Grok 4.6), which spills:

```
- [2026-10-14] Added Ultramarine 1 Flash (Paper Instruments) to Domain-specialized models: RL post-train of GLM-5.3 Flash on rubric-graded synthetic knowledge-work tasks, +4.1 points over its base across six benchmarks at $0.13 per task.
```

### wiki/history/state-of/models.md (updated)

Append at the end of the file:

```
## Archived from current page on <apply date>

- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

### wiki/training/evals-for-agentic-work.md (updated)

Frontmatter: append `paper-instruments-ultramarine-1-flash-2026-10-14` to `sources:`. `as_of` stays 2026-10-17.

In "LLM-as-judge for qualitative dimensions", insert after the "Calibrated rubrics" bullet:

```
- **One proposition per criterion:** each criterion should draw a boundary around acceptable answers. One copied from a single golden answer ("uses the phrase 'sole forecast basis'") rejects valid alternatives; a vague one ("provides a useful update") also passes incomplete or wrong answers. State the substantive condition that earns credit, with the entities, dates, and thresholds needed to check it; keep independent accomplishments as separate criteria so partial work earns partial credit. Paper Instruments used this rule to grade RL training tasks for its Ultramarine model and argues criterion boundaries matter more than picking a stronger judge (Oct 2026).
```

Recent changes: add one entry at the top:

```
- [2026-10-14] Added "one proposition per criterion" rubric guidance (overfit vs. vague criteria) from Paper Instruments' Ultramarine RL report.
```

Sources: append

```
- [Paper Instruments — Ultramarine 1 Flash: Scaling Non-Verifiable RL](../sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md)
```

### wiki/concepts/rl-harness-quality.md (updated)

Frontmatter: `as_of: 2026-10-14`; append `paper-instruments-ultramarine-1-flash-2026-10-14` to `sources:`.

New section, inserted before `## Why it matters`:

```
## Design choices from a non-verifiable RL run

Paper Instruments' Ultramarine 1 Flash report (Oct 2026) adds three environment-design choices that guard against the failure modes above:

- **Score only failures the policy caused.** Malformed calls and failing commands return an error and the trajectory continues; a lost sandbox or broken tool transport ends the attempt, which is excluded from training rather than scored zero, so infrastructure noise never enters the reward.
- **Keep the agent loop outside the sandbox.** Commands run in the sandbox, but the loop, credentials, and grader live on the orchestrator, and task-specific grading material arrives only after the rollout, so nothing the model does can alter its own harness or grader.
- **Train on neutral instructions.** A 50-token system prompt and tool descriptions that say what a tool does, not when to use it; prescriptive production prompts (1,800–4,400 tokens in surveyed harnesses) were added only in the final stage, because they narrow exploration during training.
```

Recent changes: add one entry at the top:

```
- [2026-10-14] Added three environment-design choices from Paper Instruments' Ultramarine 1 Flash report: exclude environment failures from the reward, keep the agent loop outside the sandbox, train on neutral instructions.
```

Sources: append

```
- [Paper Instruments — Ultramarine 1 Flash: Scaling Non-Verifiable RL](../sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md)
```

### wiki/sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md (new)

```
---
title: 'Ultramarine 1 Flash: Scaling Non-Verifiable RL — Paper Instruments'
type: source
source_type: article
source_file: raw/articles/2026-10-20-tco-bq3ymfajqh.md
url: https://www.paperinstruments.com/blog/ultramarine
published: 2026-10-14
ingested: 2026-10-20
domains: [models, agents, finance, legal]
---

# Ultramarine 1 Flash: Scaling Non-Verifiable RL — Paper Instruments

Technical report for Ultramarine 1 Flash, a reinforcement-learning post-train of GLM-5.3 Flash for professional knowledge work. The core contribution is a recipe for rewarding open-ended deliverables: tasks and rubrics are synthesised together, each criterion tests one proposition, and filters screen for answer leakage and reward hacking. The curriculum is fully synthetic (88 environment types across finance, law, consulting, operations), trained in the lab's minimal Feather harness on E2B sandboxes with a modified CISPO objective, LoRA rank 64, and 131k context.

## Influenced pages

- [Ultramarine 1 Flash](../../models/ultramarine-1-flash.md) — new page
- [State of Models](../../state-of/models.md) — Domain-specialized models line
- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — one-proposition-per-criterion rubric guidance
- [RL harness quality](../../concepts/rl-harness-quality.md) — three environment-design choices

## Key claims extracted

- Improves on GLM-5.3 Flash across all six knowledge-work benchmarks, +4.1 points on average, with 6.5% fewer tokens
- PI Knowledge Work (internal): 59.3 at $0.13/task vs Fable 5 57.8 ($8.19), GPT-5.6 Sol 55.1 ($2.09); within 2.6 of Opus 5.5 and 2.0 of GPT-6 Sol
- JobBench 62.9, FrontierFinance 53.3, APEX-Agents 1.1 57.0 (Gemini 3.8 Flash 64.3); Terminal-Bench 2.1 83.2 (base 84.3)
- Overfit criteria reject valid answers; vague criteria reward plausible errors; criterion boundaries matter more than a stronger judge
- Production traces rejected as RL data because they embed one user's unstated assumptions into the reward
- Environment failures are excluded from training, not scored zero; agent loop and grader sit outside the sandbox
- Training system prompt is ~50 tokens; production instructions only introduced in final stages
```

### wiki/sources/tweets/bertgodel-ultramarine-launch-2026-10-14.md (new)

```
---
title: 'Daanish Khazi (@bertgodel) — Releasing Ultramarine 1 Flash'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-14-bertgodel-2110400987622265232.md
url: https://x.com/bertgodel/status/2110400987622265232
published: 2026-10-14
ingested: 2026-10-20
domains: [models]
---

# Daanish Khazi (@bertgodel) — Releasing Ultramarine 1 Flash

Launch thread from Paper Instruments' co-founder. Adds the team-size, cost, and release-timing claims not in the technical report.

## Influenced pages

- [Ultramarine 1 Flash](../../models/ultramarine-1-flash.md) — release status, training cost, headline claim

## Key claims extracted

- Claims performance similar to Claude Fable 5 at 60x lower cost
- Post-trained by a team of five for about $300k all-in
- Available on API now; weights in two weeks; training code and tech report open-sourced
- Built for AI companies serving banks and law firms
```

## Schema / vocabulary additions

None.

## Open questions

- Rubric-graded RL for non-verifiable work now spans a model page, an evals page, and an RL page. Should a later source on the same theme get its own concept page (for example `concepts/non-verifiable-rl.md`), or keep living on those three?
