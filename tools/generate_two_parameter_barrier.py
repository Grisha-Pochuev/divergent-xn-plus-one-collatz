#!/usr/bin/env python3
"""Generate exact candidates with prescribed cycle length and height barriers."""
from __future__ import annotations

import argparse
from math import isqrt
import json


def choose_m(height: int) -> int:
    if height < 1:
        raise ValueError("height must be positive")
    m = 3
    while (1 << m) - 1 <= height:
        m += 6
    return m


def choose_k(length: int, mersenne: int) -> int:
    if length < 1:
        raise ValueError("length must be positive")
    k = 1
    while (1 << k) <= 40 * length * mersenne:
        k += 1
    return k


def construct_multiplier(length: int, height: int) -> tuple[int, int, int, int, int]:
    """Return (m,M,K,Q,floor(2^K*sqrt(2)))."""
    m = choose_m(height)
    mersenne = (1 << m) - 1
    k = choose_k(length, mersenne)
    root = isqrt(1 << (2 * k + 1))

    step = 3 * mersenne
    t = (root + 1 + step - 1) // step
    while t % 2 == 0 or t % 3 == 0:
        t += 1
    q = step * t
    return m, mersenne, k, q, root


def verify_construction(length: int, height: int) -> dict[str, object]:
    m, mersenne, k, q, root = construct_multiplier(length, height)
    t = q // (3 * mersenne)

    if m % 6 != 3:
        raise AssertionError("m must be an odd multiple of 3")
    if mersenne != (1 << m) - 1 or mersenne <= height:
        raise AssertionError("Mersenne height barrier failed")
    if mersenne % 7 != 0 or mersenne % 3 == 0:
        raise AssertionError("Mersenne congruence conditions failed")
    if not (1 << k) > 40 * length * mersenne:
        raise AssertionError("K size condition failed")
    if q != 3 * mersenne * t or t % 2 == 0 or t % 3 == 0:
        raise AssertionError("multiplier form failed")
    if q % 9 == 0:
        raise AssertionError("3 must divide Q exactly once")
    if not q * q > (1 << (2 * k + 1)):
        raise AssertionError("Q is not above the half power")
    if q - root > 12 * mersenne:
        raise AssertionError("Q is not close enough to the half power")
    if not (1 << k) < q + 1 < (1 << (k + 1)):
        raise AssertionError("first step could remain at 1")

    return {
        "requested_cycle_length_barrier": length,
        "requested_cycle_height_barrier": height,
        "m": m,
        "M": mersenne,
        "K": k,
        "Q": q,
        "Q_decimal_digits": len(str(q)),
        "cofactor_t": t,
        "Q_minus_floor_half_power": q - root,
        "proved_statement": (
            "the orbit from 1 never returns to 1; every possible nontrivial "
            f"cycle has length greater than {length} and all elements "
            f"greater than {height}"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    args = parser.parse_args()
    print(json.dumps(verify_construction(args.length, args.height), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
