---
type: proposal
sources:
  - raw/newsletters/2026-05-06-chatgpts-new-default-model-is-here.md
  - raw/newsletters/2026-05-06-chatgpts-new-default-model-just-dropped.md
  - raw/newsletters/2026-04-24-model-wars.md
  - raw/newsletters/2026-04-26-codex-moves-beyond-coding.md
status: pending
created: 2026-05-13
---

# Proposal: GPT-5.5 Instant as ChatGPT default

## Summary

Multiple newsletter sources say GPT-5.5 Instant replaced GPT-5.3 Instant as ChatGPT's default model, with claimed lower hallucination, API exposure through `chat-latest`, and a fallback window for GPT-5.3. Because these are secondary sources, the update should be caveated unless an official OpenAI source is added later.

## Intended changes

- [x] **Update** `wiki/models/gpt-5-5.md` — add Instant/default-model status as a caveated current-status bullet
    > Add to Current status: `Secondary May 2026 coverage says GPT-5.5 Instant replaced GPT-5.3 Instant as ChatGPT's default model, with API exposure via \`chat-latest\`; verify against OpenAI docs before treating specific hallucination-reduction numbers as official.`

- [x] **Update** `wiki/state-of/models.md` — add recent change
    > Add Recent changes entry: `- [2026-05-06] Secondary coverage says GPT-5.5 Instant became ChatGPT's new default model, replacing GPT-5.3 Instant; official verification still needed for exact rollout and hallucination claims.`

- [x] **Create** `wiki/sources/newsletters/gpt-5-5-instant-default-2026-05-06.md`
    > See draft below

## Page drafts

### wiki/sources/newsletters/gpt-5-5-instant-default-2026-05-06.md (new)

```markdown
---
title: GPT-5.5 Instant becomes ChatGPT default — secondary coverage
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-06-chatgpts-new-default-model-is-here.md
published: 2026-05-06
ingested: 2026-05-13
domains: [models]
---

# GPT-5.5 Instant becomes ChatGPT default — secondary coverage

Several May 6 newsletters report that GPT-5.5 Instant replaced GPT-5.3 Instant as ChatGPT's default model. They also mention `chat-latest` API exposure, lower hallucination framing, and a paid fallback window for GPT-5.3.

## Influenced pages

- [GPT-5.5](../../models/gpt-5-5.md)
- [State of Models](../../state-of/models.md)

## Key claims extracted

- GPT-5.5 Instant reportedly became the ChatGPT default.
- GPT-5.3 Instant reportedly remains available as a fallback for some paid users.
- Exact hallucination-reduction and rollout details should be verified against official OpenAI materials.
```

