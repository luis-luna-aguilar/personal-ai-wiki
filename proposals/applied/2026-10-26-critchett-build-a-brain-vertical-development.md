---
type: proposal
source: raw/tweets/2026-10-26-nathannn-critch-2101060475220079101.md
status: pending
created: 2026-10-26
---

# Proposal: "How to Build a Brain in the AI Age" — vertical development and metacognition

## Summary

### In short
Learning more AI tools does not make people good with AI; judgment does, and unguided AI use erodes it: Nathan Critchett cites a study in which half of 27,000 students who adopted AI outsourced their homework within five months and exam scores fell 24%. The proposal adds that study and a Harvard Business School / BCG figure to the cognitive-debt evidence on Anti-autopilot review friction, his horizontal-versus-vertical framing, three practices, and a source page. Reason to hesitate: both figures come through the essay, not the studies themselves.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Nathan Critchett, author of *Cognitive Architecture: How to Think When Machines Think For You*, published an X Article on 18 September 2026 (134K views) arguing that "learn AI" is the wrong instruction. He borrows a distinction from developmental psychology. Horizontal development adds new tools, facts and skills, like pouring more water into the same glass; every "master ChatGPT in 30 days" course is horizontal. Vertical development changes the structure of how a person thinks, which he calls getting a bigger glass.

He cites two studies. In a Harvard Business School study of BCG consultants, those who relied on AI when it was confidently wrong were 19 percentage points less accurate than those working without it. In a 2026 study of 27,000 Chinese secondary students given unguided access to generative AI over two years, half of the adopters had fully outsourced their homework within five months, and high-stakes exam scores fell 24%. Benjamin Riley, who analysed the data, calls this the "50 Percent Problem".

The skill he names is metacognition, thinking about one's own thinking: taking a confident, polished answer and asking whether it is right, whether it answers the right question, and what the machine could not know to include. His prescriptions: get comfortable with confusion, practise judging rather than producing, and ask what a tool is failing to see.

### What changes
Anti-autopilot review friction already has a cognitive-debt section with four studies on comprehension loss and a list of learning-posture habits, all for individual AI users.

- **Anti-autopilot review friction** gains the two studies as further data points, a short "Horizontal versus vertical development" subsection, and three practices added to the learning-posture list. The cognitive-debt section is given three subheads (Evidence, Horizontal versus vertical development, Learning-posture prescriptions), since the additions would otherwise bring it to the edge of the 800-word flat-section limit. Page date moves to 18 September.
- One new source page for the article.

### What to weigh
The HBS/BCG figure and the student study are taken from the essay; neither underlying paper nor Riley's analysis was read. The essay also speaks to school leaders and to organizations designing training, a different audience from this page's individual users, so that guidance is left out here.

## Intended changes

- [ ] **Update** `wiki/training/anti-autopilot-review-friction.md` — replace the `## Cognitive debt` section with the subheaded draft below (existing text kept, two data points, one subsection, and three prescriptions added); `as_of` moves to 2026-09-18; adds one Recent-changes entry dated 2026-09-18 (live list has 4, no spill); append one source id and link
    > See draft below

- [ ] **Create** `wiki/sources/tweets/nathannn-critch-build-a-brain-ai-age-2026-09-18.md` — source summary

## Page drafts

### wiki/training/anti-autopilot-review-friction.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-09-18
sources: [every-ai-autopilot, every-youre-the-manager-now, ai-work-intensification-march, post-vibe-coding-verification-february, every-vibe-check-april-21-2026, lennysan-simonw-interview, prof-devs-control, agents-evals-deep-research, agentic-devops-deep-research, agent-review-artifacts-2026-05-13, osmani-cognitive-debt-ai-learning-2026-05, claude-code-fast-mode-default-2026-05, powerpoint-agent-skill-failure-mode-2026-06, anthropic-ai-assistance-coding-skills-2026, every-read-the-code-2026-09-08, nathannn-critch-build-a-brain-ai-age-2026-09-18]
```

`## Cognitive debt` — full replacement section:

```
## Cognitive debt

Cognitive debt (Addy Osmani, May 2026): the accumulated deficit in comprehension and skill that results from using AI to close tasks without understanding what was produced. "Silently trading future capability for present-day speed, and the tools won't force us to do otherwise." Distinct from hallucination risk: cognitive debt accrues even when the AI output is correct.

### Evidence

**Three empirical studies:**

- **Anthropic comprehension study:** Engineers learned a new Python library — half with AI assistance, half without. Both groups finished tasks at about the same speed. But the AI group scored 50% on the follow-up comprehension quiz vs 67% for the manual group (Cohen's *d*=0.738); the gap widened most on debugging questions. Within the AI group, *how* people used the assistant mattered more than *whether* they did: three low-scoring patterns (quiz average under 40%) all involved heavy reliance with little independent thought — wholesale AI delegation, starting with a few questions before drifting into full delegation, and asking AI to debug rather than to explain. Three high-scoring patterns (65%+) all paired AI use with active comprehension-checking — generating code then asking follow-up questions, requesting code and explanation together, or asking only conceptual questions and reasoning the rest independently. Anthropic's own framing: "not all AI-reliance is the same" — the posture, not the tool, determined the outcome. Confirmed against Anthropic's own primary writeup (arXiv 2601.20245); no longer a secondary-account figure.

- **MIT brain-connectivity study:** Essay writing across LLM, search-engine, and brain-only groups. EEG showed brain connectivity scaling down with every layer of external support; LLM group showed weakest coupling. After writing, 83% of LLM users couldn't quote a single line of what they had just produced. Researchers called this "cognitive debt."

- **Anchoring study:** When participants had LLM access at the *start* of a task, the LLM framed the entire problem — even when humans did the rest of the work themselves, initial anchoring produced measurably worse decisions. Order of operations mattered more than total amount of AI used. Implication: defer AI until after you've formed your own initial frame.

**A fourth data point, and an older name for the pattern:** a 2026 review by Margaret Mitchell, Avijit Ghosh, and Samir Passi (arXiv:2608.23642) documents that extended AI-agent use measurably erodes the vigilance, critical thinking, and domain skill human oversight depends on. The underlying dynamic isn't new — it's the "irony of automation," a term coined in 1983 by a safety researcher studying human operators of automated factories and power plants: the more capable the automation gets, the faster the human's own skill erodes. Agents just make it move faster. *Source: Every, Kieran Klaassen, "To Read—Or Not to Read the Code?" (2026-09-08)*

**Two more data points, as cited by Nathan Critchett (September 2026):**

- **Confidently wrong AI:** in a Harvard Business School study of BCG consultants, those who relied on AI when it was confidently wrong were 19 percentage points less accurate than consultants working without it.
- **The "50 Percent Problem":** in a 2026 study of 27,000 Chinese secondary students given unguided access to generative AI over two years, half of the adopters had fully outsourced their homework within five months, and high-stakes exam scores fell 24%. Benjamin Riley, who analysed the data, names the pattern: homework scores went up while learning went down.

### Horizontal versus vertical development

Critchett frames the remedy with a developmental-psychology distinction. Horizontal development adds tools, facts, and skills; most "learn AI" courses are horizontal. Vertical development changes how a person thinks. His claim is that the people who do well with AI built evaluative judgment first, and that the skill AI rewards is metacognition: taking a confident, polished answer and asking whether it is right, whether it answers the right question, and what the machine could not know to include. On this reading the student study shows that AI without cognitive development does harm, not that AI does.

### Learning-posture prescriptions

- Form a hypothesis before asking: write 2–3 sentences on what you think the problem is; use the model's answer to test your theory, not replace it
- Ask for explanation before code: in unfamiliar territory, first prompt = "explain how this works, alternatives, and tradeoffs" — request code only after grasping concepts
- Treat AI output like a PR from a junior engineer: read it, critique it, push back; don't merge just because tests pass
- Re-derive by hand occasionally: recreate code the model wrote — calibration check for what you've quietly lost
- Ask the model to teach: after it writes a clever function, ask what concepts it used and what you'd read to understand the design choice
- Practise judging, not producing: spend even 20 minutes a day deliberately questioning and pushing back on what a model gives you, instead of only consuming its output
- Ask what the tool is failing to see, and whether you are solving the right problem, before asking how to get better output
- Use AI to stress-test work you built rather than to produce it; Dan Willingham's rule is to use AI only for what you already know how to do
```

`## Recent changes` — insert one entry above the 2026-09-08 entry:

```
- [2026-09-18] Cognitive debt section given subheads; added two data points cited by Nathan Critchett (HBS/BCG: 19 points less accurate when AI was confidently wrong; 27,000 students: half outsourced homework, exam scores −24%), the horizontal-vs-vertical development framing, and three judgment-practice prescriptions.
```

`## Sources` — append:

```
- [Nathan Critchett on X — How to Build a Brain in the AI Age](../sources/tweets/nathannn-critch-build-a-brain-ai-age-2026-09-18.md)
```

### wiki/sources/tweets/nathannn-critch-build-a-brain-ai-age-2026-09-18.md (new)

```
---
title: Nathan Critchett on X — How to Build a Brain in the AI Age
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-nathannn-critch-2101060475220079101.md
url: https://x.com/nathannn_critch/status/2101060475220079101
published: 2026-09-18
ingested: 2026-10-26
domains: [training]
---

# Nathan Critchett on X — How to Build a Brain in the AI Age

X Article (134K views) by Nathan Critchett, author of *Cognitive Architecture: How to Think When Machines Think For You*, arguing that "learn AI" is the wrong goal: horizontal development (more tools and skills) matters less than vertical development (changing how one thinks), and the skill that makes AI useful is metacognition. Cites a Harvard Business School study of BCG consultants and a 2026 study of 27,000 Chinese secondary students (via Benjamin Riley's "50 Percent Problem" analysis) as evidence that unguided AI use replaces thinking, critiques Alpha School's two-hour AI curriculum as horizontal development "at 2x speed", and prescribes comfort with confusion, judging over producing, and asking what a tool fails to see.

## Influenced pages
- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — two cognitive-debt data points, horizontal-vs-vertical framing, three prescriptions

## Key claims extracted
- People thriving with AI learned to evaluate, judge, and sit with ambiguity first; tools amplified that
- Horizontal development adds tools/facts/skills; vertical development changes the structure of thinking
- School-district anecdote: only the 10–15% of strong evaluative thinkers kept using rolled-out AI tools
- HBS study of BCG consultants: when AI was confidently wrong, consultants relying on it were 19 percentage points less accurate than those without it
- 2026 study of 27,000 Chinese secondary students with unguided AI access over two years: within five months half of adopters fully outsourced homework; high-stakes exam scores fell 24% (Benjamin Riley's "50 Percent Problem")
- Metacognition: asking whether a confident answer is right, whether it is the right question, and what the machine would not know to include
- Prescriptions: get comfortable with confusion; practise judgment over production (≥20 minutes a day questioning AI output); ask what the tool fails to see
- Quotes Dan Willingham: AI should not substitute for tasks where students benefit from doing the mental work; use AI only for what you already know how to do
```

## Schema / vocabulary additions

None.

## Open questions

- The essay's program-design advice (train evaluative thinking before tools when rolling AI out to a school or company) belongs to a different audience from this page. Should it go on `training/company-wide-ai-enablement.md` as one line (that page sits at its 2,500-word ceiling, so even one line puts it in the warning band), or be left out?
	- Left out
