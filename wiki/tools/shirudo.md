---
title: Shirudo
type: tool
domains: [cybersecurity]
subcategory: runtime-security
tags: [openai, open-source]
as_of: 2026-11-23
sources: [openai-cisco-shirudo]
---

# Shirudo

Open-source Linux runtime from OpenAI and Cisco for protecting running systems while a patch is tested and rolled out. It deploys temporary safeguards, called shields, that block the behavior exposing a vulnerability while legitimate requests continue, without restarting the service.

## Current status (as of 2026-11-23)
- Announced and open-sourced 2026-11-23; BSD 2-Clause, with its eBPF programs dual-licensed BSD/GPL
- Shields are eBPF programs (small vetted programs run at hook points inside the Linux kernel); operators can observe a shield's effect on real traffic before enforcing it, and approve before deployment
- Designed around four capabilities: live protection without restarts; programmable controls so agents can investigate vulnerabilities, write shields and validate them against exploits and workloads; signed shields checked by the eBPF verifier before loading; TPM-backed records of shields loaded or removed
- Demo: a [Codex](codex.md)-generated shield added an input check to Java's Base64 decoder on a running Elasticsearch process and blocked a Java4Shell exploit attempt without a restart
- Stated goal: ship tested shields alongside vulnerability disclosures; longer term, auto-generated least-privilege policies and restoring compromised systems to a verified state

## Weaknesses / caveats
- A stopgap, not a patch: it buys time between disclosure and fix
- The four capabilities are described as design goals; the public evidence is one controlled test and a conference walkthrough

## Related
- [NVIDIA OpenShell](nvidia-openshell.md) — also open-source runtime enforcement, but sandboxes agents rather than protecting production hosts
- [State of Cybersecurity](../state-of/cybersecurity.md)

## Recent changes
- [2026-11-23] Launched by OpenAI and Cisco as open source; Codex-generated shield blocked a Java4Shell exploit on running Elasticsearch

## Sources
- [OpenAI and Cisco introduce Shirudo](../sources/articles/openai-cisco-shirudo.md)
