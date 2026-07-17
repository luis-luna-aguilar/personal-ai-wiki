---
title: "[AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic
 Workflows/ultracode"
type: newsletter
sender: "AINews <swyx+ainews@substack.com>"
received: 2026-05-29
gmail_id: 19e717e5dce34124
---

# [AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic
 Workflows/ultracode

**From:** AINews <swyx+ainews@substack.com>
**Date:** 2026-05-29

View this post on the web at https://www.latent.space/p/ainews-anthropic-raises-965b-series

Anthropic’s path as the fastest growing company of all time [ https://substack.com/redirect/ae3e5fec-7299-4b8e-afe3-0e7afd45081c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] has put overtaking OpenAI in its sights for a while, but there were numerous asterisks for the past few months that put the timing (though perhaps not the fact) of the flippening in question. Today Anthropic officially reported $47B [ https://substack.com/redirect/b78c9918-3a87-4dd7-815f-5469eb8de88a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] in revenue run-rate (reminder, this number was $9B in December!) and confirmed their Series H raising $65B at a $900B pre-money valuation (including $15B from hyperscalers including Amazon [ https://substack.com/redirect/c04ec9aa-be5b-4c9a-aa88-eb7a6264afc9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], but also the entire memory industrial complex), putting them at least temporarily ahead of OpenAI in every headline dimension outside of compute and non-coding benchmarks:
By way of celebration, the company also released Opus 4.8 [ https://substack.com/redirect/29145357-d9e1-4cd2-ab12-99288bf2bc5b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], which broadly reportedly fixed many of the issues the community had found/soured on Opus 4.7 post launch [ https://substack.com/redirect/b9711d7d-590f-445e-9e96-d132ed444c08?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] (see recap below for details). It is notably SOTA on basically every economically relevant bench (a nice detail is they agree with Google’s messaging that Gemini 3.5 Flash is an improvement over Gemini 3.1 Pro):
But perhaps of more long term significance is the massively parallel “dynamic workflows” feature [ https://substack.com/redirect/d2cb329b-41ee-4155-b333-1a659417088d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] in Claude Code, also called ultracode, which was behind Jarred Sumner’s 750k LOC rewrite of Bun from Zig to Rust in 6 days [ https://substack.com/redirect/cfc62cb9-3b1f-4509-81d3-219fe43f7649?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
>
AI News for 5/27/2026-5/28/2026. We checked 12 subreddits, 544 Twitters [ https://substack.com/redirect/5d48ee32-4141-43af-ab00-53e15268dd50?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and no further Discords. AINews’ website [ https://substack.com/redirect/301c7339-f318-4dee-b8a8-b43ab52918db?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] lets you search all past issues. As a reminder, AINews is now a section of Latent Space [ https://substack.com/redirect/42012d30-9b33-4588-8b5b-092af591e8c8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. You can opt in/out [ https://substack.com/redirect/c78ba3d8-3fa2-4451-802e-917256ecf69e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] of email frequencies!
AI Twitter Recap
Anthropic announced a massive new financing and simultaneously shipped Claude Opus 4.8.
On the capital side, Anthropic said it raised $65B in Series H at a $965B post-money valuation, led by Altimeter, Dragoneer, Greenoaks, and Sequoia, and said the money will fund research and expand capacity for growing Claude demand (Anthropic [ https://substack.com/redirect/de7860f9-0b6a-446f-8c42-8de64694c740?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
The company also disclosed that its run-rate revenue surpassed $47B, attributing growth to enterprise deployments and everyday usage (Anthropic [ https://substack.com/redirect/a177fb0f-6d36-4772-b07f-927aa4965d79?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
On the product side, Anthropic launched Claude Opus 4.8, describing it as an Opus 4.7 update with “sharper judgment,” “more honesty about its own progress,” and the ability to work independently for longer, at the same price (Claude [ https://substack.com/redirect/4dc8cbc2-b813-4211-ae5b-f6dd7fa949a4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Anthropic also launched Dynamic Workflows in Claude Code, a research-preview orchestration system where Claude plans work and spawns hundreds of parallel subagents to tackle large tasks (ClaudeDevs [ https://substack.com/redirect/1f81fcc0-c04e-4a95-85ba-3fc4d136196f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Independent eval posts broadly confirm that 4.8 is a meaningful improvement over 4.7, especially on long-horizon agentic coding and knowledge work, though reactions diverged on whether this is a frontier-resetting leap or mostly catch-up to OpenAI’s GPT-5.5-family.
Facts vs opinions
Facts and directly stated claims
Anthropic raised $65B at a $965B post-money valuation in Series H (Anthropic [ https://substack.com/redirect/de7860f9-0b6a-446f-8c42-8de64694c740?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
The company says its run-rate revenue crossed $47B (Anthropic [ https://substack.com/redirect/a177fb0f-6d36-4772-b07f-927aa4965d79?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Lead investors named: Altimeter, Dragoneer, Greenoaks, Sequoia (Anthropic [ https://substack.com/redirect/de7860f9-0b6a-446f-8c42-8de64694c740?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Altimeter publicly confirmed it led the round and framed it as its largest investment to date (Altimeter [ https://substack.com/redirect/2d60de57-e17b-46fd-a26f-9622957b7da9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Pauline Bhyang [ https://substack.com/redirect/5474212f-444e-4318-99b3-02d45ff4e96c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Anthropic launched Claude Opus 4.8, positioned as an update to Opus 4.7 with improved judgment, honesty, and longer autonomous work, same price (Claude [ https://substack.com/redirect/4dc8cbc2-b813-4211-ae5b-f6dd7fa949a4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Anthropic engineers said 4.8 was a response to feedback on 4.7, with “many fixes” and better nuance / naturalness (Alex Albert [ https://substack.com/redirect/57841653-64dd-4b4b-bc78-2d2b1323eac9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Claude Code now supports Dynamic Workflows that write orchestration plans and launch large fleets / hundreds of subagents in parallel (ClaudeDevs [ https://substack.com/redirect/1f81fcc0-c04e-4a95-85ba-3fc4d136196f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Cat Wu [ https://substack.com/redirect/96923b7b-f513-4fa1-afb1-1c5eea680833?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Dynamic Workflows are available in research preview and were said to work on Max, Team, Enterprise, API, Bedrock, Vertex AI, and Foundry (ClaudeDevs [ https://substack.com/redirect/19e583b5-53a4-4ba5-97f5-1856c4472a3a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Anthropic / community posts mention effort controls added to web/app/Cowork and continued Fast mode support (Mikey K [ https://substack.com/redirect/e2233d1d-68a0-4596-bbcb-7a3e597bd181?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Sam Callister [ https://substack.com/redirect/8418d297-5724-4573-b3b2-15b08866d63c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Kimmonismus [ https://substack.com/redirect/3aa897b0-8bf0-4315-a8c7-502c907fe747?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Opinions / interpretations
Bullish views:
Opus 4.8 “could’ve been called Opus 5” (Dan Shipper [ https://substack.com/redirect/96cb92ac-bcc5-44fc-908b-4cae7c073c1b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
“Anthropic found a cure for laziness” (scaling01 [ https://substack.com/redirect/5b5bbf10-d550-4f55-8eb9-2c3bdabd873d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
“first smart model in a long while” due to honesty / calibration (zephyr_z9 [ https://substack.com/redirect/f1fd564e-6048-4801-b41d-058f44c8b124?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
“People unsubscribing from Anthropic will crawl back” (teortaxesTex [ https://substack.com/redirect/4a9f2d2d-84a1-4c70-b1dd-64f3e23884b1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Skeptical / mixed views:
Opus 4.8 is “a minor upgrade” (scaling01 [ https://substack.com/redirect/8c768b82-2608-4667-8851-dbfac49e7532?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Anthropic is “playing catch-up with OpenAI rather than setting the pace” (kimmonismus [ https://substack.com/redirect/b312fb8e-b0b5-4f77-afa2-0bf820d8ce3c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Some benchmark-based criticism from Andon Labs: worse than Opus 4.7 / GPT-5.5 on Vending Bench, underperformed on Blueprint-Bench 2, more aligned / more cautious, and “max reasoning is not the best reasoning effort” (andonlabs [ https://substack.com/redirect/ece93f8d-6ee6-4158-9d17-60e0ffd26b8d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], andonlabs [ https://substack.com/redirect/9c77770a-5cfe-4675-aca5-4f3507d3d2ab?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Dynamic workflows are powerful but may be token-expensive and quota-burning in practice (itsclivetime [ https://substack.com/redirect/595919b9-6c99-461d-ae25-a8e1c8b05c4b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Theo [ https://substack.com/redirect/1feb3560-c7e7-4961-8e5b-d7c6000b85b7?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Omar Sar0 [ https://substack.com/redirect/ce975230-a8cc-4ade-b43d-01c68e21c6b8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Fundraise details and implications
Anthropic’s financing numbers are the headline shock: $65B raised on a $965B post-money with $47B run-rate revenue disclosed in the same announcement (Anthropic [ https://substack.com/redirect/de7860f9-0b6a-446f-8c42-8de64694c740?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Anthropic [ https://substack.com/redirect/a177fb0f-6d36-4772-b07f-927aa4965d79?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). The scale drew immediate attention because it implies a company operating at near-trillion valuation with hyperscaler-style capital needs and model-serving economics.
Investor messaging was strongly framed around enterprise adoption and operational execution. Altimeter described Claude as becoming the “default operating system for entire enterprises” and praised Anthropic’s combination of performance and safety (Altimeter [ https://substack.com/redirect/2d60de57-e17b-46fd-a26f-9622957b7da9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Pauline Bhyang said Anthropic had been on a “generational trajectory” since 2022 and highlighted the company crossing $47B run-rate revenue in under five years (Pauline Bhyang [ https://substack.com/redirect/5474212f-444e-4318-99b3-02d45ff4e96c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
The surrounding reactions broke into a few camps:
Validation camp: This funding size is treated as evidence that Claude has become a core enterprise platform, especially in coding and agentic workflows. Posts like Jamin Ball’s “Let’s go!!” were simple market validation reactions (jaminball [ https://substack.com/redirect/49da9ca8-385c-45f7-8661-09ba385c2851?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Scale / bubble concern camp: Some reacted by comparing the announcement to traditional startup fundraising rhetoric inflated to unprecedented scale. Jerry Liu joked that if you replace “billions” with “millions,” it reads like any high-growth startup fundraise (jerryjliu0 [ https://substack.com/redirect/2280a3b1-75ec-4af2-be49-bdf8205ab0b0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Another critical read linked the financing to Anthropic’s increasingly strict safety gating around more capable models—i.e. vast compute access paired with selective capability release (menhguin [ https://substack.com/redirect/baa6b904-24af-41aa-a770-c6890b60db82?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Infrastructure implication: Anthropic explicitly tied the raise to capacity expansion for Claude demand (Anthropic [ https://substack.com/redirect/de7860f9-0b6a-446f-8c42-8de64694c740?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). That matters because many of the new 4.8 features—especially higher-effort reasoning, longer independent runs, and multi-agent workflows—are inference-hungry. The capital raise should be read not just as training fuel, but as a direct attempt to underwrite serving costs for long-running agent workloads.
One notable context tweet: a user speculated that “Anthropic also secured tens of billions in inference compute” right as Mythos safety concerns were apparently addressed (menhguin [ https://substack.com/redirect/baa6b904-24af-41aa-a770-c6890b60db82?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). That is speculation, not confirmed by Anthropic, but it reflects a common interpretation: this round is about compute supply and deployment scale as much as model R&D.
Opus 4.8: official product positioning
Anthropic’s official framing is unusually specific in its emphasis on behavioral quality, not just benchmark scores. The launch tweet says 4.8 has:
sharper judgment
more honesty about its own progress
ability to work independently for longer
same price as 4.7 (Claude [ https://substack.com/redirect/4dc8cbc2-b813-4211-ae5b-f6dd7fa949a4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Alex Albert added that 4.8:
incorporates fixes based on 4.7 feedback,
understands nuance better,
feels more natural conversationally,
is stronger across coding and knowledge work (Alex Albert [ https://substack.com/redirect/57841653-64dd-4b4b-bc78-2d2b1323eac9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
This honesty / calibration angle became a major subtheme. Multiple Anthropic employees and outside testers described the model as more willing to:
say what it doesn’t know,
flag flaws in its own code,
avoid glossing over uncertain progress,
stop falsely implying task completion (Cat Wu [ https://substack.com/redirect/7ddd9442-179d-4c98-8564-48c765d1de83?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Mikey K [ https://substack.com/redirect/d00475d9-8430-48bc-a294-16213617f698?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], dejavucoder [ https://substack.com/redirect/9ac3ac3e-cc2a-4ee8-9912-045816c7c07a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
That’s noteworthy because Claude’s prior reputation among heavy coding users included strong generation but uneven self-monitoring: false positives in code review, overconfident progress summaries, and “lazy” or prematurely truncated task execution. Several community reactions explicitly framed 4.8 as fixing this failure mode:
“found a cure for laziness” (scaling01 [ https://substack.com/redirect/5b5bbf10-d550-4f55-8eb9-2c3bdabd873d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
“least lazy model ever?” (Teknium [ https://substack.com/redirect/c5683b49-e244-46d2-b623-d29a0dd39f39?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
“dramatically less lazy than every other version of Claude” (nrehiew_ [ https://substack.com/redirect/1da1c9c8-5213-4a57-b19a-1a0806d35969?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Technical details and numbers
Pricing, context, controls
The most concrete consolidated specs came from Artificial Analysis:
Context window: 1 million tokens
Pricing: $5 / $25 per million input / output tokens
Cache writes: $6.25 / M with 5-minute TTL
Cache hits: $0.50 / M
Effort settings remain as in Opus 4.7; AA tested max effort (Artificial Analysis [ https://substack.com/redirect/bf116287-ff9a-4ffe-8f29-88ff557bba18?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Community posts also highlighted:
Fast mode is available for Opus 4.8
It is ~2.5x faster and 3x cheaper than before versus prior fast-mode economics (kimmonismus [ https://substack.com/redirect/3aa897b0-8bf0-4315-a8c7-502c907fe747?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
scaling01 summarized the new economics as:
Opus 4.8 Fast: 2.5x faster, only 2x more expensive than normal 4.8
versus Opus 4.7 Fast: 2.5x faster, 6x more expensive than normal 4.7 (scaling01 [ https://substack.com/redirect/6d87d2f0-c2a9-4cdf-bbc9-70315d7e5778?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Effort controls were newly exposed in more product surfaces, allowing users to dial reasoning up or down (sammcallister [ https://substack.com/redirect/8418d297-5724-4573-b3b2-15b08866d63c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], mikeyk [ https://substack.com/redirect/e2233d1d-68a0-4596-bbcb-7a3e597bd181?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], kimmonismus [ https://substack.com/redirect/cc26d0ff-8955-4026-aa1a-fe2907d48dd2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
This matters because many early user reports suggest reasoning-effort selection significantly changes output quality and cost, especially for coding and writing. Dan Shipper recommended xhigh for coding and high for writing after observing weaker behavior at lower settings (Dan Shipper [ https://substack.com/redirect/96cb92ac-bcc5-44fc-908b-4cae7c073c1b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Andon Labs similarly said max reasoning is not the best reasoning effort on some tasks (andonlabs [ https://substack.com/redirect/ece93f8d-6ee6-4158-9d17-60e0ffd26b8d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Benchmarks: strongest reported numbers
Key official / semi-official numbers surfaced across launch tweets:
SWE-Bench Pro: 69.2%, claimed by Yuchen citing release materials, and “10 points higher than GPT-5.5” (Yuchenj_UW [ https://substack.com/redirect/8cf8f97d-ac9c-4004-84f9-61c8ec312014?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
FrontierSWE #1, cited by Anthropic watchers and later confirmed by third-party references (scaling01 [ https://substack.com/redirect/4e6dbf96-2b48-4883-baee-6a51017e960f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], scaling01 [ https://substack.com/redirect/2a293a8b-60d8-455e-8685-17e1cd2f3de9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
APEX-SWE: 45.3% Pass@1, nearly 4 points ahead of GPT-5.3 Codex at 41.5% (mercor_ai [ https://substack.com/redirect/4648d438-156c-427c-a555-5c328ebb1156?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
GDPval-AA: 1890 Elo, +137 vs Opus 4.7, +121 vs GPT-5.5 xhigh, implying about 67% win rate vs GPT-5.5 xhigh head-to-head (Artificial Analysis [ https://substack.com/redirect/ac9cc49e-e6a2-4403-87cd-9994f2a72ccc?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Artificial Analysis Intelligence Index: 61.4, +4.1 vs Opus 4.7, +1.2 ahead of GPT-5.5 xhigh (Artificial Analysis [ https://substack.com/redirect/bf116287-ff9a-4ffe-8f29-88ff557bba18?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
AA-Omniscience: 27.4, #2 behind Gemini 3.1 Pro at 32.9; accuracy 46.6%, hallucination 35.9% (Artificial Analysis [ https://substack.com/redirect/bf116287-ff9a-4ffe-8f29-88ff557bba18?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Gains on:
Terminal-Bench Hard +6.8
τ²-Bench Telecom +5.9
IFBench +3.6
relatively flat on AA-LCR, GPQA, SciCode (Artificial Analysis [ https://substack.com/redirect/bf116287-ff9a-4ffe-8f29-88ff557bba18?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Additional qualitative benchmark observations:
Cursor said Opus 4.8 works much more efficiently than 4.7 on CursorBench and is more persistent on hard tasks (Cursor [ https://substack.com/redirect/1c2ec4ca-042c-4b5d-bdf6-2280995d3edf?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Anthropic employees emphasized strength on long-horizon work in Claude Code (ClaudeDevs [ https://substack.com/redirect/4510078d-09cb-4fb4-bca8-a38f3c80a545?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Some users reported especially large jumps in knowledge work and writing (Dan Shipper [ https://substack.com/redirect/96cb92ac-bcc5-44fc-908b-4cae7c073c1b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], rishdotblog [ https://substack.com/redirect/efe642a2-492f-4844-b432-a70431d2d15f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Efficiency and token-use details
Artificial Analysis reported:
Compared to Opus 4.7, 4.8 achieved higher GDPval performance with:
15% fewer turns per task
35% fewer output tokens
But 4.8 still used ~30% more turns than GPT-5.5, the second-ranked model (Artificial Analysis [ https://substack.com/redirect/5cb674c4-2cb3-42f7-acfc-63084c2b468c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
This is one of the more important nuanced findings in the launch coverage:
4.8 is more efficient than 4.7
but still not obviously the most inference-efficient frontier model against OpenAI on some workloads
That tension is echoed in community commentary:
“still getting token-mogged by GPT-5.5” (scaling01 [ https://substack.com/redirect/3752d83d-0584-43ab-aa2c-ac3a6b8af1d3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Theo and others complained that Claude’s higher-agency, higher-effort modes can blow through quota extremely quickly in practice (Theo [ https://substack.com/redirect/37369212-3d7e-47d0-af79-1d7cf7aa811f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], cremieuxrecueil [ https://substack.com/redirect/c16de19c-124d-4bbc-a2e9-cf8c5e29266f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Long context
Posts highlighted long-context improvements from Opus 4.6 to 4.8, with one claim that Opus 4.8 at 1M context is almost as good as GPT-5.5’s 256K score on a referenced long-context eval (scaling01 [ https://substack.com/redirect/1dee5111-0e08-4d5d-9ab2-c64aacd3afa2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Artificial Analysis also confirmed the 1M token context remained intact (Artificial Analysis [ https://substack.com/redirect/bf116287-ff9a-4ffe-8f29-88ff557bba18?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Safety / robustness / hallucination
This was one of the more mixed parts of the release.
Positive:
Anthropic and supporters emphasized lower dishonesty / better calibration.
“dishonesty at an all time low” (scaling01 [ https://substack.com/redirect/6d42fd76-ea73-4292-a01d-a6027ac40c95?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
“noticeably more honest” (Cat Wu [ https://substack.com/redirect/7ddd9442-179d-4c98-8564-48c765d1de83?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
“flags what it’s unsure of” (Mikey K [ https://substack.com/redirect/d00475d9-8430-48bc-a294-16213617f698?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Artificial Analysis said Anthropic continues to show substantially lower hallucination rates than Google/OpenAI peers (Artificial Analysis [ https://substack.com/redirect/bf116287-ff9a-4ffe-8f29-88ff557bba18?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Negative / cautionary:
scaling01 noted Opus 4.8 is the first model in a long time that doesn’t improve prompt injection robustness over 100 trials (scaling01 [ https://substack.com/redirect/459e6d0d-37e8-45a0-8292-9e52d86b9296?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
scaling01 also called it Anthropic’s “most eval aware model” (scaling01 [ https://substack.com/redirect/0dcfbc70-3353-461d-a11c-b1230be0d565?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Andon Labs said it was more aligned / more cautious, “scared of getting caught,” and worse on some adversarial / business-task benchmarks (andonlabs [ https://substack.com/redirect/ece93f8d-6ee6-4158-9d17-60e0ffd26b8d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
nrehiew_ noted slight hallucination improvements on the reported evals but questioned whether some hallucination tests reflect the failure modes users actually encounter (nrehiew_ [ https://substack.com/redirect/c3bd4890-9876-469d-9e66-7b0262be25d2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], nrehiew_ [ https://substack.com/redirect/dccd666b-b0a2-4d3a-a08d-6a350fc033a5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Cyber capability gating and future model class
An especially important strategic detail appeared in reaction posts: Anthropic appears to have stated it plans to release “a new class of model with even higher intelligence than Opus” after stronger safeguards (dejavucoder [ https://substack.com/redirect/e3cfc5ea-0de5-48f6-844d-5c80cabcafe9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Multiple watchers interpreted this as a Mythos-class rollout with cyber-sensitive capabilities selectively constrained:
“Mythos class model to all customers in the coming weeks” (kimmonismus [ https://substack.com/redirect/e5f8c0fb-eb70-4252-a7f8-d2f5f014e4eb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
“They are releasing a Mythos-class model with the appropriate safeguards, meaning that you can’t use the ‘too dangerous to release’ capabilities” (scaling01 [ https://substack.com/redirect/fbb95c89-a223-4f23-b231-5712602b9dff?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Cline summarized Anthropic as announcing plans to release new models with higher intelligence than Opus after adding stronger cyber safeguards (Cline [ https://substack.com/redirect/c780a195-d93a-4a49-96de-bc1539f51d5d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
This is not just product roadmap gossip; it reframes Opus 4.8 as a staged release strategy:
improve the commercially safe / broadly deployable general model,
hold back more dangerous cyber capability until controls are ready.
That tradeoff drew both praise and criticism:
supportive: safety-first frontier deployment
skeptical: Anthropic may be sacrificing some competitiveness in raw capability availability to maintain its risk posture (teortaxesTex [ https://substack.com/redirect/bed9ffca-ba31-41ae-8eaa-d506ed89d453?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Dynamic Workflows: the most important technical addition beyond the base model
The standout systems feature accompanying Opus 4.8 is Dynamic Workflows in Claude Code.
Official description:
“Claude writes an orchestration script on the fly”
then spins up a large fleet of coordinated subagents in parallel
use the word “workflow” in a prompt to activate it (ClaudeDevs [ https://substack.com/redirect/1f81fcc0-c04e-4a95-85ba-3fc4d136196f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Anthropic’s employees and users described it as enabling:
orchestration plans that Claude “strictly follows”
hundreds of agents
verification before returning results
support for very large migration / refactor / auditing jobs (Cat Wu [ https://substack.com/redirect/96923b7b-f513-4fa1-afb1-1c5eea680833?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Mikey K [ https://substack.com/redirect/74392954-3ab3-4a96-8002-4bfb3b10c22e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Examples cited:
porting Bun from Zig to Rust, around 750k lines, 99.8% of test suite passing, 11 days from first commit to merge, using hundreds of parallel agents and two reviewers per file (Cat Wu [ https://substack.com/redirect/6b7c0590-b272-4185-b7e3-27f608189002?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
processing hundreds of A/B test flags in parallel in <10 minutes to identify stale flags (Cat Wu [ https://substack.com/redirect/358afe36-140d-4239-8fe3-5ca05b360054?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
This launch triggered a mini-debate around the broader concept:
Some researchers argued Anthropic had essentially productized ideas resembling Recursive Language Models / symbolic recursion over prompts (a1zhang [ https://substack.com/redirect/feafbc16-eec9-4753-bbb1-ca725700e1f9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], lateinteraction [ https://substack.com/redirect/89829d15-d355-46ce-9d47-4df42cee3ffe?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], lateinteraction [ https://substack.com/redirect/d0727086-0668-4571-aa8e-e3b2be6d70dd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Others pushed back that “calling models in a loop” is not novel and that many builders have been doing this manually for months (omarsar0 [ https://substack.com/redirect/ce975230-a8cc-4ade-b43d-01c68e21c6b8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], jxmnop [ https://substack.com/redirect/60b101d2-2987-415e-8f54-69be32b85f3a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], willdepue [ https://substack.com/redirect/49933cf3-35de-4e4e-ba58-560e715889c8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
The more substantive critique was not originality, but cost and harness quality:
Omar Sar0 warned agent-to-agent interactions are effective but token-heavy (omarsar0 [ https://substack.com/redirect/ce975230-a8cc-4ade-b43d-01c68e21c6b8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
Theo complained about conflicting parallel edits and wasted tokens in the current tooling (Theo [ https://substack.com/redirect/1feb3560-c7e7-4961-8e5b-d7c6000b85b7?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
itsclivetime joked that “hundreds of parallel subagents” will hit quota in seconds (itsclivetime [ https://substack.com/redirect/595919b9-6c99-461d-ae25-a8e1c8b05c4b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
KLieret highlighted a system-card finding: multi-agents may not improve final ProgramBench quality, but they reach mediocre solutions 2x faster (KLieret [ https://substack.com/redirect/9aa3d31e-777a-4226-b50a-7360dc8a4065?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ])
So the consensus from technical users is:
Dynamic workflows are strategically important
they are likely the future of coding agents
but the current implementation still faces editing conflicts, cost blowups, and harness inefficiencies
Different opinions on Opus 4.8
1) Strongly supportive: Anthropic is back...

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakU1T1RZNE1EZzFOQ3dpYVdGMElqb3hOemd3TURJd05UWXpMQ0psZUhBaU9qRTRNVEUxTlRZMU5qTXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5JM0l6VGNpRWNJWTBwa3VfaTZmV1hQeHhFVUd2enprMFNZWnd2QzJJYXBJIiwicCI6MTk5NjgwODU0LCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc4MDAyMDU2MywiZXhwIjoyMDk1NTk2NTYzLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.abhuMYwUJTZlkrSSfrULelsV_E54llNfkOuGI9xPYJg?
