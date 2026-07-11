#!/usr/bin/env python3
"""Audit the retracted flow-completion endpoint identification."""
from __future__ import annotations

from verify_index_eight_small_sieve import M, ORDER_P, P, X
from verify_two_generation_predecessor_cost import O, output_label_map
from verify_two_generation_small_reciprocal import full_label, pohlig_hellman_data

TARGET = 25
EXPECTED_TARGET_LABEL = 1208196370322173126
EXPECTED_PREDECESSORS = (
    (50, 41063362403884138924, 1417145250304345366),
    (58, 29123312917045181557, 1528337129047052390),
    (72, 86491133267073699439, 1031609925039487316),
    (114, 49893509111834737687, 246249236019459722),
    (118, 96098755669746387853, 188856312470187702),
)


def verify() -> None:
    small_labels = output_label_map()
    allowed_mod_m = set(small_labels)
    tables, coefficients = pohlig_hellman_data()

    def is_full(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    target_label = full_label(
        TARGET,
        small_labels[TARGET % M],
        tables,
        coefficients,
    )
    assert target_label == EXPECTED_TARGET_LABEL

    modulus = X * X
    numerator = (
        pow(2, target_label, modulus) * TARGET - 1
    ) % modulus
    assert numerator % X == 0
    predecessor = (numerator // X) % X

    power = pow(2, O, modulus)
    assert (power - 1) % X == 0
    step = ((power - 1) // X) % X

    found: list[tuple[int, int, int]] = []
    for q in range(119):
        if is_full(predecessor):
            source_label = full_label(
                predecessor,
                small_labels[predecessor % M],
                tables,
                coefficients,
            )
            found.append((q, predecessor, source_label))
        predecessor = (predecessor + step) % X

    assert tuple(found[:5]) == EXPECTED_PREDECESSORS
    assert len({source for _q, _pred, source in found[:5]}) == 5

    # These different source labels lead to the same target.  Therefore the
    # least-cost source label is not necessarily the actual circulation
    # endpoint, which invalidates the retracted flow-completion charge.
    print("retracted flow-completion premise audited")
    print(f"target={TARGET}, target label={target_label}")
    for q, pred, source in found[:5]:
        print(f"q={q}, predecessor={pred}, source label={source}")
    print("retained small bound=0.085239095")
    print("retained sixty-million count=799470")


if __name__ == "__main__":
    verify()
