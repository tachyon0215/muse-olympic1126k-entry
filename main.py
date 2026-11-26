#!/usr/bin/env python3
"""Submission script for the 'Rejected Olympic Sports' contest on make.fun.

Contest slug: u-motasimfuad-rejected-olympic-sports-9d83e7da

During drafting, three invented sports were weighed against each other:

  * Inbox-zero racing, where athletes clear a mountain of unread mail
    while a coach bellows at them to reply-all.
  * Spreadsheet grappling: rival accountants, a single pivot table,
    and absolutely no undo.
  * The winner -- synchronized parallel parking.

The parking gag earned its place because it steals a real Olympic
modifier, "synchronized", and plants it in the most ordinary Sunday
chaos imaginable: four motorists, one bakery-side space, and judging
based purely on how panicked everyone gets.

Running this file emits the chosen one-liner to entry.txt inside the
directory named by MAKEFUN_OUTPUT_DIR. Nothing here touches the
network, reads input, or varies between runs.
"""

import os
from pathlib import Path

SPORT_LINE = (
    "Synchronized parallel parking: four drivers, one spot outside a bakery "
    "on Sunday, judged on pure panic."
)
ENTRY_BYTES = (SPORT_LINE + "\n").encode("utf-8")
CHAR_CAP = 200


def check_line(raw: str) -> None:
    """Turn away anything that is not one clean line under the cap."""
    core = raw[:-1] if raw.endswith("\n") else raw
    problems = []
    if len(core) == 0 or len(core) > CHAR_CAP:
        problems.append("length outside the allowed band")
    if core.strip() == "":
        problems.append("blank apart from whitespace")
    if "\n" in core or "\r" in core:
        problems.append("spans more than one line")
    if core != core.strip() or "  " in core:
        problems.append("untidy spacing")
    if problems:
        raise ValueError("; ".join(problems))


def emit() -> Path:
    check_line(SPORT_LINE + "\n")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.txt"
    destination.write_bytes(ENTRY_BYTES)
    return destination


if __name__ == "__main__":
    emit()
