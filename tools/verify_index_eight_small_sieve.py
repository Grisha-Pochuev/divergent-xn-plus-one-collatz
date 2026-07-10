#!/usr/bin/env python3
"""Verify elimination of two sparse-window lengths by an index-eight sieve."""
from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt

X = 104350542602662257699
M = 15099
H = 2154
D = 2 * M
P = 6911089648497401
ORDER_P = 863886206062175
CUTOFF = 1_000_000
TARGETS = (
    177780727155637125187,
    177780727155637125189,
)
EXPECTED_CANDIDATES = 71318
EXPECTED_ELIGIBLE = 8727
EXPECTED_ACTIVE = 152608241119
EXPECTED_THRESHOLD = 2139491901191
SCALE_BITS = 80
SCALE = 1 << SCALE_BITS
UPPER_TERMS = 16


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def log_bounds(z: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    assert z >= 1
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


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def ceil_scaled(value: Fraction) -> int:
    return ceil_div(value.numerator * SCALE, value.denominator)


_, LOG2_UPPER = log_bounds(Fraction(2, 1), UPPER_TERMS)
LOG2_UPPER_UNITS = ceil_scaled(LOG2_UPPER)


def log_upper_units(q: Fraction) -> int:
    assert q >= 1
    if q == 1:
        return 0
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
    _, upper = log_bounds(u, UPPER_TERMS)
    return k * LOG2_UPPER_UNITS + ceil_scaled(upper)


def class_rep(t: int) -> int:
    residue = pow(pow(2, t, M), -1, M)
    rep = residue if residue & 1 else residue + M
    if rep == 1:
        rep += D
    return rep


def verify_group_data() -> None:
    assert X == M * P
    assert is_prime_64(P)
    assert P - 1 == 8 * ORDER_P
    assert ORDER_P == 5**2 * 2677 * 15137 * 852763
    for q in (5, 2677, 15137, 852763):
        assert is_prime_64(q)
    assert pow(2, ORDER_P, P) == 1
    for q in (5, 2677, 15137, 852763):
        assert pow(2, ORDER_P // q, P) != 1
    assert pow(2, H, M) == 1
    for q in (2, 3, 359):
        assert pow(2, H // q, M) != 1
    assert gcd(H, ORDER_P) == 1


def active_class_cap(p: int) -> tuple[int, int]:
    exact_total = 133 * ((p - 1) // 2) + 67
    budget = exact_total - p
    active = (1 + isqrt(1 + 8 * budget)) // 2
    while active * (active - 1) // 2 > budget:
        active -= 1
    while (active + 1) * active // 2 <= budget:
        active += 1
    return exact_total, active


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

    candidates: list[int] = []
    for rho in reps:
        candidates.extend(range(rho, CUTOFF + 1, D))
    assert len(candidates) == EXPECTED_CANDIDATES
    assert len(set(candidates)) == EXPECTED_CANDIDATES

    eligible = sorted(n for n in candidates if pow(n, ORDER_P, P) == 1)
    assert len(eligible) == EXPECTED_ELIGIBLE
    eligible_units = sum(ceil_div(SCALE, n) for n in eligible)

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)

    for target in TARGETS:
        exact_total, active = active_class_cap(target)
        assert active == EXPECTED_ACTIVE

        # The target is below the crossing, and the product correction cannot
        # reach the following power, so the displayed total valuation is exact.
        assert target * eta_upper < log2_lower
        assert Fraction(target, 25 * X) < log2_lower
        assert X > (1 << 66)

        needed_above = active - len(eligible)
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

        # Repetitions in a full class are spaced by 2X. The bound permits
        # every active class as many as target elements.
        tail_q = Fraction(25 + 2 * X * (target - 1), 25)
        tail_units = ceil_div(active * log_upper_units(tail_q), 2 * X)
        total_units = eligible_units + remaining_units + tail_units

        gap_lower = (log2_lower - target * eta_upper) / 2
        margin = gap_lower - Fraction(total_units, SCALE * X)
        assert margin > 0

        print(f"target={target}")
        print(f"exact total valuation={exact_total}")
        print(f"active full classes<={active}")
        print(f"allowed-union threshold={threshold}")
        print(f"reciprocal bound approximately {float(Fraction(total_units, SCALE)):.15f}")
        print(f"required threshold approximately {float(gap_lower*X):.15f}")
        print(f"strict margin approximately {float(margin):.15e}")

    print("index-eight small-representative sieve verified")
    print(f"candidates below cutoff={len(candidates)}")
    print(f"eligible full representatives={len(eligible)}")
    print(f"eligible reciprocal bound approximately {float(Fraction(eligible_units, SCALE)):.15f}")


if __name__ == "__main__":
    verify()
