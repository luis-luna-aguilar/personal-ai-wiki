---
type: proposal
source: raw/newsletters/2026-08-20-the-wayfinder-skill-navigating-the-fog-of-war.md
status: pending
created: 2026-09-07
---

# Proposal: The /wayfinder skill — a named methodology for planning agent work under uncertainty

## Summary

### The source
Latent Space published a full interview with Matt Pocock — creator of "AI Skills for Real Engineers" (220K+ GitHub stars) and a YouTube channel with 347K subscribers — about a new skill he calls /wayfinder. Its purpose is helping a person and their agent plan a project whose end state isn't fully knowable up front — what Pocock calls navigating "the fog of war." The mechanism: a persistent "map" document holds every decision already made and a rough overview of what else is happening, while each individual working session gets only its own scoped "ticket" (grilling, prototype, research, or task type), so a child session isn't overloaded with irrelevant context. Pocock's broader argument is that skill design is really about finding precise, consistent terminology — "leading words" — so agent and human share what he calls a "ubiquitous language"; he's separately building a full AI-coding-dictionary graph to formalize this vocabulary across his courses and skills. He distinguishes /wayfinder from his existing "grill me" skill: use grill-me when a task fits in one planning session, wayfinder when it doesn't.

### What changes
The wiki's agent-skill-methodology page currently covers Perplexity's evals-first skill-writing method and SkillsBench/SWE-Skills-Bench findings on when skills help or hurt, but has no pattern yet for planning multi-session work under uncertainty.

- **Agent skill methodology** gains a new Proven-patterns entry on /wayfinder's map/ticket/session structure and the "leading words" terminology-design principle, plus a Recent-changes entry. Page date moves to 20 August.
- Its Recent-changes list is already at the 5-entry cap, so this proposal spills the oldest entry (29 June, presentation automation) into a new `wiki/history/training/agent-skill-methodology.md` file.
- New source page for the Latent Space interview.

### What to weigh
This is a single practitioner's named methodology, not an independently benchmarked pattern (unlike this page's SkillsBench/SWE-Skills-Bench content) — it's included on the strength of Pocock's credibility and the methodology's clear fit with the page's existing scope, not on empirical validation.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/training/agent-skill-methodology.md` — new Proven-patterns entry, Recent-changes entry, spill of oldest entry to history, as_of bump
    > See draft below

- [ ] **Create** `wiki/history/training/agent-skill-methodology.md` — new history file with the spilled entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/wayfinder-skill-2026-08-20.md` — source summary

## Page drafts

### wiki/training/agent-skill-methodology.md (updated)

```md
Frontmatter changes: as_of: 2026-08-20; sources: append wayfinder-skill-2026-08-20

## Proven patterns (new item, appended as #9)

**9. Split planning into a persistent map and per-session tickets for open-ended work**
When a project's end state isn't fully knowable up front (Matt Pocock calls this "the fog of war"), don't try to plan it in one session. Keep one persistent "map" document holding every decision made so far and a rough overview of what else is happening, and give each individual working session only its own scoped "ticket" — a grilling, prototype, research, or task ticket — so a child session isn't overloaded with irrelevant context. Use a single-session planning skill (e.g. "grill me") when the whole task fits in one sitting; switch to a map/ticket split once it doesn't.
- Precise, consistent terminology matters as much as the structure itself: Pocock calls this finding "leading words" so agent and human share a "ubiquitous language" — vague or inconsistently-used terms (calling everything a "ticket," or naming the same concept differently in different places) produce confused agent behavior.
- (Matt Pocock, /wayfinder, Aug 2026)

## Recent changes (new entry, prepended; existing list re-capped to 5)

- [2026-08-20] Added /wayfinder: a map/persistent-decisions + per-session-ticket pattern for planning work under uncertainty, plus "leading words"/ubiquitous-language as a terminology-design principle (Matt Pocock).
- [2026-07-16] Added SWE-Skills-Bench (distinct from SkillsBench): 49 skills tested against real repos, 39 with zero effect, average +1.2% gain, 7 real winners (up to +30%), 3 regressions (up to -10%) from version-mismatched guidance. Added a keep/retest/retire skill-audit pattern.
- [2026-07-15] Added SkillsBench findings: self-written skills score worse than no skills; short skills beat exhaustive documentation; loading every available skill underperforms a few relevant ones; skill regressions are invisible without a head-to-head comparison ("polish hides the damage").
- [2026-07-03] Vercel eve interview and Impeccable coverage reinforced skills as a current-knowledge and domain-judgment layer across agent harnesses.
- [2026-07-01] Added agent recipes as portable bundles of instructions, evals, failure history, and signal-processing logic.

<!-- The following entry moves to wiki/history/training/agent-skill-methodology.md: -->
<!-- [2026-06-29] Presentation automation added as a high-context skill example ... -->
```

### wiki/history/training/agent-skill-methodology.md (new)

```md
# Agent Skill Methodology — History

## Archived from current page on 2026-09-07

- [2026-06-29] Presentation automation added as a high-context skill example where reliable output requires supporting files, scripts, references, and review loops.
```

### wiki/sources/newsletters/wayfinder-skill-2026-08-20.md (new)

```md
---
title: "The /wayfinder Skill: Navigating the \"Fog of War\" of Planning"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-20-the-wayfinder-skill-navigating-the-fog-of-war.md
url: https://www.latent.space/p/wayfinder-skill
published: 2026-08-20
ingested: 2026-09-07
domains: [agents]
---

# The /wayfinder Skill: Navigating the "Fog of War" of Planning

Full Latent Space interview with Matt Pocock (creator of "AI Skills for Real Engineers," 220K+ GitHub stars) on /wayfinder, a skill for planning agent work whose end state isn't fully knowable up front. Splits planning into a persistent "map" and per-session "tickets"; emphasizes precise, consistent terminology ("leading words") as the core of good skill design.

## Influenced pages

- [Agent skill methodology](../../training/agent-skill-methodology.md) — new Proven-patterns entry

## Key claims extracted

- /wayfinder splits planning into a persistent "map" (decisions made, rough overview) and per-session "tickets" (grilling, prototype, research, task types)
- Distinguished from Pocock's "grill me" skill: grill-me for single-session tasks, wayfinder for multi-session/uncertain-scope work
- Core design principle: find precise, consistent "leading words" so agent and human share a "ubiquitous language"
- Pocock is separately building a full AI-coding-dictionary graph to formalize this vocabulary
```

## Open questions

None.
