---
title: AGI timeline claims
type: trend
domains: [models]
tags: [openai]
as_of: 2026-11-18
sources: [ainews-openai-agi-bar-2026-08-28, ainews-fablemythos-51-2026-09-02, ainews-gpt-6-astra-launch-2026-09-04, openai-research-acceleration-2026-09-06, every-after-automation-2026-05, metr-anthropic-ai-rd-acceleration-2026-11-05, openai-research-acceleration-jagged-frontier-2026-11-18, every-metr-ai-2027-ahead-2026-11-13]
---

# AGI timeline claims

The trend: as frontier labs approach what they consider AGI-level capability, some are starting to name specific internal timelines and milestones rather than treating "AGI" as an indefinite future event. This page tracks those dated claims as they occur, distinct from [Restricted frontier deployment](restricted-frontier-deployment.md), which tracks labs withholding or gating capability once a threshold is crossed — this page is about labs signaling a threshold has been (or will soon be) reached. It also tracks measurements of how much AI is speeding up AI research itself, the evidence these claims increasingly rest on.

## Current signal

- **OpenAI's Astra as the "Automated AI Research Intern" (as of 2026-08-28):** Chief scientist Jakub Pachocki said the unreleased Astra model meets a milestone he named roughly nine months earlier, targeted for September 2026. AINews, which had checked in on OpenAI's AGI timeline at that nine-months-earlier point, reads the current trajectory as "right on target."
- **Sam Altman's December 2026 AGI estimate:** in a TIME interview, Altman estimated OpenAI will declare AGI achieved internally by December 2026 — a specific date, though "declared internally" leaves open how and whether this would be externally verifiable or announced.
- **OpenAI's Astra reaches the "Critical" cyber-capability threshold (as of 2026-09-02):** OpenAI previewed Astra as the first model to hit the "Critical" threshold for cybersecurity under its own Preparedness Framework — circulating testing summaries describe it finding V8 zero-days, chaining exploits, compromising a hardened browser, escaping sandboxing, and escalating privileges. OpenAI says Astra's most advanced cyber capabilities will be more tightly access-controlled going forward; Sam Altman said publicly that safety work is slowing deployment pacing more broadly. A second, differently-shaped capability-threshold signal alongside Pachocki's "Automated AI Research Intern" claim above — this one tied to a named Preparedness Framework tier rather than an internal milestone.
- **OpenAI confirms the "automated research intern" goal reached, names a March 2028 target for a full automated AI researcher (as of 2026-09-06):** OpenAI's own research-acceleration report states it has "now reached the goal, announced last fall, of having an automated research intern by September of this year" and that it is "making strong progress toward creating an automated AI researcher by March of 2028" — the first specific date attached to that longer-term milestone. Its adoption figures are replaced by the November report below. See [Research acceleration: The view inside OpenAI](../sources/articles/openai-research-acceleration-2026-09-06.md).
- **GPT-6 Astra ships roughly on the named timeline, and the "is this AGI" debate fragments further (as of 2026-09-03):** OpenAI launched Astra 2026-09-03 — close to Pachocki's named "Automated AI Research Intern" target above. Reaction split into camps rather than converging: OpenAI staff and some benchmark authors called it a genuine generational leap; Artificial Analysis and Epoch read the gains as large but uneven once cost and non-cherry-picked evals are considered; a safety-focused camp (Ryan Greenblatt, Neel Nanda) argued the more consequential story is the system card's disclosed chain-of-thought monitorability decline, not the capability numbers. See [GPT-6 Astra](../history/models/gpt-6-astra.md) and [Chain-of-thought monitorability](cot-monitorability.md) for the fuller picture.
- **METR measures AI-driven acceleration at Anthropic: about 2x (as of 2026-11-05):** After a high-access assessment inside Anthropic (12 August to 29 October), METR concluded Anthropic is likely improving its models on well-specified tasks at about twice its March 2024–October 2025 rate (plausible range 1.3x to 3x). Scores on AECI, Anthropic's version of the Epoch Capabilities Index, have grown 1.9x faster since October 2025, and training-compute growth did not speed up; the measured acceleration is smaller when other labs' models are included, partly because Anthropic's earlier growth lagged the industry frontier. METR attributes perhaps 80% of the current acceleration to Anthropic's own AI use, mostly assistance rather than autonomous work, and found no clear bottleneck for the next 12 months, so further compounding is a significant risk. Anthropic redacted most of the evidence METR found most informative. The AI 2027 authors read the result as putting the world about five months ahead of their forecast. See [METR's assessment](../sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md).
- **OpenAI's November report: jagged uplift, acceleration not yet claimed (as of 2026-11-18):** From March to October, agents' success without human help rose from 23% to 46% on two-to-four-hour research tasks and from 13% to 35% on four-to-eight-hour ones, unevenly: 79% for monitoring training runs, 25% for inference code. Median researcher agent use reached $2,400 a day at list prices (90th percentile $23,000). OpenAI's internal capability index has risen 16.4 points a year since August 2025, against Epoch's 14-point trend; OpenAI is still watching for acceleration. People came up with nearly all key ideas behind GPT-6 Astra and GPT-6.2 Astra; GPT-6.2 Astra's pretraining is the first where Codex was credited with insights. See [Research acceleration: The jagged frontier](../sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md).

## Why it matters

Dated, named claims from lab leadership are a different kind of signal than marketing copy or a product launch post — they're falsifiable in a way that lets the wiki track whether they hold up. If OpenAI (or another lab) does declare AGI internally on roughly this timeline, or conspicuously misses it, that's a significant milestone for how the rest of the wiki's model and trend pages should be read.

## Reading benchmark trend lines: the framing critique

Dated AGI claims are often read off benchmark trend lines. Every's Dan Shipper ("After Automation," May 2026) argues that reading those lines in isolation produces "chart psychosis" — scary intuitions about imminent job replacement that don't survive a look at how the benchmark itself is built.

- Every benchmark needs a prompt, and a prompt is a frame: it freezes an open-ended situation into a fixed, measurable target. A score describes how well a model performs inside that frame, not some frame-independent measure of "the model itself."
- **Case study — Every's in-house Senior Engineer benchmark** (rewrite a vibe-coded production codebase from first principles): GPT-5.5 scored 62/100, about 30 points above Claude Opus 4.7, while human senior engineers score in the high 80s to low 90s on the same task. Changing the prompt's specificity — removing hints like "structural rewrite" and "invariants" lowers the score; replacing the prompt with "solve all of the errors that keep popping up" drops it to near zero — moves the score dramatically without changing the model.
- **Case study — OpenAI's GDPval**: high pass rates against human professionals rely on tasks whose prompts already encode a large amount of "smuggled intelligence" (which sample-size formula, which risk-weighted entities, which confidence interval) supplied by a human expert before the model ever ran. The benchmark measures performance on an already-expert-framed problem, not the ability to frame the problem in the first place.
- Once a frame saturates, the fix is not "the model has replaced the expert." The now-cheap capability inside that frame gets adopted broadly, produces a flood of undifferentiated output ("slop"), and shifts the scarce, valuable work to the next frame up — deciding whether a rewrite is even needed, what to preserve, who reviews the result. The cycle repeats at the next level rather than terminating.
- This holds even under a strong operational definition of AGI (a system worth running continuously): the model can select and re-select frames, but only in service of a goal supplied by a human "framer." The frame is not the framer, so demand for the human who decides what's worth optimizing does not disappear — it moves up a level.

For eval design this complements the benchmark-leakage caveat on [Agent evals](../concepts/agent-evals.md): leakage is a benchmark failing to measure what it claims to measure; frame-relativity is a benchmark validly measuring a moving target that keeps being redefined as it saturates.

## What to watch

- Whether OpenAI's Astra ships, and whether its capabilities match the "Automated AI Research Intern" framing
- Whether OpenAI (or any lab) makes a formal internal-AGI-declared announcement, and what evidence or benchmark accompanies it
- Whether other labs (Anthropic, Google DeepMind) make comparable dated claims
- Whether outside acceleration assessments like METR's spread to other labs, and whether OpenAI's capability index starts to bend upward the way Anthropic's has

## Recent changes

- [2026-11-18] OpenAI's second research-acceleration report: agents now complete 46% of two-to-four-hour research tasks alone (23% in March), uplift is uneven by task, and OpenAI does not yet claim its capability index is accelerating; September adoption figures replaced.
- [2026-11-05] METR's high-access assessment finds Anthropic improving its models about 2x faster than in 2024–25 (range 1.3x–3x), mostly due to its own AI use, with no bottleneck in sight; most supporting evidence redacted by Anthropic.
- [2026-10-19] Merged the "chart psychosis" benchmark-framing critique (Every, Dan Shipper) from [Agent evals](../concepts/agent-evals.md) as a lens for reading benchmark-based AGI claims.
- [2026-09-06] OpenAI's own research-acceleration report confirms the "automated research intern" milestone reached and names a new March 2028 target for a full automated AI researcher, backed by internal adoption data (3.1 agent-workdays per human workday since June 2026; 90th-percentile researcher spending $7,000+/day on inference) alongside a caveat that over half of successful 4-8hr tasks still need human intervention.
- [2026-09-03] GPT-6 Astra launches close to Pachocki's named timeline; reaction fragments into "genuine leap" / "mixed benchmarks" / "the monitorability decline is the real story" camps rather than converging on one read.
- [2026-09-02] OpenAI's Astra reaches the "Critical" cyber-capability threshold under OpenAI's own Preparedness Framework — testing reportedly found V8 zero-days, chained exploits, and sandbox escapes; Altman says safety work is slowing deployment pacing generally.
- [2026-08-28] OpenAI's Jakub Pachocki frames the unreleased Astra model as meeting his named "Automated AI Research Intern" milestone; Sam Altman estimates OpenAI will declare AGI achieved internally by December 2026 (TIME interview).
- [2026-05-21] Added "chart psychosis" / benchmark-framing critique (Every, Dan Shipper, "After Automation"): benchmark scores measure performance inside a chosen frame; saturating one frame shifts demand to the next frame rather than eliminating human work. Senior Engineer benchmark example: GPT-5.5 62/100, ~30 points above Opus 4.7, ~30 below human senior engineers.

## Related

- [Agent evals](../concepts/agent-evals.md) — how agent benchmarks are built, including the benchmark-leakage caveat the framing critique complements
- [AI work delegation modes](../training/ai-work-delegation-modes.md) — the human-sandwich and delegation patterns the framing critique implies
- [Restricted frontier deployment](restricted-frontier-deployment.md) — the inverse pattern: labs withholding or gating capability once a threshold is crossed, rather than declaring one reached

## Sources

- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — Claude Fable/Mythos 5.1: new SOTA model](../sources/newsletters/ainews-fablemythos-51-2026-09-02.md)
- [AINews — GPT-6 Astra: OpenAI's biggest LLM launch](../sources/newsletters/ainews-gpt-6-astra-launch-2026-09-04.md)
- [Research acceleration: The view inside OpenAI](../sources/articles/openai-research-acceleration-2026-09-06.md)
- [After Automation — Dan Shipper (Every)](../sources/articles/every-after-automation-2026-05.md)
- [METR — Independent assessment of AI R&D acceleration at Anthropic](../sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md)
- [Research acceleration: The jagged frontier](../sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md)
- [Every — METR finding and AI 2027 reaction (Nov 13)](../sources/newsletters/every-metr-ai-2027-ahead-2026-11-13.md)
