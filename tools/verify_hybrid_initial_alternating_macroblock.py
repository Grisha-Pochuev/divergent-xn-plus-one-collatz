#!/usr/bin/env python3
"""Verify the exact initial (1,2)-macroblock for X=2^m-3."""
from __future__ import annotations

import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def odd_step(x: int, n: int) -> tuple[int, int]:
    numerator = x * n + 1
    a = v2(numerator)
    return numerator >> a, a


def pair_map(x: int, n: int) -> int:
    numerator = x * x * n + x + 2
    if numerator % 8:
        raise AssertionError("pair formula is not integral")
    return numerator // 8


def verify_forced_pair_grid() -> int:
    checked = 0
    for m in range(4, 18):
        b = 1 << m
        x = b - 3
        for q in range(0, 200):
            n = 16 * q + 1
            if n <= 0 or n % 2 == 0:
                continue
            n1, a1 = odd_step(x, n)
            n2, a2 = odd_step(x, n1)
            if (a1, a2) != (1, 2):
                raise AssertionError((m, n, a1, a2))
            if n2 != pair_map(x, n):
                raise AssertionError("two-step affine formula failed")
            identity_num = x * x * (n - 1) + b * (b - 5)
            if identity_num % 8 or n2 - 1 != identity_num // 8:
                raise AssertionError("precision-transfer identity failed")
            checked += 1
    return checked


def verify_precision_transfer_grid() -> int:
    checked = 0
    for m in range(5, 22):
        b = 1 << m
        x = b - 3
        for length in range(4, m):
            for u in range(1, 40, 2):
                n = 1 + (1 << length) * u
                n2 = pair_map(x, n)
                if v2(n2 - 1) != length - 3:
                    raise AssertionError((m, length, u, v2(n2 - 1)))
                checked += 1
    return checked


def verify_initial_macroblocks() -> int:
    checked = 0
    for m in range(4, 80):
        x = (1 << m) - 3
        pairs = (m - 1) // 3
        n = 1
        valuations: list[int] = []
        for _ in range(pairs):
            n, a1 = odd_step(x, n)
            n, a2 = odd_step(x, n)
            valuations.extend((a1, a2))
        if valuations != [1, 2] * pairs:
            raise AssertionError("initial valuation word failed")
        if sum(valuations) != 3 * pairs:
            raise AssertionError("initial total valuation failed")
        if v2(n - 1) != m - 3 * pairs:
            raise AssertionError("terminal precision failed")
        if not n * (1 << (3 * pairs)) > x ** (2 * pairs):
            raise AssertionError("strict macroblock growth lower bound failed")
        checked += 1
    return checked


def verify_hybrid_case() -> dict[str, int | str]:
    m = 260
    x = (1 << m) - 3
    pairs = (m - 1) // 3
    if pairs != 86:
        raise AssertionError("unexpected hybrid pair count")

    n = 1
    valuations: list[int] = []
    for _ in range(pairs):
        n, a1 = odd_step(x, n)
        n, a2 = odd_step(x, n)
        valuations.extend((a1, a2))

    if valuations != [1, 2] * 86:
        raise AssertionError("hybrid valuation word failed")
    if sum(valuations) != 258:
        raise AssertionError("hybrid total valuation failed")
    if v2(n - 1) != 2:
        raise AssertionError("hybrid endpoint precision failed")
    if not n * (1 << 258) > x ** 172:
        raise AssertionError("hybrid growth inequality failed")

    return {
        "m": m,
        "X": x,
        "forced_pairs": pairs,
        "forced_accelerated_steps": 2 * pairs,
        "valuation_word": "(1,2)^86",
        "total_valuation": sum(valuations),
        "endpoint_v2_n_minus_1": v2(n - 1),
        "endpoint_bit_length": n.bit_length(),
    }


def main() -> None:
    print(json.dumps({
        "forced_pair_grid_cases": verify_forced_pair_grid(),
        "precision_transfer_cases": verify_precision_transfer_grid(),
        "initial_macroblocks_checked": verify_initial_macroblocks(),
        "hybrid": verify_hybrid_case(),
        "strict_prize_solution": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
