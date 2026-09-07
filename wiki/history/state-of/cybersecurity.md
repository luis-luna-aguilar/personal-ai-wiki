# State of Cybersecurity — History

## Archived from current page on 2026-09-07

- [2026-07-02] Cognition launched Devin Security Swarm, pushing AI-assisted vulnerability detection toward parallel agent workflows that validate exploitability and generate fix PRs.
- [2026-06-22] Gray Swan interview adds AI-native security framing: agents should be treated as untrusted systems; indirect prompt injection, identity, permissions, guardrails, and automated red teaming are core deployment concerns.
- [2026-05-23] Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch; added as a program-wide figure to the Claude Mythos Preview entry (industry-adaptation framing attributed to AINews' recap).

## Archived from current page on 2026-09-06

- [2026-05-19] Added GitHub internal-repo breach (compromised employee device, poisoned VS Code extension; attacker's ~3,800-repo claim "directionally consistent" with GitHub's investigation, not confirmed) under AI developer supply chain attacks — a non-AI-specific but dev-tooling-relevant counterpoint to Glasswing's offensive findings.
- [2026-05-13] OpenAI announced Daybreak as a thin official cyber-defense signal combining frontier models, Codex, and security partners; implementation details remain pending.
- [2026-05-13] Agentic security tooling is becoming a category signal: scanner, monitor, fix-validation, and deployment-risk workflows are being redesigned for software built and operated by agents.
- [2026-05-13] Added `AI developer supply chain attacks`: Mini Shai-Hulud campaign (persistence via .claude/settings.json + .vscode/tasks.json hooks; Guardrails AI v0.10.1 confirmed compromised) and Hugging Face Transformers impersonator; mitigations: minimumReleaseAge, blockExoticSubdeps
- [2026-05-19] Cloudflare Project Glasswing: detailed harness architecture (8 stages, ~50 concurrent agents, adversarial validate agent); Mythos exploit chain construction and proof loop confirmed; organic refusals inconsistent as safety boundary; architectural resilience over patch speed as the defender takeaway

## Archived from current page on 2026-09-05

- [2026-05-01] Added Claude Security and Cursor Security Review to AI-assisted vulnerability detection; both are secondary-source entries pending primary verification

## Archived from current page on 2026-05-19

- [2026-04-23] Added [GPT-5.5](../../models/gpt-5-5.md) under `Frontier model capabilities (offensive)` and noted OpenAI's Trusted Access for Cyber program for verified defenders
- [2026-03-09] Codex Security launched: Codex extended into vulnerability review and validation
- [2026-04-22] Page created; added `AI-specific attack surfaces` section with slopsquatting (USENIX 2025 evidence, 19.7% hallucination rate, slopcop mitigation)
- [2026-04-22] Added `Frontier model capabilities (offensive)` section; [Claude Mythos Preview](../../models/claude-mythos-preview.md) / Project Glasswing disclosed
