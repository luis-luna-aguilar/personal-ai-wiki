---
title: "AINews — How to Steal a Reasoning Trace (2026-08-12 digest)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-12-ainews-how-to-steal-a-reasoning-trace.md
url: https://www.latent.space/p/ainews-how-to-steal-a-reasoning-trace
published: 2026-08-12
ingested: 2026-09-07
domains: [coding, agents, models, cybersecurity]
---

# AINews — How to Steal a Reasoning Trace (2026-08-12 digest)

AINews's 2026-08-12 issue leads with a responsibly-disclosed paper showing that encrypted/signed reasoning traces from Claude, GPT, and Gemini APIs can be decoded and replayed onto a different model, session, or user. A preliminary scan of ~7,000 public shared traces found 62 API keys, 33 emails, and 33 passwords, most invisible outside the hidden reasoning blocks. The same issue also covers NVIDIA's Nemotron 3.5 Lightning launch (31.6B/3.6B active MoE for always-on agent workloads, with a Harvey Legal Agent Bench post-training result) and a local-AI-tooling roundup — Unsloth Desktop, an open-source app for running and training models locally across Mac/Windows/Linux positioned as a full local-AI operating environment, and OpenAI's ChatGPT desktop app for Linux with cross-agent import/sync into ChatGPT Work and Codex.

## Influenced pages

- [State of Cybersecurity](../../state-of/cybersecurity.md) — new AI-specific attack surface bullet
- [Reasoning trace leakage](../../concepts/reasoning-trace-leakage.md) — new concept page
- [Nemotron 3.5 Lightning](../../models/nemotron-35-lightning.md) — new model page
- [State of Models](../../state-of/models.md) — new leader line under Open-weight models
- [Codex](../../tools/codex.md) — Linux desktop preview and cross-agent import/sync note
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Unsloth Desktop as a local-AI-infrastructure-stack data point

## Key claims extracted

- Encrypted/signed CoT from Claude, GPT, and Gemini can be decoded and replayed onto a different model/session/user
- Scan of ~7,000 public traces found 62 API keys, 33 emails, 33 passwords; 64 secrets existed only inside hidden reasoning blocks
- Responsibly disclosed; several vulnerabilities already patched
- Reaction split between "serious privacy/safety problem" and "not a scalable distillation path"
- Nemotron 3.5 Lightning: 31.6B total / 3.6B active MoE, OpenMDW-1.1 license, NVFP4/BF16 weights
- Nemotron 3.5 Lightning: AA Intelligence Index 24; ~670 tok/s median serving (pre-release)
- Nemotron 3.5 Lightning: GDPval-AA v2 Elo 824; Terminal-Bench v2.1 24% — both major jumps over Nemotron 3 Nano
- Nemotron 3.5 Lightning: Harvey's Legal Agent Bench post-training took it 0%→8.3%, beating Opus 4.6 and Nemotron 3 Ultra; average output cut from 90k to 37k tokens; day-0 on Together AI, Ollama, Baseten, vLLM, Perplexity API
- Unsloth Desktop: open-source, Mac/Windows/Linux, MLX/GGUF, diffusion image/video/audio, CPU/multi-GPU, OpenAI-compatible APIs, tool calling, sandboxed code execution, private search, RAG, MCP; claims 2x faster training, 70% less VRAM
- ChatGPT desktop app ships for Linux in preview: Ubuntu 24.04/26.04, Debian 13, Fedora 43/44, x64/ARM64
- Desktop app can import/sync projects, chats, skills, and plugins from other agents into ChatGPT Work and Codex, with automatic updates
