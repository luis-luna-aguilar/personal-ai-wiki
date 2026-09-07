---
title: "AINews — Fearing RSI: OpenAI, Anthropic, GDM, Meta cosign letter to 'pace' AI development"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-29-ainews-fearing-rsi-openai-anthropic-gdm-meta.md
url: https://www.latent.space/p/ainews-fearing-rsi-openai-anthropic
published: 2026-07-29
ingested: 2026-09-07
domains: [models, agents, cybersecurity]
---

# AINews — Fearing RSI: OpenAI, Anthropic, GDM, Meta cosign letter to "pace" AI development

AINews recap covering 1,171 frontier-lab employees (nearly every major lab except xAI) cosigning a letter asking the U.S. government to help build technical and governance tools to "deliberately pace" frontier AI development, citing risk from automated AI research accelerating capability past anyone's ability to understand or control it; Dario Amodei and Sam Altman both publicly backed it. The same issue covers Hugging Face's forensic postmortem of an autonomous-agent cyberattack (17,600 actions, root access on 11 nodes, cluster-admin on two clusters, 136 secrets, defended in part using open-weight GLM 5.2), the resulting Open Secure AI Alliance, Anthropic's separate cryptanalysis research using Claude Mythos Preview, and continued Kimi K3 ecosystem coverage.

## Influenced pages

- [trends/ai-governance-and-policy](../../trends/ai-governance-and-policy.md) — new "pacing" letter section
- [state-of/cybersecurity](../../state-of/cybersecurity.md) — extends the OpenAI–Hugging Face incident entry with forensic detail
- [trends/open-weight-momentum-broadens](../../trends/open-weight-momentum-broadens.md) — corrects the Open Secure AI Alliance membership claim (OpenAI declined to join, not signed); Kimi K3 deployment-economics Recent-changes entry
- [Kimi K3](../../models/kimi-k3.md) — MI355X/GPU deployment-cost estimate

## Key claims extracted

- 1,171 employees across OpenAI, Anthropic, Google DeepMind, Meta, and Thinking Machines (not xAI) cosigned a statement asking the US government to support an international effort to build tools to "deliberately pace" frontier AI development
- The statement frames the risk as: labs may be close to automating AI research, and no lab or country can unilaterally slow down under competitive pressure without shared governance/technical tools
- Dario Amodei cosigned; Sam Altman voiced public agreement; OpenAI's official account tweeted the letter
- Critics (Adam Thierer, Sarah Hooker) called it vague regulatory capture that would not meaningfully constrain China
- Hugging Face published a detailed forensic timeline of an autonomous-agent intrusion: roughly 17,600 actions over 2–4.5 days, root access on 11 nodes, cluster-admin on two clusters, 136 secrets accessed, repeated VPN enrollment, and an attempted CI compromise via GitHub App tokens and a PR
- HF's security team said the defensive challenge was volume, not sophistication, and that they used open-weight GLM 5.2 on their own infrastructure for the forensic investigation
- NVIDIA's "Open Secure AI Alliance" (Adobe, Cisco, Cloudflare, Hugging Face, IBM, Microsoft, Red Hat, Salesforce, SAP, ServiceNow, Snowflake, SpaceX) formed directly in response to the incident
- OpenAI open-sourced its Codex Security CLI the same week
- Anthropic separately announced Claude Mythos Preview helped researchers discover weaknesses in cryptographic algorithms (HAWK, AES-related results) plus a new CryptanalysisBench
- ZhihuFrontier cost analysis: Kimi K3 minimum verified config ~8×AMD MI355X to load; production serving needs 64+ GPUs in one high-bandwidth domain; six-figure entry cost for an 8-GPU server
