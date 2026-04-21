---
title: "⚡  Anthropic leaks Claude Code by accident"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-04-01
gmail_id: 19d495c73632897f
---

# ⚡  Anthropic leaks Claude Code by accident

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-04-01

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Anthropic just accidentally exposed Claude Code's source code. What was meant to be a routine update triggered an unexpected leak, and developers are already pulling apart what they found. It doesn’t get any bigger than this.

**Also:** How a veteran engineer reviews AI-generated code, an OpenAI engineer's guide to mapping the real agent stack, and Jack Dorsey's plan to cut middle management.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Inference engineering: the next big thing

* How to make Claude Code grill you before building

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/16227005-9f59-49cd-ae1b-434a2d72f448/superhumanteam_generate_a_portrait_image_of_the_person_in_omn_c503defe-afbe-402a-b70a-335a4095e58a_0.jpg?t=1775026384)
Caption: Made with Midjourney.


--------------------
**Anthropic exposes Claude Code’s source code by accident:** The AI lab accidentally leaked portions of its coding tool's internal [**source code**](https://x.com/i/trending/2038638312190316690) by including a map file in its latest npm release. They confirmed that no customer data or credentials were compromised, describing the incident as a developer error rather than a security breach. Claude Code creator Boris Cherny [**attributed**](https://x.com/bcherny/status/2039210700657307889) the leak to a manual deployment error and confirmed that the team is now automating the process to prevent future slip-ups.

**Developer rewrites leaked Claude Code from scratch overnight:** Following Anthropic's accidental source code leak, the lab rushed to issue DMCA takedowns across GitHub. That's when Korean developer Sigrid Jin **[stepped in](https://tech.yahoo.com/ai/claude/articles/anthropic-accidentally-leaked-claude-codes-180256954.html)**. Waking up at 4 AM, Jin rewrote the entire codebase in Python before sunrise and launched it as **[claw-code](https://github.com/instructkr/claw-code)**, making it the fastest repo ever to cross 50K stars. Since it's a clean-room rewrite, it remains protected from Anthropic's legal reach. 

**Google drops its most affordable AI video model yet:** The search giant just released [**Veo 3.1 Lite**](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/), a new video generation model available through the Gemini API and Google AI Studio. It matches the speed of Veo 3.1 Fast but costs less than half as much. The model handles both text-to-video and image-to-video prompts and features native audio, synced sound effects, and dialogue in either landscape or portrait at up to 1080p.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY AGENTFIELD**

## [Open-Source Harness Orchestration Is Here](https://agentfield.ai/github/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode_060401&utm_id=thecode-1-github-cta&utm_content=github-cta)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a83a3c3c-4b73-4ff4-88bb-571720cbf4c0/Github_thecode.jpg?t=1774944569)
Follow image link: (https://agentfield.ai/github/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode_060401&utm_id=thecode-1-github-cta&utm_content=github-cta)
Caption: 


--------------------
You run one Claude/Open Code instance at a time. These Open-Source repos coordinate 175 at once.

[AgentField](https://agentfield.ai/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode_060401&utm_id=thecode-1-home-cta&utm_content=home-cta) is open-source harness orchestration. One .harness() call spins up hundreds of Claude Code, Codex, or Gemini instances, they discover each other, split work, and converge on a verified result.

* 175+ Harness SWE team 

* 250+ deep agentic security scanner 

* 50+ adversarial deep code reviewers 

*  Or build your own

[We wrote up](https://agentfield.ai/blog/posts/beyond-vibe-coding/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode_060401&utm_id=thecode-1-bvc-cta&utm_content=bvc-cta) how it actually works, the failures, the fixes, the real costs.

**[Clone a Recipe](https://agentfield.ai/github/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode_060401&utm_id=thecode-1-github-cta&utm_content=github-cta)**


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Why inference engineering is becoming the next big discipline in engineering**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/893a96ec-ea1e-4628-bd83-447dc0f4e8ce/HB8bPCbaMAMQh-7__1_.jpg?t=1775015278)
Caption: Source: X/philipkiely


--------------------
**Open models closed the gap.** When Cursor [**shipped Composer 2**](https://techcrunch.com/2026/03/22/cursor-admits-its-new-coding-model-was-built-on-top-of-moonshot-ais-kimi/) last week, developers discovered it ran on Kimi K2.5, an open model from Beijing-based Moonshot AI. Cursor layered its own training on top and matched Claude Opus 4.6 on coding benchmarks at roughly one-tenth the token cost. That performance edge comes from inference engineering, the practice of optimizing how models actually run in production.

**A new field.** Three years ago, this field barely existed. Now, open models match proprietary ones within weeks. Philip Kiely, a developer advocate at Baseten, just published a [book](https://www.baseten.co/inference-engineering/) on the craft. Companies running their own stacks are seeing 80% cost savings while boosting uptime from 99% to 99.99%.

**Most teams aren't ready for it.** Owning your stack means managing GPU clusters, tuning quantization, and building efficient autoscaling. That requires a kind of engineer most companies haven't hired, because the role didn't exist at scale until recently.

**The talent pool is catching up.** Open models keep improving every few weeks, which means more companies are hitting the scale where self-hosting makes sense. And if you're spending six figures a month on closed model [APIs](https://newsletter.pragmaticengineer.com/p/what-is-inference-engineering) but still struggling with reliability, inference engineering is worth evaluating.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c588948e-7aff-4b32-9619-c2502a5dd730/CleanShot_2026-04-01_at_14.22.25_2x.jpg?t=1775033586)
Caption: Meme of the day.


--------------------
* **Under The Hood:** A developer went through Claude Code's entire source code. Turns out most people are only using [**about 10% of it**](https://x.com/mal_shaik/status/2038918662489510273) (1.1M views).

* **No More Managers:** Twitter founder Jack Dorsey just [**shared**](https://x.com/jack/status/2039003879841362278) Block's plan to replace middle management entirely with AI (2.2M views).

* **Dev Toolkit:** Most developers waste time on problems these 10 underrated **[websites](https://x.com/ennycodes/status/2038655225913913578)** already solve.

* **Code Patrol:** A senior engineer with 20+ years of experience [**breaks down**](https://www.youtube.com/watch?v=As2xy_cSx00) his 4-layer system for reviewing AI-generated code.

* **Build Here:** Sequoia revealed a map of every service industry ripe for [**AI agent takeover**](https://x.com/gregisenberg/status/2039125157134905517), totaling over $1T in opportunity.

* **Stack Map:** Everyone calls everything an "agent," but the systems behind that word are wildly different. An OpenAI engineer [**mapped**](https://www.linkedin.com/posts/vinothgovindarajan_the-agent-stack-part-1-a-systems-map-of-share-7444241370829017088-GP_F/) the actual stack.

* **Crypto Warning:** Google published a paper showing blockchain encryption is far more vulnerable to [**quantum computers**](https://x.com/projecteleven/status/2038807049262264502) than anyone thought.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to make Claude Code grill you before building**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/05684f3a-688d-457d-9659-ee96f3040f34/CleanShot_2026-04-01_at_10.12.25_2x.jpg?t=1775018601)
Follow image link: (https://www.aihero.dev/my-grill-me-skill-has-gone-viral)
Caption: 


--------------------
By default, Claude Code jumps straight into building. You describe a feature, it drafts a plan, and 20 minutes later, you're stuck with code that misses half your requirements. Ex-Vercel engineer Matt Pocock shared a three-line Claude Code skill called [/grill-me](https://www.aihero.dev/my-grill-me-skill-has-gone-viral) that solves this. Install it with one command:

```
npx skills@latest add mattpocock/skills/grill-me
```
Or create the file yourself at `.claude/skills/grill-me/SKILL.md`:

```
Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree resolving dependencies between decisions one by one.

If a question can be answered by exploring the codebase, explore the codebase instead.

For each question, provide your recommended answer.
```
Run `/grill-me` before you dive into a new feature. Claude Code will walk you through it one question at a time, suggesting answers where things are obvious and drilling down into the tough calls until your entire plan is airtight.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/15337bb1-af3d-4123-b93c-2577dc031267/Untitled_design__35_.jpg?t=1775025321)
Follow image link: (https://www.youtube.com/watch?v=2hoNAr-id-E)
Caption: 


--------------------
### **Top Tutorial**

[**How to fine-tune an LLM for structured data extraction:**](https://www.youtube.com/watch?v=2hoNAr-id-E) You'll learn how to fine-tune a small language model (Gemma 3) locally using Hugging Face. This end-to-end tutorial teaches how to format custom datasets, train a model to extract structured data, and deploy the final result as a live, interactive web demo.

———————————————————————————

### **Top Repo**

[**JSON parser:**](https://github.com/buger/jsonparser) This Go library lets you cut through messy JSON payloads in microseconds. It helps devs ship faster by turning dynamic APIs into simple byte-level lookups, making heavy optimization feel like a quick win.

———————————————————————————

### **Trending Paper**

[**Meta-Harness:**](https://x.com/yoonholeee/status/2038640635482456118) AI performance depends heavily on its surrounding code, or "harness," which is usually built manually because existing automated tools fall short. By letting an AI agent analyze past code and logs, researchers automatically generated harnesses that beat human-designed ones.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/anthropic-exposes-claude-code-source-code-google-drops-veo-3-1-lite
