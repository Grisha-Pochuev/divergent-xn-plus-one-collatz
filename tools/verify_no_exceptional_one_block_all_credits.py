#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from math import lcm

M = 4501
N = (1 << 500) - 1
D = 349 * (1 << 500) - 347
B = 1 << M
X = B - D


def ln2_bounds(terms: int = 2200) -> tuple[Fraction, Fraction]:
    """Exact rational bounds from ln(2)=2*atanh(1/3)."""
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
    """Alternating-series bounds for ln(1+y), y=D/X."""
    y = Fraction(D, X)
    lower = y - y * y / 2
    upper = lower + y * y * y / 3
    return lower, upper


def main() -> None:
    assert X >= 5 and X % 2 == 1
    assert X > B // 2
    assert D < B // 2

    ln2_lo, ln2_hi = ln2_bounds()
    lny_lo, lny_hi = ln1py_bounds()

    # The denominator of every positive lower bound
    # ell*lny_lo-e*ln2_hi divides this fixed common denominator.
    common_denominator = lcm(lny_lo.denominator, ln2_hi.denominator)
    common_bits = common_denominator.bit_length()
    assert common_bits <= 22_206

    with localcontext() as ctx:
        ctx.prec = 3500
        inverse_delta = Decimal(2).ln() / (Decimal(B) / Decimal(X)).ln()

        thresholds: list[int] = []
        for e in range(1, M):
            ell = int(Decimal(e) * inverse_delta) + 1

            # Exact certificate that ell is the first integer with ell*delta>e.
            assert Fraction(ell - 1) * lny_hi < Fraction(e) * ln2_lo
            assert Fraction(e) * ln2_hi < Fraction(ell) * lny_lo

            z_lower = Fraction(ell) * lny_lo - Fraction(e) * ln2_hi
            assert z_lower > 0
            assert z_lower.denominator.bit_length() <= common_bits

            # gap = X^ell*(exp(z)-1) > X^ell*z_lower.
            # Since X>2^(M-1) and z_lower>2^(-common_bits), this is >B.
            assert (M - 1) * ell - common_bits > M
            thresholds.append(ell)

    assert len(thresholds) == M - 1
    assert thresholds == sorted(thresholds)

    print("all ordinary one-block cycles are excluded")
    print(f"certified terminal deficits=1..{M-1}")
    print(f"fixed lower-bound denominator bits<={common_bits}")
    print(f"first threshold has {len(str(thresholds[0]))} decimal digits")
    print(f"last threshold has {len(str(thresholds[-1]))} decimal digits")


if __name__ == "__main__":
    main()
