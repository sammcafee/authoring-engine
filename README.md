# authoring-engine

A self-contained, voice-gated writing pipeline for [Claude Code](https://claude.com/claude-code).
Point it at a body of your own writing, and it builds a profile of your
voice, then runs a generate → gate → review → edit → learn loop for new
pieces, so each one starts a little closer to how you actually write.

This is a generic extraction of a pattern that's been running in production
across two personal projects for a few weeks: a book manuscript and a
short-form content pipeline. Nothing here is specific to either — it's the
mechanism, with the personal material stripped out and replaced by an
example you can run end to end before pointing it at your own.

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
4. Point `/bootstrap-voice` at your own writing to replace the example
   profile with a real one, once you've tried the quickstart below.

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

Once you're comfortable with the shape of it, point `/ingest` and
`/bootstrap-voice` at your own writing and start over for real — `config/`
(not `config.example/`) is gitignored-by-convention for personal projects
that fork this repo privately; if you're keeping your fork public, keep your
real voice material and any confidential guardrails out of it.

## Project layout

```
tools/                  the deterministic gate + starter rules + hooks
.claude/commands/        the four protocol commands (see above)
docs/                    AUTHORING-STRATEGY.md, voice-ledger-format.md
config.example/          placeholder rules + fabricated sample posts
voice/                   built by /bootstrap-voice (not checked in until you run it)
drafts/, config/VOICE-LEDGER.md built by /draft and /learn as you use the pipeline
```

## Where this came from

Extracted from two production repos that share a common shape but were never
designed as a reusable tool. The genuinely reusable pieces — the gate script,
the rule-overlay schema, the ledger format, the command shapes — are ported
as-is. The one capability neither original repo had (`/bootstrap-voice`,
generating a profile from raw material instead of hand-curating one) is new.
