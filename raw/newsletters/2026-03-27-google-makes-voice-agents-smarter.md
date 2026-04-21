---
title: "🎙️  Google makes voice agents smarter"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-03-27
gmail_id: 19d2f9e16ef15f52
---

# 🎙️  Google makes voice agents smarter

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-03-27

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Ever talked to a laggy voice AI agent? It’s painful. Google just took a massive leap toward changing that with Gemini’s latest upgrade. Speed isn’t even the best part: you can now have much longer conversations thanks to its doubled memory.

**Also:** How to build agent evals, design CLIs for coding agents, and run deep research from your terminal.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* What in the world is comprehension debt?

* How to make Claude Code read Reddit

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/99ac8631-3e47-472f-af02-bf1583801a40/Untitled_design__29_.jpg?t=1774595812)
Follow image link: (https://x.com/Google/status/2037190616061284353)
Caption: Click here to see Gemini 3.1 Flash Live in action.


--------------------
**Google's Gemini 3.1 Flash Live raises the bar for voice agents:** The search giant just shipped its most powerful real-time [**audio model**](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/)** **to date, built specifically for voice-first agents that can manage complex tasks at scale. It boasts a 90.8% score on ComplexFuncBench Audio for multi-step function calling and leads Scale AI's Audio MultiChallenge for its ability to follow instructions even with real-world interruptions.

**Stripe builds a CLI so agents can set up your infrastructure:** The payments giant just launched [**Stripe Projects**](https://x.com/patrickc/status/2037190688950161709), a command-line tool that lets you set up hosting, databases, auth, and analytics with just a few commands. It handles everything from credentials and billing to plan upgrades right from the terminal, so you can stop jumping back and forth to the dashboard and focus on shipping. They've already teamed up with early partners like Vercel, Supabase, and Clerk. Click [**here**](https://projects.dev/) to request access.

**Chroma open-sources a 20B search agent that rivals frontier models:** This AI data infrastructure company just dropped [**Context-1**](https://x.com/trychroma/status/2037243681988894950), a 20B-parameter agentic search model under the Apache 2.0 license. Built on OpenAI's gpt-oss-20B, it handles complex queries by breaking them down into sub-queries, retrieving data iteratively, and automatically pruning irrelevant info to fit a 32k-token limit. It rivals heavyweights like GPT-5.4 and Opus 4.6 on public benchmarks while being faster and cheaper.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **What in the world is comprehension debt?**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f80281df-7160-4c3d-9065-f13f39a04113/CleanShot_2026-03-27_at_12.34.27_2x.jpg?t=1774595131)
Follow image link: (https://www.anthropic.com/research/AI-assistance-coding-skills)
Caption: Source: Anthropic.com


--------------------
**Faster than you can follow.** Pull requests are merging faster than ever, codebases are expanding, and every productivity metric looks fantastic. But behind the scenes, many engineers are hitting a strange wall. They can no longer explain exactly why their own systems work the way they do. Addy Osmani, Director at Google Cloud AI, recently gave this problem a [**name**](https://addyosmani.com/blog/comprehension-debt/): comprehension debt.

**Clean code, shallow understanding.** Unlike technical debt, which announces itself through slow builds and messy dependencies, comprehension debt is far more subtle. The code looks clean, the tests are green, and the reckoning only arrives at the worst possible moment — usually when something breaks and nobody can trace why.

**The broken feedback loop.** Code reviews used to be the primary engine for knowledge sharing. By reading a teammate's PR, you learned how the system evolved. But AI now generates code faster than any human can genuinely review, effectively breaking that loop. An [Anthropic study](https://www.anthropic.com/research/AI-assistance-coding-skills) of 52 engineers confirmed the impact: those using AI assistants scored significantly lower on comprehension tests, with the sharpest declines occurring in debugging performance.

**Comprehension is the job now.** AI handles the heavy lifting of writing code. The real engineering now happens in understanding what was written, why it was built that way, and whether those architectural choices were the right ones. If your team is feeling the weight of this shift, ex-Vercel engineer Matt Pocock recently [**shared**](https://x.com/mattpocockuk/status/2036768796065640554) a simple rule worth adopting.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/13ab1fca-f8cf-4918-8d71-a2c468c120cb/CleanShot_2026-03-27_at_14.46.55_2x.jpg?t=1774603083)
Caption: Meme of the day.


--------------------
* **DIY Vaccine:** An AI consultant used ChatGPT, Gemini, and Grok to design a custom mRNA cancer vaccine for his dog. Sam Altman met him this week and has a [big vision](https://x.com/sama/status/2037396826060673188) for where this goes next.

* **Broken Evals:** Most teams throw hundreds of tests at their agents and call it progress. LangChain just dropped the [**eval framework**](https://x.com/Vtrivedy10/status/2037203679997018362) they actually use instead.

* **CLI Researcher:** A dev built a [**deep research agent**](https://www.youtube.com/watch?v=2NcLtWazHFU) that runs entirely from your terminal using Browserbase.

* **Agent-Proof CLIs:** Most CLIs aren't built for AI agents. A former Microsoft PM wrote [**7 principles**](https://x.com/trevin/status/2037250000821059933) for designing ones that work seamlessly with Claude Code and Codex.

* **Vibe-Coded Science:** Google's Project Genie team needed a way to visualize world models, so they [**vibe-coded one**](https://x.com/GoogleAIStudio/status/2036926844503810115) in AI Studio.

* **GPU School:** An ML research engineer just [**open-sourced**](https://www.linkedin.com/posts/goabiaryan_fundamentals-of-gpu-engineering-share-7442915779827650562-KfQB/) 38 podcast episodes on GPU engineering fundamentals.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to make Claude Code read Reddit**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/95ecbbf2-1a3a-4770-a83c-a386e0dd7ee4/superhumanteam_A_lone_software_engineer_sitting_at_a_desk_typ_9bb62cb6-5358-42ad-9976-04fb1886c091_2.jpg?t=1774612222)
Caption: 


--------------------
Claude Code's WebFetch often hits a wall with sites like Reddit, returning a 403 error that can stall your research. To fix this, YK, an ex-Google engineer, [shared](https://github.com/ykdojo/claude-code-tips?tab=readme-ov-file#tip-11-use-gemini-cli-as-a-fallback-for-blocked-sites:~:text=just%20Claude%20Code.-,Tip%2011%3A%20Use%20Gemini%20CLI%20as%20a%20fallback%20for%20blocked%20sites,-Claude%20Code%27s%20WebFetch) a clever workaround using Claude Code's skills system. By creating a custom skill file, you can teach Claude to pivot to the Gemini CLI whenever it encounters a blocked domain. 

Just install the Gemini CLI and authenticate:

```
npm install -g @google/gemini-cli
gemini  # run once to auth with your Google account
```
Create the skill directory and download the file:

```
mkdir -p ~/.claude/skills/reddit-fetch
curl -o ~/.claude/skills/reddit-fetch/SKILL.md \
  https://raw.githubusercontent.com/ykdojo/claude-code-tips/main/skills/reddit-fetch/SKILL.md
```
The next time you ask Claude Code to pull data from Reddit, it'll automatically trigger the skill to manage the tmux session, Gemini query, and output capture. Since skills load on demand, you only use tokens when Claude Code actually needs to access Reddit.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5eecb27a-33fc-4dfa-877b-9f651a6d03f9/Untitled_design__30_.jpg?t=1774606169)
Follow image link: (https://www.youtube.com/watch?v=o5Mi5SYSDnY)
Caption: 


--------------------
### **Top Tutorial**

[**How Stripe’s team built their coding agent:**](https://www.youtube.com/watch?v=o5Mi5SYSDnY)** **This video breaks down how Stripe’s engineering team uses AI agents, or "minions," to automate their workflows. You'll see how teams can trigger these agents directly from Slack to write and deploy code at the same time. It also shows how these agents use machine-to-machine payments to independently purchase services and interact with third-party APIs.

———————————————————————————

### **Top Repo**

[**Awesome Cursor Rules:**](https://github.com/PatrickJS/awesome-cursorrules)** **This repo gives teams plug-and-play rules for dozens of stacks, helping you get sharper suggestions, write more consistent code, and ship faster across every project.

———————————————————————————

### **Trending Paper**

[**Improving Composer through real-time RL (by Cursor):**](https://cursor.com/blog/real-time-rl-for-composer) Earlier this week, Cursor dropped a technical report on how they [trained](https://x.com/cursor_ai/status/2036566134468542651) Composer 2. Now, they've shared more research into their training process for new checkpoints. With real-time RL, they’re able to ship updated versions of the model every five hours.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/google-drops-gemini-3-1-flash-stripe-unveils-stripe-projects
