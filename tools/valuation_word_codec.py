#!/usr/bin/env python3
"""Encode and verify finite exact valuation words for accelerated Xn+1."""
from __future__ import annotations

import argparse
import json
import math

from xn1 import odd_step


def parse_pattern(text: str) -> tuple[int, ...]:
    pattern = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    if not pattern or any(a < 1 for a in pattern):
        raise argparse.ArgumentTypeError("pattern must contain positive integers")
    return pattern


def word_constants(x: int, pattern: tuple[int, ...]) -> tuple[int, int]:
    if x < 5 or x % 2 == 0:
        raise ValueError("X must be odd and at least 5")
    if not pattern or any(a < 1 for a in pattern):
        raise ValueError("pattern must be nonempty and positive")
    nsteps = len(pattern)
    cumulative = 0
    b = 0
    for j, a in enumerate(pattern):
        b += x ** (nsteps - 1 - j) * (1 << cumulative)
        cumulative += a
    return cumulative, b


def coding_residue(x: int, pattern: tuple[int, ...]) -> tuple[int, int]:
    """Return (least residue, modulus) coding the exact valuation word."""
    total, b = word_constants(x, pattern)
    modulus = 1 << (total + 1)
    inverse = pow(x, -len(pattern), modulus)
    residue = (((1 << total) - b) * inverse) % modulus
    return residue, modulus


def observed_word(x: int, n: int, length: int) -> tuple[tuple[int, ...], int]:
    values: list[int] = []
    for _ in range(length):
        n, a = odd_step(x, n)
        values.append(a)
    return tuple(values), n


def verify_representatives(x: int, pattern: tuple[int, ...], count: int) -> list[dict[str, int]]:
    residue, modulus = coding_residue(x, pattern)
    rows: list[dict[str, int]] = []
    q = 0
    while len(rows) < count:
        n = residue + q * modulus
        q += 1
        if n <= 0:
            continue
        observed, endpoint = observed_word(x, n, len(pattern))
        if observed != pattern:
            raise AssertionError(f"coding failure at n={n}: {observed} != {pattern}")
        rows.append({"start": n, "endpoint": endpoint, "grew": int(endpoint > n)})
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--X", type=int, required=True)
    parser.add_argument("--pattern", type=parse_pattern, required=True)
    parser.add_argument("--representatives", type=int, default=3)
    args = parser.parse_args()

    total, b = word_constants(args.X, args.pattern)
    residue, modulus = coding_residue(args.X, args.pattern)
    nsteps = len(args.pattern)
    d = args.X**nsteps - (1 << total)
    rows = verify_representatives(args.X, args.pattern, args.representatives)
    report = {
        "X": args.X,
        "pattern": list(args.pattern),
        "length": nsteps,
        "total_v2": total,
        "average_v2": total / nsteps,
        "log2_X": math.log2(args.X),
        "B": b,
        "D": d,
        "positive_drift": d > 0,
        "coding_residue": residue,
        "coding_modulus": modulus,
        "sample_representatives": rows,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
