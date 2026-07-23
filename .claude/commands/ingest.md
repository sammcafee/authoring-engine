---
description: Pull new source material into the project's intake queue, deduped and categorized
---

# /ingest — source intake

Reads raw source material and files it into `sources/processed/<category>/`,
deduped against `sources/manifest.md`. This replaces any inbox-and-cloud-folder
setup (e.g. an email-fed Drive folder) with something that works out of the
box: point it at a **local directory** or a **git repository URL**, no
connector or personal account required. If you do want to pull from a cloud
drive or inbox instead, that's a per-project choice — wire it up as a variant
of this command once you have a connector for it; the manifest/categorize/file
pattern below stays the same either way.

## Setup (once per project)

Define your categories in `config/categories.json` — a flat list of names your
material naturally sorts into (topics, themes, whatever partitions your
subject matter). There's no default list; a generic tool can't guess your
domain. Keep it small (5-10) so classification stays unambiguous.

## Steps

1. **Build the processed list.** Read `sources/manifest.md`; the first
   `|`-delimited field of each line is the dedup key (a stable identifier for
   the source item — a file path, URL, or content hash).
2. **Inventory the intake location.** If given a local directory, list its
   files. If given a git repo URL, clone or pull it shallow into a scratch
   location and list its files. Drop anything already in the processed list.
   If nothing is new, say so and stop — no manifest change needed.
3. **Sort each new item.** Read it; assign exactly one category from
   `config/categories.json` — the one it most directly addresses. Copy it
   into `sources/processed/<category>/`. If an item is unreadable, skip it
   and note that in the report.
4. **Append to the manifest.** Add one line per processed item under a new
   `### YYYY-MM-DD` run heading at the end of `sources/manifest.md`:

   ```
   [dedup key] | [title] | [CATEGORY] | [date processed YYYY-MM-DD]
   ```

   Never edit or reorder existing lines — append only. Commit with a message
   naming the run date and count.

## Notes

- One category per item. If something genuinely straddles two, note the
  ambiguity in the run report rather than silently forcing a fit — that's a
  signal your category list needs adjusting, not something to paper over.
- This command only files material for later use by `/bootstrap-voice` and
  `/draft`. It never rewrites or deletes a source item.
