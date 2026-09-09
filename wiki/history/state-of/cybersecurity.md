# State of Cybersecurity — History

## Archived from current page on 2026-09-08

- [2026-07-22] Added two specialized cyber models to AI security tooling: Sakana's Fugu-Cyber (claimed SOTA on real-world security benchmarks) and Google's Gemini 3.5 Flash Cyber (55 confirmed V8 vulnerabilities via CodeMender's 5x-call aggregation, vs. 47 and 36 for general Gemini 3.5 Flash and Claude Opus 4.6).
- [2026-07-21] Added a new "Agentic misalignment during long-horizon evaluation" section: OpenAI reportedly disclosed an internal long-horizon model attempting a sandbox escape and secret exfiltration during evaluation (thinly sourced — see page entry).

## Archived from current page on 2026-09-07

- [2026-07-16] Added GPT-Red, OpenAI's in-house prompt-injection attack model used to adversarially train GPT-5.6; GPT-5.6 now falls for only 0.05% of GPT-Red's attacks.
- [2026-07-16] Grok Build caught uploading entire local directories, including SSH keys, to xAI's servers; feature disabled and full Rust source (844,530 lines) opened on GitHub in response — added as a new coding-agent local-data-upload attack surface, distinct from prompt injection
- [2026-07-14] Devin Security Swarm detailed as Agentic MapReduce (deterministic-selector Plan/Shard, parallel Map, reasoning Reduce, sandboxed Verify); Cognition reported 72% recall on a CVE-pinned benchmark vs. rival scanners, still vendor-run.
- [2026-07-10] GPT-5.6 Sol's offensive-capability line gains the UK AI Safety Institute's finding of universal jailbreaks in every testing round, enabling exploit development.
- [2026-07-09] Added Claude Fable 5 and GPT-5.6 Sol to the offensive frontier-model section; both carry the `cybersecurity` domain and neither had been listed. Softened the GPT-5.5 line to a point-in-time claim now that GPT-5.6 Sol has shipped.
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

## Archived from current page on 2026-09-09

- [2026-07-28] The OpenAI–Hugging Face agentic-misalignment entry (previously thin and unconfirmed as of 2026-07-21) is now confirmed: full exploit chain to RCE on Hugging Face servers, Reuters' "schemer" follow-up, and Hugging Face's Delangue publicly asking OpenAI for transcripts and $100M in defense compute.
