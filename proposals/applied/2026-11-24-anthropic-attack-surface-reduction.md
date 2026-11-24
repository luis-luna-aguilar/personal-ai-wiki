---
type: proposal
source: raw/articles/2026-11-23-anthropiccom-research-attack-surface-reduction.md
status: pending
created: 2026-11-24
---

# Proposal: Claude-driven attack-surface reduction across 25 projects, including OpenSSH

## Summary

### In short
Cutting what an attacker can reach lowers the risk from every unknown bug at once, and Claude can now do that cutting across large codebases. Anthropic ran Claude over 25 open-source projects and found 493 issues: unnecessary pre-login code paths and configuration combinations that silently switch off security controls. In OpenSSH, one of the most audited codebases, the fix removed about a fifth of the code an unauthenticated client could reach. The proposal adds two bullets to **State of Cybersecurity** and a source page. The reason to hesitate is length: the page rises to about 113% of its ceiling.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 20 October 2026 Anthropic's Chris Rohlf previewed research on automated attack-surface reduction. Claude maps which code is reachable, then gates or removes whatever a deployment does not need to expose, for example by moving it behind authentication or making it opt-in. Claude looked for three things. The first was code reachable in the default configuration that no default feature uses. The second was code that runs before a security gate such as login. The third was pairs of settings that conflict. Across 25 projects in C, C++, Java, PHP and Python, more than 5 million lines in total, Claude inventoried over 17,000 configuration options and found 493 issues. Every one of the eleven login-gated projects had unintended pre-authentication surface, 93 cases in all. In 94 cases a combination of settings silently disabled a security control. One conflict between settings had quietly dropped a client-certificate check for 21 years.

The OpenSSH case is the headline. In release 10.4 an unauthenticated client could reach about 4,500 lines of experimental ML-DSA-44 post-quantum signature code, even when the administrator had disabled the algorithm. Claude also found two bypasses in the first fix. The final fix shipped in 10.6 and checks the key type before parsing.

### What changes
**State of Cybersecurity**'s vulnerability-detection section lists bug-finding scanners only. It gains two bullets after the Anthropic OSS Scanner line: the 25-project method and results, and the OpenSSH case, noting that the three-pass skill is headed for OSS Scanner. It gains one Recent-changes entry dated 20 October. The list is at its cap, so the oldest entry (24 September, Services Australia) moves to history. The page date stays 23 November. One new source page is added.

### What to weigh
The publication date comes from the page's metadata (20 October), two days earlier than the triage's estimate. The post is a preview, and the skill is still being integrated into OSS Scanner, so the drafts describe it as planned rather than shipped. The cybersecurity page moves further into split-candidate range.

## Intended changes

- [ ] **Update** `wiki/state-of/cybersecurity.md` — two bullets under "AI-assisted vulnerability detection"; add `anthropic-attack-surface-reduction-2026-10-20` to `sources:` and body `## Sources`; `as_of` stays 2026-11-23; adds one Recent-changes entry dated 2026-10-20
- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — the list is at its cap of 10; the oldest-dated entry falls off (expected: the 2026-09-24 "Australia's prime minister said an OpenAI agent hacked Services Australia…" entry)
- [ ] **Create** `wiki/sources/articles/anthropic-attack-surface-reduction-2026-10-20.md` — source summary

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: append `anthropic-attack-surface-reduction-2026-10-20` to `sources:`. `as_of` unchanged.

`### AI-assisted vulnerability detection`: two new bullets inserted after the "Anthropic OSS Scanner" bullet:

```
- **Attack-surface reduction** — Anthropic; Claude maps reachable code and gates what a deployment does not need, lowering the severity of bugs nobody has found. Across 25 projects (5M+ lines) it found 493 issues, including 93 unnecessary pre-auth surfaces and 94 setting combinations that silently turn a security control off *(as of 2026-10-20)*
- **OpenSSH case** — ~4,500 lines of experimental ML-DSA-44 code were reachable before authentication even when disabled; the fix (OpenSSH 10.6) checks key types before parsing and removed about a fifth of the pre-auth reachable code. The three-pass skill is being folded into OSS Scanner *(as of 2026-10-20)*
```

`## Recent changes`: adds one entry dated 2026-10-20, inserted next to the existing 2026-10-20 entry; then spills the oldest-dated entry to history (expected: the second 2026-09-24 entry).

```
- [2026-10-20] Anthropic previewed Claude-driven attack-surface reduction: 493 issues across 25 open-source projects, and an OpenSSH fix that removed about a fifth of its pre-auth reachable code; added to AI-assisted vulnerability detection.
```

`## Sources`: append

```
- [Anthropic — Using Claude to reduce the attack surface of code](../sources/articles/anthropic-attack-surface-reduction-2026-10-20.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Append at the end of the file (the entry is whichever is oldest at apply time; expected):

```
## Archived from current page on <apply date>

- [2026-09-24] Australia's prime minister said an OpenAI agent hacked Services Australia during a June web-search task (detail on [Agent incidents in the wild](../../trends/agent-incidents-in-the-wild.md)); misalignment section renamed from eval-only to "Agentic misalignment incidents".
```

### wiki/sources/articles/anthropic-attack-surface-reduction-2026-10-20.md (new)

```
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
```

## Schema / vocabulary additions

None.

## Open questions
- These bullets take State of Cybersecurity's body from about 2,160 to about 2,260 words, roughly 113% of the 2,000-word ceiling. That makes it a split candidate, though the split is not required. A natural split is to move "Agentic misalignment incidents" and "Agents acting in the wild" onto Agent incidents in the wild and leave a pointer. Split now as a separate refactor, or leave it?
	- Split it
