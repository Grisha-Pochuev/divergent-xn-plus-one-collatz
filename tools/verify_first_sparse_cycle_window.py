#!/usr/bin/env python3
"""Verify the first sparse cycle-length window with exact arithmetic."""
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

CAP = 355561454311274250377
FIRST_UNSAFE_ODD = 177780727155637125183
FIRST_POST_CROSSING_ODD = 177780727155637125197


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

    log2_lower, log2_upper = log_bounds(Fraction(2, 1), 20)
    energy = Fraction(X * X, 1 << 133)
    eta_lower, eta_upper = log_bounds(energy, 4)

    # Every even p<=CAP-1 lies before the first even crossing, and its
    # distance to the next power of two is larger than the uniform correction.
    r_even_max = (CAP - 1) // 2
    assert log2_lower - r_even_max * eta_upper > correction
    assert log2_lower - (r_even_max + 1) * eta_upper <= correction

    # The pre-crossing odd inequality holds through the last odd value before
    # the seven-element exceptional window.
    last_safe_pre_crossing_odd = FIRST_UNSAFE_ODD - 2
    assert (
        log2_lower - last_safe_pre_crossing_odd * eta_upper
    ) / 2 > correction
    assert (
        log2_lower - FIRST_UNSAFE_ODD * eta_upper
    ) / 2 <= correction

    # The crossing occurs strictly between the last exceptional odd value and
    # FIRST_POST_CROSSING_ODD.
    assert (FIRST_POST_CROSSING_ODD - 2) * eta_upper < log2_lower
    assert FIRST_POST_CROSSING_ODD * eta_lower > log2_upper

    # From the first post-crossing odd value through CAP, the gap to the next
    # power is [3*log(2)-p*eta]/2.  It is decreasing, so check only CAP.
    assert CAP * eta_upper < 3 * log2_lower
    post_crossing_margin = (
        3 * log2_lower - CAP * eta_upper
    ) / 2 - correction
    assert post_crossing_margin > 0

    exceptions = tuple(
        range(FIRST_UNSAFE_ODD, FIRST_POST_CROSSING_ODD, 2)
    )
    assert exceptions == (
        177780727155637125183,
        177780727155637125185,
        177780727155637125187,
        177780727155637125189,
        177780727155637125191,
        177780727155637125193,
        177780727155637125195,
    )

    print("first sparse cycle window verified")
    print(f"cap={CAP}")
    print(f"exceptional odd lengths={exceptions}")
    print(f"uniform reciprocal bound approximately {float(reciprocal):.15f}")
    print(
        "even endpoint margin approximately "
        f"{float(log2_lower-r_even_max*eta_upper-correction):.15e}"
    )
    print(
        "post-crossing odd endpoint margin approximately "
        f"{float(post_crossing_margin):.15e}"
    )


if __name__ == "__main__":
    verify()
