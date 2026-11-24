#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single office joke (one line, 1-200 chars) to /output/entry.txt
and refuses to exit cleanly if the text is outside the gate limits.
"""

import os
import sys

JOKE = (
    "I hit reply-all asking to be removed from the thread, "
    "and 200 colleagues replied-all to say the same thing."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check_entry(text: str) -> str:
    """Return the stripped joke, or raise if it breaks the gate."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty or only whitespace")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(cleaned)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in cleaned:
        raise ValueError("entry must be a single line")
    return cleaned


def emit_entry() -> int:
    try:
        text = check_entry(JOKE)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(emit_entry())
