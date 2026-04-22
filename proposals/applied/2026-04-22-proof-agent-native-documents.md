---
type: proposal
sources:
  - raw/newsletters/2026-03-11-introducing-proof.md
  - raw/newsletters/2026-03-15-the-never-done-machine.md
status: pending
created: 2026-04-22
---

# Proposal: Proof as an agent-native document tool

## Summary

The earlier proposal overstretched by classifying Proof as an `agent-orchestration-ui`. The stronger reading of the March sources is narrower: Proof is a document collaboration tool built for mixed human/AI authorship, with provenance, comments, tracked changes, and sharing designed into the document surface itself.

This revised proposal treats Proof as a tool in the `agents` domain, but not as a multi-agent supervision/control-plane product. To classify it cleanly, this proposal also introduces a new subcategory for document-native AI collaboration tools.

## Intended changes

- [x] **Create** `wiki/tools/proof.md` — new tool page for Every's collaborative document editor built for human/agent document work
  > See full draft below.

- [x] **Update** `wiki/state-of/agents.md` — add a new `Agent-native documents` subsection and list Proof there, rather than forcing it into `Agent orchestration UIs`
  > See diff snippet below.

- [x] **Update** `wiki/index.md` — add `tools/proof` and refresh page counts
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/proof-agent-native-documents.md` — source summary page
  > See full draft below.

## Schema / vocabulary additions

No new tags are needed. The existing tags `open-source` and `agentic` fit.

- [x] **Add subcategory** `agent-native-documents`
  - **Parent domain(s):** `agents`
  - **Applies to types:** `tool`
  - **Definition:** Document editors and shared writing surfaces built for humans and agents to draft, revise, comment, and maintain the same working artifacts.

## Page drafts

### wiki/tools/proof.md (new)

```markdown
---
title: Proof
type: tool
domains: [agents]
subcategory: agent-native-documents
tags: [open-source, agentic]
as_of: 2026-03-15
sources: [proof-agent-native-documents]
---

# Proof

Proof is Every's web document editor for shared human/agent writing work. Its core thesis is that many plans, reports, memos, and working docs are already being drafted by AI, so the document itself should become the collaboration surface rather than a place where AI output gets pasted after the fact.

## Current status (as of 2026-03-15)

- Free, login-light web editor with live collaboration, comments, and tracked changes
- Open-source at launch
- Tracks provenance in-document so readers can distinguish human- and AI-written sections
- Designed around the principle that agents should be able to act on the same document surface humans use
- Every reported immediate internal use for plans, strategy docs, editorial drafting, and daily task management

## Strengths

- Clear product thesis around document-native AI collaboration rather than generic AI writing assistance
- Provenance rail makes mixed human/agent authorship more legible
- Shared web surface is better suited to ongoing collaborative drafting than laptop-bound local markdown files

## Weaknesses / caveats

- Current source cluster is mostly first-party launch and internal-use reporting
- Evidence is stronger on workflow philosophy than on broad adoption, ecosystem depth, or differentiated execution at scale

## Recent changes

- [2026-03-15] Every positioned Proof as an everyday shared work surface for plans, strategy docs, and task management
- [2026-03-11] Proof launched as a free, open-source collaborative editor for humans and agents

## Sources

- [[sources/newsletters/proof-agent-native-documents]]
```

### wiki/state-of/agents.md (updated snippet)

```markdown
### Agent-native documents

Document surfaces built for humans and agents to collaborate inside the same working artifact, with revision, provenance, and comments happening in-place instead of around pasted AI output.

- [[tools/proof]] — Every's web document editor is the clearest current example of the "agent-native document" thesis: plans, memos, and working docs are treated as shared human/AI artifacts with provenance, comments, and tracked edits built into the document itself *(as of 2026-03-15)*
```

### wiki/index.md (updated snippet)

```markdown
## Tools

- [[tools/proof]] — Every's web document editor for shared human/agent drafting, revision, and document collaboration *(as_of: 2026-03-15)*

## Page count

- tools: 18
...
**Total content pages: 54.**
```

### wiki/sources/newsletters/proof-agent-native-documents.md (new)

```markdown
---
title: Proof and agent-native documents
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-11-introducing-proof.md
published: 2026-03-11
ingested: 2026-04-22
domains: [agents]
---

# Proof and agent-native documents

This source summary groups Every's March cluster around Proof. The main signal is that documents are becoming first-class agent work surfaces: not only places where humans edit text after the fact, but shared environments where agents draft, revise, comment, and maintain working artifacts alongside people.

## Influenced pages

- [[tools/proof]] — new tool page for the product and its document-collaboration model
- [[state-of/agents]] — adds a dedicated `Agent-native documents` subsection

## Key claims extracted

- Proof launched as a free, open-source collaborative document editor designed for humans and agents together
- The editor tracks provenance so readers can see which sections came from humans versus AI
- The product thesis is that laptop-bound Markdown is a poor collaboration surface for agent-generated work
- Every reported immediate internal use for plans, strategy docs, editorial drafts, and daily task management
```

## Open questions

- None.
