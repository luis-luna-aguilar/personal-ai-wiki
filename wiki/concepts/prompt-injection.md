---
title: Prompt injection
type: concept
domains: [cybersecurity, agents]
tags: [agentic]
as_of: 2026-06-22
sources: [gray-swan-ai-security-2026-06, lennysan-simonw-interview]
---

# Prompt injection

Prompt injection is an attack where instructions from untrusted content override or redirect an AI system's intended behavior. In agent systems, the most important variant is indirect prompt injection: the attacker does not prompt the model directly. They place malicious instructions in a webpage, file, ticket, email, repo, document, or other content the agent later reads.

## Current status

- The risk is highest when an agent combines untrusted content, private data, and authority to take actions or exfiltrate information.
- Coding agents and computer-use agents are especially exposed because they routinely read repos, webpages, logs, issues, browser state, and other externally controlled text.
- Prompt injection is not solved by asking the model to "ignore malicious instructions"; production systems need permissions, data boundaries, tool controls, guardrails, and adversarial tests.

## The lethal trifecta

Simon Willison's framing names the exact condition under which prompt injection becomes unfixable with current techniques: when an agent has **all three** of —

1. Access to private data
2. Exposure to untrusted content (incoming emails, scraped web pages, third-party documents)
3. The ability to send data externally (reply to email, post to an API, write to a public channel)

— a malicious instruction hidden in the untrusted content can override the agent's intended behavior and use its own access and authority to exfiltrate the private data. No prompt-level defense reliably closes this gap once all three conditions hold; Willison has predicted a "Challenger disaster" for AI security if a major exploit along these lines hasn't already happened quietly. The practical review question for any new agent design: does this agent have all three legs of the trifecta? If so, the fix is architectural (remove one leg) rather than a better system prompt.

## Why it matters

Prompt injection turns useful agent behavior into an attack surface. The same capability that lets an agent read context and act across tools also lets hostile context steer the agent unless the harness constrains what the model can see, do, and transmit. See [Harness (agent)](harness.md) for how the security boundary is meant to sit inside overall harness design.

## Sources

- [Gray Swan AI security interview](../sources/newsletters/gray-swan-ai-security-2026-06.md)
- [Lenny Rachitsky — Simon Willison interview takeaways](../sources/tweets/lennysan-simonw-interview.md)
