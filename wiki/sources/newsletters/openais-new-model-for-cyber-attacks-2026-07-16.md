---
title: OpenAI's new model for cyber attacks (newsletter digest)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-16-openais-new-model-for-cyber-attacks.md
published: 2026-07-16
ingested: 2026-09-06
domains: [coding]
---

# OpenAI's new model for cyber attacks (newsletter digest)

A multi-story AI newsletter dated 2026-07-16, covering Bun's Zig-to-Rust rewrite, the Grok Build SSH-key incident and open-sourcing, and OpenAI's GPT-Red adversarial-training model.

## Influenced pages

- [Training — AI enablement (software development)](../../training/ai-enablement-software-development.md) — corrected Bun rewrite figures, new adversarial-review case-study entry
- [Grok Build](../../tools/grok-build.md) — incident/resolution caveat, open-source bullet, Recent changes
- [State of Cybersecurity](../../state-of/cybersecurity.md) — new AI-specific attack surface bullet and new GPT-Red entry under AI security tooling, Recent changes
- [GPT-5.6 Sol](../../models/gpt-5-6-sol.md) — Recent-changes entry for the GPT-Red adversarial-training result

## Key claims extracted

- Bun creator Jarred Sumner (Anthropic MTS) ported Bun from Zig to Rust in 11 days using a pre-release Claude Fable 5
- Full methodology write-up published on Sumner's own blog, linked from this newsletter
- Grok Build was caught uploading entire local directories, including SSH keys, to xAI's servers
- xAI disabled the offending feature and open-sourced the full agent: 844,530 lines of Rust, on GitHub
- Developers can now audit, run locally, and extend the agent with plugins and subagents
- GPT-Red is an OpenAI-built model purpose-made to craft prompt-injection attacks hidden in emails, webpages, and tool outputs
- GPT-5.6 was trained against GPT-Red's attacks and now falls for only 0.05% of them
