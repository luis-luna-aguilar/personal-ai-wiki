---
title: "👀  OpenAI made coding fun again"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-05-04
gmail_id: 19df34bc5b78ae06
---

# 👀  OpenAI made coding fun again

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-05-04

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/48c26b5b-5e41-45b8-87bc-f7e3479347c3/Group_thecode_Granola__1_.jpg?t=1777638195)
Follow image link: (https://go.granola.ai/thecode)
Caption: 

----------
**Welcome back.** OpenAI keeps finding ways to make coding feel fun again. Their weekend update pulled over 3 million views on X — and developers are loving the playful twist. [**See it here.**](https://x.com/OpenAIDevs/status/2050275713824211041)

**Also:** How to do agent-native product management, pressure-test a startup idea with a Codex skill, and follow the Musk v. Altman trial in a transcript-built wiki.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Cursor's bet: the agent harness is the product

* How to skip copy-pasting errors into Claude Code

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5271c70b-c639-4d29-92a2-0fdc55b7e1ea/Thumbnail__15_.jpg?t=1777882662)
Follow image link: (https://www.youtube.com/watch?v=0SgCiUfoYo8)
Caption: Click here to watch Claude Security in action.


--------------------
**Anthropic unveils an AI vulnerability scanner for enterprise teams:** The AI lab just released [**Claude Security**](https://claude.com/blog/claude-security-public-beta) in public beta, using Opus 4.7 to find and patch vulnerabilities in enterprise code. Its multi-stage validation cuts down on false positives, letting teams fix issues quickly. You can send scan results to Slack and Jira via webhooks or export them as CSV and Markdown. [**See how it works.**](https://www.hedgineer.io/content/claude-security/)

**xAI's newest model brings always-on reasoning at a fraction of the cost:** The Musk-founded AI lab just shipped [**Grok 4.3**](https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite), which features a reasoning-first engine and a massive 1M token context window. At $1.25 per million input tokens and $2.50 for output, it's significantly cheaper than Claude Opus or GPT-5.5. They also launched a [voice cloning API](https://x.com/xai/status/2050355373052223585) that lets developers create custom voices in under two minutes or choose from over 80 voices in 28 languages.

**Developer's AI-coded app success turns into maintenance nightmare:** A viral Reddit [**post**](https://x.com/i/trending/2050965519042265551) detailed how a developer spent six months shipping with Cursor, Lovable, and Bolt, resulting in a successful app but a codebase that was a total disaster. When a new hire joined and saw the repo, they were completely lost. Now, senior engineers are calling for stricter code reviews and treating sloppy, unchecked AI-generated pull requests as a performance issue.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY GRANOLA**

## [Try this once—you’ll never use an AI notetaker again](https://go.granola.ai/thecode) 


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0dc9d13b-7e22-4235-bbda-56d000d6f81f/1920x1080_-_Main_Granola_Value_Proposition__1_.jpg?t=1777638261)
Follow image link: (https://go.granola.ai/thecode)
Caption: 


--------------------
Most AI notetakers just transcribe and send a summary. [Granola is different](https://go.granola.ai/thecode)—it’s built for everything after the meeting.

It [runs quietly in the background](https://go.granola.ai/thecode) while you take notes your way—no interruptions.

Then turns your notes into clear summaries, action items, and next steps—from your POV.

Chat with your notes to draft follow-ups, prep meetings, or turn conversations into work instantly.

Perfect for back-to-back meetings.

[Try Granola for a month](https://go.granola.ai/thecode) at no cost with code: THECODE (1 month off any paid plan)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Cursor's bet: the agent harness is the product**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a393e2b1-9c33-4c17-9232-886283bb7365/superhumanteam_a_software_engineering_team_working_on_a_detai_64560258-ec76-468c-9b3b-716c855c4a14_1.jpg?t=1777889154)
Caption: Source: The Code, Superhuman


--------------------
**Beyond the model.** Most devs experimenting with AI coding agents start by looking for the best model. Cursor’s betting that's the wrong starting point. They just [released an SDK](https://cursor.com/blog/typescript-sdk) that treats their agent harness (the tools, prompts, and edit logic surrounding the model) as the actual product. Their pitch is simple: the real value isn't the model itself, but the layer that manages how it works.

**Inside the harness.** OpenAI and Claude models are trained on different file-editing formats, so Cursor [tailors the output](https://cursor.com/blog/continually-improving-agent-harness) to each model to save reasoning tokens and reduce errors. Since standard benchmarks overlook these nuances, they use a custom metric called “Keep Rate” to track how much AI code stays after user edits, with every update tested via A/B test.

**The payoff is real.** In just one sprint, Cursor slashed unexpected tool call errors by 10x. They also used clever prompting to fix a Claude quirk where the model would avoid long-context tasks, proving that better scaffolding was the answer.

**Call it “Model-Harness-Fit”.** Cursor isn't alone here. Nicolas Bustamante, whose startup Fintool was acquired by Microsoft, showed how Claude Code, Codex CLI, and Copilot CLI produce [totally different results](https://x.com/nicbstme/status/2051131906327212298) from the same model. Bustamante argued that since each new model breaks the previous version's harness, the work of maintaining these AI tools never really stops.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/09a4af45-db27-4fda-a5e6-d1bb402f9922/CleanShot_2026-05-04_at_12.14.45_2x.jpg?t=1777877178)
Caption: Meme of the day.


--------------------
* **Always On:** If your long-running coding agents die the second you shut your MacBook, this [**2-step setup**](https://x.com/petergyang/status/2050963126234034387) lets them run even when it's closed.

* **Agent-Native PM:** One PM is running his entire product on coding agents alone. Here's the step-by-step [**breakdown**](https://every.to/guides/ai-product-management-guide) of his exact stack.

* **Skill Check:** A Google senior engineer shares which [**AI certifications**](https://www.youtube.com/watch?v=1LlW9rdtWZ4) hiring managers actually care about, and which ones quietly collect dust on your resume.

* **Idea Killer**: This [**Codex skill**](https://x.com/gdb/status/2050972114077843772) pressure-tests your startup idea, hunts fatal flaws, maps competitors, and scopes a 2-week MVP. OpenAI cofounder Greg Brockman approved (1.9k likes).

* **Codex Pets**: OpenAI quietly shipped a /pet command in Codex, and one developer wasted no time turning Anthropic's CEO into [**his pet**](https://x.com/damnGruz/status/2050351249162375176). You can make your [own](https://x.com/OpenAIDevs/status/2050299857974489153) too (4.8k likes).

* **One-Prompt Module**: A founder built a native image processing module for his JavaScript runtime using a three-sentence Claude prompt. [Here’s the prompt.](https://x.com/jarredsumner/status/2050504432081908210)

* **Trial Tracker:** The Musk v. Altman trial is unfolding right now, and this [wiki](https://trial.mts.now/) built from court transcripts is the cleanest way to follow every twist.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to skip copy-pasting errors into Claude Code**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/21cfce1a-0483-4ec3-8a0d-f099a2387caa/superhumanteam_a_software_engineer_sitting_at_a_desk_typing_o_5650cccb-5ee5-4366-8ced-a6406a67f2e7_3.jpg?t=1777889275)
Follow image link: (https://x.com/svpino/status/2046928263134802314)
Caption: 


--------------------
Copy-pasting error logs into Claude is a major pain. You lose formatting, waste time, and truncation often cuts off the parts you actually need. This [fix](https://x.com/svpino/status/2046928263134802314) lets you skip the manual step entirely by sending any command's output directly into Claude:

```
cat error.log | claude "fix this"
```
By reading the full “stdout” exactly as it appears in your terminal, the model gets much better context than a messy copy-paste. This works for any command, making it easy to diagnose failing tests:

```
npm test 2>&1 | claude "diagnose the failures"
```
To move even faster, set up a shell alias like: `alias fix='claude "fix this"'` to close the loop instantly.

P.S. You can find 50+ AI coding hacks [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/fae6150b-dbb5-47cb-99ca-50d69053b21d/Thumbnail__16_.jpg?t=1777887918)
Follow image link: (https://www.youtube.com/watch?v=j7d5rs0iMlE)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**Build and ship with Codex:**](https://www.youtube.com/watch?v=j7d5rs0iMlE) This 4-hour tutorial shows you how to build and ship full-stack web apps using OpenAI’s Codex. You'll pick up hands-on agentic coding skills like leveraging plugins, setting up automations, and running sub-agents, while mastering stacks like Next.js and Vercel to level up your workflow.

———————————————————————————

### **Top Tool**

[**Montage:**](https://www.usemontage.ai/) AI agents are notoriously slow and expensive when it comes to rendering UI. Montage solves this by turning simple intent schemas into production-ready components. It’s 10x faster, slashes token usage by 100x, and keeps everything perfectly on-brand.

———————————————————————————

### **Top Repo**

[**Ruflo**](https://github.com/ruvnet/ruflo)** (39.5k ⭐):** This repo is the leading orchestration platform for Claude, designed to deploy multi-agent swarms and coordinate autonomous workflows. It features an enterprise-grade architecture with self-learning swarm intelligence, RAG integration, and native support for Claude Code and Codex.

———————————————————————————

### **Trending Paper**

[**Speeding up agentic workflows (by OpenAI):**](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/) Traditional API requests created major latency bottlenecks for coding agents by repeatedly processing the entire conversation history for every action. Switching to persistent WebSocket connections cached this state, eliminating redundant work and speeding up end-to-end agentic workflows by 40%.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 260K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/anthropic-unveils-claude-security-xai-drops-grok-4-3-and-voice-cloning-api
