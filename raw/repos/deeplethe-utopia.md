---
title: deeplethe/utopia: World's first open-source enterprise world model. · GitHub
type: source
source_type: repo
url: https://github.com/deeplethe/utopia
fetched: 2026-09-09
---

# deeplethe/utopia: World's first open-source enterprise world model. · GitHub

**The enterprise world model built by [DeepLethe](https://deeplethe.com).** It is the first open substrate for knowledge engineering that learns passively and governs itself. Where a knowledge graph or a vector store works to hold present knowledge, Utopia puts time awareness and ontology in the base layer: the knowledge system evolves as material arrives, and conflict detection, reasoning and decision making all run against that ontology. It deploys offline, so a company can stand up a knowledge foundation, a decision core its agents can trust, and a compliance audit trail on hardware it controls.

> Please note: we would rather this project were not framed as an open-source take on Palantir. It is **a different route to enterprise intelligence, built bottom up from knowledge governance to trustworthy decisions and simulation**.

---

Utopia.Bitemporal.graph.and.Derivation.mp4

[
](https://private-user-images.githubusercontent.com/145302500/643871134-aa226443-75de-437e-bd80-88e592ed8457.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODg5ODgwMjMsIm5iZiI6MTc4ODk4NzcyMywicGF0aCI6Ii8xNDUzMDI1MDAvNjQzODcxMTM0LWFhMjI2NDQzLTc1ZGUtNDM3ZS1iZDgwLTg4ZTU5MmVkODQ1Ny5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwOTA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDkwOVQyMTAyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00Y2Q2MWY3YTZlY2NhNzE1ZjFhYzZjNjRhMjE0MDZkN2NjYTE4NTUyYTJhOTBjMTJiMTlhNzRmNWUxMGMyMjU1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9dmlkZW8lMkZtcDQifQ.zuhvjsO6khSLE1GbNssmKbpbljFqGjDF_2qjfjVuWKo)

---

We gave it a somewhat romantic name, **Utopia**. Ptolemy's geocentric model was taken for truth for a very long time, then falsified step by step by Copernicus, Kepler, Galileo and Newton. Looking back, what we keep is not only that heliocentrism turned out to be right; it is how that history unfolded.

Where existing vector stores and knowledge graphs work to get present knowledge right, one of Utopia's founding aims is to record the whole course of changing understanding. Engineered, that becomes a **bitemporal knowledge graph**. When a decision is reviewed later, the system can produce the full course it took and the grounds it rested on. To make this hold up in practice we have iterated at length against public corpora spanning enterprise records, education, finance, law and research. Temporality is only one facet; for how knowledge is taken in, how the future is reasoned about, and how logic bounds action, see [utopia.bi/philosophy](https://utopia.bi/philosophy).

One Rust binary and one Postgres. Full-text search is embedded in the binary, vectors go in pgvector, and the job queue is a table: nothing else to run.

|  |  |
| --- | --- |
| **A complete application** | A system console, a graph browser and an ontology workbench in one web UI. A product, not a library: install it and it works. |
| **Knowledge ingest** | Upload PDF, DOCX, PPTX, XLSX, XLS, ODS, CSV, TSV, Markdown, HTML or plain text, with legacy encodings detected on the way in. Web pages, RSS, GitHub, Jira, Notion, WebDAV and S3-compatible buckets sync on a schedule; everything else comes in through the API. |
| **Search and chat** | Full-text on Tantivy, vectors on pgvector, fused with RRF. Answers stream with inline citations that open the passage they came from. Any OpenAI-compatible endpoint works (DeepSeek, Qwen, GLM, Ollama, vLLM), so the whole system can run air-gapped. |
| **Agent harness and agentic RAG** | The whole system can be driven through conversation. The built-in agent searches documents, walks the graph (an entity's facts as of any date, or what changed in a period) and queries a mounted database. The same read-only tools are exposed over MCP. |
| **Ontology and cold start** | A new knowledge base has no vocabulary of its own; it starts from the packs you pick at creation. Five ship inside the binary: schema.org, W3C Org, PROV-O, FOAF and IOF Core ([ask for your industry](https://github.com/deeplethe/utopia/issues/new?labels=enhancement&title=Ontology%20pack%20request)). Terms outside the packs are counted as they appear; confirm the common ones and they join the ontology. |
| **Bitemporal graph** | Extraction turns documents into entities and facts, following an ontology you can edit. Every fact carries when it held and where it came from. Correcting a fact closes the old version and links the new one to it rather than overwriting, so the graph keeps two timelines: when something was true in the world, and when the system came to believe it. |
| **Entity resolution and review** | Duplicates are resolved in three stages: exact name or alias, embedding similarity, then a model's call on the doubtful pairs. Every merge can be undone. Uncertain cases go to a review queue: low-confidence extractions, suspected duplicates and cardinality conflicts. |
| **Reasoning and derivation** | Ontology axioms compile into rules: transitivity, symmetry, inverses and relation hierarchy derive new facts by forward chaining. Derivation is off by default, since a wrong axiom derives wrong facts. A derived fact is marked as such on the graph, carries validity and confidence like any other, and shows what it was derived from. When it contradicts an asserted fact, the asserted one stands. |
| **Conflict detection** | Three kinds of conflict, three sets of choices. A new fact that clashes with an older one: close the old, keep both, or reject the new. Data that breaks an axiom (self-loop, asymmetry, transitive cycle, cardinality): retract the fact, relax the axiom, or accept both. The ontology itself is checked first, because violations of a self-contradictory ontology are noise. |
| **Ontology-driven querying** | Mount a database on a base (Postgres, MySQL and the engines that speak its protocol, Trino for Iceberg / Delta Lake / Hive, Databricks, Snowflake) and chat can query it alongside the documents. The agent proposes how its tables map onto the ontology, and you confirm. The method behind it, [Ontology2SQL](https://github.com/deeplethe/ontology2sql), is state of the art on BIRD Mini-Dev for SQLite and PostgreSQL ([submission](https://github.com/bird-bench/bird-bench.github.io/pull/218)). |
| **Multi-user and permissions** | Each knowledge base has its own members and roles: owner, admin, editor and viewer. Open bases are readable by everyone in the deployment, restricted ones only by invitation. The first account registered becomes the system administrator. |
| **Decision ledger** | Confirming or rejecting a fact, merging or reverting an entity, rebuilding the graph: each leaves a record of who, when, and what the object looked like at the time. The ledger is append-only, and a record outlives its object, even the base it belonged to. |
| **[Decision intelligence (in development)](#roadmap)** | Record a decision, replay both what was understood and the course it took, and reason over overlaid scenarios. |

Requirements: Docker (local development also needs Rust 1.85+, Node 20+, pnpm).

Start from the prebuilt image:

```
git clone https://github.com/deeplethe/utopia.git
cd utopia
docker compose --profile app up -d
```

Open <http://localhost:1516> and register. The first account automatically becomes the administrator, and a public knowledge base readable by everyone is created at the same time. Before extracting business documents, configure the model endpoints (chat and embedding) under Administration → Models.

The database password (`UTOPIA_DB_PASSWORD` in `.env`, default `utopia`) is applied when the data volume is first initialised. To change it on a running deployment, change it in the database as well — `docker compose exec db psql -U utopia -c "ALTER USER utopia PASSWORD '<new password>'"` — or start over with `docker compose --profile app down -v`, which deletes all data.

Or build from source:

```
docker compose -f docker-compose.yml -f docker-compose.build.yml --profile app up -d --build
```

```
# 1. Postgres with pgvector
docker compose up -d db

# 2. Backend on :1516, runs migrations on startup
cargo run -p utopia-server

# 3. Frontend on :5173, proxying /api to the backend
cd web && pnpm install && pnpm dev
```

* **Decision reasoning**: constraint computation, and replaying a decision after the fact
* **Business rules**: rules written by people over an entity's attribute facts, a threshold or a category set, that classify it as a derived fact with the rule and the premises as its explanation ([#277](https://github.com/deeplethe/utopia/issues/277))
* **Execution gate**: checking an agent's calls against ontology rules and symbolic logic
* **MaxCompute**: mapping exploration and Ontology2SQL over Alibaba Cloud MaxCompute (Iceberg / Delta Lake via Trino, Databricks and Snowflake are in, awaiting a run against a real cluster)
* **More sources**: a ClickHouse driver; a Feishu connector
* **Time to the moment**: an `instant` precision beside year / month / day, for sources that carry a real timestamp. Today a connector rounds it to a UTC day, which can shift an event across midnight by one day
* **Agent memory over MCP**: episode writes, the retrieve endpoint, and the MCP server
* **Enterprise**: OIDC SSO, backup and restore commands, benchmarks at 100k documents

Utopia is still at **v0.1**. The database schema evolves between versions and migrations only roll forward, with no rollback. Pin a specific version with `UTOPIA_IMAGE` in production, and back up the database along with the `data` directory before upgrading.

Please read [SECURITY.md](/deeplethe/utopia/blob/dev/SECURITY.md) before exposing it to the public internet.

## Community

* 💬 [Discussions](https://github.com/deeplethe/utopia/discussions): discuss the project, share your experience, and leave feedback
* 🐛 [Issues](https://github.com/deeplethe/utopia/issues): report bugs, ask design questions, and submit feature requests
* 🤝 [Contributing](/deeplethe/utopia/blob/dev/CONTRIBUTING.md): development setup, pre-push checks, and DCO sign-off
* 🔌 [Ontology2SQL](https://github.com/deeplethe/ontology2sql): the ontology-driven text-to-SQL method referenced above

[Apache-2.0](/deeplethe/utopia/blob/dev/LICENSE)
