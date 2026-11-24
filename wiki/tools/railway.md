---
title: Railway
type: tool
domains: [agents]
subcategory: agent-sandbox-infra
tags: [agentic]
as_of: 2026-10-21
sources: [railway-agent-native-cloud-2026-05-20, railway-security-disclosure-2026-10-21, every-railway-response-agents-2026-10-22]
---

# Railway

Railway is a deployment platform ("push code, get a URL") that is rebuilding network, compute, storage, and orchestration for an agent-native world. A 35-person team serves ~3M users adding ~100K signups/week; the company has raised $124M and runs most workloads on its own bare-metal data centers, bursting to public clouds when needed.

## Current status (as of 2026-05-20)

- Bare metal: ~3-month payback vs. cloud rental and ~70% margins that fund cloud bursting; a rebuilt network overlay straddles five clouds including Oracle, AWS, GCP, and Railway's own metal
- Central Station: internal system clustering customer feedback and incidents and routing them to the right team
- Agent-safe production forks: copy-on-write clones of production with PII transforms so agents can test changes against production-like state; progressive/shadow rollouts (0.1% → 1% → all) as first-class primitives
- Thesis: "the pull request is dying" — replaced by versioned, mergeable production changes; the CLI, not the canvas, becomes the primary agent input surface; agents with Railway CLI access can provision their own infrastructure

## Strengths

- Owns the full stack down to metal, which founder Jake Cooper frames as the economic basis for agent-scale workloads

## Weaknesses / caveats

- Security incident on 2026-10-21: an unauthorized party may have accessed customers' encrypted environment variables and decrypted some (API keys, database and registry credentials). Railway tied it to a series of attacks on platform companies aimed at AI inference providers, told all users to rotate stored secrets, and paused all deployments while investigating, so new keys could not be rolled out. See [AI developer supply chain attacks](../trends/ai-developer-supply-chain-attacks.md)
- Suffered a major GCP-linked outage on 2026-05-19 (workload discoverability was still tied to GCP despite the multi-cloud mesh); post-mortem published
- Single founder interview as the only source; economics and user figures are self-reported

## Recent changes

- [2026-10-21] Security disclosure: customer environment variables possibly decrypted; all users told to rotate secrets while deployments were paused
- [2026-05-20] Latent Space interview: bare-metal economics, Central Station, agent-safe production forks, progressive rollouts, "the pull request is dying," CLI over canvas

## Sources

- [Railway: The Agent-Native Cloud — Jake Cooper](../sources/newsletters/railway-agent-native-cloud-2026-05-20.md)
- [Railway — Security Disclosure: Wednesday October 21st](../sources/articles/railway-security-disclosure-2026-10-21.md)
- [Every — The agents on Every's Railway response team](../sources/newsletters/every-railway-response-agents-2026-10-22.md)
