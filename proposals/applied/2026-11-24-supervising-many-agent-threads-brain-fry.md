---
type: proposal
source: raw/newsletters/2026-11-23-your-ai-agents-can-multitask-can-you.md
status: pending
created: 2026-11-24
---

# Proposal: Supervising many agent threads — "brain fry" data and coping patterns

## Summary

### In short
Running many agents in parallel moves the bottleneck to the supervisor's attention, and the cost is now measured: in a Boston Consulting Group survey of nearly 1,500 US workers, people overseeing several agents were among the most likely to report "brain fry," with more errors and higher intent to quit. Every's head of operations gathered how nine colleagues cope, from capping active work at two projects to asking for a decision brief on re-entry. The proposal adds a "Supervising many agent threads" section to AI delegation management and a source page. Reason to hesitate: the page reaches about 99% of its length ceiling.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 23 November 2026 Arielle Shipper, Every's head of operations, published "Your AI Agents Can Multitask. Can You?" She opens with her own agent telling her she had started seven lines of work in 29 minutes, and cites a Boston Consulting Group survey (reported in Harvard Business Review) in which people overseeing multiple AI agents were among the most likely to report "brain fry": mental fatigue from using or supervising AI beyond one's capacity, which came with more errors, more decision fatigue and a stronger intention to quit.

She then asked nine colleagues, engineers and non-engineers, how they cope. One engineer caps himself at a main project plus a subproject after five sessions proved draining. An editor lets agents act alone only when he can undo the result. Another engineer spends 15 to 30 minutes on returning to a project asking the agent what happened and what needs him before deciding anything. A general manager works through threads in a fixed order: urgent, then blocked, then interesting. Others keep governing skills short and stop to rebuild the picture from the top-level goal. Several call the work exhausting and productive at once.

### What changes
The wiki notes the attention cost of agents in passing (an engineering failure mode, Anthropic's agent-idle-time data, a warning on mid-speed loops) and already has the reversible/irreversible approval line and "sort by AI-verifiability", but no survey data and no habits for supervising many threads at once.

- **AI delegation management** gains a section on supervising many threads: the BCG finding, the two-project cap, the re-entry decision brief, the urgent-blocked-interesting order, short skills, and stepping back to the goal; the approval line and the verifiable-versus-judgment sort are cross-referenced rather than repeated. One new failure mode, one Recent-changes entry; page date moves to 23 November. Its index line is updated.
- One new source page.

### What to weigh
Scope: these habits come from one company's staff, engineers and non-engineers alike, so they go on the general delegation page rather than the engineering enablement page, which is already over its length ceiling. The BCG figure is taken from the Every article; the HBR write-up was not read.

## Intended changes

- [ ] **Update** `wiki/training/ai-delegation-management.md` — new `## Supervising many agent threads` section after `## Raising the ambition of a delegation`; one new failure mode; add `every-agents-multitask-brain-fry-2026-11-23` to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-11-23 (list has 7, no spill); `as_of` 2026-10-25 → 2026-11-23
- [ ] **Update** `wiki/index.md` — refresh the AI delegation management line's description and date
- [ ] **Create** `wiki/sources/newsletters/every-agents-multitask-brain-fry-2026-11-23.md` — source summary

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

Frontmatter: `as_of: 2026-11-23`; append `every-agents-multitask-brain-fry-2026-11-23` to `sources:`.

Insert after `## Raising the ambition of a delegation` (after the line "All three directions assume the agent has a computer…") and before `## Failure modes`:

```
## Supervising many agent threads

Parallel agents move the limit to the supervisor. In a Boston Consulting Group survey of nearly 1,500 US workers (reported in HBR), people overseeing multiple AI agents were among the most likely to report "brain fry," fatigue from supervising AI beyond their capacity, which came with more errors, more decision fatigue and higher intent to quit. Habits from nine Every staff, engineers and non-engineers (November 2026):

- **Cap active work.** One engineer's ceiling is a main project plus one subproject, with only persistent tasks running in the background; five live sessions was draining.
- **Decide what runs unattended before the block starts.** Send work an AI can check to the background and keep judgment work in the foreground (the sort is described on [AI work delegation modes](ai-work-delegation-modes.md)). Another makes every creative decision up front and counts a mid-run request for input as a failure.
- **Let reversibility decide what comes back to you.** The same approval line as for standing agents (see layered access control above), applied to reduce switching: agents act alone when the result can be undone, and publishing, purchases and design calls without an obvious answer return to the human.
- **Re-enter with a decision brief, not a recap.** On returning to a project, spend 15–30 minutes asking what happened, where things stand, and which decisions need you, with options and a recommendation, before deciding anything.
- **Triage threads in a fixed order:** urgent, then blocked (unblocking frees the thread to keep going), then interesting.
- **Keep the structure plain.** A short skill per pipeline (write, check, stop for review) keeps parallel sessions from colliding; complex skills get followed worse.
- **Step back to the goal.** When deep in a sub-goal of a sub-goal, have the orchestrator restate the top-level goal and sort work in flight into needed, nice to have, or drifted before handing out more.

Some report the same mode as draining and productive at once; prior experience managing people made constant switching feel routine for one general manager.
```

`## Failure modes`, append:

```
- **Thread sprawl.** Starting new agent work while waiting on the last ("seven lines of work in 29 minutes") until no thread gets deep thought, and finished threads sit unnoticed.
```

`## Recent changes`: insert at the top:

```
- [2026-11-23] Added "Supervising many agent threads": BCG's "brain fry" survey finding and Every staff habits (two-project cap, reversibility as the autonomy line, re-entry decision brief, urgent-blocked-interesting triage, short skills, step back to the goal), plus a thread-sprawl failure mode.
```

`## Sources`: append

```
- [Every — Your AI Agents Can Multitask. Can You?](../sources/newsletters/every-agents-multitask-brain-fry-2026-11-23.md)
```

### wiki/index.md (updated)

Before:

```
- [training/ai-delegation-management](training/ai-delegation-management.md) — practical guidance for delegating work to agents using management fundamentals: scope, authority, loop tempo, review cost, definition of done, spec-first delegation, irrefutable proof, agent-built iteration tools, and async work with scheduled wake-ups *(as_of: 2026-10-25)*
```

After:

```
- [training/ai-delegation-management](training/ai-delegation-management.md) — practical guidance for delegating work to agents using management fundamentals: scope, authority, loop tempo, review cost, definition of done, spec-first delegation, irrefutable proof, agent-built iteration tools, async work with scheduled wake-ups, and supervising many threads without "brain fry" *(as_of: 2026-11-23)*
```

### wiki/sources/newsletters/every-agents-multitask-brain-fry-2026-11-23.md (new)

```
---
title: "Your AI Agents Can Multitask. Can You? — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-23-your-ai-agents-can-multitask-can-you.md
url: https://every.to/p/your-ai-agents-can-multitask-can-you
published: 2026-11-23
ingested: 2026-11-24
domains: [agents]
---

# Your AI Agents Can Multitask. Can You? — Every

Arielle Shipper (Every's head of operations) on the attention cost of supervising many agent threads, citing a BCG survey on "brain fry," and nine colleagues' habits for staying effective, each with a prompt.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — "Supervising many agent threads" section and thread-sprawl failure mode

## Key claims extracted

- BCG survey of nearly 1,500 US workers (via HBR): people overseeing multiple AI agents were among the most likely to report "brain fry," with more errors, more decision fatigue and higher intent to quit
- Lee Knowlton: productivity maxes out at a main project plus a subproject; five sessions was draining; sort work into AI-verifiable vs judgment before a block
- Jack Cheng: agents act alone when the result is reversible; publishing, purchasing and ambiguous design choices come back to him
- Jannik Jung: 15–30 minutes on re-entry asking what happened, where things stand, what needs him
- Paridhi Agarwal: "simple structure beats complex setups"; complex skills are followed worse
- Marcus Moretti: thread triage order is urgent, then blocked, then interesting
- Mike Deal: pause and ask "What are we actually trying to do and why?"
- Kieran Klaassen: decisions made before execution; agent requests for input afterwards count as failure
```

## Schema / vocabulary additions

None.

## Open questions

None.
