---
title: "🖥️  Claude now controls your computer"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-03-24
gmail_id: 19d2029fdad79b16
---

# 🖥️  Claude now controls your computer

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-03-24

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Anthropic is on a hot run. They just dropped what's likely their biggest update of the year, with the launch video already reaching 37M views. Claude can now take over your entire Mac. It can open apps, browse the web, fill out spreadsheets, and click through workflows even when you are not at your desk.

**Also:** How to review PRs like OpenClaw's creator, get GPT-5.4 to build frontends that look well designed, and find out why Jensen Huang says we don't have AGI yet.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* How teams should adopt coding agents

* How to schedule cloud jobs in Claude Code

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6b5b933c-4d84-4ec9-837a-016ee1f37ffb/Untitled_design__25_.jpg?t=1774337025)
Follow image link: (https://x.com/claudeai/status/2036195789601374705)
Caption: Click here to see Claude remote computer use in action.


--------------------
**Anthropic gives Claude direct control of your Mac:** The AI lab recently released a research preview that allows Claude to [**take over**](https://x.com/claudeai/status/2036195789601374705) your desktop and complete tasks from start to finish. It can click, type, open apps, navigate browsers, and edit files. Before using screen control, it checks for secure integrations with apps like Slack and Calendar. This new feature works alongside Dispatch, letting users assign tasks from their phones and return later to find the work already completed.

**ChatGPT now saves your files across conversations:** The ChatGPT Maker just revealed [**Library**](https://x.com/OpenAI/status/2036183180219392103), a new built-in storage feature that automatically saves any documents, spreadsheets, or images you upload or create during a chat. You can find these files in a dedicated sidebar tab on the web version, making it easy to pull them into future conversations without having to re-upload anything. Even if you delete a chat, the associated files will remain saved until you manually remove them.

**Cursor makes AI agents 1,000x faster at searching code:** The coding startup recently launched [**Instant Grep**](https://cursor.com/blog/fast-regex-search), a client-side indexing system capable of searching millions of files in just 13 milliseconds. It works by creating a local index tied to Git commits, utilizing n-grams and Bloom filters to narrow down matches before scanning files directly. This represents a significant improvement over ripgrep, which takes nearly 17 seconds for the same query. These speed gains are especially helpful in large monorepos, where slow searches have been a major bottleneck for AI coding agents.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [Bad prompts = AI slop.](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b3269ffa-03b4-4cce-9010-9e92960811f9/Newsletters_Image_1920x1080__4_.png?t=1774344622)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
The bottleneck isn't the model. It's typing detailed context 50x a day.

Wispr Flow lets you [speak full prompts](https://ref.wisprflow.ai/thecode) into Cursor, Windsurf, or ChatGPT with syntax-aware dictation that respects camelCase, snake_case, and file names.

* Dictate specs, get better first-try output

* Auto-tags files when you mention them

* Works in VS Code, Linear, Slack, and anywhere you type

Fewer reprompts. More shipping. 

[**Try Wispr Flow Free**](https://ref.wisprflow.ai/thecode)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **How engineering teams should adopt coding agents**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/aefe23ec-a7c0-475a-a964-fc197a075941/superhumanteam_a_software_engineering_team_working_on_a_white_d6a71fd5-4e0c-46dd-9af4-55a7f6fcfaa2_1.jpg?t=1774343437)
Caption: Source: The Code, Superhuman


--------------------
**The line is getting clearer.** When Andrej Karpathy coined the term "vibe coding" in February 2025, it captured something real: prompting an LLM and simply accepting the output without much thought. But engineers building production software with AI didn't see themselves as vibe coders. 

Simon Willison, the co-creator of Django, recently published a [guide](https://simonwillison.net/guides/agentic-engineering-patterns/) that draws the distinction clearly. The moment you begin reviewing and auditing agent-generated code, you've crossed into what he calls agentic engineering.

**Pull requests are the first things to break.** Willison’s sharpest warning targets a growing [**anti-pattern**](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/) where engineers submit PRs full of agent-generated code they never actually checked. This shifts the burden of proof to reviewers. To make matters worse, agent-written descriptions often read well on the surface but fail to match what the code is actually doing.

**Experience still compounds if you capture it.** The guide argues that every working snippet, proof of concept, and old repository serves as high-quality fuel for agents. Instead of describing a solution from scratch, engineers can give an agent two existing examples and tell it to merge them. This [**process**](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/) compounds years of knowledge into a single prompt in a way a beginner simply cannot replicate.

**It is cheaper to produce, but not cheaper to maintain.** Willison’s core point ties the whole guide together. Agents lower the cost of writing code, but they do not lower the cost of maintaining bad code. Without updated review processes, technical debt grows with every commit. 

Ultimately, the cost shifts from the person who wrote the prompt to the team that inherits the repository. If your team is shipping agent-generated code without a clear workflow, Willison’s **[guide](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)** is the place to start.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18a90080-a5c3-45b1-87b2-5e210cc46b8b/CleanShot_2026-03-24_at_11.28.36_2x__1_.jpg?t=1774331979)
Caption: Meme of the day.


--------------------
* **Second Opinion:** OpenClaw's creator reviews every PR with AI. His **[workflow](https://x.com/steipete/status/2036252448399171717)** shows why most first fixes actually make your codebase worse, and what to do instead.

* **Card Grid Trap:** GPT-5.4 can build polished frontends, but most devs keep getting generic layouts because they're **[missing](https://x.com/emanueledpt/status/2035402224260550921)** three prompt constraints.

* **Loop Effect:** Karpathy's autoresearch loop has been live for two weeks. Devs are already applying it to [**everything**](https://x.com/zhengyaojiang/status/2035385189719765261) — one team hit 53% faster on Shopify's template engine.

* **Jensen Unplugged:** Lex Fridman just [**dropped**](https://x.com/lexfridman/status/2036123301140111406) a 2.5-hour sit-down with NVIDIA's Jensen Huang on what he thinks is actually blocking AGI right now.

* **Vibe to Deploy:** A Google engineer broke down how to go from a single prompt to a [**deployed app**](https://x.com/_philschmid/status/2036089128899510568) with a database entirely inside AI Studio.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to schedule cloud jobs in Claude Code**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4166c74b-b739-4d4c-af3a-ad0ea8493a61/CleanShot_2026-03-24_at_10.39.48_2x.jpg?t=1774329023)
Follow image link: (https://x.com/noahzweben/status/2036129220959805859)
Caption: Source: X/noahzweben


--------------------
Claude Code's scheduled tasks used to have a frustrating catch: they only worked if your computer stayed awake. If you closed your laptop, the job would just fail to run.

Anthropic's Claude Code PM, Noah Zweben, [shared](https://x.com/noahzweben/status/2036129220959805859) a newly released fix for this. The “/schedule” command now lets you set up cloud-based recurring tasks directly from your terminal. 

Just type “/schedule” followed by what you need:

```
/schedule a daily job that looks at all PRs shipped since yesterday and update our docs based on the changes. Use the Slack MCP to message #docs-update with the changes
```
Claude sets the frequency and gives you a trigger URL. Since the job runs in the cloud, it stays on schedule even if your laptop is closed. Any connected MCP servers like Slack or GitHub work seamlessly within the scheduled prompt. 


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e835426e-a55d-4de9-ade4-8bd85da6d273/Untitled_design__26_.jpg?t=1774346450)
Follow image link: (https://www.youtube.com/watch?v=diy3kmUl8mY)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How Microsoft's AI VP automates everything:**](https://www.youtube.com/watch?v=diy3kmUl8mY)** **This tutorial shows devs how Microsoft’s AI VP uses the AI terminal Warp to automate tedious daily tasks using ad-hoc micro-agents. You'll learn to manage Azure cloud resources via the command line, process files with FFmpeg, and use custom rules and conversational prompts to streamline your workflow.

———————————————————————————

### **Top Repo**

[**MiniMax Skills:**](https://x.com/MiniMax_AI/status/2035609361826111780) This repo contains development skills for AI coding agents. By installing them, you provide structured guidance to tools like Cursor, Claude Code, Codex, and OpenCode, allowing them to stop guessing and start delivering production-quality results. 

———————————————————————————

### **Trending Paper**

[**Hyperagents:**](https://x.com/jennyzhangzt/status/2036099935083618487) Current AI stalls because its self-improvement rules are permanently fixed by humans. "Hyperagents" solve this by merging task-solving and self-editing, allowing the AI to continuously upgrade how it learns across any task.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/anthropic-s-claude-gains-mac-control-cursor-makes-ai-agents-1-000x-faster
