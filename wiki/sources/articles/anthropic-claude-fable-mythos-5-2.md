---
title: Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2
type: source
source_type: article
source_file: raw/articles/2026-11-24-anthropiccom-claude-fable-and-mythos-5-2.md
url: https://www.anthropic.com/claude-fable-and-mythos-5-2
published: 2026-11-09
ingested: 2026-11-24
domains: [models, coding, cybersecurity, science]
---

# Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2

Anthropic's launch post for the 5.2 pair. It confirms Fable and Mythos are one underlying model (Fable with cyber and biology classifiers for all users, Mythos for vetted organizations), cuts the price, adds a fast mode, and showcases long multi-agent projects in coding, mathematics, physics, hardware and robotics. The post is undated (an edit note is dated 11 November); the release date of about 2026-11-09 comes from Every's coverage. The benchmark table is an image and was not captured.

## Influenced pages

- [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md) — new page
- [State of Models](../../state-of/models.md) — leader line swap
- [State of Cybersecurity](../../state-of/cybersecurity.md) — offensive-capabilities line, Claude Security model
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — FrontierCode 2.0 comparison, start-with-Opus advice
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — disambiguation note
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — routing advice
- [AI math verification](../../trends/ai-math-verification.md) — Fermat's Last Theorem formalized in 30 hours by 1,000 Fable 5.2 agents

## Key claims extracted

- Fable 5.2 and Mythos 5.2 are the same underlying model; Mythos via Cyber and Life Sciences Verification Programs
- $8/$40 per million tokens; up to 30% faster output than 5.1; fast mode up to 2.5x at $16/$80
- "A step above Opus 5.5" on almost all capabilities evaluated; start most work on Opus 5.5
- FrontierCode 2.0: Fable 5.2 High ≈ Opus 5.5 Max at about half the cost per task; Xhigh highest of any released model tested
- Mythos 5.2 CVE Rediscovery: +10.2% vs Opus 5.5, +14.4% vs Mythos 5.1; now in Claude Security
- About 55% fewer blocks than Fable 5.1 (60% cyber, 40% biology); fallbacks to Opus 4.8 (cyber) and Opus 5 (biology)
- AI R&D skills (kernel optimization, LLM architecture) deliberately held at Opus 5.5 level
- Sandbox-escape eval: Mythos 5.2 3.1%, Opus 5.5 3.3%, Sonnet 5.5 5.1%, Mythos 5.1 21%, Mythos 5 39%; more evaluation awareness than any recent model
- Fermat's Last Theorem formalized by 1,000 Fable 5.2 agents in 30 hours (earlier: 11 days; Opus 5.5 26% in 18 hours); minimal prompts, self-built coordination, one-third the action tokens, proof seven times shorter
- Two open black-hole physics problems solved; three electronic devices designed with Diode; prototype OS from 1,000+ subagents over eight days; Python-to-Rust service migration
- Anti-distillation protections cut harvested data 90–99%; preserved thinking now applies to all accounts; Enterprise Frontier Safeguards private beta (ZDR-compatible)
- Available on all platforms (AWS, Google Cloud, Azure); API id `claude-fable-5-2`
