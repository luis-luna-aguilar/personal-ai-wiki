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
