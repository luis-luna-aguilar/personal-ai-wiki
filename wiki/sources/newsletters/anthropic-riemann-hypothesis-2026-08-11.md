---
title: AINews — Anthropic's Riemann Hypothesis bound improvement
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
url: https://www.latent.space/p/ainews-muse-glimmer-and-spark-open
published: 2026-08-11
ingested: 2026-09-07
domains: [science]
---

# AINews — Anthropic's Riemann Hypothesis bound improvement

AINews recap of an Anthropic announcement: an unreleased internal research Claude variant, tasked with the Riemann Hypothesis, improved a longstanding lower bound on the proportion of non-trivial zeta-function zeros proven to lie on the critical line, from 41.6% to 67.2%, via large-scale retries and exploration (~31M output tokens per commentary from Jarred Sumner). Framed by engineers as AI-assisted theorem search/proof iteration, not a solved conjecture; not yet independently verified by outside mathematicians. The same issue covers Muse Glimmer, GPT-5.6-Cyber, Claude Sonnet 5's permanent pricing, and a Composio harness bake-off, each covered by separate proposals.

## Influenced pages

- [trends/ai-in-science](../../trends/ai-in-science.md) — originally added as a new Current-status bullet and Recent-changes entry (second pure-math autoresearch signal alongside OpenAI's Erdős disproof); this content later moved to AI in Mathematics
- [trends/ai-in-mathematics](../../trends/ai-in-mathematics.md) — new page; primary source for the Riemann Hypothesis bound entry
- [state-of/cybersecurity](../../state-of/cybersecurity.md) — OpenAI Daybreak bullet extended with the GPT-5.6-Cyber launch
- [trends/restricted-frontier-deployment](../../trends/restricted-frontier-deployment.md) — resolution of the Astra capability-threshold-gating section
- [models/claude-sonnet-5](../../models/claude-sonnet-5.md) — pricing bullet updated to reflect permanent $2/$10 pricing
- [concepts/harness](../../concepts/harness.md) — Composio DeepSeek V4 Flash four-harness bake-off
- [models/muse-glimmer](../../models/muse-glimmer.md) — new page: full launch details and benchmarks
- [models/muse-spark](../../models/muse-spark.md) — sibling-release pointer, Spark 1.2 open-weights promise
- [trends/open-weight-momentum-broadens](../../trends/open-weight-momentum-broadens.md) — new Current-signal bullet and Recent-changes entry

## Key claims extracted

- Unreleased Anthropic research Claude variant did not solve the Riemann Hypothesis
- Improved the proven lower bound of zeta zeros on the critical line from 41.6% to 67.2%
- Reached via repeated retries and large-scale exploration over ~31M output tokens
- Engineers and observers (including mathematician @jdlichtman) characterized it as theorem-search progress, not conjecture resolution
- OpenAI launched GPT-5.6-Cyber on 2026-08-11 under an expanded Daybreak initiative
- GPT-5.6-Cyber access restricted to "approved defenders," with extra controls/monitoring for higher-risk tasks
- Cited real-world use: previously-unknown bugs found in open-source software and in Chrome V8
- Claude Sonnet 5 API pricing ($2/M input, $10/M output) is now permanent, not introductory
- The previously announced Claude Sonnet 5 step-up to $3/M input, $15/M output will not happen
- Move read as competitive pressure from open and semi-open-weight models
- Composio ran DeepSeek V4 Flash through four agent harnesses on the same 30 agentic tasks; Pi Agent was both the cheapest and the best-performing of the four
- Muse Glimmer: 30B dense, multimodal, Apache 2.0, released 2026-08-11
- Logit-distilled from Muse Spark; trained from the outset on agentic traces (not a conventional base-then-post-train release)
- ~20GB at 4-bit quantization (~60GB BF16), DFlash speculative-decoding drafter, 128K context
- Artificial Analysis Intelligence Index 35 (behind Qwen3.6-27B's 38, near Kimi K2.5's 36); Openness Index 44
- Weaker on hallucination/knowledge calibration and general agentic knowledge work vs. similarly-sized peers
- Muse Spark 1.2's own weights promised "soon" per Alexandr Wang
