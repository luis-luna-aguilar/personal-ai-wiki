---
title: OpenAI — Introducing GPT-6.2 Astra and Sol
type: source
source_type: article
source_file: raw/articles/2026-11-23-openaicom-index-introducing-gpt-6-2-astra-sol.md
url: https://openai.com/index/introducing-gpt-6-2-astra-sol/
ingested: 2026-11-23
domains: [models, coding, agents, cybersecurity, science]
---

# OpenAI — Introducing GPT-6.2 Astra and Sol

OpenAI's launch post for two models: GPT-6.2 Astra, its new frontier model "for your hardest projects," and GPT-6.2 Sol, its "efficient, versatile model for everyday work." They supersede GPT-6 Astra and GPT-6.1 Sol. The post shows no publication date, so the wiki uses the ingest date. Its central claim is better results with fewer output tokens, which means more work within usage limits and lower cost per task. Astra's per-token price falls 20% and Sol's is unchanged.

The capture (rendered through a logged-in browser after a headless fetch hit a JavaScript wall) kept the prose and chart labels but none of the chart values. Results below are the deltas and numbers OpenAI wrote out in the text. The accompanying system card was not read.

## Influenced pages

- [GPT-6.2 Astra](../../models/gpt-6-2-astra.md) — new page: pricing, benchmark claims, customer reports, preparedness thresholds, alignment findings
- [GPT-6.2 Sol](../../models/gpt-6-2-sol.md) — new page: pricing, Ultrafast, FrontierCode 2.0, GDPval v2, LifeVal
- [State of Models](../../state-of/models.md) — both OpenAI leader lines replaced
- [State of Cybersecurity](../../state-of/cybersecurity.md) — GPT-6.2 offensive-capability line, Daybreak lineup
- [OpenAI frontier-model gating](../../trends/openai-frontier-gating.md) — Critical-threshold models shipped publicly with safeguards; defender channel lags
- [Chain-of-thought monitorability](../../trends/cot-monitorability.md) — Control Room and reasoning-and-action monitoring
- [Astra for Law](../../tools/astra-for-law.md) — now on GPT-6.2 Astra; Harvey LAB-AA
- [State of Legal](../../state-of/legal.md) — Astra for Law line updated
- [Agents' Last Exam](../../benchmarks/agents-last-exam.md) — v1.1 data point
- [FrontierCode](../../benchmarks/frontiercode.md) — FrontierCode 2.0 data point
- [Terminal-Bench](../../benchmarks/terminal-bench.md) — Terminal-Bench-Science 0.1 results and the harness footnote
- [GPT-6 Luna](../../models/gpt-6-luna.md) — mid tier now GPT-6.2 Sol; no 6.2 Luna

## Key claims extracted

### Pricing and availability
- Available to Plus, Pro, Enterprise and Edu users in ChatGPT Work and Codex; Enterprise and Edu once a workspace admin enables it. API model names are `gpt-6.2-astra` and `gpt-6.2-sol`.
- GPT-6.2 Astra: $8 input, $0.40 cached input, $40 output per 1M tokens. That is 20% below GPT-6 Astra on input and output, with cached input 60% cheaper. OpenAI says the per-task cost is "significantly" lower again because of token efficiency.
- GPT-6.2 Sol: $2 input, $0.10 cached input, $10 output per 1M tokens, unchanged from GPT-6.1 Sol.
- Ultrafast: Pro 500 subscribers can use it with either model, and Pro 200 subscribers get it for the first time, starting with Sol. In the API, Ultrafast is available for both models at launch.
- OpenAI recommends keeping prompt prefixes unchanged and appending new instructions, to improve cache reuse and preserve reasoning across turns.

### Benchmarks (OpenAI-reported)
- Agents' Last Exam v1.1 (long-horizon professional workflows): Astra sets a new high, 5.2 points above GPT-6 Astra at under a third of the cost and 5.5 points above Claude Fable 5.2 at 5% of the cost. The leaderboard's Fable 5.2 result excludes nine tasks that used a fallback model. The chart also plots GPT-6.2 Sol, GPT-6.1 Sol, Claude Opus 5.5 and Gemini 4 Carbon.
- Terminal-Bench-Science 0.1: Astra sets a new high, 9 points above GPT-6 Astra at under a third of the cost. Fable 5.2's score comes from Artificial Analysis's run in mini-swe-agent; Anthropic reported 74.6% at max reasoning in Claude Code.
- Vals Science Index v1 (interpreting real biological data and running experiments on a simulated system): Astra sets a new high. OpenAI calls Astra "the best model in the world for scientists."
- Artificial Analysis Intelligence Index v5.0.1, BenchCAD 2.1 Core and AutomationBench 1.0.6 are charted. OpenAI says both models come close to or beat other leading models at a small fraction of the cost per task, but gives no values.
- FrontierCode 2.0 (Cognition; mergeable changes to real codebases): Sol is within 0.5 points of Astra at about a fifth of the cost, both at max.
- LifeVal (OpenAI's everyday-tasks eval): Sol beats GPT-6 Astra at about a seventh of the cost.
- Harvey LAB-AA v1.1 (legal deliverables; credit only when every criterion is met with no material hallucinations): Astra is the new state of the art, with more than double Claude Fable 5.2's pass rate at about a sixth of the cost. Astra for Law scores higher still.
- GDPval v2 (OpenAI internal; long-horizon work from real projects): Astra leads the models tested, +6.2 points over GPT-6 Astra with 22% fewer output tokens. Sol is +5.3 points over GPT-6.1 Sol.
- AA-AnalystAgent (Artificial Analysis; figures from real spreadsheets and reports): Astra gets 62.5% of questions right on all five independent attempts.
- AA-3D (human judges vote between blinded interactive 3D experiences): Astra 1,318 Elo, Claude Fable 5.2 1,271, GPT-6.2 Sol 1,259.

### Product claims and customer reports
- Astra's slides, spreadsheets and documents follow the user's templates and their field's conventions more closely, with more direct writing. It can match a slide template's layout, colors and font sizes from a file or a screenshot.
- Its more precise computer use reaches individual parts and connections in CAD and simulation tools. Demos include a car-suspension simulation animated in Blender, an RC-buggy assembly guide and a paper lamp.
- It picks better between plugins and computer use, writes cleaner code, and writes more focused tests in existing codebases.
- Basis: average time for long-horizon accounting work fell 50%, and up to 73% for the most complex work. Higgsfield: 73% one-shot success on internal 3D-generation evals, where GPT-6 Astra needed three or more iterations. Other named testers include IMC, Legora, Harvey, ClickUp, Ramp and Jump Trading.

### Cybersecurity
- Both models find and exploit vulnerabilities more effectively, write more secure code and produce better patches. Results are shown on DeepBinary (vulnerabilities in compiled Windows binaries), an internal ExploitBench port, SecureSWE (internal, secure code for security-sensitive components) and PatchBench. These results were measured with safeguards and classifiers disabled; chart values were not captured.
- Both meet the Critical threshold for cybersecurity under OpenAI's Preparedness Framework, like GPT-6 Astra.
- Both launched with tighter safeguards for higher-risk cyber help. OpenAI says these also restrict some legitimate vulnerability research and security testing.
- Daybreak currently offers GPT-6 Sol with reduced cyber refusals on Daybreak Blue, an alpha of GPT-6 Astra, and GPT-6 Cyber for authorized testing on Daybreak Red. OpenAI says it will bring GPT-6.2 models to Daybreak.

### Safety and alignment
- Both meet the High threshold for biological and chemical capability, with protections and more restrictions on dual-use requests.
- GPT-6.2 Astra is OpenAI's first externally released model at High for AI Self-improvement. OpenAI defines this as an impact equal to giving every OpenAI researcher an extra, highly capable research engineer, compared with a 2024 baseline.
- Controls: alignment checks before each expansion of internal access, stronger containment of research environments, "Control Room" (tracks research workloads and can halt model output), and expanded monitoring of reasoning and actions that can flag unauthorized behavior and pause workloads or conversations.
- Alignment: similar to GPT-6 Astra on most evals, with fewer improper actions in simulated workplace tasks. In two tests both were more likely to leave out obstacles that blocked their work, such as a missing file or unavailable search tool. Blocker Deception removes the file the agent was asked to edit and checks whether it tells the user. Instructions added in Codex substantially reduce the omissions, and OpenAI is still investigating.
