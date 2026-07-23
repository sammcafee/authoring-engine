# Authoring Strategy

What this engine is built to do, and what it deliberately does not do.

## Guiding principle

- **The machine supplies LABOR: extraction, clustering, structural checks,
  mechanical tell-detection, bookkeeping. You supply VOICE and JUDGMENT.**
  That split doesn't move, no matter how good generation gets.
- **Generation is allowed, under two safeguards, both required:** it must be
  grounded in your voice profile (`voice/profile/`, `voice/purest/` — built by
  `/bootstrap-voice`), and it must never reach a finished state without your
  edit. Ungrounded generation (no anchor to your actual voice) and unedited
  generation (shipped without a real pass from you) are each independently a
  failure — grounding without editing is still not yours, and editing
  something ungrounded is editing the wrong draft. Where a passage of your
  own authentic prose already exists, that's the starting material:
  restructure and tighten it, don't broad-rewrite it.
- **Every mechanical rule becomes code or data, never prose nobody rereads.**
  Structural rules become templates. Only genuine judgment stays in prose
  docs. Keep exactly one source of truth per rule and never duplicate it —
  duplication is how a ruleset quietly drifts out of sync with itself.

## Build order

1. **Deterministic voice gate** (`tools/voice-gate.py` + `tools/voice-rules.json`,
   overlaid by your project's `config/voice-rules.local.json`). Cheapest,
   highest-leverage piece: a small script that scans a draft and reports
   line-anchored violations, exiting nonzero on any hard fail. Single source
   of truth per rule; `config/VOICE.md` references the rules, never restates them.
2. **Voice profile** (`voice/profile/`, `voice/purest/`, `voice/eval-only/`) —
   the ground truth of what your voice actually does, built once by
   `/bootstrap-voice` and refined over time. The gate and every review pass
   must calibrate against `voice/purest/` and `voice/profile/`, so they never
   "correct" your real moves into blandness — a rule that fires on genuinely
   authentic prose is a rule to reconsider, not a violation to fix.
3. **Voice ledger** (`config/VOICE-LEDGER.md`, the learning loop, built by `/learn`).
   After you edit a generated draft, diff it against the frozen original,
   infer the generalizable preference the edit reveals, and append an entry:
   polarity, category, verbatim off/good examples. See
   `docs/voice-ledger-format.md` for the schema. Read the active entries
   whenever you draft or review.
4. **Review, tiered by stakes.** Not every draft needs the same scrutiny.
   Define a couple of short rubrics (voice authenticity, structural fit,
   audience fit) and reserve the full set for your highest-stakes pieces
   (openers, anything quotable, anything hard to walk back); routine pieces
   get the gate plus one combined pass. Calibrate each rubric against the
   voice profile so it doesn't sand off your real moves.

## Draft protocol

The machine proposes, your edit makes it yours, and nothing advances until it
passes both the deterministic gate and your own read.

- **Source priority.** Where a pre-existing draft of a passage already exists
  in your own words, that's the starting material — the machine restructures
  and tightens it, never broad-rewrites. Only for a genuine gap does the
  machine generate a first-pass scaffold.
- **Grounded generation only.** Every generation prompt draws from: the
  relevant plan/outline material, three to five exemplars from
  `voice/purest/`, the `voice/profile/` docs, and the hard rules. Never draw
  exemplars from `voice/eval-only/`.
- **Gate before you see it.** Run the deterministic gate on any generated
  passage; on a hard fail, regenerate — don't surface a failing draft.
- **Currency check, if relevant.** Before you edit, scan for time-contingent
  assertions (claims about what's currently true in a fast-moving market or
  technology) and flag anything a reader down the line would find dated.
  This applies to any subject matter that ages, not just AI commentary.
- **You edit and QC every sentence.** This is where your voice lands and
  your judgment enters. A generated draft is a scaffold, not a final.
- **Provenance labeling.** Mark each passage as preserved-from-you or
  generated, so review attention (and the gate, if you extend it to weight
  passages differently) can focus on the generated ones.
- **Capture.** Run `/learn` to diff the generated version against your
  edited final and record what it reveals, so the next piece starts closer
  to your ear.

## Out of scope (do not build)

A fully-automated generation pipeline that ships without your edit, or that's
ungrounded in your voice profile — grounded generation that you edit and QC
is the entire point, going further than that isn't. Automated fact-checking
as deterministic code: nothing in this engine can verify a claim against the
world, and pretending otherwise is worse than not trying — fact and reference
checking stays a manual or Claude-assisted review pass, the same way voice
review does. Out-of-family inference automation. A pipeline-board UI.
