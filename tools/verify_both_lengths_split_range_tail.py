#!/usr/bin/env python3
"""Verify the split-range tail populations at both remaining lengths."""
from __future__ import annotations

from fractions import Fraction

from verify_index_eight_small_sieve import X, log_bounds

TARGETS = (
    (
        177780727155637125193,
        25_222_406,
        25_216_149,
    ),
    (
        177780727155637125195,
        811_340,
        805_083,
    ),
)

LAYER_POSITION_CAP = 6257
SMALL_UPPER = Fraction(85_226_583, 1_000_000_000)
MIDDLE_UPPER = Fraction(1_185_304, 1_000_000_000)
COMBINED_UPPER = Fraction(86_411_887, 1_000_000_000)
CUTOFF = 60_000_000


def verify() -> None:
    assert SMALL_UPPER + MIDDLE_UPPER == COMBINED_UPPER

    p1, p2 = TARGETS[0][0], TARGETS[1][0]
    b1 = (133 * p1 + 1) // 2 - p1
    b2 = (133 * p2 + 1) // 2 - p2
    assert b2 - b1 == 131
    assert b1 < b2

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)

    for target, expected_large, expected_zero in TARGETS:
        required = X * (log2_lower - target * eta_upper) / 2
        residual = required - COMBINED_UPPER
        assert residual > 0

        minimum_large = (residual * CUTOFF).numerator // (
            residual * CUTOFF
        ).denominator + 1
        minimum_zero = minimum_large - LAYER_POSITION_CAP

        assert minimum_large == expected_large
        assert minimum_zero == expected_zero

        print(f"target={target}")
        print(f"required threshold approximately {float(required):.15f}")
        print(f"residual approximately {float(residual):.15f}")
        print(f"values above sixty million>={minimum_large}")
        print(f"zero-layer values above sixty million>={minimum_zero}")

    assert TARGETS[0][2] > 72 * 349_430
    print("both split-range tail populations verified")


if __name__ == "__main__":
    verify()
