---
title: Introducing Claude Ship
type: source
source_type: article
source_file: raw/articles/2026-11-23-claudecom-resources-articles-introducing-claude-ship.md
url: https://claude.com/resources/articles/introducing-claude-ship
published: 2026-11-23
ingested: 2026-11-23
domains: [coding, agents]
---

# Introducing Claude Ship

Anthropic's launch post for Claude Ship (beta), which takes a pull request through review, fixes, and an approval decision under a team-set policy. It combines Code Review (described as generally available) with two new beta agents: PR Steward, which keeps a PR green without approving or merging, and Claude Approvals, which applies a policy file kept in the repository. Developers start it with `/ship` in Claude Code; admins can enable it per repository. The fetched page ends at an empty "What customers are saying" heading.

## Influenced pages
- [Claude Ship](../../tools/claude-ship.md) — new tool page
- [State of Coding](../../state-of/coding.md) — new "AI code review" section
- [Claude Code](../../tools/claude-code.md) — `/ship` command
- [AI PR and code review](../../workflows/ai-pr-code-review.md) — fixer/approver separation, repo approval policy, Claude Code team numbers

## Key claims extracted
- Claude Ship available in beta on 2026-11-23; reviews PRs, fixes them, and decides what is ready to merge based on per-team policies.
- Code Review: multi-lens review against the codebase; findings collected, adversarially verified, categorized, and posted; Quick, Standard, or Deep per repository.
- PR Steward: acts on failing CI, merge conflicts, and review feedback from Code Review, other tools, or team members; comments after each push with what changed and how to undo it; `@claude` to steer, `@claude stop` to step back; designed not to approve or merge.
- Claude Approvals: applies an approval policy written as a repository file; can approve routine changes or require human sign-off; can weigh Code Review findings or team classifiers written in natural language; "like a smarter CODEOWNERS"; observe-only mode recommended first. Starts when a connected repository has a policy file on its default branch; admins can turn it off.
- `/ship` in Claude Code pushes the change, opens the PR, reviews it, and works on feedback and failing checks; what can merge depends on the developer's permissions and branch rules.
- Admins enable Code Review and PR Steward per repository and set review level, timing, and spend limits; works with existing branch protection and required checks.
- Claude Code team: Claude writes most of the code; merged PRs more than doubled June to September while the share reverted fell by more than 40% (Claude review being one layer of a broader process).
- Example: a PM used Claude Tag to open a docs fix from customer feedback about the Analytics API; Code Review found nothing blocking, a docs reviewer signed off, Claude Approvals passed, and it merged the same evening.
- Eligible Claude Enterprise organizations can claim at least $10,000 in Claude Ship credits, usable within 30 days of claiming; claim by 2027-01-15.
