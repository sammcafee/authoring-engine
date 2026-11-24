---
description: Generate a grounded draft, gate it, review it, and hand it off for your edit
---

# /draft — generate, gate, review

Two modes, same underlying loop (generate a scaffold grounded in your voice
profile → run the deterministic gate → one review pass → hand off for your
edit). Pick the one that matches what you're writing; both produce a draft
you edit yourself, never one that ships ungrounded or unedited.

- **Short-form** (a single post, one work session): one prompt in, one draft
  out.
- **Long-form** (a chapter, a report, anything with real internal structure):
  bottom-up through four stages, so a diff at any stage shows exactly what
  changed and voice only re-enters at the last one.

Both modes ground every generated passage in `voice/profile/` and exemplars
from `voice/purest/` (never `voice/eval-only/`) — run `/bootstrap-voice`
first if those don't exist yet.

## Short-form mode

1. **Angle.** Pick (or take as input) a specific claim or argument for this
   piece — not a topic, an actual point of view. If you're rotating through
   a fixed set of themes, track that rotation in `config/` however suits your
   project; nothing here prescribes a cadence.
2. **Draft.** Write full prose grounded in the voice profile and purest
   exemplars. Apply your project's local overlay rules (`config/voice-rules.local.json`)
   for anything medium-specific (length, attribution conventions, opening
   form).
3. **Gate.**
   ```sh
   tools/voice-gate.sh drafts/<file>.md
   ```
   Any hard fail gets fixed before you see the draft, not after. Advisories
   are for your judgment.
4. **Review, one lens.** Re-read the draft against your project's structural
   checklist (whatever "doesn't sound like the writer" looks like for this
   medium — preamble, tidy resolving endings, hedging, generic openers).
   Record the result in the draft's metadata footer. A fail here means fix
   it now, not after you've handed it off.
5. **Output.** Write `drafts/draft_YYYY-MM-DD_<slug>.md` plus an identical
   frozen copy at `drafts/originals/original_YYYY-MM-DD_<slug>.md` — you
   never edit the frozen copy; it's the baseline `/learn` diffs against
   later. Report the filename and anything still failing after one
   revision. Don't quote the draft back — you edit the file directly.

## Long-form mode (per chapter/section)

Work bottom-up, in order, one file per stage under
`chapters/<name>/`:

1. **`01-raw-statements.md`** — atomic claims pulled from any existing source
   material, neutral and voiceless on purpose. No existing material? Run
   `/interview` first: it produces this file (and the chapter's stories,
   evidence, and controversy prep) from conversation with you, so you start
   here at stage 2.
2. **`02-clusters.md`** — group the statements into themes. This is the real
   thinking: what belongs together, what the through-lines are.
3. **`03-skeleton.md`** — section order built from the clusters.
4. **`04-draft.md`** — prose in your voice. This is the only stage where
   voice comes back; run the gate and one review pass here exactly as in
   short-form mode, steps 3-4 above.

Generate, then critique, before committing at every stage — a stage's diff
is reviewed against the stage before it, not just against the source. Nothing
advances silently.
