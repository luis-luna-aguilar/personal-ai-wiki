---
title: AIUC
type: tool
domains: [agents]
subcategory: agent-eval-tooling
tags: [agentic]
as_of: 2026-09-16
sources: [latent-space-aiuc-rune-kvist-2026-09-16]
---

# AIUC

AIUC is a standards-and-insurance company for AI agents rather than a software tool: it certifies agents against its AIUC-1 standard, runs its own quarterly adversarial testing of certified agents, and pairs certification with agent liability insurance. In its own words it builds "confidence infrastructure for frontier AI through standards and insurance." Cofounder Rune Kvist was Anthropic's first product hire.

## Current status (as of 2026-09-16)

- Raised a $40M Series A on 2026-09-16.
- AIUC-1 covers agent security, safety and reliability: six categories, about 51 requirements and 130 controls (technical, third-party test, and policy controls).
- Auditors such as KPMG and Schellman check the evidence; AIUC itself runs thousands of simulated jailbreak, hallucination and data-leak attempts each quarter.
- Certification takes 3–10 weeks and lasts a year; a consortium of Fortune 1000 risk leaders revises the standard quarterly (recent additions: MCP and agent-to-agent risks).
- Certified: Lovable, ElevenLabs, Intercom. ElevenLabs bought an agent insurance policy underwritten with Lloyd's of London.

## Weaknesses / caveats

- Kvist's lesson for builders: most teams optimise the happy path and have never seriously stress-tested their guardrails against an adversary; certification surfaces that gap rather than closing it for them.
- Its roadmap extends to frontier models, robotics and universal red teaming; model certification is previewed, not announced.

## Recent changes

- [2026-09-16] $40M Series A announced; AIUC-1 certifications include Lovable, ElevenLabs and Intercom, with Cursor and Harvey named as companies AIUC works with.

## Related

- [Agent autonomy and governance](../training/agent-autonomy-and-governance.md) — "Certify and insure agents externally"

## Sources

- [Latent Space — Underwriting Superintelligence: Rune Kvist on AIUC-1 and agent insurance](../sources/newsletters/latent-space-aiuc-rune-kvist-2026-09-16.md)
