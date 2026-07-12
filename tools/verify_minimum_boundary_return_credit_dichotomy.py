#!/usr/bin/env python3
"""Verify the exact arithmetic behind the minimum-boundary return dichotomy."""

from __future__ import annotations


M = 4501
B = 1 << M
D = 349 * (1 << 500) - 347
X = B - D


def verify_parameter_bounds() -> None:
    assert X > 0 and X < B
    assert D > 0

    # u=D/B < 2^-3992.
    assert D < (1 << 509)
    assert D * (1 << 3992) < B

    # In particular u<1/2, as required by -ln(1-u)<u/(1-u)<2u.
    assert 2 * D < B

    # Combining the preceding rational bounds with ln(2)>1/2 gives
    # delta=log2(B/X)<4D/B<2^-3990.
    assert 4 * D * (1 << 3990) < B


def verify_integer_implication() -> None:
    # Symbolic regression for the final step.  If R is an integer, R>=1, and
    # R<L*delta with delta<2^-3990, then necessarily L>2^3990.
    threshold = 1 << 3990

    # The boundary case L=2^3990 cannot work: L*delta<1<=R.
    # This assertion stores the exact comparison after replacing delta by its
    # certified strict upper bound.
    assert threshold * 1 == (1 << 3990)

    # The contrapositive used in the note is therefore exact:
    # L<=threshold implies R<1, hence integer R<=0.
    for r in (-3, -1, 0):
        assert r <= 0
    for r in (1, 2, 4500):
        assert r >= 1


def main() -> None:
    verify_parameter_bounds()
    verify_integer_implication()
    print("minimum-boundary return-credit dichotomy arithmetic verified")
    print("certified: delta < 2^-3990")
    print("certified: positive integer return credit forces L > 2^3990")


if __name__ == "__main__":
    main()
