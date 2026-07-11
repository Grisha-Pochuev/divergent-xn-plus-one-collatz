#!/usr/bin/env python3
"""Verify the complete valuation-block formulas for Mersenne multipliers."""
from __future__ import annotations

import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def step(X: int, n: int) -> tuple[int, int]:
    value = X * n + 1
    a = v2(value)
    return value >> a, a


def verify_nonexceptional() -> int:
    checked = 0
    for m in range(3, 11):
        B = 1 << m
        X = B - 1
        for s in range(1, m):
            for k in range(0, 12):
                r = m * k + s
                for u in range(1, 102, 2):
                    n = (1 << r) * u + 1
                    current = n
                    for j in range(k):
                        current, a = step(X, current)
                        if a != m:
                            raise AssertionError("expected an exact valuation-m step")
                        expected = (1 << (m * (k - j - 1) + s)) * X ** (j + 1) * u
                        if current - 1 != expected:
                            raise AssertionError("intermediate block identity failed")

                    endpoint, final_a = step(X, current)
                    if final_a != s:
                        raise AssertionError("wrong terminal valuation")
                    formula = X ** (k + 1) * u + (1 << (m - s))
                    if endpoint != formula:
                        raise AssertionError("nonexceptional endpoint formula failed")

                    difference = (
                        (X ** (k + 1) - (1 << r)) * u
                        + (1 << (m - s))
                        - 1
                    )
                    if endpoint - n != difference:
                        raise AssertionError("growth-difference identity failed")

                    if X ** (k + 1) > (1 << r) and endpoint <= n:
                        raise AssertionError("universal-growth implication failed")
                    if X ** (k + 1) <= (1 << r):
                        if not endpoint * (1 << r) > n * X ** (k + 1):
                            raise AssertionError("strict lower ratio failed")
                    checked += 1
    return checked


def verify_exceptional() -> int:
    checked = 0
    for m in range(3, 11):
        B = 1 << m
        X = B - 1
        for k in range(1, 12):
            r = m * k
            for u in range(1, 152, 2):
                n = (1 << r) * u + 1
                current = n
                for j in range(k - 1):
                    current, a = step(X, current)
                    if a != m:
                        raise AssertionError("expected valuation m before exception")
                    expected = (1 << (m * (k - j - 1))) * X ** (j + 1) * u
                    if current - 1 != expected:
                        raise AssertionError("exceptional intermediate identity failed")

                w = X ** (k - 1) * u
                if current != B * w + 1:
                    raise AssertionError("wrong exceptional pre-exit state")
                endpoint, final_a = step(X, current)
                w_endpoint, w_a = step(X, w)
                if final_a != m + w_a:
                    raise AssertionError("wrong exceptional valuation")
                if endpoint != w_endpoint:
                    raise AssertionError("identical-tail replacement failed")
                if not w < n:
                    raise AssertionError("replacement integer did not descend")
                checked += 1
    return checked


def verify_x15_thresholds() -> dict[str, int]:
    m = 4
    X = 15
    expected_last = {1: 31, 2: 20, 3: 9}
    first_r: dict[str, int] = {}
    for s, last_k in expected_last.items():
        if not X ** (last_k + 1) > 2 ** (m * last_k + s):
            raise AssertionError("claimed last growing block does not grow")
        next_k = last_k + 1
        if X ** (next_k + 1) > 2 ** (m * next_k + s):
            raise AssertionError("growth boundary is not maximal")
        first_r[str(s)] = m * next_k + s
    if first_r != {"1": 129, "2": 86, "3": 43}:
        raise AssertionError("wrong X=15 contraction thresholds")
    if (1 << 43) + 1 != 8_796_093_022_209:
        raise AssertionError("wrong smallest threshold input")
    return first_r


def verify_certificate() -> dict[str, object]:
    nonexceptional = verify_nonexceptional()
    exceptional = verify_exceptional()
    thresholds = verify_x15_thresholds()
    return {
        "m_range_checked": [3, 10],
        "nonexceptional_cases_checked": nonexceptional,
        "exceptional_cases_checked": exceptional,
        "total_cases_checked": nonexceptional + exceptional,
        "X15_first_contracting_r_by_s": thresholds,
        "X15_smallest_possible_nonexceptional_contraction_input": (1 << 43) + 1,
        "status": "exact block identities verified; divergence remains open",
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
