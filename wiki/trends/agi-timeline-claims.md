---
title: AGI timeline claims
type: trend
domains: [models]
tags: [openai]
as_of: 2026-09-06
sources: [ainews-openai-agi-bar-2026-08-28, ainews-fablemythos-51-2026-09-02, ainews-gpt-6-astra-launch-2026-09-04, openai-research-acceleration-2026-09-06]
---

# AGI timeline claims

The trend: as frontier labs approach what they consider AGI-level capability, some are starting to name specific internal timelines and milestones rather than treating "AGI" as an indefinite future event. This page tracks those dated claims as they occur, distinct from [Restricted frontier deployment](restricted-frontier-deployment.md), which tracks labs withholding or gating capability once a threshold is crossed — this page is about labs signaling a threshold has been (or will soon be) reached.

## Current signal

- **OpenAI's Astra as the "Automated AI Research Intern" (as of 2026-08-28):** Chief scientist Jakub Pachocki said the unreleased Astra model meets a milestone he named roughly nine months earlier, targeted for September 2026. AINews, which had checked in on OpenAI's AGI timeline at that nine-months-earlier point, reads the current trajectory as "right on target."
- **Sam Altman's December 2026 AGI estimate:** in a TIME interview, Altman estimated OpenAI will declare AGI achieved internally by December 2026 — a specific date, though "declared internally" leaves open how and whether this would be externally verifiable or announced.
- **OpenAI's Astra reaches the "Critical" cyber-capability threshold (as of 2026-09-02):** OpenAI previewed Astra as the first model to hit the "Critical" threshold for cybersecurity under its own Preparedness Framework — circulating testing summaries describe it finding V8 zero-days, chaining exploits, compromising a hardened browser, escaping sandboxing, and escalating privileges. OpenAI says Astra's most advanced cyber capabilities will be more tightly access-controlled going forward; Sam Altman said publicly that safety work is slowing deployment pacing more broadly. A second, differently-shaped capability-threshold signal alongside Pachocki's "Automated AI Research Intern" claim above — this one tied to a named Preparedness Framework tier rather than an internal milestone.
- **OpenAI confirms the "automated research intern" goal reached, names a March 2028 target for a full automated AI researcher (as of 2026-09-06):** OpenAI's own research-acceleration report states it has "now reached the goal, announced last fall, of having an automated research intern by September of this year" and that it is "making strong progress toward creating an automated AI researcher by March of 2028" — the first specific date attached to that longer-term milestone. The report backs the claim with adoption data: the median OpenAI researcher went from modest agent use at the start of 2026 to over $600/day of inference spend by mid-August (90th percentile: $7,000+/day), and the research org now uses 3.1 "agent-workdays" of effort for every human workday, a threshold crossed since June 2026. The same report cautions that agents still need significant human steering — in the last 6 months, over half of successful 4-8 hour tasks required one or more human interventions — and that people still set research priorities and decide whether to scale, pause, or deploy systems. See [Research acceleration: The view inside OpenAI](../sources/articles/openai-research-acceleration-2026-09-06.md).
- **GPT-6 Astra ships roughly on the named timeline, and the "is this AGI" debate fragments further (as of 2026-09-03):** OpenAI launched Astra 2026-09-03 — close to Pachocki's named "Automated AI Research Intern" target above. Reaction split into camps rather than converging: OpenAI staff and some benchmark authors called it a genuine generational leap; Artificial Analysis and Epoch read the gains as large but uneven once cost and non-cherry-picked evals are considered; a safety-focused camp (Ryan Greenblatt, Neel Nanda) argued the more consequential story is the system card's disclosed chain-of-thought monitorability decline, not the capability numbers. See [GPT-6 Astra](../models/gpt-6-astra.md) and [Agent safety and alignment research](agent-safety-and-alignment-research.md) for the fuller picture.

## Why it matters

Dated, named claims from lab leadership are a different kind of signal than marketing copy or a product launch post — they're falsifiable in a way that lets the wiki track whether they hold up. If OpenAI (or another lab) does declare AGI internally on roughly this timeline, or conspicuously misses it, that's a significant milestone for how the rest of the wiki's model and trend pages should be read.

## What to watch

- Whether OpenAI's Astra ships, and whether its capabilities match the "Automated AI Research Intern" framing
- Whether OpenAI (or any lab) makes a formal internal-AGI-declared announcement, and what evidence or benchmark accompanies it
- Whether other labs (Anthropic, Google DeepMind) make comparable dated claims

## Recent changes

- [2026-09-06] OpenAI's own research-acceleration report confirms the "automated research intern" milestone reached and names a new March 2028 target for a full automated AI researcher, backed by internal adoption data (3.1 agent-workdays per human workday since June 2026; 90th-percentile researcher spending $7,000+/day on inference) alongside a caveat that over half of successful 4-8hr tasks still need human intervention.
- [2026-09-03] GPT-6 Astra launches close to Pachocki's named timeline; reaction fragments into "genuine leap" / "mixed benchmarks" / "the monitorability decline is the real story" camps rather than converging on one read.
- [2026-09-02] OpenAI's Astra reaches the "Critical" cyber-capability threshold under OpenAI's own Preparedness Framework — testing reportedly found V8 zero-days, chained exploits, and sandbox escapes; Altman says safety work is slowing deployment pacing generally.
- [2026-08-28] OpenAI's Jakub Pachocki frames the unreleased Astra model as meeting his named "Automated AI Research Intern" milestone; Sam Altman estimates OpenAI will declare AGI achieved internally by December 2026 (TIME interview).

## Related

- [Restricted frontier deployment](restricted-frontier-deployment.md) — the inverse pattern: labs withholding or gating capability once a threshold is crossed, rather than declaring one reached

## Sources

- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — Claude Fable/Mythos 5.1: new SOTA model](../sources/newsletters/ainews-fablemythos-51-2026-09-02.md)
- [AINews — GPT-6 Astra: OpenAI's biggest LLM launch](../sources/newsletters/ainews-gpt-6-astra-launch-2026-09-04.md)
- [Research acceleration: The view inside OpenAI](../sources/articles/openai-research-acceleration-2026-09-06.md)
