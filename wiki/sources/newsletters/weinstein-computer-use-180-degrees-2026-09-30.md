---
title: 'Ari Weinstein: computer use is "180 degrees different"'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
url: https://www.latent.space/p/devday-2026
published: 2026-09-30
ingested: 2026-10-20
domains: [computer-use, agents]
---

# Ari Weinstein: computer use is "180 degrees different"

Latent Space's DevDay 2026 episode, first half: OpenAI's computer-use lead Ari Weinstein (Sky co-founder) rebuts the claim that computer use has stalled. Agents now debug and recover instead of stalling, combine several views of the screen, and write code that performs many actions at once. Covers only the computer-use half; the API half (Nikunj Handa: Decisions API, async tool calling, compaction) is not summarized here.

## Influenced pages

- [State of Computer Use](../../state-of/computer-use.md) — Codex leader line, Recent changes
- [Codex](../../tools/codex.md) — App Shots, code-writing computer use, Sol cost
- [Harness vs model](../../concepts/harness-vs-model.md) — model/harness split in computer-use gains; in-distribution harness

## Key claims extracted

- Biggest change in the past year: agents debug, retry, and introspect instead of stalling after a good start
- Agents combine screenshots, accessibility trees, the DOM, and Playwright; in Codex they often write JavaScript that performs many actions per step
- App Shots (press Command twice) bring an app's full, token-efficient accessibility representation into Codex or ChatGPT instead of a screenshot
- Computer use is now faster than the average human in most cases; the next frontier is "literally superhuman" speed. Much of the remaining latency is waiting for websites to load
- GPT-6.1 Sol: about 1/5 of GPT-6 Astra's cost generally and about 1/7 for computer use
- Computer use is now in the Agents API; OpenAI trains on its own harness, so the in-distribution harness may be faster, cheaper, and more accurate than a custom one
- Favorite use case: agents testing the software they just built, closing the build-test loop so the human is no longer QA
- Gains come "sometimes in the harness and sometimes in the model"
