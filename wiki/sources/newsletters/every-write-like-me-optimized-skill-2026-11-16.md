---
title: "How I Finally Got AI to Write Like Me — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-16-how-i-finally-got-ai-to-write-like-me.md
url: https://every.to/also-true-for-humans/how-i-finally-got-ai-to-write-like-me
published: 2026-11-16
ingested: 2026-11-24
---

# How I Finally Got AI to Write Like Me — Every

Mike Taylor (Every's head of evals) tests four ways to build a "write like me" skill on 185 of his posts and finds that optimizing the skill against held-out posts with a blind pairwise judge beats a descriptive style guide. Gives a six-step method and releases the skill (github.com/everyinc/compound-writing). A 22 November Every recap (`raw/newsletters/2026-11-22-stop-telling-ai-how-you-write-show-it.md`) repeats the method in three steps.

## Influenced pages

- [AI style guides](../../training/ai-style-guides.md) — "Test the skill, don't just describe it" section

## Key claims extracted

- 185 posts (335,000 words, 13 publications); 54 held out; the 30 most recent Every posts optimized better than the full archive
- Each post turned into a style-free brief; drafts judged by a "pairwise gold triad" (real post + two drafts, order swapped)
- Judge consistency on swapped order: Opus 5.5 86%, Sonnet 5.5 70%, Jev 50%
- Claude-written style guide lost to autoresearch, GEPA and ce-optimize on 80–95% of held-out posts; for Opus 5.5 no skill beat it 61% of the time
- Optimizing costs $27–53 per skill vs $5 one-shot; most gains within three rounds; GEPA beat autoresearch 77–31 and ce-optimize 85–15
- Opus 5.5: 16% no skill → 93% with its GEPA skill; GPT-6 Astra 1% → 66%; Sonnet 5.5 + optimized skill beat Opus 5.5 + written skill on 46 of 60 judgments
- 44 edits on one draft versus hundreds in earlier experiments; time from opinion to piece about an hour instead of a day
- Caveat: the judge rewards resemblance to past work
