---
title: "🔥  Anthropic drops Claude Code computer use"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-03-31
gmail_id: 19d443968b49f806
---

# 🔥  Anthropic drops Claude Code computer use

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-03-31

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Anthropic is shipping fast. Their latest Claude Code update now writes, tests, and self-corrects code by navigating your screen — without you ever leaving the terminal.

**Also:** How to build CLIs that work for agents and humans, 30 Claude agent tools every dev should know, and the only 4 tech roles that survive.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* How Vercel ships AI code without breaking production

* How to automate PR reviews with Codex

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f6f29ba5-84d5-4b68-a185-2cbd6402691d/Untitled_design__33_.jpg?t=1774940180)
Follow image link: (https://x.com/claudeai/status/2038663014098899416)
Caption: Click here to see Claude Code computer use in action.


--------------------
**Claude Code gets full control of your desktop:** The AI lab just shipped [**computer use**](https://x.com/claudeai/status/2038663014098899416) for Claude Code, allowing the agent to take full control of your Mac screen. It can now open apps, navigate UIs, and capture screenshots directly from the CLI. With a single prompt, Claude can write and compile code, launch the app to find bugs, and verify the fix. This macOS-only research preview is currently available to users on Pro and Max plans.

**Alibaba unveils its most capable open-source AI models:** The Chinese tech giant dropped [**Qwen3.5-Omni**](https://qwen.ai/blog?id=qwen3.5-omni), a multimodal model family that natively handles text, images, audio, and video. Its standout feature, Audio-Visual Vibe Coding, can generate functional websites and games simply from spoken descriptions and camera input. The Plus variant even outperforms Google's Gemini-3.1 Pro on audio benchmarks, supporting speech recognition in 113 languages and processing up to 10 hours of audio. [**Watch the demo.**](https://x.com/Alibaba_Qwen/status/2038637985856733623)

**Supply chain attack hits one of npm's most downloaded packages:** A major security breach just hit [**Axios**](https://x.com/i/trending/2038812760398508539) after attackers hijacked a maintainer's account. They slipped malware into two new releases that quietly deploy a remote access trojan across macOS, Windows, and Linux before wiping their tracks to stay hidden. With over 83 million weekly downloads, the impact is massive. If you're on version 1.14.1 or 0.30.4, downgrade immediately and rotate all credentials on the affected machine.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [Your agent is only as good as your prompt.](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/69034f49-0852-43df-8c1f-05b49907bcf1/Newsletters_Image_1920x1080__5_.png?t=1774876710)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
Claude Code, Cursor, Codex. The output ceiling is insane. But "fix the bug" gets you slop. Detailed context gets you shipping code.

The problem: typing out file references, edge cases, and architecture context 40 times a day is exhausting. So you cut corners. Your agent gets lazy input.

[Wispr Flow](https://ref.wisprflow.ai/thecode) lets you speak full prompts with syntax-aware dictation. camelCase, snake_case, file names all preserved. Auto-tags files in Cursor and Windsurf.

[Used by engineers at OpenAI, Vercel, and Clay](https://ref.wisprflow.ai/thecode). Works on Mac, Windows, iPhone, and Android.

Better prompts in. Better code out. **[Try Free](https://ref.wisprflow.ai/thecode)**


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **How Vercel ships AI code without breaking production**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/10faf480-73ac-4f1e-9cb4-6ed704b4db6f/superhumanteam_a_software_engineering_team_working_on_trainin_66c7efe2-6a9f-4b16-b9a2-f886dd4ef72b_0.jpg?t=1774948776)
Caption: Source: The Code, Superhuman


--------------------
**Amazon broke first.** Following a wave of AI-related [outages](https://fortune.com/2026/03/18/ai-coding-risks-amazon-agents-enterprise/) at Amazon, internal docs show failures are becoming more frequent and hitting more systems at the same time. In response, Vercel just [published](https://vercel.com/blog/agent-responsibly) its own framework for shipping agent-generated code. The takeaway? Passing CI (Continuous Integration) is no longer a guarantee of safety.

**The "Flawless" code trap.** Agent-generated PRs often look perfect. They pass static analysis and follow all repo conventions but a [CodeRabbit study](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report) reveals that AI code produces 1.7x more bugs than human-written code, with logic errors jumping by 75%. Because agents don't understand specific failure modes, there’s a massive gap between code that is "technically correct" and code that is "operationally safe."

**Infrastructure as the safety net.** Vercel is shifting its focus from manual reviews to infrastructure-based fixes, including auto-rollback deployments and continuous production testing. As Vercel CEO Guillermo Rauch [put it](https://x.com/rauchg/status/2038759092442050651), "vibing" and mission-critical infrastructure simply don't mix.

**Three questions before every PR.** Vercel's internal guidance boils down to a checklist engineers run before shipping any agent-generated code: What does this do once rolled out? How can it hurt production or customers? And would you own an incident tied to it? If you can't answer all three, the code isn't ready.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY DEEPL**

## [AI isn’t the story anymore. Language is.](https://deeplspringlaunch.com/?utm_source=linkedin&utm_medium=newsletter&utm_campaign=DeepL_Spring_Launch&utm_content=superhuman)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/334825a2-1f3e-4a92-8a7d-48958bdf77e0/Deepl_thecode.jpg?t=1774876868)
Follow image link: (https://deeplspringlaunch.com/?utm_source=linkedin&utm_medium=newsletter&utm_campaign=DeepL_Spring_Launch&utm_content=superhuman)
Caption: 


--------------------
Everyone's talking about what AI can do. [DeepL's Spring Launch](https://deeplspringlaunch.com/?utm_source=linkedin&utm_medium=newsletter&utm_campaign=DeepL_Spring_Launch&utm_content=superhuman) is about what it can do in any language. Translation that thinks. Voice that works in real time. AI that fits the way your business already runs. 

If you're following where AI is actually going — this is worth an hour. April 16 · 4 PM CEST / 10 AM EDT.

[Save your spot](https://deeplspringlaunch.com/?utm_source=linkedin&utm_medium=newsletter&utm_campaign=DeepL_Spring_Launch&utm_content=superhuman)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/82d67d06-d29b-4fec-a11b-ad9908684830/CleanShot_2026-03-31_at_15.03.12_2x.jpg?t=1774949638)
Caption: Meme of the day.


--------------------
* **Built for Bots:** Every CLI you ship will get called by an AI agent. This **[Google Cloud guide](https://x.com/GoogleCloudTech/status/2038778093104779537)** shows you how to design for both in under 10 minutes.

* **Agent Arsenal:** Nobody had mapped the full Claude **[agent ecosystem](https://x.com/cyrilXBT/status/2038443999241924967)** until now. This thread covers 30 frameworks, libraries, and repos every dev should know.

* **Last Four Standing:** A post claiming only **[4 types of roles](https://x.com/chintanzalani/status/2038026663867330850)** will survive at tech companies is going viral (1.1M views).

* **Frenemies:** An OpenAI engineer just **[dropped a plugin](https://x.com/reach_vb/status/2038670509768839458)** that brings Codex directly into Claude Code for reviews and multi-agent handoffs (1M views).

* **Research Loop:** One developer broke down Andrej Karpathy's latest open-source release that builds AI research agents that **[improve themselves](https://x.com/DavidOndrej1/status/2037519926869585981)**.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to automate PR reviews with Codex**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/eae4be75-f7ae-4c0d-84ed-cbd835e95d0b/superhumanteam_a_software_engineer_sitting_at_a_desk_typing_o_4369c567-d9bd-4126-9b9b-39ad4afa56b5_2.jpg?t=1774939576)
Caption: Source: The Code, Superhuman


--------------------
PR reviews are a major bottleneck. Reviewers are constantly swamped, regressions slip through the cracks, and missing tests often go unnoticed until production breaks. OpenAI's Codex can [**solve this**](https://developers.openai.com/codex/use-cases/github-code-reviews) by acting as an automated, first-pass reviewer directly within GitHub.

Just enable Codex in your repo settings and comment `@codex review` on any pull request. It will post inline comments just like a human teammate would. If it flags an issue, simply comment `@codex fix it` to kick off a cloud task that patches the code and updates the PR automatically.

To customize what Codex looks for, just add an `AGENTS.md` file to your repo root:

```
## Review guidelines
- Flag typos and grammar issues as P0 issues.
- Flag potential missing documentation as P1 issues.
- Flag missing tests as P1 issues.
  ...
```
Codex applies the closest `AGENTS.md` to each changed file, so you can put stricter rules deeper in the tree for sensitive packages.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2599bbfb-3521-4a1b-aa50-1c795d0fe366/Untitled_design__34_.jpg?t=1774940366)
Follow image link: (https://www.youtube.com/watch?v=XV5bhkDpL7U)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to build voice agents with Gemini 3:**](https://www.youtube.com/watch?v=XV5bhkDpL7U) You’ll learn to build real-time voice agents using the Gemini 3 Live API. This tutorial covers everything from managing websockets and processing live audio and video to working with the Google GenAI SDK. It also explores partner tools for faster deployment.

———————————————————————————

### **Top Repo**

[**Hermes Agent:**](https://github.com/NousResearch/hermes-agent) This self-improving AI agent from Nous Research is in a league of its own. It features a built-in learning loop that allows it to develop new skills through experience and refine them in real-time. It actively retains knowledge, references past conversations, and builds a deeper understanding of you with every session. 

———————————————————————————

### **Trending Paper**

[**How Perplexity’s voice agent was built (by OpenAI):**](https://developers.openai.com/blog/realtime-perplexity-computer) Perplexity needed a reliable voice interface for their AI products that could handle long contexts and noisy environments. They solved this using the Realtime API by feeding data in smaller chunks, standardizing audio processing, and introducing voice lock controls.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/claude-code-now-controls-your-screen-alibaba-drops-qwen3-5-omni
