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
    from test_wieferich_1093 import (
        test_direct_predecessor_samples_divisible_by_q,
        test_full_wieferich_certificate,
        test_order_and_wieferich_congruence,
        test_output_coprime_to_q,
    )
    from test_power_coordinates import (
        test_fermat_coordinate_cases,
        test_fermat_grouped_exits,
        test_mersenne_coordinate_cases_and_self_similarity,
    )
    from test_strong_candidate import (
        test_rational_exponential_upper_bound,
        test_strong_candidate_cycle_bound_inequalities,
        test_strong_candidate_first_step,
        test_strong_candidate_full_certificate,
        test_strong_candidate_order_and_wieferich_data,
    )
    from test_cycle_barrier_generator import (
        test_constructed_multiplier_above_half_power,
        test_large_symbolic_barrier,
        test_minimal_k_condition,
        test_small_barriers,
    )
    from test_ultra_candidate import (
        test_ultra_candidate_cycle_inequalities,
        test_ultra_candidate_first_step,
        test_ultra_candidate_full_certificate,
        test_ultra_candidate_output_residues,
        test_ultra_candidate_structure,
    )
    from test_two_parameter_barrier import (
        test_two_parameter_closeness,
        test_two_parameter_large_case,
        test_two_parameter_mersenne_choice,
        test_two_parameter_small_cases,
    )

    tests = [
        test_v2,
        test_known_5n1_cycle,
        test_finite_growth_identity,
        test_known_5n1_cycle_block,
        test_finite_positive_drift_repetition_bound,
        test_zero_repeat_bound,
        test_complete_macroblock_formula,
        test_net_growth_survives_exit,
        test_precision_transfer_congruence,
        test_endpoint_isometry,
        test_unique_hensel_targets,
        test_order_and_wieferich_congruence,
        test_output_coprime_to_q,
        test_direct_predecessor_samples_divisible_by_q,
        test_full_wieferich_certificate,
        test_fermat_coordinate_cases,
        test_fermat_grouped_exits,
        test_mersenne_coordinate_cases_and_self_similarity,
        test_strong_candidate_order_and_wieferich_data,
        test_strong_candidate_first_step,
        test_strong_candidate_cycle_bound_inequalities,
        test_rational_exponential_upper_bound,
        test_strong_candidate_full_certificate,
        test_small_barriers,
        test_large_symbolic_barrier,
        test_minimal_k_condition,
        test_constructed_multiplier_above_half_power,
        test_ultra_candidate_structure,
        test_ultra_candidate_output_residues,
        test_ultra_candidate_first_step,
        test_ultra_candidate_cycle_inequalities,
        test_ultra_candidate_full_certificate,
        test_two_parameter_small_cases,
        test_two_parameter_large_case,
        test_two_parameter_mersenne_choice,
        test_two_parameter_closeness,
    ]
    for test in tests:
        test()

    run("tools/verify_finite_growth_block.py", "--m", "20", "--L", "50")
    run("tools/analyze_periodic_block.py", "--X", "5", "--pattern", "1,1,5", "--n", "13", "--limit", "10")
    run("tools/analyze_periodic_block.py", "--X", "33", "--pattern", "5", "--n", str((1 << 35) - 1), "--limit", "10")
    run("tools/analyze_fermat_macroblock.py", "--m", "3", "--L", "599", "--k", "0", "--precision", "17")
    run("tools/analyze_fermat_macroblock.py", "--m", "4", "--L", "78", "--k", "1", "--precision", "10")
    run("tools/verify_wieferich_1093.py")
    run("tools/verify_strong_candidate.py")
    run("tools/generate_cycle_barrier.py", "--barrier", "1000000000000")
    run("tools/verify_ultra_candidate.py")
    run("tools/generate_two_parameter_barrier.py", "--length", "1000000000000", "--height", "1000000000")
    run("tools/trajectory_report.py", "--X", "5", "--n0", "7", "--steps", "1000")
    print(f"all checks passed ({len(tests)} direct tests)")


if __name__ == "__main__":
    main()
