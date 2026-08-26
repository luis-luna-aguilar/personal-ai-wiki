---
title: Crabbox remote execution docs
type: source
source_type: article
source_file: raw/articles/2026-07-08-tco-sej2xrpad1.md
url: https://openclaw.github.io/crabbox/
published: 2026-07-08
ingested: 2026-07-08
domains: [coding, agents]
---

# Crabbox remote execution docs

Crabbox is documented as a generic remote software testing and execution control plane. It leases or reuses remote machines, syncs tracked local files, executes repository commands remotely, streams output, records evidence, and releases or retains the target.

## Influenced pages

- [Crabbox](../../tools/crabbox.md) - tool page
- [AI PR and code review](../../workflows/ai-pr-code-review.md) - remote execution evidence
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) - proof-artifact infrastructure

## Key claims extracted

- Crabbox supports tests, builds, browser checks, platform validation, and review evidence on remote capacity.
- Brokered mode keeps cloud credentials in a coordinator rather than the CLI or runner.
- The data plane uses SSH/rsync directly from CLI to runner for SSH-backed providers.
