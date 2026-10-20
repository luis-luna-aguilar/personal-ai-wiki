---
type: proposal
source: raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Computer use is "180 degrees different" (Ari Weinstein, OpenAI)

## Summary

### In short
Computer use stopped being a screenshot-and-click loop: agents now read accessibility trees and the DOM, write code that performs many actions at once, and recover from their own errors, which makes them faster than the average person on many tasks. OpenAI's computer-use lead says GPT-6.1 Sol costs about a seventh of Astra for this work, and that the most useful application is agents testing the software they just built. The proposal updates State of Computer Use, Codex and Harness vs model, and adds one source page. One scope choice to note: only the computer-use half of the episode is ingested.
[[#Open questions|Open questions: none.]]

### The source
On 2026-09-30, at OpenAI DevDay, Latent Space interviewed Ari Weinstein, the Sky co-founder who now leads computer use at OpenAI, in response to Dwarkesh Patel's claim that computer use had stalled. Weinstein says it is now "180 degrees different". A year ago, agents could start a task reliably but stalled when something went wrong. Now they debug, retry and check what is and isn't working. Agents also no longer look only at pixels. They combine screenshots, the accessibility tree (the structured description of an interface that screen readers use), the page's DOM and Playwright. In Codex they often write JavaScript that performs several actions in a single step, so they no longer have to scroll and re-screenshot over and over. App Shots, triggered by pressing Command twice, send an app's full accessibility representation into Codex or ChatGPT instead of an image.

He says computer use is now faster than the average person in most cases. The next goal is to be "literally superhuman", faster than expert users. Much of the remaining time goes to waiting for websites to load. GPT-6.1 Sol costs about a fifth of Astra in general and about a seventh for computer use. Computer use is now part of the Agents API. OpenAI trains its models on its own computer-use harness, so he suggests developers who use that "in-distribution" harness may get better speed, cost and accuracy. He says OpenAI's measured gains come sometimes from the model and sometimes from the harness. His favorite use is having the agent test the software it just built, so the human no longer acts as QA for the agent.

### What changes
The wiki's Codex leader line on the computer-use dashboard still relies on July newsletter coverage of office tasks. Harness vs model has no computer-use example.

- **State of Computer Use**: the Codex leader line is rewritten around the new approach: code-writing actions, accessibility trees and App Shots, faster-than-human claims, Agents API availability, and self-testing. The page gains one Recent-changes entry. The list is at its cap of 10, so the oldest 5 May entry (Amazon Quick) moves to history. The page date stays 14 October.
- **Codex** gains one Recent-changes entry on App Shots, code-writing computer use and Sol's cost. The oldest entry (10 May, jxnl usage patterns) moves to history. The page date stays 19 October.
- **Harness vs model** gains one paragraph: OpenAI attributes its computer-use gains to both model and harness, and recommends the harness its models were trained on. The page date moves to 30 September.
- New source page `wiki/sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md`, covering only the computer-use half of the episode.

### What to weigh
Scope: the second half of this episode (Nikunj Handa on the Decisions API, async tool calling and compaction) is left out. The source page is limited to the computer-use story, so a later proposal can create a separate page for the API half from the same newsletter. Muse for Mac computer use, also mentioned in the triage signal, belongs with the Meta Connect story and is not covered here.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/computer-use.md` — rewrite the Codex leader line; adds one Recent-changes entry dated 2026-09-30; adds source id and Sources link; `as_of` stays 2026-10-14
    > **Before:** `- [Codex](../tools/codex.md) — OpenAI; increasingly positioned as a horizontal computer-work agent for documents, spreadsheets, slides, browser flows, research, planning, inbox/CRM cleanup, meeting-note workflows, and connected workplace apps; current evidence remains newsletter synthesis *(as of 2026-07-01)*`
    > **After:** see draft below

- [ ] **Spill** `wiki/state-of/computer-use.md` → `wiki/history/state-of/computer-use.md` — the list is at 10, so the oldest-dated entry (2026-05-05 Amazon Quick) moves to history

- [ ] **Update** `wiki/tools/codex.md` — adds one Recent-changes entry dated 2026-09-30; adds source id and Sources link; `as_of` stays 2026-10-19

- [ ] **Spill** `wiki/tools/codex.md` → `wiki/history/tools/codex.md` — the list is at 10, so the oldest entry (2026-05-10 jxnl usage patterns) moves to history

- [ ] **Update** `wiki/concepts/harness-vs-model.md` — one new paragraph in Current status; adds one Recent-changes entry dated 2026-09-30; `as_of` 2026-09-09 → 2026-09-30; adds source id and Sources link

- [ ] **Create** `wiki/sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md` — source summary (computer-use story only)

## Page drafts

### wiki/state-of/computer-use.md (updated)

Frontmatter: append `weinstein-computer-use-180-degrees-2026-09-30` to `sources:`. `as_of` unchanged (2026-10-14).

Codex leader line under `### Computer use` (replaces the existing line):

```
- [Codex](../tools/codex.md) — OpenAI; horizontal computer-work agent across documents, browser flows, and connected workplace apps. OpenAI's computer-use lead says agents now combine screenshots, accessibility trees, DOM, and Playwright, write code that performs many actions per step, and recover from failures, making them faster than the average person on many tasks; computer use is also in the Agents API *(as of 2026-09-30)*
```

`## Recent changes`: insert one entry at the top, then drop the bottom entry (`[2026-05-05] Amazon Quick (caveated)…`) into history:

```
- [2026-09-30] OpenAI's Ari Weinstein calls computer use "180 degrees different" from a year ago: self-debugging agents, multi-modal input (accessibility trees, DOM, App Shots), code-writing multi-action steps, GPT-6.1 Sol at ~1/7 of Astra's computer-use cost, and agents testing the software they build.
```

`## Sources`: append

```
- [Ari Weinstein: computer use is "180 degrees different"](../sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md)
```

### wiki/history/state-of/computer-use.md (updated)

Append:

```
## Archived from current page on <apply date>

- [2026-05-05] Amazon Quick (caveated): desktop work-context assistant building personal knowledge graph from files/calendar/Slack, integrating with Kiro CLI and Claude Code; secondary coverage only — pending primary Amazon verification
```

### wiki/tools/codex.md (updated)

Frontmatter: append `weinstein-computer-use-180-degrees-2026-09-30` to `sources:`. `as_of` unchanged (2026-10-19).

`## Recent changes`: insert in date order (after the 2026-10-19 entry, before 2026-08-12), then drop the bottom entry (`[2026-05-10] Codex-maxxing usage patterns (jxnl)…`) into history:

```
- [2026-09-30] Computer use in Codex now writes JavaScript that performs many actions per step and reads accessibility trees and the DOM instead of only screenshots; App Shots (double Command press) bring an app's full accessibility representation into a chat. OpenAI says GPT-6.1 Sol runs computer use at ~1/7 of Astra's cost, and the same implementation is now in the Agents API.
```

`## Sources`: append

```
- [Ari Weinstein: computer use is "180 degrees different"](../sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md)
```

### wiki/history/tools/codex.md (updated)

Append:

```
## Archived from current page on <apply date>

- [2026-05-10] Codex-maxxing usage patterns (jxnl): durable threads, Heartbeats (thread-local scheduling), Goals with verification criteria, memory as files (vault + AGENTS.md), $browser/@chrome/@computer, side panel as live work surface
```

### wiki/concepts/harness-vs-model.md (updated)

Frontmatter: `as_of: 2026-09-30`; append `weinstein-computer-use-180-degrees-2026-09-30` to `sources:`.

Heading becomes `## Current status (as of 2026-09-30)`. Insert this paragraph after the paragraph ending "…than by the underlying model.":

```
Computer use shows the same split from inside a lab. OpenAI's computer-use lead says the past year's gains came "sometimes in the harness and sometimes in the model": the harness side gave agents richer inputs (accessibility trees, the DOM, Playwright) and let them write code that performs many actions in a single step, removing the old screenshot-scroll-screenshot loop. Because OpenAI trains its models on its own computer-use harness, he suggests developers who build on that in-distribution harness through the Agents API may get speed, cost, and accuracy advantages over a custom one. This is model-harness fit from the vendor's side.
```

`## Recent changes`: insert at top

```
- [2026-09-30] Added OpenAI's computer-use account: gains split between model and harness (accessibility trees, DOM, code-writing multi-action steps), and the case for the in-distribution harness in the Agents API.
```

`## Sources`: append

```
- [Ari Weinstein: computer use is "180 degrees different"](../sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md)
```

### wiki/sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md (new)

```
---
title: 'Ari Weinstein: computer use is "180 degrees different"'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
url: https://www.latent.space/p/devday-2026
published: 2026-09-30
ingested: 2026-10-20
domains: [computer-use, agents]
---

# Ari Weinstein: computer use is "180 degrees different"

Latent Space's DevDay 2026 episode, first half: OpenAI's computer-use lead Ari Weinstein (Sky co-founder) rebuts the claim that computer use has stalled. Agents now debug and recover instead of stalling, combine several views of the screen, and write code that performs many actions at once. Covers only the computer-use half; the API half (Nikunj Handa: Decisions API, async tool calling, compaction) is not summarized here.

## Influenced pages

- [State of Computer Use](../../state-of/computer-use.md) — Codex leader line, Recent changes
- [Codex](../../tools/codex.md) — App Shots, code-writing computer use, Sol cost
- [Harness vs model](../../concepts/harness-vs-model.md) — model/harness split in computer-use gains; in-distribution harness

## Key claims extracted

- Biggest change in the past year: agents debug, retry, and introspect instead of stalling after a good start
- Agents combine screenshots, accessibility trees, the DOM, and Playwright; in Codex they often write JavaScript that performs many actions per step
- App Shots (press Command twice) bring an app's full, token-efficient accessibility representation into Codex or ChatGPT instead of a screenshot
- Computer use is now faster than the average human in most cases; the next frontier is "literally superhuman" speed. Much of the remaining latency is waiting for websites to load
- GPT-6.1 Sol: about 1/5 of GPT-6 Astra's cost generally and about 1/7 for computer use
- Computer use is now in the Agents API; OpenAI trains on its own harness, so the in-distribution harness may be faster, cheaper, and more accurate than a custom one
- Favorite use case: agents testing the software they just built, closing the build-test loop so the human is no longer QA
- Gains come "sometimes in the harness and sometimes in the model"
```

## Schema / vocabulary additions

None.

## Open questions

None.
