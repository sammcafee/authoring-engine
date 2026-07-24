# authoring-engine

A self-contained, voice-gated writing pipeline for [Claude Code](https://claude.com/claude-code).
Point it at a body of your own writing, and it builds a profile of your
voice, then runs a generate → gate → review → edit → learn loop for new
pieces, so each one starts a little closer to how you actually write.

It's a generic mechanism, not tied to any particular author, subject, or
publishing format — the repo ships with fabricated example material so you
can run the whole loop end to end before pointing it at your own writing.

## What it does

- **`/bootstrap-voice`** — analyze a corpus of your own writing (a folder, or
  material filed by `/ingest`) and produce a voice profile: what your writing
  actually does, its sentence-level habits, its structure, and the patterns
  that should never appear in generated output.
- **`/ingest`** — pull new source material into a categorized, deduped intake
  queue, from a local folder or a git repo — no cloud connector required.
- **`/draft`** — generate a scaffold grounded in your voice profile, run it
  through the deterministic gate, give it one review pass, and hand it off
  for your edit. Short-form (one post) and long-form (bottom-up through
  raw-statements → clusters → skeleton → draft) modes.
- **`tools/voice-gate.py`** — a dependency-free, line-anchored scanner for
  mechanical voice tells (em-dashes, recognized AI-tell words, banned
  phrases). Hard fails block a commit; advisories just flag for your
  judgment. Rules are data (`tools/voice-rules.json` + your project's
  `config/voice-rules.local.json` overlay), not code, so tuning them never
  means touching the script.
- **`/learn`** — after you've edited a batch of drafts, diff each one against
  its frozen original, infer what the edit reveals, and append it to
  `config/VOICE-LEDGER.md`.

What it deliberately doesn't do: ship a draft without your edit, generate
from anything not grounded in your own voice profile, or claim to
automatically fact-check anything. See `docs/AUTHORING-STRATEGY.md` for why.

## Requirements

- [Claude Code](https://claude.com/claude-code)
- git
- Python 3 (stdlib only — `tools/voice-gate.py` has zero third-party
  dependencies)

## Setup

1. Clone this repo (or use it as a template for a new one).
2. Copy the example config into place:
   ```sh
   cp -r config.example config
   ```
3. Enable the pre-commit voice gate (optional but recommended):
   ```sh
   git config core.hooksPath tools/hooks
   ```

From here, either try the quickstart below first (recommended — it's a five
minute walkthrough using bundled fabricated material), or skip straight to
"Using this for a new project."

## Quickstart (using the bundled example)

The repo ships with `config.example/sample-source/` — three short, fully
fabricated posts — so you can run the whole loop before touching your own
material:

```sh
cp -r config.example config
```

Then, in Claude Code:

1. `/bootstrap-voice` — point it at `config/sample-source/`. It'll produce a
   voice profile under `voice/` from the example posts.
2. `/draft` — generate a new short-form piece grounded in that profile.
3. `tools/voice-gate.sh drafts/<file>.md` — check it by hand, or let the
   pre-commit hook do it for you.
4. Edit the draft as if it were real. Then run `/learn` to see how the
   diff-capture loop works.

Once you're comfortable with the shape of it, move on to the real thing
below.

## Using this for a new project

This is the full loop, start to finish, for a real project rather than the
bundled example. It assumes you've done the one-time Setup steps above.

1. **Feed it your own writing.** Two ways in: point `/ingest` at a folder or
   a git repo of your existing material (a blog archive, old essays, past
   work — whatever you have), which sorts it into a categorized, deduped
   intake queue under `sources/processed/`; or skip straight to step 2 and
   hand `/bootstrap-voice` a folder directly if you don't need the sorting
   step. Define your own categories in `config/categories.json` first if
   you're using `/ingest` — there's no default list, since a generic tool
   can't guess your subject matter.
2. **Run `/bootstrap-voice`.** Point it at your own material (either the
   folder you fed `/ingest`, or `sources/processed/` if you used it). This
   is a guided analysis, done in conversation with Claude Code, that separates
   your writing into "authentic" and "uncertain/AI-assisted" buckets, then
   produces `voice/profile/`, `voice/purest/` (exemplars), `voice/eval-only/`
   (anti-examples, never generation sources), and a starter `config/VOICE.md`.
3. **Draft.** Run `/draft` — short-form for a single piece (angle → draft →
   gate → one review pass → output), or long-form for anything with real
   internal structure, like a chapter (bottom-up through `01-raw-statements.md`
   → `02-clusters.md` → `03-skeleton.md` → `04-draft.md`). Every generated
   passage is grounded in the voice profile from step 2 and gated
   automatically before you see it.
4. **Edit it.** The output is a scaffold, not a final — edit it the way you
   normally would. `/draft` keeps a frozen, unedited copy alongside it
   specifically so the next step has a baseline to diff against.
5. **Run `/learn`.** After you've edited a batch, this diffs each one
   against its frozen original, infers what the edit reveals, and appends
   entries to `config/VOICE-LEDGER.md` — so the next `/draft` starts closer
   to your actual voice. A repeatable, mechanical edit (a word or phrase you
   keep cutting) gets proposed as a new rule for
   `config/voice-rules.local.json` instead of relying on you to catch it by
   hand every time.

Steps 3-5 repeat indefinitely as your ongoing writing loop. Revisit step 2
occasionally as your voice profile needs sharpening — it's a starting point,
not a one-shot oracle.

## Project layout

```
tools/                  the deterministic gate + starter rules + hooks
.claude/commands/        the four protocol commands (see above)
docs/                    AUTHORING-STRATEGY.md, voice-ledger-format.md
config.example/          placeholder rules + fabricated sample posts
voice/                   built by /bootstrap-voice (not checked in until you run it)
drafts/, config/VOICE-LEDGER.md built by /draft and /learn as you use the pipeline
```

## Design philosophy

Voice is judgment, so everything upstream of the deterministic gate — the
analysis in `/bootstrap-voice`, the drafting in `/draft`, the diff-reading in
`/learn` — is a guided protocol for a Claude Code session to work through
with you, not a script trying to automate judgment away. Only the mechanical,
genuinely rule-based parts (the gate itself, hooks, CI) are code. See
`docs/AUTHORING-STRATEGY.md` for the full reasoning, including what this
engine deliberately does not try to do.
