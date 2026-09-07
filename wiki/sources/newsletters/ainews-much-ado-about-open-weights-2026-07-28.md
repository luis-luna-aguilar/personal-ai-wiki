---
title: "AINews — Much ado about Open Weights"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-28-ainews-much-ado-about-open-weights.md
url: https://www.latent.space/p/ainews-much-ado-about-open-weights
published: 2026-07-28
ingested: 2026-09-06
domains: [models]
---

# AINews — Much ado about Open Weights

AINews digest covering the day's open-weight news: Kimi K3's full weight release and independent benchmark confirmation that it beats Opus 4.8, plus the parallel open-weight politics story (NVIDIA's Open Secure AI Alliance, Anthropic's position statement, and reported US/Anthropic lobbying against open models) — the politics portion is covered by a separate proposal.

## Influenced pages

- [Kimi K3](../../models/kimi-k3.md) — weights ship, real architecture specs, independent Opus-4.8-beating confirmation
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Recent-changes entries for the K3 ship date and the NVIDIA Open Secure AI Alliance / Anthropic-position / lobbying-report paragraph

## Key claims extracted

- Kimi K3: 2.8T total / 104B active parameters, 896 experts (16 active per token), FlashKDA/MoonEP/AgentENV open-sourced alongside the model
- License: "kimi-k3", hosts over $20M/year need a separate agreement, 100M+ MAU or $20M+/month products must display "Kimi K3" branding
- Independent evals: #1 open-weight on Agent Arena (+9.75%), #1 overall Frontend Code Arena, Cognition FrontierCode 1.1 58.2% (63.6% pass rate)
- Day-0 distribution across vLLM, Baseten, Modal, Fireworks, Nebius, Together, DigitalOcean, Cursor, Cognition, Ollama Cloud, Dell Enterprise Hub
- NVIDIA launches Open Secure AI Alliance (Microsoft, Hugging Face, LangChain, Nous Research, others), citing the OpenAI/Hugging Face incident
- OpenAI signs the alliance letter; Anthropic does not, publishing its own position instead
- Anthropic's stated position: no ban on open-weights models, but supports chip controls on China, anti-distillation measures, mandatory safety testing regardless of openness
- NYT: OpenAI and Anthropic lobbying Washington to restrict open-source AI despite Altman's public support for it
- US officials reportedly weighing up to a 30-day mandatory pre-release review window for frontier models
