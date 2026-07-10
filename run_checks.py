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
    from test_periodic_block import (
        test_finite_positive_drift_repetition_bound,
        test_known_5n1_cycle_block,
        test_zero_repeat_bound,
    )
    from test_fermat_macroblock import (
        test_complete_macroblock_formula,
        test_endpoint_isometry,
        test_net_growth_survives_exit,
        test_precision_transfer_congruence,
        test_unique_hensel_targets,
    )
    test_v2()
    test_known_5n1_cycle()
    test_finite_growth_identity()
    test_known_5n1_cycle_block()
    test_finite_positive_drift_repetition_bound()
    test_zero_repeat_bound()
    test_complete_macroblock_formula()
    test_net_growth_survives_exit()
    test_precision_transfer_congruence()
    test_endpoint_isometry()
    test_unique_hensel_targets()
    run("tools/verify_finite_growth_block.py", "--m", "20", "--L", "50")
    run("tools/analyze_periodic_block.py", "--X", "5", "--pattern", "1,1,5", "--n", "13", "--limit", "10")
    run("tools/analyze_periodic_block.py", "--X", "33", "--pattern", "5", "--n", str((1 << 35) - 1), "--limit", "10")
    run("tools/analyze_fermat_macroblock.py", "--m", "3", "--L", "599", "--k", "0", "--precision", "17")
    run("tools/analyze_fermat_macroblock.py", "--m", "4", "--L", "78", "--k", "1", "--precision", "10")
    run("tools/trajectory_report.py", "--X", "5", "--n0", "7", "--steps", "1000")
    print("all checks passed")


if __name__ == "__main__":
    main()
