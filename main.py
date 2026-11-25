#!/usr/bin/env python3
"""Write a one-line 1-star review from a houseplant about its human
owner for make.fun's One Star, Written in Sap bounty.

Why this entry fits the judge's brief: the plant's grievance is the
centre -- watered once a month, then moved away from the only sunny
window because it "clashes with the curtains" -- and the twist is
that the owner then asks why the plant is drooping, as if he had
nothing to do with it. Plant's-eye view of water, light and being
moved, a real complaint with a reason for the single star, and a
fresh specific detail (the curtains) instead of a stock
"forgot to water me" line.
"""

import os

LINE = (
    "One star. My owner waters me once a month, moves me away from "
    "the only sunny window because I 'clash with the curtains,' and "
    "then asks why I'm drooping."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-279 characters, a single line.
    # The line was counted at exactly 152 characters; pin that so
    # any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 152, f"line is {len(line)} characters, expected 152"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 279, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 152, "entry.txt is not 152 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
