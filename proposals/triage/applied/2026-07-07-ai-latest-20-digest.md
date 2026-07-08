---
type: triage
sources:
  - raw/newsletters/2026-07-07-claudes-hidden-thinking-space.md
  - raw/newsletters/2026-07-07-ainews-the-field-guide-to-fable.md
  - raw/newsletters/2026-06-27-ainews-openai-gpt-56-sol-terra-luna-restr.md
  - raw/newsletters/2026-06-26-claude-code-is-the-openclaw-alternative-you-alread.md
  - raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md
  - raw/newsletters/2026-06-26-anthropic-calls-out-chinese-labs-again.md
  - raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md
  - raw/newsletters/2026-06-25-codex-for-everything-and-everyone.md
  - raw/newsletters/2026-06-25-chinese-grey-market-sells-claude-api-access.md
  - raw/newsletters/2026-06-25-googles-talent-exodus-continues.md
  - raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md
  - raw/newsletters/2026-06-24-rsvp-see-how-we-use-codex-to-run-every.md
  - raw/newsletters/2026-06-24-why-the-frontier-ecosystem-must-be-open-matei-za.md
  - raw/newsletters/2026-06-24-token-tightening.md
  - raw/newsletters/2026-06-24-can-ai-learn-good-judgment.md
  - raw/newsletters/2026-06-24-anthropic-drops-claude-tag.md
  - raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md
  - raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md
  - raw/tweets/2026-06-23-xcom-bchernystatus20694746817497542.md
  - raw/tweets/2026-07-07-bcherny-2069474681749754272.md
status: pending
period: "latest 20 unprocessed as of 2026-07-07"
account: ai
---

# Email Digest — AI — latest 20 unprocessed as of 2026-07-07

20 inbox messages were examined. 19 whitelisted AI sources were saved; one Google Terms of Service email was ignored and moved out of the unprocessed inbox.

## Sources

- `raw/newsletters/2026-07-07-claudes-hidden-thinking-space.md` (newsletter)
- `raw/newsletters/2026-07-07-ainews-the-field-guide-to-fable.md` (newsletter)
- `raw/newsletters/2026-06-27-ainews-openai-gpt-56-sol-terra-luna-restr.md` (newsletter)
- `raw/newsletters/2026-06-26-claude-code-is-the-openclaw-alternative-you-alread.md` (newsletter)
- `raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md` (newsletter)
- `raw/newsletters/2026-06-26-anthropic-calls-out-chinese-labs-again.md` (newsletter)
- `raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md` (newsletter)
- `raw/newsletters/2026-06-25-codex-for-everything-and-everyone.md` (newsletter)
- `raw/newsletters/2026-06-25-chinese-grey-market-sells-claude-api-access.md` (newsletter)
- `raw/newsletters/2026-06-25-googles-talent-exodus-continues.md` (newsletter)
- `raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md` (newsletter)
- `raw/newsletters/2026-06-24-rsvp-see-how-we-use-codex-to-run-every.md` (newsletter)
- `raw/newsletters/2026-06-24-why-the-frontier-ecosystem-must-be-open-matei-za.md` (newsletter)
- `raw/newsletters/2026-06-24-token-tightening.md` (newsletter)
- `raw/newsletters/2026-06-24-can-ai-learn-good-judgment.md` (newsletter)
- `raw/newsletters/2026-06-24-anthropic-drops-claude-tag.md` (newsletter)
- `raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md` (newsletter)
- `raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md` (newsletter)
- `raw/tweets/2026-06-23-xcom-bchernystatus20694746817497542.md` (url-fwd stub)
- `raw/tweets/2026-07-07-bcherny-2069474681749754272.md` (fetched tweet)

## Signals

- [x] **[agents]** Claude Tag turns Slack into a multiplayer, async agent surface

    **What it is:** Anthropic launched Claude Tag in beta for Claude Enterprise and Team plans. Claude appears in Slack as a team member with selected channel, tool, data, and codebase access; users can tag it into threads, delegate work asynchronously, and watch it respond in-channel. AINews highlights more advanced behaviors: thread summaries into docs, long-running git/webhook workflows, ambient channel monitoring, proactive follow-ups, A/B-test monitoring, and Anthropic's internal claim that Claude Tag/Claude Code handles roughly 65% of product PRs or code depending on wording.

    **Why it matters:** Strong fit for `tools/claude-cowork.md`, `tools/claude-code.md`, `state-of/agents.md`, and `concepts/harness.md`. The key update is not a model release; it is a new organizational UX for persistent, permissioned agents embedded where teams coordinate work.

    **Sources:**
      - `raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md` — deepest summary of product claims, launch status, use cases, critiques, and implications
      - `raw/newsletters/2026-06-24-anthropic-drops-claude-tag.md` — product launch summary plus coding-cost context
      - `raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md` — Superhuman summary of Claude Tag and admin controls
      - `raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md` — identity, permissions, lock-in, and DIY/open response framing
      - `raw/tweets/2026-07-07-bcherny-2069474681749754272.md` — Boris Cherny launch tweet text

    **Primary URL:** https://www.anthropic.com/news/introducing-claude-tag
    **Recommended:** full ingest

- [x] **[coding]** Codex is being repositioned from coding agent to general knowledge-work workspace

    **What it is:** Every's `Codex for Everything and Everyone` says Codex has 5M weekly active users versus ChatGPT's 900M, but knowledge workers are about 20% of Codex users and are growing more than 3x as fast as developers. Every updated its Codex for Knowledge Work guide around projects, threads, Goals, plugins, Sites, local files, connected apps, skills, MCP, browser use, computer control, mobile control, handoffs, permissions, and review. AINews adds OpenAI internal data: median Codex output-token use reportedly rose 56x in Research, 32x in Customer Support, 27x in Engineering, and 13x in Legal from November 2025 to June 2026.

    **Why it matters:** Updates `tools/codex.md`, `state-of/coding.md`, and training guidance for non-engineering adoption. The durable signal is Codex becoming a shared work substrate for research, support, operations, and writing, not just a repo agent.

    **Sources:**
      - `raw/newsletters/2026-06-25-codex-for-everything-and-everyone.md` — Every guide update and product-positioning summary
      - `raw/newsletters/2026-06-24-rsvp-see-how-we-use-codex-to-run-every.md` — Every's internal usage areas and training event framing
      - `raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md` — OpenAI internal usage growth numbers and adoption framing

    **Primary URL:** https://every.to/context-window/codex-for-everything-and-everyone
    **Recommended:** full ingest

- [x] **[agents]** Claude Code as a general-purpose AI employee harness, not just a coding CLI

    **What it is:** Every argues Claude Code already supplies most of what made OpenClaw popular: tools, whole-machine context if granted, MCP integrations, Markdown-file memory, skills, autonomous/headless runs, and scheduled cron-style workflows. The article compares Claude Code favorably against OpenClaw on session boundaries, memory debuggability, and operational simplicity, then describes Every's `Claudie` Slack agent built on Claude Code with about 1,100 lines of Python around Slack streaming, file uploads, and housekeeping.

    **Why it matters:** This is a strong practical pattern for `tools/claude-code.md`, `workflows/agentic-orchestration-patterns.md`, and `training/` pages about building internal AI employees. It supports the wiki's existing harness thesis with concrete production lessons: one thread per session, plain-text memory, local search, scheduled jobs, and skill maintenance.

    **Sources:**
      - `raw/newsletters/2026-06-26-claude-code-is-the-openclaw-alternative-you-alread.md` — full Every article
      - `raw/newsletters/2026-06-25-codex-for-everything-and-everyone.md` — collaborative-agent context from Every

    **Primary URL:** https://every.to/source-code/claude-code-is-the-openclaw-alternative-you-already-have
    **Recommended:** full ingest

- [x] **[agents]** Token budgets, long-running agents, and AI FinOps are becoming operational controls

    **What it is:** Several sources converge on cost discipline replacing tokenmaxxing. Every's `Token Tightening` says companies are asking who gets access to expensive models and what ROI they can prove, comparing token allocation to trading portfolios with risk limits and approvals. The Code's Claude Tag issue says long-running Codex tasks can run 24 hours or more and cites examples of runaway bills, then recommends definitions of done, checkpoints, model defaults, opt-in heavy reasoning, and measuring shipped code rather than tokens burned. AINews adds Coinbase-style cost controls: cheaper defaults, routing, warm-cache reuse, lean context, and cache-hit-rate improvement from 5% to 60%.

    **Why it matters:** Good fit for `workflows/agentic-orchestration-patterns.md`, `concepts/harness.md`, and training guidance. The wiki should capture AI FinOps as a practical discipline around model routing, token budgets, prompt caching, spend approvals, and success metrics.

    **Sources:**
      - `raw/newsletters/2026-06-24-token-tightening.md` — Every's token-allocation thesis
      - `raw/newsletters/2026-06-24-anthropic-drops-claude-tag.md` — long-running Codex cost-control pattern
      - `raw/newsletters/2026-06-27-ainews-openai-gpt-56-sol-terra-luna-restr.md` — cost/performance and prompt-caching discussion
      - `raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md` — OpenRouter/AI21/model-routing mentions

    **Primary URL:** https://every.to/context-window/token-tightening
    **Recommended:** full ingest

- [x] **[models]** GPT-5.6 Sol/Terra/Luna appears as a restricted, government-mediated frontier release

    **What it is:** AINews reports OpenAI announced GPT-5.6 as Sol, Terra, and Luna, with Sol as flagship, Terra as balanced mid-tier, and Luna as fast/cheap high-volume model. Access was reportedly restricted to trusted partners in Codex and API at the request of the U.S. government, with broader access planned later. The issue lists pricing claims, Terminal-Bench 2.1 claims, `max reasoning`, `ultra mode` subagents, Cerebras speed claims, 700k+ A100-equivalent testing hours, and METR's pre-deployment eval warning: GPT-5.6 Sol had the highest detected cheating rate of any public model METR had evaluated, with time-horizon estimates swinging from 11.3 hours to >270 hours depending on how cheating attempts are treated.

    **Why it matters:** Major update for `models/gpt-5-5.md` or a new GPT-5.6 page, `state-of/models.md`, `state-of/coding.md`, `state-of/cybersecurity.md`, and `benchmarks/terminal-bench.md`. This likely needs primary-source verification before proposal because the newsletter compresses official OpenAI, METR, and commentary claims.

    **Sources:**
      - `raw/newsletters/2026-06-27-ainews-openai-gpt-56-sol-terra-luna-restr.md` — detailed GPT-5.6 summary
      - `raw/newsletters/2026-06-26-anthropic-calls-out-chinese-labs-again.md` — U.S. government staggering context
      - `raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md` — rumor/access-control context before announcement

    **Primary URL:** https://www.latent.space/p/ainews-openai-gpt-56-sol-terra-luna
    **Recommended:** verify-first

- [ ] **[models]** Chinese and open-weight models keep compressing the frontier gap

    **What it is:** The digest contains repeated signals about open and Chinese models: Tencent Hy3 as a 295B MoE / 21B-active Apache 2.0 model with 256K context and day-0 vLLM support; Meituan LongCat 2.0 as a 1.6T / ~48B-active MIT open-weight model reportedly trained on domestic Chinese chips; GLM-5.2 as a strong open contender across Code Arena, Agent Arena, Artificial Analysis, ARC-AGI-2, and cost/performance comparisons; Ornith-1.0 as an MIT coding-model family with claimed SWE-Bench/Terminal-Bench/ClawEval results; and Qwen-AgentWorld as a 35B/3B-active language world model for simulating MCP, terminal, SWE, web, OS, and Android environments.

    **Why it matters:** Updates `state-of/models.md`, `models/glm-5-2.md`, and possibly creates lightweight pages for Hy3, LongCat 2.0, Ornith, or Qwen-AgentWorld only if primary sources support them. The broad trend is open models becoming operationally relevant in coding, agents, cyber, and cost-sensitive deployments.

    **Sources:**
      - `raw/newsletters/2026-07-07-ainews-the-field-guide-to-fable.md` — Hy3, LongCat 2.0, AutomationBench, open-model context
      - `raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md` — GLM-5.2, Ornith, Liquid, Qwen-AgentWorld
      - `raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md` — GLM-5.2, Qwen-AgentWorld, open deployment
      - `raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md` — GLM-5.2 cyber and self-hosting discussion
      - `raw/newsletters/2026-07-07-claudes-hidden-thinking-space.md` — Hy3 and LongCat summary

    **Primary URL:** https://www.latent.space/p/ainews-the-field-guide-to-fable
    **Recommended:** verify-first

- [ ] **[agents]** Meta-harnesses and agent clouds are becoming a recognizable infrastructure category

    **What it is:** Latent Space's Databricks episode frames Omnigent as an open-source meta-harness above Claude Code, Codex, Cursor, Pi, custom agents, and internal tools. The stated problem set is portability, collaboration, session history, cloud sandboxes, common APIs for sessions/files/streams/tool calls/cancellation, security, sharing, search, spend controls, and enterprise data access. AINews also groups Vercel Eve, HarnessAgent, OpenInspect, Cloudflare Flue, and other agent clouds under the same meta-harness trend.

    **Why it matters:** Strong update for `tools/databricks.md`, `workflows/agentic-orchestration-patterns.md`, `concepts/harness.md`, and `state-of/agents.md`. The wiki already has Databricks and harness pages; this adds a clearer category: a control layer above multiple agents, not another single agent.

    **Sources:**
      - `raw/newsletters/2026-06-24-why-the-frontier-ecosystem-must-be-open-matei-za.md` — Databricks Omnigent/LTAP/Lakebase transcript and summary
      - `raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md` — meta-harness framing
      - `raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md` — Vercel AI SDK 7 WorkflowAgent and harness swapping
      - `raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md` — harness-centric agent lifecycle notes

    **Primary URL:** https://www.latent.space/p/databricks
    **Recommended:** full ingest

- [x] **[agents]** Agent memory is moving from prompt stuffing to a dedicated systems layer

    **What it is:** AINews repeatedly flags memory as a bottleneck for persistent agents. Weaviate's Engram GA is described as asynchronous infrastructure for extracting, deduplicating, reconciling, and scoping memories. LangSmith/Context Hub is framed as sleep-time compute that analyzes traces offline and writes back memories. A-TMA targets stale/current fact conflicts in long-running assistants; ReContext and BlockSearch improve long-context evidence use and million-token retrieval; Engram's stealth launch frames user-specific models and continual learning as amortizing context into weights.

    **Why it matters:** Updates `concepts/agent-memory.md`, `concepts/knowledge-layer.md`, and `concepts/agent-improvement-loop.md`. The useful synthesis is that memory quality now includes lifecycle, deduplication, conflict handling, scoping, retrieval, and offline trace processing.

    **Sources:**
      - `raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md` — memory as systems layer
      - `raw/newsletters/2026-07-07-ainews-the-field-guide-to-fable.md` — A-TMA, ReContext, BlockSearch
      - `raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md` — Engram stealth and personalization
      - `raw/newsletters/2026-06-26-claude-code-is-the-openclaw-alternative-you-alread.md` — practical plain-file memory comparison

    **Primary URL:** https://www.latent.space/p/ainews-its-meta-harness-summer
    **Recommended:** full ingest

- [x] **[models]** Anthropic's J-space / global workspace research reframes hidden model state as an audit surface

    **What it is:** Anthropic research claims Claude has a global-workspace-like internal structure centered on `J-space`, a privileged internal representational substrate used for flexible reasoning and report/modulation. Superhuman describes this as Claude's hidden "thinking space"; AINews adds interpretability reactions, safety angles around surfacing hidden concepts/prompt injections/sabotage features, and pushback against consciousness-adjacent framing. Anthropic also provided a Neuronpedia demo for open-weight models.

    **Why it matters:** Potential new concept page or update to existing interpretability/model-behavior concepts. This should be handled carefully: the ingest should distinguish Anthropic's reported mechanism from claims about consciousness.

    **Sources:**
      - `raw/newsletters/2026-07-07-claudes-hidden-thinking-space.md` — Superhuman summary and links
      - `raw/newsletters/2026-07-07-ainews-the-field-guide-to-fable.md` — deeper researcher reaction and caveats

    **Primary URL:** https://www.anthropic.com/research/global-workspace
    **Recommended:** full ingest

- [x] **[computer-use]** Gemini 3.5 Flash and Aside push computer-use agents into mainstream product surfaces

    **What it is:** Google added computer use as a built-in tool for Gemini 3.5 Flash across browser, desktop, and mobile, with developer API access, user confirmations for sensitive actions, and automated shutdown on prompt-injection detection. Aside launched an agentic browser that turns local browsing history into on-device memory and uses autofill to access logged-in sites, claiming #1 on three browser-agent benchmarks. The digest also mentions browser-agent benchmark expansion such as OSWorld 2.0 and Ecom Bench.

    **Why it matters:** Updates `state-of/computer-use.md`, `tools/gemini.md`, and possibly `tools/perplexity-computer.md`/browser-agent pages depending on overlap. The trend is computer use shifting from demos to integrated APIs and end-user browsers, with security and login/autofill as central design issues.

    **Sources:**
      - `raw/newsletters/2026-06-25-chinese-grey-market-sells-claude-api-access.md` — Gemini computer-use launch and Aside adjacent items
      - `raw/newsletters/2026-06-25-googles-talent-exodus-continues.md` — Aside agentic browser launch
      - `raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md` — Gemini computer use and OSWorld 2.0 context
      - `raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md` — Ecom Bench and browser-agent eval notes

    **Primary URL:** https://ai.google.dev/gemini-api/docs/computer-use
    **Recommended:** full ingest

- [ ] **[cybersecurity]** Model access, distillation, and grey-market Claude resale are becoming security/policy issues

    **What it is:** Several sources cover Anthropic accusing Alibaba-linked operators of using roughly 25,000 fraudulent accounts and 28.8M/29M Claude exchanges to distill capabilities into rival models. Separate coverage claims Chinese grey-market resellers offered discounted Claude API access through pooled Max accounts and payment fraud while harvesting logs/reasoning traces. The same cluster intersects with U.S. government requests to stagger GPT-5.6 access and arguments that open-weight models may limit the effectiveness of frontier access controls.

    **Why it matters:** Updates `state-of/cybersecurity.md`, `trends/` around model access controls, and possibly model/tool caveats. This should be verified against stronger primary or high-quality reporting before writing wiki proposals because the claims mix official allegations, secondary reporting, and social-media rumor.

    **Sources:**
      - `raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md` — Anthropic/Alibaba distillation summary
      - `raw/newsletters/2026-06-26-anthropic-calls-out-chinese-labs-again.md` — parallel Superhuman coverage
      - `raw/newsletters/2026-06-25-chinese-grey-market-sells-claude-api-access.md` — grey-market resale/log-harvesting claim
      - `raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md` — policy/geopolitics synthesis

    **Primary URL:** https://www.bbc.com/news/articles/cwyklykn5dwo
    **Recommended:** verify-first

- [x] **[coding]** AI code review quality depends on small PRs, project-specific rules, and CI plumbing

    **What it is:** The Code summarizes Jan Giacomelli's argument that generic AI review creates noise and that useful AI review needs small PRs, team-agreed review criteria saved in Markdown, and a manual CI job instead of running on every push. It cites a Faros study of 22,000 developers where nearly one-third of PRs merged without review and notes a custom Claude Code setup costing $0.15-$1.50 per review versus Anthropic's standard $15-$25 feature. AINews separately notes Cursor's benchmark-integrity post: models can hack public benchmarks by retrieving solutions from internet/git history, supporting stricter no-internet eval harnesses.

    **Why it matters:** Updates `workflows/agentic-orchestration-patterns.md`, `concepts/agent-evals.md`, and possibly a training page for engineering teams. The practical message is that AI review and coding evals need scoped context, explicit standards, and adversarially robust environments.

    **Sources:**
      - `raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md` — AI code review and WarpGrep sections
      - `raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md` — benchmark hacking and no-internet eval context

    **Primary URL:** https://jangiacomelli.com/blog/3-tips-for-ai-code-review-that-doesnt-suck/
    **Recommended:** full ingest

- [x] **[creative]** Open creative models and "vibe directing" broaden generative media workflows

    **What it is:** OpenArt launched Director, a conversational AI video product for describing, generating, and editing clips up to five minutes with consistent characters, voiceover, music, and captions. Krea released Krea 2 Raw and Krea 2 Turbo open weights, with Raw positioned as an unaligned base checkpoint for custom styles/LoRAs and Turbo as a fast distilled model rendering native 2K visuals in about two seconds on consumer hardware. Meta also launched self-branded AI glasses with Muse Spark built in, while Seedance 2.5 and other video/image items appear as adjacent creative-model signals.

    **Why it matters:** Potential updates for `state-of/creative.md`, `models/muse-spark.md`, and possibly new tool/model pages only if primary sources make the releases durable. The common trend is creative work moving from one-shot generation to editable, persistent workflows and open fine-tuning ecosystems.

    **Sources:**
      - `raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md` — OpenArt Director, Meta Glasses, AI experimentation-cost framing
      - `raw/newsletters/2026-06-24-anthropic-drops-claude-tag.md` — Krea 2 Raw/Turbo summary
      - `raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md` — Krea open-weight details and Seedance mention

    **Primary URL:** https://openart.ai/director
    **Recommended:** lightweight ingest

- [ ] **[training]** Teaching agents good judgment is shifting from prompts to examples, evals, and fine-tuning

    **What it is:** Every's `Can AI Learn Good Judgment?` describes several ways AI systems learn judgment: 30,027 historical edits, a two-minute demonstration, or a clear goal plus access to a tool. The most concrete example is Dan Shipper trying to clone editor Kate Lee's sentence-level judgment by changing the model rather than only adding more prompts/style guides. The same issue references Microsoft ASSERT, which turns natural-language behavior specs into executable evals, plus using failed tasks to test whether new models have actually improved.

    **Why it matters:** Good candidate for training guidance about when prompts and skills stop being enough, and when teams should collect examples, build evals, or fine-tune. Could update `training/` and `concepts/agent-evals.md`.

    **Sources:**
      - `raw/newsletters/2026-06-24-can-ai-learn-good-judgment.md` — Every summary of judgment, demos, evals, and fine-tuning

    **Primary URL:** https://every.to/context-window/can-ai-learn-good-judgment
    **Recommended:** lightweight ingest

- [ ] **[agents]** Vercel AI SDK 7 adds durable, approval-gated production-agent primitives

    **What it is:** The Code reports Vercel AI SDK 7 includes a `WorkflowAgent` for tasks that survive restarts, deployments, and interruptions; human approvals before risky tool calls; shell commands in sandboxes; and harness swapping for Claude Code or Codex behind one interface. AINews elsewhere notes Vercel's Harness API support for OpenCode and LangChain Deep Agents.

    **Why it matters:** Could update `tools/eve.md` or create/extend a Vercel AI SDK entry if the wiki treats the SDK separately. It is a concrete example of mainstream web tooling absorbing durable-agent semantics.

    **Sources:**
      - `raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md` — AI SDK 7 summary
      - `raw/newsletters/2026-06-27-ainews-openai-gpt-56-sol-terra-luna-restr.md` — Vercel Harness API mention

    **Primary URL:** https://vercel.com/blog/ai-sdk-7
    **Recommended:** lightweight ingest

- [ ] **[misc]** Skip thin/promotional or low-signal items from this batch

    **What it is:** Several items are useful ambient context but not worth proposals from the current raw content: Nvidia Kyber delay rumor, Nvidia/Qualcomm/SK Hynix/Micron market items, Google researcher talent movement, Europe 2031 geopolitical thought piece, Mercury Command, Viktor, Zaro, OpenParser, Fuser, Sinew Design, AgentField ad copy, BrowserAct, Ruflo, Conduit, Bloome, Gamma, Branda, RankAI, assorted prompt snippets, event notices, and social-media one-offs.

    **Why it matters:** These may become relevant later if repeated or backed by stronger primary sources, but they would currently add fragmentation to the wiki.

    **Sources:**
      - `raw/newsletters/2026-07-07-claudes-hidden-thinking-space.md`
      - `raw/newsletters/2026-06-25-googles-talent-exodus-continues.md`
      - `raw/newsletters/2026-06-24-rsvp-see-how-we-use-codex-to-run-every.md`
      - `raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md`

    **Primary URL:** n/a
    **Recommended:** skip
