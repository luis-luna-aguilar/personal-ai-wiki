---
title: OpenAI and Cisco introduce Shirudo
type: source
source_type: article
source_file: raw/articles/2026-11-23-openaicom-index-introducing-shirudo.md
url: https://openai.com/index/introducing-shirudo/
published: 2026-11-23
ingested: 2026-11-23
domains: [cybersecurity]
---

# OpenAI and Cisco introduce Shirudo

OpenAI and Cisco announced Shirudo, an open-source runtime that protects running Linux systems while patches are tested and rolled out. It deploys temporary eBPF "shields" that block the behavior exposing a vulnerability while legitimate requests continue, with operator approval before enforcement, signed shields, and TPM-backed records of what was loaded. In a controlled test, a Codex-generated shield added an input check to Java's Base64 decoder on a running Elasticsearch process and blocked a Java4Shell exploit without a restart. The code is BSD 2-Clause (eBPF programs dual BSD/GPL); the goal is to publish tested shields alongside vulnerability disclosures.

## Influenced pages
- [Shirudo](../../tools/shirudo.md) — new page
- [State of Cybersecurity](../../state-of/cybersecurity.md) — new bullet under AI security tooling

## Key claims extracted
- Shirudo launched 2026-11-23 by OpenAI and Cisco as open source (BSD 2-Clause; eBPF programs dual BSD/GPL)
- Shields block a vulnerable code path on a running Linux system without a restart; operators can monitor a shield's effect before enforcing it and approve deployment
- Designed around live protection, agent-driven shield development and validation, signed and verified shields, and TPM-backed verification
- A Codex-generated shield blocked a Java4Shell exploit attempt against running Elasticsearch in a controlled test
- Goal: tested shields published alongside vulnerability disclosures; longer term, auto-generated least-privilege policies and recovery to a verified known-good state
