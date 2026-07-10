#!/usr/bin/env python3
"""Verify the exact minimum dichotomy for p=...193."""
from __future__ import annotations

from math import gcd

from verify_index_eight_small_sieve import M, ORDER_P, P, X
from verify_two_generation_predecessor_cost import O, output_label_map
from verify_two_generation_small_reciprocal import full_label, pohlig_hellman_data

BOUND = 5106101578294348744
EXPECTED_MINIMUM = 1672312375827977333
EXPECTED_TARGET_LABEL = 992055915950997467
EXPECTED_DELAY = 33
EXPECTED_PREDECESSOR = 26970074936991792008
EXPECTED_SOURCE_LABEL = 1684217191177655995


def exact_candidates(a: int) -> list[int]:
    modulus = 1 << (a + 1)
    residue = ((1 << a) - 1) * pow(X, -1, modulus) % modulus
    start = residue if residue > 0 else modulus
    return list(range(start, BOUND + 1, modulus))


def verify() -> None:
    labels = output_label_map()
    allowed_mod_m = set(labels)
    tables, coefficients = pohlig_hellman_data()

    def is_full(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    candidates55 = exact_candidates(55)
    candidates56 = exact_candidates(56)
    assert len(candidates55) == 71
    assert len(candidates56) == 35

    full55 = [m for m in candidates55 if is_full(m)]
    full56 = [m for m in candidates56 if is_full(m)]
    assert full55 == []
    assert full56 == [EXPECTED_MINIMUM]

    minimum = EXPECTED_MINIMUM
    small_label = labels[minimum % M]
    target_label = full_label(minimum, small_label, tables, coefficients)
    assert target_label == EXPECTED_TARGET_LABEL

    modulus = X * X
    numerator = (pow(2, target_label, modulus) * minimum - 1) % modulus
    assert numerator % X == 0
    predecessor = (numerator // X) % X

    power = pow(2, O, modulus)
    assert (power - 1) % X == 0
    step = ((power - 1) // X) % X
    assert step == 63726582940809041391
    assert gcd(step, X) == 3

    delay = 0
    while not is_full(predecessor):
        predecessor = (predecessor + step) % X
        delay += 1
        assert delay <= 6257

    assert delay == EXPECTED_DELAY
    assert predecessor == EXPECTED_PREDECESSOR
    source_small_label = labels[predecessor % M]
    source_label = full_label(
        predecessor, source_small_label, tables, coefficients
    )
    assert source_label == EXPECTED_SOURCE_LABEL

    assert X > 5792 * (1 << 54)

    print("first-length minimum dichotomy verified")
    print(f"exceptional minimum={minimum}")
    print(f"target label={target_label}")
    print(f"minimum incoming full-order delay={delay}")
    print(f"least predecessor residue={predecessor}")
    print(f"predecessor label={source_label}")
    print("otherwise outgoing valuation<=54 and next>5792*minimum")


if __name__ == "__main__":
    verify()
