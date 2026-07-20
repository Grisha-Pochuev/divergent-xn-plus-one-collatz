#!/usr/bin/env python3
"""Verify the retained scalar split-range bound through sixty million."""
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
BUDGET = 11644637628694231700273
LAYER_BUDGET = 6257
CUTOFF = 1_000_000
LARGE_CUTOFF = 60_000_000
SMALL_RANGE_UPPER = Fraction(85_239_095, 1_000_000_000)
EXPECTED_CANDIDATES = 4_279_760
EXPECTED_GENUINE = 536_735
EXPECTED_DEAD = 178_632
EXPECTED_SURVIVORS = 358_103
EXPECTED_MIDDLE = 352_279
EXPECTED_FULL = 5_179
EXPECTED_BOUNDARY = (
    1_021_885,
    32_815_616_360_883_804_024,
    1_502_499_629_181_248_314,
    8,
    1_540_142_525_975_756_512,
)


def fractional_dual(
    items: list[tuple[int, int, int, int, int]],
) -> tuple[Fraction, int, tuple[int, int, int, int, int]]:
    """Items are (n, symmetric_cost, target_label, delay, source_label)."""
    budget = 2 * BUDGET
    ordered = sorted(items, key=lambda item: item[0] * item[1])
    spent = 0
    full = 0
    boundary = None
    for item in ordered:
        if spent + item[1] <= budget:
            spent += item[1]
            full += 1
        else:
            boundary = item
            break
    assert boundary is not None
    denominator = boundary[0] * boundary[1]
    bound = Fraction(budget, denominator)
    positive = 0
    for n, cost, _target, _delay, _source in items:
        if n * cost < denominator:
            bound += Fraction(1, n) - Fraction(cost, denominator)
            positive += 1
    assert positive == full
    return bound, full, boundary


def verify() -> None:
    verify_group_data()
    assert BUDGET == (133 * TARGET + 1) // 2 - TARGET

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
    assert step == 63_726_582_940_809_041_391
    assert gcd(step, X) == 3

    def is_full(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    candidate_count = 0
    genuine_count = 0
    dead_count = 0
    survivor_count = 0
    middle_items: list[tuple[int, int, int, int, int]] = []

    for t in range(1, H + 1):
        rho = class_rep(t)
        for n in range(rho, LARGE_CUTOFF + 1, D):
            candidate_count += 1
            if pow(n % P, ORDER_P, P) != 1:
                continue
            genuine_count += 1

            target_label = full_label(n, t, tables, coefficients)
            state = initial_predecessor_state(n, target_label)
            if small_distances[state] < 0:
                dead_count += 1
                continue
            survivor_count += 1

            predecessor_numerator = (
                pow(2, target_label, modulus) * n - 1
            ) % modulus
            assert predecessor_numerator % X == 0
            predecessor = (predecessor_numerator // X) % X

            delay = 0
            while not is_full(predecessor):
                predecessor = (predecessor + step) % X
                delay += 1
                assert delay <= LAYER_BUDGET

            if n <= CUTOFF:
                continue

            source_small_label = small_labels[predecessor % M]
            source_label = full_label(
                predecessor,
                source_small_label,
                tables,
                coefficients,
            )
            symmetric_cost = (
                source_label - 1
                + target_label - 1
                + 2 * O * delay
            )
            middle_items.append((
                n,
                symmetric_cost,
                target_label,
                delay,
                source_label,
            ))

    assert candidate_count == EXPECTED_CANDIDATES
    assert genuine_count == EXPECTED_GENUINE
    assert dead_count == EXPECTED_DEAD
    assert survivor_count == EXPECTED_SURVIVORS
    assert len(middle_items) == EXPECTED_MIDDLE

    middle_bound, full, boundary = fractional_dual(middle_items)
    assert full == EXPECTED_FULL
    assert boundary == EXPECTED_BOUNDARY
    assert middle_bound < Fraction(1_370_625, 1_000_000_000)

    combined_upper = SMALL_RANGE_UPPER + Fraction(
        1_370_625, 1_000_000_000
    )
    # The two printed strict component bounds sum to this exact rational cap.
    # The underlying reciprocal contribution is strict because both component
    # estimates above are strict; the cap itself is equal to the decimal value.
    assert combined_upper == Fraction(86_609_720, 1_000_000_000)

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    required = X * (log2_lower - TARGET * eta_upper) / 2
    residual = required - combined_upper
    assert residual > Fraction(13_324_486, 1_000_000_000)

    minimum_large = (residual * LARGE_CUTOFF).numerator // (
        residual * LARGE_CUTOFF
    ).denominator + 1
    assert minimum_large == 799_470

    print("scalar split-range reciprocal dual verified")
    print(f"middle-range survivors={len(middle_items)}")
    print(f"middle fractional boundary after {full} complete items")
    print(f"middle bound approximately {float(middle_bound):.15f}")
    print(f"combined bound approximately {float(combined_upper):.15f}")
    print(f"required threshold approximately {float(required):.15f}")
    print(f"necessary values above sixty million>={minimum_large}")


if __name__ == "__main__":
    verify()
