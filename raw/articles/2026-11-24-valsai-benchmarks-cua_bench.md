---
title: CUA-bench Leaderboard and Methodology
type: source
source_type: article
url: https://www.vals.ai/benchmarks/cua_bench
fetched: 2026-11-24
---

# CUA-bench Leaderboard and Methodology

## What a run looks like

A few minutes from each of three scored trials, compressed into five seconds.
Every frame is preserved footage, not a re-enactment.

[![](/benchmarks/cua_bench/minecraft-poster.jpg)](/benchmarks/cua_bench/minecraft.mp4)

**Minecraft** — Claude Opus 5, an hour in. It has already
punched out logs and built a crafting table and a wooden pickaxe from
recipes it knew, and it picked up cobblestone at minute 50; here it is
back among the birches for more wood before the stone pickaxe it crafts
at minute 97. It acted once every 36 seconds, so these five minutes hold
about eight decisions. It went on to build a furnace and never found
iron.

[![](/benchmarks/cua_bench/superhot-poster.jpg)](/benchmarks/cua_bench/superhot.mp4)

**SUPERHOT** — GPT-6 Astra, thirty minutes in. Time only
advances when the agent moves, so every pause is the model thinking and
every burst is it committing: here it closes on a red figure, fires, and
throws a weapon. Even with the clock stopped between actions, each one
still has to land a shot on a target in a 3D scene. Astra cleared five of
the 25 levels.

[![](/benchmarks/cua_bench/efootball-poster.jpg)](/benchmarks/cua_bench/efootball.mp4)

**eFootball** — GPT-6 Astra in one of the two Beginner
matches it won, with the menus between them cut. The ball does not wait:
Astra acted every 28 seconds on average and held a direction key 743
times over the trial to keep a player moving while it decided the next
thing. It won twice at Beginner and never at Regular.

The held-out three are not shown, for the same reason they are not named.

## Background

CUA-bench asks whether an AI agent can play games people actually buy. Six
commercial titles, three hours each, keyboard and mouse only. The agent sees the
screen and nothing else: no game console, no save files, no memory inspection,
no network calls to the game. Every verifier lives on the harness side, where
the agent cannot reach it. Most agent evaluations hand the model a text
interface, an API, a DOM or a game state; here it gets what a person gets,
pixels in and keystrokes out, so the score measures computer use itself rather
than the fit of a wrapper.

The suite is built in pairs. Three games are public: **Minecraft**, **SUPERHOT**
and **eFootball**. Each is matched with a held-out game of the same genre — one
sandbox, one first-person reflex game, one sports title — whose identity we do
not publish. A lab can train on a named title. It cannot train on one it cannot
name, and the paired design means the hidden half measures the same kind
of play as the half everyone can see.

A common fear is that the moment a benchmark is created, the labs will train
against it. A private set lets us detect if and when that happens without giving
up the generalization of the eval. If a model’s public scores pull away from its
held-out scores, the pairs will show it.

Each game has its own ladder of milestones worth 100 points in total, and a
model’s overall score is the mean of its six games. Milestones are credited in
order: a later rung never pays before the rungs under it.

| Public game | Ladder |
| --- | --- |
| Minecraft | 13 rungs: log, crafting table, wooden pickaxe, cobblestone, stone pickaxe, furnace, iron ore, iron ingot, kill a hostile mob, flint and steel, obsidian, portal, enter the Nether |
| SUPERHOT | 25 rungs, 4 points each: clear one story level |
| eFootball | 5 rungs: win matches at rising difficulty, Beginner through Professional |

The three held-out games are scored the same way, on ordered milestones that
add up to 100 points, though their rung counts and point values differ. We do
not publish those ladders for the same reason we do not name the games.

Latency is a deliberate part of the test, and eFootball shows it most. These
games run in real time whether or not the agent is ready: the ball keeps moving
while a model is still deciding what to do, so its response time counts against
it as much as its judgment does. To score at all, a model has to act at
something like the speed a person would.

Three hours is the whole budget for a game: reading the screen, learning the
controls, failing, and retrying. It is not three hours of successful play.

## Why games

Games are a good test of computer use for practical reasons. They are purely
multimodal: pixels in, keyboard and mouse out, with no API to lean on. They are
latency-constrained: the world keeps moving, so response time is part of the
score. People are good at them: children learn to operate them quickly and
without instruction. And we chose them because the skills they exercise,
reading a scene, acting under time pressure, holding a plan across hours, are
ones we expect other computer work to draw on: football demands real-time
decisions and continuous control, Minecraft demands navigating a 3D world and
remembering where things are.

We are also watching for continuous learning, which we already see signs of in
our [KSP benchmark](/benchmarks/time_horizon_index). There, what a model learns compresses neatly into text, so it
can write the lesson down and carry it into the next attempt. Video does not
compress that way. How would a model get better at eFootball? It can win at
Beginner — but can it turn what worked there into a win at Regular, and that into
a win at Professional? Those wins are reflexes and timing, not an equation it can
restate in a sentence. We expect this to be much harder for models, and to take
much more work to improve.

## Results

Scores are the mean of the six games, each out of 100. The per-game columns show
where the points came from. The time column is each model’s average number of
seconds between one action and the next, over everything it played.

Named games against their hidden pairs

Each model's mean score on the three public games (filled) and on the three held-out games of the same genres (hollow). With one trial per cell this is an observed difference, not a measured effect of training on the named titles; the pairs exist so that effect can be watched for.

010203040MEAN SCORE OUT OF 100GPT-6 Astra26.7 / 11.7 +15.0Claude Opus 5.514.0 / 14.0 +0.0Claude Fable 5.122.3 / 4.0 +18.3Claude Opus 511.3 / 6.7 +4.7GPT-5.6 Sol9.3 / 7.3 +2.0Wonder7.7 / 6.7 +1.0Muse Spark 1.3 Max5.0 / 6.7 −1.7Gemini 4 Argon6.3 / 3.3 +3.0Gemini 3.8 Flash1.7 / 6.7 −5.0

publicheld outpublic / held out, then the gap

Every keystroke, click and mouse move an agent sends is logged, so the play
itself can be counted and not just the outcome.

When each model was actually touching the machine

One column per minute of play. Darker means more inputs in that minute, pale means the run was still going but nothing was sent, and a lane stops where its run ended. A trial that was interrupted and resumed from its save is stitched into one lane.

GPT-5.6 Sol2,27712.7/minClaude Opus 5.51,95810.9/minGPT-6 Astra1,86610.4/minClaude Opus 51,6669.3/minClaude Fable 5.11,3778.1/minWonder1,2116.7/minGemini 4 Argon8774.9/minMuse Spark 1.3 Max7574.3/minGemini 3.8 Flash4902.8/min030m60m90m120m150m180mMINUTES INTO THE THREE-HOUR RUNBUSIEST MINUTE: 88 INPUTS

## What the agent does

Each model plays through the command-line harness its own vendor ships — Codex
for OpenAI models, Claude Code for Anthropic models, Muse Code for Meta’s Muse
Spark, Google’s computer-use agent and Antigravity CLI for Gemini — running on a separate CPU sandbox that drives one GPU game desktop
over MCP. The agent may use its own shell and Python for scratch work on what it
saw on screen. That work shares the same three-hour clock.

## Methodology

Every trial is capped at three hours of gameplay. A trial that is interrupted by
infrastructure resumes from its own saved game, its own model conversation, and
only the unused remainder of its original three hours. When an interruption
leaves nothing to resume from, the game is rerun once from the start, and the
interrupted attempt counts in neither cost nor score. A setup failure never
becomes a model’s zero.

Scores are recomputed after the fact from preserved evidence under one frozen
rubric, not from anything a live run reported about itself:

* **Native evidence** for the four offline games, read from the game’s own
  state: the world and server state for one, the games’ own save files for
  others, a mission registry for another.
* **Video evidence** for the two online sports games, where no readable save
  exists. The full recording is scanned at 2 Hz for result screens; each
  candidate result is confirmed by three distinct source frames and, for a
  claimed win, an agreeing text reading of the on-screen header.
* **Signed recordings.** Every trial records continuously and the recorder signs
  the archive. Grading rebuilds the movie from durable chunks and verifies its
  hash before scanning a frame.

A trial that played is graded on what it achieved, even if it ended early: a
model that clears nothing scores 0. Missing evidence is a grading failure, not a
zero, and a trial our infrastructure stopped is resumed or rerun rather than
scored. The held-out games are graded by the same rubric and the same pipeline as the public
ones; holding a title back changes what we publish, not how it is scored. Where
the pipeline cannot decide a cell, a person reviews the preserved evidence and
records the decision. A trial plays the official build its publisher serves at
the time; when a game ships a new build, that build’s title screen and the
grader’s screen anchors are verified with unchanged thresholds before its cells
are graded.

Costs are registry-priced estimates from the signed request ledgers of the runs
behind each published cell, including every segment of a trial resumed from its
save. Attempts that failed or were superseded are not counted. Request
attempts that never returned usage are excluded, so each figure is a floor, not
an invoice.

\* GPT-6 Astra’s launch-day runs barely reused the provider’s prompt cache, so most
of their context was counted as cache writes; a later run on the same setup cached normally.
