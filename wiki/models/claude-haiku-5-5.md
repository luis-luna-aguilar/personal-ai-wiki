---
title: Claude Haiku 5.5
type: model
domains: [models]
subcategory: small-model
tags: [anthropic]
as_of: 2026-10-10
sources: [claude-haiku-5-5-launch-2026-10-19, ainews-claude-haiku-5-5-2026-10-08, ainews-haiku-5-5-vals-cost-per-test-2026-10-08, ainews-haiku-5-5-arena-webdev-2026-10-10]
---

# Claude Haiku 5.5

Anthropic's smallest, fastest and cheapest current Claude model, launched 2026-10-07 at GPT-6 Luna's token price, built for high-volume, cost-sensitive work: summaries, context compaction, database queries, classification, live customer support, browser use, and subagent roles under [Opus 5.5](claude-opus-5-5.md) or [Sonnet 5.5](claude-sonnet-5-5.md).

## Current status (as of 2026-10-10)

- Available on the Claude Platform as `claude-haiku-5-5`, and on AWS, Google Cloud and Microsoft Azure.
- First Haiku-class model with an adjustable effort setting (Low through Max).
- Pricing per 1M tokens, prompts up to / over 100k tokens: input $0.10 / $0.50, output $0.50 / $2.50, cache writes $0.125 / $0.625, cache reads $0.01 / $0.05 (Haiku 4.5: $1.00 / $5.00 / $1.25 / $0.10). Anthropic says it costs around 75% less than Haiku 4.5 on average, and that prompts up to 100k made up about 90% of Haiku 4.5 requests.
- Launch benchmarks (Haiku 5.5 / Haiku 4.5 / GPT-6 Luna / Sonnet 5.5): GDPval-AA v2.1 1620 / 735 / 1437 / 1840; AA-Briefcase v1.1 1578 / 614 / 1336 / 1824; OSWorld 2.1 offline subset 72.4% / 15.7% / 48.9% / 83.9%; Humanity's Last Exam 45.9% no tools, 57.4% with tools (Sonnet 5.5: 56.9% / 64.5%); Terminal-Bench 4.0 39.2% / 0.0% / 16.4% / 70.6%; FrontierCode 1.1 (Main) 46.4% / — / 42.4% / 52.1% (xhigh); Chartography 46.4% / 6.4% / 29.1% / 61.6% (no tools).
- Anthropic says Sonnet 5.5 and Opus 5.5 remain the better choice for complex agentic coding. Haiku 5.5 targets narrowly scoped tasks that were previously too expensive to run on Claude.
- 1M-token context window (Haiku 4.5: 200k); text and image input.

## Independent evals and token use

- **Ahead of Luna on capability.** Artificial Analysis: Intelligence Index 43 at max effort, ahead of GLM-5.3 Flash (42), Gemini 3.8 Flash (41) and GPT-6 Luna (38), 13 points behind Sonnet 5.5. Lower hallucination than its peers (40% against Luna's 77%), partly because it more often says it doesn't know. Vals: 90.4% on Vibe Code Bench (#3); #16 on the Vals Index. Arena WebDev 1587, 257 above Haiku 4.5 and six above Luna at the same price.
- **Below Anthropic's own numbers in places.** AA measures Terminal-Bench 4.0 at 33% (Anthropic: 39.2%). AutomationBench came in at 35%, against 53–60% for Luna and other small models, depressed by a pre-release over-refusal bug Anthropic is fixing; AA will re-run it.
- **Heavy token use.** At max effort it writes about 162k output tokens per AA index task, roughly 3x Luna, and going from xhigh to max adds 2 points for about 1.8x the tokens. Vals finds it takes many more steps (59 against Haiku 4.5's 17 on legal research) and so costs more per test than Haiku 4.5 on every shared benchmark, despite the lower token price. Set effort deliberately and measure cost per task.

## Evidence from early users

- Cognition: with Haiku 5.5 as the "sidekick" under an Opus 5.5 lead, Devin Fusion holds a FrontierCode score of 66.2 while cutting cost and latency.
- AlphaSense: on 400 document-QA queries (a workload of about 8M calls a week), Haiku 5.5 scored 0.84 against Haiku 4.5's 0.76.

## Safety

- Anthropic reports far fewer misaligned behaviors than Haiku 4.5 and a lower willingness to cooperate with misuse.
- Its cyber safeguards are stricter than Haiku 4.5's but looser than recent larger models'. They allow more defensive tasks than Sonnet 5.5's safeguards and still block penetration testing. Its biology safeguards match those of Sonnet 5, Sonnet 5.5 and Opus 5.

## Related

- [Advisor strategy](../workflows/advisor-strategy.md) — the cheap-executor / expensive-advisor pattern Haiku is pitched for.
- [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) — where Haiku fits in a routing ladder.

## Recent changes

- [2026-10-10] Independent evals added: AA Intelligence Index 43 (ahead of GPT-6 Luna's 38), Terminal-Bench 4.0 33% against Anthropic's 39.2%, and heavy token use that makes it costlier per test than Haiku 4.5 on Vals.
- [2026-10-07] Launched: about 75% cheaper than Haiku 4.5, first Haiku with effort control, large benchmark gains over Haiku 4.5.

## Sources

- [Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
- [AINews — Claude Haiku 5.5 launch and Artificial Analysis evals](../sources/newsletters/ainews-claude-haiku-5-5-2026-10-08.md)
- [AINews — Haiku 5.5 on Vals and Arena](../sources/newsletters/ainews-haiku-5-5-vals-cost-per-test-2026-10-08.md)
- [AINews — Haiku 5.5 Arena WebDev rank](../sources/newsletters/ainews-haiku-5-5-arena-webdev-2026-10-10.md)
