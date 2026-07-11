#!/usr/bin/env python3
"""Verify mandatory expensive zero-layer tail populations exactly."""
from __future__ import annotations

from fractions import Fraction

from verify_index_eight_small_sieve import X, log_bounds

TARGETS = (
    (177780727155637125193, 25_216_149),
    (177780727155637125195, 805_083),
)

FINITE_RANGE_UPPER = Fraction(86_411_887, 1_000_000_000)
CHEAP_TOTAL_UPPER = Fraction(2_216, 10_000_000_000_000_000)
POSITIVE_LAYER_CAP = 6257
CUTOFF = 60_000_000


def verify() -> None:
    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)

    for target, expected in TARGETS:
        required = X * (log2_lower - target * eta_upper) / 2
        tail_required = required - FINITE_RANGE_UPPER
        expensive_zero_required = (
            tail_required
            - CHEAP_TOTAL_UPPER
            - Fraction(POSITIVE_LAYER_CAP, CUTOFF)
        )
        assert expensive_zero_required > 0

        minimum = (expensive_zero_required * CUTOFF).numerator // (
            expensive_zero_required * CUTOFF
        ).denominator + 1
        assert minimum == expected

        print(f"target={target}")
        print(
            "expensive zero-layer reciprocal requirement approximately "
            f"{float(expensive_zero_required):.15f}"
        )
        print(f"expensive zero-layer targets above sixty million>={minimum}")

    print("expensive zero-layer tail populations verified")


if __name__ == "__main__":
    verify()
