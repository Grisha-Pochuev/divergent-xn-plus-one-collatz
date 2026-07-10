#!/usr/bin/env python3
"""Verify the second sparse cycle-length window with exact arithmetic."""
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

CAP = 533342181466911375570
LAST_PRE_CROSSING_EVEN = 355561454311274250390
FIRST_POST_CROSSING_EVEN = 355561454311274250392
NEW_EVEN_EXCEPTIONS = tuple(
    range(355561454311274250378, FIRST_POST_CROSSING_EVEN, 2)
)
OLD_REMAINING_EXCEPTIONS = (
    177780727155637125193,
    177780727155637125195,
)


def log_bounds(z: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Return rigorous lower and upper atanh-series bounds for log(z)."""
    assert z > 1
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= y2
    lower = 2 * partial
    upper = lower + 2 * power / (2 * terms + 1) / (1 - y2)
    return lower, upper


def verify() -> None:
    reps = [main_class_rep(t) for t in range(1, H + 1)]
    assert len(set(r % D for r in reps)) == H
    s0 = sum((Fraction(1, r) for r in reps), Fraction(0, 1))
    sum_reps = sum(reps)
    low_first_units, low_minimum = low_residue_data()

    reciprocal, *_ = reciprocal_bound(
        CAP, reps, s0, sum_reps, low_first_units, low_minimum
    )
    correction = reciprocal / X

    log2_lower, log2_upper = log_bounds(Fraction(2, 1), 24)
    energy = Fraction(X * X, 1 << 133)
    eta_lower, eta_upper = log_bounds(energy, 5)

    # The first even crossing lies strictly between the two displayed values.
    assert (
        Fraction(LAST_PRE_CROSSING_EVEN, 2) * eta_upper
        < log2_lower
    )
    assert (
        Fraction(FIRST_POST_CROSSING_EVEN, 2) * eta_lower
        > log2_upper
    )

    # The earlier sparse theorem covers all lengths through the value just
    # before the new seven-element even window.
    last_safe_even_before_window = NEW_EVEN_EXCEPTIONS[0] - 2
    assert (
        log2_lower
        - Fraction(last_safe_even_before_window, 2) * eta_upper
        > correction
    )

    # After the crossing, the even gap to the following power is decreasing.
    # Checking the largest even endpoint therefore covers the entire interval.
    even_endpoint_margin = (
        2 * log2_lower
        - Fraction(CAP, 2) * eta_upper
        - correction
    )
    assert even_endpoint_margin > 0

    # Odd lengths lie between their first and second crossings. Their gap is
    # also decreasing, so check only the largest odd value below CAP.
    odd_endpoint = CAP - 1
    odd_endpoint_margin = (
        Fraction(3 * log2_lower - odd_endpoint * eta_upper, 2)
        - correction
    )
    assert odd_endpoint_margin > 0

    assert NEW_EVEN_EXCEPTIONS == (
        355561454311274250378,
        355561454311274250380,
        355561454311274250382,
        355561454311274250384,
        355561454311274250386,
        355561454311274250388,
        355561454311274250390,
    )

    all_exceptions = OLD_REMAINING_EXCEPTIONS + NEW_EVEN_EXCEPTIONS
    print("second sparse cycle window verified")
    print(f"cap={CAP}")
    print(f"uniform reciprocal bound approximately {float(reciprocal):.15f}")
    print(f"remaining exceptions={all_exceptions}")
    print(f"post-crossing even endpoint margin {float(even_endpoint_margin):.15e}")
    print(f"odd endpoint margin {float(odd_endpoint_margin):.15e}")


if __name__ == "__main__":
    verify()
