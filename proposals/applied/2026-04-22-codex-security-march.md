---
type: proposal
source: raw/newsletters/2026-03-09-codex-now-finds-vulnerabilities.md
status: pending
created: 2026-04-22
---

# Proposal: Codex Security

## Summary

The March 7-9 cluster around Codex Security adds a meaningful new surface to Codex: security review and vulnerability validation, not just coding or ongoing tasks. This is a clean update to the existing Codex page and the coding state-of page.

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add Codex Security as a distinct capability and product direction
- [x] **Update** `wiki/state-of/coding.md` — clarify that Codex is expanding into review / validation work, not only code generation
- [x] **Create** `wiki/sources/newsletters/codex-security-march.md` — source summary page

## Page drafts

### wiki/tools/codex.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Cloud coding agent accessible from ChatGPT and CLI
- March 2026 also expanded Codex into security review: Codex Security is a research-preview application-security agent that builds repo context, finds vulnerabilities, validates them in sandboxes, and proposes fixes
- A related Codex-for-OSS support program frames this as maintainers' security and review infrastructure, not only an enterprise feature
...

## Recent changes

- [2026-03-09] Codex Security launched in research preview, extending Codex into vulnerability review and validation workflows
- [2026-04-21] OpenAI reframes Codex around app use, memory/preferences, image creation, and repeatable tasks
...
```

### wiki/state-of/coding.md (updated snippet)

```markdown
### Terminal coding agent

- [[tools/codex]] — OpenAI; cloud coding agent via CLI and ChatGPT, now extending beyond generation into review/validation work through Codex Security and broader repeatable-task positioning *(as of 2026-03-09)*
```

### wiki/sources/newsletters/codex-security-march.md (new)

```markdown
---
title: Codex Security
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-09-codex-now-finds-vulnerabilities.md
published: 2026-03-09
ingested: 2026-04-22
domains: [coding]
---

# Codex Security

This source cluster marks Codex's move into security review. Instead of only writing or modifying code, Codex is described as building deep repo context, validating vulnerabilities in sandboxed environments, and proposing fixes for real application-security issues.

## Influenced pages

- [[tools/codex]] — adds a security-review capability surface
- [[state-of/coding]] — sharpens the trend toward coding agents as review/validation systems

## Key claims extracted

- Codex Security launched as a research-preview application-security agent
- It is positioned to find, validate, and propose fixes for vulnerabilities
- OpenAI paired it with a Codex-for-OSS support program for maintainers
- The product direction overlaps with review and validation, not only code generation
```

## Open questions

- None.
