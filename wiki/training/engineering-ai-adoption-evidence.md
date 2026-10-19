---
title: "Engineering AI adoption: evidence from practice"
type: training
domains: [coding]
as_of: 2026-09-14
sources: [shopify-latent-space-april-2026, ramp-ai-adoption-playbook, garrytan-gstack-repo, lennysan-simonw-interview, agentic-coding-trap-may-2026, stanford-labor-june-2026, shopify-claude-code-bessemer-2026-05, github-kyle-daigle-june-2026, ainews-june-05-2026, cognitioncom-blog-ai-productivity, bun-rust-rewrite-2026-07-16, openais-new-model-for-cyber-attacks-2026-07-16, anthropic-ci-test-impact-analysis-2026-09-14]
---

# Engineering AI adoption: evidence from practice

Case studies and data behind [AI enablement — software development](ai-enablement-software-development.md)'s guidance: specific engineering organizations, practitioners, and large-scale rewrites, as opposed to the cross-functional company cases on [AI adoption: evidence from practice](ai-adoption-evidence.md).

## Company-wide adoption case studies

- Shopify (April 2026, Latent Space podcast, Mikhail Parakhin): near-100% daily active AI tool adoption, with a December 2025 inflection where small model-quality improvements compounded into a phase change rather than a gradual linear improvement. CLI-first tools (Claude Code, Codex, internal River agent) growing faster than IDE tools (Cursor, Copilot). 30% month-on-month PR merge growth has shifted the main bottleneck from code generation to CI/CD, test failures, and deployment rollback
- Shopify built its own PR review tool because no external tool spends enough compute on expensive models during review — a signal that review quality is the next frontier
- Shopify's internal systems: Tangle (content-addressed ML workflow engine, dev→prod in one click), Tangent (auto-research agent loop that democratizes ML experimentation to PMs), SimGym (customer simulation on historical data, targeting 0.7 correlation with add-to-cart events as a proxy eval for product changes)
- Ramp: 84% of employees using coding agents weekly; 1,500+ apps shipped in six weeks by 800+ builders; non-engineers account for 12% of human-initiated PRs — `Dojo` skills marketplace is a key driver of the non-engineer coding adoption

## Practitioner patterns and critiques

- Garry Tan (YC CEO, April 2026): 3 production services + 40+ features shipped in 60 days part-time while running YC full-time. Measured at 810× his 2013 coding pace by "logical code change" (methodology and reproduction script published in the gstack repo). More than one-third of his PRs are from agents. Open-sourced his Claude Code configuration as [gstack](../tools/gstack.md): 23 slash commands that simulate a virtual team of specialist agents.
- Simon Willison / Lenny interview (April 2026): November 2025 named as the reliability inflection point — GPT 5.1 and Claude Opus 4.5 crossed a threshold where coding agents went from "mostly works" to "almost always does what you want." Engineers who experimented over the holiday break realized the change. Cloudflare and Shopify each hired 1,000 interns because AI cut ramp-up time from a month to a week.
- "Dark factory" at StrongDM: policy is nobody writes code, nobody reads code. A swarm of AI-simulated users (fake employees making real-system requests) runs 24/7 at ~$10,000/day in token costs. They built simulated versions of Slack, Jira, and Okta from API docs to test without rate limits. This is the most radical current example of AI-native software development.
- Red/green TDD is Simon's highest-leverage agentic engineering pattern: agents write tests first, watch them fail, write the implementation, watch them pass. The 5-word prompt "use red/green TDD" encodes the full workflow because agents recognize the jargon.
- "Hoarding things you know how to do": Simon maintains 193 small HTML/JS tools and a separate research repo of coding-agent experiments. When a new problem arrives, he points Claude Code at past projects and says "combine these two approaches." The knowledge base compounds.
- Lars Faye (May 2026, viral essay): "Agentic Coding is a Trap" — cites an Anthropic study on debugging-skill atrophy (his 47% figure isn't in the actual published study; see [Anti-autopilot review friction](anti-autopilot-review-friction.md) for the verified 50%-vs-67% figure); Willison's "no mental map" confirmation; Faye's prescription: keep implementation, use AI for specs and ad-hoc tasks
- Airbnb counter-pattern (May 2026): 64% of production PRs shipped with agents using a 15-minute playbook — high AI adoption without the orchestration-only model Faye critiques

## Scale data and large-scale case studies

- Stanford Digital Economy Lab (June 2026): 25,000-firm study; AI-exposed early-career (22-25) jobs declining 3.8%/yr since 2022; least-exposed jobs growing 2.0%; junior software devs and customer service hardest hit. Hiring implications live on [AI-native hiring and the junior talent pipeline](ai-native-hiring-and-junior-talent.md).
- Shopify (May 2026, Bessemer conference, @darkzodchi synthesis): LLM proxy, CLAUDE.md discipline, critique loop, permission config deployed fleet-wide across 23,000 engineers. Reported 20% productivity gain. Strategy-to-execution ratio flipped from 30%/70% (2024) to 70%/30% (2026). Q3 2026 target: 90% autonomous coding.
- GitHub commit volume (June 2026): 275M AI-generated commits per week in April 2026, on pace for 14B in 2026 vs 1B in 2025. At this scale, CI/CD (GitHub Actions, specifically CPU capacity) is the bottleneck — not model capability or developer willingness.
- Anthropic internal RSI data (June 2026): The strongest first-party self-reported numbers from a frontier lab. Claude writes 80%+ of Anthropic's merged code commits. Engineers report shipping 8x more code per quarter than pre-Claude. Internal automated task success rate improved from 26% -> 76% over 6 months of harness iteration. Mythos Preview achieved a 52x speedup on a training script optimization task vs. 3x for Claude Opus 4 on the same task. Mythos gave better "next step" suggestions than humans 64% of the time. Caveat: self-reported, no independent verification.
- Anthropic's test-impact-analysis (test-selection) service (September 2026): as Claude came to author 80%+ of merged code and engineers shipped 8x more code per quarter, total tests grew 10x and CI jobs grew 25x over six months, repeatedly overloading the "listener/selector" service that decides which tests run on each PR. Three sequential patches — a bigger machine, package-level sharding, then daily restarts — bought 70 days, then 29 days, then under a day, before the team redesigned the service around an external in-memory data store so listener workers could be stateless and horizontally scalable; the redesign took three weeks for one engineer versus an estimated quarter a year earlier, which is the post's central point: overhauling infrastructure is now often cheaper than patching it, because writing the replacement is no longer the bottleneck. A long-running, service-dedicated Claude Tag session monitored the listener, paged the engineer, and retained context across months whenever lag crossed a threshold, repeatedly arguing for the eventual overhaul before the team acted on it. Anthropic's stated lesson: assume 25x load within two quarters, keep state out of any process meant to scale, and instrument services as "Claude's eyes and ears."
- Cognition (Devin, July 2026): built an automated system estimating human-engineering-hours-equivalent per completed session, validated against 258 self-reported sessions from 126 users across enterprise customers, reaching `r_log = 0.74` on held-out data — stronger than Anthropic's ticket-text-only approach (0.46) though behind METR's smaller-sample internal study (0.83); deliberately calibrated to underestimate; now running in production with customers. See [Economic agent evals](../concepts/economic-agent-evals.md) for the full methodology comparison.
- Bun's Zig→Rust rewrite (Jarred Sumner, July 2026): a documented large-scale case study in adversarial-review-driven agentic refactoring. One Claude session implemented each change; two more, in fresh context windows with no visibility into the implementer's reasoning, reviewed the diff alone with the sole job of finding reasons it might fail — under a standing rule that a workaround needing a paragraph-long justifying comment is presumptively wrong. A shared porting guide and struct-lifetime table kept agents consistent across the 1,448-file codebase, which Sumner piloted on just 3 files before scaling up; Bun's own TypeScript test suite, unaffected by the underlying language, graded the port from the outside. Peak throughput ~1,300 lines/minute; total cost ~$165,000 in tokens.

## Recent changes

- [2026-10-19] Page created, split out of [AI enablement — software development](ai-enablement-software-development.md)'s "Evidence from practice" section; the origin keeps the guidance, patterns, and failure modes this evidence supports.
- [2026-09-14] Added Anthropic's test-impact-analysis CI-scaling case study (25x CI job growth, three successive patches, a three-week stateless redesign, a dedicated Claude Tag monitoring session).
- [2026-07-16] Added the Bun Zig→Rust rewrite case study: one implementer and two fresh-context adversarial reviewers, pilot-then-scale, ~$165K in tokens.
- [2026-07-14] Added Cognition's production session-productivity estimator (`r_log = 0.74`) as evidence that hours/dollar-denominated AI engineering ROI measurement is moving from research into deployed practice.
- [2026-06-05] Anthropic internal RSI evidence added: 80%+ merged code by Claude, 8x code/quarter, task success 26% -> 76%, Mythos 52x speedup on a training-script optimization task

## See also

- [AI enablement — software development](ai-enablement-software-development.md) — the engineering guidance, patterns, and failure modes this evidence supports
- [AI adoption: evidence from practice](ai-adoption-evidence.md) — company-wide (non-engineering-specific) adoption cases
- [AI-native hiring and the junior talent pipeline](ai-native-hiring-and-junior-talent.md) — hiring and junior-pipeline implications of the labor data above

## Sources

- [Shopify AI phase transition — Latent Space podcast (April 2026)](../sources/newsletters/shopify-latent-space-april-2026.md)
- [Ramp AI adoption playbook](../sources/articles/ramp-ai-adoption-playbook.md)
- [gstack — Garry Tan's Claude Code virtual engineering team](../sources/repos/garrytan-gstack-repo.md)
- [Lenny Rachitsky — Simon Willison interview takeaways](../sources/tweets/lennysan-simonw-interview.md)
- [Agentic Coding is a Trap — Lars Faye essay (May 2026)](../sources/newsletters/agentic-coding-trap-may-2026.md)
- [Stanford AI labor market data — June 2026](../sources/newsletters/stanford-labor-june-2026.md)
- [Shopify Claude Code fleet patterns — Bessemer conference synthesis](../sources/articles/shopify-claude-code-bessemer-2026-05.md)
- ["GitHub's Plan for Agents" — Kyle Daigle on Latent Space (June 2)](../sources/newsletters/github-kyle-daigle-june-2026.md)
- [AINews — Anthropic RSI and Nemotron follow-up (June 5)](../sources/newsletters/ainews-june-05-2026.md)
- [Estimating the Productivity of an Autonomous AI Software Engineer](../sources/articles/cognitioncom-blog-ai-productivity.md)
- [Rewriting Bun in Rust](../sources/articles/bun-rust-rewrite-2026-07-16.md)
- [OpenAI's new model for cyber attacks (newsletter digest)](../sources/newsletters/openais-new-model-for-cyber-attacks-2026-07-16.md)
- [Agentic coding is straining CI — Anthropic](../sources/articles/anthropic-ci-test-impact-analysis-2026-09-14.md)
