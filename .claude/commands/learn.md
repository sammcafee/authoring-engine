---
description: Diff your edits against the generated scaffold and capture what they reveal
---

# /learn — diff capture

Run this after you've edited a batch of drafts. For each one, it finds what
changed between the generated scaffold and your edited version, infers the
generalizable preference each edit reveals, and appends it to
`config/VOICE-LEDGER.md` — so the next draft starts closer to your ear. Like every
other step in this pipeline, this is a reading-and-judgment task for a Claude
Code session, not a diff parser: no code here extracts structured data from a
`git diff`, the model reads the before/after and describes what it means.

## Finding the pairs

For each `drafts/draft_YYYY-MM-DD_<slug>.md` (and any other output type your
project produces the same way):

- Prefer the frozen `drafts/originals/original_YYYY-MM-DD_<slug>.md` baseline
  written by `/draft`.
- If none exists, fall back to git: find the file's first committed version
  (`git log --follow --diff-filter=A`) and diff it against the current state.

Compare bodies only (above any metadata footer). If identical, the draft is
unedited — skip it. If no pair differs, report "No edited drafts found" and
stop.

## Analyze each edited pair

Produce, per pair:

- **WHAT CHANGED** — a bullet list of specific, concrete edits. Name exactly
  what was altered, at the granularity of "removed the scene-opening
  paragraph, replaced with a direct declarative claim," not "tightened the
  opening."
- **DIRECTION** — a 2-3 sentence synthesis of what the edit reveals about the
  preference behind it. Not "prefers clarity" — specific enough to become a
  rule.
- **EDIT NOTES** — verbatim, if you left any inline `[EDIT NOTE: ...]`
  markers explaining a change.

If two or more pairs in this batch, add **PATTERNS ACROSS THIS BATCH**: what
recurs.

## Record

Append each inferred rule to `config/VOICE-LEDGER.md` using its entry shape (see
`docs/voice-ledger-format.md`): polarity (negative = something you removed,
generally the higher-value signal; positive = a move you prefer), category
(diction / construction / structure / tone), verbatim off/good examples, and
the generalized rule.

If an edit is mechanical and repeatable — a specific word or phrase you keep
cutting — propose adding it to `config/voice-rules.local.json` so the gate
catches it automatically next time, instead of relying on you to catch it by
hand in every future draft.

Write a dated log to `feedback/feedback_YYYY-MM-DD.md` (the full per-pair
analysis) for provenance. Report: pairs processed, ledger entries added, and
the single most specific cross-batch pattern in one sentence.
