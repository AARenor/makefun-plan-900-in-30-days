#!/usr/bin/env python3
"""Write the make.fun plan bounty entry to <output dir>/entry.txt.

Python 3.13, standard library only. The plan is one literal of exactly 248
code points, written UTF-8 with no trailing newline. The output directory is
MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

ENTRY_NAME = "entry.txt"
PLAN = "Day 1: open 8 escrowed code bounties (make.fun $20-2k, Superteam Earn $1k-20k, Code4rena audits), one hardened repo each; 1 win in 4 pays $120/day. Day 12: pitch the same repos to 30 funded startups at $400 fixed. Expect $3,000 by day 30, $0 spent."


def text() -> str:
    """Return the 30-day plan: exactly 248 code points, no trailing newline."""
    return PLAN


def write_entry(out_dir: str) -> str:
    """Write the plan into out_dir/entry.txt and return that path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_NAME)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text())
    return path


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


if __name__ == "__main__":
    main()
