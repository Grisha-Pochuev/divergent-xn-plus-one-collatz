#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from math import lcm

M = 4501
B = 1 << M
D0 = 349 * (1 << 500) - 347
X = B - D0


def ln2_bounds(terms: int = 2200) -> tuple[Fraction, Fraction]:
    z = Fraction(1, 3)
    z2 = z * z
    power = z
    lower = Fraction(0, 1)
    for j in range(terms):
        lower += power / (2 * j + 1)
        power *= z2
    lower *= 2
    remainder = 2 * power / (2 * terms + 1) / (1 - z2)
    return lower, lower + remainder


def ln1py_bounds() -> tuple[Fraction, Fraction]:
    y = Fraction(D0, X)
    lower = y - y * y / 2
    upper = lower + y * y * y / 3
    return lower, upper


def main() -> None:
    ln2_lo, ln2_hi = ln2_bounds()
    lny_lo, lny_hi = ln1py_bounds()
    common_bits = lcm(lny_lo.denominator, ln2_hi.denominator).bit_length()
    assert common_bits <= 22_206

    with localcontext() as ctx:
        ctx.prec = 3500
        inverse_delta = Decimal(2).ln() / (Decimal(B) / Decimal(X)).ln()

        for total_credit in range(1, M - 1):
            ell = int(Decimal(total_credit) * inverse_delta) + 1
            assert Fraction(ell - 1) * lny_hi < (
                Fraction(total_credit) * ln2_lo
            )
            assert Fraction(total_credit) * ln2_hi < Fraction(ell) * lny_lo

            z_lower = (
                Fraction(ell) * lny_lo
                - Fraction(total_credit) * ln2_hi
            )
            assert z_lower > 0
            assert z_lower.denominator.bit_length() <= common_bits

            # Whichever of the exceptional and ordinary blocks is shorter has
            # length at most floor(p/2).  One of the two dual core equations
            # has positive right side below 2*B^(floor(p/2)+1).
            assert ell >= 12
            assert (M - 1) * ell - common_bits > (
                1 + M * (ell // 2 + 1)
            )

    print("one-exception one-ordinary cycles are excluded")
    print("certified total credits=1..4499")
    print("both choices of the shorter block are covered")


if __name__ == "__main__":
    main()
