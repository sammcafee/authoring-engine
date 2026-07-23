# Voice ledger format

`config/VOICE-LEDGER.md` is the record of what your edits have taught the pipeline
about your voice. `/learn` appends to it; every drafting step should read it
first.

## Entry shape

```
### <N> — <short description>
- **Polarity:** negative (removed) | positive (preferred)
- **Category:** diction | construction | structure | tone | argument
- **Off (cut):** "<verbatim excised text>"
- **Good:** "<verbatim preferred alternative>"   (optional — sometimes the
  fix is embedded directly in Rule instead)
- **Rule:** <the generalized guidance a future draft should follow>
- **Source:** <where this was learned — file/section, date>
```

**Polarity** distinguishes what you cut (negative — usually the higher-value
signal, since it tells the gate or a future draft what to avoid) from what you
steered toward (positive — a move to repeat). **Category** buckets the entry
so a drafting pass can skim for what's relevant: word-level choices
(diction), how a sentence or paragraph is built (construction), how a piece
is organized (structure), or register/attitude (tone).

## How entries get added

Manually, via `/learn` — a Claude Code session reads the diff between a
generated draft and your edited version, infers what the edit reveals, and
writes the entry. There's no script that parses `git diff` output
programmatically; this is judgment work, same as everything else upstream of
the deterministic gate.

## Guardrails

- **Flag contradictions, don't auto-resolve them.** If a new inferred rule
  conflicts with an existing entry, surface it for you to decide rather than
  silently overwriting or duplicating.
- **Dedupe.** Before adding an entry, check whether the same preference is
  already recorded under a different wording.
- **A zero-edit approval is a signal, not a rule.** If you approve a draft
  with no changes, that's worth noting as a clean-pass data point, but it
  doesn't generalize into a ledger entry on its own.
- **Mechanical, repeatable edits should graduate to the gate.** If the same
  word or phrase keeps getting cut, that's a candidate for
  `config/voice-rules.local.json`, not just a ledger entry you have to
  remember to apply by hand each time.
