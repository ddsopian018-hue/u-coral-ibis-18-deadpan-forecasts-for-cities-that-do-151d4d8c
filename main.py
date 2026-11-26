#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one line (at most 160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt,
falling back to ./output when the environment variable is unset.

The line is a flat, deadpan TV-weather read for Brindlewick: a high of
38 degrees, scattered showers of warm gravy, and 45 kilometre-per-hour
winds carrying umbrellas north until Tuesday. Absurd weather, broadcast
tone, one concrete image, and two numbers to make the place feel real.
It uses 153 of the 160 allowed characters.
"""

import os
import sys

# The entry: one deadpan forecast line, 153 characters.
LINE = (
    "In Brindlewick, expect a high of 38 degrees and scattered showers "
    "of warm gravy, with 45 kilometre-per-hour winds carrying umbrellas "
    "north until Tuesday."
)

MAX_CHARS = 160


def main() -> int:
    line = LINE

    # Validation: a single non-empty line within the character budget.
    if not line:
        print("error: forecast line is empty", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: forecast line has surrounding whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: forecast line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: forecast line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print("wrote %s (%d characters)" % (out_path, len(line)))
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
