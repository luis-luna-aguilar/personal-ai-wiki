---
type: proposal
sources:
  - raw/newsletters/2026-03-12-perplexity-ships-your-digital-proxy.md
  - raw/newsletters/2026-03-12-perplexity-launches-personal-computer.md
  - raw/newsletters/2026-03-12-ainews-replit-agent-4-the-knowledge-work-agent.md
status: pending
created: 2026-04-22
---

# Proposal: Perplexity Personal Computer

## Summary

The wiki already captures Perplexity Computer as a computer-use product and notes that Personal Computer exists. What is missing is the sharper March framing: an always-on dedicated Mac mini, remotely controllable from any device, positioned as a persistent digital proxy rather than just another automation feature.

This proposal strengthens the current Perplexity and computer-use pages and adds a proper source summary for the March launch cluster.

## Intended changes

- [x] **Update** `wiki/tools/perplexity-computer.md` — make the Personal Computer framing more explicit in the body
  > See diff snippet below.

- [x] **Update** `wiki/state-of/computer-use.md` — sharpen the Perplexity line so it reflects the dedicated-machine / digital-proxy pattern rather than only integrations and pricing
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/perplexity-personal-computer.md` — source summary page for the March launch cluster
  > See full draft below.

## Page drafts

### wiki/tools/perplexity-computer.md (updated snippet)

```markdown
## Current status (as of 2026-04-10)

- Exclusively available on Perplexity Max ($200/month); 10,000 credits/month, consumption varies by task complexity
- Enterprise tier at $325/seat/month with security controls and audit logs
- Connects to 400+ applications (Slack, Gmail, GitHub, Notion) and 12,000+ financial institutions via Plaid
- Personal Computer, launched 2026-03-11, frames the product as a persistent digital proxy: an always-on Mac mini environment with ongoing access to files, apps, and sessions that can still be remotely controlled from any device

## Strengths

- Multi-model orchestration avoids single-model bottlenecks; each subtask gets the best-fit model
- Deep third-party integrations (400+ apps, 12,000+ financial institutions via Plaid)
- Dedicated-machine model makes "always-on agent" behavior more concrete than a normal chat surface
- Local-ish Personal Computer variant addresses privacy-sensitive and continuity-sensitive workloads better than purely ephemeral sessions
```

### wiki/state-of/computer-use.md (updated snippet)

```markdown
### Computer use

Autonomous agents that orchestrate models, connect to external services, and execute complex workflows through application interfaces.

- [[tools/claude-cowork]] — Anthropic's March 2026 computer-use push widened Claude from chat/terminal workflows into remote desktop control and unattended knowledge-work execution; later April Cowork / Live Artifacts moves now read as expansion of that direction rather than a separate product idea *(as of 2026-04-10 for current page state; March launch context added from 2026-03-24 to 2026-03-31 sources)*
- [[tools/perplexity-computer]] — Perplexity's strongest distinctive bet is the persistent digital-proxy model: an always-on dedicated Mac mini environment, remotely controllable from any device, layered on top of 19-model orchestration plus 400+ app and 12,000+ financial-institution connectivity *(as of 2026-04-10)*
```

### wiki/sources/newsletters/perplexity-personal-computer.md (new)

```markdown
---
title: Perplexity Personal Computer
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-12-perplexity-launches-personal-computer.md
published: 2026-03-12
ingested: 2026-04-22
domains: [computer-use, agents]
---

# Perplexity Personal Computer

This source summary groups the March 12 launch cluster around Perplexity Personal Computer. The durable signal is not only that Perplexity added more integrations, but that it made the "persistent agent on its own machine" pattern concrete with a dedicated Mac mini environment that remains reachable from anywhere.

## Influenced pages

- [[tools/perplexity-computer]] — clarifies the product's digital-proxy framing and dedicated-machine model
- [[state-of/computer-use]] — sharpens the category signal around persistent computer-use agents

## Key claims extracted

- Personal Computer was framed as a continuously running Mac mini environment for an AI agent
- The product keeps access to files, apps, and sessions alive over time instead of treating each task as an isolated chat request
- Users can control the environment remotely from other devices, making the agent feel like a persistent proxy rather than a local-only helper
- The launch reinforced Perplexity's broader move toward multi-model, multi-app orchestration rather than pure answer-engine behavior
```

## Open questions

- Please remove anything related to live artifacts from the computer use files. That's not a computer use example.
