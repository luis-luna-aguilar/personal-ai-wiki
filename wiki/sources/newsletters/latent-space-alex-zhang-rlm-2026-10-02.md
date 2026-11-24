---
title: Latent Space — Academia is for Ambition (Alex Zhang, MIT)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-02-academia-is-for-ambition-alex-zhang-mit.md
url: https://www.latent.space/p/rlm
published: 2026-10-02
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — Academia is for Ambition (Alex Zhang, MIT)

Long podcast transcript with MIT PhD student Alex Zhang, author of the Recursive Language Models (RLM) work, covering GPU kernels, research taste, RLMs, Prime Agent, and harness design. Only the harness section ("Why Claude Code, Codex, and Pi are so similar", "Harnesses as compositional generalizers") was used for this ingest.

## Influenced pages

- [Harness vs model](../../concepts/harness-vs-model.md) — the "all mainstream harnesses are the same loop" dissent
- [Pi](../../tools/pi.md) — Pi as the reference harness

## Key claims extracted

- Claude Code, Codex, Pi, Oh My Pi, and Prime Agent make mostly the same design choices; Zhang uses Pi as the reference because "all other harnesses are basically just Pi"
- He calls this harness class "trajectory as a prompt": the whole rollout stays in the main model's context, even with subagents
- As models improve, putting a strong model in another mainstream harness mostly changes cost, not outcome
- Frontier labs likely train only in their own harnesses; open models need to be trained in a harness to use it well
- An RLM is a harness whose only tool is code; the model can call itself as a subagent, and other tools are functions in code
- Harnesses can act as compositional generalizers: a strategy learned on short tasks transferred to tasks 8–30x longer
- Prime Agent is Pi restricted to IPython as the only tool, plus a continual-harness mechanism
