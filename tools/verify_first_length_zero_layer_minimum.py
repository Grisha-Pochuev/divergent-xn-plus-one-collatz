#!/usr/bin/env python3
"""Verify the all-zero-layer minimum structure for p=...193."""
from __future__ import annotations

from math import gcd

from verify_index_eight_small_sieve import M, ORDER_P, P, X
from verify_two_generation_predecessor_cost import O, output_label_map
from verify_two_generation_small_reciprocal import full_label, pohlig_hellman_data

BOUND = 5106101578294348744
EXPECTED_ZERO_COUNTS = (20, 15, 10, 6, 1, 0, 1, 0, 0, 0, 0, 0)
EXPECTED_MINIMUM = 2512233706332574837
EXPECTED_TARGET_LABEL = 1163144419278463552
EXPECTED_PREDECESSOR = 48574810891984207784
EXPECTED_SOURCE_LABEL = 450155079401401655


def exact_candidates(a: int) -> range:
    modulus = 1 << (a + 1)
    residue = ((1 << a) - 1) * pow(X, -1, modulus) % modulus
    start = residue if residue > 0 else modulus
    return range(start, BOUND + 1, modulus)


def verify() -> None:
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
    assert (power - 1) % X == 0
    step = ((power - 1) // X) % X
    assert step == 63726582940809041391
    assert gcd(step, X) == 3

    zero_survivors: dict[int, list[tuple[int, int, int, int]]] = {}

    for a in range(45, 57):
        rows: list[tuple[int, int, int, int]] = []
        for m in exact_candidates(a):
            if not is_full(m):
                continue

            target_small_label = labels[m % M]
            target_label = full_label(
                m, target_small_label, tables, coefficients
            )

            numerator = (
                pow(2, target_label, modulus_x2) * m - 1
            ) % modulus_x2
            assert numerator % X == 0
            predecessor = (numerator // X) % X

            if not is_full(predecessor):
                continue

            source_small_label = labels[predecessor % M]
            source_label = full_label(
                predecessor,
                source_small_label,
                tables,
                coefficients,
            )
            rows.append((m, target_label, predecessor, source_label))

        zero_survivors[a] = rows

    counts = tuple(len(zero_survivors[a]) for a in range(45, 57))
    assert counts == EXPECTED_ZERO_COUNTS

    assert zero_survivors[51] == [(
        EXPECTED_MINIMUM,
        EXPECTED_TARGET_LABEL,
        EXPECTED_PREDECESSOR,
        EXPECTED_SOURCE_LABEL,
    )]

    assert all(not zero_survivors[a] for a in range(52, 57))
    assert not zero_survivors[50]
    assert X > 185363 * (1 << 49)

    print("first-length zero-layer minimum verified")
    print(f"zero-delay counts a=45..56: {counts}")
    print(f"unique a=51 minimum={EXPECTED_MINIMUM}")
    print(f"predecessor residue={EXPECTED_PREDECESSOR}")
    print("otherwise outgoing valuation<=49")
    print("next value>185363*minimum")


if __name__ == "__main__":
    verify()
