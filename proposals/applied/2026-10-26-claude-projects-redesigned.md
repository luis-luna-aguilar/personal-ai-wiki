---
type: proposal
source: raw/articles/2026-10-26-claudecom-blog-projects-redesigned.md
sources:
  - raw/articles/2026-10-26-claudecom-blog-projects-redesigned.md
  - raw/tweets/2026-10-26-claudeai-2100632677904744716.md
  - raw/tweets/2026-10-26-emollick-2100665801800093959.md
status: pending
created: 2026-10-26
---

# Proposal: Claude Code Projects redesigned (coordinator plus parallel threads)

## Summary

### In short

Claude Code Projects makes one chat the manager of a team of agents. You brief a coordinator like a chief of staff, and it opens parallel threads. Each thread is a full cloud session on its own branch, and all of them share one project memory. Ethan Mollick's early run used 18 threads, with nested agents and skeptic fact-checkers, over one day. The proposal fills in the Projects bullet on Claude Code, adds a worked example to Multi-agent coordination, and adds three source pages. Reason to hesitate: the wiki already covers Projects from a later interview, so what this adds is mechanics, not news.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

On 17 September Anthropic turned Projects from folders of files into a conversation that runs other conversations. You pick a goal and connect a repo or documents. A coordinator chat scopes the request, routes work to new or existing threads, reviews the results and assembles them. One example retires a v1 endpoint across three repos, with one thread per repo. Each thread is a Claude Code cloud session on its own branch, so two threads touching the same code produce an ordinary merge conflict. Threads share a project memory ("the release moved to Friday") and a library of files and artifacts. The coordinator and the workers can run different models and effort levels, and Anthropic warns that projects use up limits faster. At launch, threads ran only in the cloud. The beta went to selected Pro and Max users, with a waitlist and other plans to follow.

The same day, Wharton's Ethan Mollick described an early-access run. The orchestrator chose 18 historical mysteries and gave each one a thread. Those threads launched more agents, for avalanche simulation or code-breaking, and then write-up agents and skeptical fact-checkers. The run took about a day and mixed expensive and cheap models. Tokens were unmetered, so the cost is unknown, and he calls the results reasonable but not definitive.

### What changes

The wiki already describes Projects, from a 29 September interview and a 23 September note, as a single-player supervising agent that also runs locally. This proposal adds the launch mechanics without going back on the later local-run claim.

- **Claude Code** gets a rewritten Projects bullet covering how threads work, the rollout, and the fact that threads were cloud-only at launch. It also gets a Recent-changes entry dated 17 September, and the 30 June Sonnet 5 entry moves to history to keep the list at its cap. The page date stays 29 September.
- **Multi-agent coordination** gains a "Where these patterns surfaced" bullet that reads Projects as coordinator-specialist routing in a shipped product, with Mollick's run as the example. The page date stays 6 October.
- Three new source pages: the blog post and the two threads.

### What to weigh

The blog post has no date of its own. It says "starting today", and Anthropic's same-day thread is dated 17 September, so that date is used throughout. Projects is single-player, with one user and many agents, so the proposal leaves Multiplayer AI alone. The shared memory sits closer to Agent memory, which also stays untouched for now (see Open questions).

## Intended changes

- [ ] **Update** `wiki/tools/claude-code.md` — replace the Projects bullet in "Mods, Projects, and cloud sessions"; add one Recent-changes entry dated 2026-09-17 (it slots between the 2026-09-23 and 2026-08-08 entries); append three source ids to frontmatter `sources:` and three links to `## Sources`; `as_of` stays 2026-09-29
    > See draft below

- [ ] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — the list is at its cap of 10, so the oldest entry (2026-06-30, Sonnet 5 in Claude Code) moves to history
    > See draft below

- [ ] **Update** `wiki/workflows/multi-agent-coordination.md` — add one bullet to "Where these patterns surfaced"; add one Recent-changes entry dated 2026-09-17 (it slots between 2026-10-06 and 2026-09-09); append two source ids and two Sources links; `as_of` stays 2026-10-06
    > See draft below

- [ ] **Create** `wiki/sources/articles/claude-projects-redesigned-2026-09-17.md` — source summary for the blog post

- [ ] **Create** `wiki/sources/tweets/claudeai-projects-one-conversation-2026-09-17.md` — source summary for the @claudeai launch thread

- [ ] **Create** `wiki/sources/tweets/emollick-claude-projects-mysteries-2026-09-17.md` — source summary for Ethan Mollick's thread

## Page drafts

### wiki/tools/claude-code.md (updated)

Frontmatter: `sources:` append `claude-projects-redesigned-2026-09-17, claudeai-projects-one-conversation-2026-09-17, emollick-claude-projects-mysteries-2026-09-17`. `as_of` unchanged (2026-09-29).

In `## Mods, Projects, and cloud sessions`, replace the `**Projects:**` bullet with:

```
- **Projects:** a Claude Tag-style supervising agent for individual users without Slack admin setup. You set a goal and connect repos or documents; a coordinator chat scopes the request and routes it to parallel threads, each a full cloud session on its own branch and repo copy that opens PRs and runs tests, with overlapping edits resolved as ordinary merge conflicts. Threads share one project memory, and a library keeps added files and Claude's artifacts (each artifact with its own database several agents can read and write). Coordinator and workers take separate model and effort settings, and projects reach usage limits faster. Beta since 2026-09-17 for select Pro/Max cloud-session users (waitlist); chat, Cowork, Team and Enterprise follow. Single-player; threads were cloud-only at launch, and local runs followed.
```

In `## Recent changes`, insert between the `[2026-09-23]` and `[2026-08-08]` entries:

```
- [2026-09-17] Projects redesigned (beta, select Pro/Max cloud-session users): one coordinator chat routes work to parallel threads, each a cloud session on its own branch; shared project memory and a file/artifact library; model and effort set separately for coordinator and workers.
```

Remove from `## Recent changes` (spilled, see next draft):

```
- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
```

Append to `## Sources`:

```
- [Projects redesigned: from folder to conversation](../sources/articles/claude-projects-redesigned-2026-09-17.md)
- [Claude (@claudeai) — Projects now run from one conversation](../sources/tweets/claudeai-projects-one-conversation-2026-09-17.md)
- [Ethan Mollick — Claude Projects handles teams of agents](../sources/tweets/emollick-claude-projects-mysteries-2026-09-17.md)
```

### wiki/history/tools/claude-code.md (updated)

Append at the end of the file:

```
## Archived from current page on <apply date>

- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
```

### wiki/workflows/multi-agent-coordination.md (updated)

Frontmatter: `sources:` append `claude-projects-redesigned-2026-09-17, emollick-claude-projects-mysteries-2026-09-17`. `as_of` unchanged (2026-10-06).

In `## Where these patterns surfaced`, add after the dynamic-workflows bullet:

```
- Claude Code's redesigned Projects (beta, 2026-09-17) ship coordinator-specialist routing in a mayor-plus-polecats shape: the user briefs one coordinator chat, which opens threads that are each a full cloud session on its own branch, and overlapping edits are reconciled as ordinary merge conflicts instead of locks. In Ethan Mollick's early-access run, the orchestrator chose 18 historical mysteries and gave each its own thread; those threads launched further agents (avalanche simulation, code-breaking), then write-up agents and a separate set of skeptical fact-checkers, over about a day, mixing expensive and cheap models. Tokens were unmetered in early access, so cost is unknown, and Mollick calls the results reasonable but not definitive.
```

In `## Recent changes`, insert between the `[2026-10-06]` and `[2026-09-09]` entries:

```
- [2026-09-17] Added Claude Code Projects as a shipped instance of coordinator-specialist routing, with Ethan Mollick's 18-thread historical-mysteries run (nested agents, skeptic fact-checkers).
```

Append to `## Sources`:

```
- [Projects redesigned: from folder to conversation](../sources/articles/claude-projects-redesigned-2026-09-17.md)
- [Ethan Mollick — Claude Projects handles teams of agents](../sources/tweets/emollick-claude-projects-mysteries-2026-09-17.md)
```

### wiki/sources/articles/claude-projects-redesigned-2026-09-17.md (new)

```
---
title: 'Projects redesigned: from folder to conversation'
type: source
source_type: article
source_file: raw/articles/2026-10-26-claudecom-blog-projects-redesigned.md
url: https://claude.com/blog/projects-redesigned
published: 2026-09-17
ingested: 2026-10-26
domains: [coding, agents]
---

# Projects redesigned: from folder to conversation

Anthropic's launch post for the redesigned Projects in Claude Code. A project now has a coordinator chat that scopes a goal, routes work to parallel threads (each a Claude Code cloud session on its own branch), reviews the outputs and assembles the result, with a shared memory and a library that build up over time. The post has no date line; it says "starting today", and the same-day @claudeai thread is dated 2026-09-17.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — Projects mechanics, rollout, usage warning
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — Projects as shipped coordinator-specialist routing

## Key claims extracted

- Coordinator plus threads: you set a goal and repo/context; Claude suggests work, routes requests to new or existing threads, checks in, and follows through (PRs and tests for repos, drafts for documents)
- Each thread is a Claude Code cloud session on its own branch and repo copy; overlap between threads surfaces as a normal merge conflict; threads can further split work with subagents, loops and workflows
- Configurable per project: cloud environment, connectors, plugins, instructions, model; separate model and effort settings for the coordinator chat and worker threads
- Shared memory every thread adds to and draws from (e.g. "the release moved to Friday"); Claude also remembers working and communication style; a library collects added files and Claude-made artifacts
- Projects can reach usage limits faster; project-specific usage is visible
- Threads run in the cloud; running locally, alongside local tools and behind the user's network, is "coming very soon"
- Beta for select Pro/Max subscribers who use cloud sessions and have no existing projects on web/desktop; wider Claude Code access over the following week; then all of Claude and Team/Enterprise; waitlist for Pro/Max; existing projects keep working and will be upgraded as the rollout reaches chat and Cowork
```

### wiki/sources/tweets/claudeai-projects-one-conversation-2026-09-17.md (new)

```
---
title: 'Claude (@claudeai) — Projects now run from one conversation'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-claudeai-2100632677904744716.md
url: https://x.com/claudeai/status/2100632677904744716
published: 2026-09-17
ingested: 2026-10-26
domains: [coding, agents]
---

# Claude (@claudeai) — Projects now run from one conversation

Anthropic's launch thread for redesigned Projects, pointing to the blog post. It adds the Overview panel and the plain statement that cloud threads cannot reach local files or internal networks yet.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — launch date, cloud-only threads at launch

## Key claims extracted

- Projects run from one conversation, starting in Claude Code; Claude directs parallel threads that keep working after the laptop closes
- Beta for select Pro and Max users in cloud sessions; "coming to all Claude users soon"
- Brief Claude "the way you'd brief a chief of staff"; it routes requests to new or existing threads and checks in when it needs you
- An Overview panel shows what is waiting on you; any thread can be steered, including from a phone
- Threads run in the cloud and cannot reach files or tools on the user's computer or internal network yet; local support "coming very soon"
```

### wiki/sources/tweets/emollick-claude-projects-mysteries-2026-09-17.md (new)

```
---
title: 'Ethan Mollick (@emollick) — Claude Projects handles teams of agents'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-emollick-2100665801800093959.md
url: https://x.com/emollick/status/2100665801800093959
published: 2026-09-17
ingested: 2026-10-26
domains: [agents]
---

# Ethan Mollick (@emollick) — Claude Projects handles teams of agents

Ethan Mollick (Wharton) describes an early-access Claude Projects run in which an orchestrator agent built a small organization of agents to investigate 18 historical mysteries over a day. Results are published at historical-mysteries.netlify.app, with research notes in the open-source emollick/historical_fun repo.

## Influenced pages

- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — worked example of coordinator-specialist routing in Projects

## Key claims extracted

- You talk to one main orchestrator agent and it spins up specialists, mixing expensive and cheap agents according to your preferences
- Asked Claude Fable to select historical mysteries to try to resolve; it ran research agents, chose mysteries based on accessible data, and opened 18 threads, one per mystery
- Each thread launched more agents (e.g. avalanche simulation, code-breaking), then passed summaries to write-up agents and a separate set of skeptical fact-check agents
- About a day of work, organized by the central orchestrator
- Caveats: tokens were unlimited during early access, so costs are unknown; results are "for fun", not definitive or error-free, but mostly reasonable and grounded in the literature; Mollick takes no money from AI labs
```

## Schema / vocabulary additions

None.

## Open questions

- The shared project memory (every thread writes to and reads from it, and it remembers the user's working style) is one more product instance for `wiki/concepts/agent-memory.md`. Add a one-line mention there too, or leave it on Claude Code only (assumed: leave)?
	- Leave it
