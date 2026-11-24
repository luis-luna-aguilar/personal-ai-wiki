---
title: Anthropic — Using Claude to reduce the attack surface of code
type: source
source_type: article
source_file: raw/articles/2026-11-23-anthropiccom-research-attack-surface-reduction.md
url: https://www.anthropic.com/research/attack-surface-reduction
published: 2026-10-20
ingested: 2026-11-24
domains: [cybersecurity]
---

# Anthropic — Using Claude to reduce the attack surface of code

Chris Rohlf previews Anthropic's research into automated attack-surface analysis and reduction. Claude maps the code a deployment exposes and moves what it does not need behind a gate, such as authentication, opt-in or a later protocol state. The argument is that fixing individual bugs scales poorly, while reducing reachability lowers the severity of unknown vulnerabilities, including ones already being exploited, without having to find them.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — attack-surface reduction and OpenSSH bullets under AI-assisted vulnerability detection

## Key claims extracted
- Three methods: default-configuration reachability, configuration interactions, early reachability (before authentication, without victim interaction, or before a protocol state transition)
- 25 projects (5M+ lines; C, C++, Java, PHP, Python); 17,000+ configuration options inventoried, 3,842 security-relevant; 493 issues found
- All 11 gated projects had unintended reachable code: 93 unnecessary pre-auth surfaces in default configurations, 37 places where code ran or state was recorded before authentication, 61 combinations that weakened a pre-auth control
- 162 security-sensitive setting combinations were accepted without warning or documentation; 94 silently turned a control off; a hostname-based deny-rule pattern failed open in four unrelated projects; one conflict that dropped a client-certificate check had existed for 21 years
- OpenSSH 10.4: ~4,500 lines of ML-DSA-44 code (~16% of default sshd pre-auth code) were reachable even when the algorithm was excluded; Claude found two gaps in the 10.5 fix (advertised vs embedded key type; certificate CA signatures verified before configuration checks); the final fix in 10.6 removed roughly a fifth of pre-auth reachable code
- The techniques are combined into a three-pass Claude skill being integrated into OSS Scanner; each finding is confirmed with a dynamic trace, and default-config gates must leave the project's test results unchanged
