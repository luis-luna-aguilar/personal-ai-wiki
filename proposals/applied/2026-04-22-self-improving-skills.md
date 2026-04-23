---
type: proposal
sources:
  - raw/tweets/2026-04-22-tricalt-2032179887277060476.md
  - raw/tweets/2026-04-22-itsolelehmann-2033982679423848802.md
status: pending
created: 2026-04-22
---

# Proposal: Self-improving agent skills — auto-improvement loops for prompts

## Summary

Two complementary sources on making agent skills improve themselves over time. The core insight: skills are static but environments drift — skills fail quietly when code changes, models change, or user patterns shift. The solution is treating skills as living components with a closed feedback loop. Ole Lehmann's "meta-skill" implements this as a 5-step prompt-optimization loop.

## Intended changes

- [x] **Update** `wiki/concepts/agent-improvement-loop.md` — add self-improving skills pattern as a new section
    > **Add new section `## Self-improving skills` after `## Product example: Bugbot learned rules`:**
    > ```markdown
    > ## Self-improving skills
    >
    > A variation of the improvement loop applied at the *skill/prompt* level rather than the full agent harness. The problem: skills in a Claude Code skills folder are static, but the environment around them isn't. A skill that worked last month may quietly start failing when the codebase changes, the model updates, or user request patterns shift. The failures are often invisible until someone notices degraded output.
    >
    > **The closed loop approach (tricalt, April 2026):** Treat skills as living components, not fixed prompt files. Diagnose which component is failing (routing? individual instructions? tool call?). Close the feedback loop by automatically scoring outputs and proposing targeted changes.
    >
    > **The meta-skill approach (Ole Lehmann, April 2026):** A single meta-skill that improves any other skill automatically:
    > 1. Run the target skill and score the output
    > 2. Find what's failing in the score
    > 3. Make one small change to the skill prompt
    > 4. Run it again to see if the score went up
    > 5. Keep the change if it improved; discard if not
    >
    > This mirrors the Better-Harness pattern at the prompt level. The loop is based on Karpathy's "autoresearch" method applied to prompt optimization. Can run on autopilot; the meta-skill improves the target skill without human intervention.
    > ```
    >
    > **Update `as_of: 2026-04-22` in frontmatter.**
    > **Add to sources: `self-improving-skills`.**
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added self-improving skills pattern: closed feedback loop for skill drift; meta-skill 5-step prompt optimization loop
    > ```

- [x] **Create** `wiki/sources/tweets/self-improving-skills.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/tweets/self-improving-skills.md (new)

```md
---
title: Self-improving agent skills — auto-improvement loops
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-tricalt-2032179887277060476.md
url: https://x.com/tricalt/status/2032179887277060476
published: 2026-04-22
ingested: 2026-04-22
domains: [agents]
---

# Self-improving agent skills — auto-improvement loops

Two sources. (1) tricalt article: skills are static but environments drift; treat skills as living components with closed improvement feedback loops; diagnose routing vs instructions vs tool calls. (2) Ole Lehmann tweet: meta-skill that auto-improves any other skill in 5 steps (run → score → change one thing → re-run → keep if better). Based on Karpathy's autoresearch method.

## Influenced pages

- [[concepts/agent-improvement-loop]] — self-improving skills section added

## Key claims extracted

- Skills fail quietly when codebases change, models update, or user patterns shift
- Failures are often invisible until output is noticeably worse
- Loop needs to diagnose routing vs instructions vs tool call as separate failure points
- Meta-skill: 5-step prompt optimization loop; fully automated; improves skills without human intervention
- Based on Karpathy autoresearch method
```
