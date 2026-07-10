#!/usr/bin/env python3
"""Construct and verify arbitrary finite complete macroblock programs.

For X=2^m+1, a boundary state has the form

    n_i = 2^(m*L_i) * q_i - 1,

with q_i positive and odd.  Given boundary lengths L_i and prescribed final
excess valuations r_i, this script solves the exact backward congruence,
constructs all q_i, and verifies the resulting orbit with integer arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass

from xn1 import odd_step


@dataclass(frozen=True)
class Program:
    m: int
    lengths: tuple[int, ...]
    exits: tuple[int, ...]

    @property
    def x(self) -> int:
        return (1 << self.m) + 1


def parse_positive_list(text: str) -> tuple[int, ...]:
    try:
        values = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected comma-separated positive integers") from exc
    if not values or any(value < 1 for value in values):
        raise argparse.ArgumentTypeError("all entries must be positive integers")
    return values


def terminal_congruence(program: Program) -> tuple[int, int]:
    """Return (residue, modulus) for the terminal q_R.

    The residue is the unique class modulo X^(L_0+...+L_(R-1)) that makes
    every backward q_i integral.
    """
    x = program.x
    p = 1
    q_const = 0
    exponent_sum = 0

    for i in range(len(program.exits) - 1, -1, -1):
        a = 1 << (program.exits[i] + program.m * program.lengths[i + 1])
        b = 1 - (1 << program.exits[i])
        p = a * p
        q_const = a * q_const + b * (x**exponent_sum)
        exponent_sum += program.lengths[i]

    modulus = x**exponent_sum
    residue = (-q_const * pow(p, -1, modulus)) % modulus
    return residue, modulus


def least_positive_odd_representative(residue: int, modulus: int) -> int:
    value = residue if residue > 0 else modulus
    if value % 2 == 0:
        value += modulus
    return value


def build_q_values(program: Program, lift: int = 0) -> tuple[int, ...]:
    if program.m < 2:
        raise ValueError("m must be at least 2")
    if len(program.lengths) != len(program.exits) + 1:
        raise ValueError("need exactly one more length than exits")
    if lift < 0:
        raise ValueError("lift must be nonnegative")

    x = program.x
    residue, modulus = terminal_congruence(program)
    q_terminal = least_positive_odd_representative(residue, modulus)
    q_terminal += 2 * modulus * lift

    q_values = [0] * len(program.lengths)
    q_values[-1] = q_terminal

    for i in range(len(program.exits) - 1, -1, -1):
        numerator = (
            (1 << (program.exits[i] + program.m * program.lengths[i + 1]))
            * q_values[i + 1]
            - (1 << program.exits[i])
            + 1
        )
        denominator = x ** program.lengths[i]
        if numerator % denominator != 0:
            raise AssertionError("backward congruence failed")
        q_values[i] = numerator // denominator
        if q_values[i] <= 0 or q_values[i] % 2 == 0:
            raise AssertionError("constructed q_i is not positive odd")

    return tuple(q_values)


def boundary_value(m: int, length: int, q_value: int) -> int:
    return (1 << (m * length)) * q_value - 1


def verify_program(program: Program, q_values: tuple[int, ...]) -> dict[str, object]:
    x = program.x
    n = boundary_value(program.m, program.lengths[0], q_values[0])
    boundaries = [n]
    observed_words: list[list[int]] = []
    all_growing = True

    for i, exit_value in enumerate(program.exits):
        observed: list[int] = []
        start = n
        for _ in range(program.lengths[i]):
            n, valuation = odd_step(x, n)
            observed.append(valuation)

        expected_word = [program.m] * (program.lengths[i] - 1) + [program.m + exit_value]
        if observed != expected_word:
            raise AssertionError(
                f"block {i}: observed {observed}, expected {expected_word}"
            )

        expected_boundary = boundary_value(
            program.m, program.lengths[i + 1], q_values[i + 1]
        )
        if n != expected_boundary:
            raise AssertionError(f"block {i}: endpoint mismatch")

        observed_words.append(observed)
        boundaries.append(n)
        all_growing = all_growing and n > start

    delta = math.log2(1.0 + 2.0 ** (-program.m))
    sufficient_margins = [
        program.lengths[i] * delta - program.exits[i] - 1.0
        for i in range(len(program.exits))
    ]

    def digest(value: int) -> str:
        return hashlib.sha256(str(value).encode()).hexdigest()

    return {
        "m": program.m,
        "X": x,
        "lengths": list(program.lengths),
        "exits": list(program.exits),
        "blocks": len(program.exits),
        "q_bit_lengths": [value.bit_length() for value in q_values],
        "boundary_bit_lengths": [value.bit_length() for value in boundaries],
        "boundary_sha256_decimal": [digest(value) for value in boundaries],
        "all_boundaries_strictly_grow": all_growing,
        "sufficient_growth_margins": sufficient_margins,
        "all_sufficient_margins_positive": all(value > 0 for value in sufficient_margins),
        "first_q": q_values[0],
        "first_boundary": boundaries[0],
        "last_boundary": boundaries[-1],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--lengths", type=parse_positive_list, required=True)
    parser.add_argument("--exits", type=parse_positive_list, required=True)
    parser.add_argument(
        "--lift",
        type=int,
        default=0,
        help="add this many multiples of 2*modulus to the terminal q",
    )
    args = parser.parse_args()

    program = Program(args.m, args.lengths, args.exits)
    q_values = build_q_values(program, args.lift)
    report = verify_program(program, q_values)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
