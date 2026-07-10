#!/usr/bin/env python3
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main() -> None:
    run("-m", "compileall", "-q", "tools", "tests")
    sys.path.insert(0, str(ROOT / "tests"))
    from test_xn1 import test_finite_growth_identity, test_known_5n1_cycle, test_v2
    test_v2()
    test_known_5n1_cycle()
    test_finite_growth_identity()
    run("tools/verify_finite_growth_block.py", "--m", "20", "--L", "50")
    run("tools/trajectory_report.py", "--X", "5", "--n0", "7", "--steps", "1000")
    print("all checks passed")


if __name__ == "__main__":
    main()
