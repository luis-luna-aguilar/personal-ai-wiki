---
type: proposal
source: raw/newsletters/2026-10-08-why-we-handed-our-agents-infrastructure-to-anthro.md
sources:
  - raw/newsletters/2026-10-08-why-we-handed-our-agents-infrastructure-to-anthro.md
  - raw/newsletters/2026-10-07-building-a-more-efficient-agent.md
  - raw/newsletters/2026-10-06-introducing-the-every-agent.md
  - raw/newsletters/2026-10-06-launching-today-every-our-slack-agent.md
  - raw/newsletters/2026-10-11-one-agent-for-the-whole-company.md
  - raw/newsletters/2026-10-14-the-best-founders-have-something-ai-cant-tell-t.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Every Agent, one shared company agent on Claude Managed Agents

## Summary

### In short
One agent shared by the whole company beats an agent per employee, and most of the cost of running one is waste in your own code, not the model. Every replaced its per-person OpenClaw fleet with @Every on Claude Managed Agents, and cut token cost on 11 frequent tasks by over 80% after a failed Sonnet-to-Opus router and a broken prompt cache. The proposal updates Claude Managed Agents, Cost-aware task routing, Delegation modes, Company-wide enablement and Multiplayer AI, and maps "company agent" in the knowledge hub. Hesitation: the personal-to-shared pivot is already recorded, so part of this overlaps.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Every, the media and software company, launched the Every Agent on 6 October 2026: a single Slack agent, tagged as @Every, that the whole company shares. Dan Shipper's launch post argues that most AI use is invisible, so a good workflow found by one person never spreads; when the work happens in a public Slack thread, colleagues see the request and the corrections and copy them. Successful workflows are saved as skills anyone can run. It replaced Plus One, the March experiment that gave each employee their own OpenClaw agent. Those agents were "high-maintenance pets": dozens of cloud machines to watch, expiring sign-ins, and bots nobody remembered the purpose of.

Engineer Paridhi Agarwal's 8 October piece explains the infrastructure. After a month of self-hosting one agent, Every moved to Anthropic's Claude Managed Agents (CMA). Each Slack thread is a session on a virtual machine that costs 8 cents an hour while running, memory is folders of notes, and app calls are made by Every's servers with the asking user's login, so the agent never holds a credential. A small, fast model decides whether to answer untagged thread messages. The trade-offs she names: CMA only runs Claude, it is not eligible for zero-data retention, and long sessions hit cache-rewrite costs and empty replies near the context limit. Rotating idle DMs into a fresh session with a recap cut total cost by 39%.

A 7 October companion piece covers cost: the real wins were Opus 5.5, leaner tool outputs, and a cache bug where each user's Slack ID in memory-folder names made every system prompt unique (the fix cut 74% in a best-case test). A 14 October field report from FeanixBio, a 28-person agritech startup, shows daily operations sweeps, but its CEO stopped using the agent over beta-era cost.

### What changes
The wiki already says Every reversed its personal-agent default and lists the Every Agent as "in-progress"; Claude Managed Agents has only Spiral as a named customer.

- **Claude Managed Agents** gains Every as a production customer (thread-per-session, 8¢/hour VMs, credential proxying) and two caveats: Claude-only with no zero-data retention, and long sessions needing rotation. The "no pricing captured" caveat is replaced. Page date moves to 8 October.
- **Cost-aware AI task routing** gains one evidence bullet: the failed coordinator router and the cache-key bug, with Every's four-step cost audit.
- **AI work delegation modes** extends its existing Every bullet with the reasons personal agents failed and Willie Williams's work/home split.
- **Company-wide AI enablement** drops "in-progress" from the buy/build/rent bullet and gains a "prompt in public with one shared agent" pattern with the FeanixBio cost caveat; the oldest Recent-changes entry spills to history. Page date moves to 14 October.
- **Multiplayer AI** gains the Every Agent as the first production case scored against the manifesto's principles.
- **Knowledge architectures** gains a term-map row sending "company agent" to Multiplayer AI, not to Company brain.
- Four new source pages, one per substantive newsletter.

### What to weigh
The main judgment is the term mapping. "Company agent" could be read as an alias for Company brain, since @Every keeps memory and skills, but Every describes a shared coworker, not a knowledge system, so the draft maps it to Multiplayer AI and notes the memory part. Two raw files (the launch promo email and the 11 October recap) add nothing new and get no source page.

## Intended changes

- [ ] **Update** `wiki/tools/claude-managed-agents.md` — adds an Every Agent production bullet to Current status, replaces the "no pricing captured" caveat, adds two caveats, adds one Recent-changes entry dated 2026-10-08 (7 → 8 entries, no spill), appends two sources; `as_of` 2026-08-28 → 2026-10-08
- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — adds one bullet to Evidence from practice → Routing as infrastructure, adds one Recent-changes entry dated 2026-10-07 (5 → 6, no spill), appends one source; `as_of` stays 2026-10-19
- [ ] **Update** `wiki/training/ai-work-delegation-modes.md` — extends the existing "Every reverses its personal-agent default" bullet, adds one Recent-changes entry dated 2026-10-08 (2 → 3), appends two sources; `as_of` stays 2026-10-19
- [ ] **Update** `wiki/training/company-wide-ai-enablement.md` — edits the buy/build/rent bullet, adds one Onboarding-and-culture bullet, adds one Recent-changes entry dated 2026-10-14 (10 → 11), appends three sources; `as_of` 2026-09-04 → 2026-10-14
- [ ] **Spill** `wiki/training/company-wide-ai-enablement.md` → `wiki/history/training/company-wide-ai-enablement.md` — the oldest Recent-changes entry (2026-06-30, explicit-bets exercise) moves to history to hold the cap of 10
- [ ] **Update** `wiki/concepts/multiplayer-ai.md` — adds one Current-status bullet, adds one Recent-changes entry dated 2026-10-08, appends two sources; `as_of` 2026-09-14 → 2026-10-08
- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — adds one term-map row for "company agent", adds one Recent-changes entry dated 2026-10-08 (5 → 6), appends one source; `as_of` stays 2026-10-19
- [ ] **Create** `wiki/sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/every-agent-token-efficiency-2026-10-07.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/every-agent-launch-2026-10-06.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/every-feanixbio-field-report-2026-10-14.md` — source summary

## Page drafts

### wiki/tools/claude-managed-agents.md (updated)

Frontmatter: `as_of: 2026-10-08`; append `every-agent-claude-managed-agents-2026-10-08, every-agent-token-efficiency-2026-10-07` to `sources:`.

Heading change: `## Current status (as of 2026-08-28)` → `## Current status (as of 2026-10-08)`. Insert after the existing Spiral bullet:

```md
- **Every Agent in production (October 2026):** Every built @Every, one Slack agent shared by the whole company, on CMA after a month of self-hosting a single agent persuaded it not to run its own infrastructure. Each Slack thread is one session on a VM billed at 8 cents an hour while running; memory is folders of notes the agent reads at session start; app calls pause the agent and are made by Every's servers with the asking user's own login, so the agent never holds a credential.
```

In `## Weaknesses / caveats`, replace:

```md
- No pricing or availability tiering is captured here; the public API surface is documented above but granular pricing has not been
```

with:

```md
- Session VM pricing is known only from Every's account (8 cents an hour while running); token cost follows the Claude model chosen per session
- **Claude-only, no zero-data retention.** CMA runs only Claude models: a session can pick a cheaper Claude model, but there is no routing to other labs. Because it keeps session history to resume work, it is not eligible for Anthropic's zero-data-retention option. Every's own inventory of what leaving would take (harness, sessions, memory, tools, sandboxes) came to months of work.
- **Long sessions need rotating.** A three-day DM session kept paying to rewrite its whole history into the cache, and near the context limit Opus sometimes returned empty replies. Starting a fresh session with a short recap once a DM goes quiet cut total cost 39% on replayed conversations. Teams running their own servers beside the hosted agent must answer outstanding tool requests before a deploy, or the agent hangs.
```

`## Recent changes` — insert one entry at the top (no spill):

```md
- [2026-10-08] Every's production account of the Every Agent: thread-per-session on 8¢/hour VMs, credential proxying through its own servers, and the limits it lives with (Claude-only, no zero-data retention, long sessions rotated with a recap for −39% cost).
```

`## Sources` — append:

```md
- [Every — Why We Handed Our Agent's Infrastructure to Anthropic](../sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md)
- [Every — Building a More Efficient Agent](../sources/newsletters/every-agent-token-efficiency-2026-10-07.md)
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter: append `every-agent-token-efficiency-2026-10-07` to `sources:`; `as_of` stays 2026-10-19.

Append to the end of `### Routing as infrastructure`:

```md
- **Every Agent: fix waste before building a router.** Every first sent all Every Agent work through a Sonnet coordinator told to escalate hard jobs to Opus; quality and speed fell and cost rose, because many requests ran on both models. Engineer Paridhi Agarwal hunted waste instead: Opus 5.5, shorter tool outputs and deferred tool definitions (about 10%), and a cache bug where each user's Slack ID in memory-folder names made every system prompt unique (−74% in a best-case test). Together these cut cost on 11 frequent tasks by over 80%. Her audit: have the agent explain the system first, prefer features you already pay for, measure each change before and after including quality, then trace what is still expensive.
```

`## Recent changes` — insert one entry after the 2026-10-19 entries and before the 2026-07-08 entry (no spill):

```md
- [2026-10-07] Added Every's Every Agent cost work: a coordinator router that raised cost, and a per-user cache-key bug whose fix drove most of an >80% saving.
```

`## Sources` — append:

```md
- [Every — Building a More Efficient Agent](../sources/newsletters/every-agent-token-efficiency-2026-10-07.md)
```

### wiki/training/ai-work-delegation-modes.md (updated)

Frontmatter: append `every-agent-launch-2026-10-06, every-agent-token-efficiency-2026-10-07` to `sources:`; `as_of` stays 2026-10-19.

In `## Evidence from practice`, replace the existing bullet:

```md
- **Every reverses its personal-agent default.** After months of running individual OpenClaw-style personal agents, Every found a stronger model still can't log in when a credential expires or notice a silently-broken integration — the maintenance burden falls entirely on the agent's owner. Their new default is a single shared "Every Agent" living in Slack: the whole company shares one agent, but each person works through their own connections and context. A personal Claw can still make sense for recurring work specific to one person who's willing to maintain it and doesn't need company-wide context.
```

with:

```md
- **Every reverses its personal-agent default.** After months of running individual OpenClaw-style personal agents, Every found a stronger model still can't log in when a credential expires or notice a silently-broken integration — the maintenance burden falls entirely on the agent's owner. Their new default, launched publicly as the Every Agent in October 2026, is a single shared agent living in Slack: the whole company shares one agent, but each person works through their own connections and context. Every's other reasons: a personal agent only knew its owner's work, a good workflow stayed with one agent, every fix had to be made once per agent, and nobody remembered which bot did what, while the threads where the whole team pulled in one agent worked best. A personal Claw can still make sense for recurring work specific to one person who's willing to maintain it and doesn't need company-wide context; Every's Willie Williams expects a company agent at work and a personal agent at home, with transactional tasks going to a Codex thread.
```

`## Recent changes` — insert one entry after the 2026-10-17 entry:

```md
- [2026-10-08] Extended Every's personal-to-shared agent evidence with the reasons the per-person agents failed and the October launch of the shared Every Agent.
```

`## Sources` — append:

```md
- [Every — Introducing the Every Agent](../sources/newsletters/every-agent-launch-2026-10-06.md)
- [Every — Building a More Efficient Agent](../sources/newsletters/every-agent-token-efficiency-2026-10-07.md)
```

### wiki/training/company-wide-ai-enablement.md (updated)

Frontmatter: `as_of: 2026-10-14`; append `every-agent-launch-2026-10-06, every-agent-claude-managed-agents-2026-10-08, every-feanixbio-field-report-2026-10-14` to `sources:`.

In `### Platform, strategy, and process redesign`, in the **Buy, build, or rent** bullet, replace:

```md
and Every's own in-progress Every Agent).
```

with:

```md
and Every's own Every Agent, launched in October 2026 on rented machinery: Anthropic's [Claude Managed Agents](../tools/claude-managed-agents.md)).
```

Append to the end of `### Onboarding and culture`:

```md
- **Prompt in public with one shared agent.** Every's case for a single Slack agent over one per employee: most AI use is invisible, so colleagues never see the request or the corrections behind a good result. In a public thread they do, and a workflow saved as a skill becomes runnable by anyone (Every's editor's 30,000 copyedits became a "Kate Pass" the whole team uses). At FeanixBio, a 28-person agritech customer, the agent runs daily operations sweeps and condenses agent-bloated threads, but adoption stayed uneven: the CEO stopped delegating his tickets to it over beta-era token cost.
```

`## Recent changes` — insert one entry at the top, then spill the oldest (2026-06-30) entry to history:

```md
- [2026-10-14] Every Agent launched: the buy/build/rent example is no longer "in-progress", and a prompt-in-public shared-agent pattern is added with FeanixBio's uneven-adoption and cost caveat.
```

Remove from the live list:

```md
- [2026-06-30] Added explicit-bets strategy exercise: name token, lock-in, wrapper, vertical, data-moat, regulation, and switching-cost assumptions before committing AI strategy.
```

`## Sources` — append:

```md
- [Every — Introducing the Every Agent](../sources/newsletters/every-agent-launch-2026-10-06.md)
- [Every — Why We Handed Our Agent's Infrastructure to Anthropic](../sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md)
- [Every — How an AI-native agritech startup works with agents in Slack](../sources/newsletters/every-feanixbio-field-report-2026-10-14.md)
```

### wiki/history/training/company-wide-ai-enablement.md (updated)

Append at the end of the file:

```md

## Archived from current page on <apply date>

- [2026-06-30] Added explicit-bets strategy exercise: name token, lock-in, wrapper, vertical, data-moat, regulation, and switching-cost assumptions before committing AI strategy.
```

### wiki/concepts/multiplayer-ai.md (updated)

Frontmatter: `as_of: 2026-10-08`; append `every-agent-launch-2026-10-06, every-agent-claude-managed-agents-2026-10-08` to `sources:`.

Heading change: `## Current status (as of 2026-09-14)` → `## Current status (as of 2026-10-08)`. Append a fifth bullet:

```md
- First production case against the rubric: Every's [Every Agent](../tools/claude-managed-agents.md) (October 2026), one Slack agent the whole company shares. It fits "work with the door open" (Every's argument for the switch is that people learn by watching others' agents in public threads) and "continuously improve" (a corrected workflow is saved as a skill anyone can run). It breaks "stay model-provider-agnostic": built on Claude Managed Agents, it can only run Claude.
```

`## Recent changes` — insert one entry at the top:

```md
- [2026-10-08] Added the Every Agent as the first production shared agent scored against the manifesto's principles.
```

`## Sources` — append:

```md
- [Every — Introducing the Every Agent](../sources/newsletters/every-agent-launch-2026-10-06.md)
- [Every — Why We Handed Our Agent's Infrastructure to Anthropic](../sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter: append `every-agent-claude-managed-agents-2026-10-08` to `sources:`; `as_of` stays 2026-10-19.

In `## Term map`, insert after the `context engineering` row:

```md
| company agent, shared company agent | [Multiplayer AI](multiplayer-ai.md), outside this cluster | one agent a whole organization shares in team chat (Every Agent). Its memory folders and saved skills are [agent memory](agent-memory.md) at company scope; it is a company brain only if it also carries a knowledge layer and a refresh loop |
```

`## Recent changes` — insert one entry at the top:

```md
- [2026-10-08] Mapped "company agent" (Every Agent) to Multiplayer AI, outside the cluster, with its memory part pointed at Agent memory.
```

`## Sources` — append:

```md
- [Every — Why We Handed Our Agent's Infrastructure to Anthropic](../sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md)
```

### wiki/sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md (new)

```md
---
title: "Why We Handed Our Agent's Infrastructure to Anthropic — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-why-we-handed-our-agents-infrastructure-to-anthro.md
url: https://every.to/source-code/why-we-handed-our-agent-s-infrastructure-to-anthropic
published: 2026-10-08
ingested: 2026-10-20
domains: [agents]
---

# Why We Handed Our Agent's Infrastructure to Anthropic — Every

Every engineer Paridhi Agarwal explains how the Every Agent, a single Slack agent shared by the whole company, came to run on Claude Managed Agents: why per-employee OpenClaw agents ("pets") were abandoned, why self-hosting even one agent was dropped after a month, how Slack threads map to sessions and credentials stay on Every's servers, and the trade-offs accepted (Claude-only, no zero-data retention, deploy-time hangs, long-session cost and empty replies).

## Influenced pages

- [Claude Managed Agents](../../tools/claude-managed-agents.md) — production customer bullet, Claude-only / no-ZDR and long-session caveats
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — Every Agent no longer "in-progress"; rented machinery
- [Multiplayer AI](../../concepts/multiplayer-ai.md) — first production case against the rubric
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "company agent" term-map row

## Key claims extracted

- Every Agent launched 2026-10-06; built over five months; moved to CMA in early May after a month of self-hosting
- Each Slack thread is a CMA session on a VM costing 8 cents an hour while running; memory is folders of notes read at session start
- App calls pause the agent and are executed by Every's servers with the user's own login; the agent never holds credentials; skill changes need the skill owner's approval
- A small, fast model decides whether to reply, react with an emoji, or stay quiet on untagged thread messages
- Opus 5 made replies grow from ~280 to ~880 characters; Opus 5.5 fixed it
- Rotating idle DMs into a fresh session with a recap cut total cost 39% on replayed conversations
- CMA runs only Claude and is not eligible for zero-data retention; moving off would take months
```

### wiki/sources/newsletters/every-agent-token-efficiency-2026-10-07.md (new)

```md
---
title: "Building a More Efficient Agent — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-07-building-a-more-efficient-agent.md
url: https://every.to/context-window/building-a-more-efficient-agent
published: 2026-10-07
ingested: 2026-10-20
domains: [agents]
---

# Building a More Efficient Agent — Every

Every's Context Window edition on cutting the Every Agent's token cost, plus Every Podcast highlights on why the company traded personal agents for one company agent. A Sonnet-coordinator router raised cost; an Opus 5.5 upgrade, leaner tools, and a cache-key fix cut cost on 11 frequent tasks by over 80%. Includes a four-step cost-audit workflow with prompts.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — coordinator-router failure, cache-key bug, four-step audit
- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — reasons personal agents died off; work/home agent split
- [Claude Managed Agents](../../tools/claude-managed-agents.md) — supporting source for the production bullet

## Key claims extracted

- Routing all tasks through a Sonnet coordinator that escalated to Opus lowered quality and speed and raised cost (requests often ran on both)
- Tool-output trimming and deferred tool loading cut cost about 10%
- Per-user Slack IDs in memory-folder names made system prompts unique and broke caching; the fix cut cost 74% in a best-case test
- Overall: >80% token-cost reduction across 11 frequent tasks; tokens passed to customers at zero markup
- Willie Williams: personal bots in Slack mostly died off because they were hard to maintain and nobody remembered which did what; expects a company agent at work and a personal agent at home
```

### wiki/sources/newsletters/every-agent-launch-2026-10-06.md (new)

```md
---
title: "Introducing the Every Agent — Dan Shipper"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-06-introducing-the-every-agent.md
url: https://every.to/on-every/introducing-the-every-agent
published: 2026-10-06
ingested: 2026-10-20
domains: [agents]
---

# Introducing the Every Agent — Dan Shipper

Launch post for the Every Agent, a Slack agent shared by a whole company. Dan Shipper argues for "prompting in public": most AI use is invisible, and a shared agent working in public threads lets workflows spread by example. Successful workflows are saved as skills anyone can run. Pricing: $15 free credit per person (up to $500 per workspace), then a $30/month Every subscription, with tokens billed at zero markup.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — prompt-in-public shared-agent pattern
- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — October launch of the shared agent
- [Multiplayer AI](../../concepts/multiplayer-ai.md) — "work with the door open" and skill-saving evidence

## Key claims extracted

- One shared agent working in public "AI-pills a company faster than a horde of personal ones"; replaces the March Plus One per-person agents
- Corrections in a thread can be saved; workflows become skills runnable by anyone (e.g. a copyedit skill built from an editor's 30,000 historical edits)
- 1,000+ tool connections, with per-connection teammate access; pre-installed Every skills; "Frontier Alerts" on new models
- Built on Claude Managed Agents
```

### wiki/sources/newsletters/every-feanixbio-field-report-2026-10-14.md (new)

```md
---
title: "How an AI-native agritech startup works with agents in Slack — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-14-the-best-founders-have-something-ai-cant-tell-t.md
url: https://every.to/context-window/the-best-founders-have-something-ai-can-t-tell-them
published: 2026-10-14
ingested: 2026-10-20
domains: [agents]
---

# How an AI-native agritech startup works with agents in Slack — Every

Field report (in Every's Context Window, 14 October 2026) on FeanixBio, a 28-person cattle-genetics startup whose Slack holds several agents: an in-house OpenClaw data agent, Linear's agent, personal assistants, and the Every Agent. Also includes a new hire's account of using the Every Agent as an onboarding buddy.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — uneven adoption and cost caveat on the shared-agent pattern

## Key claims extracted

- The Every Agent produces daily operations sweeps (unhappy customers, coverage gaps) and green/yellow/red ticket reports for the CTO
- Used to condense 70-plus-message threads, half agent-generated
- The CEO stopped delegating his Linear tickets to it over beta-era cost; cheaper alternatives could not match its quality
- Every Agent token spend down about 60% since Opus 5.5 (Every engineer Marcus Moretti)
- Onboarding: a shared agent answers "who is X / what does this term mean" from company documents, but repeats errors it finds in them
```

## Schema / vocabulary additions

None.

## Open questions

- Should "company agent" map to Multiplayer AI (assumed, as drafted) or become an alias on Company brain's `## Also called` line?
