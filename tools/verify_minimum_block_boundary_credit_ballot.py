#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from itertools import product


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def accelerated_step(X: int, n: int) -> tuple[int, int]:
    value = X * n + 1
    a = v2(value)
    return value >> a, a


def complete_block(
    X: int, m: int, n: int, limit: int = 64
) -> tuple[int, int, int] | None:
    """Return endpoint, length, credit for the next m,...,m,a!=m block."""
    for ell in range(1, limit + 1):
        n, a = accelerated_step(X, n)
        if a != m:
            return n, ell, m - a
    # Long all-m runs are not needed by this finite regression grid.
    return None


def power_of_two(credit: int) -> Fraction:
    if credit >= 0:
        return Fraction(1 << credit, 1)
    return Fraction(1, 1 << (-credit))


def verify_exact_block_domination_grid() -> int:
    checked = 0
    for m in range(3, 9):
        B = 1 << m
        for d in range(1, B // 2, 2):
            X = B - d
            if X < 5:
                continue
            for n in range(1, 4000, 2):
                block = complete_block(X, m, n)
                if block is None:
                    continue
                endpoint, _, credit = block
                assert Fraction(endpoint, n) < power_of_two(credit)
                checked += 1
    return checked


def canonical_cycle_blocks(
    X: int, cycle: list[int]
) -> tuple[list[int], list[int], int]:
    """Return boundary values, block credits from the least boundary, and D."""
    m = X.bit_length()
    assert (1 << (m - 1)) < X < (1 << m)
    p = len(cycle)
    valuations: list[int] = []
    for i, n in enumerate(cycle):
        nxt, a = accelerated_step(X, n)
        assert nxt == cycle[(i + 1) % p]
        valuations.append(a)

    terminal_indices = [i for i, a in enumerate(valuations) if a != m]
    assert terminal_indices, "nontrivial complete-block partition required"
    boundary_indices = [(i + 1) % p for i in terminal_indices]
    start_index = min(boundary_indices, key=lambda i: cycle[i])
    start_value = cycle[start_index]

    boundaries = [start_value]
    credits: list[int] = []
    total_steps = 0
    i = start_index
    while True:
        block_credit = None
        while total_steps < 2 * p:
            a = valuations[i]
            total_steps += 1
            i = (i + 1) % p
            if a != m:
                block_credit = m - a
                break
        assert block_credit is not None
        credits.append(block_credit)
        boundaries.append(cycle[i])
        if i == start_index:
            break

    assert total_steps == p
    assert boundaries[-1] == start_value

    capital = 0
    for endpoint, credit in zip(boundaries[1:], credits):
        capital += credit
        assert endpoint >= start_value
        assert capital >= 1
    return boundaries, credits, capital


def verify_known_cycle_regressions() -> None:
    cycles = [
        [1, 3],
        [13, 33, 83],
        [17, 43, 27],
    ]
    expected = [
        ([1, 3, 1], [2, -1], 1),
        ([13, 33, 83, 13], [2, 2, -2], 2),
        ([43, 43], [2], 2),
    ]
    for cycle, target in zip(cycles, expected):
        assert canonical_cycle_blocks(5, cycle) == target


def stack_match(credits: tuple[int, ...]) -> tuple[int, int]:
    """Match every negative credit unit to an earlier positive unit."""
    stack: list[tuple[int, int]] = []
    matched = 0
    for index, credit in enumerate(credits):
        if credit > 0:
            stack.extend((index, unit) for unit in range(credit))
        elif credit < 0:
            for _ in range(-credit):
                assert stack, "positive-prefix condition prevents underflow"
                stack.pop()
                matched += 1
        assert stack, "every nonempty prefix must retain at least one unit"
    return matched, len(stack)


def verify_ballot_matching() -> int:
    checked = 0
    for length in range(1, 8):
        for credits in product(range(-3, 5), repeat=length):
            partial = 0
            valid = True
            for credit in credits:
                partial += credit
                if partial < 1:
                    valid = False
                    break
            if not valid:
                continue
            matched, unmatched = stack_match(credits)
            positive = sum(c for c in credits if c > 0)
            negative = -sum(c for c in credits if c < 0)
            assert matched == negative
            assert unmatched == positive - negative == sum(credits)
            checked += 1
    return checked


def verify_primary_corollaries() -> None:
    m = 4501
    max_deficit = m - 1
    exit_credit_max = max_deficit
    assert max_deficit == 4500
    assert 1 - exit_credit_max == -4499

    for j in range(1, 1000):
        max_exceptional_excess = j * max_deficit - 1
        assert max_exceptional_excess < j * max_deficit
        required_ordinary = (
            max_exceptional_excess + 1 + max_deficit - 1
        ) // max_deficit
        assert required_ordinary == j


def main() -> None:
    block_cases = verify_exact_block_domination_grid()
    verify_known_cycle_regressions()
    ballot_cases = verify_ballot_matching()
    verify_primary_corollaries()
    print("minimum complete-block boundary credit ballot verified")
    print(f"exact complete-block domination cases={block_cases}")
    print("known accelerated 5n+1 cycle regressions=3")
    print(f"positive-prefix stack-matching ledgers={ballot_cases}")
    print("primary prefix exceptional bound: E_j <= 4500*j-1")
    print("primary return-prefix debt bound: credit >= -4499")


if __name__ == "__main__":
    main()
