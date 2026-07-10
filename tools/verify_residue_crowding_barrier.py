#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

X = 104350542602662257699
M = 15099
H = 2154
BARRIER = 170000000000000000000


def allowed_odd_representatives() -> list[int]:
    inv2 = pow(2, -1, M)
    residues: list[int] = []
    r = 1
    while r not in residues:
        residues.append(r)
        r = (r * inv2) % M
    assert len(residues) == H

    reps: list[int] = []
    for residue in residues:
        rep = residue if residue % 2 else residue + M
        if rep == 1:
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
    reps = allowed_odd_representatives()
    assert min(reps) == 25
    assert len(set(r % (2 * M) for r in reps)) == H

    s0 = sum((Fraction(1, r) for r in reps), Fraction(0, 1))
    z = Fraction(2 * M * (BARRIER - 1), 25)
    k = ceil_log2_fraction(1 + z)
    assert k == 78

    # log(2) < 7/10 gives an exact upper bound for the logarithmic tail.
    reciprocal_bound = s0 + Fraction(H * k, 2 * M) * Fraction(7, 10)

    epsilon = Fraction(X * X - (1 << 133), 1 << 133)
    assert epsilon > 0

    r_even = BARRIER // 2
    even_lhs = r_even * epsilon + reciprocal_bound / X
    assert even_lhs < Fraction(2, 3)  # log(2) > 2/3

    r_odd = (BARRIER - 1) // 2
    odd_lhs = r_odd * epsilon + reciprocal_bound / X
    q_num = 1 << 67
    # log(q) > 2(q-1)/(q+1), q=2^67/X.
    odd_log_lower = Fraction(2 * (q_num - X), q_num + X)
    assert odd_lhs < odd_log_lower

    print("residue-crowding barrier verified")
    print(f"X={X}")
    print(f"M={M}, order={H}, classes={len(reps)}")
    print(f"barrier={BARRIER}")
    print(f"log-envelope exponent k={k}")
    print(f"S0 approximately {float(s0):.15f}")
    print(f"even margin approximately {float(Fraction(2,3)-even_lhs):.15e}")
    print(f"odd margin approximately {float(odd_log_lower-odd_lhs):.15e}")


if __name__ == "__main__":
    verify()
