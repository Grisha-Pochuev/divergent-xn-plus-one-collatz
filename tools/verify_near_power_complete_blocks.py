#!/usr/bin/env python3
"""Verify complete blocks for X=2^m-d and the hybrid specialization."""
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


def check_family_case(m: int, d: int, k: int, s: int, u: int) -> None:
    b = 1 << m
    x = b - d
    r = m * k + s
    numerator = (1 << r) * u + 1
    if numerator % d:
        return
    n = numerator // d
    if n <= 0 or n % 2 == 0:
        return

    current = n
    valuations: list[int] = []
    for _ in range(k + 1):
        current, a = odd_step(x, current)
        valuations.append(a)

    expected_values = [m] * k + [s]
    expected_endpoint_num = x ** (k + 1) * u + (1 << (m - s))
    if expected_endpoint_num % d:
        raise AssertionError("endpoint divisibility failed")
    expected_endpoint = expected_endpoint_num // d
    if valuations != expected_values or current != expected_endpoint:
        raise AssertionError((m, d, k, s, u, valuations, current, expected_endpoint))

    displacement_num = (
        (x ** (k + 1) - (1 << (m * k + s))) * u
        + (1 << (m - s)) - 1
    )
    if displacement_num % d or displacement_num // d != current - n:
        raise AssertionError("block displacement formula failed")

    if x ** (k + 1) > (1 << (m * k + s)) and not current > n:
        raise AssertionError("universal growth condition failed")


def check_exceptional_case(m: int, d: int, k: int, u: int) -> None:
    b = 1 << m
    x = b - d
    r = m * k
    numerator = (1 << r) * u + 1
    if numerator % d:
        return
    n = numerator // d
    if n <= 0 or n % 2 == 0:
        return

    current = n
    for _ in range(k):
        current, _ = odd_step(x, current)

    w = x ** (k - 1) * u
    core, _ = odd_step(x, w)
    if core % d:
        raise AssertionError("exceptional quotient is not integral")
    expected = core // d
    if current != expected:
        raise AssertionError("complete exceptional endpoint failed")
    if not current < n:
        raise AssertionError("exceptional block must strictly contract")


def verify_small_grid() -> int:
    checked = 0
    for m in range(3, 10):
        b = 1 << m
        for d in range(1, b // 2, 2):
            x = b - d
            if x < 5:
                continue
            for k in range(0, 5):
                for s in range(1, m):
                    for u in range(1, 32, 2):
                        before = checked
                        numerator = (1 << (m * k + s)) * u + 1
                        if numerator % d == 0 and (numerator // d) % 2 == 1:
                            checked += 1
                        check_family_case(m, d, k, s, u)
            for k in range(1, 5):
                for u in range(1, 32, 2):
                    check_exceptional_case(m, d, k, u)
    return checked


def verify_minimal_basin_growth_samples() -> int:
    checked = 0
    for m, d in ((4, 3), (7, 3), (8, 5), (10, 3), (12, 7)):
        b = 1 << m
        x = b - d
        for r in range(1, m):
            for u in range(1, 50, 2):
                numerator = (1 << r) * u + 1
                if numerator % d:
                    continue
                n = numerator // d
                if n <= 0 or n % 2 == 0:
                    continue
                nxt, a = odd_step(x, n)
                if a != r or not nxt > n:
                    raise AssertionError("low-layer minimal-basin growth failed")
                exact_difference_num = (b - (1 << r) - d) * n + 1
                if exact_difference_num % (1 << r):
                    raise AssertionError("difference integrality failed")
                if nxt - n != exact_difference_num >> r:
                    raise AssertionError("minimal-basin difference formula failed")
                checked += 1
    return checked


def verify_hybrid_samples() -> int:
    m = 260
    d = 3
    checked = 0
    for k, s in ((0, 1), (0, 259), (1, 1), (1, 137), (2, 259)):
        for u in range(1, 40, 2):
            numerator = (1 << (m * k + s)) * u + 1
            if numerator % d or (numerator // d) % 2 == 0:
                continue
            check_family_case(m, d, k, s, u)
            checked += 1
    for k in (1, 2, 3):
        for u in range(1, 40, 2):
            check_exceptional_case(m, d, k, u)
    return checked


def main() -> None:
    print(json.dumps({
        "small_nonexceptional_cases_checked": verify_small_grid(),
        "minimal_basin_growth_samples_checked": verify_minimal_basin_growth_samples(),
        "hybrid_nonexceptional_samples_checked": verify_hybrid_samples(),
        "strict_prize_solution": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
