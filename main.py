#!/usr/bin/env python3
"""Worst AI Advice entry generator.

Writes one line of confidently terrible advice to entry.txt.
The line is stored as a constant and written exactly, UTF-8, no newline.
"""

import os
from pathlib import Path

ENTRY = "To whiten your teeth fast, brush with bleach once a week — dentists hate this one simple trick."


def build_entry() -> str:
    """Return the single advice line, validated for the 1-140 char gate."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry length {len(text)} out of range")
    return text


def write_entry(output_dir: str) -> Path:
    target = Path(output_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_entry(), encoding="utf-8")
    return target


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    write_entry(output_dir)


if __name__ == "__main__":
    main()
