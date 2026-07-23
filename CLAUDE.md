# CLAUDE.md

Orientation for working in this repo.

## What this is

A generic, self-contained authoring pipeline: build a voice profile from your
own writing, then generate → gate → review → edit → learn in a loop. See
`README.md` for setup and `docs/AUTHORING-STRATEGY.md` for the design
principles behind it.

## How the pieces fit together

- `/bootstrap-voice`, `/ingest`, `/draft`, `/learn` (in `.claude/commands/`)
  are prose protocols for a Claude Code session to execute with you, turn by
  turn — not scripts. That's deliberate: voice is judgment, and every part of
  this pipeline that requires judgment stays a guided conversation. Only the
  mechanical parts (`tools/voice-gate.py`, the hooks, CI) are code.
- `tools/voice-gate.py` is the one deterministic piece. It's data-driven off
  `tools/voice-rules.json` (starter universal rules) merged with your
  project's `config/voice-rules.local.json` (your own overlay). Never hand-
  edit rule logic into the script — add or reclassify a rule in the JSON.
- `config/VOICE-LEDGER.md` accumulates what your edits reveal about your voice,
  captured by `/learn`. Read the active entries before drafting or reviewing.

## Working discipline

- **Generate, then critique before committing**, at every stage. A draft is
  a scaffold until you've edited it — nothing ships silently.
- **Grounded generation only.** Every generated passage must trace back to
  `voice/purest/` exemplars and `voice/profile/` — never to
  `voice/eval-only/` (comparison baselines, never generation sources).
- **Your calls stay yours.** For any voice, judgment, or structural fork, a
  session should surface it as options with a recommendation and wait, not
  decide it unilaterally.
- **Config vs. engine.** `config.example/` ships with the repo and contains
  no real personal material — it's a placeholder you copy to `config/` and
  replace. If you fork this repo to build on your own voice, keep `config/`
  (your real rules, your real guardrails, anything naming a real client or
  colleague) out of any copy of the repo you make public or share.

## Resuming (fresh session)

Read this file, then `README.md` and `docs/AUTHORING-STRATEGY.md`, then
`git log` for recent state. Don't regenerate committed work cold — build on
what's there.
