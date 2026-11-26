#!/usr/bin/env python3
"""Entry for 'Rejected Olympic Sports' (u-motasimfuad-rejected-olympic-sports-9d83e7da).

Three candidate sports were drafted for the brief:
  A) "Competitive inbox zero: clear 10,000 unread emails while a coach shouts 'just reply all!'"
  B) "Synchronized parallel parking: four drivers, one spot outside a bakery on Sunday, judged on pure panic."
  C) "Extreme spreadsheet wrestling: two accountants, one pivot table, no undo allowed."
Picked B: it borrows a genuine Olympic adjective (synchronized) and drops it
into an everyday scene of pure panic, while A and C never leave office humour.
The program is deterministic: fixed text, no network access, no randomness.
"""
import os
from pathlib import Path

LINE = "Synchronized parallel parking: four drivers, one spot outside a bakery on Sunday, judged on pure panic."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Sanity-check the entry: one tidy line, inside the character limit."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
