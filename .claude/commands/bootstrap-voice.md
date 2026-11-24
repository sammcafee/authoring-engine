---
description: Analyze a body of your own writing and produce a starter voice profile
---

# /bootstrap-voice — build a voice profile from raw material

This is the step that lets a new project start from nothing: point it at your
own writing, and it produces the profile documents that `/draft` and the
voice gate ground themselves in. Nothing in this engine parses prose
automatically to do this — voice is judgment, so this command is a guided
analysis protocol for a Claude Code session to work through with you, the
same way every other step in this pipeline is. Expect to run this once at
project start, then revisit it occasionally (it's a starting point, not a
one-shot oracle).

## Input

Point this at a corpus of your existing writing: a folder of files, or
material already filed by `/ingest`. More is better, but even 10-15 pieces
across a couple of years is enough to start — you'll sharpen the profile
through `/learn` as you go regardless.

**Little or no written work?** If you've run `/interview`, its
`chapters/*/00-interview-notes.md` files are your own words, captured
verbatim. File them under `voice/spoken/` and build a **provisional**
profile from them: they're good evidence for stance, recurring moves, and
vocabulary, but spoken sentences aren't written sentences, so never use
them as sentence-level generation exemplars. Mark the profile provisional
in its header, lean harder on `/learn` for the first several drafts, and
promote your own edited finals into `voice/purest/` as they accumulate.

**Separate your material into two buckets before you start, and say so out
loud in the run report:**

- **Authentic** — writing you're confident is really yours: pre-AI-assistance
  work, or anything you know you wrote start to finish yourself.
- **Uncertain or known-assisted** — anything drafted with heavy AI help,
  ghostwritten, or otherwise not a clean sample of your own voice.

Only the authentic bucket becomes a generation exemplar. The uncertain bucket
is useful only as a contrast case (what your voice does *not* sound like) —
never generate from it, never blend it in "for volume." If you're not sure
which bucket a piece belongs in, put it in uncertain; a profile built on
too little authentic material is more useful than one diluted by
imitation.

## Analysis

Read the authentic bucket closely and produce a profile with these sections
(this shape is deliberately reusable — it's what a drafting tool needs to
ground itself, not a template of what to say about any particular voice):

1. **Phases, if there are any.** Does the writing sound different across
   eras (a career change, a shift in audience, a gap where AI tools entered
   the workflow)? Name the phases and which one is the authentic reference.
2. **What the voice actually does.** Concrete, evidenced techniques — how
   pieces open, how arguments get structured, sentence-level habits,
   recurring moves — each backed by a verbatim quoted example from the
   corpus. Don't describe in the abstract; show the pattern in the writer's
   own words.
3. **Sentence-level signatures.** Rhythm, punctuation preferences, verb
   choice, list usage — the mechanical fingerprint.
4. **Preferred structure.** If a recognizable shape recurs (an arc, a beat
   sequence, an essay architecture), name it as a numbered template.
5. **Forbidden patterns.** Anything in the corpus's *inauthentic* bucket (or
   generically AI-sounding, if you're starting fresh) that must never appear
   in generated output — this feeds directly into `config/voice-rules.local.json`.
6. **Content guardrails.** Anything the writer never wants named or
   referenced in generated output — real client names, confidential
   engagements, other people's private business. Keep this as a list of
   *categories* in the shipped template; the actual names belong only in
   your private `config/`, never committed to a public or shared copy of
   this repo.

## Output

Write:

- `voice/profile/style-requirements.md` — the analysis above, in full.
- `voice/purest/` — copies (or pointers, if the material is large) of the
  authentic-bucket pieces used as exemplars.
- `voice/eval-only/` — the uncertain/inauthentic bucket, clearly labeled as
  comparison baselines, never exemplars.
- `config/VOICE.md` — a short prose summary of the hard rules (the genuinely
  non-negotiable ones from "Forbidden patterns" above), for a human to skim
  before drafting.

Report back: how many pieces went into each bucket, and the single clearest
example of "this is what the authentic voice does that generic writing
doesn't."
