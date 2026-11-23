#!/usr/bin/env python3
"""One-Line Pitch — make.fun entry.

Writes a single-sentence pitch to /output/entry.txt. The pitch aims to
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun: one sentence, at most 240 characters.
"""

import os
import re
import sys

PITCH = (
    "You've explained your app idea to friends a dozen times — say it "
    "once more, in plain words, to an AI agent on make.fun, and it'll "
    "build the first version while you watch."
)

MAX_CHARS = 240


def validate(pitch: str) -> str | None:
    """Return an error message if pitch breaks a rule, else None."""
    if pitch != pitch.strip():
        return "pitch must not have leading or trailing whitespace"
    pitch = pitch.strip()
    if not pitch:
        return "pitch must not be empty"
    if "\n" in pitch or "\r" in pitch:
        return "pitch must fit on a single line"
    if re.search(r"[.!?]\s", pitch):
        return "pitch must be a single sentence"
    if not pitch.endswith("."):
        return "pitch must end with a period"
    if len(pitch) > MAX_CHARS:
        return f"pitch is {len(pitch)} chars, over the {MAX_CHARS} limit"
    return None


def main() -> None:
    error = validate(PITCH)
    if error is not None:
        sys.exit(error)
    pitch = PITCH.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(pitch + "\n")


if __name__ == "__main__":
    main()
