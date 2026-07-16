#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

M_EXP = 4501
B = 1 << M_EXP
D0 = 349 * (1 << 500) - 347
X = B - D0
N = (1 << 500) - 1
SCALE = 1 << 4002


def atanh_term(j: int) -> Fraction:
    """Term 1/((2j+1)3^(2j+1)) in ln(2)/2."""
    return Fraction(1, (2 * j + 1) * 3 ** (2 * j + 1))


def verify_ln2_bracket() -> tuple[Fraction, Fraction]:
    # ln(2)=2*sum_{j>=0} 1/((2j+1)3^(2j+1)).
    # Positivity gives the lower bound from the first three terms.
    lower = 2 * sum((atanh_term(j) for j in range(3)), Fraction())

    # For every j>=4,
    # t_(j+1)/t_j=((2j+1)/(2j+3))/9 < 1/9.
    # Thus sum_{j>=4} t_j < (9/8)t_4.
    for j in range(4, 20):
        assert atanh_term(j + 1) < atanh_term(j) / 9
    upper = 2 * (
        sum((atanh_term(j) for j in range(4)), Fraction())
        + Fraction(9, 8) * atanh_term(4)
    )

    assert lower == Fraction(842, 1215)
    assert upper == Fraction(1910051, 2755620)
    assert lower < upper
    return lower, upper


def verify_primary_drift_bracket() -> None:
    ln2_lower, ln2_upper = verify_ln2_bracket()

    # Put u=d/B. Then
    #   -ln(1-u)>u,
    #   -ln(1-u)<u/(1-u)=d/X.
    # The cycle-floor correction coefficient is
    #   epsilon=1/(X*N*ln(2)).
    lower_delta_minus_epsilon = (
        Fraction(D0, B) - Fraction(1, X * N)
    ) / ln2_upper
    upper_delta = Fraction(D0, X) / ln2_lower

    assert lower_delta_minus_epsilon > Fraction(1007, SCALE)
    assert upper_delta < Fraction(1008, SCALE)

    # The resulting full-cycle strip is
    #   D*SCALE/1008 < p < D*SCALE/1007.
    # Its relative width is exactly 1/1007 < 0.1%.
    assert Fraction(1008, 1007) - 1 == Fraction(1, 1007)
    assert Fraction(1, 1007) < Fraction(1, 1000)

    # The bounded initial macro-exit remains below 2^4005.
    assert Fraction(4500 * SCALE, 1007) < (1 << 4005)

    # The new lower length coefficient is stronger than 2^3992.
    assert Fraction(SCALE, 1008) > (1 << 3992)


def main() -> None:
    verify_primary_drift_bracket()
    print("primary 1/1007 cycle strip verified")
    print("1007*2^-4002 < delta-epsilon")
    print("delta < 1008*2^-4002")
    print("D*2^4002/1008 < p < D*2^4002/1007")
    print("relative strip width = 1/1007 < 0.1%")


if __name__ == "__main__":
    main()
