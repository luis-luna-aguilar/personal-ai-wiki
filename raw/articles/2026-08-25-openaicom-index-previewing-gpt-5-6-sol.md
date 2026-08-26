---
title: "Previewing GPT-5.6 Sol: a next-generation model"
type: source
source_type: article
url: https://openai.com/index/previewing-gpt-5-6-sol/
fetched: 2026-08-25
note: "Initial fetch via scripts/fetch_url.py was blocked by a Cloudflare JS challenge; content below was retrieved via the aside-browser skill fallback (real browser render, accessibility-tree extraction)."
---

# Previewing GPT-5.6 Sol: a next-generation model

Published: June 26, 2026 (Product / Release)

We're beginning a limited preview of the GPT-5.6 series: Sol, our flagship model; Terra, a balanced model for everyday work; and Luna, a fast and affordable model. Terra has competitive performance to GPT-5.5 while being 2x cheaper and Luna brings strong capability at our lowest cost.

GPT-5.6 Sol launches with our most robust safety stack to date. We strengthened protections for higher-risk activity, sensitive cyber requests, and repeated misuse, and spent multiple weeks finding weaknesses, pressure-testing our system, and hardening it against real-world attacks.

We believe in broad access, and we plan to make GPT-5.6 Sol, Terra, and Luna generally available in the coming weeks. As part of our ongoing engagement with the U.S. government, we previewed our plans and the models' capabilities ahead of today's launch. At their request, we are starting with a limited preview for a small group of trusted partners whose participation has been shared with the government, before releasing more broadly. During this preview, we will continue testing and coordinating closely with partners as we work toward broader availability. We don't believe this kind of government access process should become the long-term default. It keeps the best tools from users, developers, enterprises, cyber defenders, and global partners who need them. We are taking this short-term step because we believe it is the strongest path to broader availability in the coming weeks, while we work with the Administration to develop the cyber Executive Order framework and a repeatable process for future model releases.

## Capabilities

GPT-5.6 Sol is our strongest model yet. To give a preview of model performance, we share a set of evaluations highlighting improved agentic capabilities in coding, biology, and cybersecurity, with additional safety and preparedness evaluations available in our system card. We will share an expanded suite of evaluation results when we make the model broadly available.

With GPT-5.6, we're introducing a new `max` reasoning effort to give Sol the most time to reason deeply. Additionally, we're introducing a new `ultra` mode that goes beyond the capabilities of a single agent by leveraging subagents to accelerate complex work.

For coding workflows, GPT-5.6 Sol sets a new state of the art on Terminal-Bench 2.1, which tests command-line workflows requiring planning, iteration, and tool coordination. [Chart compares GPT-5.6 Sol Ultra, GPT-5.6 Sol, Claude Mythos 5, GPT-5.6 Terra, Claude Fable 5, GPT-5.5, GPT-5.6 Luna, Claude Opus 4.8, and Gemini 3.1 Pro Preview; scores cluster roughly between 71% and 92% — exact per-model score pairing could not be reliably reconstructed from the flattened chart text extracted via accessibility tree, so specific numbers are not attributed to specific models here.]

GPT-5.6 Sol also shows broad improvements in biology workflows. On GeneBench v1, which evaluates long-horizon genomics and quantitative-biology analyses, it achieves stronger results than GPT-5.5 while using fewer tokens.

GPT-5.6 Sol is our most capable model yet for cybersecurity. It shifts the performance-efficiency frontier for long-horizon security tasks including vulnerability research and exploitation. On ExploitBench, GPT-5.6 Sol is competitive with Mythos Preview using only ~1/3 of the output tokens. On ExploitGym, a benchmark created by UC Berkeley researchers in collaboration with OpenAI and other frontier labs, GPT-5.6 Sol, Terra, and Luna models all demonstrate strong improvements in cyber capabilities as reasoning increases.

## Stronger cyber capabilities with stronger safeguards

GPT-5.6 Sol, Terra and Luna were developed with the most robust safeguards to date, with configurations matched to each model's capabilities. Safeguards are designed to increasingly hold up to real-world adversarial pressure while preserving access to legitimate work (code review, vulnerability research, patch development, debugging, security education, defensive testing). GPT-5.6 Sol is better at helping people find and fix vulnerabilities than reliably carrying out end-to-end attacks.

GPT-5.6 Sol does **not** cross the Cyber Critical threshold under OpenAI's Preparedness Framework. In evaluations involving Chromium and Firefox, it identified bugs and exploitation primitives but did not autonomously produce a functional full-chain exploit under the conditions tested.

## A layered safeguard stack

Layered safeguards include: model-level training to refuse prohibited cyber assistance (including jailbreak/disguised-intent attempts); real-time cyber and biology misuse classifiers that can pause generation for a larger reasoning model to review; account-level review across conversations and risk signals for flagged activity; and differentiated access. OpenAI is also working with enterprise customers on privacy-preserving detection, customer-operated safety controls, and risk-calibrated access.

## Improving robustness with automated red-teaming

OpenAI dedicated over 700,000 A100-equivalent GPU hours to automated red-teaming aimed at finding universal jailbreaks (attacks generalizing across many prompts/contexts), plus extensive third-party human expert red-teaming continuing through the preview period. A rapid-response process reproduces, assesses, prioritizes, and remediates newly discovered jailbreaks.

## Availability and pricing

During the preview, GPT-5.6 models are initially available through the API and Codex to a select group of trusted partners and organizations, with broader availability to ChatGPT, Codex, and API users planned soon. The new naming: the number identifies the model generation, while Sol/Terra/Luna identify durable capability tiers that can advance on their own cadence.

Pricing per 1M tokens: **Sol** $5 input / $30 output; **Terra** $2.50 input / $15 output; **Luna** $1 input / $6 output. GPT-5.6 introduces more predictable prompt caching (explicit cache breakpoints, 30-minute minimum cache life); cache writes billed at 1.25x the uncached input rate, cache reads keep the 90% cached-input discount.

GPT-5.6 Sol is also launching on Cerebras at up to 750 tokens/second in July, initially limited to select customers.

---

**Note (added at fetch time, 2026-08-25):** this is OpenAI's original June 26, 2026 restricted-preview announcement. It does not itself state that the government-requested access restriction was later lifted — that claim comes from later newsletter coverage (see `raw/newsletters/2026-07-09-chatgpt-voice-gets-more-human-like.md`, which links to this same URL while describing GPT-5.6 as "rolling out publicly after the US Commerce Department ended a weeks-long restriction"). Corroborating signal found on this same page's "Keep reading" module: a linked OpenAI post dated Aug 24, 2026 ("Advancing price-performance for developers with GPT-5.6 in Kiro") shows GPT-5.6 already integrated into a third-party product by that date, consistent with a broader public launch having occurred sometime between the June 26 restricted preview and August 2026.
