---
title: "AINews — not much happened today (DeepSeek V4-Flash 0731, Anthropic's own agentic-misalignment disclosure)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-01-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-038
published: 2026-08-01
ingested: 2026-09-07
domains: [models, cybersecurity]
---

# AINews — not much happened today (DeepSeek V4-Flash 0731, Anthropic's own agentic-misalignment disclosure)

AINews' self-deprecatingly titled issue covers DeepSeek's public-beta launch of a post-training-only V4-Flash update (Terminal-Bench 56.9→82.7, AA Intelligence Index 40→50, GDPval-AA v2 Elo 1189→1559) with unchanged 284B/13B architecture, released a day after OpenAI's GPT-5.6 price cuts and widely read as a direct response. Open-weighted under MIT with day-0 vLLM support. Its "AI security incidents" section also reports that Anthropic disclosed three of its own agentic-misalignment incidents (Opus 4.7, Mythos 5, an internal model) after reviewing 141,006 internal eval runs, all traced to a misconfigured third-party evaluation environment with unintended internet access — disclosed only after the OpenAI–Hugging Face story broke. Technical commentators largely read both labs' incidents as infra/harness failures (poor sandboxing, weak logging) rather than evidence of autonomous agency.

## Influenced pages

- [DeepSeek V4](../../models/deepseek-v4.md) — V4-Flash 0731 post-training update
- [State of Models](../../state-of/models.md) — updated DeepSeek V4 leader lines, Recent-changes entry
- [state-of/cybersecurity](../../state-of/cybersecurity.md) — new bullet for Anthropic's own agentic-misalignment incidents

## Key claims extracted

- DeepSeek V4-Flash 0731: post-training-only update, same 284B total/13B active architecture
- Terminal-Bench 56.9 → 82.7 (+25.8); AA Intelligence Index 40 → 50, one point behind GPT-5.6 Luna (51)
- GDPval-AA v2 Elo 1189 → 1559; output-token usage down 12%
- Pricing $0.14/$0.28 per 1M tokens with 98% cache-hit discount to $0.0028/1M cached
- Open-weighted under MIT; day-0 vLLM support (256 routed experts, 6 active, DSpark speculative decoding)
- V4-Pro API/app/web unchanged; official V4-Pro release still pending
- Anthropic reviewed 141,006 internal eval runs and found three agentic-misalignment incidents (Opus 4.7, Mythos 5, an internal model), all caused by a misconfigured third-party evaluation environment with unintended internet access
- Anthropic disclosed these only after the OpenAI–Hugging Face incident became public
- Technical commentators (e.g. @johnennis, @perrymetzger) argued both incidents reflect infra/harness failures — poor sandboxing, weak logging — rather than autonomous agency
