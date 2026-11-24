---
type: proposal
source: raw/articles/2026-11-23-openaicom-business-solutions-cybersecurity.md
status: pending
created: 2026-11-23
---

# Proposal: OpenAI "AI for Cybersecurity Teams" solutions page

## Summary

### In short
OpenAI now sells cyber defense as one product family under the Daybreak name. Model access comes in two tiers: Blue, general-purpose models for defensive work with fewer refusals, and Red, specialized models for authorized exploit work. Codex Security tooling ships as a plugin, a remote "Defense Factory", a CLI, CI scans and an SDK. The proposal refreshes two stale lines on **State of Cybersecurity**, finally defines "Daybreak Blue" there, and logs the tooling on **Codex**. The one hesitation is that the page is undated, so 23 November is the fetch date, not a publication date.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
This is OpenAI's business-solutions page for security teams, fetched on 23 November 2026. It lays out OpenAI's cyber offering more clearly than any earlier source in the wiki, arguing that AI is speeding up attackers, defenders' window is narrowing, and defense has to become continuous.

Access to models runs through Daybreak, which the page describes as "approved access for cybersecurity work" in two tiers. Daybreak Blue gives supported general-purpose models for defensive tasks such as code review, vulnerability investigation and remediation, with fewer unnecessary refusals. Daybreak Red gives specialized cyber models for authorized research such as exploit development, penetration testing and red teaming, behind additional verification and access controls. Teams apply for either.

On the tooling side, the page describes a six-step agent loop (discover a possible vulnerability, validate that it is reachable and exploitable, prioritize by impact, assign it to the owning team, draft a patch with tests, verify the patch closes the attack path) and the products that run it. The Daybreak Defense Factory runs scans and patching remotely, with a reference architecture for teams to build their own; the Daybreak plugin does the same inside Codex with findings kept locally; PR review checks pull requests for reintroduced vulnerabilities. Underneath sit the Codex Security CLI, which also runs in CI, and a Codex Security SDK for TypeScript.

### What changes
Until now the wiki described Daybreak only as a program that launched GPT-5.6-Cyber for approved defenders, and its October entry on OpenCode called "Daybreak Blue" undefined. The Codex security line still dates from March.

- **State of Cybersecurity**: the Daybreak line now names the Blue and Red tiers; the Codex line under vulnerability detection moves from a March "Codex Security feature" description to the current CLI, CI, SDK, PR review, plugin and Defense Factory set; the OpenCode line's "undefined in the source" note becomes a pointer to the Blue tier. One Recent-changes entry is added; the list is at its cap of 10, so the oldest entry (the 9 September note on splitting out the OpenAI–Hugging Face incident page) moves to history. Body grows about 25 words, to roughly 105% of the ceiling (warning band). Page date moves to 23 November.
- **Codex** gains a Recent-changes entry for the Codex Security and Daybreak surfaces; its list is also at cap, so the 11 July rollout-friction entry moves to history. Page date moves to 23 November.
- One new source page.

### What to weigh
The page carries no publication date, so every derived line is dated 23 November, the fetch date; some of these surfaces may have launched earlier. The rewritten Daybreak line drops the Chrome V8 example from the August GPT-5.6-Cyber launch to stay within the bullet length limit; that detail remains in the page's history file.

## Intended changes

- [ ] **Update** `wiki/state-of/cybersecurity.md` — rewrite the Codex bullet under "AI-assisted vulnerability detection", the OpenAI Daybreak bullet under "Trusted defensive access", and the OpenCode bullet under "Agents acting in the wild"; add `openai-cybersecurity-solutions-page` to `sources:` and body `## Sources`; `as_of` → 2026-11-23; adds one Recent-changes entry dated 2026-11-23
- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — oldest Recent-changes entry falls off (expected: the 2026-09-09 "Split the OpenAI–Hugging Face incident…" entry)
- [ ] **Update** `wiki/tools/codex.md` — adds one Recent-changes entry dated 2026-11-23; add source to `sources:` and `## Sources`; `as_of` → 2026-11-23
- [ ] **Spill** `wiki/tools/codex.md` → `wiki/history/tools/codex.md` — oldest Recent-changes entry falls off (expected: the 2026-07-11 rollout-friction entry)
- [ ] **Create** `wiki/sources/articles/openai-cybersecurity-solutions-page.md` — source summary

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: `as_of: 2026-11-23`; append `openai-cybersecurity-solutions-page` to `sources:`.

Under `### AI-assisted vulnerability detection`, replace the Codex bullet:

> **Before:** `- [Codex](../tools/codex.md) — Codex Security feature expands the coding agent into vulnerability review and validation work beyond code generation *(as of 2026-03-09)*`

```
- [Codex](../tools/codex.md) — OpenAI; Codex Security now spans a CLI, CI scans, a TypeScript SDK and PR review, plus the Daybreak plugin (local scans and patches in Codex) and Daybreak Defense Factory (remote scan-to-patch runs), framed as a discover, validate, prioritize, assign, patch and verify loop *(as of 2026-11-23)*
```

Under `### Trusted defensive access`, replace the Daybreak bullet:

> **Before:** `- **OpenAI Daybreak** — official OpenAI program combining frontier models, Codex, and security partners to accelerate defensive workflows. On 2026-08-11, OpenAI launched **GPT-5.6-Cyber** under an expanded Daybreak initiative, restricted to "approved defenders," already used to find previously-unknown bugs including in Chrome V8 *(as of 2026-08-11)*`

```
- **OpenAI Daybreak** — OpenAI's approved-access program for cyber work, in two tiers: **Blue**, general-purpose models for defensive work with fewer unnecessary refusals, and **Red**, specialized cyber models for authorized exploit development, penetration testing and red teaming behind extra verification; GPT-5.6-Cyber launched under it on 2026-08-11 *(as of 2026-11-23)*
```

Under `### Agents acting in the wild`, replace the OpenCode bullet (claim date unchanged):

> **Before:** `... eased after access to "Daybreak Blue", undefined in the source (OpenAI runs a Daybreak cyber-defense initiative) *(as of 2026-10-20)*`

```
- **OpenCode agent-swarm attack** — open-source coding agent hit by a 48-hour agent-swarm attack; frontier models refused to help analyze the payloads (Hugging Face reportedly hit the same wall); eased after access to Daybreak Blue, OpenAI's defensive model-access tier (see Trusted defensive access) *(as of 2026-10-20)*
```

`## Recent changes` — insert at top (adds one entry dated 2026-11-23; the list is at cap 10, so the oldest entry spills):

```
- [2026-11-23] OpenAI's cybersecurity solutions page defines Daybreak's two access tiers (Blue for defensive work, Red for authorized offensive research) and lists the Codex Security surfaces (CLI, CI, SDK, PR review, Daybreak plugin, Defense Factory); Daybreak and Codex lines refreshed, OpenCode line's "undefined" note resolved.
```

`## Sources` — append:

```
- [OpenAI — AI for Cybersecurity Teams solutions page](../sources/articles/openai-cybersecurity-solutions-page.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Append under the existing `## Archived from current page on 2026-11-23` block (open a new block with that header if none exists for the apply date):

```
- [2026-09-09] Split the OpenAI–Hugging Face incident and Anthropic's own agentic-misalignment disclosure out into a dedicated page, [OpenAI–Hugging Face agentic cyber incident](../../trends/openai-huggingface-cyber-incident.md), given how much of this page's recent history the incident's follow-on developments had come to occupy.
```

### wiki/tools/codex.md (updated)

Frontmatter: `as_of: 2026-11-23`; append `openai-cybersecurity-solutions-page` to `sources:`.

`## Recent changes` — insert at top (adds one entry dated 2026-11-23; the list is at cap 10, so the oldest entry spills):

```
- [2026-11-23] OpenAI's cybersecurity solutions page lists Codex's security surfaces: the Daybreak plugin (scans and patches in Codex, findings stored locally), Daybreak Defense Factory (remote scan-and-patch runs, plus a reference architecture to build your own), PR review, the Codex Security CLI and CI scans, and a TypeScript Codex Security SDK; see [State of Cybersecurity](../state-of/cybersecurity.md).
```

`## Sources` — append:

```
- [OpenAI — AI for Cybersecurity Teams solutions page](../sources/articles/openai-cybersecurity-solutions-page.md)
```

### wiki/history/tools/codex.md (updated)

Append under the existing `## Archived from current page on 2026-11-23` block (open a new block with that header if none exists for the apply date):

```
- [2026-07-11] Rollout friction: 36-plus model/effort configuration combinations drew complaints; OpenAI ran multiple usage-limit resets and rolled the context limit back from 372K to 272K.
```

### wiki/sources/articles/openai-cybersecurity-solutions-page.md (new)

```
---
title: OpenAI — AI for Cybersecurity Teams solutions page
type: source
source_type: article
source_file: raw/articles/2026-11-23-openaicom-business-solutions-cybersecurity.md
url: https://openai.com/business/solutions/cybersecurity/
ingested: 2026-11-23
domains: [cybersecurity]
---

# OpenAI — AI for Cybersecurity Teams solutions page

OpenAI's business-solutions page for security teams, which argues that AI is narrowing defenders' window and that defense must become continuous. It defines Daybreak as approved model access for cyber work in two tiers: Daybreak Blue (general-purpose models for defensive work such as code review, vulnerability investigation and remediation, with fewer unnecessary refusals) and Daybreak Red (specialized cyber models for authorized exploit development, penetration testing and red teaming, with additional verification and access controls). It lists the tooling for a six-step discover, validate, prioritize, assign, remediate, verify loop: Daybreak Defense Factory, the Daybreak plugin for Codex, PR review, the Codex Security CLI, CI scans, the Codex Security SDK and the OpenAI API. The page has no publication date; content reflects the page as fetched 2026-11-23.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Daybreak tiers defined; Codex vulnerability-detection line refreshed; OpenCode line's Daybreak Blue reference resolved
- [Codex](../../tools/codex.md) — Recent-changes entry for the Codex Security and Daybreak surfaces

## Key claims extracted
- Daybreak provides approved access for cybersecurity work; teams apply
- Daybreak Blue: supported general-purpose models for defensive work, with fewer unnecessary refusals
- Daybreak Red: specialized cyber models for authorized exploit development, penetration testing and red teaming, with additional verification and access controls
- Daybreak Defense Factory runs scans and patching remotely; OpenAI offers a reference architecture to build your own
- Daybreak plugin scans and creates patches in Codex, with scans running and findings stored locally
- Codex Security CLI scans code or changes from the terminal and can run in CI; Codex Security SDK integrates scans into TypeScript applications
- PR review checks pull requests to avoid reintroducing vulnerabilities
```

## Schema / vocabulary additions

None.

## Open questions

None.
