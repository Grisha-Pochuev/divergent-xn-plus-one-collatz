#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction

M = 156
D = 9
B = 1 << M
X = B - D


def ln2_bounds(terms: int = 90) -> tuple[Fraction, Fraction]:
    """Exact rational bounds from ln(2)=2*atanh(1/3)."""
    z = Fraction(1, 3)
    lower = 2 * sum(
        (z ** (2 * j + 1)) / (2 * j + 1) for j in range(terms)
    )
    remainder = (
        2
        * (z ** (2 * terms + 1))
        / Fraction(2 * terms + 1, 1)
        / (1 - z * z)
    )
    return lower, lower + remainder


def ln1py_bounds() -> tuple[Fraction, Fraction]:
    """Alternating-series bounds for ln(1+y), where y=9/X."""
    y = Fraction(D, X)
    lower = y - y * y / Fraction(2, 1)
    upper = lower + y * y * y / Fraction(3, 1)
    return lower, upper


def decimal_threshold(e: int) -> int:
    """Produce a candidate threshold; exact assertions below certify it."""
    with localcontext() as ctx:
        ctx.prec = 180
        b = Decimal(B)
        x = Decimal(X)
        delta = (b / x).ln() / Decimal(2).ln()
        return int(Decimal(e) / delta) + 1


def main() -> None:
    ln2_lo, ln2_hi = ln2_bounds()
    lny_lo, lny_hi = ln1py_bounds()
    modulus = B * B

    thresholds: list[int] = []
    minimum_residue_ratio: Fraction | None = None
    minimum_ratio_e: int | None = None

    for e in range(1, M):
        ell = decimal_threshold(e)

        # Certify ell-1 < e/delta < ell using exact rational intervals.
        assert Fraction(ell - 1, 1) * lny_hi < Fraction(e, 1) * ln2_lo
        assert Fraction(e, 1) * ln2_hi < Fraction(ell, 1) * lny_lo

        exponent = M * ell - e
        assert exponent >= 2 * M

        # At the first multiplicatively contracting length,
        # gap=2^(m*ell-e)-X^ell is positive. The first term vanishes mod B^2.
        residue = (-pow(X, ell, modulus)) % modulus
        additive = (1 << e) - 1
        assert residue > additive

        # A positive integer congruent to residue modulo B^2 is at least residue.
        # Hence gap>additive, so (-gap*u+additive)/D<0 for every odd u>=1.
        ratio = Fraction(residue, additive)
        if minimum_residue_ratio is None or ratio < minimum_residue_ratio:
            minimum_residue_ratio = ratio
            minimum_ratio_e = e
        thresholds.append(ell)

    assert len(thresholds) == 155
    assert thresholds == sorted(thresholds)
    assert minimum_residue_ratio is not None
    assert minimum_ratio_e is not None

    print(
        "verified sharp sign thresholds for all 155 "
        "nonexceptional terminal deficits"
    )
    print(f"first threshold (e=1): {thresholds[0]}")
    print(f"last threshold  (e=155): {thresholds[-1]}")
    print(
        "smallest residue/additive ratio occurs at "
        f"e={minimum_ratio_e}"
    )
    print(
        "ratio > "
        f"{minimum_residue_ratio.numerator // minimum_residue_ratio.denominator}"
    )


if __name__ == "__main__":
    main()
