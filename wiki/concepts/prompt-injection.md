---
title: Prompt injection
type: concept
domains: [cybersecurity, agents]
tags: [agentic]
as_of: 2026-06-22
sources: [gray-swan-ai-security-2026-06]
---

# Prompt injection

Prompt injection is an attack where instructions from untrusted content override or redirect an AI system's intended behavior. In agent systems, the most important variant is indirect prompt injection: the attacker does not prompt the model directly. They place malicious instructions in a webpage, file, ticket, email, repo, document, or other content the agent later reads.

## Current status

- The risk is highest when an agent combines untrusted content, private data, and authority to take actions or exfiltrate information.
- Coding agents and computer-use agents are especially exposed because they routinely read repos, webpages, logs, issues, browser state, and other externally controlled text.
- Prompt injection is not solved by asking the model to "ignore malicious instructions"; production systems need permissions, data boundaries, tool controls, guardrails, and adversarial tests.

## Why it matters

Prompt injection turns useful agent behavior into an attack surface. The same capability that lets an agent read context and act across tools also lets hostile context steer the agent unless the harness constrains what the model can see, do, and transmit.

## Sources

- [Gray Swan AI security interview](../sources/newsletters/gray-swan-ai-security-2026-06.md)
