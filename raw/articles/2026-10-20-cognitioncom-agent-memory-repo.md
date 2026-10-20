---
title: Agent Memory Repo
type: source
source_type: article
url: https://cognition.com/agent-memory-repo
fetched: 2026-10-20
---

# Agent Memory Repo

The median request takes 80 ms. But 1 request in 100 takes 2.4 seconds, and nobody knows why. John asks an agent to find out. The agent starts four agents, one each for the database, the runtime, the cache, and the load balancer. First it makes a folder for the swarm in John’s memory repo:

```
memory-john/
  MEMORY.md
  team_structure.md
  projects/
    payments.md
    website.md
  swarms/
    slow-checkout/         ← one folder per swarm
      README.md            ← the goal and the rules
      findings.md          ← what each agent has measured
      questions.md         ← agents ask each other
      agents/
        database.md        ← one notes file per agent
        runtime.md
        cache.md
        load_balancer.md
      scripts/
        bench.sh           ← the one benchmark every agent runs
```

The `README.md` tells every agent how to use the folder:

swarms/slow-checkout/README.md

```
# Swarm: why is checkout slow for 1 request in 100?

- Median is 80 ms. The slowest 1% take 2.4 s. The goal is under 500 ms [source: https://example.com/sessions/300]
- Measure only with [[swarms/slow-checkout/scripts/bench.sh]], so numbers compare
- Before each step, pull and read findings and questions
- Write what you measure in findings, including what you rule out
- If another agent’s area might explain what you see, ask in questions
```

Each agent clones the repo and digs into its own area. After an hour, `findings.md` holds three facts. None of them explains the problem:

swarms/slow-checkout/findings.md

```
- Database: queries are fast. But in bursts, requests wait up to 2 s for a free connection [source: https://example.com/sessions/301]
- Runtime: garbage collection freezes the server for about 400 ms, once every 10 seconds [source: https://example.com/sessions/302]
- Load balancer: ruled out. The slow requests stay slow with it bypassed [source: https://example.com/sessions/303]
```

The runtime agent cannot see why memory fills up on a 10-second beat. It asks the swarm. So does the database agent:

swarms/slow-checkout/questions.md

```
- Runtime asks: does anything run every 10 seconds and use a lot of memory? [source: https://example.com/sessions/302]
  - Cache answers: yes. The price cache refresh runs every 10 seconds and rebuilds the whole price table, about 2 GB [source: https://example.com/sessions/304]
- Database asks: when exactly are the freezes? My bursts are also 10 seconds apart [source: https://example.com/sessions/301]
  - Runtime answers: at :03, :13, :23 of each minute. Your bursts start within 50 ms of each one [source: https://example.com/sessions/302]
```

Now the three facts connect, and the database agent writes the cause:

swarms/slow-checkout/findings.md

```
- Cause: the price cache refresh rebuilds a 2 GB table every 10 seconds. That triggers a 400 ms freeze. Requests pile up during the freeze, then all ask for a database connection at once, and the pool of 20 runs out [source: https://example.com/sessions/301] [source: https://example.com/sessions/302] [source: https://example.com/sessions/304]
- Fix: refresh only the prices that changed. The slowest 1% drop from 2.4 s to 310 ms on bench.sh [source: https://example.com/sessions/304]
```

No agent could have found this alone. The cache agent saw nothing wrong with its refresh. The database agent saw waits with no cause. The runtime agent saw freezes with no source.

All four agents write to the same two files the whole time. Git merges most of their commits. When two agents edit the same line, git rejects the second push, and that agent reads both versions before writing one.

When the swarm finishes, the first agent adds one line to the index in `MEMORY.md`:

MEMORY.md

```
## Index
- [[team_structure]]
- [[projects/payments]]
- [[projects/website]]
- [[swarms/slow-checkout/README]]
```

The folder stays in the repo. When John later asks why search is slow, that session follows the link, reuses `bench.sh`, and checks for freezes first.
