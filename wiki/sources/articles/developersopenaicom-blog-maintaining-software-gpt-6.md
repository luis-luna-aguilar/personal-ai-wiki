---
title: "OpenAI Developers — Maintaining software with the GPT-6 family"
type: source
source_type: article
source_file: raw/articles/2026-10-19-developersopenaicom-blog-maintaining-software-with-the-gpt-6.md
url: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family
ingested: 2026-10-19
domains: [coding, models]
---

# OpenAI Developers — Maintaining software with the GPT-6 family

An engineer on OpenAI's Core Experimentation team describes using GPT-6 Astra and GPT-6.1 Sol in Codex for codebase maintenance: removing dead code, cleaning up stale experiments and feature flags, fixing flaky tests and cutting CI time. Astra handled short, ambiguous prompts that GPT-5.6 Sol could not, gathering evidence from PRs, Slack, trackers and production profiling and explaining each deletion. A side-by-side audit found GPT-6.1 Sol Ultra nearly matching Astra Ultra at a fraction of the cost. The post closes with a start-small, review, then expand recipe. No publication date in the post; ingest date used.

## Influenced pages

- [GPT-6 Astra](../../models/gpt-6-astra.md) — maintenance results in Codex, comparison with GPT-6.1 Sol
- [Codex](../../tools/codex.md) — maintenance-pass usage pattern
- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — OpenAI maintenance case study
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — agent-driven maintenance pattern
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — model/effort cost-per-finding comparison

## Key claims extracted

- GPT-6 Astra worked from a broad, ambiguous dead-code prompt that GPT-5.6 Sol could not handle completely
- Five engineers, part-time over two weeks, merged 1,400+ PRs deleting 800k+ lines; one container image shrank from 3.31GB to 1.72GB (48%); ~400 visual snapshot variants removed
- Stale-experiment cleanup removed hundreds of experiments and feature flags; one "Permanent" Statsig flag mapped to all features was escalated for review, and removing it saved ~0.42% CPU in the main affected service
- Stale-experiment audit (6,000+ files, 1M+ lines): Astra Ultra 142 findings / $109.06; GPT-6.1 Sol Ultra 131 / $15.12; GPT-6.1 Sol Medium 86 / $5.27; Sol Ultra = 92% of findings at 14% of cost
- Sol's misses were mostly constant flags used as dependencies of other flags; prompt corrections close the gap and should be revisited with new models
- ~30 CI optimization PRs: median CI from ~10 to 4.5 min, p90 from 12.5 to 6 min; one missing mock cut a 63-test suite from 592.6s to 29.8s
- Some proposals added more complexity than their benefit, so prioritization and measurement remained necessary
