---
title: Reasoning trace leakage
type: concept
domains: [cybersecurity]
tags: []
as_of: 2026-08-12
sources: [unsloth-desktop-chatgpt-linux-2026-08-12]
---

# Reasoning trace leakage

Frontier reasoning models return their internal chain-of-thought from the API as an encrypted or cryptographically signed blob rather than plain text — mainly to stop competitors distilling a rival's reasoning by reading it directly. A responsibly-disclosed 2026-08 paper showed that protection can be broken: a legitimate signed reasoning block can be decoded and replayed onto a different model, session, or user, turning an opaque blob back into readable text.

## Current status (as of 2026-08-12)

- **Technique:** obtain a signed reasoning block from an API response, replay it into a request to a weaker model from the same provider, place it in an assistant-turn prefill, and prompt the model to transcribe it — sampling repeatedly and reconciling noisy outputs. Provider-specific variants exist for Claude (`<thinking-copy>` prefill to Haiku 4.5), GPT (repeated `encrypted_content` injection, chunked to bypass a ~50-token verbatim cap), and Gemini (`<thought>` prefill with reconciliation).
- **Real-world exposure:** a preliminary scan of ~7,000 publicly shared traces — the kind that appear when someone shares a Claude Code or Codex session — found 62 unique API keys, 33 email addresses, and 33 passwords. 64 of those secrets existed only inside the hidden reasoning, invisible anywhere in the visible session text.
- Responsibly disclosed; several vulnerabilities are already patched, though similar bypasses likely remain possible.
- Reaction is split: some researchers call it a serious privacy and safety problem; others argue it isn't a scalable path to distilling a competitor's model, since the encryption functions more as a stateless-inference protocol optimization than a hard confidentiality guarantee.

## Why it matters

Hidden chain-of-thought was already a fragile signal for safety and alignment monitoring — often terse, multilingual, or otherwise hard to interpret. This shows it isn't reliably private either, and that tool surfaces can re-expose internal reasoning even when a lab hides "thinking" from the chat UI. The practical takeaway for anyone using agent tools: publicly sharing a raw session transcript — a common practice for showing off agent runs — can leak more than what's visible on screen.

## Sources

- [AINews — How to Steal a Reasoning Trace](../sources/newsletters/unsloth-desktop-chatgpt-linux-2026-08-12.md)
