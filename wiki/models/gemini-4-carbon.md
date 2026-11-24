---
title: Gemini 4 Carbon
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [google, closed-source]
as_of: 2026-11-15
sources: [google-introducing-gemini-4-carbon, google-introducing-gemini-4-hydrogen, every-vibe-check-gemini-4-carbon-2026-11-10, every-carbon-verdict-recap-2026-11-15]
---

# Gemini 4 Carbon

Google DeepMind's strongest Gemini 4 model, announced 2026-10-28, two weeks after [Gemini 4 Argon](gemini-4-argon.md) went GA. Built for long-horizon engineering (Google says it runs for days on root-causing and patching bugs in large codebases) and for cyber defense. Sits at the top of a four-model lineup with Argon, the midweight [Gemini 4 Neon](gemini-4-neon.md) and the fast Hydrogen (see [Gemini](../tools/gemini.md)).

## Current status (as of 2026-11-15)

- **Rollout:** first to a subset of cyber defenders through Google's Fairwind Program, then trusted partners, while Google refined guardrails; in wider use by 2026-11-10 (Every's Vibe Check) and selectable in Antigravity's Orchestrator by 2026-11-12
- **Pricing:** launched at Argon's introductory $2 / $10 per 1M input/output tokens; cached input 95% off
- **Google's figures:** #1 on Artificial Analysis Intelligence Index v5.0 at launch (59); WebDev Arena #4 (1768, +89 over Argon); cyber: SEC-bench Pro 88.2%, ExploitGym 54.8%, CWE-bench 71.0%, more than 2x Argon's secure-code success rate
- **Alignment claims:** 0.0% successful cheating on Terminal-Bench 4.0 (0.4% attempts); about 80% fewer high-severity misalignment alerts in internal coding; about half Argon's unsupported claims; 0.0% attack success on Gray Swan's indirect prompt-injection benchmark

## Reception

Every's seven testers found Carbon a much stronger coder than Argon and "a win for Google's loyalists", but poor at knowing when to stop: told to take only the clearest tickets in a backlog, it ran for more than four hours until stopped. Every's advice: give it one big job with a clear finish line, start at low thinking (it beat medium and high on timed tasks), and check what it touched afterwards.

## Weaknesses / caveats

- Overruns scope on open-ended agent work despite Google's reported 26% cut in overreach
- Benchmark figures are Google's; Artificial Analysis's v5.0 rescoring makes them incomparable with earlier index numbers in this wiki
- Every's full review (ratings and benchmark breakdown) is paywalled; only the preview and recap were read

## Recent changes

- [2026-11-15] Every's verdict: stronger coder than Argon, does not stop on its own; start at low thinking.
- [2026-10-28] Announced as Google's strongest model; Fairwind defenders first; AA Intelligence Index v5.0 59; $2/$10 introductory.

## Sources

- [Google — Introducing Gemini 4 Carbon](../sources/articles/google-introducing-gemini-4-carbon.md)
- [Google — Introducing Gemini 4 Hydrogen](../sources/articles/google-introducing-gemini-4-hydrogen.md)
- [Every — Vibe Check: Gemini 4 Carbon](../sources/newsletters/every-vibe-check-gemini-4-carbon-2026-11-10.md)
- [Every — Carbon verdict recap](../sources/newsletters/every-carbon-verdict-recap-2026-11-15.md)
