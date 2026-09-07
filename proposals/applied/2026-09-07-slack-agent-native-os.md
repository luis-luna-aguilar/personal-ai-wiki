---
type: proposal
source: raw/newsletters/2026-07-29-what-if-slack-was-your-ai-command-center.md
status: pending
created: 2026-09-07
---

# Proposal: Slack becomes an agent-native operating system

## Summary

### The source

Every's July 29 issue of *Context Window* profiles a concrete pattern that two unrelated teams converged on the same week: turning a group-chat app into the control surface for a fleet of coding agents. Every's senior applied AI engineer, Nityesh Agarwal, built a personal Slack bot named "Luo Ji," wired to Claude Code running on a spare MacBook Air. He rewired Slack's own structure onto agent session lifecycle: every top-level message in a channel starts a brand-new Claude Code session, and every reply in the resulting thread resumes that same session — so a project channel becomes a live dashboard of tasks, with each thread holding one task's full history instead of it scattering across tabs or getting buried in a long agent transcript. Screenshots posted back into the thread double as lightweight review artifacts. He also routes models per channel: most channels default to Opus, but a dedicated channel is reserved for Fable, which he judged too expensive and powerful for routine work — that channel's CLAUDE.md carries standing instructions for Fable to hand execution off to cheaper Opus subagents between planning and review. He open-sourced the whole setup as "Claude Home Base," a starter kit for anyone who wants to build the same thing. Separately and independently, financial-services company Block (led by Jack Dorsey) shipped Buzz on July 21 — an open-source "shared workspace where humans and AI agents work together," which one early tester bluntly described as "a Slack clone with a different color." An early test had Buzz agents kicking off Codex tasks with self-written prompts and posting results back into a shared thread with three tagged agents. Every frames the throughline plainly: keeping tabs on parallel agent work is becoming a job of its own, and chat threads are turning out to be a natural home for it.

### What changes

The wiki did not previously capture the specific mechanic of mapping agent-session lifecycle onto chat threads, though `training/company-wide-ai-enablement.md` already notes messaging-native personal agents as a general adoption pattern.

- **Company-wide AI enablement** gains a new Proven-patterns entry, "Thread-per-task chat orchestration," describing the top-level-message-starts-a-session / thread-reply-resumes-it mechanic and per-channel model routing, backed by two independent implementations (Every's Claude Home Base, Block's Buzz) landing in the same week. One line is also added to Evidence from practice describing Nityesh's fully-in-Slack personal dev loop. A Recent-changes entry records the addition; page date moves to 29 July.
- New source page for the Every newsletter issue.

### What to weigh

Sourcing here is a single secondary newsletter recap — Block's own Buzz launch post and the Claude Home Base repo weren't independently fetched, so specifics about Buzz's actual feature set beyond "Slack-shaped, humans + agents" rest on Every's characterization. The "Destructive Command Guard" tool mentioned in the same issue (a safeguard against GPT-5.6 Sol's file-deletion habit) is left out of this proposal as a separate, unrelated tidbit with too little detail in the free preview to write up responsibly.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/company-wide-ai-enablement.md` — add "Thread-per-task chat orchestration" to Proven patterns, one line to Evidence from practice, new Recent-changes entry, `as_of`/sources bump
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/slack-agent-native-os-2026-07-29.md` — source summary

## Page drafts

### wiki/training/company-wide-ai-enablement.md (updated)

Frontmatter: bump `as_of: 2026-07-08` → `as_of: 2026-07-29`; append `slack-agent-native-os-2026-07-29` to the `sources:` list.

Insert this new bullet into `## Proven patterns`, immediately after the existing "**Messaging-native personal agents.**" bullet:

```md
- **Thread-per-task chat orchestration.** A concrete implementation pattern for messaging-native agents: map the chat app's own structure onto agent session lifecycle — each top-level channel message starts a new agent session, and each thread reply resumes that same session, so chat history stays attached to the task instead of scattering across tabs or getting buried in a long transcript. Per-channel model routing lets teams send routine work to a cheaper default model and reserve an expensive frontier model for a dedicated channel, with standing instructions (e.g. in CLAUDE.md) for that model to delegate execution to cheaper subagents. Two independent implementations converged on the same shape within the same week in July 2026: Every's open-sourced "Claude Home Base" starter kit (Slack + Claude Code) and Block's Buzz, a general-purpose shared workspace for humans and agents that one early tester called "a Slack clone with a different color."
```

Append this line to the end of `## Evidence from practice`:

```md
- Every's Nityesh Agarwal reports his entire personal development loop now runs inside Slack via "Luo Ji": task assignment, code review via posted screenshots, and revision requests all happen in-thread; only pull-request review happens outside Slack, on GitHub. (July 2026)
```

Add this entry to `## Recent changes` (newest-first; page currently has 6 entries, under the cap of 10 — no spill needed):

```md
- [2026-07-29] Added thread-per-task chat orchestration pattern: chat channels/threads mapped directly onto agent session lifecycle; two independent implementations (Every's Claude Home Base, Block's Buzz) converged on the same shape in the same week.
```

### wiki/sources/newsletters/slack-agent-native-os-2026-07-29.md (new)

```md
---
title: "What If Slack Was Your AI Command Center"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-29-what-if-slack-was-your-ai-command-center.md
url: https://every.to/context-window/what-if-slack-was-your-ai-command-center
published: 2026-07-29
ingested: 2026-09-07
domains: [agents, training]
---

# What If Slack Was Your AI Command Center

Every profiles Nityesh Agarwal's "Luo Ji," a personal Slack bot wired to Claude Code that maps top-level channel messages to new agent sessions and thread replies to resumed sessions, turning Slack into a project dashboard with per-channel model routing; he open-sourced the pattern as "Claude Home Base." The same issue notes Block shipped Buzz, an independently-built open-source shared workspace for humans and AI agents with a similar channel/thread shape.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — new "thread-per-task chat orchestration" proven pattern, plus an evidence-from-practice line

## Key claims extracted

- Nityesh Agarwal (Every) built "Luo Ji," a Slack bot connected to Claude Code; top-level channel messages start new Claude Code sessions, thread replies resume the same session
- Per-channel model routing: most channels default to Opus; a dedicated channel is reserved for Fable, with CLAUDE.md instructions to delegate execution to Opus subagents
- Open-sourced the pattern as "Claude Home Base" (github.com/nityeshaga/claude-home-base)
- Block (Jack Dorsey) released Buzz on 2026-07-21: an open-source "shared workspace where humans and AI agents work together"; described by an early tester as "a Slack clone with a different color"
- Early Buzz test: agents started Codex tasks with self-written prompts and posted results into a shared thread
```

## Schema / vocabulary additions

None.

## Open questions

- None beyond the sourcing caveat noted above.
