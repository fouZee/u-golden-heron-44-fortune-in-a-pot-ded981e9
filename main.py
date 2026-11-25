#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry program.

Writes one kind, funny fortune for a houseplant (at most 120 characters)
to ``<OUTPUT_DIR>/entry.txt`` (default ``/output``) and validates the gate:
UTF-8 text, 1-120 characters, not only whitespace, a single line.
"""

import os
import sys

FORTUNE = (
    "The sun has big plans for your windowsill plant this week: "
    "new leaves, warm light, and one very smug little sprout."
)


def validate(text: str) -> None:
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if text != text.strip():
        raise SystemExit("gate failed: entry has leading/trailing whitespace")
    if len(text) > 120:
        raise SystemExit(f"gate failed: entry is {len(text)} chars, over 120")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise SystemExit("gate failed: entry contains control characters")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        raise SystemExit("gate failed: entry is not valid UTF-8")


def main() -> None:
    validate(FORTUNE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    print(f"wrote {path} ({len(FORTUNE)} chars)")
    print(FORTUNE)


if __name__ == "__main__":
    sys.exit(main())
