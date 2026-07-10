#!/usr/bin/env python3
"""Verify the retained residue-crowding cycle barrier with exact arithmetic.

The script checks the arithmetic premises used in the proof, enumerates the
complete set of allowed odd output classes modulo 2*M, and verifies the even-
and odd-length interval inequalities using only integers and Fractions.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd

X = 104350542602662257699
M = 15099
H = 2154
ORDER_PRIME_FACTORS = (2, 3, 359)
BARRIER = 170000000000000000000


def v2(n: int) -> int:
    assert n > 0
    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    return a


def verify_arithmetic_premises() -> None:
    # Output-class modulus and exact order of 2.
    assert M == 3 * 7 * 719
    assert X % M == 0
    assert H == 2 * 3 * 359
    assert pow(2, H, M) == 1
    for prime in ORDER_PRIME_FACTORS:
        assert H % prime == 0
        assert pow(2, H // prime, M) != 1

    # Premises for permanent avoidance of 1.
    # If C_X(n)=1, then 2^a == 1 modulo both 3 and 7, hence 6|a.
    # Since 2^6 == 1 (mod 9) and 3 divides X exactly once, such a
    # predecessor n=(2^a-1)/X is divisible by 3. Every accelerated output
    # is coprime to X, so the orbit from 1 cannot return to 1.
    assert X % 21 == 0
    assert X % 9 != 0
    assert pow(2, 1, 3) != 1 and pow(2, 2, 3) == 1
    assert pow(2, 1, 7) != 1 and pow(2, 3, 7) == 1
    assert pow(2, 6, 9) == 1

    first_a = v2(X + 1)
    first = (X + 1) >> first_a
    assert (first, first_a) == (26087635650665564425, 2)
    assert first != 1
    assert gcd(first, X) == 1

    # Half-power placement used to separate consecutive powers of two.
    assert X * X > (1 << 133)
    assert X < (1 << 67)


def allowed_odd_representatives() -> list[int]:
    inv2 = pow(2, -1, M)
    residues: list[int] = []
    seen: set[int] = set()
    r = 1
    while r not in seen:
        seen.add(r)
        residues.append(r)
        r = (r * inv2) % M

    assert r == 1
    assert len(residues) == H

    reps: list[int] = []
    for residue in residues:
        # Each residue modulo odd M has exactly one odd lift modulo 2*M.
        rep = residue if residue % 2 else residue + M
        if rep == 1:
            # The orbit cannot return to 1, so use the next member of this
            # arithmetic progression as its least admissible representative.
            rep += 2 * M
        reps.append(rep)
    return reps


def ceil_log2_fraction(value: Fraction) -> int:
    if value <= 1:
        return 0
    k = 0
    while (1 << k) * value.denominator < value.numerator:
        k += 1
    return k


def verify() -> None:
    verify_arithmetic_premises()

    reps = allowed_odd_representatives()
    assert min(reps) == 25
    assert len(set(r % (2 * M) for r in reps)) == H

    # Exact initial reciprocal sum over the 2154 least admissible values.
    s0 = sum((Fraction(1, r) for r in reps), Fraction(0, 1))

    # For every p<=BARRIER, monotonicity lets us use the single envelope at
    # p=BARRIER.  The logarithmic tail is bounded by log(1+z)<k*log(2).
    z = Fraction(2 * M * (BARRIER - 1), 25)
    k = ceil_log2_fraction(1 + z)
    assert k == 78

    # log(2) < 7/10 gives an exact upper bound for the logarithmic tail.
    reciprocal_bound = s0 + Fraction(H * k, 2 * M) * Fraction(7, 10)

    epsilon = Fraction(X * X - (1 << 133), 1 << 133)
    assert epsilon > 0

    # Even p=2r: total correction is strictly below log(2), so the cycle
    # product lies strictly between 2^(133r) and 2^(133r+1).
    r_even = BARRIER // 2
    even_lhs = r_even * epsilon + reciprocal_bound / X
    even_margin = Fraction(2, 3) - even_lhs
    assert even_margin > 0  # log(2) > 2/3

    # Odd p=2r+1: total correction is below log(2^67/X), so the product
    # lies strictly below 2^(133r+67), while X^p is already above
    # 2^(133r+66.5).
    r_odd = (BARRIER - 1) // 2
    odd_lhs = r_odd * epsilon + reciprocal_bound / X
    q_num = 1 << 67
    assert q_num > X
    # For q>1, log(q) > 2(q-1)/(q+1).
    odd_log_lower = Fraction(2 * (q_num - X), q_num + X)
    odd_margin = odd_log_lower - odd_lhs
    assert odd_margin > 0

    print("residue-crowding barrier verified")
    print(f"X={X}")
    print(f"M={M}, order={H}, classes={len(reps)}")
    print(f"barrier={BARRIER}")
    print(f"log-envelope exponent k={k}")
    print(f"S0 approximately {float(s0):.15f}")
    print(f"even margin above rational test {float(even_margin):.15e}")
    print(f"odd margin above rational test {float(odd_margin):.15e}")


if __name__ == "__main__":
    verify()
