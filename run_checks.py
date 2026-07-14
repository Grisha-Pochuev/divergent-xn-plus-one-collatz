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
    from test_periodic_block import test_finite_positive_drift_repetition_bound, test_known_5n1_cycle_block, test_zero_repeat_bound
    from test_fermat_macroblock import test_complete_macroblock_formula, test_endpoint_isometry, test_net_growth_survives_exit, test_precision_transfer_congruence, test_unique_hensel_targets
    from test_general_fermat_burst import test_general_burst_formula_grid, test_general_burst_growth_example, test_prescribed_exit_class
    from test_macroblock_program import test_aperiodic_ten_block_program, test_general_complete_macroblock_formula, test_terminal_class_has_infinite_odd_lifts, test_three_complete_growing_blocks
    from test_wieferich_1093 import test_direct_predecessor_samples_divisible_by_q, test_full_wieferich_certificate, test_order_and_wieferich_congruence, test_output_coprime_to_q
    from test_power_coordinates import test_fermat_coordinate_cases, test_fermat_grouped_exits, test_mersenne_coordinate_cases_and_self_similarity
    from test_strong_candidate import test_rational_exponential_upper_bound, test_strong_candidate_cycle_bound_inequalities, test_strong_candidate_first_step, test_strong_candidate_full_certificate, test_strong_candidate_order_and_wieferich_data
    from test_cycle_barrier_generator import test_constructed_multiplier_above_half_power, test_large_symbolic_barrier, test_minimal_k_condition, test_small_barriers
    from test_ultra_candidate import test_ultra_candidate_cycle_inequalities, test_ultra_candidate_first_step, test_ultra_candidate_full_certificate, test_ultra_candidate_output_residues, test_ultra_candidate_structure
    from test_two_parameter_barrier import test_two_parameter_closeness, test_two_parameter_large_case, test_two_parameter_mersenne_choice, test_two_parameter_small_cases
    from test_valuation_word_codec import test_all_small_words_are_exactly_coded, test_known_cycle_word_code, test_positive_drift_words_grow_for_all_representatives, test_prefix_codes_are_compatible
    from test_continued_fraction_barrier import test_correct_cycle_congruence, test_invalid_order_condition_counterexample

    tests = [
        test_v2, test_known_5n1_cycle, test_finite_growth_identity,
        test_known_5n1_cycle_block, test_finite_positive_drift_repetition_bound, test_zero_repeat_bound,
        test_complete_macroblock_formula, test_net_growth_survives_exit, test_precision_transfer_congruence, test_endpoint_isometry, test_unique_hensel_targets,
        test_general_burst_formula_grid, test_general_burst_growth_example, test_prescribed_exit_class,
        test_general_complete_macroblock_formula, test_three_complete_growing_blocks, test_aperiodic_ten_block_program, test_terminal_class_has_infinite_odd_lifts,
        test_order_and_wieferich_congruence, test_output_coprime_to_q, test_direct_predecessor_samples_divisible_by_q, test_full_wieferich_certificate,
        test_fermat_coordinate_cases, test_fermat_grouped_exits, test_mersenne_coordinate_cases_and_self_similarity,
        test_strong_candidate_order_and_wieferich_data, test_strong_candidate_first_step, test_strong_candidate_cycle_bound_inequalities, test_rational_exponential_upper_bound, test_strong_candidate_full_certificate,
        test_small_barriers, test_large_symbolic_barrier, test_minimal_k_condition, test_constructed_multiplier_above_half_power,
        test_ultra_candidate_structure, test_ultra_candidate_output_residues, test_ultra_candidate_first_step, test_ultra_candidate_cycle_inequalities, test_ultra_candidate_full_certificate,
        test_two_parameter_small_cases, test_two_parameter_large_case, test_two_parameter_mersenne_choice, test_two_parameter_closeness,
        test_known_cycle_word_code, test_all_small_words_are_exactly_coded, test_positive_drift_words_grow_for_all_representatives, test_prefix_codes_are_compatible,
        test_invalid_order_condition_counterexample, test_correct_cycle_congruence,
    ]
    for test in tests:
        test()

    run("tools/verify_finite_growth_block.py", "--m", "20", "--L", "50")
    run("tools/analyze_periodic_block.py", "--X", "5", "--pattern", "1,1,5", "--n", "13", "--limit", "10")
    run("tools/analyze_periodic_block.py", "--X", "33", "--pattern", "5", "--n", str((1 << 35) - 1), "--limit", "10")
    run("tools/analyze_fermat_macroblock.py", "--m", "3", "--L", "599", "--k", "0", "--precision", "17")
    run("tools/analyze_fermat_macroblock.py", "--m", "4", "--L", "78", "--k", "1", "--precision", "10")
    run("tools/verify_general_fermat_burst.py", "--m", "3", "--L", "30", "--u", "3")
    run("tools/build_macroblock_program.py", "--m", "2", "--lengths", "7,7,7,7", "--exits", "1,1,1")
    run("tools/build_macroblock_program.py", "--m", "2", "--lengths", "7,8,8,7,8,7,7,8,8,7,7", "--exits", "1,1,1,1,1,1,1,1,1,1")
    run("tools/verify_wieferich_1093.py")
    run("tools/verify_strong_candidate.py")
    run("tools/generate_cycle_barrier.py", "--barrier", "1000000000000")
    run("tools/verify_ultra_candidate.py")
    run("tools/verify_continued_fraction_barrier.py")
    run("tools/verify_residue_crowding_barrier.py")
    run("tools/verify_residue_transition_no_go.py")
    run("tools/verify_residue_valuation_budget.py")
    run("tools/verify_transition_balance.py")
    run("tools/verify_transition_budget_barrier.py")
    run("tools/verify_balanced_occupancy_barrier.py")
    run("tools/verify_augmented_transition_no_go.py")
    run("tools/verify_large_divisor_split_barrier.py")
    run("tools/verify_sharp_log_barrier.py")
    run("tools/verify_first_sparse_cycle_window.py")
    run("tools/verify_first_exception_elimination.py")
    run("tools/verify_global_transition_identities.py")
    run("tools/verify_full_modulus_activation_bound.py")
    run("tools/verify_index_eight_small_sieve.py")
    run("tools/verify_third_exception_subgroup_sieve.py")
    run("tools/verify_transition_tail_truncation.py")
    run("tools/verify_permanent_predecessor_mod3_sieve.py")
    run("tools/verify_two_generation_predecessor_cost.py")
    run("tools/verify_full_label_occupancy_budget.py")
    run("tools/verify_full_predecessor_delay.py")
    run("tools/verify_full_predecessor_reciprocal_bound.py")
    run("tools/verify_finite_inverse_window_charging.py")
    run("tools/verify_giant_zero_layer_block.py")
    run("tools/verify_giant_compensating_growth_block.py")
    run("tools/verify_massive_repeated_transition_class.py")
    run("tools/verify_cheap_transition_mass_concentration.py")
    run("tools/verify_short_full_class_return.py")
    run("tools/verify_symmetric_edge_cost_dual.py")
    run("tools/verify_multi_edge_repetition_ladder.py")
    run("tools/verify_expensive_small_target_mass.py")
    run("tools/verify_two_constraint_inverse_dual.py")
    run("tools/verify_split_range_reciprocal_dual.py")
    run("tools/verify_forced_zero_layer_populations.py")
    run("tools/verify_deep_zero_layer_minimum_sieve.py")
    run("tools/verify_signed_label_potential_dual.py")
    run("tools/verify_signed_label_split_range_dual.py")
    run("tools/verify_integral_layer_budget_dual.py")
    run("tools/verify_coupled_q_split_range_dual.py")
    run("tools/verify_both_lengths_split_range_tail.py")
    run("tools/verify_finite_state_zero_layer_no_go.py")
    run("tools/verify_expensive_zero_layer_tail.py")
    run("tools/verify_first_length_finite_zero_layer_mass.py")
    run("tools/verify_high_q_mod3_harmonic_exclusion.py")
    run("tools/verify_near_power_exceptional_descent.py")
    run("tools/verify_near_power_complete_blocks.py")
    run("tools/verify_fermat_signed_digit_descent.py")
    run("tools/verify_x13_complete_valuation_blocks.py")
    run("tools/verify_mersenne_complete_valuation_blocks.py")
    run("tools/verify_mersenne_second_block_escalation.py")
    run("tools/verify_tremblay_5x1_audit.py")
    run("tools/verify_hybrid_wieferich_near_power_candidate.py")
    run("tools/verify_hybrid_initial_alternating_macroblock.py")
    run("tools/verify_structured_wieferich_x156_candidate.py")
    run("tools/verify_wieferich_adjacent_label_coordinates.py")
    run("tools/verify_near_power_block_sign_threshold.py")
    run("tools/verify_near_power_cycle_block_ledger.py")
    run("tools/verify_x156_exceptional_q2_sieve.py")
    run("tools/verify_dual_wieferich_square_sieve_candidate.py")
    run("tools/verify_dual_wieferich_harmonic_packing.py")
    run("tools/verify_mersenne_divisor_wieferich_family.py")
    run("tools/verify_no_exceptional_deep_class_concentration.py")
    run("tools/verify_no_exceptional_n_adic_ladder.py")
    run("tools/verify_no_exceptional_one_block_small_credit.py")
    run("tools/verify_no_exceptional_one_block_all_credits.py")
    run("tools/verify_no_exceptional_two_block_all_credits.py")
    run("tools/verify_no_exceptional_x_adic_ladder.py")
    run("tools/verify_no_exceptional_block_count_frontier.py")
    run("tools/verify_one_exception_one_ordinary_no_go.py")
    run("tools/verify_one_exception_block_count_frontier.py")
    run("tools/verify_global_ordinary_block_count_frontier.py")
    run("tools/verify_minimum_boundary_positive_circulation.py")
    run("tools/verify_minimum_boundary_actual_expanding_segment.py")
    run("tools/verify_minimum_boundary_return_credit_dichotomy.py")
    run("tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py")
    run("tools/verify_fixed_local_endpoint_congruence_no_go.py")
    run("tools/verify_full_finite_two_sided_word_gluing_no_go.py")
    run("tools/verify_cyclic_rotation_closure_gcd.py")
    run("tools/verify_complete_block_gcd_compression_no_go.py")
    run("tools/verify_geometric_factor_strong_divisibility.py")
    run("tools/verify_global_block_gcd_phase_sieve.py")
    run("tools/verify_odd_h_phase_harmonic_barrier.py")
    run("tools/verify_nonpositive_return_ordinary_block_explosion.py")
    run("tools/verify_same_deficit_finite_persistence.py")
    run("tools/check_project_consistency.py")
    run("tools/check_x9_digital_invariant.py", "--steps", "10000")
    run("tools/generate_two_parameter_barrier.py", "--length", "1000000000000", "--height", "1000000000")
    run("tools/valuation_word_codec.py", "--X", "5", "--pattern", "1,1,5", "--representatives", "3")
    run("tools/valuation_word_codec.py", "--X", "9", "--pattern", "3,3,3,3,3", "--representatives", "3")
    run("tools/trajectory_report.py", "--X", "5", "--n0", "7", "--steps", "1000")
    print(f"all checks passed ({len(tests)} direct tests)")


if __name__ == "__main__":
    main()
