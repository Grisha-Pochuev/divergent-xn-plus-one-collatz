#!/usr/bin/env python3
"""Check the exact near-power exceptional-descent identities."""
from __future__ import annotations

import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def odd_step(X: int, n: int) -> tuple[int, int]:
    numerator = X * n + 1
    valuation = v2(numerator)
    return numerator >> valuation, valuation


def verify_case(m: int, d: int, n: int) -> str:
    B = 1 << m
    X = B - d
    if m < 3 or d <= 0 or d >= B or d % 2 == 0 or X < 5:
        raise ValueError("invalid near-power parameters")
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be positive and odd")

    difference = d * n - 1
    output, valuation = odd_step(X, n)

    # The sole zero difference is the trivial Mersenne fixed point.
    if difference == 0:
        if (d, n, output, valuation) != (1, 1, 1, m):
            raise AssertionError("wrong trivial Mersenne case")
        return "fixed_one"

    r = v2(difference)
    u = difference >> r
    if u % 2 == 0:
        raise AssertionError("u must be odd")

    if r < m:
        if valuation != r:
            raise AssertionError("low case has the wrong valuation")
        if output != (1 << (m - r)) * n - u:
            raise AssertionError("low-case output identity failed")
        return "low"

    if r > m:
        if valuation != m:
            raise AssertionError("strip case has the wrong valuation")
        if output != n - (1 << (r - m)) * u:
            raise AssertionError("strip-case output identity failed")
        if v2(d * output - 1) != r - m:
            raise AssertionError("strip-case residual valuation failed")
        return "strip"

    # Exceptional case r=m.
    if n != (B * u + 1) // d or (B * u + 1) % d:
        raise AssertionError("exceptional representation failed")

    smaller_output, smaller_valuation = odd_step(X, u)
    if (X * n + 1) * d != B * (X * u + 1):
        raise AssertionError("exceptional affine identity failed")
    if (X * u + 1) % d:
        raise AssertionError("required odd divisibility failed")
    if valuation != m + smaller_valuation:
        raise AssertionError("exceptional valuation identity failed")
    if smaller_output % d:
        raise AssertionError("smaller output is not divisible by d")
    if output != smaller_output // d:
        raise AssertionError("exceptional output identity failed")
    if not u < n:
        raise AssertionError("exceptional auxiliary integer must be smaller")
    return "exceptional"


def verify_x13_examples() -> dict[str, object]:
    # One example of each nontrivial branch.
    examples = {
        "low": 1,          # v2(3*n-1)=1<4
        "strip": 11,       # v2(3*n-1)=5>4
        "exceptional": 27, # 27=(16*5+1)/3
    }
    report: dict[str, object] = {}
    for expected, n in examples.items():
        branch = verify_case(4, 3, n)
        if branch != expected:
            raise AssertionError(f"expected {expected}, got {branch}")
        output, valuation = odd_step(13, n)
        report[expected] = {
            "n": n,
            "valuation": valuation,
            "output": output,
        }

    # Explicit exceptional identity for n=27 and u=5:
    # C_13(27)=11 and C_13(5)=33, hence 11=33/3.
    if odd_step(13, 27) != (11, 5):
        raise AssertionError("wrong X=13 exceptional example")
    if odd_step(13, 5) != (33, 1):
        raise AssertionError("wrong smaller X=13 example")
    return report


def verify_grid() -> dict[str, int]:
    counts = {"fixed_one": 0, "low": 0, "strip": 0, "exceptional": 0}
    checked = 0
    for m in range(3, 10):
        B = 1 << m
        for d in range(1, B, 2):
            if B - d < 5:
                continue
            for n in range(1, 5000, 2):
                branch = verify_case(m, d, n)
                counts[branch] += 1
                checked += 1
    counts["checked_parameter_state_triples"] = checked
    return counts


def main() -> None:
    print(json.dumps({
        "theorem": "near-power exceptional descent",
        "x13_examples": verify_x13_examples(),
        "finite_regression_grid": verify_grid(),
        "is_divergence_proof": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
