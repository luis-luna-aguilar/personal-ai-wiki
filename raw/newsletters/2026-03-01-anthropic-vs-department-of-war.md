---
title: "Anthropic vs Department of War"
type: newsletter
sender: "Vector Lab <news@velab.dev>"
received: 2026-03-01
gmail_id: 19cabbfaf2bc5034
---

# Anthropic vs Department of War

**From:** Vector Lab <news@velab.dev>
**Date:** 2026-03-01

You can read this online on the VectorLab site as well: [vectorlab.dev/news/weekly-2-23-to-3-1](https://vectorlab.dev/news/weekly-2-23-to-3-1)

# tl;dr

# News

## Anthropic VS DoW

Anthropic, along most of the major US AI labs, have had deals with the US government to deploy their AI models for use in different departments, including for classified use cases. 

After finding out one of their models (a fine tuned version of Sonnet 4.5) was [used to help capture Venezuelan president Nicolas Maduro](https://www.theguardian.com/technology/2026/feb/14/us-military-anthropic-ai-model-claude-venezuela-raid), Anthropic wanted assurances from the government that Claude was not being used for any use cases that Anthropic did not want it being used for; specifically, making autonomous weapons (the models are not good enough to do this yet) and mass surveillance of American citizens. 

In response, the Department of War (DoW) (previously the Department of Defense) said that they should be allowed "all lawful use", but Anthropic held firm in they demands. Because they [did not give in to the governments demands](https://x.com/AnthropicAI/status/2027150818575528261?s=20), Anthropic has now been labeled as a [supply chain risk](https://www.anthropic.com/news/statement-comments-secretary-war), which means that Claude cannot be used by the Department of War or for any DoW contracts.

After this happened, OpenAI signed a contract with the DoW themselves. [Sam Altman](https://x.com/sama/status/2027578652477821175?s=20) claimed that the same ideals that Anthropic had were upheld by OpenAI as well, and that the DoW agreed with these terms. This is contradicted by the [DoW UnderSecretary](https://x.com/undersecretaryf/status/2027594072811098230?s=46&t=SWUS-tT7iYax1OxtX4nxfA), who says that OpenAI gave them the "all lawful use" clause that they wanted, with "mutually agreed upon safety mechanisms", which Anthropic was also offered but turned down.

The situation is still developing as I write this, so I will reserve any opinions until everything that has and will happen is clear.

# Releases

## Nano Banana 2

Into more lighthearted news, Google has released a new version of their popular [Nano Banana](https://x.com/OfficialLoganK/status/2027054617616351282?s=20) image generation (and editing) model. 

_Nano Banana 2 is measurably better than its predecessor_ \-- data from [Artificial Analysis](https://x.com/ArtificialAnlys/status/2027052241019175148?s=20)

Not only is the quality measurably increased, it also has gotten cheaper and faster as well, as it is built on the (unreleased) Gemini 3.1 Flash model. Pricing has roughly halved to $0.15 per 4K image, and speeds are around 50% faster now as well. The model also now supports more extreme aspect ratios, like 4:1 and 8:1, allowing you to make some very wide (or tall) images.

_[Prompt](https://x.com/fofrAI/status/2027053842420920457?s=20): A photo of a monstera leaf against a simple backdrop, cleverly and organically appearing within the natural gaps of the leaf are the words Nano Banana_

_Enamel banasaurus pin_ \-- from [Twitter](https://x.com/NanoBanana/status/2027716950705521054?s=20)

## Qwen 3.5 Medium Models

Qwen started the release of their 3.5 series of models last week, releasing the largest model in the family, a 400 billion parameter model. It was not very interesting or notably good however, so we did not cover it. This week though, they released the [medium sized models](https://x.com/Alibaba_Qwen/status/2026339351530188939?s=20) in the family, and they are much more interesting. We have 3 new open source models, being Qwen3.5-35B-A3B, Qwen3.5-122B-A10B, Qwen3.5-27B, and a closed source model, which is Qwen3.5-Flash, which is the 35B model with longer context length and some built in tools.

For the model naming, the A3B and A10B means that the models are mixture of experts models, with 3 billion and 10 billion parameters respectively. This means that they will run as fast as a 3 (or 10) billion parameter model while having the intelligence of a 35 (or 122) billion parameter model (roughly).

The standout of these models is the 35B-A3B model. This size is fairly easy to run at home, if you have a Mac with at least 24GB of memory or a PC with a GPU and >24GB of CPU + GPU memory you can run it.

For its size, it is the best model out there right now, beating the likes of [GLM 4.7 Flash](https://vectorlab.dev/news/weekly-1-19-to-1-25/#glm-47-flash) and [NanBeige](https://vectorlab.dev/news/weekly-2-9-to-2-15/#nanobeige), and even outclassing models 5-10x larger like GPT-oss 120B and the old Qwen 3 flagship 235B model.

Normally, the Qwen models are text only models, and then the Qwen team makes a finetune of them a few months later to add in multimodal capabilities. This is not the case this time however, as all of the Qwen 3.5 models support image (and video) inputs.

The dense 27 billion parameter model seems even smarter, the issue is that because it is not a MoE model it is 5-10x slower to run, especially on compute constrained devices. It is noticeably better at difficult agentic applications, like coding.

If you like running local models and have decent hardware, I would highly recommend checking out some of these models. If you are not compute middle class, worry not, as Qwen should be releasing the small models in the next week or two.

# Finish

I hope you enjoyed the news this week. Thanks for reading. 

_Claude is a[silly guy](https://x.com/vmfunc/status/2026647932397556019?s=20)_

You received this email because you subscribed to the AI news from the Vector Engineering Lab. If you want to unsubscribe, use the link below.

[Unsubscribe](http://localhost:8000/unsubscribe/5802e140-518f-415e-859d-3c7e720fc5b8) from this list.
