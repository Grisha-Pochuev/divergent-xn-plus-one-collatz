#!/usr/bin/env python3
"""Verify the complete valuation-block formulas for X=13."""
from __future__ import annotations

import json


X = 13


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def step(n: int) -> tuple[int, int]:
    value = X * n + 1
    a = v2(value)
    return value >> a, a


def verify_nonexceptional() -> int:
    checked = 0
    expected_last_growing = {1: 9, 2: 5, 3: 2}

    for s in (1, 2, 3):
        growing_ks = [
            k for k in range(40) if X ** (k + 1) > 2 ** (4 * k + s)
        ]
        if max(growing_ks) != expected_last_growing[s]:
            raise AssertionError("wrong exact growth boundary")
        if X ** (expected_last_growing[s] + 2) > 2 ** (
            4 * (expected_last_growing[s] + 1) + s
        ):
            raise AssertionError("growth boundary is not maximal")

        for k in range(13):
            r = 4 * k + s
            for u in range(1, 202, 2):
                numerator = (1 << r) * u + 1
                if numerator % 3:
                    continue
                n = numerator // 3
                current = n

                for j in range(k):
                    next_value, a = step(current)
                    if a != 4:
                        raise AssertionError("expected an exact valuation-4 step")
                    current = next_value
                    expected_y = (1 << (4 * (k - j - 1) + s)) * X ** (j + 1) * u
                    if 3 * current - 1 != expected_y:
                        raise AssertionError("intermediate block identity failed")

                endpoint, final_a = step(current)
                if final_a != s:
                    raise AssertionError("wrong terminal valuation")
                formula = (X ** (k + 1) * u + (1 << (4 - s))) // 3
                if endpoint != formula:
                    raise AssertionError("nonexceptional endpoint formula failed")

                difference3 = (
                    (X ** (k + 1) - (1 << r)) * u
                    + (1 << (4 - s))
                    - 1
                )
                if 3 * (endpoint - n) != difference3:
                    raise AssertionError("growth-difference identity failed")

                if k <= expected_last_growing[s] and endpoint <= n:
                    raise AssertionError("universal-growth range failed")
                if k > expected_last_growing[s]:
                    if not endpoint * (1 << r) > n * X ** (k + 1):
                        raise AssertionError("contracting-block lower ratio failed")

                checked += 1

    return checked


def verify_exceptional() -> int:
    checked = 0
    for k in range(1, 13):
        r = 4 * k
        for u in range(1, 302, 2):
            numerator = (1 << r) * u + 1
            if numerator % 3:
                continue
            n = numerator // 3
            current = n

            for j in range(k - 1):
                next_value, a = step(current)
                if a != 4:
                    raise AssertionError("expected valuation 4 before exceptional exit")
                current = next_value
                expected_y = (1 << (4 * (k - j - 1))) * X ** (j + 1) * u
                if 3 * current - 1 != expected_y:
                    raise AssertionError("exceptional intermediate identity failed")

            w = X ** (k - 1) * u
            if current != ((1 << 4) * w + 1) // 3:
                raise AssertionError("wrong exceptional pre-exit state")

            endpoint, final_a = step(current)
            w_endpoint, w_a = step(w)
            if final_a != 4 + w_a:
                raise AssertionError("wrong exceptional valuation")
            if w_endpoint % 3:
                raise AssertionError("C(w) must be divisible by 3")
            if endpoint != w_endpoint // 3:
                raise AssertionError("exceptional descent formula failed")
            if not w < n:
                raise AssertionError("auxiliary integer did not descend")

            checked += 1

    return checked


def verify_threshold_minima() -> None:
    expected = {
        1: ((1 << 41) + 1) // 3,
        2: (5 * (1 << 26) + 1) // 3,
        3: ((1 << 15) + 1) // 3,
    }
    if expected[3] != 10_923:
        raise AssertionError("unexpected first s=3 threshold")

    for s, value in expected.items():
        if value <= 0 or value % 2 == 0:
            raise AssertionError(f"bad minimum for s={s}")
        r = v2(3 * value - 1)
        target_r = {1: 41, 2: 26, 3: 15}[s]
        if r != target_r:
            raise AssertionError(f"wrong threshold valuation for s={s}")


def verify_certificate() -> dict[str, int | str]:
    verify_threshold_minima()
    nonexceptional = verify_nonexceptional()
    exceptional = verify_exceptional()
    return {
        "X": X,
        "nonexceptional_cases_checked": nonexceptional,
        "exceptional_cases_checked": exceptional,
        "total_cases_checked": nonexceptional + exceptional,
        "first_possible_contracting_r_s1": 41,
        "first_possible_contracting_r_s2": 26,
        "first_possible_contracting_r_s3": 15,
        "status": "exact block identities verified; divergence remains open",
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
