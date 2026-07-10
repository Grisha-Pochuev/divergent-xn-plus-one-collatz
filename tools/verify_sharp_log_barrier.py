#!/usr/bin/env python3
"""Verify the sharpened logarithmic interval cycle barrier."""
from __future__ import annotations

from fractions import Fraction

from verify_large_divisor_split_barrier import (
    D,
    H,
    X,
    low_residue_data,
    main_class_rep,
    reciprocal_bound,
)

BARRIER = 177780727155637125182
SERIES_TERMS = 14


def log_lower(z: Fraction) -> Fraction:
    """Rigorous lower bound for log(z) from positive atanh terms."""
    assert z > 1
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(SERIES_TERMS):
        partial += power / (2 * j + 1)
        power *= y2
    return 2 * partial


def interval_margins(
    length_cap: int,
    reps: list[int],
    s0: Fraction,
    sum_reps: int,
    low_first_units: int,
    low_minimum: int,
) -> tuple[Fraction, Fraction, Fraction]:
    reciprocal, *_ = reciprocal_bound(
        length_cap, reps, s0, sum_reps, low_first_units, low_minimum
    )
    epsilon = Fraction(X * X - (1 << 133), 1 << 133)
    even_margin = (
        log_lower(Fraction(2, 1))
        - (length_cap // 2) * epsilon
        - reciprocal / X
    )
    odd_margin = (
        log_lower(Fraction(1 << 67, X))
        - ((length_cap - 1) // 2) * epsilon
        - reciprocal / X
    )
    return even_margin, odd_margin, reciprocal


def verify() -> None:
    assert X * X > (1 << 133)
    assert X < (1 << 67)

    reps = [main_class_rep(t) for t in range(1, H + 1)]
    assert len(set(r % D for r in reps)) == H
    s0 = sum((Fraction(1, r) for r in reps), Fraction(0, 1))
    sum_reps = sum(reps)
    low_first_units, low_minimum = low_residue_data()

    even, odd, reciprocal = interval_margins(
        BARRIER, reps, s0, sum_reps, low_first_units, low_minimum
    )
    assert even > 0
    assert odd > 0

    next_even, next_odd, _ = interval_margins(
        BARRIER + 1, reps, s0, sum_reps, low_first_units, low_minimum
    )
    assert next_even > 0
    assert next_odd <= 0

    print("sharp logarithmic cycle barrier verified")
    print(f"barrier={BARRIER}")
    print(f"reciprocal bound approximately {float(reciprocal):.15f}")
    print(f"odd margin approximately {float(odd):.15e}")
    print(f"next odd margin approximately {float(next_odd):.15e}")


if __name__ == "__main__":
    verify()
