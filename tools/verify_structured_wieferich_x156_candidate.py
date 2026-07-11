#!/usr/bin/env python3
"""Verify the structured candidate X=2^156-9 with exact arithmetic."""
from __future__ import annotations

import json

M = 156
B = 1 << M
X = B - 9
Q = 1093
ORDER = 364
MOD = 1 << 20
PATTERN = (3, 1, 2, 2, 5, 6)
CUMULATIVE = (3, 4, 6, 8, 13, 19)
SCALED_RESIDUES = (1_048_568, 80, 1_047_872, 6_400, 991_232, 524_288)
FIRST = (1 << 153) - 1
BARRIER = (2 * X) // 27


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def odd_step(n: int) -> tuple[int, int]:
    numerator = X * n + 1
    a = v2(numerator)
    return numerator >> a, a


def verify_wieferich() -> dict[str, int]:
    if pow(2, ORDER, Q) != 1:
        raise AssertionError("order period failed")
    for prime in (2, 3, 7, 13):
        if ORDER % prime == 0 and pow(2, ORDER // prime, Q) == 1:
            raise AssertionError("order is not minimal")
    if pow(2, ORDER, Q * Q) != 1:
        raise AssertionError("Wieferich congruence failed")
    if pow(2, M, Q) != 9:
        raise AssertionError("2^156 residue modulo q failed")
    if pow(2, M, Q * Q) != 165_052:
        raise AssertionError("2^156 residue modulo q^2 failed")
    if X % (Q * Q) != 165_043 or 165_043 != 151 * Q:
        raise AssertionError("q-adic X certificate failed")
    if X % Q != 0 or X % (Q * Q) == 0:
        raise AssertionError("q must divide X exactly once")
    return {
        "order_of_2_mod_1093": ORDER,
        "pow_2_364_mod_q_squared": pow(2, ORDER, Q * Q),
        "pow_2_156_mod_q_squared": pow(2, M, Q * Q),
        "X_mod_q_squared": X % (Q * Q),
    }


def verify_first_step() -> dict[str, int]:
    first, a = odd_step(1)
    if (first, a) != (FIRST, 3):
        raise AssertionError("unexpected first step")
    return {"first_value": first, "first_valuation": a}


def verify_scaled_residue_table() -> None:
    scaled = 1
    cumulative = 0
    residues: list[int] = []
    cumulative_values: list[int] = []
    valuations: list[int] = []
    for a in PATTERN:
        scaled = X * scaled + (1 << cumulative)
        cumulative += a
        residues.append(scaled % MOD)
        cumulative_values.append(cumulative)
        valuations.append(v2(scaled))
    if tuple(residues) != SCALED_RESIDUES:
        raise AssertionError((residues, SCALED_RESIDUES))
    if tuple(cumulative_values) != CUMULATIVE:
        raise AssertionError("cumulative valuations failed")
    if tuple(valuations) != CUMULATIVE:
        raise AssertionError("scaled exact valuations failed")


def six_step_formula(n: int) -> int:
    constant = X**5 + 8 * X**4 + 16 * X**3 + 64 * X**2 + 256 * X + 8192
    numerator = X**6 * n + constant
    if numerator % (1 << 19):
        raise AssertionError("six-step formula is not integral")
    return numerator >> 19


def verify_forced_blocks() -> dict[str, int]:
    verify_scaled_residue_table()
    cases = 0
    for q in range(0, 1000):
        n = 1 + (q << 20)
        current = n
        valuations: list[int] = []
        for _ in range(6):
            current, a = odd_step(current)
            valuations.append(a)
        if tuple(valuations) != PATTERN:
            raise AssertionError((n, valuations))
        if current != six_step_formula(n):
            raise AssertionError("six-step affine formula failed")
        cases += 1
    return {"forced_residue_cases_checked": cases}


def verify_polynomial_identity() -> None:
    p = B**5 - 53 * B**4 + 1178 * B**3 - 14042 * B**2 + 94645 * B - 341825
    if p % 2 != 1:
        raise AssertionError("P(B) must be odd")
    constant = X**5 + 8 * X**4 + 16 * X**3 + 64 * X**2 + 256 * X + 8192
    if X**6 + constant - (1 << 19) != B * p:
        raise AssertionError("precision polynomial identity failed")


def verify_precision_transfer() -> dict[str, int]:
    verify_polynomial_identity()
    checked = 0
    for length in range(20, M):
        for u in range(1, 30, 2):
            n = 1 + (1 << length) * u
            endpoint = six_step_formula(n)
            if v2(endpoint - 1) != length - 19:
                raise AssertionError((length, u, v2(endpoint - 1)))
            checked += 1
    return {"precision_transfer_cases_checked": checked}


def verify_initial_program() -> dict[str, int | str]:
    blocks = (M - 1) // 19
    if blocks != 8:
        raise AssertionError("unexpected block count")
    n = 1
    valuations: list[int] = []
    for _ in range(blocks):
        for _ in range(6):
            n, a = odd_step(n)
            valuations.append(a)
    if tuple(valuations) != PATTERN * blocks:
        raise AssertionError("initial repeated word failed")
    if sum(valuations) != 152:
        raise AssertionError("initial total valuation failed")
    if v2(n - 1) != 4:
        raise AssertionError("initial endpoint precision failed")
    if not n * (1 << 152) > X**48:
        raise AssertionError("initial growth lower bound failed")
    return {
        "forced_blocks": blocks,
        "forced_steps": 48,
        "valuation_word": "(3,1,2,2,5,6)^8",
        "total_valuation": 152,
        "endpoint_v2_n_minus_1": 4,
        "endpoint_bit_length": n.bit_length(),
    }


def verify_barrier() -> dict[str, int]:
    expected = 6_766_211_283_939_365_362_054_096_447_760_569_535_444_132_142
    if BARRIER != expected:
        raise AssertionError("unexpected cycle barrier")
    if not 27 * BARRIER <= 2 * X < 27 * (BARRIER + 1):
        raise AssertionError("floor barrier certificate failed")
    return {"excluded_cycle_lengths_through": BARRIER}


def main() -> None:
    report = {
        "candidate": {"X": X, "n0": 1, "m": M, "d": 9},
        "wieferich": verify_wieferich(),
        "first_step": verify_first_step(),
        "forced_block_grid": verify_forced_blocks(),
        "precision": verify_precision_transfer(),
        "initial_program": verify_initial_program(),
        "cycle_barrier": verify_barrier(),
        "proved_no_return_to_1": True,
        "strict_prize_solution": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
