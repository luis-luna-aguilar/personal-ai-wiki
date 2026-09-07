---
type: proposal
sources:
  - raw/newsletters/2026-07-31-the-definitive-guide-to-using-voice-with-ai.md
  - raw/newsletters/2026-08-02-your-ai-is-a-team-of-specialists.md
status: pending
created: 2026-09-07
---

# Proposal: Voice-agent workflow loop and Monologue's 500M-word milestone

## Summary

### The source

On 2026-07-31, Every published "Build Faster With Voice," a guide framing voice as the missing link between a raw thought and finished work with an AI agent. The pitch: most knowledge work starts with an act of translation — a customer call becomes a bug report, a walk-and-think becomes a typed brief — and that translation step is pure overhead. Paired with an agent, voice removes it: you can speak while details are fresh, point the agent at the relevant transcripts, code, or documents, define the outcome you want, and review what it produces. The guide formalizes this into a five-step loop — capture, then retrieve and ground, then define the outcome, then act, then review and redirect — and packages more than a dozen copyable prompts and setup instructions behind Every's paywall; the free preview covers only the five-step framing itself, not the detailed prompt library. A companion note from Every's 2026-08-02 weekly roundup adds a concrete adoption datapoint: Monologue, Every's own voice-dictation tool, passed 500 million words dictated that week, up from roughly 1 million words a week when it launched in September 2025, and now runs on Mac, iPhone, and Apple Watch.

### What changes

The wiki's `trends/voice-becomes-agent-interface.md` currently tracks voice mainly as a product-layer story (GPT-Live's full-duplex delegation, ChatGPT Voice's desktop computer-control). This proposal adds the workflow-pattern side of the same trend.

- **Voice becomes an agent interface** gains two Current-status bullets — the five-step capture/ground/define/act/review loop as an emerging standard shape for voice-driven agent work, and Monologue's 500M-words milestone as a concrete usage datapoint — plus two new Recent-changes entries and two new source citations. Page date moves to 2 August.

### What to weigh

The Every guide's substantive detail (the 14 workflow prompts, setup instructions) sits behind a paywall; only the five-step framing and its rationale are available, so the draft below keeps the claim at that level rather than implying deeper coverage. Nothing else beyond the sourcing noted above.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/voice-becomes-agent-interface.md` — add two Current-status bullets, two Recent-changes entries, two source links, bump `as_of` to 2026-08-02
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-voice-guide-2026-07-31.md` — source summary for the voice-workflow guide

- [ ] **Create** `wiki/sources/newsletters/every-team-of-specialists-2026-08-02.md` — source summary for Every's 2026-08-02 weekly roundup (Monologue milestone only; other roundup items are out of scope for this proposal)

## Page drafts

### wiki/trends/voice-becomes-agent-interface.md (updated)

Frontmatter changes:
```yaml
as_of: 2026-08-02
sources: [voice-becomes-agent-interface, gpt-live-launch-2026-07, bfl-flux-3-2026-07-24, every-voice-guide-2026-07-31, every-team-of-specialists-2026-08-02]
```

`## Current status` — add these two bullets at the end of the existing list:
```md
- A five-step workflow loop — capture, retrieve and ground, define the outcome, act, review and redirect — is emerging as the standard shape for voice-driven agent work (Every, July 2026): voice removes the "translation step" between a raw thought and a polished agent instruction, not the review step itself.
- Monologue (Every's voice-dictation tool) passed 500 million words dictated by early August 2026, up from roughly 1 million words/week at its September 2025 launch, now running on Mac, iPhone, and Apple Watch — a concrete usage datapoint for voice as a working interface rather than a novelty mode.
```

`## Recent changes` — insert these two entries in date order (newest first), ahead of the existing `[2026-07-22]` entry:
```md
- [2026-08-02] Monologue passed 500 million words dictated (up from ~1M/week at its September 2025 launch), now on Mac, iPhone, and Apple Watch.
- [2026-07-31] Every formalized a five-step voice-agent workflow loop (capture → retrieve/ground → define outcome → act → review/redirect) for turning speech into finished work with an agent.
```
No entries fall off — the list is at 4 of 10 after this insert, well under the cap; no spill needed.

`## Sources` — append:
```md
- [Build Faster With Voice — Every guide](../sources/newsletters/every-voice-guide-2026-07-31.md)
- [Every — Your AI Is a Team of Specialists (weekly roundup)](../sources/newsletters/every-team-of-specialists-2026-08-02.md)
```

### wiki/sources/newsletters/every-voice-guide-2026-07-31.md (new)

```md
---
title: "The Definitive Guide to Using Voice With AI"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-31-the-definitive-guide-to-using-voice-with-ai.md
url: https://every.to/p/the-definitive-guide-to-using-voice-with-ai
published: 2026-07-31
ingested: 2026-09-07
domains: [voice]
---

# The Definitive Guide to Using Voice With AI

Every announced "Build Faster With Voice," a practical guide to using AI agents via speech across writing, planning, software, and communication. The free preview describes a five-step loop — capture, retrieve and ground, define the outcome, act, review and redirect — that treats voice as removing the translation step between a raw thought and a usable agent instruction, while keeping consequential actions behind human review. The full prompt library, setup instructions, and 14 team workflows are paywalled.

## Influenced pages

- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — added the five-step loop as a named workflow pattern

## Key claims extracted

- Five-step voice-agent loop: capture → retrieve and ground → define the outcome → act → review and redirect
- Voice removes the "translation step" between a raw thought and a polished agent instruction; review and approval for consequential actions still required
- Full guide (paid): 14+ workflows, copyable prompts, setup instructions for connecting notes/transcripts to Codex or Claude
```

### wiki/sources/newsletters/every-team-of-specialists-2026-08-02.md (new)

```md
---
title: "Your AI Is a Team of Specialists"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-02-your-ai-is-a-team-of-specialists.md
url: https://every.to/context-window/your-ai-is-a-team-of-specialists
published: 2026-08-02
ingested: 2026-09-07
domains: [voice]
---

# Your AI Is a Team of Specialists

Every's 2026-08-02 weekly roundup. The only claim ingested from this issue is a standalone product note: Monologue, Every's voice-dictation tool, passed 500 million words dictated this week, up from roughly 1 million words/week at its September 2025 launch, and now runs on Mac, iPhone, and Apple Watch. The roundup also links out to several other Every pieces (a "Fable as CEO" org-chart framing of Anthropic's model lineup, a Slack-agent-command-center piece, an Opus 5 taming post) that are out of scope for this proposal.

## Influenced pages

- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — Monologue 500M-words adoption datapoint

## Key claims extracted

- Monologue passed 500 million words dictated as of 2026-08-02, up from ~1M words/week at September 2025 launch
- Monologue now runs on Mac, iPhone, and Apple Watch
```

## Open questions

- The roundup newsletter (2026-08-02) also capsule-describes the "Fable as CEO" org-chart/"Claudish" piece — that signal was left unchecked in this batch's triage, so it is intentionally excluded from both the trend-page draft and the source-page claims above.
