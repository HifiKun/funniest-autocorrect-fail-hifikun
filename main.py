#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt.
The joke is the entry itself: a single autocorrect slip.
"""

import os

ENTRY = (
    "I texted my boss 'I'll be working from home today' "
    "\u2014 autocorrect sent 'I'll be twerking from home today'."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = " ".join(ENTRY.split())
    if not 1 <= len(line) <= 199:
        raise SystemExit(f"entry must be 1-199 chars, got {len(line)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
