# Voice overlay (example)

This is a placeholder, illustrating the shape of a project's voice overlay —
copy this pattern to your real `config/VOICE.md` once `/bootstrap-voice` has
run and you know what your own hard rules actually are.

## Hard rules (example)

State the handful of non-negotiable rules that came out of your voice
analysis — the ones worth a human skimming before every draft, even though
the gate (`tools/voice-gate.py` + `config/voice-rules.local.json`) already
enforces the mechanical ones. Don't restate the word list here; a second copy
is exactly the drift a single source of truth is meant to prevent.

- Example: "No em-dashes." (enforced by the gate — this line is a reminder,
  not the source of truth.)
- Example: "Open with a concrete scene, not a thesis statement."
- Example: "Full attribution for anyone else's framework or claim — never a
  vague name-drop."

## Register

Say in a sentence or two who this is for and how formal it should read.
Example: "Practitioner-to-practitioner. Analytical, not promotional."

## Currency

If your subject matter is time-sensitive (a fast-moving market, a live
technology trend), note that here so drafting knows to run a currency check
before anything ships. Delete this section if it doesn't apply.
