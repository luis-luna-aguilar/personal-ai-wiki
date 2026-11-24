---
type: proposal
source: raw/articles/2026-11-23-openaicom-index-introducing-shirudo.md
status: pending
created: 2026-11-23
---

# Proposal: OpenAI and Cisco introduce Shirudo

## Summary

### In short
AI is now being pointed at the gap between finding a vulnerability and patching it: OpenAI and Cisco's open-source Shirudo lets operators deploy temporary, signed eBPF "shields" on running Linux systems, with no restart needed. In a controlled test, a Codex-generated shield blocked a Java4Shell exploit against live Elasticsearch. The proposal adds a new `tools/shirudo.md` page, one bullet on **State of Cybersecurity**, and a source page. The reason to hesitate is the schema: no existing subcategory fits host runtime protection, so the page needs a new `runtime-security` subcategory.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 23 November 2026 OpenAI and Cisco announced Shirudo (Japanese for "shield"), an open-source runtime for protecting Linux systems while a patch is still being rolled out. A patch can take days or weeks to ship, and the exploit often uses the same operating-system operation as legitimate traffic, so blocking that operation outright would take the service down.

Shirudo's answer is a "shield": a small program built on eBPF, a Linux feature that lets tiny vetted programs run at specific hook points inside the kernel. A shield blocks only the behavior that exposes the vulnerability. Operators can watch how a proposed shield would affect real traffic before enforcing it, and nothing is deployed until they approve it. OpenAI and Cisco say they are designing it around four capabilities: live protection without restarts; programmable controls so agents can investigate a vulnerability, write a shield and validate it against exploits and real workloads; signed shields checked by Linux's eBPF verifier before loading; and a TPM (a hardware security chip) that keeps a verifiable record of shields being loaded or removed. The worked example: Codex generated a shield that added an input check to Java's Base64 decoder, attached it to a running Elasticsearch process, and the exploit attempt was rejected while Elasticsearch kept serving.

The code is BSD 2-Clause (eBPF programs dual BSD/GPL), and the stated goal is to publish tested shields alongside vulnerability disclosures. Greg Brockman frames it as the other half of AI bug-finding: finding a bug today doesn't mean every system can be patched tomorrow.

### What changes
The wiki's cybersecurity coverage is mostly about finding bugs (Claude Security, Daybreak, Glasswing) and sandboxing agents (OpenShell, SPACE); nothing yet covers protecting a running host before the fix lands.

- New page `tools/shirudo.md`: what a shield is, the four design capabilities, the Java4Shell demo and licensing, dated 23 November.
- **State of Cybersecurity** gains one Shirudo bullet under "AI security tooling" and one Recent-changes entry; the list is at its cap of 10, so the oldest entry (the 9 September note on splitting out the OpenAI–Hugging Face incident page) moves to history. Body grows about 50 words, to roughly 106% of the state-of ceiling (warning band, no split). Page date moves to 23 November.
- `wiki/index.md` gains the new tool page.
- One new source page for the announcement.

### What to weigh
The tool page needs a subcategory and none fits: `agent-sandbox-infra` is defined as managed compute for agents, not protection of production hosts. The proposal adds `runtime-security` to the schema. If you would rather not grow the vocabulary for one tool, decline the Create and Schema items and approve only the bullet; the bullet then stands without a link. The four capabilities are described as design goals, and the drafts keep that wording rather than presenting them as shipped.

## Intended changes

- [ ] **Create** `wiki/tools/shirudo.md` — new open-source runtime protection tool
- [ ] **Update** `wiki/state-of/cybersecurity.md` — add Shirudo bullet under "AI security tooling" (after NVIDIA OpenShell); add `openai-cisco-shirudo` to `sources:` and body `## Sources`; `as_of` → 2026-11-23; adds one Recent-changes entry dated 2026-11-23
- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — oldest Recent-changes entry falls off (expected: the 2026-09-09 "Split the OpenAI–Hugging Face incident…" entry)
- [ ] **Update** `wiki/index.md` — add `tools/shirudo` entry; bump page count
- [ ] **Create** `wiki/sources/articles/openai-cisco-shirudo.md` — source summary

## Page drafts

### wiki/tools/shirudo.md (new)

```
---
title: Shirudo
type: tool
domains: [cybersecurity]
subcategory: runtime-security
tags: [openai, open-source]
as_of: 2026-11-23
sources: [openai-cisco-shirudo]
---

# Shirudo

Open-source Linux runtime from OpenAI and Cisco for protecting running systems while a patch is tested and rolled out. It deploys temporary safeguards, called shields, that block the behavior exposing a vulnerability while legitimate requests continue, without restarting the service.

## Current status (as of 2026-11-23)
- Announced and open-sourced 2026-11-23; BSD 2-Clause, with its eBPF programs dual-licensed BSD/GPL
- Shields are eBPF programs (small vetted programs run at hook points inside the Linux kernel); operators can observe a shield's effect on real traffic before enforcing it, and approve before deployment
- Designed around four capabilities: live protection without restarts; programmable controls so agents can investigate vulnerabilities, write shields and validate them against exploits and workloads; signed shields checked by the eBPF verifier before loading; TPM-backed records of shields loaded or removed
- Demo: a [Codex](codex.md)-generated shield added an input check to Java's Base64 decoder on a running Elasticsearch process and blocked a Java4Shell exploit attempt without a restart
- Stated goal: ship tested shields alongside vulnerability disclosures; longer term, auto-generated least-privilege policies and restoring compromised systems to a verified state

## Weaknesses / caveats
- A stopgap, not a patch: it buys time between disclosure and fix
- The four capabilities are described as design goals; the public evidence is one controlled test and a conference walkthrough

## Related
- [NVIDIA OpenShell](nvidia-openshell.md) — also open-source runtime enforcement, but sandboxes agents rather than protecting production hosts
- [State of Cybersecurity](../state-of/cybersecurity.md)

## Recent changes
- [2026-11-23] Launched by OpenAI and Cisco as open source; Codex-generated shield blocked a Java4Shell exploit on running Elasticsearch

## Sources
- [OpenAI and Cisco introduce Shirudo](../sources/articles/openai-cisco-shirudo.md)
```

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: `as_of: 2026-11-23`; append `openai-cisco-shirudo` to `sources:`.

Under `### AI security tooling`, insert after the NVIDIA OpenShell bullet:

```
- [Shirudo](../tools/shirudo.md) — OpenAI and Cisco; open-source runtime that deploys signed eBPF "shields" on running Linux systems to block a vulnerable code path until the patch lands, no restart needed; a Codex-generated shield blocked a Java4Shell exploit on live Elasticsearch in a controlled test *(as of 2026-11-23)*
```

`## Recent changes` — insert at top (adds one entry dated 2026-11-23; the list is at cap 10, so the oldest entry spills):

```
- [2026-11-23] OpenAI and Cisco open-sourced Shirudo, an eBPF runtime that shields running Linux services from a known exploit while the patch is prepared; added to AI security tooling.
```

`## Sources` — append:

```
- [OpenAI and Cisco introduce Shirudo](../sources/articles/openai-cisco-shirudo.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Append under the existing `## Archived from current page on 2026-11-23` block (open a new block with that header if none exists for the apply date):

```
- [2026-09-09] Split the OpenAI–Hugging Face incident and Anthropic's own agentic-misalignment disclosure out into a dedicated page, [OpenAI–Hugging Face agentic cyber incident](../../trends/openai-huggingface-cyber-incident.md), given how much of this page's recent history the incident's follow-on developments had come to occupy.
```

### wiki/index.md (updated)

Add in the tools section, next to `tools/nvidia-openshell`; bump the page count by one:

```
- [tools/shirudo](tools/shirudo.md) — OpenAI and Cisco's open-source Linux runtime that deploys signed eBPF shields to block a known exploit on running services until the patch lands; Codex-generated Java4Shell demo *(as_of: 2026-11-23)*
```

### wiki/sources/articles/openai-cisco-shirudo.md (new)

```
---
title: OpenAI and Cisco introduce Shirudo
type: source
source_type: article
source_file: raw/articles/2026-11-23-openaicom-index-introducing-shirudo.md
url: https://openai.com/index/introducing-shirudo/
published: 2026-11-23
ingested: 2026-11-23
domains: [cybersecurity]
---

# OpenAI and Cisco introduce Shirudo

OpenAI and Cisco announced Shirudo, an open-source runtime that protects running Linux systems while patches are tested and rolled out. It deploys temporary eBPF "shields" that block the behavior exposing a vulnerability while legitimate requests continue, with operator approval before enforcement, signed shields, and TPM-backed records of what was loaded. In a controlled test, a Codex-generated shield added an input check to Java's Base64 decoder on a running Elasticsearch process and blocked a Java4Shell exploit without a restart. The code is BSD 2-Clause (eBPF programs dual BSD/GPL); the goal is to publish tested shields alongside vulnerability disclosures.

## Influenced pages
- [Shirudo](../../tools/shirudo.md) — new page
- [State of Cybersecurity](../../state-of/cybersecurity.md) — new bullet under AI security tooling

## Key claims extracted
- Shirudo launched 2026-11-23 by OpenAI and Cisco as open source (BSD 2-Clause; eBPF programs dual BSD/GPL)
- Shields block a vulnerable code path on a running Linux system without a restart; operators can monitor a shield's effect before enforcing it and approve deployment
- Designed around live protection, agent-driven shield development and validation, signed and verified shields, and TPM-backed verification
- A Codex-generated shield blocked a Java4Shell exploit attempt against running Elasticsearch in a controlled test
- Goal: tested shields published alongside vulnerability disclosures; longer term, auto-generated least-privilege policies and recovery to a verified known-good state
```

## Schema / vocabulary additions
- [ ] Add new subcategory `runtime-security` to `wiki/_schema/subcategories.md` (append to the declared-slugs line and add a section):

```
### runtime-security
- **Parent domain(s):** cybersecurity
- **Applies to types:** tool
- **Definition:** Tools that protect running production systems in place — blocking exploit behavior, enforcing least-privilege policy, or attesting what protections are loaded — as distinct from scanners that find vulnerabilities and sandboxes that isolate agents.
- **Examples:** [Shirudo](../tools/shirudo.md)
```

## Open questions
- If you decline the `runtime-security` subcategory, should Shirudo stay as an unlinked bullet on State of Cybersecurity only (drop the tool page), or go on the page under an existing subcategory you prefer?
	- Create it
