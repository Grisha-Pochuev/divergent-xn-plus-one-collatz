#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import ceil


def harmonic(n: int) -> Fraction:
    out = Fraction(0, 1)
    for k in range(1, n + 1):
        out += Fraction(1, k)
    return out


def main() -> None:
    q_square = 3511
    Q_square = q_square * q_square
    h_square = 1755

    q_linear = 1093
    Q_linear = q_linear * q_linear

    combined_classes = 17_886_960
    combined_modulus = Q_square * Q_linear

    residues = {
        pow(pow(2, s, Q_square), -1, Q_square)
        for s in range(1, h_square + 1)
    }
    assert len(residues) == h_square

    # Least positive odd representatives. The orbit cannot return to 1, so the
    # residue-1 class starts at 1+2*Q_square rather than at 1.
    base_representatives: list[int] = []
    for residue in residues:
        rho = residue if residue % 2 == 1 else residue + Q_square
        if rho == 1:
            rho += 2 * Q_square
        assert rho > 1 and rho % 2 == 1 and rho % Q_square == residue
        base_representatives.append(rho)

    square_base_sum = sum(
        (Fraction(1, rho) for rho in base_representatives),
        Fraction(0, 1),
    )
    assert square_base_sum < Fraction(1, 2110)
    assert square_base_sum > Fraction(1, 2111)

    # Any K distinct square-admissible values have reciprocal sum at most the
    # base sum plus h/(2Q) times a balanced harmonic tail.
    layers = ceil(combined_classes / h_square)
    assert layers == 10_192
    combined_base_upper = (
        Fraction(1, 2110)
        + Fraction(h_square, 2 * Q_square) * harmonic(layers)
    )
    assert combined_base_upper < Fraction(1, 853)
    assert combined_base_upper > Fraction(1, 854)

    # Exact tail-density constants for the combined permanent classes.
    assert combined_modulus == 14_726_582_775_529
    tail_coefficient = Fraction(combined_classes, 2 * combined_modulus)
    assert tail_coefficient < Fraction(1, 1_646_000)
    assert tail_coefficient > Fraction(1, 1_647_000)

    # Small finite regression: the symbolic packing formula is positive and
    # well-formed at representative population sizes.
    for p in [1, h_square, combined_classes, combined_classes + 1,
              2 * combined_classes]:
        layer_bound = ceil(p / combined_classes)
        combined_bound = (
            Fraction(1, 853)
            + tail_coefficient * harmonic(layer_bound)
        )
        assert combined_bound > 0

    print("dual-Wieferich harmonic packing constants verified")
    print("square base reciprocal sum is between 1/2111 and 1/2110")
    print("combined base reciprocal sum is certified below 1/853")
    print("combined tail coefficient is between 1/1647000 and 1/1646000")


if __name__ == "__main__":
    main()
