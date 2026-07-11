#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from math import lcm

M = 4501
D0 = 349 * (1 << 500) - 347
B = 1 << M
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
    assert X > 1 << (M - 1)

    ln2_lo, ln2_hi = ln2_bounds()
    lny_lo, lny_hi = ln1py_bounds()
    common_bits = lcm(lny_lo.denominator, ln2_hi.denominator).bit_length()
    assert common_bits <= 22_206

    with localcontext() as ctx:
        ctx.prec = 3500
        inverse_delta = Decimal(2).ln() / (Decimal(B) / Decimal(X)).ln()

        thresholds: list[int] = []
        for total_deficit in range(2, 2 * M - 1):
            ell = int(Decimal(total_deficit) * inverse_delta) + 1

            assert Fraction(ell - 1) * lny_hi < (
                Fraction(total_deficit) * ln2_lo
            )
            assert Fraction(total_deficit) * ln2_hi < Fraction(ell) * lny_lo

            z_lower = (
                Fraction(ell) * lny_lo
                - Fraction(total_deficit) * ln2_hi
            )
            assert z_lower > 0
            assert z_lower.denominator.bit_length() <= common_bits

            # The positive cycle gap is >2^(4500*p-common_bits).
            # With the shorter block at most floor(p/2), the complete additive
            # numerator is <2*B^(floor(p/2)+1).
            assert ell >= 12
            assert (M - 1) * ell - common_bits > (
                1 + M * (ell // 2 + 1)
            )
            thresholds.append(ell)

    assert len(thresholds) == 2 * M - 3
    assert thresholds == sorted(thresholds)

    print("all ordinary two-block cycles are excluded")
    print("certified total deficits=2..9000")
    print(f"fixed lower-bound denominator bits<={common_bits}")
    print(f"first threshold has {len(str(thresholds[0]))} decimal digits")
    print(f"last threshold has {len(str(thresholds[-1]))} decimal digits")


if __name__ == "__main__":
    main()
