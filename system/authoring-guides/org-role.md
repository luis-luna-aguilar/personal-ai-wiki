# Authoring Guide — `org:Role` Individuals with SKOS Annotations

Read this before authoring a named user-role/permission-level individual (e.g. "Admin," "Member," "Owner") for a `schema:SoftwareApplication`'s access model. This is a **structural pattern**, not a single term: it composes the already-confirmed `org:Role` class with a SKOS annotation pair. `lexicon-map.yaml` catalogs individual word↔IRI mappings; it does not, and should not, catalog this multi-property recipe — that's what this file is for.

**Status in this deployment: dormant, not yet used.** This guide was ported from the source project (MUSCLE company-brain), where it modeled product-permission roles like "Super Admin"/"Admin"/"Analyst" for MUSCLE Control Tower, each with a documented, detailed permission boundary ("can view and download reports only; cannot configure operational tools"). Nothing currently in `wiki/tools/*.md` documents a tool's access model at that level of per-role detail — sources mention plan/seat tiers in passing (e.g. Claude Code's Max/Team/Enterprise plans, "admin can enable in settings") but don't yet state a role's full permission boundary the way this pattern requires. **Keep the pattern below on file for when a source does** (e.g. a future ingestion of a tool's admin-console documentation); don't force today's thin plan-tier mentions into this shape.

---

## The pattern

Each role is a plain `org:Role` individual, annotated with `skos:prefLabel`/`skos:definition` — **not** dual-typed `skos:Concept`:

```turtle
aiw:claude-code-team-admin a org:Role ;
    skos:prefLabel "Team Admin"@en ;
    skos:definition "Can enable or disable research-preview features (e.g. dynamic workflows) org-wide via managed settings; individual members cannot override an admin-disabled feature."@en .
```

*(Illustrative — no source yet documents Claude Code's admin/member role boundary in enough detail to commit this individual; write the real one once a source does.)*

- [ ] The role individual is typed **`org:Role`** — never a bespoke `swe:`/`biz:` role class. `org:Role` is already confirmed and general enough (inherited via VCR-0001).
- [ ] `skos:prefLabel` carries the display name exactly as the source names it ("Team Admin," not "TeamAdmin" or "team_admin").
- [ ] `skos:definition` carries the permission boundary verbatim from the source (what the role *can* and *cannot* do) — this is where Rule 5 fidelity actually lives for this pattern; don't compress "can enable dynamic workflows org-wide, individual members cannot override" down to "an admin role."
- [ ] The application that defines these roles links to each one via `swe:hasUserRole` (inherited, confirmed) — the role individual itself does **not** point back to the application.
- [ ] **Do not add `a skos:Concept`.** A role is a position/permission level, not an open-ended subject-matter tag — it fails `skos-concept.md`'s own test (no `schema:knowsAbout`/`schema:about` ever targets a role). The `skos:prefLabel`/`skos:definition` predicates are reused here purely as a convenient annotation vocabulary, not as a signal that this is a `skos:Concept`.

---

## Before minting anything, check for reuse

- [ ] **Does this exact role already exist under a different application?** Grep `wiki/**/*.ttl` for `a org:Role` before creating a new individual — a role named identically on two different tools (e.g. two products both having an "Admin" role) should still get **two separate individuals** if their permission boundaries differ (they're different roles that happen to share a display name), but reuse the same individual if the source is describing the literal same role definition copied across pages.
- [ ] **Do not mint a native role class.** "Admin," "Member," etc. are `org:Role` individuals, full stop — there is no scenario in this project's vocabulary where a bespoke `swe:AdminRole`-style class adds anything `org:Role` + `skos:prefLabel`/`skos:definition` doesn't already say.

---

## Naming convention

- [ ] Role individual: `aiw:<tool-slug>-<role-slug>` in lowercase-kebab-case (e.g. `aiw:claude-code-team-admin`) — prefixing with the tool slug avoids collisions between two different tools' same-named roles that turn out to have different permission boundaries (see the reuse check above).

## Before finishing

- [ ] Confirmed the role is typed `org:Role` only (not also `skos:Concept`).
- [ ] Confirmed `skos:definition` captures the full permission boundary from the source, not a paraphrase.
- [ ] Grepped `wiki/**/*.ttl` for `a org:Role` and confirmed this role doesn't already exist under a different page.
- [ ] If this is the first real (non-illustrative) role committed under this pattern, update the "Status in this deployment" note above — the pattern is no longer dormant once a page actually uses it.
