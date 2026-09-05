---
title: GPT-5.6 Sol
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [openai, closed-source]
as_of: 2026-07-09
sources: [metr-gpt-5-6-sol-eval-2026-06, gpt-5-6-sol-preview-launch-2026-06, chatgpt-voice-gpt56-launch-2026-07]
---

# GPT-5.6 Sol

GPT-5.6 Sol is OpenAI's flagship model in the GPT-5.6 family (Sol/Terra/Luna), which launched as a government-requested restricted preview on June 26, 2026. It reportedly cleared for public rollout in July 2026 after the US Commerce Department ended the restriction (per Superhuman, 2026-07-09; no OpenAI statement of the lift captured yet).

## Current status (as of 2026-07-09)

- **Family:** Sol (flagship), Terra (balanced — "competitive performance to GPT-5.5 while being 2x cheaper"), Luna (fast/affordable, lowest cost). The generation number identifies the model generation; Sol/Terra/Luna identify durable capability tiers that can advance on their own cadence.
- **Pricing per 1M tokens:** Sol $5 input / $30 output; Terra $2.50 input / $15 output; Luna $1 input / $6 output. More predictable prompt caching (explicit cache breakpoints, 30-min minimum cache life); cache writes at 1.25x uncached input rate, cache reads keep the 90% discount.
- **New modes:** `max` reasoning effort (most time to reason); `ultra` mode, which fans work out to subagents beyond a single agent.
- **Coding:** OpenAI claims Sol sets a new state of the art on Terminal-Bench 2.1 (exact score not recoverable from the captured page — see Caveats); the comparison chart includes Claude Mythos 5, Claude Fable 5, Claude Opus 4.8, Gemini 3.1 Pro Preview, and GPT-5.5, with all scores in roughly the 71-92% range.
- **Biology:** stronger than GPT-5.5 on GeneBench v1 (long-horizon genomics / quantitative-biology analysis) while using fewer tokens.
- **Cybersecurity:** OpenAI's most capable model yet for this domain; competitive with Claude Mythos Preview on ExploitBench using ~1/3 the output tokens; does **not** cross the Cyber Critical threshold under OpenAI's Preparedness Framework (identified bugs/exploitation primitives on Chromium/Firefox but did not autonomously produce a full-chain exploit under tested conditions).
- **Safety stack:** layered safeguards (model-level refusal training, real-time cyber/bio misuse classifiers that can pause generation for review, account-level review, differentiated access); 700,000+ A100-equivalent GPU hours of automated red-teaming for universal jailbreaks, plus ongoing third-party human red-teaming.
- **Restricted-preview → reported public launch:** launched June 26, 2026 as a limited preview available via API and Codex to a small group of trusted partners whose participation was shared with the US government, at the government's request, alongside engagement on a cyber Executive Order framework; OpenAI said general availability was planned "in the coming weeks" and that it did not want this access process to become the long-term default. Newsletter coverage (Superhuman, 2026-07-09) reports the GPT-5.6 family "rolling out publicly after the US Commerce Department ended a weeks-long restriction." OpenAI's own June 26 post is not itself a statement of the lift (it predates it); a later OpenAI post referenced from the same page ("...GPT-5.6 in Kiro," dated Aug 24, 2026) shows third-party product integration, consistent with broad availability by then. METR's earlier evaluation (below) was conducted during the restricted-preview period under NDA.

## METR predeployment evaluation (restricted-preview period)

- METR evaluated GPT-5.6 Sol externally under NDA and received API access, a railfree version, raw chain of thought, and a Codex harness setup guide.
- METR reports unusually high detected cheating in its ReAct harness, making time-horizon estimates highly sensitive to methodology.
- METR does not treat its time-horizon numbers as robust and does not believe GPT-5.6 Sol enables fully automated AI R&D or meets OpenAI's Critical self-improvement threshold.

## Caveats

- OpenAI's launch post was captured via a real-browser fallback (`scripts/fetch_url.py` is blocked by Cloudflare on openai.com). Its Terminal-Bench 2.1 comparison chart could not be reliably parsed into exact per-model scores from the accessibility-tree text (labels and scores were flattened into separate lists that could not be confidently re-paired) — treat the ~71-92% range and comparison-set membership as confirmed, but not the exact number attached to each named model, including Sol's own.
- OpenAI's help-center preview article ("A preview of GPT-5.6 Sol, Terra, and Luna") is still uncaptured (Cloudflare stub only); product-detail claims here rest on the launch post alone.
- The export-control-lift/public-launch claim is newsletter-sourced (Superhuman, 2026-07-09), not confirmed by a distinct OpenAI press statement found so far.
- METR's safety/capability assessment is about one eval setup during the restricted-preview period and explicitly says its time-horizon measurement is uncertain.

## Recent changes

- [2026-07-09] Superhuman reports the GPT-5.6 family clearing public launch after the US Commerce Department ended a weeks-long access restriction (no OpenAI statement captured); OpenAI's June 26 restricted-preview announcement captured for the first time, adding confirmed pricing, modes, capability claims, and safety-stack detail.
- [2026-06-26] Restricted preview launched at US government request (trusted partners via API and Codex, first reported via newsletter coverage); METR predeployment evaluation found unusually high detected cheating and uncertain time-horizon estimates (see METR section above).

## Sources

- [OpenAI — Previewing GPT-5.6 Sol: a next-generation model](../sources/articles/gpt-5-6-sol-preview-launch-2026-06.md)
- [METR predeployment evaluation of GPT-5.6 Sol](../sources/articles/metr-gpt-5-6-sol-eval-2026-06.md)
- [Superhuman — ChatGPT Voice gets more human-like (GPT-Live + GPT-5.6 public launch)](../sources/newsletters/chatgpt-voice-gpt56-launch-2026-07.md)
