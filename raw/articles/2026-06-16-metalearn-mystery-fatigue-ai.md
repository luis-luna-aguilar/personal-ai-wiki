# I Solved My Mystery Fatigue with AI

**Source:** https://metalearn.substack.com/p/i-solved-my-mystery-fatigue-with-ai
**Author:** Amy Deng
**Published:** June 16, 2026
**Type:** article (Substack)

---

## Subtitle
Here's how you can do the same

## Summary

Amy Deng (AI researcher, formerly at METR) developed a 4-step process for investigating her mystery fatigue episodes using AI. After a prolactinoma (pituitary tumor) and two brain surgeries, she experienced episodic fatigue, brain fog, lightheadedness, and nausea. Using frontier AI models and a systematic process, she solved the mystery and has been symptom-free for a month.

**Bold claim:** "An AI-literate patient running a good process with a frontier model can outperform most PCP visits for ambiguous, multi-system symptoms."

The models raised nearly every hypothesis the specialist's NP offered on a phone visit, and even flagged the same specialized test (ACTH stimulation test) the NP independently ordered.

---

## The 4-Step Process

### Step 0: Health Prompting Tips

**Basics:**
- Always use reasoning models with high thinking effort (Claude Opus 4.8 or GPT 5.5). Paid subscription is "the most worthwhile $20 I've spent."
- Create a project to organize health records. Upload clinical records once; the model builds memory around your health concerns over time.
- For advanced users: try a coding agent (Codex or Claude Code). Advantages: handles complex file formats (CT/MRI, large data dumps), planning mode surfaces unknown-unknowns, no re-uploading when files change, can build custom tools.

**Provide ALL the context:**
- Write up medical history: gender, age, weight, height, family history.
- Attach all relevant records: blood work, specialty tests, clinical notes.
- ChatGPT Health allows connecting EHR systems directly.
- Average doctor lets patient talk only ~11s before interrupting; models have infinite patience.

**Be Specific:**
- Describe symptoms: severity, duration, what happened beforehand, what caused it to stop.
- For test results: give full test name, exact value, reference range. T4 ≠ free T4; "in range" doesn't tell the full story.

**Be Critical:**
- Models can confidently be wrong. Best defense: understand the underlying science yourself (ask models to teach it).
- When answer seems off, regenerate a few times and compare across different models.
- Don't take risky medical action without care team sign-off.

### Step 1: Tracking

**Why track?**
- Memory can't hold all the variables. Longitudinal data sets a baseline for any intervention.
- Forces you to question assumptions and look systematically at every variable.
- Helps see progress when healing isn't linear.

**What to track:**
- Ask an LLM to suggest high-signal metrics given your symptoms and working hypothesis.
- Tracking is iterative — start small and expand.

**How to track:**
Amy's setup (~20 min/day):
- Specialized apps: Garmin (sleep/steps), Cronometer (food/liquid), continuous glucose monitor.
- Core Notion spreadsheets: hourly log (energy 1–5, symptoms, notes) and daily log (cycle day, medication dose, sleep score, calories, carbs, exercise, stressors, average energy).
- Had an AI agent build the spreadsheets and auto-populate fields.

Rules: make it as easy as possible; keep it in a format easy to export and parse.

### Step 2: Testing

Tracking is subjective; run tests in parallel to find root causes.

Amy's tests:
- **General blood work:** Function Health, 100+ biomarkers, $365/year.
- **Specialized testing:** Full pituitary hormone panel; ACTH stimulation test (same test her NP independently ordered).
- **At-home blood pressure measurements:** screen for orthostatic intolerance.
- **Gut health testing:** rule out contribution from frequent bloating.

Caution: avoid over-testing (costly and emotionally exhausting). Ask model what additional tests are worthwhile — they're "just conservative enough."

### Step 3: Analyzing

With longitudinal data and test results, you can put AI to fullest use. No PCP can sift through a month of scattered notes.

Amy handed the model:
- All tracked data: central spreadsheet + Cronometer + CGM exports + full Garmin history (via coding agents).
- All test results: Function Health, pituitary labs, gut health, blood pressure.

Specific questions asked:
- "Looking through all the data, can you find any patterns in what triggers my fatigue and what resolves it?"
- "What hypotheses might explain my symptoms?"
- "Why do my symptoms tend to hit in the mid-afternoon, and why does social interaction temporarily relieve them?"
- "Given those hypotheses, what interventions might reduce frequency/severity? Would additional testing help?"

By the time she talked to her PCP, endocrinologist, and NP, every question they asked was something she'd already investigated.

### Step 3.5: Building a Supporting Cast

Specialists complement AI. Amy consulted a dietitian based on patterns in her logs (snack improved symptoms, was under-fueling ~300 cal/day). This surfaced insights the AI had missed.

Supporting cast could include: physical therapist, sleep coach, psychologist.

### Step 4: Experimenting

Amy's experiments:
- **Low ferritin → iron supplements** (even though iron and saturation were normal)
- **+300 cal/day**, hitting carb recommendations specifically
- **Tracked fluid intake** to rule out dehydration
- **Creatine** post-workout
- **Paused exercise** for a week, then resumed — no post-exertion fatigue
- **Stopped tumor medication** for 4 weeks, restarted at half dose (prolactin was too low)
- **Estrogen testing** across cycle days 1, 14, 21 — may need supplementation

Three categories of experiments:
1. **Definitely worth doing** (iron when ferritin is below range, hydration) — start immediately
2. **Harmless but maybe useless** (creatine) — space out from other experiments to isolate effects
3. **Potentially risky or costly** (medication changes, stopping exercise) — consult physician, time-bound

---

## Outcome

Feeling consistently good for a month. Loop mostly closed on the fatigue mystery. Now applying same process to body recomposition with hormonal complications.

---

## Appendix I: Plug-and-Play Artifacts

- System prompt: https://github.com/amydeng2000/health-self-investigation-skill/blob/main/skills/health-self-investigation/references/portable-core.md
- Skill for Codex and Claude Code: https://github.com/amydeng2000/health-self-investigation-skill

---

## Appendix II: Build Your Personal Health Stack

AI's coding and research capabilities now allow each of us to build personalized health tools:
- Set up scheduled ChatGPT tasks or Claude apps to ping you hourly for tracking.
- Build jobs to pull food photos from iCloud daily.
- Build a website to visualize health data (as GitLab co-founder Sid did for his cancer data).

Biggest unlock ahead: continuous monitoring beyond blood glucose (hormone monitoring, etc.).

---

## Key claims

- AI-literate patient + good process + frontier model can outperform most PCP visits for ambiguous multi-system symptoms.
- Models raised nearly all the same hypotheses as trained specialists; flagged the same niche ACTH stimulation test.
- Always use reasoning models with high thinking effort (Claude Opus 4.8, GPT 5.5).
- Coding agents (Claude Code, Codex) offer advantages for complex data and planning.
- ChatGPT and Claude are not HIPAA-compliant by default; users can opt out of data training.
- Most people have a significant "elicitation gap" — they don't know how to use models for health effectively.
- Author worked at METR evaluating agents on software engineering tasks and observed the elicitation gap firsthand.
