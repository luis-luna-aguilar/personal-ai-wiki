---
title: "We can measure slop"
type: newsletter
sender: "Vector Lab <news@velab.dev>"
received: 2026-03-29
gmail_id: 19d3a482f6e018a3
---

# We can measure slop

**From:** Vector Lab <news@velab.dev>
**Date:** 2026-03-29

You can read this online on the VectorLab site as well: [vectorlab.dev/news/weekly-3-23-to-3-29](https://vectorlab.dev/news/weekly-3-23-to-3-29)

# tl;dr

  * We can now measure how AI turns our codebases into slop over time
  * GitHub is training on your data now by default



# Research

## Slop Code Bench

I have been looking for a good benchmark that shows what happens to codebases when building them with vibe coding and I have finally found one, called [Slop Code Bench](https://x.com/GOrlanski/status/2037560777356238881?s=20).

OpenAI model performance (GPT 5.4 and 5.3 Codex)

They find that across all metrics that they measured, across 20 codebases with up to 8 (sequential) tasks, coding performance decreases. This decrease in quality can be measured in terms of code structure, verbosity, test pass rate, and cost.

They also were testing models in their "natural habitats", ie Claude Code or the Codex CLI, and also tried different prompting techniques, including instruction on how to prevent sloppy code or adding in a planning phase at the start as well. These prompting techniques were able to make the code better at the start, but they still did not stop the decrease in code quality as more and more features were added by the AI.

I hope to see this benchmark expand even more and be updated with new models, and if they do you will be seeing me reference it when new models are released.

_Human made answers do not have the same degradation over time that we see with LLMs_

# Quick Hits

## GitHub trains on your data

A PSA for those that use GitHub: by default they use your repo data to train their models with.

To turn it off, go to Settings > Copilot > Features > Privacy and set Allow GitHub to use my data for AI model training to disabled.

# Finish

It was a quiet week for AI news. I hope you enjoyed and can spend the extra time catching up with previous releases. If you want to get the news every week, be sure to join our mailing list below. 

_caterpillar(?)_ by [Neda](https://x.com/nekimar_/status/2037111995476890035?s=20) on Twitter

You received this email because you subscribed to the AI news from the Vector Engineering Lab. If you want to unsubscribe, use the link below.

[Unsubscribe](http://localhost:8000/unsubscribe/5802e140-518f-415e-859d-3c7e720fc5b8) from this list.
