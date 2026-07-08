---
title: "👀  Alibaba allegedly cloned Claude"
type: newsletter
sender: "The Code <superhumancode@news.codenewsletter.ai>"
received: 2026-06-26
gmail_id: 19f04429451e3636
---

# 👀  Alibaba allegedly cloned Claude

**From:** The Code <superhumancode@news.codenewsletter.ai>
**Date:** 2026-06-26

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ff9288c7-55c3-479a-8305-a80a13a4b716/Group_AI21_Latest.jpg?t=1782438303)
Follow image link: (https://www.ai21.com/blog/spend-isnt-going-down-what-now/?utm_source=TheCode)
Caption: 

----------
**Welcome back.** Protecting model reasoning has become the top priority for AI labs. Anthropic claims Chinese giant Alibaba used nearly 29 million exchanges to extract Claude's capabilities. They've taken the fight all the way to the US Senate, asking Congress to step in and hold companies accountable for this kind of extraction. 

**Also:** How to use Claude Tag, fixing your team’s code review process and how to choose between code and LLMs.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18b4e61a-952c-4556-8c57-2d0e65314c17/superhumanteam_generate_a_portrait_image_of_the_person_in_omn_7bf7424f-9fbd-4a84-83e9-c8f7d8ad2f92_3.jpg?t=1782467368)
Caption: Made with Midjourney.


--------------------
**Anthropic reportedly accuses Alibaba of mass distillation attack:** The AI lab informed US lawmakers that operators linked to a Chinese e-commerce giant used thousands of fake accounts to run nearly [29 million exchanges](https://www.bbc.com/news/articles/cwyklykn5dwo). According to the lab, this was a distillation attack designed to copy Claude's reasoning into a cheaper rival model. They're now calling on Congress to penalize what they describe as industrial-scale theft, mirroring similar accusations OpenAI has leveled against Chinese groups. 

**OpenRouter lets your agents choose AI models:** The LLM marketplace just rolled out [**an MCP**](https://x.com/OpenRouter/status/2070160491360780798) that lets your AI agent choose the right AI model for the right task. They provide access to 400 models, which prevents your agent from relying on outdated training data. You can set it up in your CLI with just two commands. Once it's connected, your agent can access real-time benchmarks, pricing, and documentation. You can easily find models that cost less than $2 per million tokens and price, test, and swap models in under a minute.

**Vercel ships AI SDK 7 with durable agents:** The hosting platform just dropped [**version 7 of the AI SDK**](https://vercel.com/blog/ai-sdk-7), specifically designed for production-ready agents. Its new WorkflowAgent keeps tasks active through restarts, deployments, and interruptions, so you never start from scratch. Agents can now pause for human approval before risky tool calls and run shell commands inside sandboxes. Plus, you can also swap in harnesses like Claude Code or Codex through one interface.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY AI21**

## [Why are you still paying for tokens that do nothing?](https://www.ai21.com/blog/spend-isnt-going-down-what-now/?utm_source=TheCode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c28a4a46-11c4-4c7c-95de-74d9de406b02/The_code_banner__2__-_Almog_Bashan__1_.png?t=1782438396)
Follow image link: (https://www.ai21.com/blog/spend-isnt-going-down-what-now/?utm_source=TheCode)
Caption: 


--------------------
Most production agents carry [dead weight](https://www.ai21.com/blog/spend-isnt-going-down-what-now/?utm_source=TheCode): context they re-send, instructions they repeat, tools they never touch. But the invoice doesn’t say what was waste, and what worked. Hand-authored rules don't keep up with new model drops, pricing shifts, or workflow drifts.

[AI21 is building the drop-in layer that](https://www.ai21.com/blog/spend-isnt-going-down-what-now/?utm_source=TheCode) reads your live traffic, finds the waste, and cuts it at runtime.

[**Read why we need a self-updating model router.**](https://www.ai21.com/blog/spend-isnt-going-down-what-now/?utm_source=TheCode)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **A smarter AI code reviewer won't cut the noise. Here's what will:**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e9a890bb-1349-407a-ad99-8daf255fa53c/superhumanteam_a_software_engineering_team_working_on_reviewi_f22b3ac7-2bca-4777-956b-5b7c20256809_2.jpg?t=1782466678)
Caption: Source: The Code, Superhuman


--------------------
**Reviews can't keep up.** Teams are shipping more code than managers can review. A recent study tracked 22,000 developers and [found](https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways) that nearly one-third of PRs now merge without any review at all. Reviewers just can't keep up with the volume. The usual fix is an AI reviewer. But that often backfires. It floods you with nitpicks that get ignored. Some open-source maintainers have been overwhelmed by AI-filed issues. They've even started blocking outside contributions. 

Jan Giacomelli, a dev who runs AI review on every backend merge at Ren Systems, argues the value comes from three specific moves most teams avoid:

**First, think about size.** Both you and the AI have a limited context window. Massive merge requests are basically unreadable for everyone. Keep your PRs small. They should be tiny enough that you wouldn't mind scrapping them if the AI messes up. Small changes are where the real review happens.

**Second, you need context.** A generic “review this” prompt just gives you noise. Instead, get the team together. Agree on what’s worth flagging. Save those rules in a markdown file for the AI. If you are not sure where to start, look back at common complaints. Find past human reviews and turn those into your new guidelines.

**The third tip is all about the plumbing.** Set up the review as a manual Continuous Integration (CI) job. Don't run it on every push. This saves tokens and keeps a human in the loop. The real payoff is the cost. Anthropic's standard feature costs $15 to $25 per review. But Giacomelli's custom Claude Code setup uses Sonnet and Haiku. That only costs between $0.15 and $1.50. You can read his [full setup here](https://jangiacomelli.com/blog/3-tips-for-ai-code-review-that-doesnt-suck/) or, for the wider agentic-review picture, former Google Cloud AI Director Addy Osmani's [guide here](https://addyosmani.com/blog/agentic-code-review/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY DATADOG**

## [The developer toolkit you need for the agents era](https://r2trck.com/the-code-datadog-12?utm_medium=newsletter&utm_source=the-code-r&utm_campaign=dg-content-toolkit-2026AIEraDeveloper-delivery-cipipe-ww-en-701VY00000kMeE2YAK&utm_content=paid&utm_term=1-1-2026)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cdef3930-2bd8-49c3-9dfa-fb1275d1bf62/Datadog_X_The_Code_Ad_10_June_26_compressed__1_.jpg?t=1782438881)
Follow image link: (https://r2trck.com/the-code-datadog-12?utm_medium=newsletter&utm_source=the-code-r&utm_campaign=dg-content-toolkit-2026AIEraDeveloper-delivery-cipipe-ww-en-701VY00000kMeE2YAK&utm_content=paid&utm_term=1-1-2026)
Caption: 


--------------------
_Anyone_ can make an AI demo. The hard part is shipping it, monitoring it, and knowing when it breaks (and how to fix it).

[Datadog's Developer Toolkit for the AI Era](https://r2trck.com/the-code-datadog-12?utm_medium=newsletter&utm_source=the-code-r&utm_campaign=dg-content-toolkit-2026AIEraDeveloper-delivery-cipipe-ww-en-701VY00000kMeE2YAK&utm_content=paid&utm_term=1-1-2026) gives you the playbook for building, deploying, and observing AI applications at scale. It covers: CI pipelines, LLM observability, feature flags, testing, and modern AI delivery workflows.

[**Get the toolkit and ship with confidence.**](https://r2trck.com/the-code-datadog-12?utm_medium=newsletter&utm_source=the-code-r&utm_campaign=dg-content-toolkit-2026AIEraDeveloper-delivery-cipipe-ww-en-701VY00000kMeE2YAK&utm_content=paid&utm_term=1-1-2026)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/436fd2ab-0715-4334-8368-9c9d1c63c598/CleanShot_2026-06-26_at_11.41.01_2x.jpg?t=1782454314)
Caption: Meme of the day.


--------------------
* **Beautiful UI:** A full-stack engineer used Claude to build a token-based [design system](https://x.com/Rasmic/status/2069967490575192401) that scales without manual tweaks (4.2K bookmarks).

* **Tag Claude In:** Anthropic recently unveiled an AI coworker you can tag in Slack. This video covers **[how it works](https://x.com/ClaudeDevs/status/2070235730295865661)** and the best practices behind it (1.6K likes).

* **No-JS Forms:** An ex-Meta staff engineer [explains](https://www.linkedin.com/posts/yangshun_i-feel-sad-whenever-people-blindly-reach-share-7471195958345650176-KWul/) why you shouldn’t use JavaScript for form validation and submission.

* **Post-Training Hub:** Everything on Reinforcement Learning from Human Feedback (RLHF) and LLM post-training now lives in [**one place**](https://rlhfbook.com/), with code examples at every stage.

* **Markdown Trap:** Don't make an LLM do work that plain code does faster, cheaper, and safer. This piece explains exactly when to [**reach for AI**](https://structural.chat/articles/programming-in-markdown/) and when to skip it.

* **Loop Engineering:** A former senior Amazon engineer shares when to stop hand-steering your coding agent and what's [worth automating.](https://rico.codes/loops-not-prompts)

* **AI Roadmap:** A complete [**path to LLMs**](https://x.com/ParamSiddh/status/2070180602964570402), agents, and MCP, built entirely from credible courses and open-source projects.

* **Agent Swarms:** Worktrees defer agent collisions, they don't fix them. A software architect shares his [**single-branch workflow**](https://davidwells.io/blog/multi-agent-coding-without-worktree-chaos) for running multiple coding agents without the chaos.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to stop Codex wasting time searching your codebase**

Codex often spends more time searching for code than actually writing it. In large repos, it triggers too many greps and reads the wrong files. This clogs the context with noise. 

To fix this, Morph launched WarpGrep. It is a search [subagent](https://www.morphllm.com/setup) that runs in its own context window. It returns only the specific file and line ranges Codex needs. You can install it with one command using your API key. 

```
npx -y @morphllm/morph-setup --morph-api-key YOUR_API_KEY
```
Choose Codex when prompted. Then get your API key. You can now ask broad questions like explain the auth flow. Codex uses WarpGrep to find the answer. 

It takes five seconds instead of seventy. Morph benchmarks show Codex scores three points higher on SWE-Bench Pro with this tool. It also works in Claude Code and Cursor. 

P.S. Get 50+ AI coding hacks for Claude Code, Cursor, and Codex [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/72f709e9-891d-44c9-99e6-b89424fb976a/Thumbnail__30_.jpg?t=1782454449)
Follow image link: (https://www.youtube.com/watch?v=5duo9qHw660)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to build a coding agent:**](https://www.youtube.com/watch?v=5duo9qHw660) You'll learn how to build a modular Python coding agent using a three-layer architecture. The tutorial shows you how to swap out LLM providers, manage stateless agent loops with stateful harnesses, and build a terminal user interface that supports real-time event streaming and custom coding tools.

———————————————————————————

### **Top Tool**

[BrowserAct:](https://www.browseract.com) A browser automation CLI designed for AI agents. It enables agents to open pages, read their state, click, type, and extract data.

———————————————————————————

### **Top Repo**

[**Ruflo**](https://github.com/ruvnet/ruflo)** (61.5K ⭐):** The leading multi-agent harness for Claude. Build and deploy autonomous workflows and conversational AI with adaptive memory, RAG, and native Claude Code integration. 

———————————————————————————

### **Trending Cookbook**

[**How agents are transforming work (by OpenAI):**](https://openai.com/index/how-agents-are-transforming-work/) Traditional chatbots usually only handle quick tasks, but the real impact of advanced AI agents on the workplace has been hard to pin down. This research paper shows that employees are quickly moving toward using agents for long-term projects, with non-devs leading the charge in expanding what they can do. 


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN CASE YOU MISSED IT**


--------------------
### ==**Our most-clicked story from yesterday**==

A GitHub director rebuilt her workday using 40 automations, which helped her become a more effective leader. She [published a guide](https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/) detailing each one and why it's essential. 


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 300K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/anthropic-accuses-alibaba-of-mass-distillation-attack-vercel-ships-ai-sdk-7
