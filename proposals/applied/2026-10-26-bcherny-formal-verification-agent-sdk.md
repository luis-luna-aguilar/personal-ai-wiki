---
type: proposal
source: raw/tweets/2026-10-26-bcherny-2102543349102338309.md
status: pending
created: 2026-10-26
---

# Proposal: Boris Cherny formally verifies the Claude Agent SDK with Opus 5.5

## Summary

### In short
Formal methods are becoming a practical bug-finding tool for engineers who don't know them, because the model writes the formal model of the code. Boris Cherny says a couple of short prompts to Opus 5.5 produced Lean and TLA+ models of the Claude Agent SDK and led to 16 PRs fixing bugs and race conditions. TLA+ worked best for concurrency. The proposal adds model-checked specifications as an oracle on **Acceptance contracts and test oracles** and an early-user bullet on **Claude Opus 5.5**. One reason to hesitate: the capture is partial, since his description of the method is cut off and the video was not reviewed.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 22 September 2026, the day Opus 5.5 launched, Boris Cherny, who leads Claude Code at Anthropic, posted that he had used the model to formally verify the Claude Agent SDK with Lean. Lean is a proof language. TLA+ is a language for specifying and model-checking concurrent systems, meaning it searches every possible ordering of events for one that breaks a rule. A couple of short prompts produced 16 pull requests fixing bugs and race conditions. He says TLA+ also works well, and he sometimes combines the two to look for problems in data flow, concurrency and state management. He doesn't know either language well, but says Claude is excellent at both, and that the approach finds bugs a human probably wouldn't spot.

In a follow-up the next day he described the loop. Claude models a tricky state machine or race-prone part of the program, finds counterexamples in that model (each a suspected bug), and then reproduces them. The captured text is cut off at that point. Asked which language suits race conditions, he answered TLA+. Hillel Wayne, a formal-methods author, pushed back in a reply: in his experience, models have been very bad at coming up with even basic high-level system properties, and the last one he tried was Fable 5.1. Cherny said Opus 5.5 "feels much better" and asked for his view. The post had about 2.1 million views.

### What changes
The wiki's only formal-verification coverage is mathematical theorem proving (Axiom Math). Its coding-side oracle list stops at proof-carrying types (gdp-ts).

- **Acceptance contracts and test oracles** gains a "model-checked specifications" oracle: the agent writes a TLA+ or Lean model of the risky part, the checker finds counterexamples, and only bugs reproduced in the real code count. It carries Hillel Wayne's caveat that a person still has to choose the properties worth checking. It gains one Recent-changes entry dated 22 September, and the page date stays 19 October.
- **Claude Opus 5.5** gains an early-user bullet on the SDK verification and one Recent-changes entry dated 22 September. The page date stays 27 September.
- One new source page for the thread.

### What to weigh
The capture is partial: the 23 September method description is truncated and the attached video was not reviewed. The other call is scope. This is a practitioner anecdote, so it goes in as an oracle technique and a usage note rather than a new page. The `formal-verification` subcategory exists, but no formal-methods tool here is used enough to warrant a page. Tagging Axiom Math or linking it would mix math theorem proving with checking software behaviour, so neither is done.

## Intended changes

- [ ] **Update** `wiki/training/acceptance-contracts-and-test-oracles.md` — add one oracle bullet after "Proof-carrying types"; adds one Recent-changes entry dated 2026-09-22 (inserted at its date position, 3 → 4, no spill); merges source id and link; `as_of` unchanged (2026-10-19)
- [ ] **Update** `wiki/models/claude-opus-5-5.md` — add one bullet to `## Evidence from early users`; adds one Recent-changes entry dated 2026-09-22 (2 → 3, no spill); merges source id and link; `as_of` unchanged (2026-09-27)
- [ ] **Create** `wiki/sources/tweets/bcherny-formal-verification-agent-sdk-2026-09-22.md` — source summary

## Page drafts

### wiki/training/acceptance-contracts-and-test-oracles.md (updated)

Frontmatter (merge, do not replace):

```
sources: [...existing..., bcherny-formal-verification-agent-sdk-2026-09-22]
```

In `## Oracles agents can't game`, insert after the "Proof-carrying types" bullet:

```
- **Model-checked specifications** have the agent write a formal model of the risky part of the code (TLA+ for concurrency and races, Lean for state and data flow), let the checker search for counterexamples, then reproduce each one in the real code before fixing it. Boris Cherny reports that a couple of prompts to Opus 5.5 turned the Claude Agent SDK into 16 bug- and race-fix PRs, without his knowing either language well. The caveat: models have been weak at choosing the high-level properties worth checking, so a person should review those (Hillel Wayne).
```

In `## Recent changes`, insert at its date position (after the 2026-10-14 entry, as the oldest dated content entry):

```
- [2026-09-22] Added model-checked specifications (TLA+/Lean) as an oracle: Opus 5.5 modeled the Claude Agent SDK and its counterexamples became 16 bug- and race-fix PRs.
```

In `## Sources`, append:

```
- [Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5](../sources/tweets/bcherny-formal-verification-agent-sdk-2026-09-22.md)
```

### wiki/models/claude-opus-5-5.md (updated)

Frontmatter (merge, do not replace):

```
sources: [...existing..., bcherny-formal-verification-agent-sdk-2026-09-22]
```

In `## Evidence from early users`, append:

```
- Formal methods for non-specialists: Claude Code lead Boris Cherny used it to model the Claude Agent SDK in Lean and TLA+, and a couple of prompts yielded 16 PRs fixing bugs and race conditions. A formal-methods author replied that earlier models were poor at proposing system properties; Cherny says Opus 5.5 feels much better. See [Acceptance contracts and test oracles](../training/acceptance-contracts-and-test-oracles.md).
```

In `## Recent changes`, insert between the 2026-09-27 entry and the 2026-09-22 launch entry:

```
- [2026-09-22] Boris Cherny reports formally verifying the Claude Agent SDK with Opus 5.5 in Lean and TLA+ (16 bug- and race-fix PRs).
```

In `## Sources`, append:

```
- [Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5](../sources/tweets/bcherny-formal-verification-agent-sdk-2026-09-22.md)
```

### wiki/sources/tweets/bcherny-formal-verification-agent-sdk-2026-09-22.md (new)

```
---
title: Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-bcherny-2102543349102338309.md
url: https://x.com/bcherny/status/2102543349102338309
published: 2026-09-22
ingested: 2026-10-26
domains: [coding, models]
---

# Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5

X thread from Claude Code lead Boris Cherny on launch day of Opus 5.5. He used the model to formally verify the Claude Agent SDK in Lean, sometimes combined with TLA+, and a couple of short prompts produced 16 PRs fixing bugs and race conditions, despite his not knowing either language well. A follow-up sketches the loop (model a race-prone part, find counterexamples, reproduce), and a reply from formal-methods author Hillel Wayne questions whether models can choose good system properties. The attached video was not reviewed.

## Influenced pages

- [Acceptance contracts and test oracles](../../training/acceptance-contracts-and-test-oracles.md) — model-checked specifications as an oracle
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — early-user formal-verification result

## Key claims extracted

- Opus 5.5 + Lean formally verified the Claude Agent SDK; a couple of short prompts → 16 PRs fixing bugs and race conditions
- TLA+ also works well; combining Lean and TLA+ helps find data-flow, concurrency and state-management issues; TLA+ preferred for race conditions
- Loop (2026-09-23 follow-up, truncated): build a model of a tricky state machine or race-prone code, find counterexamples (suspected bugs), reproduce them
- Cherny does not know either language well; says Claude is excellent at both
- Hillel Wayne: models have been very bad at proposing even beginner-level high-level system properties (last tried Fable 5.1); Cherny: Opus 5.5 "feels much better"
- Side note: Cherny runs at least 10 Claude Tag/Projects sessions at a time
```

## Schema / vocabulary additions

None.

## Open questions

None.
