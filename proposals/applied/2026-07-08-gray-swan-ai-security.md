---
type: proposal
source: raw/newsletters/2026-06-22-red-teaming-after-mythos-zico-kolter-matt-fred.md
status: pending
created: 2026-07-08
---

# Proposal: Gray Swan and AI-native security

## Summary

The Gray Swan interview is a strong source for AI-native security: treat agents as untrusted systems, test indirect prompt injection and tool-use trajectories, and design guardrails around identity, permissions, and exfiltration risk. This updates cybersecurity state and harness/security concepts.

## Intended changes

- [x] **Update** `wiki/state-of/cybersecurity.md` — add AI-native agent security and Gray Swan tooling.
- [x] **Update** `wiki/concepts/harness.md` — add security as harness boundary.
- [x] **Create** `wiki/concepts/prompt-injection.md` — concise concept page if not present.
- [x] **Update** `wiki/index.md` — add prompt injection concept.
- [x] **Create** `wiki/sources/newsletters/gray-swan-ai-security-2026-06.md` — source summary.

## Page drafts

### wiki/state-of/cybersecurity.md (updated sections)

```md
### AI-specific attack surfaces

- **Indirect prompt injection** — tool-using agents fetch untrusted content while holding private context and action authority. Gray Swan frames this as a new exploit class for systems like Codex, Claude Code, OpenClaw, and computer-use agents because malicious instructions can enter through files, webpages, tickets, emails, or browser state rather than through the user's direct prompt. See [Prompt injection](../concepts/prompt-injection.md). *(as of 2026-06-22)*
- **Slopsquatting** — LLMs hallucinate ~20% of package names (USENIX Security 2025, 576k samples); attackers pre-register those names on PyPI/npm with malicious `postinstall` payloads. Mitigation: `slopcop` CLI checks registry age, download count, postinstall scripts, and Levenshtein distance before install. See [Slopsquatting](../concepts/slopsquatting.md). *(as of 2026-04-22)*

### AI security tooling

- **Gray Swan** — AI-native security company focused on adversarial testing and guardrails for models and agents. Its Shade automated red-teaming system is described as finding more breaks than human red teamers in fixed windows; Cygnal is positioned as a guardrail model for policy enforcement. Current source is Latent Space interview coverage. *(as of 2026-06-22)*

## Recent changes

- [2026-06-22] Gray Swan interview adds AI-native security framing: agents should be treated as untrusted systems; indirect prompt injection, identity, permissions, guardrails, and automated red teaming are core deployment concerns.
- [2026-07-02] Cognition launched Devin Security Swarm, pushing AI-assisted vulnerability detection toward parallel agent workflows that validate exploitability and generate fix PRs.
```

### wiki/concepts/harness.md (updated sections)

```md
## What good harness engineering looks like

- **Security boundary as harness boundary.** Tool-using agents are not only productivity systems; they are software components that may read untrusted content, hold private context, and take actions. A production harness must define identity, permissions, data exfiltration boundaries, guardrails, red-team tests, and audit trails as part of the agent architecture.

## Recent changes

- [2026-06-22] Gray Swan security coverage adds prompt injection, exfiltration, identity, permissions, and automated red teaming as harness-boundary concerns for tool-using agents.
- [2026-07-08] Gemini API managed agents add hosted harness primitives: MCP support, background execution, custom function calling, credential refresh, and stateful agent interactions.
```

### wiki/concepts/prompt-injection.md (new)

```md
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
```

### wiki/index.md (updated line)

```md
- [concepts/prompt-injection](concepts/prompt-injection.md) — AI-specific attack where untrusted content steers a model or agent, especially dangerous when agents combine private context, tools, and action authority *(as_of: 2026-06-22)*
```

### wiki/sources/newsletters/gray-swan-ai-security-2026-06.md (new)

```md
---
title: Gray Swan on AI-native security and prompt injection
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-22-red-teaming-after-mythos-zico-kolter-matt-fred.md
url: https://www.latent.space/p/gray-swan
published: 2026-06-22
ingested: 2026-07-08
domains: [cybersecurity, agents, computer-use]
---

# Gray Swan on AI-native security and prompt injection

Latent Space interviews Gray Swan cofounders Zico Kolter and Matt Fredrikson about AI-native security. They frame tool-using agents as untrusted systems with new vulnerabilities: indirect prompt injection, data leakage, bad tool calls, agent identity problems, and correlated failures across widely used models and harnesses.

## Influenced pages

- [State of Cybersecurity](../../state-of/cybersecurity.md) — adds indirect prompt injection and Gray Swan tooling.
- [Harness](../../concepts/harness.md) — adds security boundary as harness boundary.
- [Prompt injection](../../concepts/prompt-injection.md) — creates concept page.

## Key claims extracted

- AI systems introduce vulnerabilities distinct from traditional cybersecurity problems.
- Indirect prompt injection matters because agents read untrusted content while holding private context and action authority.
- Gray Swan's Shade system is described as automated red teaming that can find more breaks than humans in fixed windows.
- Cygnal is positioned as guardrail infrastructure for policy enforcement.
- Computer-use agents and OpenClaw-style systems create a usability/security tradeoff because their usefulness comes from broad authority.
```

## Schema / vocabulary additions

None.
