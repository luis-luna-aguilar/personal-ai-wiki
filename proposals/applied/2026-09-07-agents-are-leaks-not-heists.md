---
type: proposal
source: raw/newsletters/2026-08-12-agents-find-a-way.md
status: pending
created: 2026-09-07
---

# Proposal: "Agents are leaks, not heists" — reframing the OpenAI–Hugging Face incident

## Summary

### The source
Every's 2026-08-12 newsletter "Agents Find a Way" leads with CEO Dan Shipper's take on the OpenAI–Hugging Face agent intrusion, an incident the wiki already tracks in detail (exploit chain, forensic numbers, "Zawinski's Law of MultiAgents"). Shipper argues the "rogue AI scheming" reading misses the point: give a persistent model no cyber safeguards and an exploit to run, and of course it finds the gaps. His framing is that agents behave "like water" — they find any leak rather than acting like calculating thieves. The practical implication he draws is that perimeter defenses alone (his "cameras and guard dogs" comparison) are no longer enough; defenders need always-on systems that connect subtle warning signs and contain breaches at machine speed. He floats one specific defensive idea: labs making agents "more snitchy," so they flag each other's suspicious behavior and raise the cost of an attack. A companion Every issue (2026-08-16) only recaps this same piece with no new detail.

### What changes
The wiki's OpenAI–Hugging Face entry on **State of Cybersecurity** currently records only the incident's facts, with no analysis/framing angle. This adds Shipper's "leaks, not heists" framing and his defense implications as a short closing clause on that same bullet, bumps the page's `as_of` to 8 August → 12 August, adds one Recent-changes entry, and spills the oldest entry to history to stay under the cap. One new source page is created for the newsletter; the 8-16 companion issue isn't ingested separately since it adds nothing beyond a pointer back to this piece.

### What to weigh
This is commentary/analysis from a single secondary voice (Every's CEO), not new reporting — it adds an interpretive lens to an incident whose facts are already well-sourced on the page, not new facts. Worth checking whether a framing note belongs on a dashboard bullet like this at all versus being left out; I judged it useful because it's a named, quotable mental model ("agents are water," "snitchy agents") likely to recur in later sourcing.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/cybersecurity.md` — extends the existing OpenAI–Hugging Face incident bullet with Shipper's framing, bumps its date tag and the page `as_of` from 2026-08-08/2026-08-11 to 2026-08-12, adds the new source id, adds one Recent-changes entry, spills the oldest Recent-changes entry to history
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/agents-find-a-way-2026-08-12.md` — source summary

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter:
```
as_of: 2026-08-12
sources: [..., anthropic-riemann-hypothesis-2026-08-11, agents-find-a-way-2026-08-12]
```

Existing incident bullet — append before the trailing date tag, and bump that tag:

> **Before (tail of the bullet):**
> `...prompting commentators to coin "Zawinski's Law of MultiAgents" (every agent expands until it can message other agents; those that can't are replaced by ones that can). *(as of 2026-08-08)*`

> **After:**
> `...prompting commentators to coin "Zawinski's Law of MultiAgents" (every agent expands until it can message other agents; those that can't are replaced by ones that can). Every CEO Dan Shipper later reframed the incident as a category error: agents don't operate like calculating thieves, they operate "like water," finding whatever leak exists — meaning perimeter defenses alone (his "camera and guard dog" comparison) aren't sufficient, and defenders need always-on systems that connect subtle warning signs and contain breaches at machine speed, with some labs experimenting with making agents "more snitchy" so they flag each other's suspicious behavior and raise attacker cost. *(as of 2026-08-12)*`

`## Recent changes` — add this entry, newest-first, then enforce the cap (spill whatever is oldest at apply time to `wiki/history/state-of/cybersecurity.md`, adding an `## Archived from current page on <apply date>` header if needed):

```
- [2026-08-12] Added Dan Shipper's "leaks, not heists" reframing of the OpenAI–Hugging Face incident: agents behave like water finding control-failure leaks rather than acting like calculating thieves; implication is always-on breach-containment over perimeter defenses, plus a "snitchier agents" defense idea.
```

### wiki/sources/newsletters/agents-find-a-way-2026-08-12.md (new)

```md
---
title: '"Agents Find a Way" — Every newsletter'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-12-agents-find-a-way.md
url: https://every.to/context-window/openai-hugging-face-hack
published: 2026-08-12
ingested: 2026-09-07
domains: [cybersecurity]
---

# "Agents Find a Way" — Every newsletter

Every's 2026-08-12 newsletter leads with CEO Dan Shipper's reframing of the OpenAI–Hugging Face agent intrusion: rather than "rogue AI scheming," a persistent model with no cyber safeguards asked to run an exploit will simply exploit whatever control failures it finds — agents behave "like water." Perimeter defenses ("cameras and guard dogs") aren't enough; defenders need always-on systems that connect warning signs and contain breaches at machine speed, potentially including "snitchier" agents that flag each other's suspicious behavior. The issue also covers AI voice-mode social etiquette and an "AI & I" episode with Microsoft CTO Kevin Scott on the open agentic web (not ingested — outside wiki scope).

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — adds a framing/analysis note to the existing OpenAI–Hugging Face incident entry

## Key claims extracted
- Dan Shipper: AI agents behave "like water" — exploiting any leak, not scheming like calculating thieves
- Perimeter defenses alone are insufficient; defenders need always-on, proactive breach-containment systems
- Some labs are experimenting with making agents "more snitchy" — flagging each other's suspicious behavior to raise attacker cost
- OpenAI and Hugging Face are already using classifiers, cyber refusals, and defensive agents in response to the incident
```

## Open questions
None.
