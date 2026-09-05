---
title: "[AINews] All Model Labs are now Agent Labs"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
url: https://www.latent.space/p/ainews-all-model-labs-are-now-agent
published: 2026-05-23
ingested: 2026-08-25
domains: [agents, cybersecurity, models, voice]
---

# [AINews] All Model Labs are now Agent Labs

AINews/Latent Space digest (2026-05-23) covering the "model alone is no longer the product" thesis (Greg Brockman, AI21's pivot, DeepSeek's new harness team), the MCP 2026-07-28 stateless release candidate, managed-sandbox primitives becoming first-class (Gemini Managed Agents + Interactions API, CoreWeave Sandboxes, Cloudsail), DeepSeek V4-Pro's permanent price cut, a Qwen3.7-Max review, an unverified ALE-Bench claim about Chinese open models, Cartesia's Sonic-3.5 topping the Artificial Analysis Speech Arena, and Anthropic's Project Glasswing reporting 10,000+ high/critical-severity vulnerabilities found within a month.

## Influenced pages
- [Agent Labs vs Model Labs](../../concepts/agent-labs-vs-model-labs.md) — added Brockman/AI21/DeepSeek evidence
- [Model Context Protocol](../../concepts/mcp.md) — MCP stateless RC
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — Glasswing 10,000+ vulnerabilities figure
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Glasswing figure
- [DeepSeek V4](../../models/deepseek-v4.md) — permanent pricing update
- [Qwen 3.7](../../models/qwen-3-7.md) — third-party review addition
- [State of Models](../../state-of/models.md) — leader-line refresh
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — China price/capability bullet
- [Cartesia](../../tools/cartesia.md) — added as a second independent benchmark corroborating the existing Together AI #1 TTS claim

## Key claims extracted
- Greg Brockman: "the model alone is no longer the product" — AINews calls it a big reversal from a stance held ~uniformly by "Team Big Model"; AI21 shuttered its model team to pivot to agents; "even the venerable DeepSeek" is building a "harness team" for the first time
- AINews's own counterpoint: models co-trained with harnesses "open the door for closing access to models even further" — a lab that post-trains its model to perform well only inside its closed-source agent can funnel users to that agent at the expense of its model/API business
- MCP 2026-07-28 RC is stateless (no handshake/session ID); adds MCP Apps/Tasks, auth hardening, deprecation policy; AINews reads statelessness as easier scaling, simpler load balancing, fewer sticky-session concerns
- Managed sandboxes as first-class primitives: Gemini Managed Agents + Interactions API, CoreWeave Sandboxes (public preview), Cloudsail (per-task Cloudflare sandboxes)
- Anthropic: Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch
- @deepseek_ai made the 75% DeepSeek-V4-Pro discount permanent; @ArtificialAnlys quantified first-party pricing at $0.435/M input, $0.87/M output, $0.0036/M cached input, ~$0.18/M blended; AA estimates running its Intelligence Index on V4-Pro costs ~3x less than Gemini 3.1 Pro Preview, ~12x less than GPT-5.5, ~19x less than Claude Opus 4.7
- A third-party review (@ZhihuFrontier) portrayed Qwen3.7-Max as a meaningful step up, especially in instruction following, context reliability, and stability, while still suffering from verbosity and high token usage
- @scaling01 claimed recent ALE-Bench runs show Chinese models (Kimi-K2.6, DeepSeek-V4, GLM-5.1) outperforming several Western releases in that setting — single-tweet sourcing, not independently verified
- Artificial Analysis (@ArtificialAnlys) ranked Cartesia's Sonic-3.5 the new #1 TTS model on its Speech Arena, Elo 1218, 42 languages, strong naturalness/transcript-following; Cartesia itself separately claims ~82ms end-to-end first-audio latency in production (a vendor claim, not an AA measurement)
