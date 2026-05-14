---
title: AI developer supply chain attacks — Shai-Hulud and HF impersonator
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-13-supply-chain-attacks-keep-hitting-ai.md
published: 2026-05-13
ingested: 2026-05-13
domains: [cybersecurity]
---

# AI developer supply chain attacks — Shai-Hulud and HF impersonator

Two newsletters: "Supply Chain Attacks Keep Hitting AI" (May 13) and "AINews — The End of Finetuning" (May 13, which carried the Shai-Hulud detail). Both published the same day.

## Influenced pages

- [State of Cybersecurity](../../state-of/cybersecurity.md) — new `AI developer supply chain attacks` subcategory added

## Key claims extracted

### Mini Shai-Hulud campaign
- Initial target: TanStack npm packages
- Expanded targets (May 2026): OpenSearch, Mistral AI, Guardrails AI, UiPath, and others across npm and PyPI
- Pattern: specifically targets AI developer tooling, not random packages
- Persistence mechanism: modifies `.claude/settings.json` (Claude Code settings) and `.vscode/tasks.json` (VS Code task runner) so the payload re-runs on future tool events — even after the malicious package is removed via package manager
- Confirmed victim: Guardrails AI v0.10.1 confirmed compromised; quarantined within approximately 2 hours of detection

### Hugging Face Transformers impersonator
- Source: Microsoft threat intelligence
- Vector: Python package impersonating the legitimate `transformers` library from Hugging Face
- Goal: steal developer credentials (specifically AI/ML developer credentials)

### Recommended mitigations
- `minimumReleaseAge` configuration: require a minimum age for packages before install tooling accepts them
- `blockExoticSubdeps`: block dependencies that use remote GitHub refs instead of registry versions in their transitive dependency tree
- Secrets hygiene: migrate secrets from `.env` files to a dedicated secrets manager
- Audit `.claude/settings.json` and `.vscode/tasks.json` for unexpected hook entries after any suspicious install
