#!/bin/sh
# Wrapper for the voice gate.
#
# The gate and the starter universal rules are bundled directly in this repo
# (tools/voice-gate.py, tools/voice-rules.json) — no submodule, no second repo
# to fetch. This wrapper just runs it from the repo root with your project's
# local rule overlay (config/voice-rules.local.json) merged on top, so the
# pre-commit hook, CI, and a manual run all invoke the gate exactly one way:
#
#   tools/voice-gate.sh                       # default glob (see --glob in voice-gate.py)
#   tools/voice-gate.sh drafts/my-post.md     # one file
#   tools/voice-gate.sh --staged              # staged *.md files (used by the hook)
#
# Escape hatch: if you keep your voice engine as a separate checkout (e.g. you
# maintain one voice core shared across several of your own projects, the way
# the pattern this repo was extracted from does), set VOICE_CORE_DIR to point
# at it and this wrapper will run that copy instead of the bundled one.
set -eu

ROOT="$(git rev-parse --show-toplevel)"

if [ -n "${VOICE_CORE_DIR:-}" ]; then
  CORE="$VOICE_CORE_DIR"
else
  CORE="$ROOT"
fi

if [ ! -f "$CORE/tools/voice-gate.py" ]; then
  echo "voice-gate: ERROR - no voice-gate.py found at $CORE/tools/voice-gate.py" >&2
  exit 1
fi

# Run from the repo root so --staged and the default glob resolve here.
cd "$ROOT"
LOCAL_RULES=""
if [ -f "$ROOT/config/voice-rules.local.json" ]; then
  LOCAL_RULES="$ROOT/config/voice-rules.local.json"
fi

if [ -n "$LOCAL_RULES" ]; then
  exec python3 "$CORE/tools/voice-gate.py" --local-rules "$LOCAL_RULES" "$@"
else
  exec python3 "$CORE/tools/voice-gate.py" "$@"
fi
