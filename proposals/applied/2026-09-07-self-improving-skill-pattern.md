---
type: proposal
source: raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md
status: pending
created: 2026-09-07
---

# Proposal: Self-improving agent skills as a personal workflow habit, not just a team process

## Summary

### The source

Every's newsletter on "cloning your coworkers" describes a small, concrete habit that turns this wiki's existing "codify production failures as standing instructions" principle into something one person runs on their own workflow rather than a team-wide skill-authoring process. Every's head of operations, Arielle Shipper, works almost exclusively in Codex and keeps a "self-improve" skill on hand: whenever the agent produces a wrong or off-tone result, she feeds it feedback on what went wrong and what a better response would have looked like, then runs the skill, which reviews the failure, interrogates the cause, and proposes a targeted edit to Codex's own operating instructions so the same mistake is less likely to recur — for example, adding a rule that Codex must always re-read a Slack thread's prior messages before drafting a reply, after a mismatched-tone message. It's the same compounding mechanism behind Every's team-facing KateBench and DanLens skills (which rewrite themselves based on which suggestions get accepted or rejected), but framed here as a lightweight, single-person loop rather than infrastructure a team builds and maintains — and the skill itself is published on GitHub for others to adopt directly.

### What changes

The wiki's agent-skill-authoring page already has principle #4 ("codify production failures as standing instructions") and a numbered list of proven patterns through #9; this adds a tenth, concrete instance of that principle running as a personal habit rather than a team process.

- **Agent skill methodology** gains a new numbered proven pattern (#10) describing the self-improve-skill loop, plus a Recent-changes entry. Page date moves to 26 August. The page's Recent-changes list (6 entries) is well under its 10-entry cap, so no spill is needed.
- Reuses the Every source page already drafted by a companion proposal (the cost-normalized/open-weight-opening proposal) for this same raw file, rather than creating a duplicate.

### What to weigh

This is a single named individual's personal workflow habit at one company, not a benchmarked or widely-adopted practice — it's included because it's a clean, concrete instance of an existing principle rather than because it's independently validated at scale.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/training/agent-skill-methodology.md` — add proven pattern #10, Recent-changes entry, bump as_of
    > See draft below

## Page drafts

### wiki/training/agent-skill-methodology.md (updated)

> **Frontmatter:** `as_of: 2026-08-20` → `as_of: 2026-08-26`; append `every-cloning-your-coworkers-2026-08-26` to `sources:`.

> New numbered pattern appended to `## Proven patterns`:

```md
**10. Run a personal self-improve loop, not just a team skill library**
Every's head of operations, Arielle Shipper, keeps a standing "self-improve" skill for her own Codex workflow: whenever the agent produces a wrong or off-tone result, she feeds it feedback on what went wrong and what a better response would have looked like, then runs the skill — which reviews the failure, interrogates the cause, and proposes a targeted edit to Codex's own operating instructions so the mistake is less likely to repeat (e.g. "always re-read prior thread messages before drafting a Slack reply"). This is the same compounding mechanism behind team-facing skills like Every's KateBench/DanLens (which rewrite themselves based on which suggestions get accepted or rejected), scaled down to something one person runs on their own workflow rather than infrastructure a team builds and maintains.
- (Arielle Shipper, Every, Aug 2026 — skill published on GitHub)
```

> **Recent changes:** add as the newest entry:
```md
- [2026-08-26] Added a personal self-improve-skill pattern (Arielle Shipper, Every): feed the agent feedback on a mistake, then run a skill that proposes a targeted edit to the agent's own operating instructions — the same compounding mechanism as team-facing skills, run by one person on their own workflow.
```

> **Sources** (append):
```md
- [Every — The Case for Cloning Your Coworkers](../sources/newsletters/every-cloning-your-coworkers-2026-08-26.md)
```

## Open questions

- None beyond the scope note above.
