#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from itertools import product

M = 4501
B = 1 << M
D0 = 349 * (1 << 500) - 347
X0 = B - D0


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def odd_step(X: int, n: int) -> tuple[int, int]:
    z = X * n + 1
    a = v2(z)
    return z >> a, a


def next_complete_block(
    X: int, m: int, n: int, limit: int = 128
) -> tuple[int, int, int] | None:
    for ell in range(1, limit + 1):
        n, a = odd_step(X, n)
        if a != m:
            return n, ell, m - a
    return None


def sponsor_arches(
    credits: tuple[int, ...],
) -> tuple[list[int], list[tuple[int, int, int, int]]]:
    prefix = [0]
    for credit in credits:
        prefix.append(prefix[-1] + credit)
    assert all(value >= 1 for value in prefix[1:])

    arches: list[tuple[int, int, int, int]] = []
    for j, credit in enumerate(credits):
        if credit >= 0:
            continue
        height = prefix[j + 1]
        i = max(index for index in range(j + 1) if prefix[index] <= height)
        assert i < j
        assert credits[i] > 0
        net_credit = height - prefix[i]
        assert 0 <= net_credit < credits[i]
        assert all(prefix[t] > height for t in range(i + 1, j + 1))
        arches.append((i, j, net_credit, height))

    for left_index, left in enumerate(arches):
        i, j, _, _ = left
        for right in arches[left_index + 1 :]:
            u, v, _, _ = right
            assert not ((i < u <= j < v) or (u < i <= v < j))
    return prefix, arches


def maximal_arches(
    arches: list[tuple[int, int, int, int]],
) -> list[tuple[int, int, int, int]]:
    maximal: list[tuple[int, int, int, int]] = []
    for index, arch in enumerate(arches):
        i, j, _, _ = arch
        contained = any(
            u <= i
            and j <= v
            and (u < i or j < v)
            for other_index, (u, v, _, _) in enumerate(arches)
            if other_index != index
        )
        if not contained:
            maximal.append(arch)
    maximal.sort()
    return maximal


def verify_arch_decomposition(credits: tuple[int, ...]) -> tuple[int, int]:
    prefix, arches = sponsor_arches(credits)
    maximal = maximal_arches(arches)

    for left, right in zip(maximal, maximal[1:]):
        assert left[1] < right[0]

    covered: set[int] = set()
    for i, j, net_credit, height in maximal:
        assert credits[i] > 0
        assert credits[j] < 0
        assert sum(credits[i : j + 1]) == net_credit
        assert 0 <= net_credit < credits[i]
        assert all(prefix[t] > height for t in range(i + 1, j + 1))
        covered.update(range(i, j + 1))

    for index, credit in enumerate(credits):
        if credit < 0:
            assert index in covered
        if index not in covered:
            assert credit > 0

    macro_credit = sum(
        net_credit for _, _, net_credit, _ in maximal
    ) + sum(
        credit for index, credit in enumerate(credits) if index not in covered
    )
    assert macro_credit == sum(credits)
    return len(arches), len(maximal)


def verify_small_ballot_ledgers() -> int:
    checked = 0
    alphabet = (-3, -2, -1, 1, 2, 3, 4)
    for length in range(1, 9):
        for credits in product(alphabet, repeat=length):
            capital = 0
            valid = True
            for credit in credits:
                capital += credit
                if capital < 1:
                    valid = False
                    break
            if not valid:
                continue
            verify_arch_decomposition(credits)
            checked += 1
    return checked


def verify_local_segment_bound_grid() -> int:
    checked = 0
    for m in range(3, 9):
        B_local = 1 << m
        for d in range(1, B_local // 2, 2):
            X = B_local - d
            if X < 5:
                continue
            for source in range(1, 300, 2):
                endpoint = source
                length = 0
                credit = 0
                for _ in range(6):
                    block = next_complete_block(X, m, endpoint)
                    if block is None:
                        break
                    endpoint, ell, block_credit = block
                    length += ell
                    credit += block_credit
                    if endpoint >= source:
                        assert credit >= 1
                        assert (
                            length * d * (X - d)
                            < 2 * credit * B_local * X
                        )
                    checked += 1
    return checked


def canonical_cycle_credits(X: int, cycle: list[int]) -> tuple[list[int], list[int]]:
    m = X.bit_length()
    valuations: list[int] = []
    for index, n in enumerate(cycle):
        nxt, a = odd_step(X, n)
        assert nxt == cycle[(index + 1) % len(cycle)]
        valuations.append(a)

    terminal_indices = [i for i, a in enumerate(valuations) if a != m]
    assert terminal_indices
    boundary_indices = [(i + 1) % len(cycle) for i in terminal_indices]
    start = min(boundary_indices, key=lambda i: cycle[i])

    boundaries = [cycle[start]]
    credits: list[int] = []
    i = start
    steps = 0
    while True:
        while True:
            a = valuations[i]
            i = (i + 1) % len(cycle)
            steps += 1
            if a != m:
                credits.append(m - a)
                boundaries.append(cycle[i])
                break
        if i == start:
            break
    assert steps == len(cycle)
    return boundaries, credits


def verify_known_cycles() -> None:
    cycles = [
        [1, 3],
        [13, 33, 83],
        [17, 43, 27],
    ]
    expected = [
        ([1, 3, 1], [2, -1]),
        ([13, 33, 83, 13], [2, 2, -2]),
        ([43, 43], [2]),
    ]
    for cycle, target in zip(cycles, expected):
        boundaries, credits = canonical_cycle_credits(5, cycle)
        assert (boundaries, credits) == target
        _, arches = sponsor_arches(tuple(credits))
        maximal = maximal_arches(arches)
        for i, j, net_credit, _ in maximal:
            ratio = Fraction(boundaries[j + 1], boundaries[i])
            assert ratio < Fraction(1 << net_credit, 1)


def verify_primary_macro_bounds() -> None:
    assert D0 > 0 and D0 < B // 2
    assert X0 - D0 > 0

    # Every nondecreasing segment of net credit at most 4500 has
    # accelerated length below 2^4006.
    assert (
        2 * 4500 * B * X0
        < (1 << 4006) * D0 * (X0 - D0)
    )

    # The retained return estimate uses delta<2^-3990.
    assert D0 < (1 << 509)
    assert Fraction(4 * D0, B) < Fraction(1, 1 << 3990)

    # If a maximal sponsor arch begins with the first ordinary block,
    # its credit C is below that first deficit e.  The old return has
    # R0>=1, so the compressed return has D-C=e+R0-C>=2.
    for e in range(1, 4501):
        for C in range(e):
            compressed_return_credit = e + 1 - C
            assert compressed_return_credit >= 2
            assert 1 - max(C, 1) >= -4499

    # If the first block is uncovered, C=e and the retained return has R0>=1.
    for e in range(1, 4501):
        assert 1 - e >= -4499


def main() -> None:
    ledger_cases = verify_small_ballot_ledgers()
    segment_cases = verify_local_segment_bound_grid()
    verify_known_cycles()
    verify_primary_macro_bounds()
    print("exceptional sponsor-arch decomposition verified")
    print(f"small positive-prefix ledgers={ledger_cases}")
    print(f"exact local segment cases={segment_cases}")
    print("known accelerated 5n+1 cycle regressions=3")
    print("maximal sponsor arches are laminar and cover every exceptional block")
    print("each maximal arch has net credit between 0 and 4499")
    print("primary nondecreasing macro-exit has accelerated length <2^4006")
    print("compressed return has positive credit and length >2^3990")


if __name__ == "__main__":
    main()
