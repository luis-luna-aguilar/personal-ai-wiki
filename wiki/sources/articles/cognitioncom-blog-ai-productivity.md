---
title: Estimating the Productivity of an Autonomous AI Software Engineer
type: source
source_type: article
source_file: raw/articles/2026-07-14-cognitioncom-blog-ai-productivity.md
url: https://cognition.com/blog/ai-productivity
ingested: 2026-07-14
domains: [coding, agents]
---

# Estimating the Productivity of an Autonomous AI Software Engineer

Cognition built an automated system that reviews each completed Devin session, classifies whether it produced useful work, and estimates the equivalent human-engineering hours saved — crediting only work the user hadn't already specified and conservatively assuming the reference engineer already has relevant expertise. Trained and validated on 258 self-reported sessions from 126 users (233 held-out for evaluation), the estimator reaches `r_log = 0.74`, calibrated to deliberately underestimate rather than overestimate. Cognition positions this as the first automated system measuring AI engineering productivity in production, and compares it favorably to Anthropic's ticket-text-only approach (`r_log = 0.46`) while noting METR's smaller, more homogeneous internal sample scored higher (`r_log = 0.83`). No explicit publish date was visible in the fetched content; using ingest date as `as_of` fallback per the date rule.

## Influenced pages

- [Devin](../../tools/devin.md) — productivity estimator feature
- [Agent evals](../../concepts/agent-evals.md) — new Human-hours-equivalent productivity estimation section
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — evidence from practice

## Key claims extracted

- Estimator classifies session usefulness (merged-PR filter plus a classifier for non-PR sessions), then predicts human-engineer-hours-equivalent.
- Design principles: reason about the human's likely path (not the agent's actual trajectory), credit only work the user hadn't already specified, account for codebase familiarity, assume relevant expertise (conservative).
- Dataset: 258 sessions / 126 users across enterprise customers; 233 held-out evaluation sessions.
- `r_log = 0.74` on held-out data; calibrated via log-space regression (`h = 2.28 × m^0.923`, ~2.08x multiplicative correction); reports the unadjusted, deliberately conservative total.
- Compares to METR (`r_log = 0.83`, 34 sessions, 7 internal staff) and Anthropic (`r_log = 0.46`, 1,000 Jira tickets, text-only, no execution trace).
- Threats to validity: self-reported ground truth (interview bias), sampling skew toward engaged users, hours ≠ business value, hours don't capture post-merge defects/quality.
- Now running in production with customers.
