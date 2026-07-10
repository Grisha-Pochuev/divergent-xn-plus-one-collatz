#!/usr/bin/env python3
"""Analyze a periodically repeated exact valuation block.

The script computes the block affine map, its rational 2-adic center,
and the rigorous upper bound on how often a positive integer can repeat
that exact block before the pattern must break (unless it is a cycle).
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction

from xn1 import odd_step, v2


def parse_pattern(text: str) -> tuple[int, ...]:
    try:
        pattern = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    except ValueError as exc:
        raise argparse.ArgumentTypeError("pattern must be comma-separated positive integers") from exc
    if not pattern or any(a < 1 for a in pattern):
        raise argparse.ArgumentTypeError("pattern must contain positive integers")
    return pattern


def block_constants(x: int, pattern: tuple[int, ...]) -> tuple[int, int, int]:
    """Return (A, B, D) for F(n)=(X^p*n+B)/2^A and D=X^p-2^A."""
    if x < 5 or x % 2 == 0:
        raise ValueError("X must be odd and at least 5")
    if not pattern or any(a < 1 for a in pattern):
        raise ValueError("pattern must be nonempty and positive")

    p = len(pattern)
    cumulative = 0
    b = 0
    for j, a in enumerate(pattern):
        b += (x ** (p - 1 - j)) * (1 << cumulative)
        cumulative += a
    total = cumulative
    d = x**p - (1 << total)
    return total, b, d


def repetition_bound(x: int, n: int, pattern: tuple[int, ...]) -> int | None:
    """Return the rigorous repetition upper bound, or None at the block fixed point."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    total, b, d = block_constants(x, pattern)
    witness = d * n + b
    if witness == 0:
        return None
    return max(-1, (v2(abs(witness)) - 1) // total)


def actual_repetitions(x: int, n: int, pattern: tuple[int, ...], limit: int) -> int:
    """Count exact consecutive repetitions, stopping at `limit`."""
    count = 0
    for _ in range(limit):
        current = n
        observed: list[int] = []
        for _expected in pattern:
            current, a = odd_step(x, current)
            observed.append(a)
        if tuple(observed) != pattern:
            break
        count += 1
        n = current
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--X", type=int, required=True)
    parser.add_argument("--pattern", type=parse_pattern, required=True,
                        help="comma-separated exact v2 values, for example 1,1,5")
    parser.add_argument("--n", type=int,
                        help="optional positive odd start for a repetition check")
    parser.add_argument("--limit", type=int, default=1000,
                        help="maximum repetitions to simulate when --n is supplied")
    args = parser.parse_args()

    pattern = args.pattern
    total, b, d = block_constants(args.X, pattern)
    p = len(pattern)
    fixed = Fraction(-b, d)

    report: dict[str, object] = {
        "X": args.X,
        "pattern": list(pattern),
        "block_length": p,
        "total_v2": total,
        "B": b,
        "D": d,
        "fixed_point_numerator": fixed.numerator,
        "fixed_point_denominator": fixed.denominator,
        "log2_block_multiplier": p * math.log2(args.X) - total,
        "expanding_block": d > 0,
        "conclusion": (
            "an infinite exact repetition is a cycle; in the expanding case "
            "its rational fixed point is negative"
        ),
    }

    if args.n is not None:
        bound = repetition_bound(args.X, args.n, pattern)
        actual = actual_repetitions(args.X, args.n, pattern, args.limit)
        report.update({
            "n": args.n,
            "rigorous_repetition_bound": bound,
            "actual_repetitions_up_to_limit": actual,
            "simulation_limit": args.limit,
            "is_block_fixed_point": bound is None,
        })
        if bound is not None and actual > bound:
            raise AssertionError("observed repetitions exceed the proved bound")

    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
