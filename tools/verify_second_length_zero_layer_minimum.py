#!/usr/bin/env python3
"""Verify the all-zero-layer minimum structure for p=...195."""
from __future__ import annotations

from fractions import Fraction

from verify_first_length_refined_valley import (
    K,
    minimum_cheap_representative,
)
from verify_index_eight_small_sieve import M, ORDER_P, P, X
from verify_two_generation_predecessor_cost import O, output_label_map
from verify_two_generation_small_reciprocal import full_label, pohlig_hellman_data

TARGET = 177780727155637125195
EXPECTED_BOUND = 25894009212734490968
EXPECTED_ZERO_COUNTS = {
    50: 2,
    51: 3,
    52: 0,
    53: 1,
    54: 0,
    55: 0,
    56: 0,
    57: 0,
    58: 0,
}
EXPECTED_MINIMUM = 6815423150285083765
EXPECTED_TARGET_LABEL = 401703252155000920
EXPECTED_PREDECESSOR = 102306570270931706569
EXPECTED_SOURCE_LABEL = 1619960862681130392


def exact_candidates(a: int, bound: int) -> range:
    modulus = 1 << (a + 1)
    residue = ((1 << a) - 1) * pow(X, -1, modulus) % modulus
    start = residue if residue > 0 else modulus
    return range(start, bound + 1, modulus)


def verify() -> None:
    minimum_cheap, _pair, _count = minimum_cheap_representative()
    A = (133 * TARGET + 1) // 2
    expensive = 2 * (A - TARGET) // K
    cheap = TARGET - expensive
    required = Fraction(99_934_206, 1_000_000_000)
    residual = required - Fraction(cheap, minimum_cheap)
    forced_bound = (
        expensive * residual.denominator + residual.numerator - 1
    ) // residual.numerator - 1
    assert forced_bound == EXPECTED_BOUND

    labels = output_label_map()
    allowed_mod_m = set(labels)
    tables, coefficients = pohlig_hellman_data()

    def is_full(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    modulus_x2 = X * X
    power = pow(2, O, modulus_x2)
    step = ((power - 1) // X) % X

    rows_by_a: dict[int, list[tuple[int, int, int, int]]] = {}
    for a in range(50, 59):
        rows: list[tuple[int, int, int, int]] = []
        for m in exact_candidates(a, forced_bound):
            if not is_full(m):
                continue
            target_small = labels[m % M]
            target_label = full_label(m, target_small, tables, coefficients)
            numerator = (
                pow(2, target_label, modulus_x2) * m - 1
            ) % modulus_x2
            assert numerator % X == 0
            predecessor = (numerator // X) % X
            if not is_full(predecessor):
                continue
            source_small = labels[predecessor % M]
            source_label = full_label(
                predecessor, source_small, tables, coefficients
            )
            rows.append((m, target_label, predecessor, source_label))
        rows_by_a[a] = rows

    assert {a: len(rows_by_a[a]) for a in rows_by_a} == EXPECTED_ZERO_COUNTS
    assert rows_by_a[53] == [(
        EXPECTED_MINIMUM,
        EXPECTED_TARGET_LABEL,
        EXPECTED_PREDECESSOR,
        EXPECTED_SOURCE_LABEL,
    )]
    assert all(not rows_by_a[a] for a in range(54, 59))
    assert not rows_by_a[52]

    assert X > 11585 * (1 << 53)
    assert X > 46340 * (1 << 51)

    print("second-length zero-layer minimum verified")
    print(f"forced minimum bound={forced_bound}")
    print(f"zero-delay counts={EXPECTED_ZERO_COUNTS}")
    print(f"unique a=53 minimum={EXPECTED_MINIMUM}")
    print("otherwise outgoing valuation<=51 and next>46340*minimum")


if __name__ == "__main__":
    verify()
