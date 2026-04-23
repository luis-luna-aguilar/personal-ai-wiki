---
title: "👀  OpenAI drops a privacy focused model"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-04-23
gmail_id: 19dbaa5d0c437f64
---

# 👀  OpenAI drops a privacy focused model

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-04-23

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/92805d3c-0c91-487e-ae58-c3097ba7b872/Group_MongoDB__7_.jpg?t=1776846413)
Follow image link: (https://fandf.co/4dQRPTm)
Caption: 

----------
**Welcome back.** Your private data should stay exactly where it belongs: on your device. OpenAI just dropped a new open-weight model that lets developers redact sensitive info locally before it ever hits the cloud. And it wasn't the only thing they shipped yesterday.

**Also:** Plug 80 Nvidia-hosted models into your coding agent at no cost, 5 design patterns for long-running agents, and why Karpathy says a 1,800x smaller model can match a 1.8T giant.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* How AI is rewriting engineering interviews

* How to stop restarting Gemini CLI on long tasks

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c5d75c05-885e-480f-b615-c5283a6e1e59/Thumbnail__2_.jpg?t=1776935726)
Follow image link: (https://www.youtube.com/watch?v=yyvVUEPSCu0)
Caption: Click here to see OpenAI’s workspace agents in action.


--------------------
**OpenAI ships open-weight model for redacting private data:** The ChatGPT maker just dropped [**Privacy Filter**](https://openai.com/index/introducing-openai-privacy-filter/), a new 1.5B-parameter open-weight model that automatically hides personal info like emails and API keys on your own device. The lab also introduced [**workspace agents**](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) for Business and Enterprise users. These Codex-powered agents can handle complex workflows in Slack and ChatGPT and are currently free to try through May 6. Try the new privacy model on [**Hugging Face**](https://huggingface.co/openai/privacy-filter) now.

**Alibaba unveils a smaller model that tops coding benchmarks:** The Chinese tech giant just open-sourced [**Qwen3.6-27B**](https://qwen.ai/blog?id=qwen3.6-27b), a multimodal model that beats their previous 397B-parameter flagship across all major coding benchmarks. Its dense architecture makes it much easier to deploy than complex MoE models, bringing top-tier coding performance to a more practical scale. [Run the model locally.](https://unsloth.ai/docs/models/qwen3.6)

**Google evolves Vertex AI into an agent platform:** The search giant just unveiled the [**Gemini Enterprise Agent Platform**](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) at Cloud Next '26, effectively replacing its flagship AI development suite. Moving forward, all Vertex AI updates will live on this new platform, which features a low-code Agent Studio and a graph-based kit for building sub-agent networks. The new runtime now powers autonomous workflows that can run for days, all while Google’s models handle a staggering 16 billion tokens per minute via API.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY MONGODB**

## [Join the builders shaping what’s next.](https://fandf.co/4dQRPTm)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e4eb5e53-1216-4d4f-876e-1ea53ad45a78/mongo_db_23rd_april.jpg?t=1776930074)
Follow image link: (https://fandf.co/4dQRPTm)
Caption: 


--------------------
[MongoDB.local London 2026](https://fandf.co/4dQRPTm) brings together developers, founders, and AI leaders for a full day of real-world talks, hands-on sessions, and networking. 

Learn how teams are taking AI from prototype to production, explore modern data architectures, and connect with experts solving today’s toughest engineering challenges.

**[London | May 7— Save your spot.](https://fandf.co/4dQRPTm)**


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **How AI is rewriting engineering interviews**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c0e86954-86d3-47ac-a507-4819a17350b3/CleanShot_2026-04-23_at_18.05.26_2x.jpg?t=1776947805)
Caption: Source: Augment Code


--------------------
**Code stopped being the test.** Coding interviews became obsolete the second Claude Code and Codex started passing them on autopilot. Sierra, the AI agent startup founded by former Salesforce co-CEO Bret Taylor, just [published](https://sierra.ai/blog/the-ai-native-interview) the most in-depth look yet at what's taking their place.

**The signal cratered first. **Traditional interviews mostly measured syntax and framework recall, things LLMs now handle in seconds. Karat, an interview-as-a-service firm, which has run [over 600,000](https://www.businesswire.com/news/home/20251210685922/en/Karat-Launches-NextGen-Interviews-The-First-Human-Led-AI-Enabled-Talent-Evaluation-Solution) interviews for companies like Atlassian and PayPal, sees this shift as well. Stick to pre-LLM rubrics today, and you’re basically just testing if a candidate remembered to use AI.

**Live builds replaced live coding.** A consistent pattern is emerging. Give candidates two hours, their AI of choice, and a real product to build, then grade their output and decision-making. This is the core of Sierra’s onsite interview. Augment Code [shipped](https://www.augmentcode.com/blog/how-we-hire-ai-native-engineers-now) a similar model in March, evaluating engineers on dimensions like product taste and architectural judgment.

**Calibration is the new headache.** Open-ended interviews are harder to grade and often spark debate during debriefs. But the payoff is worth it. It’s better to hire for standout strengths like strong product taste and sharp architectural instincts instead of just checking for a lack of weaknesses. The real question has shifted from whether someone can code to what they build and why.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c6b348f3-4eb3-49cd-9695-07e3c7df3ad1/CleanShot_2026-04-23_at_15.17.54_2x.jpg?t=1776937713)
Caption: Meme of the day.


--------------------
* **Free Inference:** Nvidia is quietly [**hosting**](https://x.com/dhruvtwt_/status/2047006444701274380) nearly 80 frontier models you can plug straight into your coding agent (21K bookmarks).

* **Pixel Stream:** Shopify's CEO is hyping a prototype that [**streams entire UIs**](https://x.com/tobi/status/2047133338150842676) directly from an AI model, skipping the frontend stack entirely (2.6M views).

* **Agent Blueprint:** Google Cloud AI Director Addy Osmani [**mapped out**](https://x.com/GoogleCloudTech/status/2046989964077146490) the 5 design patterns behind production-grade AI agents (1.7K bookmarks).

* **Code Guard:** This new Claude Code **[command](https://x.com/ClaudeDevs/status/2046999435239133246)** runs a fleet of cloud bug-hunters before you merge (1.8M views).

* **Data Over Size:** OpenAI co-founder Andrej Karpathy claims today's 1.8T parameter frontier could be matched by a model [**1,800x smaller**](https://x.com/aakashgupta/status/2046860622160371869) (465K views).

* **Agent Fluency:** Google open-sourced a spec that gives AI agents a [**shared language**](https://x.com/stitchbygoogle/status/2046624729403142320) across projects (3.8M views).

* **Buy the Future:** AngelList's Naval Ravikant just launched a fund that lets you [**own a slice**](https://x.com/naval/status/2046991137022648800) of OpenAI, Anthropic, and xAI for $500 (3.9M views).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to stop restarting Gemini CLI on long tasks**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8feeffc6-c5a8-47ce-92cb-1ce696c8c08c/CleanShot_2026-04-23_at_10.48.26_2x.jpg?t=1776921622)
Follow image link: (https://x.com/EvanOtero/status/2016507012633255941)
Caption: Source: X/EvanOtero


--------------------
Long agentic runs often stall when context windows max out, forcing a restart that wipes your state. Evan Otero from the Gemini CLI team [**solved this**](https://github.com/gemini-cli-extensions/ralph) by porting Geoffrey Huntley's Ralph loop technique into a new extension. It fixes the issue in a single command. You'll need Gemini CLI v0.26.0 or newer to use the hooks required for the setup:

```
gemini extensions install https://github.com/gemini-cli-extensions/ralph
```
Then run a loop with an iteration cap and a completion phrase:

```
/ralph:loop "Build a REST API for todos with CRUD and full test coverage. Output 'DONE' when all tests pass." --completion-promise "DONE" --max-iterations 20
```
An AfterAgent hook clears session memory and restarts the agent with the original prompt after every turn, keeping the context stable until it finishes or hits the limit. Use the “-y” flag in sandbox mode to keep the loop running without pausing for tool calls.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a736fa30-c28c-4e09-aab5-62b342c32132/Thumbnail__3_.jpg?t=1776940036)
Follow image link: (https://www.youtube.com/watch?v=rFGlJ4oIlhw)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

**[How to run Parallel agents in Claude Code:](https://www.youtube.com/watch?v=rFGlJ4oIlhw)** This tutorial shows developers how to scale their AI coding output. You'll learn how to safely run multiple AI sessions simultaneously using Git worktrees, isolate databases to prevent conflicts, and automate your workflow from GitHub issues all the way to fully validated pull requests.

———————————————————————————

### **Top Tool**

[**Code Rabbit:**](https://www.coderabbit.ai/) An AI-powered code review assistant that integrates with GitHub, GitLab, and Bitbucket to provide automated, line-by-line feedback on code quality, security vulnerabilities, and bugs.

———————————————————————————

### **Top Repo**

[**Claude Context**](https://github.com/zilliztech/claude-context)** (8k ⭐):** This repo contains an MCP plugin that enables semantic code search for Claude Code and other AI coding assistants, providing them with deep context from your entire codebase.

———————————————————————————

### **Trending Paper**

[**When should agents use direct APIs vs CLIs vs MCP? (by Anthropic):**](https://x.com/ClaudeDevs/status/2047086372666921217) Linking AI agents to external systems through APIs or CLIs often leads to massive integration headaches at scale. MCP fixes this by providing a standardized, portable layer that seamlessly connects cloud-based agents to remote tools and data.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 240K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/openai-ships-a-new-open-source-model-alibaba-drops-qwen3-6-27b
