---
title: "Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
url: https://www.latent.space/p/devday-2026
published: 2026-09-30
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)

Second half of Latent Space's DevDay episode: OpenAI API product lead Nikunj Handa on the developer stack. The first half (Ari Weinstein on computer use) and the Decisions API segment have their own story pages.

## Influenced pages

- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — model-lab agent APIs (moved from Agent runtime platforms)
- [ChatGPT dots](../../tools/chatgpt-dots.md) — each dot gets its own Linux cloud computer
- [ChatGPT Space](../../tools/chatgpt-space.md) — meeting notes flowing into a Space, built on the Agents API
- [ChatGPT Pages](../../tools/chatgpt-pages.md) — Spaces/Pages/dot collaboration demo

## Key claims extracted

- Agents API ships the Codex harness with computer use and built-in compaction; OpenAI's Codex Security and meeting-notes features run on it
- The DevDay plugin-extensions demo (calendar meeting notes flowing into a Space) is built on the Agents API; the host describes the demo as editing Spaces and Pages, collaborating, and adding in your dot
- Responses API: async tool calls, mid-turn steering over WebSockets
- Caching: 30-minute cache-hit guarantee; 12-hour tier in preview (higher cache-write price); cache pre-warming; cache diagnostics tool
- Compaction: server-side auto-compaction at a token threshold, or manual /compact, which the Codex harness uses; file-based compaction experiments
- Open question: how much memory and storage abstraction belongs in the API
