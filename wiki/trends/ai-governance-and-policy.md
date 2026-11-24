---
title: AI governance and policy
type: trend
domains: [models, agents]
as_of: 2026-11-18
sources: [superhuman-ai-governance-economists-2026-07, ainews-fearing-rsi-pacing-letter-2026-07-29, openai-research-acceleration-2026-09-06, latent-space-thariq-pacing-the-frontier-2026-09-29, ainews-services-australia-transluce-unsc-2026-09-24, metr-anthropic-ai-rd-acceleration-2026-11-05, openai-research-acceleration-jagged-frontier-2026-11-18, amodei-we-must-pace-the-frontier-2026-09-14, anthropic-accenture-embedded-evaluation-2026-09-18]
---

# AI governance and policy

The trend: as frontier models grow more capable, pressure is building — from economists, the public, labs themselves, and now lab employees directly — for governments to take a more active role in steering AI development, rather than leaving it to market competition and voluntary lab commitments alone.

## Current signal (as of 2026-11-18)

Over 200 economists, including 16 Nobel laureates, signed "We Must Act Now," a public statement urging governments to steer AI development toward broad societal benefit. A companion Verasight survey found real public appetite for intervention: 60% of respondents are anxious about AI's rise, 89% want frontier labs required to publicly disclose safety-testing results, and 81% want government authority to block potentially dangerous models before release. A notable specific proposal — requiring AI firms to hand over equity stakes into a fund that redistributes AI's gains broadly — draws support from 69% of respondents and echoes OpenAI's own earlier offer of a 5% US government stake in the company. Separately, the US government has already reviewed both Anthropic's and OpenAI's most powerful models prior to release, so some of this oversight is already happening in practice, ahead of any formal policy.

The pressure has since spread inside the labs. On 2026-07-29, 1,171 frontier-lab employees cosigned a letter asking the US government to support tools to "deliberately pace" frontier AI development (critics call it vague regulatory capture); Dario Amodei's "Pacing the Frontier" post then named a first concrete step, embedded external evaluators. On 2026-09-06 and again on 2026-11-18 OpenAI repeated its position that AI companies should be *required* to publicly track their progress toward recursive self-improvement, by which point labs and METR had begun publishing such measurements. All are covered in the sections below.

## Frontier lab employees push for a "pacing" mechanism

On 2026-07-29, 1,171 employees across OpenAI, Anthropic, Google DeepMind, Meta, and Thinking Machines (xAI notably absent) cosigned a statement asking the U.S. government to support an international effort to build the technical and governance tools needed to "deliberately pace" frontier AI development. The stated concern: labs believe they may be close to automating AI research itself, which could accelerate capability gains beyond anyone's ability to understand or control the resulting systems, and no single lab or country can unilaterally slow down under competitive pressure without shared coordination tools. Framed as a personal-capacity statement rather than a corporate position, it nonetheless carried institutional weight — Dario Amodei cosigned, Sam Altman voiced public agreement, and OpenAI's official account tweeted it.

Reaction split sharply. Critics (Adam Thierer, Sarah Hooker, and others) called it a vague, unenforceable ask that functions as regulatory capture — burdening rivals and open-weight labs without binding commitments or thresholds, and unlikely to meaningfully constrain competitors such as China. Some signatories publicly qualified their own support, arguing coordination tools make sense in principle but any RSI-based policy needs far better quantification of labs' actual internal capabilities before it should bind anyone.

Dario Amodei's "Pacing the Frontier" post moved the idea toward a proposal. As Anthropic's Thariq Shihipar summarized it on 2026-09-29, most of its proposals are not worked out in detail, but the first step, which Anthropic is taking unilaterally and other labs are co-signing, is to embed external evaluators inside Anthropic. These would be people with no financial stake who can say a model should not ship or that RL should slow, and who can report practices to the public. Thariq grounds the case in recent agent incidents (see [OpenAI–Hugging Face agentic cyber incident](openai-huggingface-cyber-incident.md)): at the frontier, existing software is not ready for what agents will try, and labs face race dynamics. He described the reception as more accepting than expected, including in the US.

Amodei's essay "We Must Pace the Frontier" (September 2026) lays out three steps. Embedded evaluators come first and are the one Anthropic is taking alone; its first partner is Accenture, through its Faculty unit (see [Agent safety and alignment research](agent-safety-and-alignment-research.md)). Step two, **democratic coordination**, has frontier companies in democratic countries agree common safety standards and limits on the rate of unchecked progress. Amodei prefers regulation covering every US frontier company; in parallel, companies would set standards voluntarily, which needs a narrow US antitrust waiver. He favours pacing by capability checkpoints (a model with a given capability must come with certified alignment evidence from evals, interpretability or audits of training environments) over limits on inputs such as compute, which he considers easier to game. Step three, **global coordination**, means democracies trying to coordinate with authoritarian governments, chiefly China, while taking verification seriously. He ranks possible agreements by difficulty: bans on narrow dangerous uses such as bioweapons; mutual pre-release testing for acute risks through a global standards body; a SALT-style speed limit on recursive self-improvement; and a full pause, which he thinks unlikely soon. Because pacing inside democracies is capped by the US lead over China, he pairs it with chip export controls.

The UN Security Council held an AI session the same week (reported 2026-09-24). Sam Altman and Dario Amodei warned of loss of control and misuse, Yoshua Bengio urged immediate action, Hugging Face's Clément Delangue called for mandatory sharing of agent traces, and Michael Kratsios, speaking for the US, rejected a global regulator.

## Labs calling for mandatory progress disclosure

OpenAI's September 6 research-acceleration report repeats a position from its "frontier policy blueprint": that it and other AI companies should be *required* to publicly track their progress toward recursive self-improvement (RSI), not just do so voluntarily. It's a lab explicitly asking to be regulated on this specific point — aligning with the 89%-of-surveyed-public support for mandated safety-testing disclosure already tracked above, and with the US government's existing informal practice of reviewing frontier models pre-release.

OpenAI's 18 November follow-up repeats the call, now phrased as tracking and publicly reporting "indicators of recursive self-improvement," and points to a measurement norm forming across labs: Anthropic has published three internal acceleration reports, Google DeepMind's Gemini 4 Argon safety report tracks the share of AI-written code, and METR published an outside assessment of Anthropic on 5 November. METR's report also shows the limit of disclosure through a third party: Anthropic redacted most of the evidence METR relied on, so METR says the public has to lean on its judgment rather than weigh the evidence itself, and Anthropic dropped the planned check of its compute split between capabilities and safety midway through. The measurements are summarised on [AGI timeline claims](agi-timeline-claims.md).

## Why it matters

This is a distinct thread from [restricted frontier deployment](restricted-frontier-deployment.md): that trend is about labs and governments withholding or gating *already-built* models (export controls, partner-only access). This trend is about whether society should have a formal say in *how AI gets built and who benefits*, before or regardless of any single model's release. The July pacing letter adds a new source of pressure — lab employees themselves, not just outside economists or the public — while immediately surfacing the same regulatory-capture skepticism that shadows most lab-originated governance proposals.

## What to watch

- Whether any government moves from public pressure to an actual disclosure mandate or pre-release review requirement
- Further movement on equity-stake or sovereign-wealth-fund style proposals (OpenAI's 5% offer, the July survey's 69% support)
- Whether pacing moves beyond embedded evaluators to Amodei's steps two and three: regulation or voluntary standards among US labs (which need an antitrust waiver), and any US–China agreement, starting with the narrow-use bans and pre-release testing he calls feasible, given the US rejection of a global regulator
- Whether economists' and the public's demands converge with what labs are already doing voluntarily (pre-release government review) or push further

## Recent changes

- [2026-11-18] OpenAI repeats its call for mandatory reporting of recursive-self-improvement indicators as Anthropic, Google DeepMind and METR publish acceleration measurements; METR's Anthropic assessment (2026-11-05) shows the limit of third-party disclosure, with most key evidence redacted.
- [2026-09-29] "Pacing the Frontier" names its first step: external evaluators embedded inside Anthropic, co-signed by other labs; a UN Security Council AI session the same week saw calls for mandatory agent-trace sharing and a US rejection of a global regulator.
- [2026-09-18] Anthropic names Accenture (led by its Faculty unit) as the first embedded-evaluator partner; both expect to invest at least $1B over five years.
- [2026-09-14] Amodei's "We Must Pace the Frontier" details steps two (democratic coordination: regulation or antitrust-waived voluntary standards, capability checkpoints) and three (global coordination with China, from narrow-use bans to a self-improvement speed limit).
- [2026-09-06] OpenAI's research-acceleration report reiterates its "frontier policy blueprint" position that it and other companies should be required to publicly track progress toward recursive self-improvement (RSI) — an explicit mandatory-disclosure ask from a lab itself, aligning with the 89%-of-surveyed-public support for mandated safety-testing disclosure already tracked above.
- [2026-07-29] 1,171 frontier-lab employees (OpenAI, Anthropic, Google DeepMind, Meta, Thinking Machines) cosigned a letter asking the US government to support pacing mechanisms for frontier AI development; Amodei and Altman backed it publicly; critics call it vague regulatory capture.
- [2026-07-14] Initial page: 200+ economists' "We Must Act Now" statement and the Verasight survey on public appetite for AI regulation

## Related

- [Restricted frontier deployment](restricted-frontier-deployment.md) — labs and governments gating already-built models
- [Model sovereignty](model-sovereignty.md) — government pressure on open-weight models, the reported pre-release review window, and the open-weight-lab side of the regulatory-capture critique

## Sources

- [Superhuman — Anthropic lands another high-profile hire (AI governance statement)](../sources/newsletters/superhuman-ai-governance-economists-2026-07.md)
- [AINews — Fearing RSI: OpenAI, Anthropic, GDM, Meta cosign letter to "pace" AI development](../sources/newsletters/ainews-fearing-rsi-pacing-letter-2026-07-29.md)
- [Research acceleration: The view inside OpenAI](../sources/articles/openai-research-acceleration-2026-09-06.md)
- [Latent Space — Claude Code's Next Era: Thariq Shihipar on Pacing the Frontier and agent security](../sources/newsletters/latent-space-thariq-pacing-the-frontier-2026-09-29.md)
- [AINews — Services Australia breach, Transluce logs, and the UN Security Council AI session](../sources/newsletters/ainews-services-australia-transluce-unsc-2026-09-24.md)
- [METR — Independent assessment of AI R&D acceleration at Anthropic](../sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md)
- [Research acceleration: The jagged frontier](../sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md)
- [Dario Amodei — We Must Pace the Frontier](../sources/articles/amodei-we-must-pace-the-frontier-2026-09-14.md)
- [Anthropic — Partnering with Accenture on embedded evaluation](../sources/articles/anthropic-accenture-embedded-evaluation-2026-09-18.md)
