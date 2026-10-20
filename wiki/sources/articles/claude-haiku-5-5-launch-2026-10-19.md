---
title: Claude Haiku 5.5 launch
type: source
source_type: article
source_file: raw/articles/2026-10-19-anthropiccom-claude-haiku-5-5.md
url: https://www.anthropic.com/claude-haiku-5-5
ingested: 2026-10-19
domains: [models]
---

# Claude Haiku 5.5 launch

Anthropic's launch page for Claude Haiku 5.5 presents it as its cheapest, fastest and most capable small model, built for high-volume, cost-sensitive tasks and subagent roles under Opus 5.5 and Sonnet 5.5. It includes a benchmark table against Haiku 4.5, GPT-6 Luna and Sonnet 5.5, two-tier pricing split at 100k-token prompts, quotes from six launch customers, and safety notes. The same page announces a Sonnet 5.5 cache-read price cut, monthly API credits for Max and Team subscribers, and computer-use and browser-use support in the Claude SDKs. The page carries no publication date; the fetch date (2026-10-19) is used.

## Influenced pages
- [Claude Haiku 5.5](../../models/claude-haiku-5-5.md) — new page: benchmarks, pricing, effort control, availability, safety
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — cache-read price cut to $0.10 per 1M tokens
- [State of Models](../../state-of/models.md) — new Small / fast models section
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — Anthropic tier split and Cognition sidekick result

## Key claims extracted
- Haiku 5.5 is available on all platforms (AWS, Google Cloud, Microsoft Azure) and on the Claude Platform as `claude-haiku-5-5`.
- It costs around 75% less to run than Haiku 4.5 on average. Per 1M tokens, for prompts up to / over 100k: input $0.10 / $0.50, output $0.50 / $2.50, cache writes $0.125 / $0.625, cache reads $0.01 / $0.05. Prompts up to 100k made up around 90% of requests to Haiku 4.5.
- Benchmarks (Haiku 5.5 / Haiku 4.5 / GPT-6 Luna / Sonnet 5.5): GDPval-AA v2.1 1620 / 735 / 1437 / 1840; AA-Briefcase v1.1 1578 / 614 / 1336 / 1824; OSWorld 2.1 offline subset 72.4% / 15.7% / 48.9% / 83.9%; HLE no tools 45.9% / 10.2% / — / 56.9%, with tools 57.4% / 18.7% / — / 64.5%; Terminal-Bench 4.0 39.2% / 0.0% / 16.4% / 70.6%; FrontierCode 1.1 (Main) 46.4% / — / 42.4% / 52.1% (xhigh); Chartography 46.4% / 6.4% / 29.1% / 61.6%.
- It is the first Haiku-class model with an adjustable effort setting.
- Anthropic says Sonnet 5.5 and Opus 5.5 remain the better choices for complex agentic coding. Haiku suits narrowly scoped tasks such as compaction, summarization and subagent work.
- Customer reports: Asana saw over 30% lower task latency and up to 2.5x faster inference per agent turn; HubSpot got 92.8% on its CRM suite, the best score it has seen; AlphaSense got 0.84 against 0.76 for Haiku 4.5 on 400 document-QA queries; Box saw +11 points over Haiku 4.5 at about half the latency; Cognition's Devin Fusion holds FrontierCode 66.2 with Haiku 5.5 as sidekick under Opus 5.5.
- Safety: Anthropic reports large alignment gains over Haiku 4.5. Cyber safeguards are stricter than Haiku 4.5's but looser than recent larger models', and penetration testing is still blocked. Biology safeguards match Sonnet 5, Sonnet 5.5 and Opus 5.
- Sonnet 5.5 cache reads cut 50%, from $0.20 to $0.10 per 1M tokens, which Anthropic says makes Sonnet 5.5 around 20% cheaper on most agentic tasks.
- New monthly API credits on the Claude Platform: $100 for Max 5x, $200 for Max 20x, and up to $500 pooled for Team.
- The Claude Python and TypeScript SDKs add computer-use and browser-use support in beta.
