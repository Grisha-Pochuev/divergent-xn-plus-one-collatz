#!/usr/bin/env python3
"""Verify full-predecessor reciprocal bounds through sixty million."""
from __future__ import annotations

from fractions import Fraction
from math import gcd

from verify_index_eight_small_sieve import (
    D,
    H,
    M,
    ORDER_P,
    P,
    X,
    class_rep,
    log_bounds,
    verify_group_data,
)
from verify_two_generation_predecessor_cost import (
    O,
    R,
    initial_predecessor_state,
    one_generation_admissible,
    output_label_map,
    state_distances,
)
from verify_two_generation_small_reciprocal import (
    full_label,
    pohlig_hellman_data,
)

TARGET = 177780727155637125195
TOTAL_VALUATION = 11822418355849868825468
INCREMENTAL_BUDGET = 11644637628694231700273
LAYER_BUDGET = 6257
LARGE_CUTOFF = 60_000_000

EXPECTED_CANDIDATES = 4_279_760
EXPECTED_GENUINE = 536_735
EXPECTED_SMALL_DEAD = 178_632
EXPECTED_SURVIVORS = 358_103
EXPECTED_ZERO_DELAY = 9_462
EXPECTED_MAX_DELAY = 558
EXPECTED_DELAY_SUM = 12_752_005


def base_predecessor_mod_x(n: int, label: int) -> int:
    modulus = X * X
    numerator = (pow(2, label, modulus) * (n % modulus) - 1) % modulus
    assert numerator % X == 0
    return (numerator // X) % X


def fractional_dual(
    items: list[tuple[int, int, int, int]],
    expected_full: int,
    expected_boundary: tuple[int, int, int, int],
) -> Fraction:
    """Items are (n, incremental_cost, label, delay)."""
    ordered = sorted(items, key=lambda item: item[0] * item[1])
    spent = 0
    full = 0
    boundary: tuple[int, int, int, int] | None = None
    for item in ordered:
        if spent + item[1] <= INCREMENTAL_BUDGET:
            spent += item[1]
            full += 1
        else:
            boundary = item
            break

    assert full == expected_full
    assert boundary == expected_boundary
    assert boundary is not None
    denominator = boundary[0] * boundary[1]

    bound = Fraction(INCREMENTAL_BUDGET, denominator)
    positive_terms = 0
    for n, cost, _label, _delay in items:
        if n * cost < denominator:
            bound += Fraction(1, n) - Fraction(cost, denominator)
            positive_terms += 1
    assert positive_terms == expected_full
    return bound


def verify() -> None:
    verify_group_data()
    assert TOTAL_VALUATION == 133 * ((TARGET - 1) // 2) + 67
    assert INCREMENTAL_BUDGET == TOTAL_VALUATION - TARGET
    assert INCREMENTAL_BUDGET // O == LAYER_BUDGET

    small_labels = output_label_map()
    allowed_mod_m = set(small_labels)
    small_admissible = [
        one_generation_admissible(state, small_labels)
        for state in range(R)
    ]
    small_distances = state_distances(small_admissible)
    tables, coefficients = pohlig_hellman_data()

    modulus = X * X
    power = pow(2, O, modulus)
    assert (power - 1) % X == 0
    step = ((power - 1) // X) % X
    assert step == 63726582940809041391
    assert gcd(step, X) == 3

    def is_full_output_residue(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    candidate_count = 0
    genuine_count = 0
    small_dead = 0
    delay_sum = 0
    zero_delay = 0
    maximum_delay = 0
    all_items: list[tuple[int, int, int, int]] = []

    for t in range(1, H + 1):
        rho = class_rep(t)
        for n in range(rho, LARGE_CUTOFF + 1, D):
            candidate_count += 1
            if pow(n, ORDER_P, P) != 1:
                continue
            genuine_count += 1
            label = full_label(n, t, tables, coefficients)

            small_state = initial_predecessor_state(n, label)
            if small_distances[small_state] < 0:
                small_dead += 1
                continue

            predecessor = base_predecessor_mod_x(n, label)
            delay: int | None = None
            for q in range(LAYER_BUDGET + 1):
                if is_full_output_residue(predecessor):
                    delay = q
                    break
                predecessor = (predecessor + step) % X
            assert delay is not None

            delay_sum += delay
            zero_delay += delay == 0
            maximum_delay = max(maximum_delay, delay)
            cost = label - 1 + O * delay
            assert cost > 0
            all_items.append((n, cost, label, delay))

    assert candidate_count == EXPECTED_CANDIDATES
    assert genuine_count == EXPECTED_GENUINE
    assert small_dead == EXPECTED_SMALL_DEAD
    assert len(all_items) == EXPECTED_SURVIVORS
    assert zero_delay == EXPECTED_ZERO_DELAY
    assert maximum_delay == EXPECTED_MAX_DELAY
    assert delay_sum == EXPECTED_DELAY_SUM

    small_items = [item for item in all_items if item[0] <= 1_000_000]
    assert len(small_items) == 5_824

    small_bound = fractional_dual(
        small_items,
        expected_full=564,
        expected_boundary=(
            33_223,
            47_070_022_334_752_482_215,
            549_750_138_304_358_466,
            25,
        ),
    )
    assert small_bound < Fraction(87_551_912, 1_000_000_000)

    large_bound = fractional_dual(
        all_items,
        expected_full=1_115,
        expected_boundary=(
            14_165,
            109_786_607_076_232_013_436,
            1_859_575_580_472_366_337,
            58,
        ),
    )
    assert large_bound < Fraction(87_618_737, 1_000_000_000)

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    required = X * (log2_lower - TARGET * eta_upper) / 2

    small_residual = required - small_bound
    large_residual = required - large_bound
    assert small_residual > Fraction(12_382, 1_000_000)
    assert large_residual > Fraction(12_315, 1_000_000)

    small_needed = (small_residual * 1_000_000).numerator // (
        small_residual * 1_000_000
    ).denominator + 1
    large_needed = (large_residual * LARGE_CUTOFF).numerator // (
        large_residual * LARGE_CUTOFF
    ).denominator + 1
    assert small_needed == 12_383
    assert large_needed == 738_929

    print("full-predecessor reciprocal bound verified")
    print(f"finite modular candidates={candidate_count}")
    print(f"genuine full representatives={genuine_count}")
    print(f"small-modulus dead representatives={small_dead}")
    print(f"full-delay survivors={len(all_items)}")
    print(f"zero-delay survivors={zero_delay}")
    print(f"maximum full delay={maximum_delay}")
    print(f"small-cutoff bound approximately {float(small_bound):.15f}")
    print(f"sixty-million bound approximately {float(large_bound):.15f}")
    print(f"required threshold approximately {float(required):.15f}")
    print(f"necessary values above one million>={small_needed}")
    print(f"necessary values above sixty million>={large_needed}")


if __name__ == "__main__":
    verify()
