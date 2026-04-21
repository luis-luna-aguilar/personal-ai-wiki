---
title: "Opus 4.7 is a Flop"
type: newsletter
sender: "Vector Lab <news@velab.dev>"
received: 2026-04-21
gmail_id: 19dadf50867d813d
---

# Opus 4.7 is a Flop

**From:** Vector Lab <news@velab.dev>
**Date:** 2026-04-21

Sorry for the delay, forgot to send out the email yesterday.

You can read this online on the VectorLab site as well: [vectorlab.dev/news/weekly-4-13-to-4-19](https://vectorlab.dev/news/weekly-4-13-to-4-19)

# tl;dr

  * Opus 4.7 is not the upgrade we expected 
  * Qwen releases an open source model worthy of OpenClaw



# Releases

## Opus 4.7

Only a week after announcing the existence of [Mythos](https://vectorlab.dev/news/weekly-4-6-to-4-12/) Anthropic has released [Opus 4.7](https://x.com/claudeai/status/2044785261393977612?s=20).

_New benchmarking chart meta: show your new public model beating all the other labs' models, but still losing to your internal "actually good" model_

The consensus for Opus 4.7 is not as clear as previous releases. Usually a new model release is clearly better than its predecessors; this is the case for pretty much every lab (except [Mistral](https://vectorlab.dev/news/weekly-3-16-to-3-22/#mistral-4-small)). But for Opus 4.7 I have been seeing mixed opinions so far. 

It seems to lack the level of refinement of previous Claude models. Its personality and soul are lacking, and it capabilities within Claude Code, while still good, are a bit shaky, with [multiple people](https://x.com/theo/status/2044912111827161384?s=20) (including myself) running into a higher than normal number of tool call failures.

For coding the model does seem smarter, but also more unreliable, from [Chubby](https://x.com/kimmonismus/status/2045063637639762056?s=20) on Twitter: 

> Opus 4.7 feels like a disgruntled employee whose results you can't judge and have to check afterward. The trust you had with 4.6 is gone. It's like hiring a new employee who had excellent grades in their application but is totally sloppy and disgruntled in practice and doesn't follow instructions. 

This seems to be due to the new adaptive thinking mode that the model uses. This allows the model to think more or less for a given query based on how hard it thinks it is. The GPT series of models has had this for a while and it has worked very well, but Anthropic seemed to have missed the mark with their implementation of it. Opus 4.7 [only considers coding or STEM related tasks](https://x.com/MParakhin/status/2044991136087826660?s=20) to be hard enough for more thinking, causing to reason less and give worse answers for almost every other domain.

For OpenAI, their adaptive thinking was for a better user experience, since users prefer faster answers. Anthropic on the other hand, being far more compute constrained than OpenAI is right now, are using adaptive thinking to save compute. From a [HackerNews poster](https://news.ycombinator.com/item?id=47803639): 

> [Adaptive thinking is] a solved problem for the companies. It solves their problems. Not yours ;)

To add insult to injury, Anthropic also updated the tokenizer for the model, which makes it use more tokens than normal, causing it to be [20-50% more expensive](https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you) than Opus 4.6 for the same number of characters.

For most people, Opus 4.7 is a sidegrade at most, trading off raw intelligence and capability for reliability. For most other use cases it seems to be a bit of a downgrade, so I would not recommend using it at this time unless it performs noticeably better for your own use cases.

## Qwen 3.6 35B

Less than 2 months after the Qwen 3.5 releases, we now have our first open source Qwen 3.6 model, an update to the [35B-A3B mixture of experts](https://x.com/Alibaba_Qwen/status/2044768734234243427?s=20) model.

The Qwen 3.5 and Gemma 4 dense models (the 27B and 31B models in the chart above) were considered to be the first models that were good enough to be used in coding harnesses and agent interfaces like OpenClaw. This Qwen 3.6 model is able to handily beat both of its dense counterparts, while being far more efficient, making it runnable at decent speeds (>20 tokens per second) on pretty much any hardware with at least 24GB of memory.

In terms of its benchmark scores, it's around the Sonnet 4.5 level, which is insane since it is at least one order of magnitude smaller than Sonnet, which was released only 5 months ago. If this trend continues, that means that we will have a Opus 4.6/GPT 5.4 level model that we can run at home fairly easily in 6 months.

I have been personally using this model with [Hermes Agent](https://github.com/nousresearch/hermes-agent) (a OpenClaw alternative that is a bit friendlier for open source models) and it has worked fairly well with no major issues. I have seen similar sentiment from those on [LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) who have been using it as a personal agent and also as a fairly competent coding assistant.

As I said for the Qwen3.5 and Gemma 4 models, now is the best time to start using local LLMs, because they are starting to get good enough to replace OpenAI and Anthropic for easy and medium difficulty tasks. 

# Finish

I hope you enjoyed the news this week. Thanks for reading. 

[ ▶️ Click to watch video https://vectorlab.dev/2026-4-18/OEHnAtntoxEe1maV.mp4 ](https://vectorlab.dev/2026-4-18/OEHnAtntoxEe1maV.mp4)

_Midjourney 8.1 and Seedance 2.0_ made by [Jerrod Lew](https://x.com/jerrod_lew/status/2044403126791266602?s=20) on Twitter

You received this email because you subscribed to the AI news from the Vector Engineering Lab. If you want to unsubscribe, use the link below.

[Unsubscribe](http://localhost:8000/unsubscribe/5802e140-518f-415e-859d-3c7e720fc5b8) from this list.
