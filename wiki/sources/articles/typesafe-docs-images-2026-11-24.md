---
title: TypeSafe docs — Images
type: source
source_type: article
source_file: raw/articles/2026-11-24-docstypesafeai-images.md
url: https://docs.typesafe.ai/images
ingested: 2026-11-24
domains: [models]
---

# TypeSafe docs — Images

TypeSafe's documentation page on sending images to Jev. An image can go anywhere text can in a System One request (the state, a question's instructions, its criteria), and every question type accepts it. Images are referenced by strings that point into a top-level `assets` map; the SDKs create these references automatically. The feature is labelled "Dreamer-ready": meant for prototypes, not yet production-ready, with format, answers and limits subject to change. The companion Box reference page (`raw/articles/2026-11-24-docstypesafeai-primitives-box.md`) describes the Box answer format. The page is undated; read 2026-11-24.

## Influenced pages
- [Jev](../../models/jev.md) — image input and Box questions; "no image input" caveat replaced
- [State of Models](../../state-of/models.md) — Jev line no longer says "text only"

## Key claims extracted
- Jev 1.13 and Jev 1.14 accept images; Box questions need Jev 1.14
- Images and Box questions are off by default; each request needs the `TypeSafe-Danger-Zone-Images: true` header
- A Box answer gives top, bottom, left and right edges as fractions of the image size, plus a confidence from 0 to 1
- A Box question has no "not found" answer; pair it with a Noul asking whether the target is present
- Each reference to an image adds another copy to what the model reads and counts toward the request limit
