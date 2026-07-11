#!/usr/bin/env python3
"""Verify exclusion of Q>=6242 for the first remaining cycle length."""
from __future__ import annotations

from fractions import Fraction
from math import isqrt

from verify_first_length_finite_zero_layer_mass import (
    BUDGET,
    CHEAP_TOTAL_UPPER,
    CUTOFF,
    EDGE_THRESHOLD,
    FINITE_RANGE_UPPER,
    LAYER_POSITION_CAP,
    TARGET,
)
from verify_index_eight_small_sieve import (
    SCALE,
    X,
    ceil_div,
    log_bounds,
    log_upper_units,
)
from verify_permanent_predecessor_mod3_sieve import (
    H,
    M,
    REFINED_MODULUS,
)
from verify_two_generation_predecessor_cost import O

FIRST_EXCLUDED_Q = 6242
LAST_Q = 6257
SURVIVING_REFINED_CLASSES = 2 * H
FIRST_DENOMINATOR = CUTOFF + 1
EXPECTED_CAP_6241 = 7_914_149_047
EXPECTED_CAP_6242 = 7_675_423_986


def active_label_cap(q_total: int) -> int:
    label_budget = BUDGET - O * q_total
    assert label_budget >= 0
    cap = (1 + isqrt(1 + 8 * label_budget)) // 2
    assert cap * (cap - 1) // 2 <= label_budget
    assert (cap + 1) * cap // 2 > label_budget
    return cap


def packing_upper(q_total: int) -> Fraction:
    count = active_label_cap(q_total)
    blocks = ceil_div(count, SURVIVING_REFINED_CLASSES)

    # At most J surviving refined residue classes occur in each interval of
    # length W.  The first possible denominator is CUTOFF+1.
    log_argument = Fraction(
        FIRST_DENOMINATOR + REFINED_MODULUS * blocks,
        FIRST_DENOMINATOR,
    )
    log_units = log_upper_units(log_argument)
    return (
        Fraction(SURVIVING_REFINED_CLASSES, FIRST_DENOMINATOR)
        + Fraction(
            SURVIVING_REFINED_CLASSES * log_units,
            REFINED_MODULUS * SCALE,
        )
    )


def verify() -> None:
    assert TARGET == 177780727155637125193
    assert BUDGET // O == LAST_Q
    assert REFINED_MODULUS == 90_594
    assert SURVIVING_REFINED_CLASSES == 4_308

    expensive_edge_cap = (2 * BUDGET) // EDGE_THRESHOLD
    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    required = X * (log2_lower - TARGET * eta_upper) / 2
    finite_zero_required = (
        required
        - FINITE_RANGE_UPPER
        - CHEAP_TOTAL_UPPER
        - Fraction(LAYER_POSITION_CAP, CUTOFF)
        - Fraction(expensive_edge_cap, X)
    )
    assert finite_zero_required > Fraction(375_632_520, 1_000_000_000)

    assert active_label_cap(6241) == EXPECTED_CAP_6241
    assert active_label_cap(6242) == EXPECTED_CAP_6242

    upper_6241 = packing_upper(6241)
    upper_6242 = packing_upper(6242)

    # This compact relaxation first becomes contradictory at Q=6242.
    assert upper_6241 > finite_zero_required
    assert upper_6242 < finite_zero_required
    assert upper_6242 < Fraction(375_630_659, 1_000_000_000)

    previous = upper_6242
    for q_total in range(FIRST_EXCLUDED_Q + 1, LAST_Q + 1):
        current = packing_upper(q_total)
        assert current <= previous
        assert current < finite_zero_required
        previous = current

    print("high-Q mod-3 harmonic exclusion verified")
    print(f"required finite mass approximately {float(finite_zero_required):.15f}")
    print(f"Q=6241 packing upper approximately {float(upper_6241):.15f}")
    print(f"Q=6242 packing upper approximately {float(upper_6242):.15f}")
    print("excluded Q range=6242..6257")
    print("remaining Q<=6241")


if __name__ == "__main__":
    verify()
