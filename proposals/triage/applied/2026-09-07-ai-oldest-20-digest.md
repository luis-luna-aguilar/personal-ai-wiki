---
type: triage
sources:
  - raw/newsletters/2026-08-21-simulation-the-new-scaling-law-joon-sung-park.md
  - raw/newsletters/2026-08-22-the-evolution-of-the-agent-harness.md
  - raw/newsletters/2026-08-22-ainews-10-worse-100x-cheaper-10000x-faster-w.md
  - raw/newsletters/2026-08-23-life-after-automation.md
  - raw/newsletters/2026-08-24-i-tried-the-ai-model-built-to-fix-ai-writing.md
  - raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md
  - raw/newsletters/2026-08-25-benchmarks-dont-know-your-job.md
  - raw/newsletters/2026-08-26-we-have-foundation-models-for-language-not-for.md
  - raw/newsletters/2026-08-26-the-future-of-saas-is-apps-that-agents-can-use.md
  - raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md
status: pending
period: "oldest 20 unprocessed as of 2026-09-07"
account: ai
---

# Email Digest — Ai — oldest 20 unprocessed as of 2026-09-07

10 sources fetched (10 saved, 0 videos skipped). 9 further emails had no ingestible URL (X/tweet screenshots, video-only, GitHub repo link with no URL captured) and were skipped.

## Sources

- `raw/newsletters/2026-08-21-simulation-the-new-scaling-law-joon-sung-park.md` (newsletter)
- `raw/newsletters/2026-08-22-the-evolution-of-the-agent-harness.md` (newsletter)
- `raw/newsletters/2026-08-22-ainews-10-worse-100x-cheaper-10000x-faster-w.md` (newsletter)
- `raw/newsletters/2026-08-23-life-after-automation.md` (newsletter)
- `raw/newsletters/2026-08-24-i-tried-the-ai-model-built-to-fix-ai-writing.md` (newsletter)
- `raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md` (newsletter)
- `raw/newsletters/2026-08-25-benchmarks-dont-know-your-job.md` (newsletter)
- `raw/newsletters/2026-08-26-we-have-foundation-models-for-language-not-for.md` (newsletter)
- `raw/newsletters/2026-08-26-the-future-of-saas-is-apps-that-agents-can-use.md` (newsletter)
- `raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md` (newsletter)

## Signals

- [x] **[trends]** Simile's $2B round makes "simulate the human" the next synthetic-data frontier

    **What it is:** Simile AI (cofounded by Generative Agents/"Smallville" author Joon Sung Park) raised a $2B Series B (GreenOaks, Index, backed by Fei-Fei Li and Andrej Karpathy) to build "digital twins" — models post-trained on two-hour biographical interviews, transaction data, and registered randomized-controlled-trial data from the Open Science Framework — that reproduce a real person's survey and behavioral responses 85% as accurately as the person reproduces their own answers two weeks later. Frontier chat models manage only 20-60% on the same replication task, because they're trained to be rational/agentic rather than to copy human bias and inconsistency. Customers (CVS, Wealthfront, Gallup, Deloitte) use it for concept testing, focus-group replacement, and earnings-call simulation at the population level. A same-week AINews piece frames this as "Stage 7" of a broader pattern it traces back to 2022: judges, training data, teachers, curricula, researchers, and RL environments have each gone synthetic in turn, and the human "subject" (preferences/behavior/demand) is next — with the physical world (wet-lab science) the one stage that resists full synthesis.

    **Why it matters:** No existing wiki page covers AI-simulated human populations/digital twins as a category; this is a well-sourced, multi-signal candidate for a new concept or trend page, with the "synthetic-everything" framing as useful connective tissue to existing coverage of synthetic data / RLVR / agent environments.

    **Sources:**
      - `raw/newsletters/2026-08-21-simulation-the-new-scaling-law-joon-sung-park.md` — Latent Space podcast transcript with Joon Sung Park
      - `raw/newsletters/2026-08-22-ainews-10-worse-100x-cheaper-10000x-faster-w.md` — AINews "synthetic-everything" framing essay, cites Simile as Stage 7

    **Primary URL:** https://www.latent.space/p/simile
    **Recommended:** full ingest — new page

- [x] **[agents]** The agent harness keeps compounding: co-evolution theory, self-modifying harnesses, and enterprise MCP auth

    **What it is:** A Latent Space essay argues model and harness capability have been racing each other since 2022 (ReAct → AutoGPT's premature autonomy → Cursor's human-in-the-loop retreat → Claude Code's "curves cross" moment in Feb 2025), and that the harness now absorbs capability from the model in a repeating train→absorb→shed cycle (Anthropic reportedly deleted 80% of Claude Code's system prompt as the model absorbed what it used to specify). Concretely: Harness-Bench found a 23.8-point swing (52.4→76.2) running the same model through different harnesses on the same 106 tasks, and OpenAI tripled GPT-5.6 Sol's ARC-AGI-3 score (13.3%→38.3%) via harness changes (retained reasoning + compaction) alone. The same week, AINews reports NVIDIA proposing a "Skill Lift" metric (measuring task-completion delta with/without a skill, since structural skill checks barely predict usefulness — Spearman ρ=0.14), two new open-source "self-modifying" agent harnesses (Headlong: persistent/continuously-thinking agents with DAG-based trajectory storage; exo: recursive self-improvement with append-only event logs and rollback-safe sandboxes), a position paper arguing enterprises should standardize on one harness rather than bespoke orchestration graphs, and Anthropic's enterprise-managed auth for MCP connectors (centralized via org identity provider, no more per-tool OAuth).

    **Why it matters:** Directly extends [concepts/harness.md](../../wiki/concepts/harness.md), which already tracks the "harness matters as much as the model" thesis and managed-agent platform primitives.

    **Sources:**
      - `raw/newsletters/2026-08-22-the-evolution-of-the-agent-harness.md` — Latent Space essay, "Harness 1.0/2.0/3.0" framing
      - `raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md` — AINews harness/persistent-agent/MCP roundup

    **Primary URL:** https://www.latent.space/p/attention-interface
    **Recommended:** full ingest

- [x] **[models]** DeepSeek-V4-Flash-Vision-Exp adds multimodal input, claims near-Opus-4.8 agent performance

    **What it is:** DeepSeek shipped DeepSeek-V4-Flash-Vision-Exp, adding multimodal (text+image) input to V4-Flash while reportedly preserving its text capability. Benchmarks per AINews: 83.9 Terminal-Bench 2.1, 75.9 Toolathlon-Verified, 64.3 Chartography — a large jump over the prior V4-Flash-0731 release, positioned as closing the multimodal-agent gap to Opus-4.8. Ships with mixed text+image API support (up to 384 tokens/image at Flash pricing) and a new Files API for reusable image uploads. Weights not yet found on Hugging Face at time of writing — appears API-only for now.

    **Why it matters:** [models/deepseek-v4.md](../../wiki/models/deepseek-v4.md) exists and is due an update; this is a concrete version/capability bump.

    **Sources:**
      - `raw/newsletters/2026-08-22-ainews-10-worse-100x-cheaper-10000x-faster-w.md`

    **Primary URL:** https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x
    **Recommended:** lightweight ingest

- [x] **[training]** Andrew Ng relaunches DeepLearning.AI around four "AI Engineering" skills

    **What it is:** Andrew Ng (Google Brain/Coursera cofounder) relaunched DeepLearning.AI's focus on "AI Engineering," based on analysis of 10,000+ job postings plus structured interviews with hiring managers and recruiters. He names four core skills: (1) building/deploying AI applications — LLMs, context engineering, RAG, agentic workflows, disciplined evals/error-analysis loops; (2) software engineering fundamentals — architecture/tradeoff judgment that separates good delegators from vibe-coders who don't know what context to give their agent; (3) using coding agents effectively — mental models for agent limits, when to write a spec vs skip one, multi-agent orchestration, guardrails against costly mistakes; (4) shaping the build — product sense, business context, knowing when to ship an MVP vs slow down.

    **Why it matters:** A named, evidence-gathered (job-posting analysis) skills taxonomy from a well-known educator; no existing wiki page names this taxonomy directly, though it's adjacent to the wiki's `training/` guidance on delegation and evals.

    **Sources:**
      - `raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md`

    **Primary URL:** https://www.latent.space/p/ainews-andrew-ng-gets-into-ai-engineering
    **Recommended:** lightweight ingest

- [x] **[training]** Cost-normalized benchmarks and open-weight adoption data both point the same way: intelligence is outpacing the need for it

    **What it is:** Two data threads converge on a "diminishing returns on frontier intelligence for typical work" narrative. Cost-normalized agent benchmarks: Together AI found GLM-5.3 completes 5x more DeepSWE work than Fable 5 under a fixed $100 budget (~17 vs ~3 solved tasks) despite similar first-try quality; GPT-5.6 Sol Max scored 72.7% on DeepSWE v1.1 for $6.47/task vs Fable 5 Max's 69.7% for $21.63/task; Cline found Ox Alpha solved a real bugfix using ~3x fewer output tokens than Fable. Separately, Every's own data shows Fable — "the most capable model on the market" — is barely used: 6% of Anthropic tokens purchased and 11% of model spend a month after launch, largely because it lacks a zero-data-retention option many enterprises require; Every's head of tech consulting reports getting "no relative gain from Fable on 80 percent" of knowledge-work tasks. Meanwhile open-weight models' share of tokens routed through Vercel's AI Gateway rose from 11% to 29% in two months (per Ramp/Vercel data cited by Every), though still under 4% of spend — high-volume, low-stakes work is already migrating to cheaper models.

    **Why it matters:** Directly extends [training/cost-aware-ai-task-routing.md](../../wiki/training/cost-aware-ai-task-routing.md) (routing decisions by cost/risk) and [trends/open-weight-momentum-broadens.md](../../wiki/trends/open-weight-momentum-broadens.md) (open-weight share growth), both recently updated in the prior digest.

    **Sources:**
      - `raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md` — cost-normalized DeepSWE/Cline data
      - `raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md` — Fable adoption data, Vercel Gateway open-weight share

    **Primary URL:** https://every.to/context-window/the-case-for-cloning-your-coworkers
    **Recommended:** full ingest

- [x] **[training]** "Benchmarks don't know your job": the case for task-specific evals over leaderboard-chasing

    **What it is:** Mercor CEO Brendan Foody and Box CEO Aaron Levie argue companies spending tens of millions on AI without offline evals (a fixed set of real internal tasks used to compare models before they touch live work) are flying blind — public leaderboards say a model is more capable, not whether it caught the clause your lawyers care about or matched your house style. Every's own KateBench (an AI copyeditor trained on ~30,000 of its editor-in-chief's past edits, run inside Google Docs) illustrates the trap: it looks like an 85-90% acceptance rate, but that number was inflated by a silent cap that discarded suggestions past the 40th, and the acceptance rate itself is noisy run-to-run since the model doesn't produce identical edits twice. Two new benchmarks reinforce the caution: CentaurBench found the model best at solo task completion often isn't the best at improving a weaker model's first attempt (true on 5 of 7 tasks); Thinkingbox found the strongest coding model's 65% single-attempt pass rate fell to 25% when required to perform reliably across 20 consecutive attempts.

    **Why it matters:** Concrete evidence and a worked example for [training/evals-for-agentic-work.md](../../wiki/training/evals-for-agentic-work.md) (task-specific metrics, pass^k reliability) and [concepts/agent-evals.md](../../wiki/concepts/agent-evals.md).

    **Sources:**
      - `raw/newsletters/2026-08-25-benchmarks-dont-know-your-job.md`

    **Primary URL:** https://every.to/context-window/benchmarks-don-t-know-your-job
    **Recommended:** full ingest

- [x] **[training]** Self-improving agent skills as a personal workflow habit, not just a team process

    **What it is:** Every's head of operations Arielle Shipper runs a "self-improve" Codex skill: whenever the agent makes a mistake, she feeds it feedback on what went wrong and what a better response would have looked like, then runs the skill, which reviews the failure and proposes a targeted edit to Codex's own instructions so the mistake is less likely to repeat (e.g. adding a rule to always re-read thread context before drafting a Slack message). This is the same compounding mechanism behind Every's KateBench/DanLens skills (Codex rewrites the skill based on which suggestions get accepted vs. rejected), but framed here as something one person runs on their own workflow rather than a team-wide skill library. The skill itself is published on GitHub.

    **Why it matters:** A concrete "codify production failures as standing instructions" pattern (already principle #4 on [training/agent-skill-methodology.md](../../wiki/training/agent-skill-methodology.md)) turned into a reusable self-service loop — worth a line as a named proven pattern.

    **Sources:**
      - `raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md`

    **Primary URL:** https://github.com/arielleshipper/every-thing/tree/main/skills/self-improve
    **Recommended:** lightweight ingest

- [x] **[agents]** Lovable pivots from app builder to "company brain": SaaS becomes agent-callable capabilities via MCP

    **What it is:** Lovable (AI app-building platform, $13.3B valuation after a $400M Series C, >$500M ARR, 60M+ projects created) is repositioning around "capabilities" — discrete functions from a published app exposed as tools through a hosted MCP server, so an agent (from ChatGPT, Claude, or elsewhere) can call the function directly instead of a human opening the app. Credentials are held server-side by Lovable's connector gateway (never exposed to the generated app or its code) and each user's app-level permissions are preserved via short-lived scoped keys. Lovable CTO Fabian Hedin frames the end state as a single "company brain" agent per organization that orchestrates many such capabilities, deliberately avoiding the word "agent" for the whole because it implies an employee-replacement framing rather than a context/capability-connection one. Vercel (@𝚟) is building a similar internal-agent concept; Hedin argues Lovable's edge is being the best place to build the capabilities themselves, not the orchestration layer.

    **Why it matters:** A concrete, funded example of the "MCP turns SaaS into agent-callable tools" pattern that [concepts/mcp.md](../../wiki/concepts/mcp.md) already tracks abstractly — this gives it a named, large-scale case study.

    **Sources:**
      - `raw/newsletters/2026-08-26-the-future-of-saas-is-apps-that-agents-can-use.md`

    **Primary URL:** https://www.latent.space/p/lovable-future-of-saas
    **Recommended:** lightweight ingest

- [ ] **[misc]** Walleye Capital: mandatory AI fluency at a $10B hedge fund

    **What it is:** Every's AI & I podcast revisits a conversation with Walleye Capital CEO/CIO Will England, who has made AI use mandatory for all 400 employees. England sent a firm-wide email opening with "I used ChatGPT to write this email, you should be using it too, and be proud of it," arguing results matter more than manual effort and that ignoring AI tools in 2026 is like refusing to use the internet in 1995.

    **Why it matters:** A concrete, named "mandatory AI adoption" data point for [training/ai-delegation-management.md](../../wiki/training/ai-delegation-management.md)'s evidence-from-practice section.

    **Sources:**
      - `raw/newsletters/2026-08-26-the-case-for-cloning-your-coworkers.md`

    **Primary URL:** https://every.to/on-every/introducing-ai-i
    **Recommended:** lightweight ingest

- [ ] **[?]** Deft: a writing-focused model built to fix "AI sameness" — mixed early results

    **What it is:** New research lab Deft (cofounded by Justin Murphy and an AI researcher going by "Rosmine") released DFT v1, trained with a custom "distribution fine-tuning" method that compares batches of model output against batches of human writing (rather than grading one response at a time) to reduce repetitive AI phrasing patterns. Every's review found the output measurably less predictable/more "surprising" at the sentence level, but also denser, harder to parse, prone to inventing unrequested details even in "strict" mode, and with a limited API (sends jobs to Deft's system rather than allowing iterative collaboration). Verdict: a promising demonstration that AI-prose sameness is a tractable training problem, but not yet a usable writing tool.

    **Why it matters:** Niche, single-source, unproven lab and product; no existing wiki page tracks AI-writing-quality tooling specifically.

    **Sources:**
      - `raw/newsletters/2026-08-24-i-tried-the-ai-model-built-to-fix-ai-writing.md`

    **Primary URL:** https://every.to/working-overtime/i-tried-the-ai-model-built-to-fix-ai-writing
    **Recommended:** skip — thin, single-source, no durable wiki fit

- [ ] **[?]** Physics foundation models remain data-starved and resistant to token-scale approaches

    **What it is:** Caltech's Anima Anandkumar discusses Neural Operators (combining data with physical laws to model functions across scales rather than fixed grids), used in her FourCastNet weather models (competitive with physics-based simulation, runs on consumer GPUs) and in fusion-plasma disruption prediction (a few thousand samples predict disruptions ~1,000,000x faster than simulation). Her argument: physical systems (weather, fusion, fluid/heat flow) resist the transformer/scaling playbook because required context length would run into the hundreds of billions to trillions of tokens — progress here comes from building in structure (inductive biases, physical priors), not more data or compute. Also covers TorchLean (formally verifying PyTorch-style networks inside the Lean proof assistant).

    **Why it matters:** No existing wiki page tracks AI-for-physical-science; interesting but narrow research-lab content with no clear near-term reader action.

    **Sources:**
      - `raw/newsletters/2026-08-26-we-have-foundation-models-for-language-not-for.md`

    **Primary URL:** https://www.latent.space/p/anima
    **Recommended:** skip — niche research content, no clear wiki fit at present
