#!/usr/bin/env python3
"""Verify elimination of the third remaining sparse-window exception."""
from __future__ import annotations

from fractions import Fraction

from verify_index_eight_small_sieve import (
    D,
    H,
    M,
    ORDER_P,
    P,
    SCALE,
    X,
    active_class_cap,
    ceil_div,
    class_rep,
    log_bounds,
    log_upper_units,
    verify_group_data,
)

CUTOFF = 60_000_000
TARGET = 177780727155637125191
EXPECTED_CANDIDATES = 4_279_760
EXPECTED_ELIGIBLE = 536_735
EXPECTED_ACTIVE = 152_608_241_119
EXPECTED_THRESHOLD = 2_139_543_499_307


def count_above_cutoff(limit: int, reps: list[int]) -> int:
    total = 0
    for rho in reps:
        lower_index = 0 if rho > CUTOFF else (CUTOFF - rho) // D + 1
        upper_index = -1 if limit < rho else (limit - rho) // D
        if upper_index >= lower_index:
            total += upper_index - lower_index + 1
    return total


def verify() -> None:
    verify_group_data()
    reps = [class_rep(t) for t in range(1, H + 1)]
    assert len(set(rho % D for rho in reps)) == H
    assert min(reps) == 25

    candidate_count = 0
    eligible_count = 0
    eligible_units = 0
    for rho in reps:
        for n in range(rho, CUTOFF + 1, D):
            candidate_count += 1
            if pow(n, ORDER_P, P) == 1:
                eligible_count += 1
                eligible_units += ceil_div(SCALE, n)

    assert candidate_count == EXPECTED_CANDIDATES
    assert eligible_count == EXPECTED_ELIGIBLE

    exact_total, active = active_class_cap(TARGET)
    assert active == EXPECTED_ACTIVE

    needed_above = active - eligible_count
    low = CUTOFF + 1
    high = CUTOFF + D * ((needed_above + H - 1) // H) + max(reps)
    while low < high:
        middle = (low + high) // 2
        if count_above_cutoff(middle, reps) >= needed_above:
            high = middle
        else:
            low = middle + 1
    threshold = low
    assert threshold == EXPECTED_THRESHOLD

    remaining_units = 0
    remaining_count = 0
    for rho in reps:
        lower_index = 0 if rho > CUTOFF else (CUTOFF - rho) // D + 1
        upper_index = -1 if threshold < rho else (threshold - rho) // D
        count = max(0, upper_index - lower_index + 1)
        remaining_count += count
        if count:
            start = rho + D * lower_index
            remaining_units += ceil_div(SCALE, start)
            q = Fraction(start + D * (count - 1), start)
            remaining_units += ceil_div(log_upper_units(q), D)
    assert remaining_count == needed_above

    tail_q = Fraction(25 + 2 * X * (TARGET - 1), 25)
    tail_units = ceil_div(active * log_upper_units(tail_q), 2 * X)
    total_units = eligible_units + remaining_units + tail_units

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    assert TARGET * eta_upper < log2_lower
    gap_lower = (log2_lower - TARGET * eta_upper) / 2
    margin = gap_lower - Fraction(total_units, SCALE * X)
    assert margin > 0

    print("third-exception subgroup sieve verified")
    print(f"target={TARGET}")
    print(f"exact total valuation={exact_total}")
    print(f"candidates below cutoff={candidate_count}")
    print(f"eligible full representatives={eligible_count}")
    print(f"active full classes<={active}")
    print(f"allowed-union threshold={threshold}")
    print(f"reciprocal bound approximately {float(Fraction(total_units, SCALE)):.15f}")
    print(f"required threshold approximately {float(gap_lower*X):.15f}")
    print(f"strict margin approximately {float(margin):.15e}")


if __name__ == "__main__":
    verify()
