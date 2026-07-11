#!/usr/bin/env python3
"""Verify the first-length finite zero-layer population exactly."""
from __future__ import annotations

from fractions import Fraction

from verify_index_eight_small_sieve import X, log_bounds

TARGET = 177780727155637125193
BUDGET = (133 * TARGET + 1) // 2 - TARGET
EDGE_THRESHOLD = 5000
CUTOFF = 60_000_000
LAYER_POSITION_CAP = 6257
FINITE_RANGE_UPPER = Fraction(86_411_887, 1_000_000_000)
CHEAP_TOTAL_UPPER = Fraction(2_216, 10_000_000_000_000_000)
EXPECTED_EXPENSIVE_EDGE_CAP = 4_657_855_051_477_692_680
EXPECTED_FINITE_ZERO = 22_537_952


def verify() -> None:
    expensive_edge_cap = (2 * BUDGET) // EDGE_THRESHOLD
    assert expensive_edge_cap == EXPECTED_EXPENSIVE_EDGE_CAP

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

    minimum = (finite_zero_required * CUTOFF).numerator // (
        finite_zero_required * CUTOFF
    ).denominator + 1
    assert minimum == EXPECTED_FINITE_ZERO
    assert minimum > 64 * 349_430

    print("first-length finite zero-layer mass verified")
    print(f"expensive edge cap={expensive_edge_cap}")
    print(f"required finite reciprocal mass approximately {float(finite_zero_required):.15f}")
    print(f"expensive zero-layer targets in (60000000,X)>={minimum}")


if __name__ == "__main__":
    verify()
