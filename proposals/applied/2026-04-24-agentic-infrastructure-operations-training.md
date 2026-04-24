---
type: proposal
source: raw/deep-research/2026-04-24 Agentic Devops.md
status: applied
created: 2026-04-24
---

# Proposal: Training page for safe agentic infrastructure operations

## Summary

The wiki currently has almost no practical guidance for how agents should operate around live infrastructure. This report is broad, but its durable contribution is clear: infrastructure agents need stricter governance than ordinary coding agents. They should gather context freely, propose actions clearly, and execute mutations only through explicit approval gates, deterministic policy layers, and isolated runtimes.

This proposal creates a new training page focused on safe agentic infrastructure operations, then threads it into the existing enablement and review-friction pages. It also adds a source summary for the report.

## Intended changes

- [x] **Create** `wiki/training/agentic-infrastructure-operations.md`
- [x] **Create** `wiki/sources/deep-research/2026-04-24-agentic-devops.md`
- [x] **Update** `wiki/training/company-wide-ai-enablement.md`
- [x] **Update** `wiki/training/anti-autopilot-review-friction.md`
- [x] **Update** `wiki/index.md`

## Page draft

### `wiki/training/agentic-infrastructure-operations.md` (new)

```md
---
title: Agentic infrastructure operations
type: training
domains: [agents, coding]
as_of: 2026-04-24
sources: [agentic-devops-deep-research]
---

# Agentic infrastructure operations

Agentic infrastructure operations is the practice of using AI agents around live production systems without letting them become an unbounded source of operational risk. The recurring lesson is simple: infrastructure agents are useful long before they are safe to trust with unsupervised mutations. The winning pattern is not "full autonomy." It is controlled autonomy.

## Current guidance

- Let infrastructure agents read freely, but gate mutations explicitly
- Prefer propose-only workflows before mutate-with-approval workflows
- Use deterministic policy layers for enforcement; do not rely on prompt text alone
- Standardize tool connectivity through protocols such as MCP instead of one-off wrappers where possible
- Sandbox all agent-generated code or remediation scripts away from primary hosts
- Verify after changes using synthetic checks, cluster health checks, or other post-action evidence

## Practical execution ladder

A useful operating model for infrastructure agents has three modes:

1. **Read-only** — gather telemetry, inspect config, correlate logs, retrieve runbooks
2. **Propose-only** — open tickets, draft PRs, generate rollback plans, suggest commands
3. **Mutate-with-approval** — execute a change only after a human explicitly approves it and only through controlled tooling

The exact labels are less important than the structure. Infrastructure work is high-blast-radius work. Human approval should disappear last, not first.

## Why prompt-only safety is not enough

The core operational mistake is assuming the model can reliably enforce its own limits. In practice, safe infrastructure agents need a harness that can:

- separate reads from writes
- validate tool inputs structurally
- block prohibited actions deterministically
- record who approved what
- preserve enough context and artifacts to replay the run later

This is one of the clearest places where harness quality matters more than model quality.

## Standard tool-access layer

Protocolized tool access matters more in infrastructure than in lighter-weight workflows because the environment is large, heterogeneous, and high-risk. MCP is useful here not only as a generic integration protocol, but as a way to make observability tools, infra tools, and policy-enforced actions legible and reusable across agents.

The practical goal is not protocol purity. It is reducing bespoke glue and making execution surfaces auditable and replaceable.

## Sandboxing and verification

Infrastructure agents should never execute generated scripts directly on primary hosts. Even when the action is low risk, the execution surface should be isolated. Sandboxes matter for two separate reasons:

- they reduce blast radius when the agent generates bad code or bad shell commands
- they make replay and forensic inspection easier after something goes wrong

Verification should continue after the action. A safe infra loop is:

1. inspect
2. plan
3. approve
4. execute in a controlled runtime
5. verify outcome against the original intent

## Failure modes

- Treating diagnosis success as proof that mutation is safe
- Prompting the model to "be careful" instead of enforcing policy in code
- Letting agents execute generated scripts on shared hosts
- Using custom wrappers everywhere and losing auditability and portability
- Treating infrastructure changes as complete when the command returned 0 instead of when the system state is actually verified

## Open questions

- Which infrastructure actions are low-risk enough to graduate from propose-only to mutate-with-approval first?
- What evidence is sufficient to promote an infrastructure agent toward narrower pockets of bounded autonomy?
- Where should policy enforcement live: tool wrapper, runtime, cluster policy layer, or all three?

## Sources

- [[sources/deep-research/2026-04-24-agentic-devops]]
```

### `wiki/sources/deep-research/2026-04-24-agentic-devops.md` (new)

```md
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
```

### `wiki/training/company-wide-ai-enablement.md` (update)

Add under `## Current guidance`:

```md
- For production infrastructure workflows, start even narrower than normal: read-only first, then propose-only, then mutate-with-approval after explicit evidence that the agent can operate safely
```

Add to `## See also`:

```md
- [[training/agentic-infrastructure-operations]] — practical guidance for safe agent use around production infrastructure, deployment safety, and post-action verification
```

### `wiki/training/anti-autopilot-review-friction.md` (update)

Add under `## Proven patterns`:

```md
- **Human gate on infrastructure mutations.** In production ops, review friction should not disappear as the agent gets more capable. It should become more explicit: read actions can flow, but writes pause for human approval and post-action verification.
```

### `wiki/index.md` (update)

Add under `## Training`:

```md
- [[training/agentic-infrastructure-operations]] — safe operating patterns for infrastructure agents: read-only diagnosis, propose-only plans, approval-gated mutations, sandboxing, and post-deploy verification *(as_of: 2026-04-24)*
```
