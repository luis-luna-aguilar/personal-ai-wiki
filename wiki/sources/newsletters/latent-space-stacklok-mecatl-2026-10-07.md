---
title: Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-07-can-a-cloud-native-harness-make-agents-reliable-be.md
url: https://www.latent.space/p/stacklok
published: 2026-10-07
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)

Latent Space interview with Kubernetes co-creators Craig McLuckie and Joe Beda about Stacklok, which pivoted from software supply-chain security to Kubernetes-based agent infrastructure. Its main product is Mecatl, an open-source "cloud-native harness" (started June 2026) that separates the agent loop from client, model provider, state store, and execution environment so enterprises can run and govern agents centrally, the way Kubernetes did for containers.

## Influenced pages

- [Mecatl](../../tools/mecatl.md) — new page
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — Mecatl and the Stacklok control plane in the durable-harness section
- [State of Agents](../../state-of/agents.md) — Mecatl added under Agent frameworks

## Key claims extracted

- Desktop-first harnesses run the loop, local execution, and session state in one process or tightly coupled processes, even when pluggable
- "Lift and shift" into VMs, containers, or sandboxes causes problems with agent lifecycle and with quiescing (safely pausing while waiting for human input)
- Mecatl keeps the agent loop independent of client, model provider, state store, and execution environment; session management and memory move out of JSONL files on disk into manageable systems
- Beda: enterprise agent interactions belong to the enterprise and will be managed and governed like email
- Goal includes reducing enterprise dependency on frontier-lab harnesses (Codex, Claude Code, GitHub Copilot)
- ToolHive: open-source platform for running and governing MCP servers, now with a Kubernetes gateway, registry, and operator
- AI Gateway (not yet open source): access control, budgets, reporting, provider routing; no semantic per-task model routing, which McLuckie prefers inside the harness
- Customers are mostly regulated industries (banks, semiconductor companies, telcos); the commercial product is the "enterprise spine" control plane for identity, authorization, policy, and auditing
