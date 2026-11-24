---
title: 'Every — Context Engineering Is Knowing When to Start Over'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-16-context-engineering-is-knowing-when-to-start-over.md
published: 2026-10-16
ingested: 2026-10-20
domains: [training]
---

# Every — Context Engineering Is Knowing When to Start Over

Mike Taylor (Every's head of evals, author of O'Reilly's *Context Engineering with DSPy*) adapts Drew Breunig's long-context failure modes for everyday chat users: seven ways context goes wrong, each with a sign to watch for and a fix. A Context Window recap on 18 October (`raw/newsletters/2026-10-18-codexs-comeback-up-close.md`) summarizes the essay and adds nothing new.

## Influenced pages

- [Managing chat context](../../training/chat-context-management.md) — page created from this essay

## Key claims extracted

- Taylor keeps memory off in Claude and ChatGPT and opens a fresh thread for every task
- Seven failure modes: distraction, confusion, neglect, drift, clash, poisoning, underspecification
- Distraction: adding "i-" examples moved "i-" product names from 21% to 100% of suggestions
- Confusion: a GitHub-COO persona used a favorite framework in 5 of 12 answers; the real person never mentioned it
- Neglect: "Lost in the Middle" (Liu et al.); a bug report at position six of nine documents was ignored
- Clash: splitting prompts into step-by-step messages gave 39% worse results across models (Microsoft and Salesforce research)
- Poisoning: Gemini 2.5 spent 100+ turns hunting a nonexistent Pokémon item; fix by editing the earlier message, not arguing
- Underspecification: closing prompt "What information would have been useful to know at the start of this task…?" carried into a new thread as a handoff
- Long-term fix: keep the best context in local files the agent reads as needed
