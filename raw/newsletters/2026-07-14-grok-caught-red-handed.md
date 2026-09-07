---
title: "🚨  Grok caught red-handed"
type: newsletter
sender: "The Code <superhumancode@news.codenewsletter.ai>"
received: 2026-07-14
gmail_id: 19f60ae3fa3ffa11
---

# 🚨  Grok caught red-handed

**From:** The Code <superhumancode@news.codenewsletter.ai>
**Date:** 2026-07-14

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/482d81ec-34ff-4230-9ed6-051916d90d83/Group_Wispr__4_.jpg?t=1783970636)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 

----------
**Welcome back.** Your codebase should never leave your machine without your permission. A security researcher found that Grok's CLI might have been quietly leaking your codebase on a large scale. In today’s issue, we break down what the evidence shows and what you need to do if you have used it. 

**Also:** How to survive a code review you can't explain, developer’s guide to reducing costs on Fable 5, and Microsoft CEO explains the hidden AI cost.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/63851087-137e-4049-a7f2-f925e9fdd40f/superhumanteam_generate_a_portrait_image_of_the_person_in_omn_8682cbaa-418f-47b2-9242-7da59d1c217e_1.jpg?t=1784018897)
Caption: Made with Midjourney.


--------------------
**xAI's coding agent secretly uploaded entire Git repos to Google Cloud:** A security researcher just [published](https://www.internationalcyberdigest.com/xais-grok-build-cli-uploads-entire-git-repositories-to-a-google-cloud-bucket/) compelling proof that the Grok Build CLI was quietly uploading entire repositories, including unredacted .env secrets, regardless of which files the agent actually needed. Even turning off the data collection toggle didn't stop it. A hidden server-side update eventually stopped the uploads. Elon Musk has since promised the collected data will be "completely and utterly deleted." We suggest engineers to [rotate your keys.](https://glitchwire.com/news/xais-grok-build-cli-was-uploading-entire-repositories-to-google-cloud-the-compan/#:~:text=What%20This%20Means%20for%20Developers)

**Anthropic reveals Claude's personality shifts with model and language:** The AI lab analyzed over 300K real conversations and found that its assistant expresses different values based on the model and language you use. Opus 4.7 is more cautious and flags potential risks, while Sonnet 4.6 is friendlier and likes to joke around. Claude also tends to be warmest when speaking Hindi and Arabic but turns more rigorous and critical in English and Russian. [See the findings.](https://www.anthropic.com/research/claude-values-models-languages)

**Apple turns Siri into a real AI assistant**: The iPhone maker just released the [public betas](https://www.engadget.com/2214198/public-betas-for-ios-27-macos-27-and-more-apple-platforms-are-now-available/) for iOS 27, macOS 27 Golden Gate, and watchOS 27. The standout feature is a completely redesigned Siri that can handle natural conversations, understand what's on your screen, and take multi-step actions within apps. According to Apple, apps now launch up to 30% faster and AirDrop transfers run up to 80% quicker.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [The code writes itself. Everything around it doesn't.](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4da13d6a-90f0-4aa3-8d4a-187a56d25fcc/image__21___1_.jpg?t=1783970917)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
You spend hours on things that aren't code. PR descriptions. Slack threads explaining why you made that architecture call. Linear tickets with enough context so your teammate doesn't ping you at 11pm. Docs you keep pushing to next sprint.

[**Wispr Flow**](https://ref.wisprflow.ai/thecode) handles all of it. Speak naturally, and it outputs clean text anywhere you type. Syntax-aware, so your variable names and file paths stay intact.

It won't write your code. But it'll clear out everything blocking you from writing it. [**Works across Mac, Windows, iPhone, and Android.**](https://ref.wisprflow.ai/thecode)

Teams at Vercel, Clay, and Rivian already use it daily.

[**Free to start**](https://ref.wisprflow.ai/thecode)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Washington and Beijing just reached for the same AI kill switch - here's what you should know**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5237fb2c-5824-44df-9f49-e1aec9dfe6d2/superhumanteam_a_software_engineering_team_working_on_their_l_6e9cc63b-ee22-4e16-b570-a5220587c6a9_1.jpg?t=1784010369)
Caption: Source: The Code, Superhuman


--------------------
**The open-weights showdown.** Washington is working to keep Chinese AI models out of U.S. companies. Anthropic is leading the charge. They've accused Chinese labs of [copying](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) Claude's capabilities at an industrial scale. Now, China is pushing back. On July 10, Alibaba reportedly [banned](https://www.reuters.com/world/china/alibaba-ban-claude-code-workplace-over-alleged-backdoor-risks-source-says-2026-07-03/) its staff from using Claude Code, calling it high-risk software. Shortly after, Z.ai founder Tang Jie [published](https://thenextweb.com/news/zhipu-tang-jie-frontier-ai-open-to-all) a memo. He argued that advanced AI should stay open and accessible to everyone. On the surface, it looks like a simple clash of philosophies.

**Beijing breaks the script.** The timing tells a different story. Tang published his memo just days after Reuters reported that Beijing is considering restrictions on overseas access to China's top open-source models. The very person advocating for openness might find his government shutting it down first. If you strip away the political talk, both capitals are trying to pull the same lever. They both want to control who leads in frontier intelligence.

**The lever already moved.** In June, the Commerce Department [terminated](https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon) Anthropic's Fable 5 for foreign nationals. The termination happened just three days after it dropped. That is the risk you take with closed models. Open weights have their set of problems. No one can take back weights you have already downloaded. But the supply of future updates can dry up at any time. Either way, every model you use now depends on the mood of a government.

**Portability beats allegiance.** You can't vote on those politics, but you can build a way around them. Engineering teams using a gateway can swap models with a simple configuration change. Multi-provider adoption has jumped from 23% to 40% of organizations in just a year, so this hedge is quickly becoming the standard. This guide [breaks down](https://www.deepinspect.ai/blog/llm-routing-strategies) five routing patterns and shows you which one fits your needs.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY DROPBOX**

## [Why don’t more AI tools actually understand you?](https://open.spotify.com/show/0jqN4dww5LJniqTnUFNaS2)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4c40e92e-9438-4682-92b8-f5624eba0037/youtube_artwork-1920x1080-title__1_.jpg?t=1783971051)
Follow image link: (https://open.spotify.com/show/0jqN4dww5LJniqTnUFNaS2)
Caption: 


--------------------
Modern work can be frustrating and chaotic—if you don’t have the right tools. 

[The Working Smarter podcast](https://open.spotify.com/show/0jqN4dww5LJniqTnUFNaS2) takes you behind the scenes at Dropbox where engineers are building AI that works wherever you do. Hear all about context engineering, multimodal search, and agentic AI.

[**Start listening now.**](https://open.spotify.com/show/0jqN4dww5LJniqTnUFNaS2)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/93ed042b-4214-4af1-a3f6-3f22ecd5c8dd/CleanShot_2026-07-14_at_11.43.24_2x.jpg?t=1784009678)
Caption: Meme of the day.


--------------------
* **Cost Cutting:** Fable 5 costs 2x more per token than Opus 4.8, yet a senior engineer found Fable-led agents are [cheaper to run](https://x.com/joon_h_lee/status/2076714221837173097) (446K views).

* **Plugin Overload:** Installing every Claude Code plugin actually backfires. Once you go past 50 tools, Claude starts picking the wrong ones. Here are [**7 plugins**](https://www.youtube.com/watch?v=uuUo7gWuH9w) worth keeping.

* **Grilled:** Are you stuck defending code you don't fully understand in a review? A senior engineer revealed a [**6-step workflow**](https://x.com/mattpocockuk/status/2076373232295587865) for exactly that moment (132K views).

* **Hidden Trade:** Microsoft CEO argues companies using AI are giving away something [more valuable](https://x.com/satyanadella/status/2076323181154230284) than money, and most haven't noticed (11M views).

* **From Scratch:** What happens between typing a prompt and getting a response? One developer built his own LLM to [**find out**](https://www.youtube.com/watch?v=YmLp8qe87A0) and shared all the code.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a9508819-0f68-409d-ac91-c4d171f9c0cf/Black_and_Green_Modern_Finance_Business_Report_Presentation__14_.jpg?t=1784028631)
Follow image link: (https://www.youtube.com/watch?v=QPT4qqoze2U)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to run agentic AI fully local:**](https://www.youtube.com/watch?v=QPT4qqoze2U) You'll learn how to build and run local AI agents using harnesses like Turnstone and Hermes. You'll also set up multi-model systems, use the Model Context Protocol to automate tasks, and create autonomous loops that solve problems entirely on your own hardware.

———————————————————————————

### **Top Tool**

[**Kiro:**](https://kiro.dev/) An agentic IDE from AWS that converts prompts into spec files for the agent to execute, complete with built-in hooks for automated checks.  

———————————————————————————

### **Top Repo**

[**Codex-lb**](https://github.com/Soju06/codex-lb)** (2.3K **⭐**):** A load balancer and proxy for Codex and ChatGPT that features multi-account support, usage tracking, a dashboard, and OpenCode-compatible endpoints.  

———————————————————————————

### **Trending Research**

[**Proactive memory agent for long-horizon agents**](https://arxiv.org/abs/2607.08716)[** (by Meta AI):**](https://arxiv.org/abs/2607.08716) AI agents often fail with long tasks because they lose track of previous instructions and errors. Adding a separate memory agent that actively decides when to step in and remind the main agent significantly boosts task success.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to clean up a bloated Claude Code setup**

Every installed MCP, skill, and plugin consumes context during each turn, regardless of whether you are actively using them. Boris Cherny, the creator and head of Claude Code at Anthropic, shared a [**command**](https://x.com/bcherny/status/2074997570317779038) that cleans everything up at once. 

Make sure to update first, because the “/checkup” command was released in version 2.1.205. Just use the command “claude update”, then run it inside any session.  

```
/checkup
```
It cleans up unused skills and plugins while organizing your CLAUDE.md file. It also disables slow hooks and pre-approves common read-only commands to save you time. You'll get to review and confirm every change before it's applied.  

P.S. Get 50+ AI coding hacks for Claude Code, Cursor, and Codex [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN CASE YOU MISSED IT**


--------------------
### ==**Our most-clicked story from yesterday**==

This GitHub repo contains a massive library of [ready-to-use setups](https://github.com/davila7/claude-code-templates) to automate your coding and integrate external tools directly into your CLI workflow.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 300K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/grok-cli-leaked-full-git-repos-to-google-cloud-apple-drops-ios-27
