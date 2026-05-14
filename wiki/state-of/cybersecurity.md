---
title: State of Cybersecurity
type: state-of
domains: [cybersecurity]
tags: []
as_of: 2026-05-13
sources: [slopcop-repo, glasswing, openai-gpt-5-5-launch, ai-security-scanners-2026-05-01, supply-chain-attacks-2026-05-13, agentic-security-tooling-2026-05-13, openai-daybreak-2026-05-13]
---

# State of Cybersecurity

Current state of AI applied to cybersecurity: AI-specific attack surfaces, vulnerability detection, and security tooling for development workflows.

## Subcategories

### AI-specific attack surfaces

Attack vectors unique to or amplified by AI systems in development workflows.

- **Slopsquatting** — LLMs hallucinate ~20% of package names (USENIX Security 2025, 576k samples); attackers pre-register those names on PyPI/npm with malicious `postinstall` payloads. Mitigation: `slopcop` CLI checks registry age, download count, postinstall scripts, and Levenshtein distance before install. See [Slopsquatting](../concepts/slopsquatting.md). *(as of 2026-04-22)*

### AI developer supply chain attacks

Coordinated attacks targeting Python and npm packages used by AI developers, distinct from traditional slopsquatting because they are intentionally crafted rather than passively occupying hallucinated names.

**Mini Shai-Hulud campaign (May 2026)**
- Expanded from its initial TanStack target to hit: OpenSearch, Mistral AI, Guardrails AI, UiPath, and others across npm and PyPI
- Specifically targets AI developer tooling (not generic software)
- Persistence vector: hooks into `.claude/settings.json` and `.vscode/tasks.json` — the compromise **re-executes on future Claude Code or VS Code task events** even after the malicious package is removed; uninstalling the package is not sufficient remediation
- Guardrails AI confirmed: package v0.10.1 was compromised; quarantined within ~2 hours

**Hugging Face Transformers impersonator (May 2026)**
- Microsoft found malware hidden in a Python package name-spoofing Hugging Face's `transformers` library
- Goal: steal developer credentials, specifically targeting AI/ML developers

**Mitigations**
- `minimumReleaseAge`: require packages to have been published for a minimum number of days before your tooling installs them
- `blockExoticSubdeps`: block transitive dependencies that point to remote GitHub refs rather than a registry version
- Move secrets out of `.env` files into a dedicated secrets manager
- Verify `.claude/settings.json` and `.vscode/tasks.json` for unexpected entries after any unusual package install

### AI-assisted vulnerability detection

Coding agents extended into security review and vulnerability validation.

- [Codex](../tools/codex.md) — Codex Security feature expands the coding agent into vulnerability review and validation work beyond code generation *(as of 2026-03-09)*
- **Claude Security** — Anthropic; reported repo vulnerability scanner that validates findings and suggests fixes using Opus 4.7; source is AINews secondary coverage *(as of 2026-05-01)*
- **Cursor Security Review** — Cursor; reported always-on PR review plus scheduled codebase scans; source is AINews secondary coverage *(as of 2026-05-01)*
- **Vercel DeepSec** — secondary May 2026 coverage describes security scanning/review for agent-built applications; pending primary verification *(as of 2026-05-04)*

The category is shifting from one-off scanners toward agent-compatible security loops: vulnerability monitoring, fix validation, supply-chain checks, and deployment-risk review inside coding-agent workflows.

### Frontier model capabilities (offensive)

Frontier models operating above public tiers, deployed selectively for cybersecurity research.

- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview; autonomously found thousands of zero-days across major OSes and browsers without human steering; partners: Cisco, AWS, Microsoft; substantially above Opus 4.6 on CyberGym *(as of 2026-04-22)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; CyberGym 81.8% in the launch comparison table, above GPT-5.4 and Claude Opus 4.7 among publicly available models; publicly deployed with tighter safeguards rather than restricted-access-only release *(as of 2026-04-23)*

### Trusted defensive access

Provider programs that expand access to higher-risk cyber capabilities for verified defenders rather than to the general public.

- **OpenAI Trusted Access for Cyber** — verified defenders protecting critical infrastructure can apply for broader GPT-5.5 cyber capability access with fewer restrictions *(as of 2026-04-23)*
- **OpenAI Daybreak** — official OpenAI program/product framing for cyber defenders that combines frontier models, Codex, and security partners to accelerate defensive workflows; current source is a short announcement tweet, so implementation details remain pending. *(as of 2026-05-13)*

## Recent changes

- [2026-05-13] OpenAI announced Daybreak as a thin official cyber-defense signal combining frontier models, Codex, and security partners; implementation details remain pending.
- [2026-05-13] Agentic security tooling is becoming a category signal: scanner, monitor, fix-validation, and deployment-risk workflows are being redesigned for software built and operated by agents.
- [2026-05-13] Added `AI developer supply chain attacks`: Mini Shai-Hulud campaign (persistence via .claude/settings.json + .vscode/tasks.json hooks; Guardrails AI v0.10.1 confirmed compromised) and Hugging Face Transformers impersonator; mitigations: minimumReleaseAge, blockExoticSubdeps
- [2026-05-01] Added Claude Security and Cursor Security Review to AI-assisted vulnerability detection; both are secondary-source entries pending primary verification
- [2026-04-23] Added [GPT-5.5](../models/gpt-5-5.md) under `Frontier model capabilities (offensive)` and noted OpenAI's Trusted Access for Cyber program for verified defenders
- [2026-03-09] Codex Security launched: Codex extended into vulnerability review and validation
- [2026-04-22] Page created; added `AI-specific attack surfaces` section with slopsquatting (USENIX 2025 evidence, 19.7% hallucination rate, slopcop mitigation)
- [2026-04-22] Added `Frontier model capabilities (offensive)` section; [Claude Mythos Preview](../models/claude-mythos-preview.md) / Project Glasswing disclosed
