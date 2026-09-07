---
title: "AINews — Codex usage growth, coding-agent cost/perf tradeoffs, and Devin Fusion"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-14-ainews-codex-usage-up-10x-in-6-months-to-7m-use.md
url: https://www.latent.space/p/ainews-codex-usage-up-10x-in-6-months
published: 2026-07-14
ingested: 2026-09-06
domains: [training, agents, coding]
---

# AINews — Codex usage growth, coding-agent cost/perf tradeoffs, and Devin Fusion

AINews' July 14 issue leads with Codex's reported usage growth (roughly 10x year-to-date to 6-7M users) and also includes a "Coding Agents, Harness Design, and Cost-Per-Task Competition" section reporting that benchmarks are shifting from token price to cost per task.

## Influenced pages

- [Codex](../../tools/codex.md) — usage-growth estimate and its sourcing chain, plus OpenAI's rollout-friction fixes
- [Devin](../../tools/devin.md) — added the delegation-efficiency mechanism (81% no-edit statistic) behind Devin Fusion's cost advantage on Fable 5
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — added as corroborating detail in the eval-data-as-moat evidence bullet

## Key claims extracted

- GPT-5.6 launched July 9; a July 12 tweet reported 6M Codex/ChatGPT-Work users in the prior 48 hours; a follow-up ~24.5 hours later reported 7M
- Fidji Simo's March disclosure put Codex at 2M users, implying roughly 550K-700K users on January 1 — used to derive an approximate 10x year-to-date growth estimate
- Claude Code's last public figure is ~2M weekly active users and $2.5B ARR, reported in February; Anthropic has not published a comparably recent number, possibly because coding usage has shifted partly to Claude Tag/Slack surfaces with different, harder-to-compare usage statistics
- OpenAI's Thibault Sottiaux described several fixes for GPT-5.6 Sol in ChatGPT Work/Codex: ~10% more usage from inference optimizations, a context-limit rollback from 372K to 272K after billing/usage side effects, reversion of some experimental reasoning-effort ("juice") changes, and fixes for overactive multi-agent spawning at high/xhigh settings
- skirano built a coding-agent index explorer and found Terra Max slightly ahead of Fable 5 Max on score for materially lower cost
- Cognition reported that Devin Fusion now uses Fable 5, and that it can be lower cost per task than Opus 4.8 because stronger delegation and judgment reduce unnecessary work
- imjaredz highlighted the key stat: in 81% of Fable-led runs, the lead model never makes a code edit, implying expensive models can be cheaper when they avoid wasted actions
- Separately in the same section: harnesses are increasingly described as "the app" (threepointone), LangChain argues task-specialized harnesses beat generic wrappers, and Artificial Analysis emphasizes cost-per-task over token pricing as the more meaningful long-horizon metric
