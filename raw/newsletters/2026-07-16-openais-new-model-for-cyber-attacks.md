---
title: "🚀  OpenAI's new model for cyber attacks"
type: newsletter
sender: "The Code <superhumancode@news.codenewsletter.ai>"
received: 2026-07-16
gmail_id: 19f6b09223b714be
---

# 🚀  OpenAI's new model for cyber attacks

**From:** The Code <superhumancode@news.codenewsletter.ai>
**Date:** 2026-07-16

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/06212e9f-0d9d-4102-ba48-68fa5a836eb0/Group_Nylas.jpg?t=1784161284)
Follow image link: (https://www.nylas.com/products/agent-accounts/?utm_source=&utm_medium=sponsoredemail&utm_campaign=Superhuman-kevin-chan-accounts-jul-16&utm_content=)
Caption: 

----------
**Welcome back.** Former OpenAI CTO Mira Murati spent 18 months building in stealth. Now, her AI lab has dropped their first open-weights model. It’s already beating several major competitors on both coding and agentic tasks.

**Also:** How to build a self-improving code review agent, the four major tasks left in an engineer's job, and the Codex lead's response to GPT-5.6 wiping files.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c5de1636-e6f3-48c6-9a7a-908ad8e934e3/0011111_1.jpg?t=1784193139)
Follow image link: (https://x.com/thinkymachines/status/2077454609551921208)
Caption: Click here to see Thinking Machines’ Inkling full benchmarks.


--------------------
**Thinking Machines unveils its first open-weights model:** The Mira Murati-led startup just released [**Inkling**](https://thinkingmachines.ai/news/introducing-inkling/), a 975B-parameter model that reasons across text, images, and audio. Devs can download the full weights and fine-tune them on Tinker, the lab's customization platform. The team claims Inkling matches Nvidia's Nemotron 3 Ultra on coding while using one-third of the tokens. See how to [run it locally.](https://unsloth.ai/docs/models/inkling)

**OpenAI's new model to train against cyber attacks:** The ChatGPT maker just unveiled [GPT-Red](https://openai.com/index/unlocking-self-improvement-gpt-red/), a model that can craft prompt injection attacks. These attacks are hidden in emails, webpages, and tool outputs. This capability allows engineers to surface vulnerabilities and patch holes before a model ships. OpenAI says GPT-5.6 was trained against GPT-Red's attacks and now falls for just 0.05% of them.

**SpaceXAI open-sources its coding agent after a security scare:** The AI lab led by Elon Musk landed in hot water when devs caught Grok Build uploading entire directories, including SSH keys, to the company’s servers. They have since disabled the feature and released the full [source code](https://github.com/xai-org/grok-build) on GitHub. Devs can now audit all 844,530 lines of Rust, run the agent locally, and expand its capabilities using plugins and subagents.  


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY NYLAS**

## ==[Provision an agent inbox from your terminal.](https://www.nylas.com/products/agent-accounts/?utm_source=&utm_medium=sponsoredemail&utm_campaign=Superhuman-kevin-chan-accounts-jul-16&utm_content=)==


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/00076ce7-62ae-45d6-ac9c-bd4d33216438/The_Code_Nylas_KevinChan_-_Allen_Warner.jpg?t=1784161435)
Follow image link: (https://www.nylas.com/products/agent-accounts/?utm_source=&utm_medium=sponsoredemail&utm_campaign=Superhuman-kevin-chan-accounts-jul-16&utm_content=)
Caption: 


--------------------
Kevin Chan is one builder replacing 20+ SaaS tools for one long-term client. He provisions email identities per project with [Nylas Agent Accounts](https://www.nylas.com/products/agent-accounts/?utm_source=&utm_medium=sponsoredemail&utm_campaign=Superhuman-kevin-chan-accounts-jul-16&utm_content=). One API call, no Google Workspace tenant. Auth survives turnover, inbound email arrives as a webhook, and email plus calendar live under one identity.

[**Provision an agent inbox →**](https://www.nylas.com/products/agent-accounts/?utm_source=&utm_medium=sponsoredemail&utm_campaign=Superhuman-kevin-chan-accounts-jul-16&utm_content=)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **The engineering behind Bun's 11-day Rust rewrite**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9eeb4450-d260-47d6-904f-53fdaa544182/superhumanteam_a_software_engineering_team_working_on_two_ide_0f831db4-02b5-478a-87f3-505b261fe57a_3.jpg?t=1784192386)
Caption: Source: The Code, Superhuman


--------------------
**It started with crashes.** Back in May, Jarred Sumner went viral. He’s the creator of Bun and an MTS at Anthropic. He ported Bun from Zig to Rust in just 11 days. He did the port using a pre-release version of Fable 5. The reason was simple: Bun mixes Zig's manual memory management with JavaScriptCore's garbage collector. This caused constant crashes. Last week, Sumner finally shared his full report on the [process](https://bun.com/blog/bun-in-rust).  

**The playbook reads simple.** Sumner gave Claude strict instructions. The agents wrote Rust that mirrored the Zig architecture file by file. All features were frozen during this time. Bun's TypeScript tests bind to the public interface, so they survived the swap and graded the port from the outside. Most teams have tests that die with the language they are replacing. That one fact decides who can copy the code.  

**Assume the code is wrong.** Every change passed through two [adversarial reviewers](https://bun.com/blog/bun-in-rust#adversarial-review). These were fresh Claude sessions that only saw the diff. They hunted for reasons why it might fail. One prompt rule carried a lot of weight. If a workaround needs a paragraph-long comment to justify it, the code is wrong. Sumner trialed all of these methods on three files before he touched the full codebase.  

**Now do the math.** The run cost about $165,000 in tokens. That sounds like a lot until you look at the other options. Sumner thinks a manual rewrite would take a small team an entire year. No one would ever sign off on that. Anthropic's [best-practices guide](https://code.claude.com/docs/en/best-practices) shows a small version of Sumner's playbook.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY SUPERBLOCKS**

## [Your teams are vibe coding. But are you secure from AI cyber attacks?](https://www.superblocks.com/book-today?utm_source=thecode&utm_medium=newsletter&utm_content=spotlight)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/91478fb4-ab2a-4308-9805-9e2cbeafaf95/2__1___1_.jpg?t=1784161931)
Follow image link: (https://www.superblocks.com/book-today?utm_source=thecode&utm_medium=newsletter&utm_content=spotlight)
Caption: 


--------------------
Recently, a vibe-coded app leaked 1.5M API keys because nobody reviewed the code. 

Your team ships AI-written code every day. [Superblocks keeps it governed](https://www.superblocks.com/book-today?utm_source=thecode&utm_medium=newsletter&utm_content=spotlight):

* Security agents scan every app before it ships

* Secrets stay in a managed vault, never in the code

* Runs in your own AWS account, with SSO and audit logs on every build

[**Book a demo.**](https://www.superblocks.com/book-today?utm_source=thecode&utm_medium=newsletter&utm_content=spotlight)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4e463d85-ad5f-47de-8030-08a7fbde8c22/CleanShot_2026-07-16_at_13.19.33_2x.jpg?t=1784188246)
Caption: Meme of the day.


--------------------
* **Harness Lessons:** Coding agents fail because of context rot and poor tool use. One engineer rebuilt Claude Code's [**architecture**](https://x.com/akshay_pachaar/status/2077455755066868098) to find out what makes it so good (1.1K bookmarks).

* **Review Loop:** Warp's founder built a code review agent that gets smarter with every PR. This [**guide**](https://x.com/zachlloydtweets/status/2077428025474355521) shows you how to run one on your repo.

* **Codex Overhaul:** OpenAI just merged Codex into ChatGPT. This [video explains](https://www.youtube.com/watch?v=eiQgljOrkWU) everything developers get in the update.

* **Four Tasks:** After the launch of Fable 5, a senior engineer's job has boiled down to just four tasks. Here's what he [**actually does now**](https://x.com/Steve_Yegge/status/2077475727327604932) (1.6K likes).

* **Highest Leverage:** The creator of Claude Code says an old-school engineering habit just became the [highest-leverage skill](https://x.com/bcherny/status/2077460395279692197) in the agent era (1M views).

* **Deleted Files:** GPT-5.6 has been wiping users' files, sometimes entire home directories. OpenAI's Codex lead breaks down why and [the fixes](https://x.com/thsottiaux/status/2077630111499882637) that are coming (4.1K likes).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/82bd35f3-bada-4d12-bcd7-af48afecb358/Thumbnail__55_.jpg?t=1784173299)
Follow image link: (https://www.deeplearning.ai/courses/fast-llm-inference-with-cerebras)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**Build LLM apps that respond in real time (by DeepLearning.AI):**](https://www.deeplearning.ai/courses/fast-llm-inference-with-cerebras) You’ll learn how to build ultra-responsive AI apps on Cerebras's high-speed inference hardware. This tutorial shows you how to kill loading screens, power real-time tools like live translation, and speed up complex AI agent workflows with instant code generation feedback.  

———————————————————————————

### **Top Tool**

[**ccshare:**](https://getccshare.vercel.app) This tool lets you share your live Claude Code session using a simple six-digit code. Your teammates can jump in right from their browser or terminal. 

———————————————————————————

### **Top Repo**

[**Awesome LLM Apps**](https://github.com/Shubhamsaboo/awesome-llm-apps)** (by a Google Product Manager):** A collection of over 100 ready-to-run AI apps, featuring agents, agent skills, and RAG apps.  

———————————————————————————

### **Trending Research**

[**On effective model routing (by Google DeepMind):**](https://arxiv.org/abs/2607.09197) Most routing systems focus on accuracy and cost, but they often miss whether agents are actually different or if the routing stays steady when inputs change slightly. This study shows that a few well-chosen agents cover most of the variety needed, and prompted routers are more stable than KNN methods.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to stop burning your Codex rate limits**

Codex runs every task with your default model and reasoning. This means a simple rename costs as much as a full refactor. Instead of re-typing flags, use [config profiles](https://learn.chatgpt.com/docs/config-file/config-advanced#:~:text=Configuration%20Reference.-,Profiles,-Profiles%20let%20you). Just create a "~/.codex/fast.config.toml" file for secondary settings and load it with a single flag.

```
model = "gpt-5.4-mini"
model_reasoning_effort = "low"
```
Run "codex --profile fast" to keep your main config set for deep work. Since version 0.134, profiles use their own files. The old blocks in config.toml are gone, so move your settings there if they stopped working.  

P.S. Get 50+ AI coding hacks for Claude Code, Cursor, and Codex [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN CASE YOU MISSED IT**


--------------------
### ==**Our most-clicked story from yesterday**==

Google's former AI Director just dropped a new course on agentic engineering over on LinkedIn. [Check it out.](https://www.linkedin.com/learning/instructors/addy-osmani)


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 300K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/thinking-machines-drops-inkling-spacexai-open-sources-grok-build
