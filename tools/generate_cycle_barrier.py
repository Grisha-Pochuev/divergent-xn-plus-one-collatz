#!/usr/bin/env python3
"""Generate explicit strong-Crandall candidates with a requested cycle barrier."""
from __future__ import annotations

import argparse
from math import isqrt
import json


def choose_k(barrier: int) -> int:
    if barrier < 1:
        raise ValueError("barrier must be positive")
    k = 8
    while (1 << k) <= 255 * barrier:
        k += 1
    return k


def construct_multiplier(barrier: int) -> tuple[int, int, int]:
    """Return (K,Q,floor(2^K*sqrt(2)))."""
    k = choose_k(barrier)
    square_target = 1 << (2 * k + 1)
    floor_root = isqrt(square_target)
    if floor_root * floor_root == square_target:
        raise AssertionError("unexpected square")

    t = (floor_root + 1 + 20) // 21
    while t % 2 == 0 or t % 3 == 0:
        t += 1
    q = 21 * t
    return k, q, floor_root


def verify_construction(barrier: int) -> dict[str, object]:
    k, q, floor_root = construct_multiplier(barrier)
    square_target = 1 << (2 * k + 1)

    if not (1 << k) > 255 * barrier:
        raise AssertionError("K size condition failed")
    if not q * q > square_target:
        raise AssertionError("Q is not above the half power")
    if q - floor_root > 84:
        raise AssertionError("Q is not close enough to the half power")
    if q % 21 != 0:
        raise AssertionError("Q is not divisible by 21")
    t = q // 21
    if t % 2 == 0 or t % 3 == 0:
        raise AssertionError("cofactor condition failed")
    if q % 9 == 0:
        raise AssertionError("3 must divide Q exactly once")
    if not (1 << k) < q + 1 < (1 << (k + 1)):
        raise AssertionError("first step could be the trivial 1 cycle")

    # This exact integer inequality implies B*(253/3)/2^K < 1/3.
    if not 253 * barrier < (1 << k):
        raise AssertionError("exponential headroom condition failed")

    return {
        "requested_cycle_barrier": barrier,
        "K": k,
        "Q": q,
        "Q_decimal_digits": len(str(q)),
        "Q_factor_21_cofactor": t,
        "floor_half_power": floor_root,
        "Q_minus_floor_half_power": q - floor_root,
        "proved_statement": (
            "the orbit from 1 never returns to 1 and any nontrivial "
            f"positive cycle it enters has length greater than {barrier}"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--barrier", type=int, required=True)
    args = parser.parse_args()
    print(json.dumps(verify_construction(args.barrier), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
