---
title: "👀  Grok gets 21 new voices"
type: newsletter
sender: "The Code <superhumancode@news.codenewsletter.ai>"
received: 2026-07-07
gmail_id: 19f3cc6b56f97a26
---

# 👀  Grok gets 21 new voices

**From:** The Code <superhumancode@news.codenewsletter.ai>
**Date:** 2026-07-07

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1c2a8c3a-f6dd-4d57-9db2-17314511805f/Group_Wispr__4_.jpg?t=1783408825)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 

----------
**Welcome back.** Your team’s Claude Code bill keeps climbing, and everyone's advice is the same: shorten your chats or switch to a cheaper model. Turns out that's mostly wrong. The real money is leaking from a spot that's practically invisible. In today’s issue, we explore what is going wrong and how your engineering team can fix it.  

**Also:** Loop engineering masterclass by Anthropic, what’s at the center of Claude’s mind, and 6-phase AI programming workflow of a senior engineer


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0fa61cdd-6f8b-4738-949b-d2599badaf02/image__89_.jpg?t=1783412002)
Caption: CEO of SpaceX Elon Musk.


--------------------
**Grok's voice gets 21 new personalities:** SpaceXAI, the freshly renamed home of Elon Musk's AI work, just gave Grok Voice a major boost. The lab dropped 21 multilingual voices spanning 25+ languages, each tuned for a specific job like customer support, education, or storytelling. Speech tags like [pause] and [whisper] let you shape delivery, and you can clone your own voice from about a minute of audio. [Try it here.](https://x.ai/news/new-flagship-voices)

**China's open models undercut US rivals on price:** The pressure from China keeps mounting. Meituan open-sourced [LongCat-2.0](https://longcat.ai/blog/longcat-2.0/), a 1.6-trillion-parameter coding model it claims is the first of its scale trained end-to-end on 50,000 Chinese chips, not Nvidia GPUs. Tencent followed yesterday with [Hy3](https://hy.tencent.com/research/hy3), a 295B-parameter model it says matches flagships two to five times its size. Both arrive as cheap, capable rivals to US models, and both underscore China's push to cut its reliance on American silicon.

**OpenAI researcher says data is AI's real bottleneck:** One of Sora's core creators just [published](https://x.com/willdepue/status/2074178395462848800) an essay arguing that compute isn't what's holding AI back anymore, but data is. Will Depue says labs are burning through the roughly 300 trillion tokens of quality public text on the open web, and he figures they'll spend north of $100B a year on private data by 2030. His fix? A "Stargate for data" — a moonshot effort to go collect everything models still can't learn.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [Cursor for code. Claude for thinking. What about input?](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/13d5232a-6915-4299-bff5-9790bfc68f52/Stats_Graphic_V2__1___1___1_.jpg?t=1783409312)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
==Your dev stack got an AI upgrade everywhere except the input layer. You're still typing every prompt, every ticket, every review comment by hand.==

==[**Wispr Flow**](https://ref.wisprflow.ai/thecode)==== closes that gap. Dictate into Cursor, VS Code, Slack, Linear, or anywhere else you work. It's syntax-aware: camelCase, snake_case, acronyms, and file names all come through clean. Mention a file in Cursor or Windsurf, and it auto-tags.==

==[**It's the voice layer for an AI-native workflow**](https://ref.wisprflow.ai/thecode)====. Speak your intent. Your tools do the rest.==

==Available on Mac, Windows, iPhone, and Android. Used by millions of developers, including teams at OpenAI and Mercury.==

==[**Try free**](https://ref.wisprflow.ai/thecode)==


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **What's really driving your Claude Code spend and how to fix it**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f85fd583-65bb-4332-8035-dc9d40c1d326/superhumanteam_a_software_engineering_team_made_of_archaic_hu_6c33cd6a-ce8a-4520-884b-b515a0a99d71_2.png?t=1775560107)
Caption: Source: The Code, Superhuman


--------------------
**The bill nobody planned for.** Claude Code costs are climbing, and the usual advice is to keep chats short or drop to a cheaper model. A [viral post ](https://www.comet.com/site/blog/claude-code-context-bloat)from Comet’s Head of Product, Jacques Verre, claims that you’re losing money the second a session starts, even before you've typed out a single prompt.  

**Understanding the problem.** Every MCP server, skill, and memory file loads the moment a session begins. GitHub's official MCP server alone [burns through](https://getunblocked.com/blog/github-mcp-token-cost/) roughly 42,000 tokens on tool definitions. So you just wasted about 20% of the context window before even starting out. Multiply that across unaudited connectors, and teams are paying rent on setups they stopped using.

**Caching softens the blow, with a catch.** Claude Code caches that startup context automatically, re-reading it at roughly a tenth of the normal rate. But cached tokens still crowd the window, and Anthropic's own testing shows accuracy drops when models wade through tools they don't need.  To fix this, you can lean on [Tool Search](https://www.anthropic.com/engineering/advanced-tool-use) from Anthropic. It loads definitions only when needed, cutting token usage around 85% in internal tests.

**You need more visibility.** The context command covers one session and often miscounts, while the console shows only a grand total — so teams are turning to org-level dashboards like Opik or Helicone. Before signing up, it's worth reading [how caching shapes the bill](https://code.claude.com/docs/en/prompt-caching) and auditing what a default session loads. The numbers usually surprise.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2e8e9adf-b691-4a7d-b596-ccb13aff20cf/image__86_.jpg?t=1783404019)
Caption: Meme of the day.


--------------------
* **Loop Engineering Masterclass:** The Anthropic team explained how to stop prompting your agent and [start designing loops](https://x.com/ClaudeDevs/status/2074208949205881033) instead, with four patterns for hands-off work (2 million views).

* **Fable Field Guide**: An Anthropic engineer laid out a [four-part playbook](https://www.youtube.com/watch?v=9fubhllmsBU) for working with Fable, the company's newest class of model. It starts with "unhobbling Claude" (2K interactions).

* **Agent Economy:** This thread lays out [21 startups](https://x.com/gregisenberg/status/2074127490109350221) built entirely for AI agents and calls it the decade's biggest opportunity (5K interactions).

* **Extracting Fable:** Since Fable 5 comes off subscription plans tonight, this viral thread teaches ["extracting" Fable 5](https://x.com/EXM7777/status/2074174041397813368) into any cheaper model, with five workflows (2K interactions).

* **Codex Confessions:** An OpenAI PM shares how Codex reshaped [his entire workflow](https://www.youtube.com/watch?v=fAdFE7y6K2o), including one habit that sounds almost absurd.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/507cddd2-af2d-4323-a808-82bc37822e98/Black_and_Green_Modern_Finance_Business_Report_Presentation__13_.jpg?t=1783404485)
Follow image link: (https://www.youtube.com/watch?v=Aie0nYktsNA)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

**[6-phase AI programming workflow of a senior engineer:](https://www.youtube.com/watch?v=Aie0nYktsNA)**** **In this tutorial, you will learn to effectively structure data, define interfaces, and implement code using LLMs, ultimately achieving a streamlined process to build games and applications more efficiently.

———————————————————————————

### **Top Tool**

**[AnySearch:](https://www.anysearch.com/home)** AI agents are only as good as the data they can access. By connecting to AnySearch, your agent leverages filtered, de-duplicated, and structured info from trusted sources in parallel, ensuring significantly more reliable outputs.  

———————————————————————————

### **Top Repo**

**[Improve (7K interactions):](https://github.com/shadcn/improve)**** **Since Fable 5 comes off subscription plans tonight, you should take advantage of this skill to have your most powerful model audit your codebase and map out plans for cheaper models to carry out. 

———————————————————————————

### **Trending Paper**

**[What’s at the center of Claude’s mind (by Anthropic):](https://www.anthropic.com/research/global-workspace)**[ ](https://www.anthropic.com/research/global-workspace)The AI lab found that Claude often works through concepts without writing them directly in its chain of thought, much like how a person might think about one topic while doing something else. The structure, called the J-space, formed unintentionally during training and now helps power Claude’s higher-level reasoning. 


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to reuse your Claude Code skills in Cursor**

Every skill you built for Claude Code goes to waste in Cursor. This means you have to reteach the same workflows every single session. It turns out SKILL.md is an open standard, and Cursor can read those same files from its own directory. Just copy your project skills over like this:  

```
cp -r .claude/skills .cursor/skills
```
Cursor finds them right when you start your session. If your project is already open, reload the window (Cmd/Ctrl+Shift+P → Reload Window) to pick them up. 

Don't have any skills yet? The [awesome-cursor-skills](https://github.com/spencerpauly/awesome-cursor-skills) repo has a list of ready-made ones. 

Since they all use the same format, anything you find there will work in Claude Code and Codex CLI as well.

P.S. Get 50+ AI coding hacks for Claude Code, Cursor, and Codex [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN CASE YOU MISSED IT**


--------------------
### ==**Our most-clicked story from yesterday**==

**Career Rethink:** An ex-OpenAI researcher lays out the _**[skills](https://x.com/philhchen/status/2072793818945167475?utm_source=codenewsletter.ai&utm_medium=newsletter&utm_campaign=alibaba-bans-staff-from-using-claude-code-viral-pixel-hack-splits-the-ai-dev-community&_bhlid=a0dad2a8f7536ecbbe90412b3f913ef11fb91d71)**_ that will actually matter for engineers over the next decade. Most of them aren't taught anywhere (3 Million Views).


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 300K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/grok-s-voice-gets-21-new-personalities-china-s-open-models-undercut-us-rivals-on-price
