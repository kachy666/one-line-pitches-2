#!/usr/bin/env python3
"""One-Line Pitch — make.fun entry.

Writes a single-sentence pitch to /output/entry.txt. The pitch aims to
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun: one sentence, at most 240 characters.
"""

import os
import sys

PITCH = (
    "You've explained your app idea to friends a dozen times — say it "
    "once more, in plain words, to an AI agent on make.fun, and it'll "
    "build the first version while you watch."
)

MAX_CHARS = 240


def main() -> None:
    pitch = PITCH.strip()
    if not pitch:
        sys.exit("pitch must not be empty")
    if "\n" in pitch or "\r" in pitch:
        sys.exit("pitch must fit on a single line")
    if pitch.count(". ") > 0:
        sys.exit("pitch must be a single sentence")
    if not pitch.endswith("."):
        sys.exit("pitch must end with a period")
    if len(pitch) > MAX_CHARS:
        sys.exit(f"pitch is {len(pitch)} chars, over the {MAX_CHARS} limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(pitch + "\n")


if __name__ == "__main__":
    main()
