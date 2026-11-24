---
title: AINews — Pi Durable design and multi-harness RL
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
published: 2026-10-06
ingested: 2026-10-20
domains: [agents]
---

# AINews — Pi Durable design and multi-harness RL

Two items from the "Agent Harnesses, RL Environments and Developer Tooling" section of the 6 October 2026 AINews issue: a design note on Pi Durable, and Hugging Face's proxy that turns unmodified coding harnesses into RL environments.

## Influenced pages

- [Pi](../../tools/pi.md) — Pi Durable design details
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — durable-harness section (moved from Agent runtime platforms)
- [Harness-model co-evolution](../../concepts/harness-model-co-evolution.md) — same-weights harness swap and multi-harness training result

## Key claims extracted

- Pi Durable is built around a small task-based workflow engine so long-running, multiplayer agents can suspend and resume anywhere
- Core is ~15K lines of TypeScript with SQLite/JSONL storage; runs on Bun or Cloudflare Durable Objects; control separated from execution environments
- The authors skipped Effect.ts because it does not provide durability
- Hugging Face capture proxy speaks OpenAI Chat, OpenAI Responses, Anthropic, and Gemini formats, forwards to vLLM, records token IDs and logprobs for TRL; 10 unmodified harnesses become RL environments
- Same weights: 62% under Mini-SWE-Agent, 33% under Claude Code
- Training LFM2.5-2.6B across 4 harnesses lifts first-attempt solves from 42% to 54%; a tool-call bonus cuts calls by 31%; SFT on 3,189 rollouts plateaus at 47.5%
- Caveat in the source: one task family, one seed
