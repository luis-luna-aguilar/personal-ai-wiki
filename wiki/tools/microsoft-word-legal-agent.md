---
title: Microsoft Word Legal Agent
type: tool
domains: [legal, agents]
subcategory: legal-ai
tags: [microsoft, closed-source, agentic]
as_of: 2026-05-01
sources: [microsoft-word-legal-agent]
---

# Microsoft Word Legal Agent

Microsoft Word Legal Agent is a contract-review and redlining agent inside Word, launched through Microsoft's Frontier program for US Windows desktop users. It is positioned for legal teams that already work in Word and need AI assistance without leaving the tracked-change document surface.

## Current status (as of 2026-05-01)

- Reviews contracts clause by clause against a legal playbook
- Drafts negotiation-ready redlines using Word tracked changes
- Compares document versions and cites source language for review
- Runs inside Microsoft 365 security and compliance controls
- Microsoft says the editing layer does not rely on a language model to directly generate every document mutation; it uses a deterministic resolution layer to preserve formatting, lists, tables, tracked changes, and author-specific edits

## Strengths

- Strong native-workflow fit: lawyers can review edits in Word instead of exporting AI suggestions back into a separate document.
- The deterministic edit layer is a useful domain-agent design pattern for high-stakes document work.

## Weaknesses / caveats

- Frontier availability is narrower than general Microsoft 365 Copilot availability.
- Independent practitioner evidence is not yet represented in the wiki.

## Recent changes

- [2026-05-01] Legal Agent in Word announced in Frontier.

## Sources

- [Word: Legal Agent in Frontier](../sources/articles/microsoft-word-legal-agent.md)
