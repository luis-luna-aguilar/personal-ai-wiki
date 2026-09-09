---
title: "Cloudflare OS: an open platform for agents, apps, and work"
type: source
source_type: article
source_file: raw/articles/2026-09-07-blogcloudflarecom-cloudflare-os.md
url: https://blog.cloudflare.com/cloudflare-os/
ingested: 2026-09-08
domains: [agents]
---

# Cloudflare OS: an open platform for agents, apps, and work

Cloudflare open-sources a rebuilt version of Cloudflare OS: a per-person agent workspace with an isolated execution runtime, a Gatekeeper-based security/governance framework tracking what agents have observed, and a platform for personal, shareable, modifiable apps.

## Influenced pages

- [Company brain](../../concepts/company-brain.md) — full architecture description

## Key claims extracted

- Three parts: agent workspace, security/governance framework (Gatekeepers, observation log), personal-app platform
- Rebuilt because plain MCP tool-access control doesn't track what an agent has *observed*, only which tools it can call
- Every app runs as an independent lightweight Worker; sharing a "blueprint" gives code without data/credentials
- Available today, open source, deployable into any Cloudflare account
