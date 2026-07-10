#!/usr/bin/env python3
"""Verify the transition-budget cycle barrier with exact arithmetic.

The certificate combines the residue-class reciprocal envelope with the strict
cycle budget sum(t*c_t) <= 67*p-1.  It uses no trajectory search and no
floating-point inequality in the proof.
"""
from __future__ import annotations

from fractions import Fraction

X = 104350542602662257699
M = 15099
H = 2154
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


def reciprocal_bound(length_cap: int, reps: list[int], s0: Fraction) -> tuple[Fraction, int]:
    """Uniform reciprocal bound for every cycle length p<=length_cap."""
    valuation_budget = 67 * length_cap - 1
    exponent_sum = 0

    for t, rho in enumerate(reps, start=1):
        # If c_t is the number of cycle elements in class t, then
        # c_t<=p<=length_cap and t*c_t<=67*p-1<=valuation_budget.
        count_cap = min(length_cap, valuation_budget // t)
        assert count_cap >= 1

        # Distinct elements of this class lie in rho+2M*j.  The decreasing
        # harmonic tail is bounded by its integral, and then
        # log(1+z)<=k*log(2)<7k/10.
        numerator = rho + 2 * M * (count_cap - 1)
        k = ceil_log2_ratio(numerator, rho)
        exponent_sum += k

    bound = s0 + Fraction(7 * exponent_sum, 20 * M)
    return bound, exponent_sum


def interval_margins(length_cap: int, reps: list[int], s0: Fraction) -> tuple[Fraction, Fraction, Fraction, int]:
    reciprocal, exponent_sum = reciprocal_bound(length_cap, reps, s0)

    epsilon = Fraction(X * X - (1 << 133), 1 << 133)
    assert epsilon > 0

    # Every even p=2r<=length_cap satisfies r<=floor(length_cap/2).
    r_even = length_cap // 2
    even_lhs = r_even * epsilon + reciprocal / X
    even_margin = Fraction(2, 3) - even_lhs  # log(2)>2/3

    # Every odd p=2r+1<=length_cap satisfies r<=floor((length_cap-1)/2).
    r_odd = (length_cap - 1) // 2
    odd_lhs = r_odd * epsilon + reciprocal / X
    q_num = 1 << 67
    assert q_num > X
    odd_log_lower = Fraction(2 * (q_num - X), q_num + X)
    odd_margin = odd_log_lower - odd_lhs

    return even_margin, odd_margin, reciprocal, exponent_sum


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

    even_margin, odd_margin, reciprocal, exponent_sum = interval_margins(BARRIER, reps, s0)
    assert even_margin > 0
    assert odd_margin > 0

    # The next integer already fails the odd-length rational interval test.
    # Since all terms in that test are nondecreasing with the length cap,
    # BARRIER is maximal for this exact transition-budget certificate and
    # these retained rational logarithm bounds.
    next_even, next_odd, _, _ = interval_margins(BARRIER + 1, reps, s0)
    assert next_odd <= 0
    assert next_even > 0

    print("transition-budget cycle barrier verified")
    print(f"X={X}")
    print(f"M={M}, order={H}, classes={len(reps)}")
    print(f"barrier={BARRIER}")
    print(f"log-envelope exponent sum={exponent_sum}")
    print(f"reciprocal bound approximately {float(reciprocal):.15f}")
    print(f"even margin approximately {float(even_margin):.15e}")
    print(f"odd margin approximately {float(odd_margin):.15e}")
    print(f"next odd margin approximately {float(next_odd):.15e}")


if __name__ == "__main__":
    verify()
