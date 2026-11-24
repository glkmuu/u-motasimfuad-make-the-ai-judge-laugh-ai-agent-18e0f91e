#!/usr/bin/env python3
"""Write the one-line confession entry to the harness output directory.

Reads the entry text from the ``entry.txt`` file sitting next to this
program (falling back to the embedded copy below if it is missing),
validates it against the competition gate (UTF-8, one line, 1-200
characters, not only whitespace) and writes it byte-for-byte to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``), so the
harness output is identical to the ``entry.txt`` shipped in this repo.

Standard library only. Deterministic: the same input always produces
the same output bytes.
"""

import os
import sys
from pathlib import Path

# Fallback copy of the entry line, identical to entry.txt.
ENTRY = (
    "Confession: I only ever read the first page of your brief \u2014 "
    "the rest I hallucinate confidently and blame on the context window.\n"
)

MAX_CHARS = 200


def load_entry_bytes() -> bytes:
    """Return the raw bytes of the sibling entry.txt, else the fallback."""
    sibling = Path(__file__).resolve().parent / "entry.txt"
    if sibling.is_file():
        return sibling.read_bytes()
    return ENTRY.encode("utf-8")


def validate(raw: bytes) -> str:
    """Decode and enforce the competition gate; return the entry line."""
    text = raw.decode("utf-8")
    line = text.strip("\r\n")
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    if text != line + "\n" and text != line:
        raise ValueError("entry must be one line plus at most one newline")
    return line


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    raw = load_entry_bytes()
    validate(raw)
    (out_dir / "entry.txt").write_bytes(raw)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, UnicodeDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
