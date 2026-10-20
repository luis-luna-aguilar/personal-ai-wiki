---
type: proposal
source: raw/newsletters/2026-10-16-context-engineering-is-knowing-when-to-start-over.md
sources:
  - raw/newsletters/2026-10-05-when-trying-to-make-ai-better-makes-it-worse.md
  - raw/newsletters/2026-10-16-context-engineering-is-knowing-when-to-start-over.md
  - raw/newsletters/2026-10-11-one-agent-for-the-whole-company.md
  - raw/newsletters/2026-10-18-codexs-comeback-up-close.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Instruction bloat and seven ways chat context goes wrong

## Summary

### In short
More instructions can make AI worse: when a context grows, the concrete, checkable rules crowd out the judgment ones, and the fix is usually to remove context or start a fresh thread. Katie Parrott's writing setup grew one style guide from 759 to 3,855 words and needed 127 drafts for one essay until she cut her guides to 513 words. The proposal adds an instruction-bloat section to AI style guides and creates a training page for everyday chat users on Mike Taylor's seven context failure modes. One reason to hesitate: it adds a new training page.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Two essays from Every, eleven days apart, make the same argument for non-engineers. On 5 October 2026 staff writer Katie Parrott described how she broke a working setup. Each column she writes had its own folder with a short voice guide, a short style guide and sample drafts, read by the agent through an AGENTS.md file. In September she made three changes: log every experiment and turn any note given twice into a checklist item, link 385 files across folders in Zettelkasten style, and codify every pattern she noticed. One style guide grew to 3,855 words with eight approved openings. Drafts got worse after each correction; one essay took 127 drafts and over a million words. A review by GPT-5.6 Sol in Codex found the cause: "the concrete rules are easier to verify, so they can overwhelm the subtler ones while every checklist still passes." She archived everything and rebuilt in about 20 minutes. The new guides total 513 words, against 6,109 before, and treat drafts and notes as "evidence, never new instructions".

On 16 October Mike Taylor, Every's head of evals and author of a book on context engineering, adapted Drew Breunig's list of long-context failures for chat users. Taylor's seven: distraction (earlier examples narrow new answers), confusion (irrelevant details steer the reply), neglect (material in the middle of long input is overlooked), drift (early instructions fade), clash (a brief fed in over several turns gets worse results; he cites a 39% drop), poisoning (an earlier mistake keeps returning) and underspecification (missing details produce generic answers). Each comes with a sign to watch for and a fix. He keeps memory off and opens a fresh thread for every task.

### What changes
The wiki mentions context rot only for coding agents, and its AI style guides page (dated March) says to codify taste and iterate from failures, with no warning about guides that grow too long.

- **AI style guides** gains a guidance bullet, an "Instruction bloat" section with Parrott's case and her three rebuild principles, and a failure mode. It gets its first Recent-changes section, with one entry. Page date moves to 5 October.
- New page `training/chat-context-management.md` for everyday chat users: the seven failure modes, each with its sign and fix, plus the habit of starting fresh with a handoff.
- **Index** gains the new page and updates the AI style guides line; the training count moves from 20 to 21.
- Two new source pages, one per essay. The two weekly recaps get none.

### What to weigh
The wiki's vocabulary hub assigns "context engineering" to the Harness concept page, which is already over its length warning, so this practical guidance goes to a training page instead of a concept page. The two essays address different readers: Parrott's is about writing guides, Taylor's about chat threads in general. They are therefore split across two pages rather than merged into one.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-style-guides.md` — one Current-guidance bullet, new "Instruction bloat" section, one failure mode, new Recent-changes section with one entry dated 2026-10-05, Related line, as_of 2026-03-19 → 2026-10-05, append source

- [ ] **Create** `wiki/training/chat-context-management.md` — new training page for everyday chat users

- [ ] **Update** `wiki/index.md` — add the new page, refresh the ai-style-guides line, training count 20 → 21

- [ ] **Create** `wiki/sources/newsletters/every-instruction-bloat-parrott-2026-10-05.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-context-engineering-start-over-2026-10-16.md` — source summary

## Page drafts

### wiki/training/ai-style-guides.md (updated)

Frontmatter:

```
as_of: 2026-10-05
sources: [how-to-build-an-ai-style-guide, every-instruction-bloat-parrott-2026-10-05]
```

`## Current guidance` — append one bullet:

```
- Keep the guide short and descriptive ("often, not always"); before adding a rule, ask whether it belongs in every task or only the one in front of you
```

New section, inserted after `## Proven patterns` and before `## Failure modes`:

```
## Instruction bloat

Turning taste into instructions has a limit. Every staff writer Katie Parrott (October 2026) grew one column's style guide from about 759 to 3,855 words, with eight approved openings, six endings and two checklists, after telling her agent to log every experiment, turn any note given twice into a checklist item, and cross-link 385 files across folders. Every draft got worse after each correction; one essay took 127 drafts. A model review found the mechanism: concrete, checkable rules ("open with one of these eight approaches") are easier for an agent to verify than judgment rules ("let one experience carry the piece"), so they crowd the judgment out while every checklist passes. She archived the old context and rebuilt it from scratch, cutting her guides from 6,109 words to 513, under three principles:

- **The agent asks first.** Nothing enters the style guide, voice guide or drafts folder without approval.
- **Every folder stands alone.** No links into other projects; the agent reads only the folder it is working in.
- **The guides stay short.** They describe what a good piece "often (not always)" does; drafts, notes and reviews are "task material or evidence, never new instructions."

When an "improved" setup starts producing worse drafts, remove something before adding more.
```

`## Failure modes` — append one bullet:

```
- Codifying every correction into the guide until checkable rules crowd out judgment, so drafts get worse with each round of feedback
```

New sections at the end of the page, before `## Sources`:

```
## Related

- [Managing chat context](chat-context-management.md) — the same over-context problem in everyday chat threads, with signs to watch for and fixes

## Recent changes

- [2026-10-05] Added "Instruction bloat": Katie Parrott's 759 → 3,855-word style guide, why checkable rules crowd out judgment, and her three rebuild principles (guides cut from 6,109 to 513 words).
```

`## Sources` — append:

```
- [Every — When Trying to Make AI Better Makes It Worse](../sources/newsletters/every-instruction-bloat-parrott-2026-10-05.md)
```

### wiki/training/chat-context-management.md (new)

```
---
title: Managing chat context
type: training
as_of: 2026-10-16
sources: [every-context-engineering-start-over-2026-10-16, every-instruction-bloat-parrott-2026-10-05]
---

# Managing chat context

For everyday users of Claude, ChatGPT and similar chat apps. Everything in a conversation, plus memory and custom instructions, shapes the next answer, and models are poor at deciding that earlier material no longer applies. Output does not announce that a thread has gone bad; it just gets worse. Managing chat context means choosing what the model sees: context engineering (see [Harness](../concepts/harness.md)) done by hand, one thread at a time.

## Current guidance

- Start a fresh thread whenever the task changes, even within the same project.
- Put the full brief in the first message instead of feeding it in over several turns.
- Keep memory off and custom instructions minimal; one offhand preference can leak into every chat.
- When the model gets something wrong, edit your earlier message or regenerate instead of arguing in the thread.
- Before leaving a long thread, ask: "What information would have been useful to know at the start of this task that would have eliminated several steps or mistakes?" Edit the answer and paste it into the new thread's brief.
- Keep reusable context (preferences, briefs, standard procedures) in saved files you paste in or point an agent at, not in a long-running thread.

## Seven ways context goes wrong

Mike Taylor (Every, October 2026), adapted from Drew Breunig's long-context failure modes:

| Failure | Watch for | What to do |
|---|---|---|
| Distraction: earlier examples narrow new answers | You ask for a new direction and suggestions still follow the old pattern | New thread when the tone or task changes; add examples on purpose and test how many you need |
| Confusion: irrelevant details steer the reply | The model keeps raising a fact or framework unrelated to the question | Memory off, minimal custom instructions |
| Neglect: the middle of long input is overlooked | The answer skips a key detail buried among documents | Upload only what the task needs; separate threads for separate documents; task at the top |
| Drift: the original goal fades | Earlier constraints (spelling, length) slip back to defaults | Keep standing preferences in a saved note and paste them at the top of each chat |
| Clash: early assumptions conflict with later information | The model builds on a guess made before you clarified | Full brief in the first message; if you left something out, restart with the complete brief |
| Poisoning: an earlier error keeps returning | A corrected fact reappears in the next draft | Edit the message that led to the error rather than correcting it in the thread |
| Underspecification: missing detail yields a generic answer | The answer could apply to anyone | Supply your own experience and constraints; carry a handoff summary into the new thread |

Taylor's examples: adding a few "i-" names to a Steve Jobs-style naming prompt moved "i-" names from 21% to 100% of suggestions; splitting a prompt across several messages cost 39% in a Microsoft and Salesforce study; and his writer colleague's 3,855-word style guide made drafts worse until it was cut to 513 words (see [AI style guides](ai-style-guides.md)).

## Failure modes

- Treating a long thread as the place where project knowledge lives.
- Arguing with the model about a mistake, which keeps both the error and the complaint in context.
- Saving every preference to memory or custom instructions "just in case".

## Related

- [AI style guides](ai-style-guides.md) — instruction bloat in persistent writing context
- [Agent memory](../concepts/agent-memory.md) — how memory systems decide what to keep; why stale facts resurface
- [Agent loop design](../workflows/agent-loop-design.md) — fresh-context loops as the coding-agent answer to context rot

## Recent changes

- [2026-10-16] Page created from Mike Taylor's seven context failure modes for chat users and Katie Parrott's instruction-bloat case.

## Sources

- [Every — Context Engineering Is Knowing When to Start Over](../sources/newsletters/every-context-engineering-start-over-2026-10-16.md)
- [Every — When Trying to Make AI Better Makes It Worse](../sources/newsletters/every-instruction-bloat-parrott-2026-10-05.md)
```

### wiki/index.md (updated)

Replace the `training/ai-style-guides` line:

```
- [training/ai-style-guides](training/ai-style-guides.md) — how to externalize editorial taste and anti-patterns so AI writing stops drifting generic, and how to keep guides short so checkable rules don't crowd out judgment *(as_of: 2026-10-05)*
```

Insert after it:

```
- [training/chat-context-management](training/chat-context-management.md) — for everyday chat users: seven ways context goes wrong (distraction to underspecification), signs to watch for, and when to start a fresh thread *(as_of: 2026-10-16)*
```

Page count: `- training: 20` → `- training: 21`.

### wiki/sources/newsletters/every-instruction-bloat-parrott-2026-10-05.md (new)

```
---
title: 'Every — When Trying to Make AI Better Makes It Worse'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-05-when-trying-to-make-ai-better-makes-it-worse.md
published: 2026-10-05
ingested: 2026-10-20
domains: [training]
---

# Every — When Trying to Make AI Better Makes It Worse

Katie Parrott's Working Overtime column on how she degraded a working AI writing setup by adding logs, cross-links and codified rules, and how she rebuilt it. A Context Window recap on 11 October (`raw/newsletters/2026-10-11-one-agent-for-the-whole-company.md`) summarizes the essay and adds nothing new.

## Influenced pages

- [AI style guides](../../training/ai-style-guides.md) — "Instruction bloat" section, guidance bullet, failure mode
- [Managing chat context](../../training/chat-context-management.md) — example of over-context

## Key claims extracted

- Setup: one folder per column with a voice guide, a style guide and drafts, read via AGENTS.md; a Command Center folder above them
- Three changes in September: durable record of every experiment and "repeated mistakes should become review checklist items"; Zettelkasten links across 385 files; codify every pattern into the guides
- One style guide grew from ~759 to 3,855 words (eight approved openings, six endings, two checklists)
- One essay: 127 drafts, over 1 million words
- GPT-5.6 Sol diagnosis: "the concrete rules are easier to verify, so they can overwhelm the subtler ones while every checklist still passes"
- Rebuild in ~20 minutes from an empty desktop; old guides archived, not deleted; guides cut from 6,109 to 513 words
- Principles: the agent asks before writing to context files; every folder stands alone; guides stay short ("often (not always)"); drafts and notes are "task material or evidence, never new instructions"
- Personal rule: no major context decisions under pressure or right after a new model launch
```

### wiki/sources/newsletters/every-context-engineering-start-over-2026-10-16.md (new)

```
---
title: 'Every — Context Engineering Is Knowing When to Start Over'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-16-context-engineering-is-knowing-when-to-start-over.md
published: 2026-10-16
ingested: 2026-10-20
domains: [training]
---

# Every — Context Engineering Is Knowing When to Start Over

Mike Taylor (Every's head of evals, author of O'Reilly's *Context Engineering with DSPy*) adapts Drew Breunig's long-context failure modes for everyday chat users: seven ways context goes wrong, each with a sign to watch for and a fix. A Context Window recap on 18 October (`raw/newsletters/2026-10-18-codexs-comeback-up-close.md`) summarizes the essay and adds nothing new.

## Influenced pages

- [Managing chat context](../../training/chat-context-management.md) — page created from this essay

## Key claims extracted

- Taylor keeps memory off in Claude and ChatGPT and opens a fresh thread for every task
- Seven failure modes: distraction, confusion, neglect, drift, clash, poisoning, underspecification
- Distraction: adding "i-" examples moved "i-" product names from 21% to 100% of suggestions
- Confusion: a GitHub-COO persona used a favorite framework in 5 of 12 answers; the real person never mentioned it
- Neglect: "Lost in the Middle" (Liu et al.); a bug report at position six of nine documents was ignored
- Clash: splitting prompts into step-by-step messages gave 39% worse results across models (Microsoft and Salesforce research)
- Poisoning: Gemini 2.5 spent 100+ turns hunting a nonexistent Pokémon item; fix by editing the earlier message, not arguing
- Underspecification: closing prompt "What information would have been useful to know at the start of this task…?" carried into a new thread as a handoff
- Long-term fix: keep the best context in local files the agent reads as needed
```

## Schema / vocabulary additions

None.

## Open questions

- Should the chat-context guidance get its own page (as drafted), or go onto an existing page? No current training page is written for everyday chat users; the closest alternative is folding the table into AI style guides, which would give that page a second audience.
