---
type: proposal
source: raw/newsletters/2026-09-01-prs-not-welcome-how-top-ai-open-source-projects-a.md
status: pending
created: 2026-09-09
---

# Proposal: "Software factories" — top AI-native OSS projects close PRs by default

## Summary

### The source

Latent Space's Swyx reports that several prominent AI-native open-source projects have stopped accepting human-written pull requests, routing incoming contributions through their own agent pipelines instead. Vercel's AI SDK (20M+ weekly npm downloads) built a "software factory" — separate agents that reproduce a bug, implement a fix, and review it, with a human merging at the end — and four weeks after deployment it authors 25–35% of merged PRs and closes 70–80% of issues; Vercel engineer Lars Grammel explains the logic as trusting a specific, proven agent configuration more than an unknown community contributor. Astro creator Fred Schott built a similar auto-triage system that, after years of an unmanageable issue backlog, let the team treat triage as a routine weekly task rather than a constant losing battle — and it directly led him to build a new agent framework, Flue, which goes further: every external pull request is automatically closed and converted into an issue or discussion instead of being reviewed as code. tldraw (50,000 GitHub stars) does the same, a policy founder Steve Ruiz first announced in January and reiterated five months later. Both Ruiz and Ghostty creator/HashiCorp co-founder Mitchell Hashimoto argue this is where large open-source projects are generally heading: once well-specified issues can be implemented by an agent, a human PR carries less value than the issue that specifies it — so community contribution increasingly narrows to reporting, discussion, and perspective rather than code.

### What changes

- **Agentic orchestration patterns** gains a new named pattern — PRs closed by default, software factories instead — with concrete production numbers from three named projects, sitting alongside the page's existing (more abstract) "software factory loop" pattern. The list is already at its 10-entry Recent-changes cap, so the oldest entry spills to history.
- **Flue** gains a new section on its contributor policy (auto-closes external PRs, converts them to issues/discussions) — a concrete detail the page didn't previously cover.

### What to weigh

This is a single-source proposal (one Latent Space feature); the production numbers (Vercel's 25–35%/70–80% figures, Astro's backlog turnaround) are Vercel's and Schott's own self-reported claims relayed through the article, not independently audited. Nothing else here requires a judgment call.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add the "PRs closed by default" pattern and a `## Where these patterns surfaced` line; add 1 Recent-changes entry (list is at the 10-entry cap, so the oldest entry spills to `wiki/history/workflows/agentic-orchestration-patterns.md`)
    > See draft below

- [ ] **Update** `wiki/tools/flue.md` — add a contribution-policy section; add 1 Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-pr-not-welcome-2026-09-01.md` — source summary

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Insert this new bullet directly after the existing `**Software factory loop.**` bullet under `## Current patterns`:

```md
- **PRs closed by default, software factories instead.** Several AI-native OSS projects now auto-close external human pull requests rather than reviewing them as code, routing incoming issues through their own agent pipelines instead: Vercel's AI SDK factory (20M+ weekly npm downloads) authors 25-35% of merged PRs and closes 70-80% of issues, four weeks after deployment; Astro's auto-triage system reversed years of unmanageable issue backlog into a routine weekly task; [Flue](../tools/flue.md) goes further, auto-converting every external PR into an issue or discussion. The framing from tldraw's Steve Ruiz and Ghostty's Mitchell Hashimoto: once agents can implement a well-specified issue, a human PR is no longer more valuable than the issue that specifies it — so large OSS projects increasingly limit community contribution to reporting, discussion, and perspective rather than code.
```

Add this line under `## Where these patterns surfaced`:

```md
- Latent Space's "PRs Not Welcome" feature documents three production software factories (Vercel AI SDK, Astro/Flue, tldraw) that closed PRs to humans and routed contributions through their own agents instead.
```

Recent changes — add this entry at the top (list is at the 10-entry cap; the oldest entry, `[2026-06-24] Token-tightening coverage adds AI FinOps controls...`, spills to `wiki/history/workflows/agentic-orchestration-patterns.md`):

```md
- [2026-09-01] Added the "PRs closed by default" software-factory pattern with three named production examples (Vercel AI SDK, Astro/Flue, tldraw) and their concrete PR/issue-closure numbers.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `latent-space-pr-not-welcome-2026-09-01`.

### wiki/tools/flue.md (updated)

Insert this new section directly after `## Weaknesses / caveats` and before `## Recent changes`:

```md
## Contribution policy (as of 2026-09-01)

Flue auto-closes external pull requests and converts them into issues or discussions instead — Schott's contributor guide frames this as preventing "drive-by AI slop PRs" while still channeling community input through discussion. Once a direction is decided in the issue or discussion, agents are deployed for research, design, implementation, and initial review. A concrete instance of the "PRs closed by default" pattern — see [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md).
```

Recent changes — add this entry at the top:

```md
- [2026-09-01] Contribution policy detailed: Flue auto-closes external PRs, converting them into issues/discussions instead; agents handle research, design, implementation, and initial review once a direction is chosen.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `latent-space-pr-not-welcome-2026-09-01`.

### wiki/sources/newsletters/latent-space-pr-not-welcome-2026-09-01.md (new)

```md
---
title: "PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of Contributors"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-01-prs-not-welcome-how-top-ai-open-source-projects-a.md
url: https://www.latent.space/p/pr-not-welcome
published: 2026-09-01
ingested: 2026-09-09
domains: [coding, agents]
---

# PRs NOT Welcome — Latent Space

Latent Space reports that Vercel's AI SDK, Astro/Flue (Fred Schott), and tldraw (Steve Ruiz) have all stopped accepting external human pull requests, routing incoming contributions through their own agent pipelines instead — with concrete production numbers from Vercel and Astro, and commentary from Ghostty's Mitchell Hashimoto arguing this is where large OSS projects are generally heading.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — new "PRs closed by default" pattern
- [Flue](../../tools/flue.md) — contribution-policy update

## Key claims extracted

- Vercel's AI SDK software factory (20M+ weekly npm downloads) authors 25-35% of merged PRs and closes 70-80% of issues, four weeks after deployment
- Astro's auto-triage system reversed a multi-year unmanageable issue backlog into a routine weekly task, per creator Fred Schott
- Flue auto-closes every external PR, converting it into an issue or discussion instead
- tldraw (50,000 GitHub stars) auto-closes external PRs; founder Steve Ruiz first announced the policy in January, reiterated it five months later
- Ghostty creator/HashiCorp co-founder Mitchell Hashimoto: "the future is that large open source projects will close contributions completely"
```

## Open questions

- The software factory pattern deserves a page of its own.
