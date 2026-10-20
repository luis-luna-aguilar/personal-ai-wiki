---
title: "[AINews] Claude Haiku 5.5 — better than GPT-6 Luna at the same pricing"
type: newsletter
sender: "AINews <swyx+ainews@substack.com>"
received: 2026-10-08
gmail_id: 1a11a6c683f8e328
---

# [AINews] Claude Haiku 5.5 — better than GPT-6 Luna at the same pricing

**From:** AINews <swyx+ainews@substack.com>
**Date:** 2026-10-08

View this post on the web at https://www.latent.space/p/ainews-claude-haiku-55-better-than

It’s been about a year since Anthropic shipped Haiku 4.5 [ https://substack.com/redirect/0eab4144-e09e-4068-b4c5-36690872f360?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and with successive launches of Sonnet and Opus and Fable up to 5.5 it was seeming a little forgotten, especially as OpenAI launched Luna 6 alongside Astra and Sol 6.
Well, it’s here, and it’s a welcome update. More in the summary below.
AI News for 10/06/2026-10/7/2026. We checked 12 subreddits, 544 Twitters [ https://substack.com/redirect/6973fc8f-17fe-4378-b32b-040a75f7384f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and no further Discords. AINews’ website [ https://substack.com/redirect/e1328eae-d684-4005-9fb0-450ec963fe34?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] lets you search all past issues. As a reminder, AINews is now a section of Latent Space [ https://substack.com/redirect/5ad4ec06-7fe8-4e95-8f2f-0e89e10b1c65?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. You can opt in/out [ https://substack.com/redirect/f5b7157c-df12-4a53-935e-a227c1b8ee11?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] of email frequencies!
AI Twitter Recap
Top Story: Anthropic releases Claude Haiku 5.5
What happened
Anthropic shipped Claude Haiku 5.5, its first Haiku-tier update in about a year. It is priced to match OpenAI’s GPT-6 Luna, and Anthropic cut prices on Sonnet 5.5 and its subscription plans the same day.
Pre-launch signals. @scaling01 [ https://substack.com/redirect/c81fbeb2-eaae-48db-a6bb-0061d25d6898?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] posted “happy Haiku 5.5 day” before the announcement. @kimmonismus [ https://substack.com/redirect/40a77b02-44ff-4180-8c2d-6bf515228880?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] said the model had already appeared in a Claude Code update and predicted “Luna-pricing.” He then posted the pricing ahead of the official post (@kimmonismus [ https://substack.com/redirect/7234392c-3aba-48fa-a5a9-704cc00a18f6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]) and confirmed when it went live (@kimmonismus [ https://substack.com/redirect/ea629aa2-d907-4afc-80e0-80719aa2c87a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Official launch. @claudeai [ https://substack.com/redirect/8f64d7de-d0d2-4886-b0fd-c3454ac86002?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @AnthropicAI [ https://substack.com/redirect/8e3bc23c-a9cd-4bb6-a5ed-c57b87cf76a7?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] called it “the cheapest, fastest, and most capable small model we’ve ever released,” costing about 75% less to run than Haiku 4.5 on average.
Availability and intended use. It is live on the Claude Platform and in Claude Code (@ClaudeDevs [ https://substack.com/redirect/7b3444a7-0cac-4a65-999d-e8cc939e8323?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Anthropic positions it as a subagent paired with Opus 5.5 or Sonnet 5.5, for high-volume, cost-sensitive work such as summaries, compactions and database queries. @mikeyk [ https://substack.com/redirect/75af9a15-b79b-4cef-ae1f-7bb53b498008?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] described the split as “Opus does the heavy thinking, Haiku does the high-volume work.”
Tiered pricing (@ClaudeDevs [ https://substack.com/redirect/a32c4cfc-3110-4470-9d17-6229e045f227?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]):
Prompt lengthInput / output per 1M tokensCache reads per 1MUnder 100K tokens$0.10 / $0.50$0.01Over 100K tokens$0.50 / $2.50$0.05
Sonnet 5.5 price cut. Cache reads were halved from $0.20 to $0.10 per 1M tokens. Anthropic says this makes Sonnet 5.5 about 20% cheaper on most long-running or agentic work (@claudeai [ https://substack.com/redirect/460ef54e-5bd1-4b3d-a5a0-b187c8acc809?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
API credits for subscribers. Monthly Claude Platform API credits now come with Max 5x ($100), Max 20x ($200) and Team (up to $500, pooled). They work on any model, including Haiku 5.5, and in third-party harnesses (@ClaudeDevs [ https://substack.com/redirect/f206fa0f-bdf6-4c99-ab84-46a71d73e18d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Same-day SDK update. Computer-use and browser-use toolsets are now built into the Python and TypeScript Claude SDKs. The SDK runs the action loop and sends clicks and keystrokes to drivers from browser_use, Browserbase, E2B or Daytona, so developers no longer write that loop themselves (@ClaudeDevs [ https://substack.com/redirect/c98e119f-176b-4557-8bf0-af960533acae?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], quickstart [ https://substack.com/redirect/30461395-2e0c-499a-a78d-95c855e061b3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Partner rollouts on day one:
Cursor: @cursor_ai [ https://substack.com/redirect/ae90bc1a-2ceb-49ea-9840-fcff28e7dcaf?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] claims “10x less than Haiku 4.5” on shorter requests and published CursorBench comparisons (@cursor_ai [ https://substack.com/redirect/fa00ffdc-7662-469d-af94-eeec4588531b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
GitHub Copilot in VS Code: @code [ https://substack.com/redirect/ce96e55f-9625-4769-b362-d2b75ab86fd6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] reports it “matched Claude Sonnet 5 on many coding tasks while using fewer tokens and steps.”
Devin: @cognition [ https://substack.com/redirect/967e68f9-2389-4850-9dae-f4c07d7ad9c1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] reports 58.4% on FrontierCode 1.1, ahead of Sonnet 5 at roughly one-eighth the cost per task, and recommends it as a “sidekick” under an Opus 5.5 lead in Fusion.
Arena: added to Agent Arena, Code Arena WebDev, Text, Document and Vision, with scores pending (@arena [ https://substack.com/redirect/506cc9a3-f833-4c47-a1d4-464391a308e6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
OpenDocRouter: added the same day (details below).
Independent evaluation: Artificial Analysis
@ArtificialAnlys [ https://substack.com/redirect/66538231-8ffb-445a-ba04-5740624043f2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] published the most detailed third-party numbers (per-eval breakdown [ https://substack.com/redirect/aad706a5-4232-4b46-ad60-7b5247bda610?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], comparison page [ https://substack.com/redirect/48aae59c-c3f2-46c4-8461-79a31778e3f0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Intelligence Index: 43 at max effort, up 26 points from the previous Haiku.
Slightly ahead of GLM-5.3 Flash (42), Gemini 3.8 Flash (41) and GPT-6 Luna (38).
Comparable to Kimi K3 (44), a 2.8T-parameter open-weights model.
Trails Claude Sonnet 5.5 at max effort (56) by 13 points.
New controls. This is the first Haiku with Anthropic’s effort settings and adaptive thinking.
Token usage is the main caveat.
At max effort it uses about 162k output tokens per Index task, roughly 3x GPT-6 Luna at max (~50k).
Going from xhigh to max adds 2 points for about 1.8x the tokens.
At equal score it is still more verbose: Haiku 5.5 at high effort scores 38 using ~55k tokens, versus Luna at max scoring 38 with ~50k. The gap widens at lower effort settings.
Cost figures are provisional. Artificial Analysis does not yet model the 5x price step above 100K tokens. Cost-per-task numbers will follow.
AA-Briefcase (private agentic knowledge-work eval): 1578 Elo. That is ahead of Kimi K3 and GLM-5.3, and comparable to Muse Spark 1.3 at max.
Terminal-Bench 4.0: 33%, up from 0% for Haiku 4.5.
Level with GLM-5.3 Flash.
Ahead of Gemini 3.8 Flash (20%) and GPT-6 Luna (13%).
Knowledge versus hallucination (AA-Omniscience):
ModelAccuracyHallucination rateHaiku 5.536%40%Gemini 3.8 Flash55%55%GPT-6 Luna44%77%
Part of Haiku’s lower accuracy comes from being more willing to say it doesn’t know.
AutomationBench-AA: 35%, versus 53–60% for Luna, Gemini 3.8 Flash and GLM-5.3 Flash. A pre-release safety bug caused the model to over-refuse. Anthropic is working on a fix, and Artificial Analysis will re-run the eval and expects the score to rise.
Specs:
1M-token context, up from 200k for Haiku 4.5.
Text and image input, text output.
5-minute cache writes cost $0.125 per 1M tokens ($0.625 above 100K).
Other benchmark claims (mostly vendor or secondhand)
@ShayneRedford [ https://substack.com/redirect/22738614-59fc-4bc2-bc70-355e0e125b23?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] summarized Anthropic’s reported jumps:
OSWorld (computer use): 15% → 72%.
TerminalBench: 0% → 39%. This differs from Artificial Analysis’s independent 33% on Terminal-Bench 4.0.
10–50% gains in knowledge work and reasoning.
Beats Luna on most of these.
1M context with roughly 12k max output tokens.
@alexalbert__ [ https://substack.com/redirect/367d96a9-2f0c-47c1-a68d-f3366b90b9d3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] (Anthropic) stressed that Haiku 4.5 shipped Oct 15, 2025, so the comparison spans less than a year.
@TheRundownAI [ https://substack.com/redirect/8b907d81-14b1-4274-b48b-96ecead4922d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] reported that it beats GPT-6 Luna “across a variety of benchmarks.”
Document parsing (independent, on ParseBench):
@LoganMarkewich [ https://substack.com/redirect/09f39312-8ee7-43b4-a7d8-46082fa7b3e7?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: overall close to Luna, slightly better on tables, worse on chart understanding.
@jerryjliu0 [ https://substack.com/redirect/329347fa-1deb-41a1-b301-7fb2f2af328f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: about $1.2 per 1,000 pages. Good at tables and reading order for the price; weaker on charts, semantic formatting and bounding boxes.
Anecdotal:
@simonw [ https://substack.com/redirect/fcd425dd-0882-4dec-baad-5c78d4a39090?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] wrote pricing notes and ran his pelican-on-a-bicycle test. He says it is “SO MUCH better” than Haiku 4.5, which costs 10x more (comparison [ https://substack.com/redirect/c7d1ac5b-d970-41cd-b032-70e4f6f71290?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
@AI_Screening [ https://substack.com/redirect/6cb5fdb5-153a-46ba-ad32-55f7a728c25c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] says Haiku 5.5 “cooked” Luna on a Three.js zebra simulation (single prompt, not systematic).
Opinions and reactions
Bullish
@kimmonismus [ https://substack.com/redirect/b4ffc688-49d5-46f2-9ed7-eeb08646c526?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: “Way better than GPT-6-Luna, close[r] to Sonnet 5.5… Cheap and smart.”
@theo [ https://substack.com/redirect/38fdf1c3-01f8-414f-8e72-45baaf1cb06e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] likes the tiered pricing: charging a fifth of the price under 100K tokens “makes it really clear what the model is for.” He also found it striking to see an Anthropic model “so far to the left on the cost/intelligence charts” (@theo [ https://substack.com/redirect/294aae6c-ef47-4435-9326-a21cdf5c7176?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]) and covered the launch on stream (@theo [ https://substack.com/redirect/ad2b7d87-a10d-420f-a4c3-18a3534dff5d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
@draecomino [ https://substack.com/redirect/aa017466-6a0e-410c-9659-2158c1fe04bb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: “Haiku at max effort performs like a frontier model.”
@kipperrii [ https://substack.com/redirect/086b5c03-a523-4d78-92c8-b4eff65f580f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] argues small, cheap models matter more now that they can do “a ton of useful things.”
@scaling01 [ https://substack.com/redirect/fbac1d95-50ca-4ec3-bc98-ded93205c880?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] (”cheap af”) and later (@scaling01 [ https://substack.com/redirect/c70799e6-6d91-4944-ab7d-8549f2877c77?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]): “5.5 models are looking good.”
@NotTomBrown [ https://substack.com/redirect/a98b448c-bda2-4716-806f-685b512f36dc?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] (”small but mighty”) and @edwinarbus [ https://substack.com/redirect/628b9730-7c8d-4cf2-b618-04f616c2fe7c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], both from the Anthropic side, posted celebratory notes.
Competitive framing
The launch is widely read as aimed at OpenAI’s GPT-6 Luna: “rip gpt 6 luna” (@dejavucoder [ https://substack.com/redirect/0902a95a-54f6-4edc-b40a-434d969e99f3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]), “time to cook Luna” (@scaling01 [ https://substack.com/redirect/ac22eefb-af57-44e6-8269-c81d6e1422b2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
@kimmonismus [ https://substack.com/redirect/d0dc5fce-6831-4baf-8d0a-159eec26afb4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] framed the Sonnet cache-read cut as Anthropic pressuring OpenAI. On the API credits he added, “OpenAI: your turn” (@kimmonismus [ https://substack.com/redirect/25f3bed7-cf56-419d-9aaa-b033d49b60c7?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
@teortaxesTex [ https://substack.com/redirect/002796fe-8823-49db-b944-83e7a9e79281?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] says Anthropic now has “the deepest product lineup of all labs” (Haiku/Sonnet/Opus/Fable plus Mythos) versus OpenAI’s Luna/Sol/Astra. He still thinks Anthropic “cares less about products,” which he reads as a sign of how much slack it has had through 2026.
ThursdAI’s @altryne [ https://substack.com/redirect/9c964864-c345-42c5-b8e3-45ca192516c0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] questioned the middle tier: “Sonnet made sense when Opus was expensive.” The show plans to cover Haiku 5.5 (@thursdai_pod [ https://substack.com/redirect/ed629fdc-96a4-4be1-a8f4-68abf15a6718?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]).
Caveats (mostly from the data, not loud critics)
The headline price may overstate real savings.
Heavy token use (about 3x Luna at max effort) offsets part of the per-token discount.
Prompts over 100K tokens pay 5x more, which matters for long-context agent loops.
These two effects likely explain why Cursor’s “10x cheaper on short requests” differs from Anthropic’s “75% cheaper on average.”
Factual recall is weaker than Gemini 3.8 Flash and Luna.
The over-refusal bug currently depresses the automation score.
Not yet benchmarked: Arena scores are pending, and independent cost-per-task figures await tiered-pricing support.
Context
Haiku 4.5 has been Anthropic’s small model since October 2025. Since then, OpenAI’s GPT-6 Luna, Gemini 3.8 Flash, GLM-5.3 Flash and DeepSeek V4.1 Flash have competed at the low-cost end.
Haiku 5.5 matches Luna’s sticker price exactly. It adds effort control and a 1M context.
It is explicitly positioned as the cheap worker inside multi-model agent harnesses: Claude Code subagents, Devin Fusion, Copilot subagents, and compaction or summarization steps.
Anthropic paired it with Sonnet cache-read cuts and subscription API credits, a coordinated push on agent economics. That push lands amid wider debate over token bills (see @theo [ https://substack.com/redirect/76b6722d-6d45-407e-ae01-bcac560cdf75?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] below).
Other News
OpenAI’s 722 Math Manuscripts: Scale, Efficiency and Fallout...

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakl4T1RNNE5qUTVNaXdpYVdGMElqb3hOemt4TkRRME5qY3hMQ0psZUhBaU9qRTRNakk1T0RBMk56RXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5OcWZ6cEU0d1lORzM3RHpzd3BPaHRmb2g2dXBzU0xURUxka3RTZHF5emRNIiwicCI6MjE5Mzg2NDkyLCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc5MTQ0NDY3MSwiZXhwIjoyMTA3MDIwNjcxLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.IGI7h9WvP5zwcBi6TTnjP9PCQ2soRAaBWozEAlytAok?
