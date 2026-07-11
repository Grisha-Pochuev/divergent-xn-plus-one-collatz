#!/usr/bin/env python3
"""Verify the exact arithmetic in MERSENNE_SECOND_BLOCK_ESCALATION.md."""
from __future__ import annotations

import json

B = 16
X = 15
K = {1: 32, 2: 21, 3: 10}


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def odd_step(n: int) -> tuple[int, int]:
    numerator = X * n + 1
    a = v2(numerator)
    return numerator >> a, a


def verify_thresholds() -> None:
    for s, threshold in K.items():
        if not X ** (threshold + 1) < 2 ** (4 * threshold + s):
            raise AssertionError(f"threshold does not contract for s={s}")
        if threshold > 0 and not X ** threshold > 2 ** (4 * (threshold - 1) + s):
            raise AssertionError(f"threshold is not minimal for s={s}")


def verify_universal_minimality_inequalities() -> None:
    for s, threshold in K.items():
        for t in (1, 2, 3):
            # It is enough to check the least k and least positive odd v.
            left = (1 << t) * ((1 << (4 * threshold + s)) - X ** (threshold + 1))
            right = B - (1 << s)
            if not left > right:
                raise AssertionError((s, t, threshold, left, right))

            # Once positive, the coefficient difference is strictly increasing:
            # d_(k+1)=15*d_k+2^(4*k+s).
            d = (1 << (4 * threshold + s)) - X ** (threshold + 1)
            d_next = (1 << (4 * (threshold + 1) + s)) - X ** (threshold + 2)
            if d_next != X * d + (1 << (4 * threshold + s)):
                raise AssertionError("difference recurrence failed")
            if not d_next > d > 0:
                raise AssertionError("difference must increase after threshold")


def verify_parametric_coordinates() -> int:
    checked = 0
    for s in (1, 2, 3):
        offset = (1 << (4 - s)) - 1
        for k in range(0, K[s] + 4):
            for t in (1, 2, 3):
                # Scan a complete set of odd v modulo 30.  Integrality of u is
                # periodic modulo 15 because powers of two are units modulo 15.
                for v in range(1, 30, 2):
                    numerator = (1 << (4 * k + t)) * v - offset
                    if numerator % X:
                        continue
                    u = numerator // X
                    if u <= 0 or u % 2 == 0:
                        continue

                    w = (1 << s) * u + 1
                    y = X * u + (1 << (4 - s))
                    if y - 1 != (1 << (4 * k + t)) * v:
                        raise AssertionError("second-state coordinate failed")
                    if not y > w:
                        raise AssertionError("minimal seed first step must grow")

                    state = y
                    valuations: list[int] = []
                    for _ in range(k):
                        state, a = odd_step(state)
                        valuations.append(a)
                    p = (1 << t) * (X ** k) * v + 1
                    if valuations != [4] * k or state != p:
                        raise AssertionError("pre-exit state formula failed")

                    formula_w_num = (1 << (4 * k + t + s)) * v + (1 << s) - 1
                    if formula_w_num % X or formula_w_num // X != w:
                        raise AssertionError("recovered w formula failed")

                    if k >= K[s] and not p < w:
                        raise AssertionError("minimality inequality failed")
                    checked += 1
    return checked


def verify_escalation_table() -> dict[int, list[tuple[int, int, int]]]:
    remaining: dict[int, list[tuple[int, int, int]]] = {}
    for s in (1, 2, 3):
        rows: list[tuple[int, int, int]] = []
        for t in (1, 2, 3):
            lower = K[t]
            upper = K[s] - 1
            if lower <= upper:
                rows.append((t, lower, upper))
                if not t > s:
                    raise AssertionError("contracting type did not escalate")
        remaining[s] = rows

    expected = {
        1: [(2, 21, 31), (3, 10, 31)],
        2: [(3, 10, 20)],
        3: [],
    }
    if remaining != expected:
        raise AssertionError((remaining, expected))
    return remaining


def main() -> None:
    verify_thresholds()
    verify_universal_minimality_inequalities()
    checked = verify_parametric_coordinates()
    table = verify_escalation_table()
    print(json.dumps({
        "X": X,
        "thresholds": K,
        "parametric_cases_checked": checked,
        "remaining_contracting_second_blocks": {
            str(s): rows for s, rows in table.items()
        },
        "strict_prize_solution": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
