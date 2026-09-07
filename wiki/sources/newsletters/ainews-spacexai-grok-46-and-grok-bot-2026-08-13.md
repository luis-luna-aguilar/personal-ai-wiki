---
title: AINews — SpaceXAI Grok 4.6 and Grok Bot (2026-08-13 digest)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-13-ainews-spacexai-grok-46-and-grok-bot.md
url: https://www.latent.space/p/ainews-spacexai-grok-46-and-grok
published: 2026-08-13
ingested: 2026-09-07
domains: [science, models, agents, healthcare]
---

# AINews — SpaceXAI Grok 4.6 and Grok Bot (2026-08-13 digest)

AINews daily digest for 2026-08-13, covering "Frontier Model Day" — a same-day cluster of four launches: xAI/SpaceXAI's Grok 4.6 (1.5T MoE, AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing) and its accompanying Grok Bot "AI teammate" product; Alibaba's Qwen3.8-Max shipping open weights (2.4T/95B active, text-only initial drop); DeepSeek V4 Pro reaching general availability at $0.435/$0.87 pricing with a 15.8% Terminal-Bench gain over preview; and Microsoft's MAI-Thinking-1 reaching availability in Azure AI Foundry. The same issue also carries a widely-engaged but unverified tweet from Steven Strogatz reporting that a neurosurgery resident used ChatGPT 5.6 to solve an open numerical-linear-algebra problem, plus a Reddit recap section explaining Anthropic's rollout of imperceptible Claude text watermarking and C2PA file-provenance metadata for models launched on or after 2026-08-02.

## Influenced pages
- [Grok 4.6](../../models/grok-4-6.md) — new page, supersedes Grok 4.5
- [Grok Bot](../../tools/grok-bot.md) — new page
- [Qwen 3.8](../../models/qwen-3-8.md) — open weights shipped
- [DeepSeek V4](../../models/deepseek-v4.md) — V4 Pro general availability
- [MAI-Thinking-1](../../models/mai-thinking-1.md) — Foundry GA note
- [State of Models](../../state-of/models.md) — leader-line and Recent-changes updates
- [State of Agents](../../state-of/agents.md) — Grok Bot added to Agent orchestration
- [AI in Mathematics](../../trends/ai-in-mathematics.md) — added a caveated Recent-changes entry noting the unconfirmed claim
- [Claude Sonnet 5](../../models/claude-sonnet-5.md) — added a note on Claude's text-watermarking/file-provenance rollout
- [State of Healthcare](../../state-of/healthcare.md) — new Google ResidencyRL bullet under Healthcare triage and patient operations

## Key claims extracted
- Grok 4.6: 1.5T MoE, AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, GDPval-AA v2 Elo 1753, $2/$6 pricing (unchanged from 4.5)
- Grok Bot: "AI teammates with their own cloud computers," launched 2026-08-13
- Qwen3.8-Max: open weights shipped 2026-08-13, 2.4T total/95B active, text-only initial drop, day-0 vLLM/Together/Baseten support
- DeepSeek V4 Pro: GA 2026-08-13, $0.435/M input, $0.87/M output, +15.8% Terminal-Bench over preview
- MAI-Thinking-1: available in Azure AI Foundry; Microsoft soliciting tool-use feedback
- Steven Strogatz tweeted (2026-08-13 digest) that a neurosurgery resident reportedly used ChatGPT 5.6 to solve a significant open problem in numerical linear algebra — no name, paper, or institutional confirmation; tweet link resolves through an obscured redirect, not directly verifiable from this source.
- Separately, "another EpochAI open problem apparently fell" per a different account (scaling01) the same day — equally unverified, no further detail given.
- Claude models launched on/after 2026-08-02 embed an imperceptible, generation-time text watermark surviving copy-paste and light edits.
- Supported file outputs (.png/.jpg/.svg) carry digitally signed C2PA provenance metadata.
- Third-party detection tooling not yet available; older models to be updated during a transition period.
- Mechanism (per commenter explanation): keyed token-sampling bias, detected via a statistical z-score-like test; degrades under heavy paraphrasing or cross-model regeneration.
- Per Anthropic's own support-article framing, the robust claim is metadata/provenance marking, not an "undeletable" text watermark.
- Google's ResidencyRL: training Gemini 3.5 Flash over 49,870 simulated telehealth encounters raised diagnostic accuracy under adversarial conditions from 81% to 88%, missed red flags down 31% — reported via a secondary summary thread (kimmonismus), no primary Google paper or blog post linked.
