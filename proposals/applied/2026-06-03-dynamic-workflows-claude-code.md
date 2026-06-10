---
type: proposal
source: raw/articles/2026-06-03-claudecom-blog-introducing-dynamic-workflows-in-claude-code.md
status: pending
created: 2026-06-03
---

# Proposal: Dynamic workflows in Claude Code

## Summary
Anthropic introduces **dynamic workflows** in Claude Code (research preview, announced 2026-05-28): Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, verifies findings before they reach the user, and iterates with adversarial agents until answers converge. Built for long-running (hours-to-days) work — codebase-wide bug hunts, security/optimization audits, large migrations, and double-checked critical work. Enabled via the `ultracode` effort setting (sets effort to xhigh; Claude auto-decides when to spawn a workflow); uses substantially more tokens than a normal session.

## Notes / judgment
- Substantive new Claude Code feature → main update is `tools/claude-code.md`.
- It instantiates several existing patterns on `workflows/agentic-orchestration-patterns.md` (plan→fan-out→verify→converge, evaluator separation, durable/resumable execution, coordinator-specialist), so I propose a short sourced pointer there rather than a new pattern. See open question.
- **`as_of` is 2026-05-28**, the article's stated publish date (Date: May 28, 2026), per the source-date-beats-ingest-date rule.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add a `## Dynamic workflows` section, a recent-change entry, update `as_of` to 2026-05-28, add source ID. (Spills oldest recent-change entry — see below.)
    > See draft below.

- [x] **Update** `wiki/state-of/coding.md` — extend the Claude Code leader line and add a recent-change entry; update `as_of` to 2026-05-28 and add source ID.
    > **Before (leader line):** `- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: `/goal` autonomous loops, Opus 4.7 fast mode, and Agent View (`claude agents`) multi-session supervision with `/bg` and `claude --bg` *(as of 2026-05-13)*`
    > **After (leader line):** `- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: `/goal` autonomous loops, Agent View multi-session supervision, and now dynamic workflows (`ultracode`) — tens-to-hundreds of parallel subagents that plan, verify, and iterate to convergence on hours-to-days work *(as of 2026-05-28)*`
    > **Add to `## Recent changes` (top):**
    > `- [2026-05-28] Claude Code adds dynamic workflows (research preview): the `ultracode` effort setting lets Claude write orchestration scripts that fan tens-to-hundreds of parallel subagents, verify findings (with adversarial agents) before folding them in, and iterate to convergence; runs checkpoint and resume across hours-to-days. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens. Bun's Zig→Rust port (~750K LOC Rust, 99.8% tests passing, 11 days) is the flagship case.`

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add one sourced bullet under `## Where these patterns surfaced` and add the source ID; update `as_of` to 2026-05-28.
    > **Add to `## Where these patterns surfaced`:**
    > `- Anthropic's dynamic workflows (Claude Code, research preview) productize the plan→fan-out→verify→converge loop: Claude writes orchestration scripts running tens-to-hundreds of parallel subagents, with adversarial agents trying to break each finding before it surfaces, durable checkpoint/resume, and coordination held outside the conversation so the plan survives as the task grows. The Bun Zig→Rust rewrite is the cited large-scale example.`

- [x] **Create** `wiki/sources/articles/dynamic-workflows-claude-code.md` — source summary.
    > See draft below.

- [x] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — oldest recent-change entry (`[2026-05-13] Agent View added…`) falls off to keep the cap at 5.

## Page drafts

### wiki/tools/claude-code.md (new section + recent-change + frontmatter)

Add `dynamic-workflows-claude-code` to the `sources:` list and set `as_of: 2026-05-28`.

Insert this section after `## Routines`:

````md
## Dynamic workflows

Dynamic workflows (research preview, announced 2026-05-28) let Claude **dynamically write orchestration scripts** that run tens to hundreds of parallel subagents in a single session. Claude plans the task, breaks it into subtasks, fans them out, and verifies each result before folding it back in — agents attack the problem from independent angles while other agents try to refute their findings, and the run iterates until the answers converge, reaching results a single pass cannot.

- **Built for long-running, parallel work** — runs extend into hours or days, doing complex engineering work that previously took weeks.
- **Durable by default** — progress is checkpointed as the run proceeds, so an interrupted job resumes where it left off; coordination lives outside the conversation, so the plan stays on track as the task grows.
- **Typical use cases** — codebase-wide bug hunts, profiler-guided optimization audits, security/hardening passes, large migrations and language ports across thousands of files, and high-stakes work you want independently double-checked.
- **How to run** — turn on auto mode, then either ask Claude to "create a workflow" or enable the `ultracode` setting from the effort menu (sets effort to xhigh and lets Claude decide when a workflow is warranted).
- **Higher cost** — consumes substantially more tokens than a typical session; the first time a workflow triggers, Claude Code shows what is about to run and asks for confirmation. Org admins can disable workflows via managed settings.
- **Availability** — research preview in the Claude Code CLI, Desktop, and VS Code extension, and on the Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry. On by default for Max and Team (and the API); off by default for Enterprise at launch (admin can enable in settings).

**Flagship example — Bun rewrite:** Jarred Sumner used dynamic workflows to port Bun from Zig to Rust — ~750,000 lines of Rust, 99.8% of the existing test suite passing, eleven days from first commit to merge. One workflow mapped the correct Rust lifetime for every struct field; the next wrote each `.rs` file as a behavior-identical port of its `.zig` counterpart (hundreds of agents in parallel, two reviewers per file); a fix loop drove the build and test suite until clean; an overnight workflow removed unnecessary data copies and opened a PR per fix for review. (Not yet in production.)
````

Add to top of `## Recent changes` (and spill the oldest entry to history):

```
- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify (with adversarial agents), and iterate to convergence on hours-to-days work; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens.
```

### wiki/sources/articles/dynamic-workflows-claude-code.md (new)

````md
---
title: Introducing dynamic workflows in Claude Code
type: source
source_type: article
source_file: raw/articles/2026-06-03-claudecom-blog-introducing-dynamic-workflows-in-claude-code.md
url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
published: 2026-05-28
ingested: 2026-06-03
domains: [coding, agents]
---

# Introducing dynamic workflows in Claude Code

Anthropic announces dynamic workflows in Claude Code (research preview): Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, plans and splits the task, verifies each result (with adversarial agents trying to refute findings) before folding it in, and iterates until answers converge. Targets long-running parallel engineering work (hours to days) — bug hunts, audits, large migrations, double-checked critical work — and checkpoints progress so interrupted runs resume.

## Influenced pages
- [Claude Code](../../tools/claude-code.md) — new `## Dynamic workflows` section, recent-change entry
- [State of Coding](../../state-of/coding.md) — extended Claude Code leader line, recent-change entry
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — added to "Where these patterns surfaced"

## Key claims extracted
- Dynamic workflows: Claude dynamically writes orchestration scripts running tens-to-hundreds of parallel subagents in a single session → plan → split → parallel fan-out → verify before merge → iterate to convergence.
- Adversarial verification: independent agents attempt the problem from different angles; other agents try to break each finding before it reaches the user.
- Built for parallel/long-running work spanning hours to days; checkpoints progress and resumes interrupted runs; coordination happens outside the conversation.
- Enabled via `ultracode` (effort menu; sets effort to xhigh; Claude auto-decides when to spawn a workflow). Auto mode recommended. Alternatively ask Claude to "create a workflow."
- Consumes substantially more tokens than a typical session; first run prompts for confirmation; org admins can disable via managed settings.
- Availability (research preview): Claude Code CLI, Desktop, VS Code extension; Claude API; Amazon Bedrock; Vertex AI; Microsoft Foundry. On by default for Max/Team/API; off by default (admin-enabled) for Enterprise.
- Use cases cited: codebase-wide bug hunts, profiler-guided optimization audits, security/hardening passes (auth, input validation, unsafe patterns), large migrations and language ports across thousands of files, high-stakes double-checked work.
- Flagship case: Bun ported Zig→Rust with dynamic workflows — ~750,000 lines of Rust, 99.8% test suite passing, 11 days first commit to merge; lifetime-mapping workflow, behavior-identical per-file port (hundreds of parallel agents + 2 reviewers/file), build/test fix loop, overnight data-copy cleanup opening one PR per fix. Not yet in production.
- Published 2026-05-28.
````

## Open questions
- For `workflows/agentic-orchestration-patterns.md`, I added a "where these surfaced" pointer rather than a new pattern bullet, since plan→fan-out→verify→converge, evaluator separation, and durable execution already exist there. Want a distinct **"Dynamic workflow orchestration"** pattern bullet too, or is the pointer enough?
	- The pointer is enough

