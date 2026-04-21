---
title: "👀  MiniMax drops open weight coding model"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-04-13
gmail_id: 19d872584de841c3
---

# 👀  MiniMax drops open weight coding model

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-04-13

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Three weeks ago, China-based MiniMax claimed they built a coding model that trains itself. Now that it is making rounds on X, they just dropped M2.7 as an open-weight model on Hugging Face. Coincidence? You can test it and decide for yourself.

**Also:** How an ex-Oracle director tests code with agents, 18 Cursor tips from their engineer, and an Atlassian engineer explains how to crack a Staff Engineer interview.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Why training your own LLM is still so hard

* How to pull live git data into Claude Code

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7d4e8ea5-feea-481d-8b3d-ffcec9f90e62/CleanShot_2026-04-13_at_15.14.53_2x.jpg?t=1776073518)
Follow image link: (https://x.com/MiniMax_AI/status/2043132047397659000)
Caption: See how MiniMax M2.7 compares with frontier models.


--------------------
**MiniMax opens up its coding agent model and ships a new CLI:** MiniMax just released M2.7 as an [open-weight download](https://x.com/MiniMax_AI/status/2043132047397659000) on Hugging Face, allowing teams to run the 230-billion-parameter model locally on 128GB RAM setups. It holds its own against top closed models on engineering benchmarks like SWE-Pro (56.22%) and Terminal Bench 2 (57.0%). Along with the model, they launched [MMX-CLI](https://x.com/MiniMax_AI/status/2042641521653256234), a command-line tool that gives agents native access to image, video, voice, and search capabilities without needing any MCP setup. [Try it here.](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)

**Developers highlight sharp decline in Claude Code quality:** Anthropic is facing backlash after AMD's senior director of AI [**published**](https://github.com/anthropics/claude-code/issues/42796) metrics from nearly 7,000 coding sessions. The report shows Claude Code's reasoning length dropped by 67%, while API requests have spiked 80x since February. Anthropic [**confirmed**](https://x.com/bcherny/status/2043163965648515234) they lowered the default thinking effort from high to medium to cut down on token costs, though users can still manually set it back to max if they need that deep reasoning.

**Apple tests four designs for its first smart glasses:** The iPhone maker is [reportedly](https://techcrunch.com/2026/04/12/apple-reportedly-testing-four-designs-for-upcoming-smart-glasses/) testing four different frame styles for its upcoming smart glasses, which are slated for a 2027 release but could be teased as early as this year. According to Bloomberg, these glasses won't include a display. Instead, they'll focus on cameras for photos and video, phone calls, music, and an upgraded Siri. The move marks a major push into the wearable market, putting Apple in direct competition with Meta's Ray-Bans.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Why training your own LLM is still so hard**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/68760fde-94e8-4e5d-9ba1-932d52c925bc/superhumanteam_a_software_engineering_team_made_of_archaic_hu_5c375212-6e78-42c0-be4b-1c62ce80de8e_0.jpg?t=1776076566)
Caption: Source: The Code, Superhuman


--------------------
**$5.9 billion and counting.** The enterprise LLM market is on track to hit that [figure this year](https://www.fortunebusinessinsights.com/enterprise-llm-market-114178), with a massive chunk of that budget going toward custom model training. This means more engineering teams than ever are diving into the open-source training stack for the first time. But as Paras Stefanopoulos, an AI engineer at Baseten, writes in a recent [deep dive](https://www.baseten.co/blog/open-source-llm-training-is-a-mess-here-is-how-it-all-works/), what they're finding is a total mess.

**Framework overlap.** Stefanopoulos mapped the entire stack and found five major frameworks that overlap significantly. This lack of consensus means teams waste days troubleshooting library combinations that crash before training even begins.

**The obvious fix isn't ready.** Even PyTorch's [native stack](https://github.com/pytorch/torchtitan) is struggling. Reports show gradient explosions after just 1,000 steps on newer architectures and frequent out-of-memory crashes during large-scale workloads.

**The smart play.** Baseten is currently relying on NVIDIA’s [Megatron framework](https://arxiv.org/abs/2603.07685) for its reliability at scale. The main takeaway for developers is to stick with stable tools like Megatron for now while keeping your codebase modular enough to easily swap components as the ecosystem matures.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d56108b8-6d2b-49c4-9e7d-7e6c5acf6b83/CleanShot_2026-04-13_at_14.18.10_2x.jpg?t=1776070130)
Caption: Meme of the day.


--------------------
* **Under Wraps:** A leaked Anthropic feature shows a Lovable-style [app builder](https://x.com/marmaduke091/status/2043382991901147158) living directly inside Claude (2.7M views).

* **Swift Skills:** If you're using Codex or Claude Code for iOS development, these [**5 skill packs**](https://x.com/PaulSolt/status/2042716870512353294) from devs who are actually shipping apps can help you get more out of them.

* **Prep Trap:** A Principal Engineer at Atlassian posted a [**Staff interview playbook**](https://x.com/system_monarch/status/2042573963608674673) that's gaining traction, and it starts with a mistake he sees almost everyone make.

* **Inside The Lab:** OpenAI just **[shared](https://x.com/gabrielchua/status/2043339151278506234)** how their team uses Codex internally, from reviewing PRs to onboarding new hires.

* **700 AI Coworkers:** A billion-dollar company gave every employee a personal **[AI coworker](https://x.com/sebgoddijn/status/2042285915435937816)** and published the full breakdown of what they built to make it work.

* **Cursor Flow:** A Cursor engineer just dropped **[18 workflow tips](https://x.com/tibor_tee/status/2041233650881266170)** he regularly shares with users who want better results out of the tool.

* **Career Bet:** Box CEO Aaron Levie thinks AI-generated code is about to trigger a [**massive shift**](https://x.com/levie/status/2043318118169354302) in who gets hired in security, and it's not what most people expect.

* **Test-First Agents:** Ex-Director of Engineering at Oracle [**walks through**](https://www.youtube.com/watch?v=Kx7bAwVH_1c) how he builds with test-driven development (TDD) in Claude Code.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/90c8bac0-f1ab-4721-84aa-473171b2712d/Untitled_design__46_.jpg?t=1776070893)
Follow image link: (https://www.youtube.com/watch?v=nQFtsehu7h0)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[Meta staff engineer's guide to Codex:](https://www.youtube.com/watch?v=nQFtsehu7h0) This tutorial teaches developers how to master OpenAI’s Codex app to boost productivity. You'll learn to navigate its IDE, manage parallel tasks with git worktrees, write effective AI prompts, and build custom automated workflows using an agents.md file.

———————————————————————————

### **Top Repo**

**[Agent Reach:](https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md)** This repo gives your agents instant access to social platforms like Twitter and Reddit. It cuts out the manual overhead and complex configurations, letting you start scraping with just a single command.

———————————————————————————

### **Trending Paper**

[Single-agent LLMs vs. Multi-agent systems:](https://arxiv.org/abs/2604.02460) It's still up for debate whether multi-agent AI is actually smarter or if it just relies on more compute. Interestingly, when you level the playing field on computing power, single agents often perform just as well, or even better than multi-agent systems, on complex reasoning.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to pull live git data into Claude Code commands**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0787bf8a-a4a3-4d49-b76e-4e9f957e78f8/CleanShot_2026-04-13_at_10.53.48_2x.jpg?t=1776058008)
Follow image link: (https://x.com/theo/status/2043103001121034581)
Caption: Source: X/theo


--------------------
Most people think Claude Code slash commands are static, but there is a hidden way to make them dynamic. If you prefix a shell command with “!” in your command file, Claude runs it first and pulls the output as context. 

T3 Chat founder Theo Browne **[shared](https://x.com/theo/status/2043103001121034581)** a PR summary command that automatically pulls diffs and comments by setting up a file at “.claude/commands/pr-summary.md”.

```
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

## Your task
Summarize this pull request...
```
Just run “/pr-summary" on any branch with an open PR to automatically pull in the live diff, comment thread, and file list. Since the “!” syntax works with any shell command, you can also use it to grab things like test results, logs, or database schemas.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 230K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/minimax-drops-an-open-weight-model-apple-designs-its-first-smart-glasses
