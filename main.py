#!/usr/bin/env python3
"""Write the make.fun plan bounty entry to <output dir>/entry.txt.

Standard library only, Python 3.13. plan_text() is one literal of exactly 262
Unicode code points, written as UTF-8 with no trailing newline. The output
directory is DEFAULT_OUTPUT_DIR unless MAKEFUN_OUTPUT_DIR overrides it.
"""

import os

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_NAME = "entry.txt"
PLAN = "Day 1: enter 10 open escrowed bounties daily: make.fun ($20-500 pools, 10-20 paid places) and Superteam Earn ($1k-20k), one hardened repo per category, 1 win in 4 ≈$35/day. Day 10: add Code4rena audit contests, $200+ a finding. Expect ≈$1000 by day 30, $0 spent."


def plan_text() -> str:
    """Return the 30-day plan: exactly 262 code points, no trailing newline."""
    return PLAN


def write_entry(out_dir: str) -> str:
    """Write the plan into out_dir/entry.txt and return that path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_NAME)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(plan_text())
    return path


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)


if __name__ == "__main__":
    main()
