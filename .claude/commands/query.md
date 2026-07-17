---
description: Ask the AI Wiki query layer a question — routed through the query-orchestrator for a grounded, engine-verified answer.
---

Spawn the `query-orchestrator` subagent (Agent tool, `subagent_type: query-orchestrator`) with the following question, passed verbatim and unmodified:

$ARGUMENTS

When it returns, relay its merged answer to the user in full — verdict, rationale with citations, proof, recommendation, caveats. Add nothing from your own knowledge; if the orchestrator reports that neither the wiki nor the graph contains the answer, that IS the answer.

If no question was provided above, ask the user what they want to know about the AI Wiki.
