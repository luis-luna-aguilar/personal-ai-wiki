---
title: Google drops Gemini 3.1 Flash TTS, Anthropic rebuilds its coding app
type: source
source_type: newsletter
url: https://codenewsletter.ai/p/google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app?_bhlid=74e0f25e11de2860e67ab30fb51e7973e2b0e201
fetched: 2026-04-16
---

# Google drops Gemini 3.1 Flash TTS, Anthropic rebuilds its coding app

**Welcome back.** Things in AI are getting pretty crazy. Allbirds (yes, the sneaker company) is selling off its shoe business and is pivoting into \*checks notes\* buying GPUs and renting them out to AI companies. The company’s stock price surged more than 5x on the move.

**Today:** Gemini’s new TTS model, 7 concepts behind senior backend interviews, a viral prompt that uses 8 subagents to fix messy code, and why Nvidia's CEO says chip restrictions are backfiring.

### **Today’s Insights**

* Powerful new updates and hacks for devs
* Why is Cloudflare rebuilding its CLI for agents
* Monitor deploys without leaving Claude Code
* Trending social posts, top repos, and more

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/d63aeac2-71d6-48c2-8f22-784af2cc49e8/Untitled_design__49_.jpg)](https://x.com/GoogleAI/status/2044447560384102592?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)

Click here to see Gemini 3.1 Flash TTS in action.

**Google unveils a speech model that acts on your cues:** The search giant just released **[Gemini 3.1 Flash TTS](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts/?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)**, a text-to-speech model that lets you use natural language prompts to control tone, pace, and delivery on the fly. It supports over 70 languages, native multi-speaker dialogue, and consistent character voices across scenes. Additionally, Google launched a native **[Gemini app](https://gemini.google/mac/?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)** for macOS. This Swift build was prototyped in just days using their Antigravity coding platform.

**OpenAI’s SDK gets serious about agent safety:** The ChatGPT maker just shipped major updates to its **[Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)**, giving enterprises a safer way to deploy automated helpers. A fresh sandbox integration isolates agents within controlled workspaces, limiting their access to only the files and code they need. The SDK also gains an in-distribution harness for frontier models, which should help tackle those complex, multi-step jobs that have proven notoriously tricky to automate.

**Anthropic rebuilds its coding app for parallel agents:** The AI lab just rebuilt Claude Code from the **[ground up](https://claude.com/blog/claude-code-desktop-redesign?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)**, centering it on a new split-pane interface. Developers can now handle several sessions at once using a sidebar that keeps tasks organized by project or current status. With built-in file editing, diff reviews, and a terminal, you'll rarely need to jump between different apps. That said, the rollout hasn't been perfectly smooth — senior engineer and T3 Chat CEO, Theo Browne, [reported](https://x.com/theo/status/2044680030706663726?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai) 40 bugs within just his first hour of use.

Booting a VM or configuring cloud services steals your focus. Provisioning, networking, secrets management…

[Exe.dev fixes tha](https://fandf.co/3PFGJXk?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)[t](https://fandf.co/3PFGJXk?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai) with instant VMs, persistent disks, and built-in HTTPS, so you can go from idea to running code in seconds.

Get 2 CPUs, 8 GB of RAM, and 25 GB of disk—shared across up to 25 VMs for $20/month.

##### **INSIGHT**

## **Why is Cloudflare rebuilding its CLI for agents**

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/9a8ffc34-d9ab-4405-ab05-bd407eb99899/superhumanteam_software_enginners_working_in_the_Cloudflare_o_ad8de9f2-62c1-4ca3-ac90-68ae2bad6608_3.jpg)

Source: The Code, Superhuman

**Agents outrank humans.** This week, Cloudflare **[announced](https://blog.cloudflare.com/cf-cli-local-explorer/?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)** they are rebuilding its Wrangler CLI from scratch, and the reason behind it is pretty significant. The company says AI agents are now the main users of its APIs, yet most of its 100+ products don't even have CLI commands.

**Where agents stumble.** Cloudflare’s main issue was that inconsistent CLI commands were breaking AI agents. While humans can navigate different terms like “get” or “info” for the same action, agents can't. To fix this, Cloudflare built a single schema to automatically generate every command, enforcing strict naming rules at the system level instead of relying on manual code reviews.

**They're not alone in this bet.** In early 2026, six major open-source projects [**launched**](https://ossinsight.io/blog/agent-native-cli-wave-2026?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai) with a focus on providing structured CLIs for AI agents. This approach is 10 to 32 times more cost-effective on tokens than MCP-based setups and significantly more reliable.

**No single winner.** Cloudflare still ships MCP servers, meaning even the company pushing hardest for CLIs isn't settling on just one method. The platforms that can adapt the fastest across all these standards will likely set the new bar.

##### **IN THE KNOW**

## **What’s trending on socials and headlines**

* **Prompt Prank:** The internet is increasingly being written for agents. Here’s one [hilarious example](https://x.com/venturetwins/status/2044087794176541138?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai) of a user prompt injecting a website to trick an agent.
* **Agent Academy:** Cursor's VP of Developer Education just dropped a 30-minute course on [**using coding agents**](https://cursor.com/learn/working-with-agents?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai) to plan features, squash bugs, and ship.
* **Huang's Warning:** On a recent podcast, Nvidia's CEO argued U.S. chip restrictions are doing the **[exact opposite](https://x.com/i/trending/2044472714283651440?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)** of what they were designed for.
* **Mac Mode:** An OpenAI Codex engineer **[shipped](https://x.com/dimillian/status/2041948910512652313?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)** a plugin that finally teaches the agent how native Mac apps should feel, not just compile.
* **Cleanup Crew:** This viral prompt spins up **[8 subagents](https://x.com/shawmakesmagic/status/2044269097647779990?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)** to fix everything wrong with a vibecoded codebase in one sweep.
* **The Seven:** One engineer claims 93.5% of senior backend interviews boil down to just **[7 core concepts](https://x.com/0xlelouch_/status/2044325606809317763?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)**.

##### **AI CODING HACK**

## **How to monitor deploys without leaving Claude Code**

You just kicked off a deploy, and now you're constantly switching tabs to see if it passed. Or maybe you're stuck watching a CI pipeline crawl through its stages while your Claude session sits idle. Instead, use the [/loop command](https://code.claude.com/docs/en/scheduled-tasks?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai) to run a recurring prompt in the background while you stay focused on your work. Just set a check to fire every five minutes:

```
/loop 5m check if the deploy succeeded and report back
```

The interval supports seconds, minutes, hours, and days. If you skip the interval, it defaults to 10 minutes. You can also loop other commands:

```
/loop 20m /review-pr 1234
```

Tasks are session-scoped and expire after three days, so you don't have to worry about a forgotten loop running indefinitely.

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/bf127501-661c-4b7a-be63-edd771a7eb42/Untitled_design__50_.jpg)](https://www.deeplearning.ai/short-courses/spec-driven-development-with-coding-agents/?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)

Click here to watch the tutorial.

### **Top Tutorial**

**[Spec-driven development with coding agents (by DeepLearning.AI):](https://www.deeplearning.ai/short-courses/spec-driven-development-with-coding-agents/?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)** This tutorial teaches developers how to build better software using AI coding agents. You'll learn to write clear markdown specs and project guides. This structured approach ensures your AI stays on track to build exactly what you want, even in older codebases.

### **Top Repo**

**[Gemini Scribe:](https://github.com/allenhutchison/obsidian-gemini?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)** An Obsidian plugin that integrates Google’s Gemini models to search, edit, and organize your vault files. It acts as an AI agent for developers, providing deep research with citations and IDE-style completions directly within your notes.

### **Trending Paper**

**Grow customers & revenue:** Join companies like Google, IBM, and Datadog. Showcase your product to our 240K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code?utm_campaign=google-drops-gemini-3-1-flash-tts-anthropic-rebuilds-its-coding-app&utm_medium=referral&utm_source=codenewsletter.ai)

### What did you think of today's newsletter?

Your feedback helps us create better emails for you!

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team
