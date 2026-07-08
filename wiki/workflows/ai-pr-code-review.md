---
title: AI PR and code review
type: workflow
domains: [coding, agents]
subcategory: agentic-orchestration-patterns
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

1. **Surface logic review** - summarize the diff, identify changed behavior, and map the change to the stated task.
2. **Deterministic checks** - run the repo's existing tests and static checks before asking a model for qualitative judgment.
3. **Scope and blast-radius checks** - verify the PR did not touch unrelated modules, configuration, schemas, credentials, generated files, or deployment paths.
4. **Deep code review** - use a capable model with the repo's local review standards to inspect architecture, security, edge cases, migrations, and test adequacy.
5. **Human comprehension artifact** - generate an annotated explainer or teaching document so the reviewer understands the change well enough to approve, redirect, or start the next agent loop.
6. **Eval capture** - record accepted comments, rejected comments, missed issues, and post-merge failures as future review eval data.

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

- [Evals for agentic software development](../training/evals-for-agentic-software-development.md) - broader eval stack for coding agents
- [AI enablement - software development](../training/ai-enablement-software-development.md) - broader engineering adoption and supervision guidance
- [Agent evals](../concepts/agent-evals.md) - why historical replay and trajectory analysis matter
- [Agentic orchestration patterns](agentic-orchestration-patterns.md) - where review artifacts fit in agent loops

## Recent changes

- [2026-07-08] Created dedicated AI PR/code-review workflow from DashBench and understanding-preserving review coverage.

## Sources

- [AI code review and benchmark integrity](../sources/newsletters/ai-code-review-eval-integrity-2026-06.md)
- [Purpose-built review artifacts for agent work](../sources/tweets/agent-review-artifacts-2026-05-13.md)
- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
