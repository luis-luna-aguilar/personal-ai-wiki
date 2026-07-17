# Authoring Guide — Controlled English (ACE) Sidecars

**Status:** Draft (Phase 0 / T1) · destined for `system/authoring-guides/controlled-english.md` at adoption.
**Audience:** the prose→ACE sub-agent and any human reviewing a `.ace` sidecar.

A `.ace` sidecar restates a wiki page's **assertable facts** in Attempto Controlled English — a strict subset of English that the APE parser turns into logic deterministically. This guide is the closed set of rules for writing ACE that **parses** and **maps to the right ontology terms**. Every rule here is one APE actually enforces or that our experiments proved necessary.

> **Golden rule:** if a sentence is not a *checkable fact*, it does not belong in the `.ace`. Marketing phrasing, rhetoric, and narrative stay in the Markdown.

---

## 1. What goes in (and what doesn't)

- **In:** type statements (`X is a Y`), relationships (`X verbs Y`), enumerations, cardinality and conditional rules, datatype-valued facts.
- **Out: aliases.** Alias names are recorded in the page's frontmatter `aliases:` array and as `skos:altLabel` triples in the `.ttl` — **never as ACE identity sentences** (see rule 3 below).
- **Out:** vague adjectives ("leading", "comprehensive", "robust"), tone, history-as-narrative, anything with no truth value. Dropping these is **not** lossy — they carry no fact the graph can hold (see `AGENTS.md` Rule 5: this is the fact-vs-rhetoric line).

---

## 2. Sentence shapes (the only ones allowed)

| Shape | Example | Compiles to |
|---|---|---|
| Class membership | `Claude-Code is a software-application.` | `aiw:claude-code a schema:SoftwareApplication` |
| Relationship (SVO) | `Claude-Code integrates-with Cursor.` | object property triple |
| ~~Identity / alias~~ | ~~`Claude-Code is Claude-CLI.`~~ | **retired** — see rule 3 |
| Coordination | `… integrates-with Cursor and integrates-with Codex.` | two triples |
| Enumeration | `Every license-model is an open-source or is an open-weights or is a closed-source.` | `owl:oneOf` |
| Cardinality | `Every benchmark-result has exactly one score-value.` | SHACL `minCount/maxCount` |
| Conditional | `If a benchmark-result has a score-unit that is a percentage then a benchmark-result must have a score-value that is at most 100.` | SHACL `sh:or` / SWRL |

---

## 3. Hard rules (APE rejects violations — proven)

1. **Every noun phrase needs a determiner — mass nouns included.** ✗ `achieves benchmark-result` → ✓ `achieves a benchmark-result`. ✗ `has license-model` → ✓ `has a license-model`. This is the #1 cause of parse failures.
2. **Coin hyphenated *verbs*, never noun+preposition.** ✗ `Claude-Code is a fork-of Codex.` → ✓ `Claude-Code is a fork of Codex.` (noun `fork` + the function word `of`). Coin verbs like `integrates-with`, `achieved-by` freely.
3. **Aliases never appear in ACE at all.** The old convention (`X is Y.` → `owl:sameAs`) minted a second, bare IRI for the alias that inherits every type through `sameAs` and then fails the entity/tool shapes (no label/comment/provider). Per project rules, many names collapse onto **one** IRI: record aliases in the `.md` frontmatter `aliases:` array **and** as `skos:altLabel` (with a language tag) on the primary individual in the `.ttl`. If a source sentence is only an alias statement, classify it DROP with reason "alias — recorded as altLabel".
4. **Proper names are Capitalized; everything else is lowercase.** A Capitalized token is treated as a named individual (→ `aiw:<slug>`) with **no lexicon entry needed**. A common noun/verb must be lowercase **and** declared in the lexicon map.
5. **One word = one meaning; reuse the lexicon.** Never introduce a synonym for a relation/type that the map already names. Normalize the source word to the canonical term.
6. **Use the closed deontic/quantifier vocabulary**, never paraphrases: `must`, `must not`; `every / each / all / no / only`; `at most N / at least N / exactly N`; `must be one of {…}` (written as `… or … or …`); `if … then … must …`. Collapse "should/needs to/has to" → `must`.

---

## 4. The word-class ⇄ ontology-role contract

What you choose as a word-class **is** what it becomes in the graph. Get this right and compilation needs no guessing:

| Write it as… | …and it must be, in the map | …compiles to |
|---|---|---|
| common **noun** | `Class` | `x a <ClassIRI>` |
| **proper name** (Capitalized) | *(instance — not in the map)* | `aiw:<slug>` |
| transitive **verb** | `ObjectProperty` | `s <propIRI> o` |
| noun used as a value carrier (`has a score-value`) | `DatatypeProperty` | datatype triple + Rule-10 shape |
| **adjective** (`is multimodal`) | `Qualifier` | boolean/qualifier property |
| noun naming a closed set (`license-model`) | `Class` + `enumeration` | `owl:oneOf` |

If a word you need isn't in the lexicon map, **do not invent an IRI** — flag it as a new term (it becomes a VCR). The sub-agent never mints.

---

## 5. Datatype values (Rule 10)

State the value with its determiner; the **domain** (datatype, unit, range) lives in the lexicon map, not in the sentence. "A benchmark-result has a score-value" + the map's `{datatype: xsd:decimal, unit: percentage, min: 0, max: 100}` → a SHACL property shape (see `aiw:BenchmarkPercentageRangeShape`, VCR-0003). A structured value with internal parts (amount + currency, magnitude + unit) reifies to its own individual rather than a bare literal — `aiw:BenchmarkResult` itself is exactly this reification (`onBenchmark` + `achievedBy` + `scoreValue` + `scoreUnit` + `asOf`), never a bare decimal hung off the model.

---

## 6. Completed checklist (paste into the proposal per page)

- [ ] Every assertable fact from the Markdown is represented; all rhetoric dropped (Rule 5 fact-vs-rhetoric honored).
- [ ] Every noun phrase has a determiner (incl. mass nouns).
- [ ] No noun+preposition coined as one token.
- [ ] Aliases kept OUT of the ACE — frontmatter `aliases:` + `skos:altLabel` in the `.ttl` only.
- [ ] Every common word resolves to a lexicon-map term; new words flagged as VCRs (none minted).
- [ ] Constraints use the closed deontic/quantifier vocabulary.
- [ ] Datatype-valued facts carry their domain via the map.
- [ ] The whole `.ace` **passes `validate-ace.sh` (APE)** — the objective gate.

---

## 7. Known pitfalls (from the experiment)

- `-guess` mode makes APE *guess* word-classes and silently mistype common nouns as proper names — **never rely on it**; always use the declared lexicon.
- A constraint must not assign a property a range that conflicts with the map (caught by the coherence checker, T11).
- A model or tool with multiple public names (e.g. a codename used pre-launch vs. its shipped product name) is recorded as `skos:altLabel` on the canonical `aiw:<slug>` individual — never as a second `owl:sameAs` individual.
