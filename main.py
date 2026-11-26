#!/usr/bin/env python3
"""Museum of the Year 3000 — a one-line entry for make.fun.

A museum in the year 3000 puts a small label beside every object
from our time. This program is the label press for one of them: a
plastic fork from 2025, a single-use tool from the Age of
Convenience, when humans threw away forever-objects after a single
lunch. It checks the label against the contest rules and mounts it
in the entry file.
"""

import os
import sys
from pathlib import Path

LIMIT = 200
FALLBACK_OUTPUT = "/output/entry.txt"
SENTENCE_MARK = "."

LABEL = "Plastic fork, 2025: a single-use eating tool from the Age of Convenience, when humans threw away forever-objects after a single lunch."


def checks():
    """The contest rules, each as a (name, test) pair over the label."""
    return [
        ("non-empty", lambda line: bool(line.strip())),
        ("no edge whitespace", lambda line: line == line.strip()),
        (
            "at most 200 characters",
            lambda line: len(line) <= LIMIT,
        ),
        ("exactly one sentence", lambda line: line.count(SENTENCE_MARK) == 1),
        ("single line", lambda line: "\n" not in line and "\r" not in line),
    ]


def failing_rules(line):
    """Names of the rules the label breaks; empty when it passes all."""
    return [name for name, test in checks() if not test(line)]


def resolve_output(argv):
    """Pick the destination: --output wins, then OUTPUT_PATH, then default."""
    for index, token in enumerate(argv):
        if token == "--output" and index + 1 < len(argv):
            return argv[index + 1]
        if token.startswith("--output="):
            return token.split("=", 1)[1]
    return os.environ.get("OUTPUT_PATH", FALLBACK_OUTPUT)


def mount(label, destination):
    """Write the label and confirm the mounted copy word for word."""
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(label + "\n", encoding="utf-8")
    mounted = path.read_text(encoding="utf-8")
    if mounted != label + "\n":
        raise SystemExit("mounted label differs from the approved text")
    return path


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    broken = failing_rules(LABEL)
    if broken:
        print(
            "label breaks these rules: " + ", ".join(broken),
            file=sys.stderr,
        )
        return 1
    if "--verify-only" in argv:
        print(f"label OK: {len(LABEL)} characters, one line")
        return 0
    destination = resolve_output(argv)
    mount(LABEL, destination)
    if "--quiet" not in argv:
        print(LABEL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
