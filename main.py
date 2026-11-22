#!/usr/bin/env python3
"""Write the make.fun plan bounty entry to <output dir>/entry.txt.

Standard library only, Python 3.13. The plan is one literal, 262 code points,
written UTF-8 with no trailing newline. Output directory comes from
MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

PLAN = "Day 1: enter 10 open escrowed bounties daily: make.fun ($20-500 pools, 10-20 paid places) and Superteam Earn ($1k-20k), one hardened repo per category, 1 win in 4 ≈$35/day. Day 10: add Code4rena audit contests, $200+ a finding. Expect ≈$1000 by day 30, $0 spent."

DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(PLAN)


if __name__ == "__main__":
    main()
