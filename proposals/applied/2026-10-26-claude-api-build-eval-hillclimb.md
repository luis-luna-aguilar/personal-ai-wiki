---
type: proposal
source: raw/articles/2026-10-26-claudedev-blog-automating-eval-design-and-hillclimbing.md
status: pending
created: 2026-10-26
---

# Proposal: Automating eval design and hill-climbing with the claude-api skill

## Summary

### In short
An eval is only worth hill-climbing against if it passes a few checks first. A stronger model or more effort must score higher, the best setup must stay well below 100%, and the score must barely move between runs. Each change must also lift a held-out set. Anthropic built these rules into `/claude-api build-eval` and `/claude-api hillclimb` in Claude Code. In one example, held-out support tickets rose from 78.6% to 90.5% accuracy at about a fifth of the cost. The proposal updates **Evals for workflow and task agents**, **Automated harness optimization** and **Agent skill methodology**. One reason to hesitate: the post is undated.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Anthropic's claude.dev blog explains guidance it added to the claude-api skill, which ships inside Claude Code. A good eval, it says, mirrors production tasks and scores higher with stronger models and more effort; if it doesn't, a vague task or a bad grader is usually to blame. It leaves real headroom below 100% at the frontier, not explained by impossible tasks, and varies little between runs, though leftover state such as a file or git history can hand the agent the answer. Hard cases should be ones a person can explain as hard: picking only cases today's model fails measures that model's blind spots, not the job.

`/claude-api build-eval` gathers cases from production transcripts first, then tickets, a few hand-written cases and synthetic ones, and shows every input for review. It proposes the cheapest grader that fits: a code check where outputs are constrained, otherwise an LLM judge from a different model, scoring against checkable claims rather than a 1-to-5 scale. It runs the grader twice on the same output to catch drift and warns if the baseline already scores 95% or more.

`/claude-api hillclimb` holds out a random test set it never reads and checks that the eval's noise is smaller than the smallest gain worth acting on. Each round makes one root-cause patch, kept only if both train and test improve. After two or three flat rounds, Claude sorts the remaining failures by cause, which can expose broken tasks or graders. In the support example the climb ended on Sonnet 5 at low effort with a better prompt, at 1 cent per ticket instead of 4.6. On the claude-api skill's own eval the pass rate rose from 66% to 88%, once failure sorting showed the model was writing API shapes remembered from training despite the skill documenting current ones.

### What changes
The wiki already has LangChain's Better-Harness hill-climbing and a pass^k- and judge-focused page on workflow-agent evals. It has no checklist for whether an eval is fit to optimize against.

- **Evals for workflow and task agents** gains a section on designing an eval you can hill-climb (the four checks, how cases are sampled, grader validation) and a cost-routing example under Evidence from practice. It gains one Recent-changes entry, and the page date moves to 26 October.
- **Automated harness optimization** gains a short section on the hillclimb command's keep/revert rule, noise check and failure sorting. It gains one Recent-changes entry, and the page date moves to 26 October.
- **Agent skill methodology** gains one Evidence bullet: a model can ignore current guidance in a skill in favour of what it learned in training, and a "remembered form → current form" table near the top of the skill fixed it. It gains one Recent-changes entry, and the page date moves to 26 October.
- The **Index** dates for those three pages move, and there is one new source page.

### What to weigh
The post has no date. It uses Sonnet 5 rather than Sonnet 5.5, which suggests late September, but the drafts use the 26 October ingest date. **Automated harness optimization** ends at about 1,280 body words, 107% of its ceiling: a warning, not a split. The cost example was left off **Cost-aware AI task routing** because that page is already at its 110% limit.

## Intended changes

- [ ] **Update** `wiki/training/evals-for-agentic-work.md` — new section `## Designing an eval you can hill-climb` after `## Current guidance`; one Evidence-from-practice bullet; adds one Recent-changes entry dated 2026-10-26 (2 → 3, no spill); merges source id and link; `as_of` 2026-10-17 → 2026-10-26
- [ ] **Update** `wiki/concepts/automated-harness-optimization.md` — new section `## Guided hill-climbing in Claude Code` after `## Better-Harness`; adds one Recent-changes entry dated 2026-10-26 (5 → 6, no spill); merges source id and link; `as_of` 2026-10-09 → 2026-10-26
- [ ] **Update** `wiki/training/agent-skill-methodology.md` — one bullet in `## Evidence from practice`; adds one Recent-changes entry dated 2026-10-26 (8 → 9, no spill); merges source id and link; `as_of` 2026-09-03 → 2026-10-26
- [ ] **Update** `wiki/index.md` — as_of and description for the three pages above
- [ ] **Create** `wiki/sources/articles/claude-api-build-eval-hillclimb.md` — source summary

## Page drafts

### wiki/training/evals-for-agentic-work.md (updated)

Frontmatter (merge, do not replace):

```
as_of: 2026-10-26
sources: [...existing..., claude-api-build-eval-hillclimb]
```

Insert a new section after `## Current guidance`:

```
## Designing an eval you can hill-climb

Before tuning prompts, skills or model choice against an eval, check that the eval can tell a better setup from a worse one. Anthropic's four checks:

1. **Tasks mirror production.** Sample what the system will actually face, not what is easy to generate or grade.
2. **Stronger models and more effort score higher.** If they don't, suspect ambiguous tasks or a miscalibrated grader.
3. **Headroom at the frontier.** The best model at max effort should sit well below 100%, and not because of impossible tasks: a task that fails every replicate usually means a broken task. A good task is one where two domain experts would agree on the verdict and everything the grader checks is stated in the task.
4. **Low run-to-run variance.** Noise often comes from vague tasks, an unstable grader, inconsistently applied effort settings, or leftover environment state (a file, a git history) that hands the agent the answer.

**Sampling.** Pick hard cases because a person can say why they are hard, not because today's model fails them; failure-picked cases measure one model's blind spots. Order of preference: production transcripts, bug reports and tickets, five to ten hand-written cases, then synthetic cases anchored on real ones. Raw user traffic can skew easy, because users try what they expect to work.

**Grader.** Use the cheapest grader that fits: a code check (exact match, fixed label set, schema, tests) when outputs are constrained, otherwise an LLM judge from a different model than the one under test, with a rubric of checkable claims rather than a 1-to-5 scale, or a blind, order-randomized comparison against a baseline. Grade a handful of cases by hand and compare, then run the grader twice on the same output to catch drift. Check that timeouts, API errors and truncated answers aren't counted as model variance. If the baseline already scores ~95%, aim the work at cost or latency instead.

The `/claude-api build-eval` command in Claude Code walks through these steps, pausing for approval of the inputs and grader. The hill-climbing side is on [Automated harness optimization](../concepts/automated-harness-optimization.md).
```

In `## Evidence from practice`, append:

```
- **Hill-climbing for cost on a support eval (Anthropic).** On 44 support tickets (30 searched, 14 held out), `/claude-api hillclimb` first removed mandatory tool-call rituals, a scratchpad step and contradictory rules from the prompt, then moved from Opus 4.8 at high effort to Opus 5.5 at low effort, then stepped down to Sonnet 5 at low effort, which scored the same at about half the cost. Routing rules and a refund-cap cross-reference took search accuracy from 74.4% to 98.9% and cost per ticket from 4.6¢ to 1¢. On the held-out tickets the final setup scored 90.5% against 78.6% at roughly a fifth of the cost. That gap is why the held-out number is the one to report.
```

In `## Recent changes`, insert as the newest entry:

```
- [2026-10-26] Added Anthropic's checks for an eval you can hill-climb (production-like tasks, scores rising with model and effort, headroom, low variance), plus case sampling, grader validation, and a support-ticket cost hill-climb (held-out 78.6% → 90.5% at ~1/5 the cost).
```

In `## Sources`, append:

```
- [Anthropic — Automating eval design and hillclimbing with Claude](../sources/articles/claude-api-build-eval-hillclimb.md)
```

### wiki/concepts/automated-harness-optimization.md (updated)

Frontmatter (merge, do not replace):

```
as_of: 2026-10-26
sources: [...existing..., claude-api-build-eval-hillclimb]
```

Insert a new section after `## Better-Harness: autonomous harness hill-climbing`:

```
## Guided hill-climbing in Claude Code

Anthropic's `/claude-api hillclimb` productizes the same loop. The user picks what may change (prompt, skills, tool descriptions, model and effort, harness code) and the goal (quality, or cost at equal quality). A random test split is never read, and the eval's noise must be smaller than the smallest gain worth acting on. Each round makes one root-cause patch, kept only if train and test both rise. Failing transcripts never go into the prompt. After two or three flat rounds Claude sorts the remaining failures by cause, which catches broken tasks and graders. It advises against merging gains within noise. Cheap, attributable surfaces (prompt text, skill descriptions) climb best; open-ended harness rewrites and near-saturated evals stall. Eval design is on [Evals for workflow and task agents](../training/evals-for-agentic-work.md).
```

In `## Recent changes`, insert as the newest entry:

```
- [2026-10-26] Added Anthropic's `/claude-api hillclimb`: train/test split, noise check, one patch per round kept only if both sets rise, failure sorting by cause when the score stalls.
```

In `## Sources`, append:

```
- [Anthropic — Automating eval design and hillclimbing with Claude](../sources/articles/claude-api-build-eval-hillclimb.md)
```

### wiki/training/agent-skill-methodology.md (updated)

Frontmatter (merge, do not replace):

```
as_of: 2026-10-26
sources: [...existing..., claude-api-build-eval-hillclimb]
```

In `## Evidence from practice`, append:

```
- **Training priors can override the skill.** Hill-climbing Anthropic's claude-api skill against a docs-derived eval took it from 66% to 88%. Adding eight missing features and fixing C#/Java type tables got it to 77%. Sorting the remaining failures by cause then showed the skill already had the right content, but Claude kept writing older API shapes it remembered from training (fixed-budget extended thinking instead of adaptive thinking, old web-search and web-fetch tool versions). A "remembered form → current form" table near the top of the skill fixed most of it. The same sort exposed tasks whose graders contradicted the docs, which were fixed rather than climbed against.
```

In `## Recent changes`, insert as the newest entry:

```
- [2026-10-26] Added the claude-api skill hill-climb (66% → 88%): a model can ignore current guidance in favour of training priors; a remembered-to-current mapping table near the top fixed it.
```

In `## Sources`, append:

```
- [Anthropic — Automating eval design and hillclimbing with Claude](../sources/articles/claude-api-build-eval-hillclimb.md)
```

### wiki/index.md (updated)

```
- [concepts/automated-harness-optimization](concepts/automated-harness-optimization.md) — systems that improve an agent's harness automatically: Better-Harness and Claude Code's /claude-api hillclimb, label-free Harness², self-improving skills, self-modifying harnesses, guarded evolution *(as_of: 2026-10-26)*
- [training/agent-skill-methodology](training/agent-skill-methodology.md) — evals-first method for writing maintainable agent skills with natural triggers, principles, production lessons, pruning, portable domain judgment, and benchmark evidence (SkillsBench, SWE-Skills-Bench, Skill Lift, retrieval actual-use effect) *(as_of: 2026-10-26)*
- [training/evals-for-agentic-work](training/evals-for-agentic-work.md) — eval patterns for workflow and task agents: designing an eval you can hill-climb, pass^k reliability, task-specific metrics, simulated users *(as_of: 2026-10-26)*
```

### wiki/sources/articles/claude-api-build-eval-hillclimb.md (new)

```
---
title: Anthropic — Automating eval design and hillclimbing with Claude
type: source
source_type: article
source_file: raw/articles/2026-10-26-claudedev-blog-automating-eval-design-and-hillclimbing.md
url: https://claude.dev/blog/automating-eval-design-and-hillclimbing/
ingested: 2026-10-26
domains: [agents, coding]
---

# Anthropic — Automating eval design and hillclimbing with Claude

Anthropic's claude.dev post on eval-design and hill-climbing guidance added to the claude-api skill in Claude Code. `/claude-api build-eval` builds an eval in the user's codebase: it samples cases from production first, validates the grader with the user, and runs noise, plumbing and headroom checks. `/claude-api hillclimb` improves a prompt, skill, model choice or harness one patch at a time, with a held-out split to catch overfitting. Two worked examples: a support-ticket cost climb and the claude-api skill's own eval. No publication date in the post; ingest date used (it uses Sonnet 5, not 5.5, suggesting late September 2026).

## Influenced pages

- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — eval-design checks, case sampling, grader validation, support-ticket example
- [Automated harness optimization](../../concepts/automated-harness-optimization.md) — the hillclimb loop and its overfitting guards
- [Agent skill methodology](../../training/agent-skill-methodology.md) — training priors overriding skill content

## Key claims extracted

- Four elements of a good eval: tasks mirror production; stronger models and more effort score higher; "passable" headroom at the frontier (not from impossible/ambiguous tasks); low run-to-run variance (including environment leftovers)
- Adversarial sampling: choosing cases today's model fails samples its capability valleys; pick cases a human can explain as hard; user traffic can skew easy
- build-eval input order: production transcripts (after retention/sensitivity questions), bug reports/tickets, 5–10 hand-written, codebase-synthesized; review page before proceeding
- Grader: cheapest that fits; programmatic when outputs are constrained; otherwise LLM judge, different model from the one tested, rubric as checkable claims, blind random-order comparison against a baseline when one exists
- Diagnostics: grader run twice on identical output; timeouts/API errors/truncation; warn when baseline ≥ ~95%
- Hillclimb: random train/test split; noise must be below the smallest actionable gain; one root-cause patch per round; keep only if train and test both improve; revert on train-only gain or any regression; after 2–3 stalled rounds, sort failures by cause; finish on the best test-set version; recommend against merging gains within noise
- Overfitting guards: split cases, never paste failures into the prompt, keep answers structurally out of reach
- Support example: 44 tickets (30 search / 14 held out); Opus 4.8 high 74.4% at 4.6¢ → Opus 5.5 low 87.8% at 1.9¢ → Sonnet 5 low 88.9% at 1¢ → improved prompt 98.9% at 1¢; held-out 90.5% vs 78.6% at ~1/5 the cost; Opus 5.5 tokens 20% cheaper than Opus 4.8, cache reads 60% cheaper
- claude-api skill eval: 66.1% → 74% (eight missing features) → 77% (C#/Java type tables) → 80% (remembered-to-current API table) → ~88% (fixed a mis-specified task and a grader contradicting the docs)
```

## Schema / vocabulary additions

None.

## Open questions

None.
