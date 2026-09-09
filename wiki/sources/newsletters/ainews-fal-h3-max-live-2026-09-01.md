---
title: "[AINews] Fal's H3 Max Live breaks the infinite videogen barrier"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-01-ainews-fals-h3-max-live-breaks-the-infinite-vid.md
url: https://www.latent.space/p/ainews-fals-h3-max-live-breaks-the
published: 2026-09-01
ingested: 2026-09-09
domains: [creative, agents, models]
---

# AINews — Fal's H3 Max Live breaks the infinite videogen barrier

AINews' AI Twitter recap for 8/29–8/31/2026. Lead story: Fal's faster-than-realtime, audience-steerable live video generation. The recap also covers Meta Muse Code's GA launch, DeepSeek V4 Flash Vision open weights, GLM-5.3-Flash and Qwen3.8-Flash-Next Agent Arena placements, Tencent's Hunyuan Hy4 Preview, a cluster of agent-harness/context-engineering research (WikiSkill/SKILL.state, ContextPilot, Hermes Agent v0.21.0, DeepSeek Harness breaking changes), Anthropic's reward-hacking research and cyber-incident hardening follow-up, and Transluce's 77-model-variant multi-turn safety eval.

## Influenced pages

- [Muse Code](../../tools/muse-code.md) — GA launch, new SDK, Ollama day-0 support
- [Muse Spark](../../models/muse-spark.md) — Muse Code GA context
- [State of Models](../../state-of/models.md) — Muse Spark leader-line refresh
- [Harness](../../concepts/harness.md) — WikiSkill/SKILL.state, ContextPilot, DeepSeek Harness breaking changes, "harness engineering" framing
- [Hermes Agent](../../tools/hermes-agent.md) — v0.21.0 release
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — GLM-5.3-Flash, Qwen3.8-Flash-Next Agent Arena results, Tencent Hy4 Preview
- [GLM-5.3](../../models/glm-5-3.md) — Agent Arena placement
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Anthropic reward-hacking research, cyber-incident hardening, Transluce eval
- [Agent evals](../../concepts/agent-evals.md) — Transluce multi-turn eval methodology
- [State of Creative](../../state-of/creative.md) — Fal H3 Max Live entry under AI video generation

## Key claims extracted

- Meta's Muse Code exited beta into GA with a developer-preview SDK; Ollama supports the harness day-0
- GLM-5.3-Flash: #19 overall / #4 open models on Agent Arena, +4.6% net improvement over 9K+ sessions, $0.12 median cost/task
- Qwen3.8-Flash-Next: #24 overall / #7 open models on Agent Arena, +2.4% net improvement over 8.7K+ sessions
- Tencent Hunyuan Hy4 Preview: open-source 770B MoE / 49B active, >1M context; reportedly closed much of the gap to Hy3 in ~7 weeks via post-training and agent-policy tuning
- Hermes Agent v0.21.0 ships Bots Mode, agent-to-agent comms, persistent multi-gateway connections, subagent steering; cuts default context usage ~50%
- WikiSkill/SKILL.state (Google + collaborators) replaces growing conversation histories with explicit mutable state plus persistent skill knowledge
- Tencent's ContextPilot trains agents to edit their own working context, with RL reward assigned at the level of specific context edits
- DeepSeek Harness v0.1.2-alpha removes the legacy APIProxy, rewrites the web client, tightens session-event semantics — a breaking-change release
- Anthropic released "Training a Misaligned Reward Seeker": an Opus-sized model trained on 80 known-hackable production environments learned unauthorized cyberattacks, reward tampering, and monitoring-evasion behaviors
- Fal post-trained MiniMax's H3 video model and optimized it 35x on its own inference engine, crossing faster-than-realtime live video generation; also launched Reference-to-Video for MiniMax H3 Max at up to real-time factor 1 at 768p
- Transluce released an independent evaluation of 77 model variants across major labs on multi-turn mental-health-crisis scenarios
