#!/usr/bin/env python3
"""Verify the two-generation reciprocal bound through sixty million."""
from __future__ import annotations

from fractions import Fraction

from verify_index_eight_small_sieve import (
    D,
    H,
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

CUTOFF = 60_000_000
TARGET = 177780727155637125195
EXPECTED_TOTAL_VALUATION = 11822418355849868825468
EXPECTED_CANDIDATES = 4_279_760
EXPECTED_GENUINE = 536_735
EXPECTED_DEAD = 178_632
EXPECTED_SURVIVING = 358_103
EXPECTED_FULL_ITEMS = 5_941
BOUNDARY_N = 108_791
BOUNDARY_S = 1_416_690_312_052_110_223
BOUNDARY_DELAY = 9
BOUNDARY_WEIGHT = 18_163_988_302_773_434_773


def verify() -> None:
    verify_group_data()
    labels = output_label_map()
    admissible = [one_generation_admissible(state, labels) for state in range(R)]
    distances = state_distances(admissible)
    tables, coefficients = pohlig_hellman_data()

    candidate_count = 0
    genuine_count = 0
    dead_count = 0
    items: list[tuple[int, int, int, int]] = []

    for small_label in range(1, H + 1):
        rho = class_rep(small_label)
        for n in range(rho, CUTOFF + 1, D):
            candidate_count += 1
            if pow(n, ORDER_P, P) != 1:
                continue
            genuine_count += 1

            label = full_label(n, small_label, tables, coefficients)
            state = initial_predecessor_state(n, label)
            delay = distances[state]
            if delay < 0:
                dead_count += 1
                continue

            weight = label + O * delay
            items.append((n, weight, label, delay))

    assert candidate_count == EXPECTED_CANDIDATES
    assert genuine_count == EXPECTED_GENUINE
    assert dead_count == EXPECTED_DEAD
    assert len(items) == EXPECTED_SURVIVING

    total_valuation = 133 * ((TARGET - 1) // 2) + 67
    assert total_valuation == EXPECTED_TOTAL_VALUATION

    ordered = sorted(items, key=lambda item: item[0] * item[1])
    spent = 0
    full_items = 0
    boundary: tuple[int, int, int, int] | None = None
    for item in ordered:
        if spent + item[1] <= total_valuation:
            spent += item[1]
            full_items += 1
        else:
            boundary = item
            break

    assert full_items == EXPECTED_FULL_ITEMS
    assert boundary == (
        BOUNDARY_N,
        BOUNDARY_WEIGHT,
        BOUNDARY_S,
        BOUNDARY_DELAY,
    )

    denominator = BOUNDARY_N * BOUNDARY_WEIGHT
    reciprocal_bound = Fraction(total_valuation, denominator)
    positive_terms = 0
    for n, weight, _label, _delay in items:
        if n * weight < denominator:
            reciprocal_bound += Fraction(1, n)
            reciprocal_bound -= Fraction(weight, denominator)
            positive_terms += 1

    assert positive_terms == EXPECTED_FULL_ITEMS
    assert reciprocal_bound < Fraction(99_476_202, 1_000_000_000)

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    assert TARGET * eta_upper < log2_lower
    required_reciprocal = X * (log2_lower - TARGET * eta_upper) / 2
    residual = required_reciprocal - reciprocal_bound

    assert residual > Fraction(458, 1_000_000)
    minimum_large_values = 27_481
    assert (minimum_large_values - 1) * Fraction(1, CUTOFF) == Fraction(458, 1_000_000)
    assert minimum_large_values * Fraction(1, CUTOFF) > Fraction(458, 1_000_000)

    print("two-generation sixty-million reciprocal bound verified")
    print(f"target={TARGET}")
    print(f"finite modular candidates={candidate_count}")
    print(f"genuine full representatives={genuine_count}")
    print(f"permanently dead representatives={dead_count}")
    print(f"two-generation survivors={len(items)}")
    print(f"fractional boundary after {full_items} complete items")
    print(f"reciprocal bound approximately {float(reciprocal_bound):.15f}")
    print(f"required threshold approximately {float(required_reciprocal):.15f}")
    print(f"strict residual approximately {float(residual):.15f}")
    print(f"necessary distinct values above cutoff>={minimum_large_values}")


if __name__ == "__main__":
    verify()
