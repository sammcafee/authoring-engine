#!/bin/bash
# Publish status of every piece, grouped.
#
# Source of truth is the STATUS field in each file: a "STATUS:" line in a
# piece's metadata footer, or a "<!-- STATUS: ... -->" comment. Values:
# draft (in progress) | queued (approved, ready to publish) | published.
# When you publish something, set its STATUS to published and fill PUBLISHED
# with the date and/or link, then commit. This script just reads those
# fields, so the list never drifts from reality.
#
# Adjust the `files=(...)` glob list below to match where your project's
# generated pieces live (e.g. drafts/*.md, or one glob per content type).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
shopt -s nullglob
files=(drafts/*.md)

for want in published queued draft; do
  echo "== ${want^^} =="
  n=0
  for f in "${files[@]}"; do
    s=$(grep -ioE 'STATUS:[[:space:]]*(published|queued|draft)' "$f" | head -1 \
        | grep -ioE '(published|queued|draft)' | tr '[:upper:]' '[:lower:]' || true)
    [ -z "$s" ] && s=draft
    if [ "$s" = "$want" ]; then
      pub=$(grep -ioE 'PUBLISHED:[^>]*' "$f" | head -1 \
            | sed -E 's/.*PUBLISHED:[[:space:]]*//I' | sed -E 's/[[:space:]-]*$//' || true)
      printf '  %s%s\n' "$(basename "$f" .md)" "${pub:+  -> $pub}"
      n=$((n+1))
    fi
  done
  [ "$n" -eq 0 ] && echo '  (none)'
  echo
done
