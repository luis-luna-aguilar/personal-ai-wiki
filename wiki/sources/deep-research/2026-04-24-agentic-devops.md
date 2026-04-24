---
title: Agentic infrastructure and operations
type: source
source_type: deep-research
source_file: raw/deep-research/2026-04-24 Agentic Devops.md
published: 2026-04-24
ingested: 2026-04-24
domains: [agents, coding]
---

# Agentic infrastructure and operations

Deep-research synthesis on production-grade AI tooling for infrastructure operations: Kubernetes-native agent runtimes, incident triage agents, deterministic policy engines, execution sandboxes, and post-deploy verification. Treat as an operational map rather than a canonical ranking of vendors or products.

## Influenced pages

- [[training/agentic-infrastructure-operations]] — new training page for safe agentic operations around live infrastructure
- [[training/company-wide-ai-enablement]] — infrastructure-specific example of staged autonomy and approval gating
- [[training/anti-autopilot-review-friction]] — why review friction matters more, not less, in production mutations
- [[tools/kagent]] — Kubernetes-native agent runtime / control plane
- [[tools/k8sgpt]] — Kubernetes diagnostics surface usable by humans and agents
- [[tools/skyflo]] — approval-gated AI control layer for Kubernetes and CI/CD
- [[tools/checkly]] — post-deploy synthetic verification with Playwright and Monitoring as Code

## Key claims extracted

- Infrastructure agents are most useful when integrated into observability and control planes, not only as code generators
- High-risk agent actions should separate read-only, propose-only, and mutate-with-approval modes
- Deterministic policy engines are becoming a critical safety layer for state-mutating operations
- MCP and similar protocol layers matter operationally because they reduce custom glue in high-risk environments
- Sandboxed execution and post-deploy verification are mandatory parts of safe agentic operations
