#!/usr/bin/env python3
"""Check signed digit descent for X=2^m+1."""
from __future__ import annotations

import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def signed_step(X: int, n: int, epsilon: int) -> tuple[int, int]:
    numerator = X * n + epsilon
    if numerator <= 0:
        raise ValueError("signed numerator must be positive")
    valuation = v2(numerator)
    return numerator >> valuation, valuation


def alternating_sum(B: int, k: int) -> int:
    total = 0
    power = 1
    sign = 1
    for _ in range(k):
        total += sign * power
        power *= B
        sign = -sign
    return total


def full_blocks(B: int, X: int, n: int, epsilon: int) -> tuple[int, int, int]:
    """Return (blocks, residual_integer, residual_sign)."""
    blocks = 0
    current = n
    sign = epsilon
    while current % B == (-sign) % B:
        numerator = current + sign
        if numerator % B:
            raise AssertionError("descent divisibility failed")
        current = numerator // B
        sign = -sign
        blocks += 1
    return blocks, current, sign


def verify_one(m: int, n: int, epsilon: int) -> int:
    B = 1 << m
    X = B + 1
    if epsilon not in (-1, 1):
        raise ValueError("epsilon must be +/-1")
    if X * n + epsilon <= 0:
        return 0

    output, valuation = signed_step(X, n, epsilon)
    blocks, residual, residual_sign = full_blocks(B, X, n, epsilon)
    residual_output, residual_valuation = signed_step(
        X, residual, residual_sign
    )

    if valuation != blocks * m + residual_valuation:
        raise AssertionError("iterated valuation identity failed")
    if output != residual_output:
        raise AssertionError("iterated signed output identity failed")

    S = alternating_sum(B, blocks)
    modulus = B**blocks
    if blocks:
        if (n + epsilon * S) % modulus:
            raise AssertionError("alternating suffix congruence failed")
        reconstructed = (n + epsilon * S) // modulus
        if reconstructed != residual:
            raise AssertionError("alternating suffix reconstruction failed")

        # Maximality: the next signed residue must fail.
        if residual % B == (-residual_sign) % B:
            raise AssertionError("descent stopped too early")

    if valuation // m != blocks:
        raise AssertionError("full-block count does not equal floor valuation")
    return blocks


def verify_examples() -> dict[str, object]:
    if signed_step(9, 7, 1) != (1, 6):
        raise AssertionError("wrong X=9 n=7 example")
    if signed_step(9, 23, 1) != (13, 4):
        raise AssertionError("wrong X=9 n=23 example")

    residues = {}
    for k in range(1, 5):
        B = 8
        residue = (-alternating_sum(B, k)) % (B**k)
        residues[str(k)] = residue
    expected = {"1": 7, "2": 7, "3": 455, "4": 455}
    if residues != expected:
        raise AssertionError("wrong X=9 signed suffix residues")
    return {
        "n7": {"output": 1, "valuation": 6},
        "n23": {"output": 13, "valuation": 4},
        "plus_suffix_residues": residues,
    }


def verify_grid() -> dict[str, int]:
    checked = 0
    maximum_blocks = 0
    for m in range(2, 10):
        for n in range(0, 20000):
            for epsilon in (-1, 1):
                if ((1 << m) + 1) * n + epsilon <= 0:
                    continue
                blocks = verify_one(m, n, epsilon)
                maximum_blocks = max(maximum_blocks, blocks)
                checked += 1
    return {
        "checked_signed_states": checked,
        "maximum_full_blocks_seen": maximum_blocks,
    }


def main() -> None:
    print(json.dumps({
        "theorem": "Fermat signed digit descent",
        "examples": verify_examples(),
        "finite_regression_grid": verify_grid(),
        "is_divergence_proof": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
