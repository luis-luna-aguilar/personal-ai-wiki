---
title: State of Cybersecurity
type: state-of
domains: [cybersecurity]
tags: []
as_of: 2026-04-23
sources: [slopcop-repo, glasswing, openai-gpt-5-5-launch]
---

# State of Cybersecurity

Current state of AI applied to cybersecurity: AI-specific attack surfaces, vulnerability detection, and security tooling for development workflows.

## Subcategories

### AI-specific attack surfaces

Attack vectors unique to or amplified by AI systems in development workflows.

- **Slopsquatting** — LLMs hallucinate ~20% of package names (USENIX Security 2025, 576k samples); attackers pre-register those names on PyPI/npm with malicious `postinstall` payloads. Mitigation: `slopcop` CLI checks registry age, download count, postinstall scripts, and Levenshtein distance before install. See [[concepts/slopsquatting]]. *(as of 2026-04-22)*

### AI-assisted vulnerability detection

Coding agents extended into security review and vulnerability validation.

- [[tools/codex]] — Codex Security feature expands the coding agent into vulnerability review and validation work beyond code generation *(as of 2026-03-09)*

### Frontier model capabilities (offensive)

Frontier models operating above public tiers, deployed selectively for cybersecurity research.

- [[models/claude-mythos-preview]] — Anthropic; restricted preview; autonomously found thousands of zero-days across major OSes and browsers without human steering; partners: Cisco, AWS, Microsoft; substantially above Opus 4.6 on CyberGym *(as of 2026-04-22)*
- [[models/gpt-5-5]] — OpenAI; CyberGym 81.8% in the launch comparison table, above GPT-5.4 and Claude Opus 4.7 among publicly available models; publicly deployed with tighter safeguards rather than restricted-access-only release *(as of 2026-04-23)*

### Trusted defensive access

Provider programs that expand access to higher-risk cyber capabilities for verified defenders rather than to the general public.

- **OpenAI Trusted Access for Cyber** — verified defenders protecting critical infrastructure can apply for broader GPT-5.5 cyber capability access with fewer restrictions *(as of 2026-04-23)*

## Recent changes

- [2026-04-23] Added [[models/gpt-5-5]] under `Frontier model capabilities (offensive)` and noted OpenAI's Trusted Access for Cyber program for verified defenders
- [2026-03-09] Codex Security launched: Codex extended into vulnerability review and validation
- [2026-04-22] Page created; added `AI-specific attack surfaces` section with slopsquatting (USENIX 2025 evidence, 19.7% hallucination rate, slopcop mitigation)
- [2026-04-22] Added `Frontier model capabilities (offensive)` section; [[models/claude-mythos-preview]] / Project Glasswing disclosed
