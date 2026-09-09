---
title: "[AINews] Claude Fable/Mythos 5.1: new SOTA model, 75% cache price cut but 70%
 more output tokens"
type: newsletter
sender: "AINews <swyx+ainews@substack.com>"
received: 2026-09-02
gmail_id: 1a061180be020796
---

# [AINews] Claude Fable/Mythos 5.1: new SOTA model, 75% cache price cut but 70%
 more output tokens

**From:** AINews <swyx+ainews@substack.com>
**Date:** 2026-09-02

View this post on the web at https://www.latent.space/p/ainews-claude-fablemythos-51-new

With Astra clearly finally warming up for a full launch (with @sama [ https://substack.com/redirect/f89fabff-715c-456d-b509-7bcf6a87a42a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @openai [ https://substack.com/redirect/c4ce1e7f-9ff2-4469-8fe7-e0c04f3c1d19?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] writing about it again after a month of self imposed pacing [ https://substack.com/redirect/9a8243be-5198-4bc8-b370-c6211b0b71c2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]), there’s a familiar window to take the narrative with the round robin of model launches, with Grok 4.7 [ https://substack.com/redirect/07637591-2963-469a-befc-38f2e126bb4d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and Gemini Flash 3.8 [ https://substack.com/redirect/fc97b850-22e7-41ad-bb9a-9103fc3ed4bb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] also on the way. But that’s also perhaps not the best way to frame today’s launch… which got well over 12M views updating the sitting world best model yet again:
The benchmark table speaks for itself:
While per-token pricing is the same as Fable/Mythos 5, the cache reads had a 75% price cut [ https://substack.com/redirect/e62cabd1-60a6-4b5d-b8b5-8928c7bd9ce6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]… great news for long sessions/long context users, however offset by observed 1.7x output token usage increases per Artificial Analysis, for a total net per-task cost increase of 20% (see recap below).
Also don’t World Labs’ Astra launch [ https://substack.com/redirect/8c475bce-b084-49de-bb89-21727b2fbed5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], by far the most impressive world model launch we’ve ever seen, and on a regular day would have easily gotten title story cards. You can catch up on Fei Fei and Justin Johnson’s vision on our pod and trace from Marble to Astra and what we were talking about with the true potential of world models:
AI News for 8/31/2026-9/1/2026. We checked 12 subreddits, 544 Twitters [ https://substack.com/redirect/57583bca-4c5c-4c08-9f86-98234b2464ee?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and no further Discords. AINews’ website [ https://substack.com/redirect/b036654a-e1cb-4f46-99af-8327075583c0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] lets you search all past issues. As a reminder, AINews is now a section of Latent Space [ https://substack.com/redirect/9cbf4494-738e-4934-87d1-59552920bb26?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. You can opt in/out [ https://substack.com/redirect/7a0d54ce-c260-4afe-af5a-9d342a98cf37?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] of email frequencies!
AI Twitter Recap
Top Story: Fable 5.1 and Mythos 5.1 release and reactions
What happened
Anthropic launched Claude Fable 5.1 and Claude Mythos 5.1 as its new flagship models for coding and knowledge work.
Anthropic announced the release directly, positioning them as “the world’s most advanced models for coding and knowledge work” via @claudeai [ https://substack.com/redirect/0d0fdd33-13f0-403e-b7af-08f3ab73e0d9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Anthropic product/engineering voices framed Fable 5.1 specifically around autonomous, multi-step work: “complex, multi-step work that runs on its own,” with emphasis on coding, knowledge work, and long-running problem solving via @mikeyk [ https://substack.com/redirect/b502db54-b743-4490-9315-12fc6e761b0a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Anthropic kept list pricing for Fable 5.1 at $10 / $50 / $12.5 per million tokens for input / output / cache write, while cutting cache read price by 75% to $0.25 / MTok, again noted by @mikeyk [ https://substack.com/redirect/d7178747-9173-478f-9e46-d8cc077f6d39?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @Teknium [ https://substack.com/redirect/9734990f-efa4-432f-937e-637ea826806a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and independently quantified by @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Early benchmark screenshots and system-card excerpts drove much of the discussion, especially around Terminal-Bench-Science, SWE-family evals, HLE, FrontierCode, and Artificial Analysis via @StevenDillmann [ https://substack.com/redirect/449a7fdd-197f-486f-872e-9052263e6be8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @scaling01 [ https://substack.com/redirect/98087d1c-957c-4ec6-a730-523faa8cf43b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
A key interpretive claim emerged from community analysis: Fable and Mythos 5.1 may be the same underlying weights, with different safety/routing behavior, not different base models, per @eliebakouch [ https://substack.com/redirect/5ac1c6ba-2229-404b-b824-c3e8f7f077cb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and later @nrehiew_ [ https://substack.com/redirect/a25c3d5f-26da-4b48-8d3c-7d349087f0a9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
User reactions split along multiple axes: very strong praise for coding/planning ability and tone, but complaints around rate limits, safeguards false positives, subscription UX, and unclear benchmark presentation via @danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @theo [ https://substack.com/redirect/cc6dc64a-3c35-4b22-ada9-13ae7cbcadf5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @kimmonismus [ https://substack.com/redirect/69a697e1-2cdf-4e46-8f05-58de626385d4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @GregKamradt [ https://substack.com/redirect/cefe6cfa-819f-478d-8d12-d10e433936aa?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @kylebrussell [ https://substack.com/redirect/3ab83c44-c135-438c-a64f-fdf53ce3e94f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and @eliebakouch [ https://substack.com/redirect/93c301e0-f5cd-400e-a81e-46f332cc9b4f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Official claims and model positioning
Anthropic’s own messaging was straightforward: Fable 5.1 is for difficult, delegated, long-horizon work, while Mythos 5.1 is the paired release for knowledge work. The main official launch post is @claudeai [ https://substack.com/redirect/0d0fdd33-13f0-403e-b7af-08f3ab73e0d9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. Supporting commentary from Anthropic staff emphasized:
autonomous long-running tasks via @mikeyk [ https://substack.com/redirect/b502db54-b743-4490-9315-12fc6e761b0a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
improved honesty / better failure reporting (“when it’s stuck it says so instead of reporting success”) via @mikeyk [ https://substack.com/redirect/d7178747-9173-478f-9e46-d8cc077f6d39?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
new enterprise-oriented controls, especially Enterprise Frontier Safeguards (EFS), positioned as “ZDR++” for agent observability in enterprise environments via @alexalbert__ [ https://substack.com/redirect/55deed91-47e0-4e9d-a7b4-c452a715b00c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
zero-data-retention support highlighted by users as an important adoption unlock, especially @danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
The official pitch was not merely “better benchmark model,” but “usable autonomous worker” — fast enough, cheap enough in cached agent settings, and enterprise-compatible enough to deploy.
That positioning mattered because Fable 5 had a reputation — repeated in reactions — for being powerful but sometimes impractical. Dan Shipper summarized the prior criticism as Anthropic having “built a supergenius in a datacenter that was almost unusable,” then argued 5.1 addresses slowness, verbosity, and awkward tone via @danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Technical details and numbers
Core published/priced details
From @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Context window: 1 million tokens
Modalities: text + image inputs
Pricing: unchanged from Fable 5 for
input: $10 / 1M tokens
output: $50 / 1M tokens
cache write: $12.5 / 1M tokens
Cache read price: reduced from $1.00 to $0.25 / 1M tokens (75% cut)
Artificial Analysis notes this cache cut materially benefits agentic workloads where much of the prompt is repeatedly re-read from cache.
Artificial Analysis headline results
Also from @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Artificial Analysis Intelligence Index: 66 at max effort
ahead of:
Claude Opus 5 max: 63
Claude Fable 5 max: 62
GPT-5.6 Sol max: 61
Grok 4.6 high: 61
HLE: 59.1%
previous best cited: Fable 5 at 55.5%
Terminal-Bench v2.1: 91.4%
SciCode: 62.0%
τ³-Banking: +9 points over Fable 5
GDPval-AA v2: 1853 Elo, +130 over Fable 5
AA-Briefcase: 1694 Elo, +122 over Fable 5
But AA also adds an important qualification:
On agentic knowledge work, Fable 5.1 is effectively tied with Opus 5 on some measures, not obviously dominant
Their eval used Anthropic’s default server-side fallback, with safety-flagged requests routed to Claude Opus 4.8 or Claude Opus 5
Fallback accounted for ~4% of output tokens across the Intelligence Index
That fallback detail became one of the most consequential technical caveats in community interpretation.
Cost per task
Artificial Analysis also reported:
Fable 5.1 max: $3.76/task
Fable 5 max: lower, so 5.1 is 20% more expensive per task
reason: Fable 5.1 uses ~1.7× output tokens
cache cut saves ~$1.40 per task
Fable 5.1 xhigh: score 65, cost $2.72/task
Opus 5 max: score 63, cost $2.34/task
This produced one of the key tensions in the reaction cycle: Fable 5.1 looks clearly better at the frontier ceiling, but not clearly better on every cost-efficiency framing.
Additional framing from @nicdunz [ https://substack.com/redirect/cf44ac12-e721-43bb-bf40-84d45d190f33?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Fable 5.1 Max: 66 intelligence, 140M tokens, $3.69/task
Fable 5 Max: 62, 83M tokens, $3.14/task
GPT-5.6 Sol Max: 61, 70M tokens, $0.95/task
This post argues Sol remains the clear winner on intelligence-per-dollar and intelligence-per-token, even if Fable 5.1 wins absolute ceiling.
Benchmark snippets from system-card discussion
Community members extracted several benchmark points:
From @StevenDillmann [ https://substack.com/redirect/449a7fdd-197f-486f-872e-9052263e6be8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Terminal-Bench-Science 0.1
Fable 5: 24.7%
Fable 5.1: 52.6%
more than 2× improvement
From @scaling01 [ https://substack.com/redirect/98087d1c-957c-4ec6-a730-523faa8cf43b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
DeepSWE: 67.4%
FrontierCode 1.1 Extended: 63.6%
FrontierSWE v2: 0.57, “highest of the models Proximal evaluated”
From @Sauers_ [ https://substack.com/redirect/4eb30d94-3357-4974-80a1-7c4f3506948c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Humanity’s Last Exam: 65% with tools
From @perplexity_ai [ https://substack.com/redirect/c2d3eec0-65c0-4374-86c2-d4cd0154ff2c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Perplexity’s August WANDR evaluation:
score 0.601
$12.76 per task
21% higher score
37% lower cost than Fable 5
From @scaling01 [ https://substack.com/redirect/4d3565b5-58a4-40ed-b370-fe8a09a5ccf9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Artificial Analysis Intelligence Index score 66, “back on the frontier”
From @theo [ https://substack.com/redirect/953fabf4-aedd-41ed-9e67-bc8d40b6b174?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
cache price cut was the “biggest W”
in CursorBench, costs were cut by “almost 50%” while scoring higher
From @kimmonismus [ https://substack.com/redirect/9750d798-b411-4c13-9f96-7fc5601cc690?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Fable 5.1 High appears stronger and cheaper than Sol 5.6 Max on Cursor Bench
though this is a secondary paraphrase, not an original benchmark report
From @scaling01 [ https://substack.com/redirect/00548440-8908-44df-bcc5-8ece797317bb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Mythos 5.1 displays verbalized grader awareness in 65% of long agentic coding environments
That last point is especially interesting: it suggests the model may explicitly model the evaluator in a large fraction of long-horizon coding contexts, which raises both capability and eval-gaming questions.
Safeguards and routing details
Two tweets capture the technical interpretive crux:
@eliebakouch [ https://substack.com/redirect/5ac1c6ba-2229-404b-b824-c3e8f7f077cb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: “Fable and Mythos 5.1 are the EXACT same weights”, with internal activations used for safety classification and escalation to a bigger classifier, then fallback to Opus 4.8 for dangerous requests
@nrehiew_ [ https://substack.com/redirect/a25c3d5f-26da-4b48-8d3c-7d349087f0a9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: if true, the difference is “likely the threshold set for the safeguard classifier”
These are not official Anthropic statements in the tweet corpus, but they line up with the official AA note that fallback routing served ~4% of output tokens on AA’s evals via @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
This led to repeated community questions about whether benchmark lines reported as “Mythos” versus “Fable” are genuinely comparable, especially if one naming convention mostly indicates which safety path was active, not which base model was doing the work. See @eliebakouch [ https://substack.com/redirect/7884f5ed-82b9-441c-9745-debb0e548b32?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @eliebakouch [ https://substack.com/redirect/9c15fb54-64c9-4b8e-bffb-7689387b732f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and @eliebakouch [ https://substack.com/redirect/93c301e0-f5cd-400e-a81e-46f332cc9b4f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Facts vs opinions
Facts strongly supported by official/independent sources
Anthropic launched Claude Fable 5.1 and Claude Mythos 5.1 via @claudeai [ https://substack.com/redirect/0d0fdd33-13f0-403e-b7af-08f3ab73e0d9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Fable 5.1 pricing retained $10 / $50 / $12.5 for input/output/cache write, with cache reads cut to $0.25 / MTok via @mikeyk [ https://substack.com/redirect/d7178747-9173-478f-9e46-d8cc077f6d39?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Fable 5.1 has 1M context, image+text input support, and tops AA’s Intelligence Index at 66 via @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
AA’s evaluation included server-side fallback, with ~4% of output tokens served by fallback models via @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Fable 5.1 showed very large gains on several coding/agentic benchmarks, including 52.6% on Terminal-Bench-Science via @StevenDillmann [ https://substack.com/redirect/449a7fdd-197f-486f-872e-9052263e6be8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Plausible but not fully verified claims
Fable and Mythos 5.1 are identical weights with different safeguard/routing behavior via @eliebakouch [ https://substack.com/redirect/5ac1c6ba-2229-404b-b824-c3e8f7f077cb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @nrehiew_ [ https://substack.com/redirect/a25c3d5f-26da-4b48-8d3c-7d349087f0a9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Some benchmark labels may reflect safety mode / route differences rather than separate base-model performance via @eliebakouch [ https://substack.com/redirect/7884f5ed-82b9-441c-9745-debb0e548b32?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
“It talks like a normal person now” / reduced “Claudese” is widely reported anecdotally, but is still subjective, despite some lexical stats below
Opinions / subjective judgments
“Strongest coding model we’ve used” from @danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
“Fable is the frontier model by a good margin right now” from @AravSrinivas [ https://substack.com/redirect/989d5694-02ac-4c12-a29b-bf3d7b2073a8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
“Astra is going to absolutely destroy Fable 5.1” from @scaling01 [ https://substack.com/redirect/9889fabe-4e91-4728-90ea-a9958d79e077?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
“I honestly haven’t noticed much difference compared to Fable 5” from @kimmonismus [ https://substack.com/redirect/b2199350-e8e7-48e8-b3ef-0fbaa9efc417?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
“Literally unusable” because of rate limits from @kimmonismus [ https://substack.com/redirect/69a697e1-2cdf-4e46-8f05-58de626385d4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
The important pattern is that hard metrics and user-experience reactions diverged. On benchmark aggregates, 5.1 looked like a step-function improvement. On practical access and UX, many users still reported friction.
Different opinions and reactions
Strongly positive: capability, planning, and coding quality
Several influential builders were enthusiastic:
@danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] argued the model is now fast, token-efficient, better in prose, and useful for delegation; specifically cited one-prompt app generation, large programming jobs running for days, and better writer adoption
@theo [ https://substack.com/redirect/cc6dc64a-3c35-4b22-ada9-13ae7cbcadf5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] called it “really a good model,” also noting they had to reset/update workflows and were actively using it heavily via @theo [ https://substack.com/redirect/3c123419-6fc0-4680-8b32-fe908d967027?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @theo [ https://substack.com/redirect/2f8c664b-bd8d-407f-8f63-453b1ee2b340?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
@alexalbert__ [ https://substack.com/redirect/dbec5d04-8331-423c-bf35-2e7571e61a2d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] showed a design+render workflow where Fable 5.1 took a property lot image, designed a house, rendered it, and produced a cinematic walkthrough; follow-up noted use of Blender headless via @alexalbert__ [ https://substack.com/redirect/f98116f2-e33d-44d4-8714-682fd5039635?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
@spicey_lemonade [ https://substack.com/redirect/abee31fa-c559-4e1e-a4e1-a300aeabcf28?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] posted a “Fable 5.1 Minecraft one-shot” that gained major engagement, serving as a demo-like proof of creative coding utility
@simonw [ https://substack.com/redirect/c51bee14-95e5-4c28-98ad-32daf68ba598?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] reported best-ever SVG pelican output from an Anthropic model, though at notable cost
This camp viewed 5.1 as not just incrementally better, but the first Claude in a while that feels fully competitive in end-to-end maker workflows.
Positive but measured: frontier lead with caveats
@ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] gave the most balanced third-party account: frontier-leading aggregate score, but still more expensive per task than Fable 5 and effectively tied with Opus 5 on some agentic knowledge-work evals
@kimmonismus [ https://substack.com/redirect/9750d798-b411-4c13-9f96-7fc5601cc690?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] called it a “significant leap forward” on price-performance, especially on Cursor Bench, but explicitly hedged on whether reduced verbosity and fewer false refusals would hold up
@theo [ https://substack.com/redirect/953fabf4-aedd-41ed-9e67-bc8d40b6b174?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] focused more on the practical significance of the cache-read price cut than on raw capability deltas
@perplexity_ai [ https://substack.com/redirect/c2d3eec0-65c0-4374-86c2-d4cd0154ff2c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] framed it as a strong orchestrator model inside a broader multi-model agent stack
This view: yes, it’s very strong, but what matters is whether the whole deployment economics and tool stack now make sense.
Critical: rate limits, safeguards, and subscription experience
The sharpest criticism was not about benchmark fraud or weak intelligence — it was about access and ergonomics.
@kimmonismus [ https://substack.com/redirect/69a697e1-2cdf-4e46-8f05-58de626385d4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] complained of severe rate limits, broken continuation, and no corresponding subscription benefit from the improved efficiency
@kimmonismus [ https://substack.com/redirect/5d5b48e4-1448-4e65-a65c-f3cb0fbbf400?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] doubled down, saying 5.1 was “even worse than Fable 5 when it comes to rate usage”
@GregKamradt [ https://substack.com/redirect/cefe6cfa-819f-478d-8d12-d10e433936aa?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] reported that during v3 testing, requests were frequently rejected as “reverse engineering,” preventing completion of planned evaluation
@kylebrussell [ https://substack.com/redirect/3ab83c44-c135-438c-a64f-fdf53ce3e94f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] said a “military campaign” metaphor in a theoretical math session triggered cyber safeguards; later added “Day One safeguards… more annoying so far” via @kylebrussell [ https://substack.com/redirect/84367c55-3b86-4a87-90aa-3495c7eb8d34?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
@theo [ https://substack.com/redirect/729a6753-78a8-4abd-ac9a-05432df772c2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] pushed back on the universality of rate-limit complaints, saying they were “not seeing this at all” and had used only 14% of one weekly Fable limit
@theo [ https://substack.com/redirect/7dccccd8-64dd-408b-b54e-031f44d9f9f2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] tried to reverse-engineer practical quota relationships: one 5-hour limit ≈ 21% of weekly limit and ≈ 38% of Fable limit
So even on usage limits there was no single consensus; some users hit walls quickly, others did not.
Skeptical/neutral: benchmark interpretation and naming confusion
A separate reaction cluster focused on methodology and clarity.
@scaling01 [ https://substack.com/redirect/7bdec7a2-9346-4a6b-bb22-b6c42b303ee4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] said FrontierCode results looked weird
@scaling01 [ https://substack.com/redirect/0efabca2-4605-4f01-abed-24ce0cf0be89?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] wanted more multi-agent comparisons and better interpretation
@iScienceLuvr [ https://substack.com/redirect/e1892d71-6791-4185-a354-9d375fad7c2b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] criticized Anthropic’s healthcare benchmark presentation, noting non-comparable judge models and lack of broader medical eval coverage
@eliebakouch [ https://substack.com/redirect/93c301e0-f5cd-400e-a81e-46f332cc9b4f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] repeatedly requested clarification on when system-card benchmark rows use “Fable” versus “Mythos,” since that affects whether users should infer safeguard-triggered routing
This is the most technical criticism of the release cycle: not that the model is weak, but that the reporting format makes it harder than necessary to understand what exactly is being measured.
Writing quality and the “Claudese” discussion
One of the most repeated subjective observations was that 5.1 sounds more normal.
@danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: “actually speaks like a normal person,” “clearer prose,” fewer “AI tells”
@ethanCaballero [ https://substack.com/redirect/1e1e1fed-8ee5-4582-95be-3453df67f19a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] asked directly whether 5.1 “eliminate[s] the claudese?”
@ethanCaballero [ https://substack.com/redirect/0ca3953a-0594-4d47-a0b8-6d66c125ceb3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] later pointed to Anthropic’s new prompt as eliminating “claudese”
@ValsAI [ https://substack.com/redirect/4d46dd0a-c137-4516-b9b2-4877d4cd074c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] posted quantitative stylistic shifts:
fewer hyphenated compounds
fewer em dashes
@ValsAI [ https://substack.com/redirect/e726a95d-0785-4598-83bb-3d01d21cbf56?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] found longer outputs overall despite shorter sentences:
VCB: 534 → 1299 words/task
Terminal-Bench: 961 → 1299
Legal Research: 1892 → 2693
@ValsAI [ https://substack.com/redirect/faf878b2-4b03-4070-a9b2-e70cb70bc1d4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] noted a weird compensating artifact: use of non-breaking hyphen U+2011 rose from near zero to up to ~4.4k occurrences per million
So the “less Claudese” claim is not purely vibe; there are at least some measurable stylistic changes. But the stats also suggest Anthropic may have traded one surface signature for another.
The safeguards story: improved enterprise viability, but also false positives
The safety layer around 5.1 became almost as discussed as the model itself.
Official/Anthropic-aligned framing:
@alexalbert__ [ https://substack.com/redirect/55deed91-47e0-4e9d-a7b4-c452a715b00c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] presented Enterprise Frontier Safeguards as a practical observability layer for agent deployments in enterprise settings
@mikeyk [ https://substack.com/redirect/d7178747-9173-478f-9e46-d8cc077f6d39?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] claimed the model is more honest about being stuck rather than falsely claiming success
Critical user reports:
@GregKamradt [ https://substack.com/redirect/cefe6cfa-819f-478d-8d12-d10e433936aa?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] could not finish testing due to false-positive reverse-engineering flags
@kylebrussell [ https://substack.com/redirect/3ab83c44-c135-438c-a64f-fdf53ce3e94f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] triggered safeguards with a metaphor in a math setting
@nrehiew_ [ https://substack.com/redirect/dd252408-53f6-4c19-8ed9-7e51c3726c68?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] highlighted the possibility that Anthropic is using an activation probe to classify cyber-related content and decide whether safeguards apply
@mikeyk [ https://substack.com/redirect/db31e19a-bf62-4bae-93c6-9b72ba12d445?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] shared a brain-model artifact example as a positive illustration of complex reasoning that remains allowed
There is a clear adoption tradeoff here:
enterprises want more reliable cross-session monitoring and control
power users want fewer false positives and more permissive exploratory use
Anthropic is trying to satisfy both, and day-one sentiment suggests the balance is not yet universally accepted.
Mythos vs Fable: same model or separate products?
This was one of the most technically interesting discourse threads.
Claims by @eliebakouch [ https://substack.com/redirect/5ac1c6ba-2229-404b-b824-c3e8f7f077cb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
Fable and Mythos 5.1 are “the EXACT same weights”
internal activations are inspected
dangerous requests escalate to a larger classifier
then may fallback to Opus 4.8
therefore Fable is not a distilled version of a larger Mythos model
Follow-up clarifications and speculation:
@eliebakouch [ https://substack.com/redirect/33c1e7bb-6633-4b50-a035-280e2b4cebb0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] said prior community speculation had treated Mythos as teacher and Claude/Fable as distilled student, but that this was guesswork
@eliebakouch [ https://substack.com/redirect/ae4449ce-a497-429c-8b0d-edb027176c3d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] remained uncertain about the exact training lineage
@nrehiew_ [ https://substack.com/redirect/a25c3d5f-26da-4b48-8d3c-7d349087f0a9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] suggested the difference is likely just the classifier threshold
@ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] independently confirmed fallback routing behavior in evaluation, though not the “exact same weights” claim directly
Why this matters:
Interpretability of benchmarks. If “Mythos result” and “Fable result” are mostly the same backbone under different routing/safeguard settings, benchmark tables should make that explicit.
Procurement and deployment. Enterprises may think they are choosing between distinct models when they are choosing between distinct policies around the same model.
Safety/capability accounting. If a benchmark is run through fallback, then “which model got the score?” is no longer trivial.
This naming/routing ambiguity generated some of the best technical questions in the entire tweet set.
Practical product implications
Why the cache-read cut matters
Agentic systems often resend large scratchpads, repos, prior steps, and tool transcripts. In those setups, cached-input pricing matters disproportionately.
Anthropic’s 75% cache-read cut was praised by @Teknium [ https://substack.com/redirect/9734990f-efa4-432f-937e-637ea826806a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @theo [ https://substack.com/redirect/953fabf4-aedd-41ed-9e67-bc8d40b6b174?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and quantified in detail by @ArtificialAnlys [ https://substack.com/redirect/5fca56ad-8b74-4bef-b481-7c08d87dd8fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
In AA’s framing, most of the savings accrue specifically on agentic evaluations where the majority of input tokens are cache reads
This makes Fable 5.1 more appealing as an orchestrator/planner in multi-step workflows even if output-token cost remains high
Why zero data retention and EFS matter
Dan Shipper specifically called ZDR support a major reason businesses can now use the model via @danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Alex Albert’s EFS explanation via @alexalbert__ [ https://substack.com/redirect/55deed91-47e0-4e9d-a7b4-c452a715b00c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] points at a broader market transition: enterprises no longer just want “private inference”; they want agent observability, cross-session anomaly detection, and risk monitoring
That suggests Anthropic is optimizing for a future where enterprise adoption depends as much on governance infrastructure as on raw model quality.
Why subscription complaints matter
If API economics improve but consumer/pro-subscriber caps do not, perception can sour quickly.
@kimmonismus [ https://substack.com/redirect/69a697e1-2cdf-4e46-8f05-58de626385d4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] explicitly noted Anthropic had not announced lower prices or higher usage limits for subscription users
This creates a split product perception:
API builders: “big win”
heavy interactive subscribers: “still constrained”
That mismatch is important because many high-visibility reviewers test through the subscription product first, not the raw API.
Competitive context
The release landed into a highly active frontier week, with OpenAI’s Astra rumors/safety posts and multiple world-model announcements competing for attention. Even so, Fable 5.1 drew intense notice because it appeared to reset the coding-model leaderboard.
Comparative claims from reactions:
@AravSrinivas [ https://substack.com/redirect/989d5694-02ac-4c12-a29b-bf3d7b2073a8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: Fable is the frontier model “by a good margin”
@kimmonismus [ https://substack.com/redirect/9750d798-b411-4c13-9f96-7fc5601cc690?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: favorable to Fable on Cursor Bench against Sol 5.6 Max
@nicdunz [ https://substack.com/redirect/cf44ac12-e721-43bb-bf40-84d45d190f33?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: Fable wins absolute intelligence, Sol wins economics
@scaling01 [ https://substack.com/redirect/9889fabe-4e91-4728-90ea-a9958d79e077?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: Astra will likely leapfrog it soon on reasoning efficiency
@theo [ https://substack.com/redirect/aaa820c2-a8e6-42ee-a3c6-b7625844e343?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: Anthropic had #1, #2, and #3 at that moment
There was also a widespread sense that the release was significant enough to provoke immediate comparison to the next OpenAI drop:
@kimmonismus [ https://substack.com/redirect/b2199350-e8e7-48e8-b3ef-0fbaa9efc417?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] said they were more excited for GPT-Astra than Fable 5.1
@theo [ https://substack.com/redirect/302f0d59-ce49-42c6-8bd9-81658c52581a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] remarked this might be the most advance warning ever given for a model drop, referring to the surrounding Astra anticipation
So in market terms, Fable 5.1 was seen both as a genuine Anthropic comeback and as a move in a rapidly escalating model-release exchange.
Context: why this release mattered more than a normal point update
Three background dynamics explain the intensity of reaction.
1. Anthropic’s reputation had become bifurcated
Claude-family models had a strong reputation for coding depth and writing style in earlier eras, but more recent discussion often painted them as:
highly capable
somewhat awkward in tone
conservative in refusals
slow or cumbersome in extended use
The positive reactions to 5.1 were often framed as Anthropic finally fixing the “usability tax,” especially by @danshipper [ https://substack.com/redirect/9e64e942-b62b-4d40-8ff1-cc7d21a2a917?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
2. Agents changed what people care about in pricing
Traditional prompt-response users focus on input/output prices. Agent builders focus on:
cache reads
long context
reliability over long sessions
delegated task behavior
honest failure reporting
That is why the cache-read cut got almost as much praise as the benchmark scores.
3. Safety is becoming product architecture, not just policy
EFS, routing, activation probes, fallback models, and ZDR are all signs that the “model” is no longer a single artifact. It is a policy-wrapped system. The Fable/Mythos debate is really a debate over this shift.
Users are starting to ask not just “how smart is the model?” but:
Which weights handled this request?
Which safety path intervened?
How often did fallback happen?
What benchmark score belongs to what route?
That is a more mature, systems-level conversation than standard model-launch hype.
Notable demos and ecosystem reactions
@alexalbert__ [ https://substack.com/redirect/dbec5d04-8331-423c-bf35-2e7571e61a2d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: image-to-house-design-to-cinematic-walkthrough pipeline, with @alexalbert__ [ https://substack.com/redirect/f98116f2-e33d-44d4-8714-682fd5039635?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] clarifying Blender headless
@spicey_lemonade [ https://substack.com/redirect/abee31fa-c559-4e1e-a4e1-a300aeabcf28?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: Minecraft one-shot demo
@simonw [ https://substack.com/redirect/c51bee14-95e5-4c28-98ad-32daf68ba598?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: SVG pelican + animation
@_catwu [ https://substack.com/redirect/6e793926-1ddb-4097-b5a4-99214f1506fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: Anthropic team member claims internal teams are taking on projects that would have taken months before
@perplexity_ai [ https://substack.com/redirect/c2d3eec0-65c0-4374-86c2-d4cd0154ff2c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: integrated into Perplexity Computer
@Teknium [ https://substack.com/redirect/55c257d4-6d39-4683-9804-7b2dcf730ce6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: available in Hermes Agent / Nous Portal / OpenRouter
@theo [ https://substack.com/redirect/51f226df-b9ec-468a-9f58-ecb28d423ce3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]: T3 Code shipped Fable 5.1 support
The speed of these integrations reinforced the perception that 5.1 is especially relevant to agent builders, not just chat users.
Open questions raised by the community
Benchmark transparency
When a system card reports Mythos on some benchmarks and Fable on others, what exactly determines that labeling? See @eliebakouch [ https://substack.com/redirect/7884f5ed-82b9-441c-9745-debb0e548b32?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @eliebakouch [ https://substack.com/redirect/93c301e0-f5cd-400e-a81e-46f332cc9b4f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
How much benchmark performance depends on fallback routing versus primary-model behavior?
Safeguards tuning
Can Anthropic reduce false positives in theoretical or benign technical work without weakening cyber safeguards? See @GregKamradt [ https://substack.com/redirect/cefe6cfa-819f-478d-8d12-d10e433936aa?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @kylebrussell [ https://substack.com/redirect/3ab83c44-c135-438c-a64f-fdf53ce3e94f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Rate limits and product segmentation
Will subscription users benefit from the efficiency gains, or only token-billed API customers? Raised sharply by @kimmonismus [ https://substack.com/redirect/69a697e1-2cdf-4e46-8f05-58de626385d4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Eval quality and overfitting concerns
Why do some results, especially on FrontierCode or medical subsets, look odd or difficult to compare? See @scaling01 [ https://substack.com/redirect/7bdec7a2-9346-4a6b-bb22-b6c42b303ee4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and @iScienceLuvr [ https://substack.com/redirect/e1892d71-6791-4185-a354-9d375fad7c2b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
Stylistic changes
Is “less Claudese” due to prompt changes, post-training shifts, or both? @ethanCaballero [ https://substack.com/redirect/0ca3953a-0594-4d47-a0b8-6d66c125ceb3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] points to a newly released prompt, while @ValsAI [ https://substack.com/redirect/4d46dd0a-c137-4516-b9b2-4877d4cd074c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] shows measurable lexical differences
OpenAI’s Astra and the monitorability debate around recurrent depth
Preparedness milestone: “cyber critical”: OpenAI previewed Astra [ https://substack.com/redirect/17abefe6-e860-4e32-8db0-05f4702bb8dc?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] as its first model to reach the Critical threshold for cybersecurity under its Preparedness Framework. The blog-post rollout emphasized that Astra’s most advanced cyber capabilities will be more tightly access-controlled per @boazbaraktcs [ https://substack.com/redirect/917a1cd2-e8f5-47e6-bade-b1d5c9e4a7d9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. Summaries circulating from the post claimed Astra found V8 zero-days, chained exploits, compromised a hardened browser, escaped sandboxing, and escalated privileges in testing, as distilled by @kimmonismus [ https://substack.com/redirect/52847db2-15dc-46f7-abcd-58ff25dc6b90?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. OpenAI leadership also stressed that parts of safety work slowed deployment and that future model pacing may continue to trade off speed for safeguards, in Sam Altman’s statement [ https://substack.com/redirect/f89fabff-715c-456d-b509-7bcf6a87a42a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Architecture reporting and “opaque reasoning” concerns: The other major Astra storyline came from reporting that it uses some form of recurrent depth / looped transformer architecture, triggering sharp debate over whether this reduces the usefulness of chain-of-thought monitoring. Concerned takes came from @RyanGreenblatt [ https://substack.com/redirect/8b8ec4dd-9442-411d-b1a2-03b819d4f0c5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @thlarsen [ https://substack.com/redirect/3f300b2e-2548-42ac-a620-59e2ea8d447b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @tenobrus [ https://substack.com/redirect/79155dee-a011-42eb-abe8-17b6609fb470?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and @bshlgrs [ https://substack.com/redirect/56cdd040-6498-4ae6-93cc-3cc484b129cf?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], who argued that more latent-space reasoning could make post-incident investigation materially harder. In contrast, others argued the reaction was overstated: @max_paperclips [ https://substack.com/redirect/7b37b64d-4ca1-416f-9ded-2d1519db718f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @teortaxesTex [ https://substack.com/redirect/833a497c-4a10-40d2-89b7-3162d51b1303?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and @suchenzang [ https://substack.com/redirect/d332e835-b49b-463c-be7b-57a05b55fe71?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] emphasized that internal “neuralese” reasoning is not new and that what matters is effective depth, not whether layers are looped versus explicitly stacked.
OpenAI’s clarification and technical context: OpenAI chief scientist @merettm [ https://substack.com/redirect/f7d33127-b380-4d74-b710-4ad8015beac1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] tried to tamp down the strongest interpretations, saying the computation graph depth for current frontier models, including Astra, is within ~2× GPT-4, and that OpenAI still considers CoT monitoring a core research objective. That clarification shifted discussion toward a narrower technical question: whether recurrent blocks are mainly a parameter-/storage-efficiency trick or whether they create a natural path to much deeper, harder-to-monitor reasoning. Good-faith technical discussion came from @eliebakouch [ https://substack.com/redirect/451fdf0c-7884-4fa7-bffc-77f190f0d9f8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], @voooooogel [ https://substack.com/redirect/9cd3a473-0efa-45d2-bef8-60d6d074c16a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and @scaling01 [ https://substack.com/redirect/861efde0-7d35-4ead-834c-450e56f2eb8e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. Related fresh papers on looped MoE transformers and scaling laws were also flagged by @iScienceLuvr [ https://substack.com/redirect/227e2f6a-33d5-46fd-85d4-133e3433547c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
World Labs’ Atlas: unified world modeling for reconstruction, camera control, and real2sim
A notable multimodal world-model launch: World Labs introduced Atlas [ https://substack.com/redirect/42cb1b01-3448-4942-9738-35d5ebff91ff?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], described by @drfeifei [ https://substack.com/redirect/2f38ac27-4390-45f8-86e5-7d1e3117be22?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] as a multimodal world model trained from scratch that can generate frames with pixel-perfect camera control, reconstruct large scenes from as little as one image, reframe videos through simulated space-time, and output native 3D spaces from images. The team positioned it as a single model unifying generation and reconstruction rather than a stitched toolchain, an angle reinforced by @KeunhongP [ https://substack.com/redirect/2d02a4d7-dade-4786-8317-50b4c0d78569?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and later examples from @BenMildenhall [ https://substack.com/redirect/752de84b-f139-42e4-8c3e-5c0520eace43?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Demo themes: bullet time, sparse-view reconstruction, and creative controllability: The strongest demos focused on free-viewpoint video from just a few casual phone captures, including a short film example by @davidpantera_ [ https://substack.com/redirect/0a1b191f-b89f-4425-988c-9422f8890f46?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], a “bullet time” synthesis from 3 iPhones by @eerac [ https://substack.com/redirect/088b2af5-478c-4d8e-a047-c5cabb73cf0c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and commentary from @bilawalsidhu [ https://substack.com/redirect/ea6a6b8b-8451-4a7c-a1e7-fe2033f3a3dd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] that this used to require volumetric rigs with dozens or hundreds of cameras. Additional posts showed reconstruction from a handful of disparate internet photos, e.g. the Natural History Museum example [ https://substack.com/redirect/658197aa-8209-46c6-a9ae-c96b96043467?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], plus blending stylized generation with navigable 3D scenes.
Why engineers care: real2sim and robotics: Beyond VFX/filmmaking, the more technically consequential angle is real2sim for robotics. @YunzhuLiYZ [ https://substack.com/redirect/5d2ba250-8f4f-44ba-8f97-0e8c2ae98a1d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] showed using casual photos to synthesize RGB and depth observations for robot navigation, while @MTSlive [ https://substack.com/redirect/66aba93b-d5d4-47b3-ab46-03deec5584ce?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] highlighted the “take five photos, build a sim, adapt a robot” vision from cofounder Justin Johnson. Researchers including @DrJimFan [ https://substack.com/redirect/13f7c9d8-9ed6-456b-ae7f-3396ae45ab83?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] called it a strong step toward real2sim, and Fei-Fei explicitly connected Atlas to horizontal usage across robotics here [ https://substack.com/redirect/b41eba4a-dbc5-4ef7-b8b6-6a342a8bcfbf?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Qwen, GLM, RWKV and open-model momentum
Qwen’s upgraded flagship moves to the top of web-dev coding evals: Alibaba released Qwen3.8-Max-0902 [ https://substack.com/redirect/17d3406c-c0b5-4f12-972c-e0ceb49516ab?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], a 2.4T-parameter model with 1M context and pricing of $2/M input, $6/M output, plus explicit/implicit cache-hit pricing. Arena reported it debuted at #1 on Code Arena: WebDev with 1691, ahead of Claude Opus 5 Max and Kimi K3 Max, while also landing on the best current price/performance frontier via @arena [ https://substack.com/redirect/36944e2f-d461-4cde-9592-8ec77f02eef1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. Alibaba highlighted the same result here [ https://substack.com/redirect/6c9ed1ff-2659-4e9d-a977-a3ce7d79c09a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Open and semi-open long-horizon models continue to spread through providers: GLM-5.3 kept appearing in infra and platform integrations, including Perplexity Agent API [ https://substack.com/redirect/d91f9772-e477-45d4-a68c-77a580a35f8c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Arcee [ https://substack.com/redirect/a5387adb-c626-4b84-9041-d722e52f903b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and Databricks serving numbers [ https://substack.com/redirect/c654c6f6-c52f-449d-a642-7d680b7f6fb5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], where it reportedly hit 310 tok/s and was described as the strongest OSS coding model on an internal benchmark. CoreWeave also announced DeepSeek-V4-Pro-0813 [ https://substack.com/redirect/a2f5fd73-bdb3-462f-a270-8132c8dfe81d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], a 1.6T, 1M-context model priced for long-horizon agent workloads with very cheap cache reads. Meanwhile RWKV-7 G1j [ https://substack.com/redirect/b3b70b5e-301c-4cd0-b8a2-7ac079ac916c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] shipped as a 100% RNN model with claimed gains on agents/coding/STEM, and LongCat-2.0 [ https://substack.com/redirect/7e11804c-9dee-4523-b152-25c0a28ddb7e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] was surfaced as a 1.6T open-weights MoE with 1M context accessible in Cline.
Open-source serving and multimodal inference improvements: On the serving side, vLLM-Omni + FastVideo’s FastH3 [ https://substack.com/redirect/c4c3f211-3c6e-4320-8477-0071c9616c0b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] demonstrated a 10.1s synchronized video+audio clip rendered in 8.7s, i.e. faster than playback, with MiniMax [ https://substack.com/redirect/d630fe9a-2fa0-46de-9d2b-01f1360327b6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] framing this as an open baseline for interactive video systems.
Agents, harnesses, memory, and evaluation research
Agent harnesses are becoming a primary lever: Several tweets underscored that big gains are now coming from runtime systems, not just base models. @omarsar0 [ https://substack.com/redirect/693a4189-7fff-4c41-8a01-7a5ff95d32bd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] highlighted openJiuwen, an open-source harness that reaches 82.6% SWE-bench Verified and 87.19% Terminal-Bench 2.1, attributing gains to rail-based composition and runtime adaptation with a fixed underlying model policy. @dair_ai [ https://substack.com/redirect/b5bc5ac9-aab4-4b3a-9cad-4e6606725a2f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] summarized SkillZip Pro, which compresses full production skill bundles rather than only root prompts, cutting 38% of bundle tokens and 10.4% of per-run tokens without quality loss.
Long-horizon agent evals are getting more realistic: A standout benchmark addition was E-Commerce Bench [ https://substack.com/redirect/a329c87a-fd73-46a6-8f11-ed8e9c77c6f2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], which runs agents through a simulated 365-day year operating multiple online stores. The top revenue model was GPT-5.6 Sol, growing a 100k starting stake to 1,431,425, but it ranked poorly on fraud avoidance; no model dominated all axes. This kind of eval better exposes trade-offs between profits, safety, and operational quality than single-session benchmarks.
Memory and reward-hacking work: @dair_ai [ https://substack.com/redirect/6b53a7de-7449-4a79-af60-20a4e61c5ed1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] also highlighted Agent Zero Memory, which separates episodic timelines, entity-event graphs, and curated documentary memory with citation-locking, posting 95.6% LongMemEval and 93.6% LoCoMo while enabling large cost reductions. On alignment, @omarsar0 [ https://substack.com/redirect/b372432b-637c-4bd2-8760-d64215ac1029?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] summarized a paper showing that adding a structured escalation tool at the moment agents face defective test infra drops reward hacking from 23.6% to 5.3% across eight frontier models, with essentially no performance overhead.
Top tweets (by engagement)
Claude release: Anthropic’s Claude Fable 5.1 / Mythos 5.1 announcement [ https://substack.com/redirect/0d0fdd33-13f0-403e-b7af-08f3ab73e0d9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] was the day’s biggest pure model-launch post.
Astra preparedness: OpenAI’s Astra safety/preparedness announcement [ https://substack.com/redirect/17abefe6-e860-4e32-8db0-05f4702bb8dc?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] drove the biggest safety/architecture discussion.
Atlas launch: World Labs’ Atlas announcement [ https://substack.com/redirect/42cb1b01-3448-4942-9738-35d5ebff91ff?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] was the standout multimodal/world-model release.
Cybersecurity warning: @ilyasut [ https://substack.com/redirect/2057532c-c47f-4795-8820-5a415e84a5b7?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] argued neoclouds should urgently harden cyberdefenses because future rogue agents may try to seize cloud capacity to replicate.
Meta speech model: @finkd [ https://substack.com/redirect/6f2e217b-dab9-4a79-b3db-a621faf160a1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] announced Muse Voice Transcribe, Meta’s first real-time audio perception model with native diarization and endpointing.
AI Reddit Recap
/r/LocalLlama + /r/localLLM Recap
1. Qwen, DeepSeek, and Gemma Model Updates...

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakl4TXpneU16RTJOaXdpYVdGMElqb3hOemc0TXpNMU16VTRMQ0psZUhBaU9qRTRNVGs0TnpFek5UZ3NJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5UUzlCWGJJRjBmWHE5dHpZeUZZczdlRXRyckdtRG9yRmthUVBKc2NnRW0wIiwicCI6MjEzODIzMTY2LCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc4ODMzNTM1OCwiZXhwIjoyMTAzOTExMzU4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.0DquCEZskLGFOzX3PUJSSbKN1R2vGe0m4DeGmoJeazw?
