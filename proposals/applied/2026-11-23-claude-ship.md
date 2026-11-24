---
type: proposal
source: raw/articles/2026-11-23-claudecom-resources-articles-introducing-claude-ship.md
status: pending
created: 2026-11-23
---

# Proposal: Anthropic launches Claude Ship

## Summary

### In short

Anthropic now sells the whole path after a pull request, not just the review: Claude Ship reviews a PR, fixes it, and decides whether it can merge under a policy file the team keeps in the repository. It bundles the generally available Code Review with two beta agents, PR Steward and Claude Approvals, and adds a `/ship` command to Claude Code. The proposal creates a Claude Ship tool page, opens an "AI code review" section on State of Coding, and updates Claude Code and the AI PR review workflow. Reason to hesitate: it needs a new `ai-code-review` subcategory.

[[#Open questions|Open questions: 2 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

On 23 November 2026 Anthropic announced Claude Ship in beta. The pitch starts from a familiar annoyance: a developer opens a pull request, moves on, and is pulled back each time a review comes in, a check fails, or an approver has to be found. Anthropic says most code on its Claude Code team is now written by Claude, and it wanted everything after the PR to move as fast as the writing.

Claude Ship has three parts. Code Review, which the post describes as already generally available, reviews a PR against the codebase from several angles, checks its own findings adversarially, and posts them, at a Quick, Standard, or Deep level chosen per repository. PR Steward keeps the PR green: it acts on failing CI checks, merge conflicts, and review comments from people or other tools, says after each push what it changed and how to undo it, and takes `@claude` instructions or `@claude stop`. It is built never to approve or merge. Claude Approvals then applies an approval policy the team writes as a file in the repository, "a smarter CODEOWNERS": it can approve routine changes alone or require human sign-off, weighing Code Review findings and the team's own plain-language classifiers. Anthropic recommends running it in observe-only mode before making it a required branch-protection check.

Developers can call it with `/ship` in Claude Code, which pushes the change, opens the PR, reviews it, and works the feedback. Admins can instead turn it on per repository, with review level, timing, and a monthly spend limit, alongside existing branch protection. On the Claude Code team, where Claude's review is one layer among several, merged PRs more than doubled from June to September while the share reverted fell by over 40%.

### What changes

The wiki covers AI code review as a workflow and Claude Code's own `/code-review` and `/ultrareview` commands, but has no page or State of Coding section for review products.

- New page `tools/claude-ship.md` describing the three agents, the two ways to start, and the caveats.
- **State of Coding** gains an "AI code review" section with Claude Ship as its first entry and a Recent-changes entry; the oldest entry (Sonnet 5 launch, 30 June) moves to history. Page date moves to 23 November.
- **Claude Code** gains a short `/ship` section and a Recent-changes entry; the oldest entry (`/design-sync`, 8 July) moves to history. Page date moves to 23 November.
- **AI PR and code review** gains guidance on keeping the approval policy as a repo file run in observe-only mode first, and on keeping the fixer agent separate from the approver, plus the Claude Code team's merge and revert numbers. Page date moves to 23 November.
- Index gets the new page (count 289 → 290) and refreshed lines; one new source page.

### What to weigh

The fetched page stops at an empty "What customers are saying" heading, so any customer quotes after it were not read. The post does not say how the Code Review product relates to Claude Code's existing `/code-review` command or `/ultrareview`, so the drafts keep them apart rather than merge them. The new subcategory is the main schema call; the alternative is filing Claude Ship under `agentic-devops`, whose definition is about infrastructure.

## Intended changes

- [ ] **Create** `wiki/tools/claude-ship.md` — new tool page, subcategory `ai-code-review`
- [ ] **Update** `wiki/state-of/coding.md` — new `### AI code review` section after `### AI end-to-end testing`; adds one Recent-changes entry dated 2026-11-23 at the top (list at cap 10, so the oldest entry spills); append 1 source id; `as_of` 2026-10-19 → 2026-11-23
- [ ] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — oldest Recent-changes entry ([2026-06-30] Official Sonnet 5 launch) appended to the existing "Archived from current page on 2026-11-23" block
- [ ] **Update** `wiki/tools/claude-code.md` — new `## Claude Ship (/ship)` section after `## /ultrareview`; adds one Recent-changes entry dated 2026-11-23 at the top (list at cap 10, so the oldest entry spills); append 1 source id and 1 link; `as_of` 2026-10-26 → 2026-11-23
- [ ] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — oldest Recent-changes entry ([2026-07-08] `/design-sync`) appended to the existing "Archived from current page on 2026-11-23" block
- [ ] **Update** `wiki/workflows/ai-pr-code-review.md` — one Current-guidance bullet, one Evidence-from-practice bullet, one Related line; adds one Recent-changes entry dated 2026-11-23 at the top (6 of 10, no spill); append 1 source id and 1 link; `as_of` 2026-10-25 → 2026-11-23
- [ ] **Update** `wiki/index.md` — add `tools/claude-ship`, refresh the `tools/claude-code` and `workflows/ai-pr-code-review` lines, total 289 → 290
- [ ] **Create** `wiki/sources/articles/claude-ship-launch-2026-11-23.md` — source summary

## Page drafts

### wiki/tools/claude-ship.md (new)

```
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
```

### wiki/state-of/coding.md (updated)

Frontmatter changes:

```
as_of: 2026-11-23
sources: [...existing..., claude-ship-launch-2026-11-23]
```

New section inserted directly after the `### AI end-to-end testing` section, before `## Recent changes`:

```
### AI code review

Tools that review pull requests, fix failing checks and review feedback, or decide what can merge under a policy the team sets.

- [Claude Ship](../tools/claude-ship.md) — Anthropic; Code Review plus beta fixer (PR Steward) and policy-file approver (Claude Approvals) agents; `/ship` in Claude Code or per-repository admin enablement *(as of 2026-11-23)*
```

Recent changes — one entry inserted at the top, above the first 2026-10-19 entry; the oldest entry ([2026-06-30] Official Sonnet 5 launch) is removed and spilled:

```
- [2026-11-23] New "AI code review" section (new `ai-code-review` subcategory) with Claude Ship: Anthropic's review, fix, and policy-based approval agents for pull requests, in beta.
```

### wiki/history/state-of/coding.md (updated)

Appended to the end of the existing `## Archived from current page on 2026-11-23` block:

```
- [2026-06-30] Official Sonnet 5 launch confirms Claude Code availability and `claude-sonnet-5` API access.
```

### wiki/tools/claude-code.md (updated)

Frontmatter changes:

```
as_of: 2026-11-23
sources: [...existing..., claude-ship-launch-2026-11-23]
```

New section inserted directly after the `## /ultrareview` section:

```
## Claude Ship (/ship)

`/ship` (beta, 2026-11-23) hands a finished change to [Claude Ship](claude-ship.md): Claude pushes it, opens the PR, reviews it, and works on feedback and failing checks until it is ready to merge, within the developer's permissions and the repository's branch rules.
```

Recent changes — one entry inserted at the top, above the 2026-10-26 entry; the oldest entry ([2026-07-08] `/design-sync`) is removed and spilled:

```
- [2026-11-23] `/ship` command added (beta): pushes the change, opens the PR, and hands it to [Claude Ship](claude-ship.md) for review, fixes, and an approval decision.
```

Sources — one link appended:

```
- [Introducing Claude Ship](../sources/articles/claude-ship-launch-2026-11-23.md)
```

### wiki/history/tools/claude-code.md (updated)

Appended to the end of the existing `## Archived from current page on 2026-11-23` block:

```
- [2026-07-08] Claude Code and Claude Design add bidirectional `/design-sync` between repo work and Claude Design canvases.
```

### wiki/workflows/ai-pr-code-review.md (updated)

Frontmatter changes:

```
as_of: 2026-11-23
sources: [...existing..., claude-ship-launch-2026-11-23]
```

`## Current guidance` — one bullet inserted directly after the "Review from a session that never saw the implementer's transcript" bullet:

```
- **Separate the fixer from the approver, and write the approval rule down.** Anthropic's Claude Ship (November 2026) splits the post-PR loop into a reviewer, a fixer that works failing checks, conflicts, and review comments but never approves or merges, and an approver that applies a policy file kept in the repository: routine changes can pass alone, named scenarios need a person, and the policy can weigh review findings and team-written plain-language classifiers. Run the approval policy in observe-only mode until its calls match the team's, then make it a required branch-protection check.
```

`## Evidence from practice` — one bullet appended at the end of the list:

```
- On Anthropic's Claude Code team, where Claude's review is one layer of a broader process, merged PRs more than doubled from June to September 2026 while the share of PRs reverted fell by more than 40% ([Claude Ship](../tools/claude-ship.md)).
```

`## Related` — one line appended:

```
- [Claude Ship](../tools/claude-ship.md) - Anthropic's productized review, fix, and policy-based approval loop for pull requests
```

Recent changes — one entry inserted at the top, above the 2026-10-25 entry:

```
- [2026-11-23] Added fixer/approver separation with a repo-file approval policy run observe-only first, and the Claude Code team's merge and revert numbers, from Anthropic's Claude Ship launch.
```

Sources — one link appended:

```
- [Introducing Claude Ship](../sources/articles/claude-ship-launch-2026-11-23.md)
```

### wiki/index.md (updated)

New line inserted directly after the `tools/claude-tag` line:

```
- [tools/claude-ship](tools/claude-ship.md) — Anthropic's post-PR agents (beta): Code Review, PR Steward fixes failing checks and feedback without approving, Claude Approvals applies a repo policy file; `/ship` in Claude Code or per-repository admin enablement *(as_of: 2026-11-23)*
```

Two lines replaced in place:

```
- [tools/claude-code](tools/claude-code.md) — Anthropic's terminal-first AI coding agent; /goal, Agent View, dynamic workflows, cloud sessions (GA), Projects, Claude Mods harness customization (function hooks early access from 2.1.274), Claude Security plugin, `/ship` hand-off to Claude Ship; practices and /ultrareview split to workflows/claude-code-practices *(as_of: 2026-11-23)*
```

```
- [workflows/ai-pr-code-review](workflows/ai-pr-code-review.md) — workflow for AI-assisted pull request analysis, code-review execution, review by blast radius, fixer/approver separation with repo approval policies, judge calibration, historical PR replay, and understanding-preserving review artifacts *(as_of: 2026-11-23)*
```

Total line:

```
**Total content pages: 290.**
```

### wiki/sources/articles/claude-ship-launch-2026-11-23.md (new)

```
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
```

## Schema / vocabulary additions

- [ ] Add new subcategory `ai-code-review` to `wiki/_schema/subcategories.md`:

```
### ai-code-review
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** Tools that review pull requests, fix failing checks and review feedback, or decide what can merge under a team-set policy; distinct from `agentic-devops` (infrastructure provisioning, operation, and post-deploy verification) and `ai-e2e-testing` (agent-driven application tests).
- **Examples:** [Claude Ship](../tools/claude-ship.md)
```

## Open questions

- Is a new `ai-code-review` subcategory right, or should Claude Ship go under `agentic-devops` (or `agent-orchestration`) and sit in an existing State of Coding section?
	- Yes, new sub-category, and check if we need to move other stuff
- Should Claude Ship have its own page (drafted), or live as a section on the Claude Code page the way Claude Security does? It runs repo-wide for admins without anyone opening Claude Code, which is why the draft gives it a page.
	- Separate it
