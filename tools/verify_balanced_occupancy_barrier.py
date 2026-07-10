#!/usr/bin/env python3
"""Verify the balanced occupancy cycle barrier with exact arithmetic."""
from __future__ import annotations

from fractions import Fraction

X = 104350542602662257699
M = 15099
H = 2154
D = 2 * M
BARRIER = 176022359338834903230
ALPHA = -32
BETA = 33
SCALE_BITS = 70
SCALE = 1 << SCALE_BITS
SERIES_TERMS = 12


def class_rep(t: int) -> int:
    residue = pow(pow(2, t, M), -1, M)
    rep = residue if residue & 1 else residue + M
    if rep == 1:
        rep += 2 * M
    return rep


def atanh_log_upper(z: Fraction) -> Fraction:
    """Rigorous upper bound for log(z), valid for 1<=z<=2."""
    assert 1 <= z <= 2
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(SERIES_TERMS):
        partial += power / (2 * j + 1)
        power *= y2
    remainder = power / (2 * SERIES_TERMS + 1) / (1 - y2)
    return 2 * (partial + remainder)


def ceil_scaled(value: Fraction) -> int:
    return (value.numerator * SCALE + value.denominator - 1) // value.denominator


LOG2_UNITS = ceil_scaled(atanh_log_upper(Fraction(2, 1)))


def log_upper_units(q: Fraction) -> int:
    """Return U with log(q)<=U/2^SCALE_BITS for q>1."""
    assert q > 1
    numerator = q.numerator
    denominator = q.denominator
    k = numerator.bit_length() - denominator.bit_length()
    while numerator < (denominator << k):
        k -= 1
    while numerator >= (denominator << (k + 1)):
        k += 1
    assert k >= 0
    u = q / (1 << k)
    assert 1 <= u < 2
    return k * LOG2_UNITS + ceil_scaled(atanh_log_upper(u))


def reciprocal_bound(length_cap: int) -> Fraction:
    reps = [class_rep(t) for t in range(1, H + 1)]
    s0 = sum((Fraction(1, r) for r in reps), Fraction(0, 1))
    sum_r = sum(reps)
    sum_tr = sum(t * r for t, r in enumerate(reps, start=1))

    c_scale = D * length_cap
    log_units = 0
    for t, rho in enumerate(reps, start=1):
        dual_numerator = ALPHA + BETA * t
        assert dual_numerator > 0
        q = Fraction(c_scale, rho * dual_numerator)
        assert q > 1
        log_units += log_upper_units(q)

    weighted_budget = 67 * length_cap - 1
    count_term = Fraction(ALPHA, D)
    if ALPHA < 0:
        # If m classes are occupied, sum max(c_t-1,0)=p-m.
        # Since m<=H and ALPHA<0, this is the safe worst case.
        count_term += Fraction(-ALPHA * H, D * length_cap)

    return (
        s0
        + count_term
        + Fraction(BETA * weighted_budget, D * length_cap)
        - Fraction(H, D)
        + Fraction(ALPHA * sum_r + BETA * sum_tr, c_scale * D)
        + Fraction(log_units, D * SCALE)
    )


def interval_margins(length_cap: int) -> tuple[Fraction, Fraction, Fraction]:
    reciprocal = reciprocal_bound(length_cap)
    epsilon = Fraction(X * X - (1 << 133), 1 << 133)
    even_margin = Fraction(2, 3) - (length_cap // 2) * epsilon - reciprocal / X

    q_num = 1 << 67
    odd_log_lower = Fraction(2 * (q_num - X), q_num + X)
    odd_margin = (
        odd_log_lower
        - ((length_cap - 1) // 2) * epsilon
        - reciprocal / X
    )
    return even_margin, odd_margin, reciprocal


def verify() -> None:
    assert M == 3 * 7 * 719
    assert X % M == 0
    assert pow(2, H, M) == 1
    for prime in (2, 3, 359):
        assert pow(2, H // prime, M) != 1
    assert X + 1 < (1 << 67)
    assert X * X > (1 << 133)

    reps = [class_rep(t) for t in range(1, H + 1)]
    assert len(set(r % D for r in reps)) == H
    assert min(reps) == 25

    even, odd, reciprocal = interval_margins(BARRIER)
    assert even > 0
    assert odd > 0

    next_even, next_odd, _ = interval_margins(BARRIER + 1)
    assert next_even > 0
    assert next_odd <= 0

    print("balanced occupancy barrier verified")
    print(f"barrier={BARRIER}")
    print(f"reciprocal bound approximately {float(reciprocal):.15f}")
    print(f"even margin approximately {float(even):.15e}")
    print(f"odd margin approximately {float(odd):.15e}")
    print(f"next odd margin approximately {float(next_odd):.15e}")


if __name__ == "__main__":
    verify()
