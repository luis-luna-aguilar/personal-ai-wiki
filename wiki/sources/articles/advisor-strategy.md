---
title: The advisor strategy — Claude blog
type: source
source_type: article
source_file: raw/articles/2026-04-09-claudecom-blog-the-advisor-strategy.md
url: https://claude.com/blog/the-advisor-strategy
ingested: 2026-04-09
domains: [agents]
---

# The advisor strategy — Claude blog

Anthropic announces the "advisor strategy" — pairing Opus (advisor) with Sonnet or Haiku (executor) inside a single agentic task — and ships the `advisor_20260301` server-side tool on the Claude API to make it a one-line API change. Positioning post plus API feature launch, with vendor eval numbers attached.

## Influenced pages

- [[workflows/advisor-strategy]] — new page, main subject of the ingest
- [[state-of/agents]] — new `model-orchestration` subcategory created; advisor strategy placed under it

## Key claims extracted

- Executor (Sonnet or Haiku) runs the agentic loop end-to-end — calls tools, reads results, iterates. The advisor (Opus) is consulted only when the executor hits a decision it can't reasonably solve.
- The advisor returns a plan, a correction, or a stop signal. It does *not* call tools and does *not* produce user-facing output.
- Inverts the common sub-agent pattern where a larger orchestrator decomposes work for smaller workers.
- New server-side tool `advisor_20260301`. Declared in a Messages API request alongside other tools, with `model`, `name`, `max_uses`. Executor decides when to invoke it. Handoff stays inside a single `/v1/messages` call — no extra round-trips, no caller-side context management.
- Advisor typically returns 400–700 text tokens.
- Billing: executor tokens at executor rate, advisor tokens at advisor rate; each reported separately in the `usage` block.
- `max_uses` is the only built-in cap on advisor calls per request.
- **Sonnet + Opus advisor** vs Sonnet alone on SWE-bench Multilingual: +2.7 percentage points in score, −11.9% cost per agentic task.
- **Haiku + Opus advisor** on BrowseComp: 41.2% vs Haiku solo 19.7% — more than double.
- **Haiku + Opus advisor** vs Sonnet solo: trails by 29 points in score, costs 85% less per task. Framed as a strong option for high-volume tasks.
- Also reports gains on BrowseComp and Terminal-Bench 2.0 for Sonnet+Opus-advisor, without specific numbers for those combinations.
- Works alongside other server-side tools (web search, code execution) in the same loop.

## Caveats

- All numbers are from Anthropic's own internal evals on their own models. No independent replication.
- The post references three footnote markers (SWE-bench Multilingual, BrowseComp, Terminal-Bench 2.0). The footnote bodies were not captured in the raw extract.
