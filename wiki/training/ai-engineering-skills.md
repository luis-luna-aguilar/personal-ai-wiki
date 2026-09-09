---
title: AI Engineering skills
type: training
as_of: 2026-08-31
sources: [ainews-andrew-ng-ai-engineering-2026-08-25, every-anthropic-certification-critique-2026-08-31]
---

# AI Engineering skills

A practical skills taxonomy for anyone working with AI day to day, not just people with "AI Engineer" in their title. Andrew Ng (Google Brain/Coursera cofounder) relaunched DeepLearning.AI's curriculum around it in August 2026, based on an analysis of 10,000+ job postings plus structured interviews with hiring managers and recruiters.

## Current guidance

Four core skills, in Ng's framing:

- **Building and deploying AI applications** — understanding the building blocks (LLMs, context engineering, RAG, agentic workflows, classic ML/deep learning) and, critically, running disciplined evals and error-analysis loops to measure, steer, and govern AI system behavior. Closest to traditional MLE/MLOps work, extended through prompt/harness engineering and fine-tuning.
- **Software engineering fundamentals** — architecture, data-store design, and testing judgment that determines whether someone can spot the tradeoffs their coding agent is silently making. Ng frames this as the difference between an experienced developer directing an agent well and an inexperienced one "vibe coding" a solution without knowing what context the agent needed.
- **Using coding agents effectively** — a working mental model of agent limits: knowing how much to intervene versus leave the agent alone, when a written spec is worth the overhead and when it isn't, how to orchestrate multiple agents working together, and how to avoid costly mistakes (for example, an agent misconfiguring a production database). Because agentic coding practice moves fast, this skill includes a standing habit of testing new tools and revising workflow as best practices shift, not a fixed technique set.
- **Shaping the build** — product sense: understanding business context and customer goals well enough to help decide what to build, including judgment calls like when to ship a fast MVP for user testing versus slow down and build more carefully.

## Why it matters

Ng frames the first two skills as adjacent to the traditional MLE and SWE tracks respectively, the third as newly critical since coding agents went mainstream, and the fourth — product/business judgment — as the dimension the original "AI Engineer" framing (2023) didn't fully anticipate.

## Evidence from practice

- **Every's review of Anthropic's certification program (August 2026):** roughly 10 Every staff completed Anthropic's new 4-course certification (Agent Skills, Claude API, MCP, Claude Code — 10-15 hours total). Conclusion: the courses mainly succeed at establishing shared vocabulary (what Anthropic means by "skill," "MCP," "API") rather than teaching workflow transformation, and Anthropic's own documentation is "the gold standard" for anyone who wants real depth. Weaknesses: content already stale in places (a deprecated Sonnet API model used in examples, no mention of Anthropic's own MCP-builder skill), and one-size-fits-all delivery with no role-based tailoring — reactions split sharply by role, from "largely unnecessary" to "should be part of onboarding."

## Open questions

- How much of this taxonomy holds for non-technical roles (marketing, ops) using AI day to day, versus being specific to people building AI-powered software?
- Does "software engineering fundamentals" matter less over time as agents absorb more tradeoff-navigation work themselves, or more as the floor for unskilled use rises?

## Recent changes

- [2026-08-31] Added Every's practitioner review of Anthropic's certification program as a first "Evidence from practice" section: useful mainly for shared vocabulary, not workflow transformation; stale content and no role-based tailoring were the main weaknesses cited.
- [2026-08-25] Page created from Andrew Ng's DeepLearning.AI relaunch around four AI Engineering skills, based on a 10,000+ job-posting analysis plus hiring-manager interviews.

## Sources

- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
- [Every — What We Learned From 15 Hours of Anthropic Certification Training](../sources/newsletters/every-anthropic-certification-critique-2026-08-31.md)
