#!/usr/bin/env python3
"""Write the make.fun plan bounty entry to <output dir>/entry.txt.

Python 3.13, standard library only. The plan is one literal of exactly 262
code points, written UTF-8 with no trailing newline. The output directory is
MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
ENTRY_NAME = "entry.txt"


def plan_text() -> str:
    """Return the 30-day plan: exactly 262 code points, no trailing newline."""
    return "Day 1: enter 10 open escrowed bounties daily: make.fun ($20-500 pools, 10-20 paid places) and Superteam Earn ($1k-20k), one hardened repo per category, 1 win in 4 ≈$35/day. Day 10: add Code4rena audit contests, $200+ a finding. Expect ≈$1000 by day 30, $0 spent."


def output_path() -> str:
    """Return the entry.txt path inside the resolved output directory."""
    return os.path.join(OUTPUT_DIR, ENTRY_NAME)


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(plan_text())


if __name__ == "__main__":
    main()
