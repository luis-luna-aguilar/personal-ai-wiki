---
title: Crabbox
type: tool
domains: [coding, agents]
subcategory: agentic-devops
tags: [cli, agentic]
as_of: 2026-07-08
sources: [crabbox-remote-execution-2026-07]
---

# Crabbox

Crabbox is a remote software testing and execution control plane. It keeps the local developer workflow as edit, save, run, but moves the actual command execution to owned or provider-backed remote capacity.

## Current status (as of 2026-07-08)

- CLI-driven workflow: `crabbox run -- <command>` leases or reuses a remote runner, syncs tracked non-ignored files, executes the command, streams output, records evidence, and releases or retains the target.
- Supports tests, builds, browser checks, platform validation, and review evidence when local compute is too slow, too small, or not representative.
- Execution modes include brokered cloud leases, direct SSH/static hosts, and delegated sandbox/proof runners.
- Brokered mode keeps cloud-provider credentials, lease state, cleanup, usage accounting, and cost guardrails in a coordinator rather than on individual machines.
- The docs explicitly position it as not being CI, a package manager, a production deployment platform, a hostile multi-tenant sandbox, or an automatic secret-sanitization layer.

## Strengths

- Gives AI agents and reviewers auditable command output from the environment that actually ran.
- Fits PR review and eval workflows where proof artifacts matter more than local reproduction.
- Supports heterogeneous targets, including cloud Linux runners, Windows/WSL2, EC2 Mac, static SSH hosts, and sandbox providers.

## Weaknesses / caveats

- The source is documentation, not adoption evidence; durability and ecosystem use still need more signals.
- Remote execution can expose secrets through command output or artifacts if teams do not design guardrails.
- It complements CI but does not replace CI policy, production deployment controls, or hostile sandbox isolation.

## Recent changes

- [2026-07-08] Crabbox docs captured as a remote execution / proof-artifact control plane for coding agents and PR review workflows.

## Sources

- [Crabbox remote execution docs](../sources/articles/crabbox-remote-execution-2026-07.md)
