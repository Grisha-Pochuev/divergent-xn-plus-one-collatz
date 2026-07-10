#!/usr/bin/env python3
"""Verify the transition-budget cycle barrier with exact arithmetic.

The certificate combines the residue-class reciprocal envelope with the strict
cycle budget sum(t*c_t) <= 67*p-1. It also audits the numerical gain against a
fully saturated version of the previous independent-class envelope.
"""
from __future__ import annotations

from fractions import Fraction

X = 104350542602662257699
M = 15099
H = 2154
RETAINED_OLD_BARRIER = 170000000000000000000
OPTIMIZED_OLD_BARRIER = 176022359338834903224
BARRIER = 176022359338834903228


def class_rep(t: int) -> int:
    residue = pow(pow(2, t, M), -1, M)
    rep = residue if residue & 1 else residue + M
    if rep == 1:
        # The fixed orbit cannot return to the literal value 1.
        rep += 2 * M
    return rep


def ceil_log2_ratio(numerator: int, denominator: int) -> int:
    """Least k>=0 with numerator/denominator <= 2^k."""
    assert numerator >= denominator > 0
    if numerator == denominator:
        return 0
    k = max(0, numerator.bit_length() - denominator.bit_length())
    while (1 << k) * denominator < numerator:
        k += 1
    while k > 0 and (1 << (k - 1)) * denominator >= numerator:
        k -= 1
    return k


def transition_reciprocal_bound(length_cap: int, reps: list[int], s0: Fraction) -> tuple[Fraction, int]:
    """Uniform transition-budget bound for every cycle length p<=length_cap."""
    valuation_budget = 67 * length_cap - 1
    exponent_sum = 0

    for t, rho in enumerate(reps, start=1):
        # If c_t is the number of cycle elements in class t, then
        # c_t<=p<=length_cap and t*c_t<=67*p-1<=valuation_budget.
        count_cap = min(length_cap, valuation_budget // t)
        assert count_cap >= 1

        numerator = rho + 2 * M * (count_cap - 1)
        exponent_sum += ceil_log2_ratio(numerator, rho)

    bound = s0 + Fraction(7 * exponent_sum, 20 * M)
    return bound, exponent_sum


def independent_reciprocal_bound(length_cap: int, s0: Fraction) -> tuple[Fraction, int]:
    """Previous envelope, saturated at the supplied length cap."""
    numerator = 25 + 2 * M * (length_cap - 1)
    k = ceil_log2_ratio(numerator, 25)
    bound = s0 + Fraction(7 * H * k, 20 * M)
    return bound, k


def interval_margins(length_cap: int, reciprocal: Fraction) -> tuple[Fraction, Fraction]:
    epsilon = Fraction(X * X - (1 << 133), 1 << 133)
    assert epsilon > 0

    r_even = length_cap // 2
    even_lhs = r_even * epsilon + reciprocal / X
    even_margin = Fraction(2, 3) - even_lhs

    r_odd = (length_cap - 1) // 2
    odd_lhs = r_odd * epsilon + reciprocal / X
    q_num = 1 << 67
    assert q_num > X
    odd_log_lower = Fraction(2 * (q_num - X), q_num + X)
    odd_margin = odd_log_lower - odd_lhs

    return even_margin, odd_margin


def verify() -> None:
    assert M == 3 * 7 * 719
    assert X % M == 0
    assert H == 2 * 3 * 359
    assert pow(2, H, M) == 1
    for prime in (2, 3, 359):
        assert pow(2, H // prime, M) != 1

    assert X + 1 < (1 << 67)
    assert X * X > (1 << 133)
    assert X < (1 << 67)

    reps = [class_rep(t) for t in range(1, H + 1)]
    assert len(set(r % (2 * M) for r in reps)) == H
    assert min(reps) == 25
    s0 = sum((Fraction(1, rho) for rho in reps), Fraction(0, 1))

    reciprocal, exponent_sum = transition_reciprocal_bound(BARRIER, reps, s0)
    even_margin, odd_margin = interval_margins(BARRIER, reciprocal)
    assert even_margin > 0
    assert odd_margin > 0

    next_reciprocal, _ = transition_reciprocal_bound(BARRIER + 1, reps, s0)
    next_even, next_odd = interval_margins(BARRIER + 1, next_reciprocal)
    assert next_odd <= 0
    assert next_even > 0

    # Fair comparison: saturate the previous independent-class envelope.
    old_reciprocal, old_k = independent_reciprocal_bound(OPTIMIZED_OLD_BARRIER, s0)
    old_even, old_odd = interval_margins(OPTIMIZED_OLD_BARRIER, old_reciprocal)
    assert old_even > 0
    assert old_odd > 0

    old_next_reciprocal, _ = independent_reciprocal_bound(OPTIMIZED_OLD_BARRIER + 1, s0)
    old_next_even, old_next_odd = interval_margins(OPTIMIZED_OLD_BARRIER + 1, old_next_reciprocal)
    assert old_next_odd <= 0
    assert old_next_even > 0

    assert BARRIER - OPTIMIZED_OLD_BARRIER == 4
    assert BARRIER > RETAINED_OLD_BARRIER

    print("transition-budget cycle barrier verified")
    print(f"X={X}")
    print(f"M={M}, order={H}, classes={len(reps)}")
    print(f"previous retained barrier={RETAINED_OLD_BARRIER}")
    print(f"optimized old-envelope barrier={OPTIMIZED_OLD_BARRIER}")
    print(f"transition-budget barrier={BARRIER}")
    print(f"strict gain over optimized old envelope={BARRIER-OPTIMIZED_OLD_BARRIER}")
    print(f"transition exponent sum={exponent_sum}")
    print(f"old envelope exponent={old_k}")
    print(f"transition reciprocal bound approximately {float(reciprocal):.15f}")
    print(f"old reciprocal bound approximately {float(old_reciprocal):.15f}")
    print(f"transition odd margin approximately {float(odd_margin):.15e}")
    print(f"next transition odd margin approximately {float(next_odd):.15e}")
    print(f"old odd margin approximately {float(old_odd):.15e}")
    print(f"next old odd margin approximately {float(old_next_odd):.15e}")


if __name__ == "__main__":
    verify()
