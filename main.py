#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry writer.

Writes a single original one-word verdict on an ex to /output/entry.txt.
The word is the whole entry: no trailing newline, no extra text.
"""

import os

WORD = "Preowned"


def main() -> None:
    verdict = WORD.strip()
    if not verdict:
        raise SystemExit("verdict is empty")
    if len(verdict) > 111:
        raise SystemExit("verdict must be at most 111 characters")
    # One word, letters only: no spaces, no hyphens, no punctuation tricks.
    if not verdict.isalpha():
        raise SystemExit("verdict must be exactly one word of letters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(verdict)
    print(f"wrote {verdict!r} ({len(verdict)} chars) to /output/entry.txt")


if __name__ == "__main__":
    main()
