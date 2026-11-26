"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note to /output/entry.txt: a software fix for the bug
where the brain replays an embarrassing moment from 2014 every night at
3:04 AM. Pure Python 3.13 standard library, deterministic: no network,
no clock, no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

ENTRY = "v2.0.1: fixed a bug where the brain replayed an embarrassing moment from 2014 every night at 3:04 AM."

# Bounty gate: the entry must be one line of 1-160 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 160


def main() -> None:
    entry = ENTRY
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        print(
            f"invalid entry: {len(entry)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in entry or "\r" in entry:
        print("invalid entry: must be a single line", file=sys.stderr)
        sys.exit(1)
    if entry != entry.strip():
        print(
            "invalid entry: must not start or end with whitespace",
            file=sys.stderr,
        )
        sys.exit(1)
    if not entry.strip():
        print("invalid entry: must not be only whitespace", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
