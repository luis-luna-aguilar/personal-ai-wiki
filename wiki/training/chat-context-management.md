---
title: Managing chat context
type: training
as_of: 2026-10-16
sources: [every-context-engineering-start-over-2026-10-16, every-instruction-bloat-parrott-2026-10-05]
---

# Managing chat context

For everyday users of Claude, ChatGPT and similar chat apps. Everything in a conversation, plus memory and custom instructions, shapes the next answer, and models are poor at deciding that earlier material no longer applies. Output does not announce that a thread has gone bad; it just gets worse. Managing chat context means choosing what the model sees: context engineering (see [Harness](../concepts/harness.md)) done by hand, one thread at a time.

## Current guidance

- Start a fresh thread whenever the task changes, even within the same project.
- Put the full brief in the first message instead of feeding it in over several turns.
- Keep memory off and custom instructions minimal; one offhand preference can leak into every chat.
- When the model gets something wrong, edit your earlier message or regenerate instead of arguing in the thread.
- Before leaving a long thread, ask: "What information would have been useful to know at the start of this task that would have eliminated several steps or mistakes?" Edit the answer and paste it into the new thread's brief.
- Keep reusable context (preferences, briefs, standard procedures) in saved files you paste in or point an agent at, not in a long-running thread.

## Seven ways context goes wrong

Mike Taylor (Every, October 2026), adapted from Drew Breunig's long-context failure modes:

| Failure | Watch for | What to do |
|---|---|---|
| Distraction: earlier examples narrow new answers | You ask for a new direction and suggestions still follow the old pattern | New thread when the tone or task changes; add examples on purpose and test how many you need |
| Confusion: irrelevant details steer the reply | The model keeps raising a fact or framework unrelated to the question | Memory off, minimal custom instructions |
| Neglect: the middle of long input is overlooked | The answer skips a key detail buried among documents | Upload only what the task needs; separate threads for separate documents; task at the top |
| Drift: the original goal fades | Earlier constraints (spelling, length) slip back to defaults | Keep standing preferences in a saved note and paste them at the top of each chat |
| Clash: early assumptions conflict with later information | The model builds on a guess made before you clarified | Full brief in the first message; if you left something out, restart with the complete brief |
| Poisoning: an earlier error keeps returning | A corrected fact reappears in the next draft | Edit the message that led to the error rather than correcting it in the thread |
| Underspecification: missing detail yields a generic answer | The answer could apply to anyone | Supply your own experience and constraints; carry a handoff summary into the new thread |

Taylor's examples: adding a few "i-" names to a Steve Jobs-style naming prompt moved "i-" names from 21% to 100% of suggestions; splitting a prompt across several messages cost 39% in a Microsoft and Salesforce study; and his writer colleague's 3,855-word style guide made drafts worse until it was cut to 513 words (see [AI style guides](ai-style-guides.md)).

## Failure modes

- Treating a long thread as the place where project knowledge lives.
- Arguing with the model about a mistake, which keeps both the error and the complaint in context.
- Saving every preference to memory or custom instructions "just in case".

## Related

- [AI style guides](ai-style-guides.md) — instruction bloat in persistent writing context
- [Agent memory](../concepts/agent-memory.md) — how memory systems decide what to keep; why stale facts resurface
- [Agent loop design](../workflows/agent-loop-design.md) — fresh-context loops as the coding-agent answer to context rot

## Recent changes

- [2026-10-16] Page created from Mike Taylor's seven context failure modes for chat users and Katie Parrott's instruction-bloat case.

## Sources

- [Every — Context Engineering Is Knowing When to Start Over](../sources/newsletters/every-context-engineering-start-over-2026-10-16.md)
- [Every — When Trying to Make AI Better Makes It Worse](../sources/newsletters/every-instruction-bloat-parrott-2026-10-05.md)
