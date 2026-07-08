---
type: proposal
source: raw/newsletters/2026-07-08-claude-cowork-now-runs-on-mobile.md
status: pending
created: 2026-07-08
---

# Proposal: AI pull-request review as a first-class workflow

## Summary

DoorDash's DashBench and Geoffrey Litt's "understanding is the bottleneck" argument make AI pull-request review bigger than a small eval bullet. The topic spans reviewer execution, historical PR replay, model-combo benchmarking, human comprehension, review artifacts, and the management problem of deciding when code can move from human-visible review into more autonomous execution.

This reframes PR/code-review analysis into a dedicated training page, then trims the surrounding pages down to pointers so the topic has one durable home.

## Intended changes

- [x] **Create** `wiki/training/ai-pr-code-review.md` — new first-class page for AI-assisted pull request analysis, review execution, historical PR replay, and understanding-preserving review.
- [x] **Update** `wiki/training/evals-for-agentic-software-development.md` — keep the eval-stack framing, but move detailed AI code review guidance into the new page.
- [x] **Update** `wiki/training/ai-enablement-software-development.md` — point engineering enablement guidance at the new dedicated PR-review page instead of adding another local bullet.
- [x] **Update** `wiki/concepts/agent-evals.md` — add DashBench as a historical-work replay example and link to the dedicated PR-review page.
- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — connect review standards / review artifacts to the new PR-review page.
- [x] **Update** `wiki/index.md` — add the new training page.
- [x] **Create** `wiki/sources/newsletters/dashbench-code-review-understanding-2026-07.md` — source summary.

## Page drafts

### wiki/training/ai-pr-code-review.md (new)

```md
---
title: AI PR and code review
type: training
domains: [coding, agents, training]
tags: [agentic]
as_of: 2026-07-08
sources: [ai-code-review-eval-integrity-2026-06, agent-review-artifacts-2026-05-13, dashbench-code-review-understanding-2026-07]
---

# AI PR and code review

AI pull-request review is becoming its own workflow, not just a final checkbox after code generation. The useful question is no longer "can an AI leave plausible comments on a diff?" It is whether the review system catches real defects, applies local standards, produces evidence humans can inspect, and helps the human keep enough understanding to steer the next agent loop.

This page covers both sides of the workflow: automated review execution and human understanding preservation.

## Current guidance

- Treat PR review as a high-compute, high-context step. Fast generic comments are cheap to produce and easy for teams to ignore.
- Keep reviewed PRs small enough that both the model and the human can reason about the diff.
- Put team-specific review standards in repo-local Markdown so the reviewer applies local architecture, security, naming, migration, and testing norms instead of generic style taste.
- Trigger AI review deliberately, for example through a manual CI job or merge-gate workflow, rather than commenting on every push.
- Use deterministic gates first: compile, test, lint, type-check, secret scan, dependency scan, and scope-impact checks before qualitative model review.
- Ask the review agent to emit evidence, not only opinions: changed files, risk areas, invariants, missing tests, suspected regressions, and exact code references.
- Require a human-facing understanding artifact for meaningful agent-written diffs: what changed, why, what assumptions the agent made, what could break, and what the reviewer should verify.

## Review execution stack

A practical AI PR review stack is layered:

1. **Surface logic review** — summarize the diff, identify changed behavior, and map the change to the stated task.
2. **Deterministic checks** — run the repo's existing tests and static checks before asking a model for qualitative judgment.
3. **Scope and blast-radius checks** — verify the PR did not touch unrelated modules, configuration, schemas, credentials, generated files, or deployment paths.
4. **Deep code review** — use a capable model with the repo's local review standards to inspect architecture, security, edge cases, migrations, and test adequacy.
5. **Human comprehension artifact** — generate an annotated explainer or teaching document so the reviewer understands the change well enough to approve, redirect, or start the next agent loop.
6. **Eval capture** — record accepted comments, rejected comments, missed issues, and post-merge failures as future review eval data.

The review agent should have access to the task brief, diff, relevant files, tests, local instructions, and prior review standards. It should not be asked to infer the team's norms from the patch alone.

## Historical PR replay

DashBench, from DoorDash, is an important eval pattern because it evaluates AI reviewers against historical PRs and known issues rather than synthetic prompts. The point is to test whether a reviewer catches the kinds of defects that mattered in the real codebase.

The Code's July 8, 2026 coverage reports that a Kimi K2.6 + Claude Fable 5 combination beat DoorDash's own production setup on weighted recall. The operational lesson is not that one model is universally best. It is that review quality depends on the model mix, prompt, harness, repository context, scoring rubric, and defect distribution. Teams should benchmark review systems against their own past misses before trusting them on future PRs.

Good historical replay datasets include:

- PRs where reviewers caught important issues before merge
- PRs that introduced production incidents or regressions
- PR comments that led to meaningful code changes
- Security fixes, migration mistakes, data-shape bugs, and flaky-test repairs
- Human review decisions that distinguish accepted findings from noisy comments

## Understanding-preserving review

Geoffrey Litt's "understanding is the new bottleneck" argument is the human side of the same workflow. Verification is not the only reason to read code. The reviewer needs a mental model of the change because that model drives the next prompt, architecture decision, rollback question, or follow-up task.

If humans stop understanding agent-written code, cognitive debt accumulates. The system may keep shipping, but the human loses the ability to steer it.

A practical pattern is **explain-diff review**:

- The agent explains the diff before the reviewer reads it line by line.
- The explanation names the changed behavior, assumptions, invariants, and risk areas.
- The agent asks a small quiz or checklist that forces the reviewer to reconstruct the mental model.
- The reviewer does not approve until they can explain the change back in their own words.

This is different from asking for a prettier PR summary. The goal is to preserve the human's ability to participate in the next loop.

## Review artifacts

For complex PRs, the review surface matters. A GitHub diff is often too low-context for agent-written changes, especially when the change spans files, migrations, UI behavior, or hidden assumptions.

Useful artifacts include:

- Annotated HTML explainers with the actual diff, architecture diagram, risk areas, and reviewer questions
- Markdown review memos that separate facts, assumptions, risks, and suggested tests
- Checklists tied to local standards, such as migrations, permissions, privacy, accessibility, and rollback
- Browser traces, screenshots, or videos for frontend-changing work
- Reproduction steps and failing-test evidence for bug fixes

Artifacts should make review faster and more accurate. They should not become decorative paperwork that hides the underlying diff.

## Failure modes

- **Plausible-comment review:** the model leaves reasonable-sounding comments that do not catch the actual risky behavior.
- **Generic standards:** the review applies generic best practices while missing team-specific architecture, data, security, or operational constraints.
- **Large-diff blindness:** the PR is too broad for either the model or human to build a coherent mental model.
- **Review noise:** automated comments fire on every push, teams learn to ignore them, and real findings get buried.
- **Cognitive debt:** humans approve code they cannot explain, which weakens their ability to direct future agent work.
- **Eval leakage:** the review benchmark becomes a public or overfit artifact that models can game rather than a realistic test of review judgment.

## Evidence from practice

- DoorDash's DashBench replays historical PRs to evaluate whether AI reviewers catch real issues in DoorDash's own code-review distribution.
- The Code reports that model combinations matter: a Kimi K2.6 + Claude Fable 5 combo beat DoorDash's production setup on weighted recall in the covered benchmark.
- Shopify built its own PR review tooling because external tools did not spend enough compute on expensive models during review, suggesting review quality is becoming a bottleneck as generation gets cheaper.
- Geoffrey Litt's `explain-diff` pattern turns changes into teaching artifacts and quizzes so understanding survives the agent loop.

## Related

- [Evals for agentic software development](evals-for-agentic-software-development.md) — broader eval stack for coding agents
- [AI enablement — software development](ai-enablement-software-development.md) — broader engineering adoption and supervision guidance
- [Agent evals](../concepts/agent-evals.md) — why historical replay and trajectory analysis matter
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — where review artifacts fit in agent loops

## Recent changes

- [2026-07-08] Created dedicated AI PR/code-review page from DashBench and understanding-preserving review coverage.

## Sources

- [AI code review and benchmark integrity](../sources/newsletters/ai-code-review-eval-integrity-2026-06.md)
- [Purpose-built review artifacts for agent work](../sources/tweets/agent-review-artifacts-2026-05-13.md)
- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
```

### wiki/training/evals-for-agentic-software-development.md (updated sections)

```md
---
title: Evals for agentic software development
type: training
as_of: 2026-07-08
sources: [agents-evals-deep-research, qa-tooling-for-software-agents-deep-research, cost-aware-agent-evaluation-2026-04-28, opus-4-7-tokenizer-economics-2026-04-30, agentic-security-tooling-2026-05-13, ai-code-review-eval-integrity-2026-06, dashbench-code-review-understanding-2026-07]
---

## Current guidance

Add / revise these bullets:

- Use historical PR replay for code-review evals when possible: test whether the reviewer catches real past defects, not whether it writes plausible comments.
- For detailed AI PR-review execution patterns, use [AI PR and code review](ai-pr-code-review.md); this page keeps the broader eval-stack framing.

## Task-specific eval patterns

Replace the `Code review` row with:

| Code review | Historical PR replay + stacked tool evaluation: deterministic gates, scope checks, LLM architectural review, and human-audited accepted/rejected comments | Plausible review comments that miss real defects or local standards |

## Converting real artifacts into eval cases

Update the opening paragraph:

Production artifacts (bug reports, PR review comments, postmortems, and historical PRs) are the highest-quality source of eval cases because they reflect real failures, not synthetic prompts. For code review specifically, historical PR replay should preserve both the original diff and the known review outcome so the AI reviewer can be scored against defects humans actually cared about. See [AI PR and code review](ai-pr-code-review.md) for the dedicated workflow.

## AI code review

Replace this section with:

AI code review is now large enough to warrant its own page. See [AI PR and code review](ai-pr-code-review.md) for review execution, historical PR replay, model-combo benchmarking, review artifacts, and understanding-preserving review.

## Evidence from practice

Add:

- DoorDash's DashBench evaluates AI reviewers by replaying historical PRs, a stronger signal than synthetic review prompts because it anchors review quality to real team-specific defects.

## Recent changes

- [2026-07-08] Moved detailed AI PR/code-review execution guidance into a dedicated page and added DashBench historical PR replay as the review-eval pattern.
- [2026-06-26] Added AI review workflow guidance and public-benchmark leakage caveat from The Code / AINews coverage.

## Sources

Add:

- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
```

### wiki/training/ai-enablement-software-development.md (updated sections)

```md
---
title: AI enablement — software development
type: training
as_of: 2026-07-08
sources: [ramp-ai-adoption-playbook, shopify-latent-space-april-2026, lennysan-simonw-interview, agentic-cognitive-overhead, garrytan-gstack-repo, the-code-2026-04-23, qa-tooling-for-software-agents-deep-research, agent-review-artifacts-2026-05-13, agentic-coding-trap-may-2026, ai-stack-fungibility-hashimoto-2026-05, shopify-claude-code-bessemer-2026-05, stanford-labor-june-2026, github-kyle-daigle-june-2026, ainews-june-05-2026, software-factories-fde-2026-07, dashbench-code-review-understanding-2026-07]
---

## Current guidance

Add / revise these bullets:

- Treat pull-request review as its own AI workflow: deterministic gates first, local standards in repo context, historical PR replay for evals, and human-facing review artifacts for comprehension. See [AI PR and code review](ai-pr-code-review.md).
- For complex PRs, ask the agent to generate an annotated explainer with the actual diff, architecture diagram, risk areas, and reviewer questions. The purpose is not only verification; it is preserving the reviewer's mental model for the next agent loop.

## Failure modes

Add:

- **Cognitive debt from agent-written code.** If engineers stop reading and understanding code because agents can self-check syntax and tests, they lose the system model needed to steer future work. Review should shift from "can I find every bug manually?" toward "do I understand the change well enough to direct the next loop?"

## Recent changes

- [2026-07-08] Added AI PR/code-review workflow as a first-class enablement concern: historical PR replay, local review standards, and understanding-preserving review artifacts.
- [2026-07-01] Added software-factory/FDE rollout pattern: enterprise agent adoption needs workflow integration capacity, not only developer tooling.

## See also

Add:

- [AI PR and code review](ai-pr-code-review.md) — dedicated workflow for AI-assisted pull request analysis, review execution, historical PR replay, and comprehension-preserving review artifacts

## Sources

Add:

- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
```

### wiki/concepts/agent-evals.md (updated sections)

```md
---
title: Agent evals
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-07-08
sources: [agents-evals-deep-research, cost-aware-agent-evaluation-2026-04-28, vending-bench-andon-june-2026, ainews-not-much-happened-2026-07-02, autoresearch-agent-recipes-2026-07, ai-code-review-eval-integrity-2026-06, dashbench-code-review-understanding-2026-07]
---

## Infrastructure layer (as of 2026-07-08)

Agent evaluation is splitting into several infrastructure problems:

- **Historical-work replay.** DashBench, from DoorDash, replays historical PRs to test whether AI reviewers catch real issues that mattered in production rather than writing plausible comments. This is stronger than synthetic review prompts because it anchors review quality to known defects and team-specific code context. See [AI PR and code review](../training/ai-pr-code-review.md).
- **Agent arenas** compare models or harnesses in agent mode, not only chat mode.
- **Systems efficiency metrics** such as AA-AgentPerf measure agents-per-megawatt, making inference and runtime efficiency part of agent evaluation.
- **World-model evals** such as WorldModelGym test whether a simulated world supports better decisions, not only plausible generations.
- **Incident reporting** efforts such as FLARE-AI aim to route AI flaws and safety incidents to the right developers and registries.

The pattern: evals are no longer only pass/fail task scores. They are becoming observability, incident intake, cost accounting, historical replay, and system-capacity infrastructure.

## Related

Add:

- [AI PR and code review](../training/ai-pr-code-review.md) — dedicated workflow for historical PR replay and understanding-preserving code review

## Recent changes

- [2026-07-08] DashBench adds a historical-PR replay pattern for AI code review evals: measure whether the reviewer catches real past issues, not whether it sounds useful.
- [2026-07-02] Added eval infrastructure layer: Agent Arena, AA-AgentPerf, WorldModelGym, and FLARE-AI show agent evaluation expanding into benchmarking, systems efficiency, world-model quality, and incident reporting.

## Sources

Add:

- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
```

### wiki/workflows/agentic-orchestration-patterns.md (updated sections)

```md
---
title: Agentic orchestration patterns
type: workflow
domains: [agents, coding]
subcategory: orchestration-pattern
tags: [agentic]
as_of: 2026-07-08
sources: [notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, harness-engineering-early-april, open-agent-orchestration-late-march, skills-and-plugin-packaging-late-march, harness-engineering-march, deep-agents-overview, goose-platform, googlecloudtech-adk-2-orchestration-patterns, agent-infrastructure-harness-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, production-agent-orchestration-2026-04-29, agent-html-artifacts-2026-05-13, gas-city-software-factory-2026-05, dynamic-workflows-claude-code, loopcraft-june-2026, aiewf-loops-debate-2026-07-03, shepherd-live-agent-rollback-2026-07-06, claude-code-getting-started-with-loops-2026-06-30, software-factories-fde-2026-07, ai-code-review-eval-integrity-2026-06, token-tightening-ai-finops-2026-06, what-the-hell-is-a-loop-anyway, dashbench-code-review-understanding-2026-07]
---

## Patterns

Revise / add:

- **Review artifacts over raw transcripts.** For complex agent work, ask for purpose-built review artifacts (HTML explainers, annotated diffs, comparison grids, one-off editors) when a human needs to inspect options, tune values, or export structured decisions back into the workflow. For pull requests, see [AI PR and code review](../training/ai-pr-code-review.md).
- **Review standards as repo context.** Put team-specific AI review criteria in Markdown near the code so code-review agents can apply local rules rather than generic style advice. This becomes more important as PR review becomes a distinct agent workflow with its own evals and replay datasets.

## Failure modes

Revise:

- Generic AI review on large PRs creates noise unless review standards, diff scope, trigger points, and reviewer-comprehension artifacts are controlled.

## Recent changes

- [2026-07-08] Linked PR review artifacts and repo-local review standards to the dedicated AI PR/code-review workflow.
- [2026-06-26] Added AI review standards and review-noise failure mode from code-review workflow coverage.

## Sources

Add:

- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
```

### wiki/index.md (updated section)

```md
## Training

Add:

- [training/ai-pr-code-review](training/ai-pr-code-review.md)
```

### wiki/sources/newsletters/dashbench-code-review-understanding-2026-07.md (new)

```md
---
title: DashBench and understanding-preserving AI code review
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-08-claude-cowork-now-runs-on-mobile.md
url: https://codenewsletter.ai/p/anthropic-extends-fable-5-access-doordash-drops-dashbench
published: 2026-07-08
ingested: 2026-07-08
domains: [coding, agents, training]
---

# DashBench and understanding-preserving AI code review

The Code reports that DoorDash released DashBench, a benchmark that replays historical PRs to evaluate AI code reviewers against real issues. The same issue summarizes Geoffrey Litt's argument that engineers should still understand agent-written code because understanding is what lets them participate in the next loop.

## Influenced pages

- [AI PR and code review](../../training/ai-pr-code-review.md) — creates a dedicated page for pull-request analysis, review execution, historical PR replay, review artifacts, and understanding-preserving review.
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — keeps broader eval-stack framing and links to the dedicated PR-review page.
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — adds PR review as a first-class enablement workflow.
- [Agent evals](../../concepts/agent-evals.md) — adds historical PR replay as an eval-infrastructure pattern.
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — links review artifacts and repo-local review standards to the dedicated workflow.

## Key claims extracted

- DashBench replays DoorDash historical PRs to test whether AI reviewers catch real issues.
- The Code reports a Kimi K2.6 + Claude Fable 5 combo beat DoorDash's production setup on weighted recall.
- Geoffrey Litt argues verification is not the only reason to read agent-written code; comprehension drives the next move.
- His `explain-diff` skill turns changes into teaching docs and quizzes.
- The practical workflow combines automated review execution with human understanding preservation.
```

## Schema / vocabulary additions

None.

## Open questions

- Should this page live under `training/` as an operational playbook, or under `workflows/` as a reusable PR-review workflow? I used `training/` because the page is primarily about how engineering teams should adopt and govern AI PR review.
	- Under workflows.
- Should `ai-pr-code-review.md` also absorb the older `AI code review` section from `evals-for-agentic-software-development.md` when the proposal is applied? This draft assumes yes: the evals page keeps only a short pointer.
	- yes, it should.
