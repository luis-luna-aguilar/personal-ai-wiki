---
type: proposal
source: raw/newsletters/2026-09-21-how-to-create-your-own-personal-ai-benchmark.md
sources:
  - raw/newsletters/2026-09-21-how-to-create-your-own-personal-ai-benchmark.md
  - raw/newsletters/2026-09-24-why-evals-are-so-hot-right-now.md
  - raw/newsletters/2026-09-25-copilot-gets-a-seat-in-the-org-chart.md
  - raw/newsletters/2026-09-27-opus-55-and-sol-split-the-team.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Personal AI benchmarks (Every's three-level method)

## Summary

### In short
Knowing which model suits your job now takes a small private benchmark built from your own failed tasks, because public leaderboards no longer separate models on everyday work. Every's Mike Taylor gives a three-level method: mine your sessions for ten failures, grade with yes/no checks rather than scores, then grow each task to 20+ cases. Evals are also becoming routine: Microsoft runs about 16,000 internal ones. The proposal creates a training page for individuals, adds a pattern and an evidence bullet to the workflow-agent evals page, and three source pages. One reason to hesitate: it adds a 21st training page instead of extending one.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 21 September 2026 Mike Taylor, who runs evaluations at Every, published "How to Create Your Own Personal AI Benchmark". His point: trivia and competition-math benchmarks say little about whether a model helps with your job. His method has three levels. First, collect failures: ask your coding or desktop agent to search the past month of session history for about ten tasks that needed heavy back-and-forth or were abandoned, run them on several models in parallel, and have the agent build a side-by-side viewer. Second, turn taste into tests: dictate what you liked and disliked, have a model convert that into yes-or-no checks, and let a second model grade outputs against them. Taylor warns against 100-point scores, because model ratings cluster around 70/100 and imply precision they lack. Third, scale up: turn each task into a skill that files every brief, output and piece of feedback until each task has 20 or more cases with a gold example and an eval script.

His own consulting benchmark showed OpenAI's cheapest model, Luna, within a few points of Fable. He reads that as Luna being good enough for tasks below the "discernment horizon", where most models pass. Benchmarks also expire: as models improve, the tasks must get harder.

Three days later Every's Context Window newsletter reported that nearly half of 25 product-manager openings Lenny Rachitsky shared asked for eval experience, that Sentry's code changes triggered about 1,800 eval runs in a month (from near zero in May), and that Every is helping all staff build personal benchmarks. The next day, reporting from Microsoft's Copilot relaunch, Every said Microsoft runs about 16,000 internal evals built by domain experts, and that its successful customers have the person who does the job build the eval, treat failing tests as the to-do list ("embrace the red"), and measure the human baseline first. A 27 September recap repeated the method.

### What changes
The wiki covers evals for coding agents and for deployed workflow agents, with Every's August argument that public benchmarks cannot answer buying decisions. It has no guidance for an individual choosing their own daily model.

- New page `training/personal-ai-benchmarks.md` for individual knowledge workers: guidance, the three levels, evidence and failure modes.
- **Evals for workflow and task agents** gains a proven pattern from Microsoft's practice (practitioner-built evals, "embrace the red", human baseline first) and one evidence bullet on evals becoming a job requirement and an engineering routine (Rachitsky, Sentry), with a pointer to the new page. Two Recent-changes entries dated 24 and 25 September (4 entries, no spill). Page date stays at 17 October.
- **Index** gains the new page; the training count moves from 20 to 21.
- Three new source pages: Taylor's essay, the "evals go mainstream" story from the 24 September newsletter, and the eval-practice story from the 25 September Copilot piece. The recap gets no page.

### What to weigh
The main call is scope. The triage suggested folding Taylor's method into the workflow-agent evals page, but that page is written for teams evaluating agents they deploy, and Taylor writes for one person picking a model, so the proposal gives individuals their own page. The other stories in the 24 September newsletter (a Grok 4.7 vibe check, a video workflow, Slack agents) and the Copilot product news in the 25 September piece are left out.

## Intended changes

- [ ] **Create** `wiki/training/personal-ai-benchmarks.md` — new training page for individual knowledge workers

- [ ] **Update** `wiki/training/evals-for-agentic-work.md` — one new Proven-patterns bullet and one new Evidence-from-practice bullet; adds two Recent-changes entries dated 2026-09-25 and 2026-09-24 (list goes 2 → 4, no spill); append two source ids and links

- [ ] **Update** `wiki/index.md` — add the new training page; training count 20 → 21

- [ ] **Create** `wiki/sources/newsletters/every-personal-ai-benchmark-2026-09-21.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-evals-go-mainstream-2026-09-24.md` — story-specific source summary

- [ ] **Create** `wiki/sources/newsletters/every-microsoft-company-evals-2026-09-25.md` — story-specific source summary (Microsoft's eval practice only)

## Page drafts

### wiki/training/personal-ai-benchmarks.md (new)

```
---
title: Personal AI benchmarks
type: training
as_of: 2026-09-24
sources: [every-personal-ai-benchmark-2026-09-21, every-evals-go-mainstream-2026-09-24]
---

# Personal AI benchmarks

For individual knowledge workers choosing which model to use for their own work. A personal benchmark is a small, private set of tasks from your own job, with checks that encode your standards, run against each new model. Public benchmarks measure trivia and competition math; they cannot tell you whether a model helps with your job, or whether a cheaper one would do just as well. With frontier models now exceeding most everyday needs, speed, price and fit with your taste decide the daily driver, and a personal benchmark is how you know whether a release changes anything for you.

## Current guidance

- Build from failures, not successes. Tasks your current model already handles only matter if a new one does them more cheaply. Keep a list of what AI got wrong ("back-pocket evals", Steve Yegge's term) and rerun it on each release.
- Grade with three to ten yes-or-no checks per task, not scores. Model ratings cluster around 4/5 or 70/100 and carry less precision than the number implies.
- Include hard tasks. Easy tasks sit below the "discernment horizon", where most models pass and you learn nothing about the stronger one.
- Treat the benchmark as expiring. When models start passing everything, make the tasks harder.

## Three levels (Mike Taylor, Every)

1. **Fill your back pocket with failures.** Ask your coding or desktop agent to search the past month of local session history for about ten tasks that needed a lot of back-and-forth or were abandoned, and to collect the session logs and reference files. Add the context and advice you would give an intern. Run all ten in parallel on several models and have the agent build an HTML viewer that shows outputs side by side. Compare a large and a small model, two providers, and the same model three times to see how much it varies.
2. **Turn your taste into tests.** Dictate what you liked and disliked about each output, have the model turn that into yes-or-no checks, and let a second model judge new outputs against them.
3. **Scale it into a real benchmark.** Turn each task into a skill that files the brief, output and feedback every time it runs, until each task has 20 or more cases. Taylor's layout: a folder per task, a folder per case holding `prompt.txt`, `context/`, `gold/` (the ideal result) and `evals.py`, and an `index.html` viewer. At this point the private test becomes a team engineering problem; see [Evals for workflow and task agents](evals-for-agentic-work.md).

## Evidence from practice

- **Cheap models clear routine work.** On Taylor's ten-task consulting benchmark (dashboards, articles, slide decks), OpenAI's cheapest model, Luna, came within a few points of Fable. He sends routine work to Luna and the ambitious tasks to Fable and Sol.
- **Every is rolling this out company-wide.** Applied AI engineer Nityesh Agarwal is helping all staff build personal benchmarks so they can tell which releases deserve attention.
- **Results can move after launch.** Taylor's benchmark scored Grok 4.7 at 42% against Grok 4.6's 84% in pre-release testing; a heavy user found the launched model much improved. Rerun before you settle.

## Failure modes

- Testing only tasks every model already passes, then concluding the models are equal.
- Trusting a model's numeric score as if 70/100 were clearly better than 65/100.
- Judging from one success; one good deck can be a fluke, twenty are evidence.
- Keeping a saturated benchmark: Ethan Mollick's "otter on a plane using wifi" test became too easy and had to be replaced.

## Related

- [Evals for workflow and task agents](evals-for-agentic-work.md) — the team-scale version for agents in production
- [Cost-aware AI task routing](cost-aware-ai-task-routing.md) — what to do once you know a cheaper model is good enough
- [Agent skill methodology](agent-skill-methodology.md) — skills as the place where cases and feedback accumulate

## Recent changes

- [2026-09-24] Page created from Mike Taylor's three-level personal-benchmark method and Every's company-wide rollout.

## Sources

- [Every — How to Create Your Own Personal AI Benchmark](../sources/newsletters/every-personal-ai-benchmark-2026-09-21.md)
- [Every — Evals go mainstream](../sources/newsletters/every-evals-go-mainstream-2026-09-24.md)
```

### wiki/training/evals-for-agentic-work.md (updated)

Frontmatter: append `every-evals-go-mainstream-2026-09-24` and `every-microsoft-company-evals-2026-09-25` to `sources:`. `as_of` stays 2026-10-17.

New bullet at the end of `## Proven patterns` (after "Calibrate rubrics with real cases"):

```
- **Have the person who does the job build the eval, and measure the human baseline first.** Microsoft says it runs about 16,000 internal evals, each a common task found in usage data and built by a domain expert. Charles Lamanna's pattern for customers who succeed: the person who does the work daily writes the eval; they "embrace the red", treating a failing test as the to-do list and writing a harder one once it passes; and before the agent tries, they measure how people do the job today (error rates, contract turnaround time) so the agent has a real number to beat.
```

New bullet at the end of `## Evidence from practice` (after the Thinkingbox bullet):

```
- **Evals become a job requirement and an engineering routine.** Nearly half of 25 product-manager openings Lenny Rachitsky shared in September 2026 asked for experience writing evals, and at Sentry proposed code changes triggered about 1,800 eval runs in a month, up from near zero in May, catching cases such as revised instructions that break tasks an agent used to handle. The individual version of the same practice, a personal benchmark for choosing a daily model, is on [Personal AI benchmarks](personal-ai-benchmarks.md).
```

`## Recent changes` — adds two entries dated 2026-09-25 and 2026-09-24, inserted between the 2026-10-17 and 2026-08-25 entries (list goes from 2 to 4, no spill):

```
- [2026-09-25] Added the "person who does the job builds the eval" pattern from Microsoft (~16,000 internal evals; "embrace the red"; measure the human baseline first).
- [2026-09-24] Added evidence that evals are going mainstream (about half of 25 PM openings ask for eval experience; Sentry at ~1,800 eval runs a month) and a pointer to the new personal-benchmarks page.
```

`## Sources` — append:

```
- [Every — Evals go mainstream](../sources/newsletters/every-evals-go-mainstream-2026-09-24.md)
- [Every — Microsoft's company-specific evals](../sources/newsletters/every-microsoft-company-evals-2026-09-25.md)
```

### wiki/index.md (updated)

Insert under `## Training`, after the `training/evals-for-agentic-work` line:

```
- [training/personal-ai-benchmarks](training/personal-ai-benchmarks.md) — for individuals choosing a daily model: build a private benchmark from your own failed tasks, yes/no checks over scores, scale each task to 20+ cases *(as_of: 2026-09-24)*
```

Page count: `- training: 20` → `- training: 21`.

### wiki/sources/newsletters/every-personal-ai-benchmark-2026-09-21.md (new)

```
---
title: 'Every — How to Create Your Own Personal AI Benchmark'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-21-how-to-create-your-own-personal-ai-benchmark.md
url: https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark
published: 2026-09-21
ingested: 2026-10-20
domains: [training]
---

# Every — How to Create Your Own Personal AI Benchmark

Mike Taylor, Every's head of evals, explains how an individual can build a private benchmark from their own work to pick a daily-driver model and spot when a cheaper one is good enough. Three levels: collect about ten recent failures from session history and compare models side by side; turn dictated likes and dislikes into yes-or-no checks graded by a second model; then turn each task into a skill that accumulates 20+ cases with a gold example and an eval script. A 27 September Context Window recap (`raw/newsletters/2026-09-27-opus-55-and-sol-split-the-team.md`) repeats the method and adds nothing new.

## Influenced pages

- [Personal AI benchmarks](../../training/personal-ai-benchmarks.md) — page created from this method

## Key claims extracted

- Public benchmarks (MMLU-Pro, Math Olympiad) measure something, but not whether a model helps with your job
- Level 1: have the agent mine the past month's sessions for ~10 tasks that needed heavy back-and-forth or were abandoned; run them in parallel across models in an HTML viewer; compare large vs small, two providers, and three runs of one model
- "Back-pocket evals" (Steve Yegge): tasks AI failed at, rerun on each new model
- Level 2: dictate likes and dislikes, convert to yes/no checks, LLM-as-judge; avoid 100-point scales because ratings cluster around 4/5 or 70/100
- Taylor's 10-task consulting benchmark: Luna came within a few points of Fable; routine tasks sit below the "discernment horizon"
- Level 3: one skill per task that files brief, output and feedback until there are 20+ cases; folder per case with prompt.txt, context/, gold/, evals.py and an index.html viewer
- Benchmarks saturate and must be made harder over time (Mollick's otter test)
```

### wiki/sources/newsletters/every-evals-go-mainstream-2026-09-24.md (new)

```
---
title: 'Every — Evals go mainstream'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-24-why-evals-are-so-hot-right-now.md
published: 2026-09-24
ingested: 2026-10-20
domains: [training]
---

# Every — Evals go mainstream

The "Evals go mainstream" signal and the Grok 4.7 personal-benchmark data point from Every's Context Window edition "Why Evals Are So Hot Right Now" (Laura Entis). It reports evals turning into a hiring requirement and an engineering routine, and Every's effort to give every employee a personal benchmark. The edition's other stories (Grok 4.7 vibe check, short-video workflow, Slack agents) are not covered here.

## Influenced pages

- [Personal AI benchmarks](../../training/personal-ai-benchmarks.md) — company-wide rollout and the Grok 4.7 pre-release result
- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — evals-as-job-requirement evidence bullet

## Key claims extracted

- Nearly half of 25 product-management openings Lenny Rachitsky shared asked for experience writing evals
- Sentry: proposed code changes triggered ~1,800 eval runs in the past month, from near zero in May
- Nityesh Agarwal is helping everyone at Every build personal benchmarks; frontier models exceed most everyday needs, so speed, price and taste now decide the daily driver
- Mike Taylor's personal benchmark scored Grok 4.7 at 42% vs Grok 4.6's 84% before launch; designer Tyler Nishida found the launched model improved
```

### wiki/sources/newsletters/every-microsoft-company-evals-2026-09-25.md (new)

```
---
title: "Every — Microsoft's company-specific evals"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-copilot-gets-a-seat-in-the-org-chart.md
published: 2026-09-25
ingested: 2026-10-20
domains: [agents, training]
---

# Every — Microsoft's company-specific evals

The eval-practice part of Ryan Sloan's Every piece "Copilot Gets a Seat in the Org Chart", reporting from Microsoft's 23 September Copilot launch in Redmond. Microsoft spent much of the event on how customers should judge Copilot. The piece's product news (the unified Copilot app and Autopilot agents) is not covered here.

## Influenced pages

- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — "person who does the job builds the eval" proven pattern

## Key claims extracted

- Satya Nadella called for "evals specific to your company": tests based on the work your people do
- Microsoft runs about 16,000 internal evals, each a common task or workflow identified in usage data and built by domain experts; it also builds evals with customers
- Successful customers have the person who does the job every day build the eval
- They "embrace the red": a failing test shows what to fix; once it passes, write a harder one
- They measure how humans do the job now (error rates, contract turnaround time) so the agent has a baseline to beat
```

## Schema / vocabulary additions

None.

## Open questions

- Should the personal-benchmark method live on its own page (as drafted), or be folded into Evals for workflow and task agents as the triage suggested? The drafts assume a separate page because the audiences differ (one person picking a model versus a team evaluating a deployed agent).
