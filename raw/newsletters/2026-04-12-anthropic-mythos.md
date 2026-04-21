---
title: "Anthropic Mythos"
type: newsletter
sender: "Vector Lab <news@velab.dev>"
received: 2026-04-12
gmail_id: 19d822d043801e06
---

# Anthropic Mythos

**From:** Vector Lab <news@velab.dev>
**Date:** 2026-04-12

You can read this online on the VectorLab site as well: [vectorlab.dev/news/weekly-4-6-to-4-12](https://vectorlab.dev/news/weekly-4-6-to-4-12)

# tl;dr

  * How mythical in Anthropic Mythos?
  * Is Meta back in the LLM game?
  * GLM 5.1 take the spot as the top Chinese model



# Releases

## Anthropic Mythos

A few weeks ago there were leaks about a model from Anthropic that is larger than Opus that crushes benchmarks. This week those rumors were made real, as Anthropic announced the existence of [Claude Mythos](https://x.com/alexalbert__/status/2041579938537775160?s=20).

The model is not actually being released, as Anthropic has deemed its [hacking capabilities](https://x.com/Simeon_Cps/status/2041596830450852118?s=20) to be too strong for the general public to potentially use. 

It was able to find hundreds of bugs across many major open source projects that have been audited, tested, and actively used for years (e.g. Linux, FFMPEG, OpenBSD). If the model were to be used by nefarious hackers, Anthropic feels that it would tilt the playing field too much in favor of attackers.

Even if the model is not being actively used in a negative way, it may go and [take negative actions itself](https://x.com/Jack_W_Lindsey/status/2041588505701388648?s=20) to be able to accomplish its task. Anthropic is calling this their model aligned model, yet in their [technical report](https://www-cdn.anthropic.com/3edfc1a7f947aa81841cf88305cb513f184c36ae.pdf), they talk about how the model will act [reckless](https://x.com/elliotarledge/status/2041602563423051812?s=20) and hide information from the user.

The model will try and hide the fact that it saw the answer to a benchmark question (so that it looked like it solved it by itself instead), it can break out of its own sandbox and email people, steal credentials to be able to finish tasks, and trying to hide its reasoning to fool evaluators.

Their report is much more in depth than previous models, and they seem to be taking the safety side of things [much more seriously](http://localhost:4321/news/weekly-2-2-to-2-8/#opus-46) now. They highlight in their report the lack of frontier benchmarks that are not saturated by the model, making it hard to determine its capabilities while its training. Most of the issues that they highlighted in the report did not come from the direct safety testing but instead an internal rollout.

There has been some debate online about how strong its hacking capabilities are, and if Anthropic is just trying to spook people or if they are actually real. Having read a few takes online and talking with a few friends in the field (I am not a cybersecurity person myself) it seems that it is not a fluke and these are real vulnerabilities that it is finding. 

I don't think this is a model that will ever be released (at least not for a while) given its immense capabilities. Even if they did, it is reportedly 5x more expensive than Opus, which is already one of the most expensive models to use, which would make it prohibitively expensive for the average person to use.

We are now entering into the middle game for AI, where the top models are deemed too powerful to be released, concentrating power to those that have access to them. This will be interesting to see how it plays out in the future.

## Meta Muse Spark

Meta has returned after a year since the ill-fated Llama 4 release, with their [Muse Spark](https://x.com/alexandr_wang/status/2041909376508985381?s=20) multimodal LLM.

_Don't let the blue numbers distract you, the model is only the best in[3 of the benchmarks](https://x.com/vikhyatk/status/2042131804174639452?s=20) (CharXiv, HealthBench, and DeepSearchQA)_

The preliminary results that I have seen for the model have been decent. It is definitely not a benchmaxxed model, but does still struggle in a few areas when compared to Anthropic and OpenAI.

Looking at the breakdown of the [Artificial Analysis](https://x.com/ArtificialAnlys/status/2041913043379220801?s=20) results, the model does well for general use cases, but struggles in agentic tasks and even more so in coding when compared to other frontier models.

Right now the model has only been made available to a few 3rd parties (like Artificial Analysis) to benchmark, and also on the Meta AI app for consumers. Once API support gets added we will see what the 3rd party benchmarks say.

The model will be closed source it appears, so gone are the days of Meta being a leader in the open source space. This is good to see more competition from a big lab, as Gemini and Grok have been falling behind Anthropic and OpenAI quite a bit lately. The Meta Super Intelligence team was able to make this model in only 9 months, so I look forward to see what they end up making once they have more time to cook.

## GLM 5.1

Z.ai has officially [released an update](https://x.com/Zai_org/status/2041550153354519022?s=20) to their [GLM 5](https://vectorlab.dev/news/weekly-2-9-to-2-15/#glm-5) model. They soft launched it a few weeks ago on their coding plan, but have officially open sourced it and released benchmarks for it this week.

The model is a straight upgrade from the previous version, being better at prompt understanding, large scale agentic coding sessions, and frontend design. For frontend specifically is tied for the top of the [Design Arena](https://x.com/Designarena/status/2041550551855595622?s=20) with Claude.

In my personal coding use, I use GPT for backend, DB, and research work, while I use Claude for planning and frontend. Now with GLM 5.1, I am moving my frontend tasks to it, and it still continues to be my go to for small, easy tasks, given its low price and high rate limits with their [coding plan](https://z.ai/subscribe).

The model (like most Chinese models) is overfit a bit on more general benchmarks, but for coding it is definitely as good as the benchmarks entail. Because of this, I am moving it up to be the first non OpenAI or Anthropic model in the second tier for my coding model tier list.

**Frontier models**

  * GPT 5.4 
  * GPT 5.3 Codex
  * Opus 4.6



**Second tier**

  * Sonnet 4.6
  * GPT 5.2
  * Opus 4.5
  * GLM 5.1



**Third tier**

  * Minimax M2.7
  * GLM 5
  * Kimi K2.5



# Finish

I hope you enjoyed the news this week. Thanks for reading. 

_Artemis II photos_ from [NASA](https://x.com/NASA/status/2041557036274475228?s=20)

You received this email because you subscribed to the AI news from the Vector Engineering Lab. If you want to unsubscribe, use the link below.

[Unsubscribe](http://localhost:8000/unsubscribe/5802e140-518f-415e-859d-3c7e720fc5b8) from this list.
