---
type: proposal
source: raw/tweets/2026-09-09-dhravyashah-2081987040468517186.md
status: pending
created: 2026-09-09
---

# Proposal: Dhravya Shah — "How to Build Your Company Brain in 5 Minutes" (2026-07-28)

## Summary

### The source

On July 28, 2026, Dhravya Shah — founder of Supermemory, self-described as "the memory/context guy" — published an X Article (114,825 views, 926 likes) arguing that "every company will have a company brain, whether they believe it or not," then walks through Supermemory's own packaged version of one. The pitch: invite a Supermemory bot into a company's Slack, and it backfills up to three months of channel history plus whatever tools get connected, learning how the team works and talks. From there it answers cross-functional questions — sales, engineering, HR, research — can tag other bots to execute work, and supports scheduled automations such as a daily brief of urgent issues, all runnable from DMs or channels. A companion plugin carries the same accumulated knowledge outside Slack into Claude Code, Codex, and other tools. The post quotes Supermemory's own launch tweet (619K views) for the product pitch. This is a positioning shift worth noting on its own: the wiki has tracked Supermemory only as an [agent memory](../wiki/concepts/agent-memory.md) library (its ASMR extraction system) — this article is the company repackaging that same underlying tech as a full organization-scope system, the same move Lovable made in August and Cloudflare made in September.

### What changes

[Company brain](../wiki/concepts/company-brain.md) currently names two large production examples (Lovable's capabilities pivot, Cloudflare OS) beyond the 9-implementation survey. This proposal adds a third, dated earlier than both (July 28, so it slots in first chronologically): Supermemory Company Brain, described above. The intro sentence's count word is incremented by one to match. [Knowledge architectures](../wiki/concepts/knowledge-architectures.md) gets "Supermemory Company Brain" appended to the Company brain row's tracked-examples cell, alongside a one-line Recent-changes note; Supermemory stays listed on the Agent memory row too, since the underlying memory-layer product this new bot is built on is still that. Neither page's `as_of` moves, since both already carry a newer claim (2026-09-07). One new source page is created.

### What to weigh

This is entirely vendor self-report: the founder's own promotional X Article, quoting the company's own launch tweet, with no independent verification of adoption, accuracy, or how the Slack bot actually performs in practice. The drafts below flag this explicitly rather than presenting Supermemory's claims at the same evidentiary weight as Lovable's or Cloudflare's own engineering write-ups.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/company-brain.md` — add Supermemory Company Brain as a third production example (chronologically first), increment the intro count word, append the source id, add one Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — append "Supermemory Company Brain" to the Company brain row's Examples-tracked cell, append the source id, add one Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/tweets/dhravyashah-supermemory-company-brain-2026-07-28.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/concepts/company-brain.md (updated)

Frontmatter: append `dhravyashah-supermemory-company-brain-2026-07-28` to `sources:`. `as_of` unchanged (2026-09-07 is newer than this source's 2026-07-28).

Change:

```
Two larger production examples show the pattern scaling into full platforms rather than personal tools:
```

to (word incremented by one from whatever the live page reads at apply time — currently "Two"):

```
Three larger production examples show the pattern scaling into full platforms rather than personal tools:
```

Insert this bullet first in the list (before the Lovable bullet, since July 28 predates both existing examples):

```md
- **Supermemory Company Brain (July 2026):** Supermemory — until now tracked here only via its underlying [agent memory](agent-memory.md) tech — packaged a full company-brain product: invite its bot into a Slack workspace and it backfills up to three months of channel history plus whatever tools get connected, then answers sales/engineering/HR/research questions, tags other bots to execute work, and runs scheduled automations (e.g. a daily priority brief); a companion plugin carries the same knowledge outside Slack into Claude Code, Codex, and other tools. Vendor self-report via the founder's own X Article — no independent verification.
```

Add to `## Recent changes` (placed after the existing 2026-09-07 entry, since this source predates it):

```
- [2026-07-28] Added Supermemory Company Brain as a third production example: a Slack-resident bot built on Supermemory's agent-memory tech, with cross-tool (Claude Code/Codex) access and scheduled automations. Vendor self-report via the founder's X Article, no independent verification.
```

Add to `## Sources`:

```
- [Dhravya Shah on X — How to Build Your Company Brain in 5 Minutes](../sources/tweets/dhravyashah-supermemory-company-brain-2026-07-28.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter: append `dhravyashah-supermemory-company-brain-2026-07-28` to `sources:`. `as_of` unchanged (2026-09-07 is newer than this source).

In the `## Canonical pages` table, change the Company brain row's Examples-tracked cell from:

```
GBrain, Slite Agent, Gorgias Cortex, Lovable capabilities, Cloudflare OS
```

to:

```
GBrain, Slite Agent, Gorgias Cortex, Lovable capabilities, Cloudflare OS, Supermemory Company Brain
```

Add to `## Recent changes`:

```
- [2026-07-28] Added Supermemory Company Brain to the Company brain row's tracked examples, mirroring the new production example on that page.
```

### wiki/sources/tweets/dhravyashah-supermemory-company-brain-2026-07-28.md (new)

```md
---
title: Dhravya Shah on X — How to Build Your Company Brain in 5 Minutes
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-dhravyashah-2081987040468517186.md
url: https://x.com/dhravyashah/status/2081987040468517186
published: 2026-07-28
ingested: 2026-09-09
domains: [agents]
---

# Dhravya Shah on X — How to Build Your Company Brain in 5 Minutes

X Article (114,825 views, 926 likes) by Dhravya Shah, founder of Supermemory, arguing "every company will have a company brain" and walking through Supermemory's own packaged version of one: invite its bot into Slack, it backfills up to three months of channel history and any connected tools, then answers cross-functional questions (sales, engineering, HR, research), delegates work to other bots, and runs scheduled automations such as a daily priority brief. A companion plugin extends the same knowledge outside Slack into Claude Code, Codex, and other tools. Quotes Supermemory's own launch post (619K views) for the product pitch. Self-published by the vendor's founder — no independent verification of adoption or accuracy claims.

## Influenced pages
- [Company brain](../../concepts/company-brain.md) — added as a third production example, alongside Lovable's capabilities pivot and Cloudflare OS
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — added to the Company brain row's tracked examples

## Key claims extracted
- Supermemory launched a packaged "company brain" product: a Slack bot that backfills ~3 months of channel history plus connected tools
- The bot can answer sales/engineering/HR/research questions and tag other bots to execute tasks
- Supports scheduled automations (e.g., a daily brief of urgent issues)
- A companion plugin carries the same knowledge into Claude Code, Codex, and other outside-Slack tools
- Positions the product against Supermemory's previous "memory layer" framing, now selling the full org-scope system
```
