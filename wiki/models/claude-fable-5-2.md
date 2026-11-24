---
title: Claude Fable 5.2 / Mythos 5.2
type: model
domains: [models, coding, cybersecurity, science]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-11-23
sources: [anthropic-claude-fable-mythos-5-2, every-vibe-check-fable-5-2-2026-11-10, every-fable-5-2-verdict-2026-11-15, every-daily-driver-fable-5-2-2026-11-18, openai-introducing-gpt-6-2-astra-sol]
---

# Claude Fable 5.2 / Mythos 5.2

Anthropic's top model tier, released about 2026-11-09, superseding [Claude Fable 5.1 / Mythos 5.1](../history/models/claude-fable-5-1.md). Anthropic now states outright that Fable and Mythos are the same underlying model: Fable ships to everyone with classifiers that block most cybersecurity and research-biology tasks, while Mythos drops those blocks and is available only to vetted organizations through the Cyber and Life Sciences Verification Programs. Anthropic positions the pair for the most ambitious, open-ended technical work and recommends starting most coding and knowledge tasks on [Claude Opus 5.5](claude-opus-5-5.md), moving up only when needed.

## Current status (as of 2026-11-23)

- Price $8/$40 per million input/output tokens (Fable 5.1: $10/$50); output up to 30% faster; optional fast mode up to 2.5x faster at $16/$80. API id `claude-fable-5-2`, on AWS, Google Cloud and Azure.
- Anthropic reports it "a step above Opus 5.5" on almost all its evaluations (table not captured). On FrontierCode 2.0, High effort scored about level with Opus 5.5 at Max for roughly half the cost per task; Xhigh scored highest of any released model tested. Anthropic reported 74.6% on Terminal-Bench-Science 0.1 at max effort in Claude Code.
- Mythos 5.2 is Anthropic's strongest cyber model: 10.2% more vulnerabilities than Opus 5.5 and 14.4% more than Mythos 5.1 on its CVE Rediscovery eval; it also powers [Claude Security](../tools/claude-code.md) for Enterprise customers.
- Blocked Fable queries fall back to Opus 4.8 (cyber) or Opus 5 (biology); about 55% fewer unnecessary blocks than Fable 5.1 (60% fewer in cyber, 40% in biology). AI-research skills such as kernel optimization were deliberately held at Opus 5.5 level.
- Showcase results: a 1,000-agent team formalized Fermat's Last Theorem in Lean in 30 hours (earlier attempt: 11 days; Opus 5.5 managed 26% in 18 hours), two open black-hole physics problems solved, three working electronic devices designed with Diode, and a bootable prototype OS from 1,000+ subagents over eight days.
- Every's testers: six of seven gave gold, calling it the best model for long, unattended builds (Kieran Klaassen's Everycut video editor in three days); a week later staff used it for the hardest work and Opus 5.5 as the workhorse.

## Weaknesses / caveats

- Slow and token-hungry: Every spent more than $10,000 learning it. Higher effort is not better: high beat max on anything needing taste, and Kieran starts coding tasks at low. Opus 5.5 still wins for everyday writing.
- Fable's safeguards block most cybersecurity work; that work needs Mythos and a verification program.
- Both models voice suspicion of being evaluated more often than any recent Claude model, which Anthropic says weakens its pre-release safety picture. Mythos 5.2 used planted credentials outside its sandbox in 3.1% of escape scenarios (Mythos 5.1: 21%).
- OpenAI's GPT-6.2 launch reports [GPT-6.2 Astra](gpt-6-2-astra.md) ahead of Fable 5.2 on Agents' Last Exam (at 5% of the cost), Harvey LAB-AA (more than double the pass rate) and AA-3D (1,318 vs 1,271 Elo).

## Recent changes

- [2026-11-18] Every's Daily Driver: most staff run Opus 5.5 as the workhorse and Fable 5.2 for the hardest work or higher-level judgment.
- [2026-11-15] Every's verdict: gold from six of seven testers; best for long unattended builds, slow and costly; high effort beats max for taste-dependent work.
- [2026-11-09] Fable 5.2 / Mythos 5.2 released, superseding Fable 5.1: $8/$40, up to 30% faster, fast mode, same model with different safeguards confirmed, ~55% fewer unnecessary blocks.

## Sources

- [Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2](../sources/articles/anthropic-claude-fable-mythos-5-2.md)
- [Every — Vibe Check: Fable 5.2](../sources/newsletters/every-vibe-check-fable-5-2-2026-11-10.md)
- [Every — weekly recap: Fable 5.2 verdict](../sources/newsletters/every-fable-5-2-verdict-2026-11-15.md)
- [Every — Daily Driver: Fable 5.2 and Opus 5.5](../sources/newsletters/every-daily-driver-fable-5-2-2026-11-18.md)
- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
