---
title: "👀  Anthropic does it again"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-04-17
gmail_id: 19d9bbfeedde3d00
---

# 👀  Anthropic does it again

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-04-17

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** There's a new ceiling for agentic performance. Anthropic just dropped Opus 4.7 and it's also the stepping stone to Mythos, the more powerful model they're still keeping behind closed doors for safety reasons.

**Also:** How to build the right AI stack in 2026, six Claude Code team tips for mastering Opus 4.7 and find out why data from dead startups is now a goldmine for AI labs.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* How to pick agent patterns that actually scale

* How to cut your Gemini API bill in half

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c6920696-eed5-4d6f-a014-69b688a0ec46/CleanShot_2026-04-17_at_15.39.43_2x.jpg?t=1776421595)
Caption: Claude Opus 4.7 benchmark performance.


--------------------
**Anthropic unveils Claude Opus 4.7 with powerful new tools for devs:** The AI lab just dropped its latest **[flagship model](https://www.anthropic.com/news/claude-opus-4-7)**, designed to tackle complex engineering tasks with minimal oversight. Opus 4.7 is more rigorous with long-running workflows, follows instructions with more accuracy, and self-verifies its work before finishing. Vision capabilities also got a major upgrade, now supporting images at over three times the previous resolution.

**OpenAI arms devs with its most capable Codex upgrade:** The team behind ChatGPT just gave its **[coding agent](https://openai.com/index/codex-for-almost-everything/)** the ability to see, click, and type across your Mac, allowing multiple agents to run in parallel. A new in-app browser lets you leave comments directly on pages to streamline frontend development. This update also introduces image generation via gpt-image-1.5, persistent memory that remembers your preferences, and over 90 new plugins.

**Alibaba drops a lean open model for coding agents:** The Chinese tech giant released **[Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b)**, a mixture-of-experts model that packs 35B total parameters but only uses 3B for inference. Even with its small footprint, it outperforms the dense Qwen3.5-27B in coding and rivals Claude Sonnet 4.5 in multimodal tasks. You can find the weights on Hugging Face and ModelScope, and it integrates directly with Claude Code, OpenClaw, and Qwen Code.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY AI COUNCIL**

## [You're Invited: Join the world’s top engineers building AI systems (including the creator of ChatGPT)](https://aicouncil.com/sf-2026)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c0215de9-13e5-47eb-bafc-e6ba54bf6175/AI_COUNCIL_THE_CODE_AD_2__1___1_.png?t=1776411078)
Follow image link: (https://aicouncil.com/sf-2026)
Caption: 


--------------------
For 10+ years, [AI Council](https://aicouncil.com/sf-2026) has been gathering the world's top AI infrastructure minds to share what’s working (and where we’re headed next). 

[You’re invited for 3 days of high-quality discourse](https://aicouncil.com/sf-2026) with 1,200+ technical experts, including office hours, small groups, and zero marketing keynotes. 

**Speakers include:**

* The co-inventor of ChatGPT

* Creator of DuckDB and Codex

* Engineers behind ClickHouse, Databricks, Datadog, and LangChain

…and more. Takes place May 12-14 in San Francisco.

[See the full speaker lineup here](https://aicouncil.com/sf-2026) and **use code THECODE20 for 20% off.**


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **How to pick agent patterns that actually scale**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/77eac916-d04f-476c-9a25-a6632d641d6c/CleanShot_2026-04-15_at_17.04.58_2x__1_.jpg?t=1776400473)
Caption: 


--------------------
**The coordination gap.** As AI agents handle more complex tasks, the question has shifted from whether you should use them to how you should orchestrate them. Anthropic recently [published](https://claude.com/blog/multi-agent-coordination-patterns) a guide breaking down five coordination patterns (see image above), and the pick depends on one thing: how much your agents need each other.

**Sophistication backfires.** Many teams over-engineer their setups by choosing patterns based on complexity rather than fit. Anthropic's advice is to start with the simplest option that could work and only add complexity when it breaks. For most use cases, that means the first two patterns on the list (see image above).

**Proof is in the kernel.** Cursor and NVIDIA recently [showed](https://cursor.com/blog/multi-agent-kernels) what the right pattern choice looks like in practice. They pointed a multi-agent system at CUDA kernel optimizations for Blackwell GPUs, the kind of assembly-level tuning that normally takes specialized engineers months. A planner agent distributed and rebalanced work across autonomous workers, coordinated by a single markdown file. Three weeks later, the system delivered a 38% speedup.

**Before you build.** Ask whether your agents need each other's work while it's still in progress. If so, shared state. Otherwise, keep them independent. Anthropic's full [guide](https://claude.com/blog/multi-agent-coordination-patterns) walks through when to transition between patterns.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/576512ff-3179-4083-a0d9-e26f6b8aa064/CleanShot_2026-04-17_at_14.28.19_2x.jpg?t=1776416389)
Caption: Meme of the day.


--------------------
* **Opus Workflow:** The creator of Claude Code just dropped **[6 strategies](https://x.com/bcherny/status/2044847848035156457)** to help you get the most out of Opus 4.7 in Claude Code (1.1M views).

* **Builder's Guide:** A dev's **[2026 blueprint](https://x.com/Av1dlive/status/2044453102703841645)** makes the case that the winners won't build their own models, just the right stack around them.

* **Risk Flipped:** Shopify's CEO posted data on **[first-time founders](https://x.com/tobi/status/2044446135906119717)** that flips which career path is the safer bet right now.

* **Talent War:** Meta has snatched yet **[another founding engineer](https://x.com/CharlesRollet1/status/2044533757626228974)** from Mira Murati's Thinking Machines Lab. This time, the dev is behind their flagship product.

* **Context Mastery:** One of Anthropic’s Claude Code engineers **[broke down](https://x.com/trq212/status/2044548257058328723)** why our long Claude sessions are rotting our outputs.

* **Data Gold Rush:** AI labs are quietly **[paying](https://x.com/_IainMartin/status/2044758204773486925)** hundreds of thousands for the Slack archives, Jira tickets, and emails of dead startups.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to cut your Gemini API bill in half**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2e208927-4ec8-4946-a441-d659720ae9e2/CleanShot_2026-04-17_at_10.06.43_2x.jpg?t=1776400644)
Follow image link: (https://x.com/patloeber/status/2043986265691795564)
Caption: 


--------------------
API costs can really spiral when you're dealing with high-volume tasks. Google DevRel engineer Patrick Loeber recently [shared](https://x.com/patloeber/status/2043986265691795564) a simple, one-line fix that cuts Gemini pricing in half for any jobs that don't need an immediate response. 

Just add **service_tier: "flex"** to the config of any “generate_content” call:

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents="Analyze this dataset for trends...",
    config={"service_tier": "flex"},
)

print(response.text)
```
Flex cuts your Gemini costs by 50% by using Google’s spare capacity. You'll trade a 1 to 15 minute delay for massive savings, like `Flash-Lite` at just $0.125 per million input tokens. 

It's ideal for background tasks, batch jobs, or nightly data processing. Stick to the standard tier for real-time needs and offload everything else to Flex. Check the [full breakdown](https://ai.google.dev/gemini-api/docs/flex-inference) in the docs.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/14654f08-6441-4a43-837b-0976403fb14d/Untitled_design__52_.png?t=1776417688)
Follow image link: (https://www.youtube.com/watch?v=03CfGf9iw_U)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

**[How to use Hooks effectively in coding agents:](https://www.youtube.com/watch?v=03CfGf9iw_U)** This tutorial covers how to use hooks in AI coding agents like Copilot or Claude Code. You'll learn how to intercept the agent's lifecycle, inject custom context, and use pre-tool hooks to ensure the AI writes clean, linted code before any changes are saved.

———————————————————————————

### **Top Repo**

**[HyperFrames (by HeyGen):](https://github.com/heygen-com/hyperframes)** A new framework for generating AI videos straight from code. It allows AI agents to whip up high-quality MP4s using standard HTML, CSS, and JavaScript.

———————————————————————————

### **Trending Paper**

**[Designing synthetic datasets for the real world (by Google):](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)** Specialized AI struggles because real-world training data is often scarce, private, and expensive. Simula solves this by using reasoning models to systematically design entire synthetic datasets, proving that structured, high-quality data generation heavily outperforms simpler baselines.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 240K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/anthropic-unveils-claude-opus-4-7-openai-upgrades-codex-35cf
