#!/usr/bin/env python3
"""Verify the refined minimum valley for p=...193 exactly."""
from __future__ import annotations

from fractions import Fraction

from verify_index_eight_small_sieve import M, ORDER_P, P, X
from verify_two_generation_predecessor_cost import output_label_map

TARGET = 177780727155637125193
K = 9000
EXPECTED_EXPENSIVE = 2587697250820940377
EXPECTED_MINIMUM_CHEAP = 437624995949268865515542163747121
EXPECTED_PAIR = (2736, 5392)
EXPECTED_MINIMUM_BOUND = 5106101578294348744
EXPECTED_COUNTS = (18, 9, 4, 3, 1, 1, 0, 0, 0, 0)


def minimum_cheap_representative() -> tuple[int, tuple[int, int], int]:
    modulus = X * X
    inv_x = [0] + [pow(2, -u, X) for u in range(1, K + 1)]
    inv_x2 = [0] + [pow(2, -v, modulus) for v in range(1, K + 1)]

    minimum = 2 * modulus
    argmin = (0, 0)
    count = 0
    for u in range(1, K + 1):
        rhs = 1 + X * inv_x[u]
        for v in range(1, K + 2 - u):
            representative = inv_x2[v] * rhs % modulus
            if representative % 2 == 0:
                representative += modulus
            if representative < minimum:
                minimum = representative
                argmin = (u, v)
            count += 1
    return minimum, argmin, count


def verify() -> None:
    minimum, pair, count = minimum_cheap_representative()
    assert count == K * (K + 1) // 2 == 40_504_500
    assert minimum == EXPECTED_MINIMUM_CHEAP
    assert pair == EXPECTED_PAIR

    A = (133 * TARGET + 1) // 2
    expensive = 2 * (A - TARGET) // K
    assert expensive == EXPECTED_EXPENSIVE
    cheap = TARGET - expensive

    required = Fraction(506_785_306, 1_000_000_000)
    residual = required - Fraction(cheap, minimum)
    assert residual > 0
    forced_target = (
        expensive * residual.denominator + residual.numerator - 1
    ) // residual.numerator - 1
    assert forced_target == EXPECTED_MINIMUM_BOUND

    allowed_mod_m = set(output_label_map())
    counts: list[int] = []
    for a in range(57, 67):
        modulus = 1 << (a + 1)
        residue = ((1 << a) - 1) * pow(X, -1, modulus) % modulus
        start = residue if residue > 0 else modulus
        candidates = list(range(start, forced_target + 1, modulus))
        counts.append(len(candidates))

        for m in candidates:
            assert (X * m + 1) % (1 << a) == 0
            assert (X * m + 1) % (1 << (a + 1)) != 0
            is_full = (
                m % M in allowed_mod_m
                and pow(m % P, ORDER_P, P) == 1
            )
            assert not is_full

    assert tuple(counts) == EXPECTED_COUNTS
    assert X > 1448 * (1 << 56)

    print("first remaining length refined valley verified")
    print(f"target={TARGET}")
    print(f"cheap pair classes={count}")
    print(f"minimum cheap representative={minimum} at pair={pair}")
    print(f"forced cycle minimum<={forced_target}")
    print("outgoing valuation<=56")
    print("next value>1448*minimum")


if __name__ == "__main__":
    verify()
