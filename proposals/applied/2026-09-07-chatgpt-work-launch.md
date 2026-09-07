---
type: proposal
source: raw/newsletters/2026-08-04-unpacking-chatgpt-work-the-agent-for-a-billion-us.md
status: pending
created: 2026-09-07
---

# Proposal: ChatGPT Work — architecture teardown

## Summary

### The source

On July 9, OpenAI launched ChatGPT Work, its agent product for knowledge work — three new models across fourteen configurations, a merged ChatGPT/Codex desktop app, and cloud agents in their most mainstream form yet. Three weeks later, Latent Space guest writer Shlok published a detailed teardown of what Work actually is under the hood, based on directly poking around inside it with Codex. Work connects to the tools people already use — Slack, email, Drive, calendars, CRMs, and a 1,000+-entry plugin directory — and runs on the Codex harness inside a persistent, isolated cloud microVM (Pro accounts get 8 CPUs, 20GB RAM, 64GB disk; Plus gets 14GB RAM), alongside a managed Chrome browser service the agent operates through tool calls. Three weeks in, Work plus Codex had reportedly crossed 10 million users, and Greg Brockman has confirmed Work and regular Chat will merge into one product by year-end — making Work's current design choices a preview of how ChatGPT's roughly one billion weekly users will eventually work.

The most interesting finding is architectural: unlike OpenClaw, where an agent's whole state lives on one always-on computer, Work deliberately keeps continuity in the ChatGPT product layer rather than the machine. Each task gets its own scratch working directory, but cross-task context flows through separately-managed services — Personal Context (queries chat/Work history), the Library (a canonical file store distinct from each thread's local copy, so the two can silently diverge), and Projects (standing instructions plus source files, not represented as a real directory the way Codex represents one). The user's persistent "memory" is a synthesized profile the product supplies at task start; the agent can read but not edit it. The piece also covers early proactive task suggestions drawn from calendar/email context, two-tier Scheduled Tasks (a standalone saved-prompt automation vs. a heartbeat-triggered automation that resumes a specific thread with its context intact), and the Plugin Directory's discovery gap — Work never suggests an installed-but-relevant plugin, even when a user names the service by name.

### What changes

The wiki has no page dedicated to Work's own architecture; the closest existing coverage is **Codex**, which already tracks OpenAI's July 14 "superapp" merge (Chat/Work/Codex modes inside one desktop app) and Work's earlier "Workspace Agents" framing in **State of Agents**.

- **Codex** gains a new section on Work's cloud-computer architecture: the microVM specs, the deliberate split between agent-owned scratch space and product-managed continuity (Personal Context / Library / Projects), the browser-service tool-call model with a persistent browser profile, proactive task suggestions, the two Scheduled Tasks types, and the Plugin Directory's scale-vs-discovery gap. New Recent-changes entry; `as_of` moves to 8 August.
- **State of Agents** refreshes its existing Codex/Workspace-Agents line in the Agent orchestration subcategory to reflect the 10M-user milestone and the confirmed Chat/Work merger timeline; `as_of` for that line moves to 8 August.
- One new source page for the Latent Space teardown.

### What to weigh

This is a single secondary-analysis source (a guest writer's independent investigation, not an OpenAI primary announcement), though it's unusually well-grounded — the author links each specific claim to a live conversation transcript with Codex/Work as evidence. The main judgment call is scope: I folded this into the existing Codex page rather than creating a standalone `tools/chatgpt-work.md`, since the wiki already treats Work as a mode of the same Codex-harness product rather than a separate tool, and the July 14 entry already anchors that framing — a separate page would duplicate rather than extend that context. Reopen this if you'd rather Work get its own page going forward as it grows more distinct from developer-facing Codex.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/codex.md` — new section on ChatGPT Work's cloud-computer architecture, new Recent-changes entry, `as_of` → 2026-08-04, new source id
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — refresh the Codex/Workspace-Agents line in Agent orchestration with the 10M-user milestone and confirmed Chat/Work merger; line date → 2026-08-04
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/chatgpt-work-launch-2026-08-04.md` — source summary

## Page drafts

### wiki/tools/codex.md (updated)

Add a new section after `## Codex Chronicle (as of 2026-04-21)` and before `## Recent changes`:

```md
## ChatGPT Work architecture (as of 2026-08-04)

A detailed independent teardown of Work — the ChatGPT mode OpenAI folded Codex into on 2026-07-14 — clarifies how the product actually holds state across tasks.

- Each Work task runs inside a persistent, isolated cloud microVM (Pro: 8 CPUs/20GB RAM/64GB disk; Plus: 14GB RAM), with the agent operating a separately hosted, persistent-profile Chrome browser through tool calls rather than a local browser on the same machine.
- Continuity across tasks deliberately does **not** live on the computer the way it does in OpenClaw. Each task gets its own `/workspace/scratch` directory, but cross-task context flows through product-managed services instead: Personal Context (queries prior chat/Work history on demand), the Library (a canonical file store distinct from each thread's local copy — the two can silently diverge if a file changes in the Library after a thread already has a local copy), and Projects (standing instructions plus source files, supplied to new tasks but not represented as a real directory).
- The user's "memory" supplied to each task is a product-maintained synthesized profile; the agent can reason from it but can't edit it or write OpenClaw-style memory files other tasks load by default.
- Early proactive-task suggestions: Work can surface a pre-authored prompt drawn from calendar/email context (e.g. a meeting-prep brief) at the start of a new conversation, though the user still has to select and run it — full unprompted autonomy isn't there yet.
- Scheduled Tasks come in two forms: a standalone automation that opens a fresh task from a saved prompt each run, and a heartbeat-triggered automation that resumes a specific existing thread with its context intact (heartbeats work in the desktop app but aren't yet exposed in Work on the web).
- The Plugin Directory has scaled past 1,000 plugins (apps, skills, app templates) but has a real discovery gap: Work doesn't suggest an installed-but-relevant plugin for a task, even when the user names the target service directly.
- Three weeks after the July 9 launch, Work plus Codex had reportedly crossed 10 million users; Greg Brockman has confirmed Work and regular Chat will merge into one product by the end of 2026.
```

Also update the frontmatter `as_of:` from `2026-07-14` to `2026-08-04`, and append `chatgpt-work-launch-2026-08-04` to the `sources:` list.

Add to `## Recent changes` (as the newest entry, before the existing `[2026-07-14]` entry):

```md
- [2026-08-04] Independent architecture teardown of ChatGPT Work: persistent cloud microVM specs, deliberate split between agent-owned scratch space and product-managed continuity (Personal Context/Library/Projects), browser-service tool-call model, two-tier Scheduled Tasks, Plugin Directory discovery gap, and 10M-user milestone three weeks post-launch.
```

Add to `## Sources` (as a new entry):

```md
- [ChatGPT Work architecture teardown](../sources/newsletters/chatgpt-work-launch-2026-08-04.md)
```

### wiki/state-of/agents.md (updated)

Replace the existing Codex line in `### Agent orchestration`:

> **Before:**
> `- [Codex](../tools/codex.md) (Workspace Agents) — OpenAI; shareable team agents in Slack and ChatGPT for scheduling, research, drafting, coding, and data analysis; now positioned as a broader computer-work agent (docs, sheets, slides, browser flows, connected apps) beyond software engineering; Every's July coverage frames it as a general-purpose workspace agent spanning inbox, CRM, healthcare coordination, writing, and personal-knowledge workflows *(as of 2026-07-01)*`

> **After:**
> `- [Codex](../tools/codex.md) (ChatGPT Work) — OpenAI; Work runs on the Codex harness inside a persistent cloud microVM and connects to Slack, email, Drive, calendars, CRMs, and a 1,000+-entry plugin directory; reportedly crossed 10M users (with Codex) three weeks after its July 9 launch, and OpenAI has confirmed Work will merge into regular Chat by year-end *(as of 2026-08-04)*`

### wiki/sources/newsletters/chatgpt-work-launch-2026-08-04.md (new)

```md
---
title: Unpacking ChatGPT Work — the Agent for a Billion Users
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-04-unpacking-chatgpt-work-the-agent-for-a-billion-us.md
url: https://www.latent.space/p/unpacking-chatgpt-work
published: 2026-08-04
ingested: 2026-09-07
domains: [agents]
---

# Unpacking ChatGPT Work — the Agent for a Billion Users

Latent Space guest post (Shlok) independently investigating OpenAI's July 9 ChatGPT Work launch, based on direct hands-on use with Codex/Work. Covers Work's cloud-microVM architecture, its deliberate split between agent-owned scratch space and product-managed continuity (Personal Context, Library, Projects), browser-service tool use with a persistent browser profile, early proactive task suggestions, two-tier Scheduled Tasks, and the 1,000+-plugin Plugin Directory's discovery gap. Reports Work plus Codex crossing 10M users three weeks post-launch and a confirmed Chat/Work merger by year-end.

## Influenced pages

- [tools/codex](../../tools/codex.md) — new section on Work's cloud-computer architecture and continuity model
- [state-of/agents](../../state-of/agents.md) — refreshed Codex/Workspace-Agents line with the 10M-user milestone and merger timeline

## Key claims extracted

- ChatGPT Work launched 2026-07-09: three new models across fourteen configurations, merged ChatGPT/Codex desktop app, mainstream cloud agents
- Work plus Codex reportedly crossed 10M users three weeks post-launch
- Pro cloud microVM: 8 CPUs, 20GB RAM, 64GB disk; Plus: 14GB RAM
- Continuity across tasks flows through Personal Context, Library, and Projects — not through the computer itself, unlike OpenClaw
- Library and per-thread local file copies can silently diverge (no sync)
- Two Scheduled Tasks types: standalone (fresh task from saved prompt) and heartbeat-triggered (resumes an existing thread with context intact)
- Plugin Directory has 1,000+ plugins but doesn't suggest relevant installed-but-unused plugins, even when the service is named directly
- Greg Brockman has confirmed Work and Chat will merge into one product by end of 2026
```

## Open questions

- Should Work eventually get its own `tools/chatgpt-work.md` page once/if it diverges further from developer-facing Codex, or should the wiki keep treating "Codex" as the umbrella product across all three ChatGPT modes indefinitely? Leaving as Codex-umbrella for now per the note above.
