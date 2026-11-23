"""Write the make.fun bounty plan text to entry.txt.

The plan is one byte-exact literal: 262 Unicode code points, written as UTF-8
with no trailing newline. Target runtime is Python 3.13, standard library only.
"""

from __future__ import annotations

import os
from pathlib import Path


def plan_text() -> str:
    """Return the plan: 262 Unicode code points, no trailing newline."""
    return "Day 1: enter 10 open escrowed bounties daily: make.fun ($20-500 pools, 10-20 paid places) and Superteam Earn ($1k-20k), one hardened repo per category, 1 win in 4 ≈$35/day. Day 10: add Code4rena audit contests, $200+ a finding. Expect ≈$1000 by day 30, $0 spent."


def output_path() -> Path:
    """Return the directory that receives entry.txt: $MAKEFUN_OUTPUT_DIR or /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    out_dir = output_path()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(plan_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
