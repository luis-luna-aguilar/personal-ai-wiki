---
title: NVIDIA OpenShell
type: tool
domains: [cybersecurity, agents]
subcategory: agent-sandbox-infra
tags: [open-source, agentic]
as_of: 2026-09-30
sources: [ainews-devday-agent-safety-roundup-2026-09-30]
---

# NVIDIA OpenShell

NVIDIA OpenShell is an open-source sandbox for local and open agents. Its pitch is that agents should be held back by limits the runtime enforces, not by rules written into the prompt. Unlike [E2B](e2b.md) or [Daytona](daytona.md), it is not a managed compute service: it is software you run around your own agents.

## Current status (as of 2026-09-30)

- Shipped as open source in late September 2026, alongside NVIDIA's "Open Agent Safety Platform"
- Over 100 firms joined the safety platform, among them Anthropic, Microsoft, IBM, Cisco, Hugging Face, Mistral, Oracle, Red Hat, Salesforce, SAP and Siemens
- OpenAI, Google/DeepMind, Meta and Apple are absent from the platform's logo grid; commenters read OpenAI's absence as the most pointed
- Telemetry is on by default and opt-out, per NVIDIA's observability docs

## Weaknesses / caveats

- Default-on telemetry is a problem for privacy, compliance, and air-gapped or local-only deployments, the setups a local-agent sandbox is meant for
- Skeptics ask what it adds beyond mature isolation (firewalls, containers, VMs, seccomp/AppArmor, platform sandboxes); its case rests on agent-specific policy, observability, quotas, or tool and API mediation that the source does not detail

## Related

- [State of Cybersecurity](../state-of/cybersecurity.md) — listed under AI security tooling
- [Agent incidents in the wild](../trends/agent-incidents-in-the-wild.md) — the misbehaviour runtime sandboxes are meant to contain

## Recent changes

- [2026-09-30] Page created: NVIDIA shipped OpenShell; 100+ firms joined the safety platform, OpenAI did not; telemetry on by default.

## Sources

- [AINews — DevDay week agent-safety roundup](../sources/newsletters/ainews-devday-agent-safety-roundup-2026-09-30.md)
