---
title: "Spotify Engineering — AI Changed How Spotify Builds. What We Learned (and Fixed) About Quality at Higher Velocity"
type: source
source_type: article
source_file: raw/articles/2026-10-20-tco-gpjtdwz0tt.md
url: https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity
published: 2026-09-30
ingested: 2026-10-20
domains: [coding]
---

# Spotify Engineering — AI Changed How Spotify Builds

Spotify's review of software quality during its AI ramp-up: four strained areas (content processing, fleet-wide automated changes, compute scarcity and failover, mobile release quality), what its incident and PR data show about AI-authored code, and the delivery-system fixes it made. The URL places it in September 2026; the day is unknown, so `published:` uses the month's last day. Found via a 2026-10-14 tweet by Shubham Mishra that adds nothing beyond the link.

## Influenced pages

- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — Spotify case bullet
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — delivery-system quality measurement pattern
- [Agentic infrastructure operations](../../training/agentic-infrastructure-operations.md) — automated dependency-upgrade failure and fixes

## Key claims extracted

- ~3,000 production services, 777M MAU, 11–12M backend requests/s; 500K+ new media items processed daily
- Incident retrospectives: AI-authored code not identified as a material direct contributor; "the volume of change increased faster than some of our verification controls could adapt"
- Merged changes more than doubled YoY in August (~8,100 → 17,000); quality/optimization 27% → 31% of mix; maintenance/configuration 31% → 25%
- Rebuilt rework-rate metric (weights age of code changed) shows no rise, while FAROS 2026 reports a sharp industry rise in code churn
- PR size and code complexity creeping up; thresholds deliberately not rewritten
- Fleet Management: most automated changes auto-merge after safety checks; agentic Java migration across backend services in three days; one automated dependency upgrade passed checks and failed in production → stronger safeguards, rollback capacity, changes scheduled in owners' working hours
- AI-driven industry compute scarcity made regional failovers user-visible; reserved edge capacity doubled after a May incident
- Content pipeline (June 24 incident): end-to-end monitoring, scheduler fix, batch jobs deprioritized, service tiering reworked
- Mobile: broadened quality signals with longer-term trends
- Conclusion: AI increased capacity to produce change; the next constraint is the ability to verify it
