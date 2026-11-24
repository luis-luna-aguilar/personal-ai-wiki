---
title: 'Anthropic — Using Claude Code: Spending your effort'
type: source
source_type: article
source_file: raw/articles/2026-10-20-claudedev-blog-spending-your-effort.md
url: https://claude.dev/blog/spending-your-effort/
published: 2026-09-25
ingested: 2026-10-20
domains: [coding, models]
---

# Anthropic — Using Claude Code: Spending your effort

Thariq Shihipar (Anthropic, Claude Code) explains what the effort setting does and when to use each level, from his own runs of the same tasks at several levels on Opus 5.5 and a pass through every Terminal-Bench 3.0 result for Fable 5.1, Opus 5 and Fable 5. His conclusion: effort mainly changes how much verification and edge-case testing Claude does and how many judgment calls it makes on its own, so it pays off on edge-case-heavy work (security, hardware, code review) and matters little once a detailed spec is given. The same text was posted as an X Article (`raw/tweets/2026-09-25-trq212-2103576349499855160.md`); this page covers both.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — effort rule of thumb added to the middle-tier FinOps control
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — Terminal-Bench evidence bullet
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — spec → implement low/medium → verify high loop

## Key claims extracted

- Effort approximates how much compute the user wants spent; higher effort means more independent verification and judgment calls
- Underspecified build ("fitness tracker app"): low 1.5 min (log plus graph) vs max 67 min (much richer app); with a detailed spec from an interview, levels converge (16 to 79 min, similar designs)
- Terminal-Bench 3.0, Fable 5.1, 370 attempts per level: passes 140 at low (median 73k tokens) vs 214 at max (median 222k); "missed a case" failures 59 → 24; "made the wrong call" 133 → 107
- Pass rate low → top effort by area (Fable 5.1): security 64% → 87%, hardware 34% → 75%, ML 54% → 73%, science 41% → 61%, software 43% → 56%, media 18% → 30%, operations 12% → 22%
- Worked examples: `html-js-filter` 1/5 at low → 5/5 at xhigh (Fable 5.1); `mvcc-lsm-compaction` 0/5 → 4/5, `cli-2ph-simplex` 0/5 → 5/5, `gsea-proteomics` 0/5 → 4/5 (Opus 5.5)
- Rule of thumb: low for in-the-loop brainstorming and easy changes; medium for most feature work; high for verification-heavy work such as brownfield bugs; max for fully autonomous hard problems such as security audits
- Recommended loop: spec plus interview, implement at low effort, review, verify and test at high effort
- Numbers are internal runs, 5 attempts per task, production safety interventions off for Fable 5.1, security tasks without internet; they will not match the public leaderboard
