---
title: Claude Ship
type: tool
domains: [coding, agents]
subcategory: ai-code-review
tags: [anthropic, agentic]
as_of: 2026-11-23
sources: [claude-ship-launch-2026-11-23]
---

# Claude Ship

Anthropic's product for everything after a pull request is opened: it reviews the PR, fixes it, and decides whether it is ready to merge under a policy the team sets. Launched in beta on 2026-11-23, aimed at teams whose code is increasingly written by agents.

## Current status (as of 2026-11-23)

- Three parts: **Code Review** (described as generally available), plus two beta agents, **PR Steward** and **Claude Approvals**.
- **Code Review** reviews a PR against the codebase from several angles, adversarially verifies and categorizes findings, and posts them; Quick, Standard, or Deep level per repository.
- **PR Steward** works on failing CI checks, merge conflicts, and review feedback from Code Review, other tools, or people; comments after each push with what changed and how to undo it; steered with `@claude`, paused with `@claude stop`. Designed never to approve or merge.
- **Claude Approvals** applies an approval policy written as a file in the repository ("a smarter CODEOWNERS"): approves routine changes alone where the policy allows, requires human sign-off elsewhere, and can weigh Code Review findings and team-written plain-language classifiers. Starts when a connected repository has a policy file on its default branch.
- Two entry points: `/ship` in [Claude Code](claude-code.md) for a developer's own PRs, or per-repository enablement by an admin (review level, when reviews run, monthly spend limit). Works with existing branch protection and required checks.
- Eligible Claude Enterprise organizations can claim at least $10,000 in credits, usable for 30 days after claiming, by 2027-01-15.

## Evidence from practice

On Anthropic's Claude Code team, where Claude's review is one layer of a broader process, merged PRs more than doubled from June to September 2026 while the share reverted fell by more than 40%. A product manager there can turn customer feedback into a PR through [Claude Tag](claude-tag.md) and leave Claude Ship to take it through review, fixes, and approval; one documentation fix merged the same evening.

## Weaknesses / caveats

- PR Steward and Claude Approvals are beta; Anthropic notes Claude Ship may miss bugs, security vulnerabilities, or other issues.
- Anthropic recommends running Claude Approvals in observe-only mode before making it a required branch-protection check.
- What `/ship` can merge depends on the developer's permissions and the repository's branch rules.
- The launch post does not say how Code Review relates to Claude Code's `/code-review` command or `/ultrareview`.

## Related

- [AI PR and code review](../workflows/ai-pr-code-review.md) - the vendor-neutral workflow this product packages
- [Claude Code practices](../workflows/claude-code-practices.md) - `/ultrareview`, Claude Code's cloud multi-agent review mode

## Recent changes

- [2026-11-23] Launched in beta: Code Review (GA) plus PR Steward and Claude Approvals; `/ship` in Claude Code; per-repository admin enablement; Enterprise launch credits.

## Sources

- [Introducing Claude Ship](../sources/articles/claude-ship-launch-2026-11-23.md)
