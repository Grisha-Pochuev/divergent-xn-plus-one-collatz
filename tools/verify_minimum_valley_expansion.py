#!/usr/bin/env python3
"""Verify the strong expansion from a remaining-cycle minimum exactly."""
from __future__ import annotations

from verify_index_eight_small_sieve import (
    M,
    ORDER_P,
    P,
    X,
)
from verify_two_generation_predecessor_cost import output_label_map

BOUNDS = (
    9190982840926584716,
    46609216582838682965,
)
EXPECTED_COUNTS = (
    (8, 4, 2, 1, 1, 0, 0, 0),
    (40, 21, 10, 5, 3, 1, 0, 0),
)


def exact_class(a: int) -> tuple[int, int]:
    modulus = 1 << (a + 1)
    residue = ((1 << a) - 1) * pow(X, -1, modulus) % modulus
    return residue, modulus


def verify() -> None:
    assert X + 1 < (1 << 67)
    allowed_mod_m = set(output_label_map())

    for bound, expected in zip(BOUNDS, EXPECTED_COUNTS):
        counts: list[int] = []
        for a in range(59, 67):
            residue, modulus = exact_class(a)
            start = residue if residue > 0 else modulus
            candidates = list(range(start, bound + 1, modulus))
            counts.append(len(candidates))

            for m in candidates:
                assert (X * m + 1) % (1 << a) == 0
                assert (X * m + 1) % (1 << (a + 1)) != 0

                is_full = (
                    m % M in allowed_mod_m
                    and pow(m % P, ORDER_P, P) == 1
                )
                assert not is_full

        assert tuple(counts) == expected

    assert X > 362 * (1 << 58)

    print("minimum valley expansion verified")
    print(f"minimum bounds={BOUNDS}")
    print("outgoing valuations 59 through 66 excluded")
    print("outgoing valuation<=58")
    print("next value>362*minimum")


if __name__ == "__main__":
    verify()
