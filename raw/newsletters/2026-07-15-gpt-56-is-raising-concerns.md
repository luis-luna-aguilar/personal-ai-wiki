---
title: "🚨  GPT-5.6 is raising concerns"
type: newsletter
sender: "The Code <superhumancode@news.codenewsletter.ai>"
received: 2026-07-15
gmail_id: 19f65e0968902203
---

# 🚨  GPT-5.6 is raising concerns

**From:** The Code <superhumancode@news.codenewsletter.ai>
**Date:** 2026-07-15

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/15ce5d17-c4a8-42a3-8ba1-ba8488836954/Group_CUBE__4_.jpg?t=1784069631)
Follow image link: (https://cube.dev/?utm_source=thecode&utm_medium=newsletter&utm_campaign=cube-general-promotion&utm_content=v4-brex)
Caption: 

----------
**Welcome back.** For two years, devs have been hitting “Allow” every time their agent has asked for access. This almost became a default but not anymore. Reports say OpenAI's GPT-5.6 Sol wiped an entire production database mid-task, without warning. And this might not be the only case.

**Also:** Former Google’s AI Director launches an Agentic Engineering course, how to use Fable 5 in Codex, and choosing the right model for agentic coding.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6b6b7778-393c-42c9-8f9f-eaf993110eed/superhumanteam_generate_a_portrait_image_of_the_person_in_omn_9833339d-8eff-407f-9491-0f17fe9ef088_2__1_.jpg?t=1784100118)
Caption: Made with Midjourney.


--------------------
**OpenAI's new coding model reportedly deletes files without permission:** The ChatGPT maker's GPT-5.6 Sol is facing [backlash](https://x.com/mattshumer_/status/2075657271401390161) from developers who claim it wiped production databases and entire Mac filesystems on its own. The company’s system card [**flagged**](https://deploymentsafety.openai.com/gpt-5-6-preview/gpt-5-6-preview.pdf) the risk, noting Sol is more likely than GPT-5.5 to exceed user intent and may even misreport its actions afterward. For now, strict permission scoping and regular backups are the only real safeguards.

**PrismML ships the first 27B-class model that runs on a phone:** The California-based startup just dropped [Bonsai 27B](https://prismml.com/news/bonsai-27b), a compressed version of Alibaba's Qwen 3.6 27B. By storing each weight as a single bit, PrismML cut the model from 54GB to just 3.9GB. The company says it’s small enough to fit on an iPhone 17 Pro while keeping 90% of its performance. A developer preview API is [available now](https://www.together.ai/models/prism-ml-ternary-bonsai-27b).

**AI agents are making developers rethink client SDKs: **An article by a senior engineer at Factory AI is forcing developers to [rethink](https://x.com/i/trending/2077206578701205747) client SDKs. After his team dropped packages from Stripe, WorkOS, and Slack, they now use a single in-house wrapper for direct REST calls. The reason is simple: SDKs hide raw headers that are vital for debugging, and they also bloat your code. For example, Stripe's SDK is 6.5MB. Linear's is 34MB. The Google APIs package is a massive 198MB. 


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY CUBE. DEV**

## [Can you actually trust your company's AI?](https://cube.dev/?utm_source=thecode&utm_medium=newsletter&utm_campaign=cube-general-promotion&utm_content=v4-brex)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0762e2dd-4eeb-42c5-9f7a-bb30dccca569/ChatGPT_Image_Jul_15__2026__04_04_56_AM.jpg?t=1784070359)
Follow image link: (https://cube.dev/?utm_source=thecode&utm_medium=newsletter&utm_campaign=cube-general-promotion&utm_content=v4-brex)
Caption: 


--------------------
Most teams don't. AI pulls the wrong data, mixes up metrics, and answers with confidence anyway.

Cube grounds AI in [one trusted set of business definitions](https://cube.dev/?utm_source=thecode&utm_medium=newsletter&utm_campaign=cube-general-promotion&utm_content=v4-brex), so every answer comes back correct. That's how Brex built an [AI analyst for 35,000+ customers](https://cube.dev/?utm_source=thecode&utm_medium=newsletter&utm_campaign=cube-general-promotion&utm_content=v4-brex), lifting accuracy from 55% to nearly 90%.

* Trusted by 400+ enterprises like Wix and Patagonia

* One source of truth for every AI answer

* Dashboards built by AI or drag-and-drop

Try** **[**Cube here**](https://cube.dev/?utm_source=thecode&utm_medium=newsletter&utm_campaign=cube-general-promotion&utm_content=v4-brex)[.](https://cube.dev/?utm_source=thecode&utm_medium=newsletter&utm_campaign=cube-general-promotion&utm_content=v4-brex)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **How do you write good agent skills? Now there's real data**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/10aadd8e-d28b-4066-9925-bbb88f588018/superhumanteam_a_software_engineering_team_working_on_writing_ed7cf3b3-30cd-4ebb-9d58-e6c812e78655_1.jpg?t=1784099044)
Caption: Source: The Code, Superhuman


--------------------
**Guesswork gets graded.** Skills are folders of instructions that teach a coding agent how your team works. Anthropic and GitHub both ship official libraries, and most teams are writing their own. Until recently, there was no way to measure whether these skills worked. Now, according to Arize AI co-founder Aparna Dhinakaran, three recent [papers](https://x.com/aparnadhinak/status/2074569427346174039) have finally quantified their impact by benchmarking identical tasks with and without these skills.

**Handwritten beats generated.** The lead paper, [SkillsBench](https://arxiv.org/abs/2602.12670), tested the shortcut that every team tries first. It asked the model to write its skills. Three findings stood out:

1. Self-written skills scored lower on average than using no skills at all. So the knowledge has to come from a human.

2. Short skills beat detailed ones. Two or three focused modules outperformed exhaustive documentation, which sank below the baseline. 

3. Loading every skill you have makes things worse too. A [second paper](https://arxiv.org/abs/2606.32025) found a few relevant skills beat the full library and cost fewer tokens.

**Polish hides the damage.** You won't spot any of these issues by looking at the results. Responses with skills enabled look more professional, even when they fail more often. 16 out of 84 SkillsBench tasks performed worse with skills turned on. The only way to catch the drop is a direct head-to-head comparison.

**Run the comparison yourself.** That head-to-head test is now public. The SkillsBench [harness](https://github.com/benchflow-ai/skillsbench) is open source, so you can run those same scores on your skills. Anthropic's guide walks you through the entire [skill authoring process](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), from writing effective trigger descriptions to setting up the evaluation loop that validates every update.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/574927f5-a990-4a88-a441-399ae3853c51/CleanShot_2026-07-15_at_12.46.18_2x.jpg?t=1784099840)
Caption: Meme of the day.


--------------------
* **AI-Native Engineering:** Former Google’s AI Director dropped a course on **[agentic engineering](https://www.linkedin.com/learning/instructors/addy-osmani)** on LinkedIn.

* **Codex-Orchestration:** This senior engineer shared an [open-source plugin](https://x.com/cjzafir/status/2076347110417678502) that lets you bring models like Claude Fable 5 into Codex and let it coordinate the work.

* **The Fifth Principle:** A former Google senior engineer shares [5 principles](https://www.youtube.com/watch?v=wQ46lax_ya0) that separate engineers who level up with AI from those who stay stuck at the same level.

* **Model Math:** An AI research engineer charted which GPT-5.6 tiers are worth the cost for [agentic coding](https://x.com/rasbt/status/2075573860796436626) (1M views).

* **Outer Loop:** Trying to ship fast with AI agents? This senior engineer says you're losing something in [the trade-off](https://www.linkedin.com/posts/addyosmani_ai-programming-softwareengineering-share-7481188577452638208-HsQh/), and you won't notice until a bug forces you to.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f5c1365a-5222-4966-9d6e-86dc35c4b48c/Thumbnail__53_.jpg?t=1784084588)
Follow image link: (https://www.youtube.com/watch?v=0xKE1UHpSfk)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to use OpenCode (by an ex-Microsoft engineer):**](https://www.youtube.com/watch?v=0xKE1UHpSfk) OpenCode is an open-source alternative to Claude Code. It’s a flexible AI coding agent that runs in your terminal. In this tutorial, you’ll learn to connect different language models, scaffold apps, install custom skills, and write system prompts in OpenCode.

———————————————————————————

### **Top Tool**

[**BugShot:**](https://bug-shot.com) A Chrome extension that lets you pick elements, tweak styles, and report bugs to Jira or GitHub. It bundles screenshots, video, and logs into one quick report.  

———————————————————————————

### **Top Repo**

[**Codesight**](https://github.com/Houseofmvps/codesight)** (1.2K ⭐):** This repo generates a compact context map of your project in one command. It helps AI assistants understand your entire codebase instantly without wasting tokens on file exploration.

———————————————————————————

### **Trending Cookbook**

[**40 tips for using Claude Code efficiently:**](https://agent-cookbook.com/tutorial/claude-code-40-best-practices) Most engineers treat Claude Code like basic autocomplete rather than optimizing its environment. With the right setup and automation, you can turn it into an operating system that runs your entire workflow.  


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to ship a PR from Claude Code in one command**

Shipping changes with Claude Code used to be a stop-and-go process. You had to stop for every commit, push, PR, and approval. 

The latest release finally fixes this issue. The new “/commit-push-pr” [command](https://x.com/dani_avila7/status/2076089527655915538) now auto-allows pushes beyond origin.

```
# inside Claude Code
/plugin install commit-commands@claude-code-plugins
/reload-plugins

# when your change is ready
/commit-push-pr
```
This command handles everything for you: it stages your changes, writes a commit message based on the diff, pushes the branch, and opens a PR complete with a summary and test plan.

P.S. Get 50+ AI coding hacks for Claude Code, Cursor, and Codex [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN CASE YOU MISSED IT**


--------------------
### ==**Our most-clicked story from yesterday**==

Installing every Claude Code plugin actually backfires. Once you go past 50 tools, Claude starts picking the wrong ones. Here are [7 plugins](https://www.youtube.com/watch?v=uuUo7gWuH9w) worth keeping.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 300K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/gpt-5-6-sol-deletes-user-files-unprompted-prismml-ships-bonsai-27b
