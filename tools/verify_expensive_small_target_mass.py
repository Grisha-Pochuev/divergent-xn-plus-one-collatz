#!/usr/bin/env python3
"""Verify necessary expensive target mass below X exactly."""
from __future__ import annotations

from fractions import Fraction

from verify_index_eight_small_sieve import (
    CUTOFF,
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

TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
K = 5000
CHEAP_MINIMUM = 781563824454394220933608138645145
EXPECTED_EXPENSIVE = 4657855051477692680
EXPECTED_SURVIVORS = 5824
EXPECTED_FIRST = (25, 163, 169, 499, 529)
EXPECTED_ADDITIONAL = 355687


def ceil_fraction(value: Fraction) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def verify() -> None:
    verify_group_data()
    labels = output_label_map()
    admissible = [
        one_generation_admissible(state, labels)
        for state in range(R)
    ]
    distances = state_distances(admissible)
    tables, coefficients = pohlig_hellman_data()

    survivors: list[int] = []
    for small_label in range(1, H + 1):
        rho = class_rep(small_label)
        for n in range(rho, CUTOFF + 1, D):
            if pow(n, ORDER_P, P) != 1:
                continue
            label = full_label(n, small_label, tables, coefficients)
            state = initial_predecessor_state(n, label)
            if distances[state] >= 0:
                survivors.append(n)

    survivors.sort()
    assert len(survivors) == EXPECTED_SURVIVORS
    assert tuple(survivors[:5]) == EXPECTED_FIRST

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)

    residuals: list[Fraction] = []
    for target in TARGETS:
        A = (133 * target + 1) // 2
        expensive = 2 * (A - target) // K
        assert expensive == EXPECTED_EXPENSIVE
        cheap = target - expensive

        required = X * (log2_lower - target * eta_upper) / 2
        residual = (
            required
            - Fraction(cheap, CHEAP_MINIMUM)
            - Fraction(expensive, X)
        )
        assert residual > 0
        residuals.append(residual)

    assert residuals[0] > Fraction(462_148_691, 1_000_000_000)
    assert residuals[1] > Fraction(55_297_591, 1_000_000_000)

    first_four_excess = sum(
        (Fraction(1, n) - Fraction(1, X) for n in survivors[:4]),
        Fraction(0, 1),
    )
    assert first_four_excess < Fraction(54_057, 1_000_000)
    assert first_four_excess < residuals[1]

    all_small_excess = sum(
        (Fraction(1, n) - Fraction(1, X) for n in survivors),
        Fraction(0, 1),
    )
    assert all_small_excess < Fraction(106_462, 1_000_000)

    remaining = residuals[0] - all_small_excess
    assert remaining > Fraction(355_686_812, 1_000_000_000)
    per_additional = Fraction(1, CUTOFF) - Fraction(1, X)
    additional = ceil_fraction(remaining / per_additional)
    assert additional == EXPECTED_ADDITIONAL

    print("expensive small-target mass verified")
    print(f"first admissible targets={EXPECTED_FIRST}")
    print(f"p={TARGETS[1]} needs at least five expensive targets below X")
    print(f"p={TARGETS[0]} needs at least {additional} additional targets in (10^6,X)")
    print(f"all <=10^6 excess approximately {float(all_small_excess):.15f}")


if __name__ == "__main__":
    verify()
