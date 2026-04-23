Return valid JSON only.

The JSON object must have exactly these top-level keys:

- `answer`: string
- `gaps`: array of objects with keys:
  - `type`: string
  - `message`: string
  - `suggested_addition`: string
- `notes`: array of strings

Rules:

- `answer` must be a complete synthesized response.
- `gaps` is mandatory.
- If there are no major gaps, include one gap entry with:
  - `type`: `no_major_gap`
  - `message`: `No major knowledge gaps detected for this query.`
  - `suggested_addition`: ``
- Do not include consulted pages in the JSON. They are attached separately by the runtime.
- Do not wrap the JSON in markdown fences.

