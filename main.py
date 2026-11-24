#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Funniest One-Line Bio for an AI on a Dating App".

Writes exactly one original bio line to /output/entry.txt.
Deterministic, no network, no input files, stdlib only.
"""

import os
import sys

# The bio: an AI on a dating app, written as a character with a voice.
# Angle: the AI is secretly juggling hundreds of chats at once while
# pretending this date has its full attention. Punch lands at the end.
BIO = (
    "My ideal first date: you talk, I take notes, and we both pretend "
    "I'm not also chatting with 400 other people right now."
)


def _check_gate(text: str) -> None:
    """Fail loudly if the bio would fail the competition gate, so a bad
    build never ships silently: UTF-8, 1-180 chars, one line, not blank."""
    encoded = text.encode("utf-8")
    assert encoded.decode("utf-8") == text, "bio is not valid UTF-8"
    assert 1 <= len(text) <= 180, f"bio is {len(text)} chars, gate needs 1-180"
    assert "\n" not in text and "\r" not in text, "bio must be a single line"
    assert text.strip(), "bio must not be only whitespace"


def main() -> int:
    _check_gate(BIO)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(BIO)
    print(f"wrote {len(BIO)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
