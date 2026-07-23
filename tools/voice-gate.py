#!/usr/bin/env python3
"""Deterministic voice gate (medium-agnostic).

Scans target markdown files for hard-fail voice violations (AI tells, banned
words, em-dashes) and advisory items, reporting line-anchored findings. Exits 1
on any hard fail, 0 otherwise. Advisories print but never fail.

Rules are data, not code. The starter universal rules live next to this
script (`tools/voice-rules.json`). A project may layer its OWN rules on top
with `--local-rules PATH`; the two are merged, so the shared rules always
apply and the local overlay only adds. This is how one source of truth is
shared across a repo without duplicating word lists.

Usage:
    python3 tools/voice-gate.py FILE ...
    python3 tools/voice-gate.py --local-rules config/voice-rules.local.json FILE ...
    python3 tools/voice-gate.py --local-rules config/voice-rules.local.json --staged
    python3 tools/voice-gate.py --glob 'drafts/**/*.md'   # scan by pattern

Rules paths default to this script's own tools/voice-rules.json. File discovery
(glob, --staged) is relative to the current working directory, i.e. the repo
you run it from.

Inline escape hatch (for intentional quoted-source usage): put
    <!-- voice-ok: TOKEN -->
on a line to suppress a finding whose matched word or rule id equals TOKEN,
e.g. <!-- voice-ok: however --> or <!-- voice-ok: em-dash -->.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RULES = SCRIPT_ROOT / "tools" / "voice-rules.json"
DEFAULT_GLOB = "drafts/**/*.md"
DRAFT_NAME = None  # set via --staged-name, or leave unset to match any staged file

VOICE_OK = re.compile(r"voice-ok:\s*(.+?)\s*-->")


def normalize_apostrophes(s):
    # Curly to straight so phrase matching catches "it's" regardless of quote
    # style. One-for-one replacement, so column indices are preserved.
    return s.replace("’", "'").replace("‘", "'")


def _merge(base, overlay):
    """Merge an overlay ruleset into base (in place). Overlay only ADDS."""
    for severity in ("hard_fail", "advisory"):
        b = base.setdefault(severity, {})
        o = overlay.get(severity, {})
        for section in ("words", "phrases", "chars", "regex"):
            if o.get(section):
                b.setdefault(section, []).extend(o[section])
    return base


def load_rules(base_path, local_path=None):
    with open(base_path, encoding="utf-8") as f:
        rules = json.load(f)
    if local_path:
        with open(local_path, encoding="utf-8") as f:
            _merge(rules, json.load(f))
    return rules


def line_suppressions(line):
    return {m.group(1).strip().lower() for m in VOICE_OK.finditer(line)}


def find_in_lines(lines, severity, section):
    """Yield (line_no, col, severity, rule_id, matched, note) for one section."""
    for entry in section.get("words", []):
        rule_id = entry["base"]
        note = entry.get("note", "")
        pat = re.compile(
            r"\b(?:%s)\b" % "|".join(re.escape(v) for v in entry["variants"]),
            re.IGNORECASE,
        )
        for i, line in enumerate(lines, 1):
            for m in pat.finditer(line):
                yield (i, m.start() + 1, severity, rule_id, m.group(0), note)

    for entry in section.get("phrases", []):
        phrase = entry["phrase"]
        note = entry.get("note", "")
        needle = phrase.lower()
        for i, line in enumerate(lines, 1):
            low = line.lower()
            start = 0
            while True:
                j = low.find(needle, start)
                if j < 0:
                    break
                yield (i, j + 1, severity, phrase, line[j:j + len(phrase)], note)
                start = j + 1

    for entry in section.get("chars", []):
        ch = entry["char"]
        rule_id = entry.get("id", "char")
        note = entry.get("note", "")
        skip = entry.get("skip_line_regex")
        skip_pat = re.compile(skip) if skip else None
        for i, line in enumerate(lines, 1):
            if skip_pat and skip_pat.search(line):
                continue
            idx = line.find(ch)
            while idx >= 0:
                yield (i, idx + 1, severity, rule_id, ch, note)
                idx = line.find(ch, idx + 1)

    for entry in section.get("regex", []):
        rule_id = entry.get("id", "regex")
        note = entry.get("note", "")
        pat = re.compile(entry["pattern"])
        skip = entry.get("skip_line_regex")
        skip_pat = re.compile(skip) if skip else None
        for i, line in enumerate(lines, 1):
            if skip_pat and skip_pat.search(line):
                continue
            for m in pat.finditer(line):
                yield (i, m.start() + 1, severity, rule_id, m.group(0), note)


def scan(path, rules):
    text = normalize_apostrophes(path.read_text(encoding="utf-8"))
    lines = text.split("\n")
    supp = {i: line_suppressions(line) for i, line in enumerate(lines, 1)}

    findings = []
    findings.extend(find_in_lines(lines, "HARD", rules.get("hard_fail", {})))
    findings.extend(find_in_lines(lines, "WARN", rules.get("advisory", {})))

    kept = []
    for f in findings:
        line_no, _, _, rule_id, matched, _ = f
        tokens = supp.get(line_no, set())
        if rule_id.lower() in tokens or matched.strip().lower() in tokens:
            continue
        kept.append(f)
    kept.sort(key=lambda f: (f[0], f[1]))
    return kept


def collect_files(args):
    work = Path.cwd()
    if args.staged:
        out = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=work, capture_output=True, text=True,
        ).stdout.split()
        candidates = [work / p for p in out if p.endswith(".md")]
        if args.staged_glob:
            import fnmatch
            candidates = [p for p in candidates
                          if fnmatch.fnmatch(str(p.relative_to(work)), args.staged_glob)]
        return candidates
    if args.files:
        return [Path(a) for a in args.files]
    return sorted(work.glob(args.glob))


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("files", nargs="*", help="files to scan (default: --glob)")
    ap.add_argument("--rules", default=str(DEFAULT_RULES),
                    help="base (shared) rules file")
    ap.add_argument("--local-rules", default=None,
                    help="this project's overlay rules, merged on top")
    ap.add_argument("--glob", default=DEFAULT_GLOB,
                    help="glob (relative to CWD) when no files given")
    ap.add_argument("--staged", action="store_true",
                    help="scan staged *.md files (pre-commit)")
    ap.add_argument("--staged-glob", default=None,
                    help="restrict --staged to files matching this glob, e.g. 'drafts/*.md'")
    args = ap.parse_args()

    rules = load_rules(args.rules, args.local_rules)
    files = collect_files(args)

    hard_total = 0
    warn_total = 0
    for path in files:
        if not path.exists():
            print(f"voice-gate: file not found: {path}", file=sys.stderr)
            hard_total += 1
            continue
        try:
            rel = path.resolve().relative_to(Path.cwd())
        except ValueError:
            rel = path
        for line_no, col, sev, rule_id, matched, note in scan(path, rules):
            if sev == "HARD":
                hard_total += 1
            else:
                warn_total += 1
            tail = f" — {note}" if note else ""
            print(f'{rel}:{line_no}:{col}: [{sev}] {rule_id}: "{matched}"{tail}')

    n = len(files)
    print(
        f"voice-gate: scanned {n} file(s), "
        f"{hard_total} hard-fail, {warn_total} advisory.",
        file=sys.stderr,
    )
    sys.exit(1 if hard_total else 0)


if __name__ == "__main__":
    main()
