---
title: Matt Pocock on X: "No video today. But my thoughts are around the benefits of up-front research as part of PRD design. 'Research' in AI coding basically means doing an Explore phase with an agent and caching it - usually saving it to a markdown file in the repo. This can be really useful for" / X
type: source
source_type: tweet
url: https://x.com/mattpocockuk/status/2027319225400856992
fetched: 2026-04-22
---

# Matt Pocock on X: "No video today. But my thoughts are around the benefits of up-front research as part of PRD design. 'Research' in AI coding basically means doing an Explore phase with an agent and caching it - usually saving it to a markdown file in the repo. This can be really useful for" / X

No video today.
But my thoughts are around the benefits of up-front research as part of PRD design.
'Research' in AI coding basically means doing an Explore phase with an agent and caching it - usually saving it to a markdown file in the repo.
This can be really useful for when the thing you're exploring is hard to access, such as API docs or a internal process. I've been using it to create docs on a repo that's external to my codebase so I can integrate with it.
This means that agents in the repo after that can reference that piece of research, making future Explore phases more efficient.
However, I'm always thinking about the TTL for any piece of research I do. If the cache goes stale, the research will be useless and will actively harm the coding agent.
Or if the research is too lossy (i.e. summarized poorly) it might confuse the agent and result in poor code.
So, pro's and cons - but essentially the same tradeoffs as traditional caching.
