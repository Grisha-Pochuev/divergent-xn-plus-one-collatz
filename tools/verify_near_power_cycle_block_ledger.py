#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def odd_step(X: int, n: int) -> tuple[int, int]:
    y = X * n + 1
    a = v2(y)
    return y >> a, a


def pow2_fraction(c: int) -> Fraction:
    if c >= 0:
        return Fraction(1 << c, 1)
    return Fraction(1, 1 << (-c))


def complete_block(
    X: int,
    m: int,
    d: int,
    n: int,
) -> tuple[int, list[int]]:
    r = v2(d * n - 1)
    k, s = divmod(r, m)
    length = k + (1 if s else 0)
    assert length >= 1

    cur = n
    valuations: list[int] = []
    for _ in range(length):
        cur, a = odd_step(X, cur)
        valuations.append(a)
    return cur, valuations


def verify_block(X: int, m: int, d: int, n: int) -> None:
    B = 1 << m
    r = v2(d * n - 1)
    u = (d * n - 1) >> r
    k, s = divmod(r, m)
    endpoint, valuations = complete_block(X, m, d, n)

    if s:
        ell = k + 1
        e = m - s
        assert valuations == [m] * k + [s]
        expected = (pow(X, ell) * u + (1 << e)) // d
        terminal_credit = e
    else:
        ell = k
        assert k >= 1
        b = v2(pow(X, k) * u + 1)
        assert valuations == [m] * (k - 1) + [m + b]
        expected = (pow(X, k) * u + 1) // (d * (1 << b))
        terminal_credit = -b
        assert endpoint * (1 << b) < n

    assert endpoint == expected

    correction = Fraction(1, 1) + Fraction(
        pow(B, ell) - pow(X, ell),
        pow(X, ell) * d * n,
    )
    ratio = (
        pow2_fraction(terminal_credit)
        * Fraction(pow(X, ell), pow(B, ell))
        * correction
    )
    assert ratio == Fraction(endpoint, n)

    raw_correction = Fraction(
        pow(B, ell) - pow(X, ell),
        pow(X, ell) * d * n,
    )
    assert raw_correction > 0
    assert raw_correction < Fraction(ell * d, 2 * pow(X, ell))


def partition_cycle(
    X: int,
    m: int,
    cycle: list[int],
) -> tuple[list[int], list[tuple[int, int, int]]]:
    p = len(cycle)
    valuations: list[int] = []
    for i, n in enumerate(cycle):
        nxt, a = odd_step(X, n)
        assert nxt == cycle[(i + 1) % p]
        valuations.append(a)

    assert any(a != m for a in valuations)
    first_end = next(i for i, a in enumerate(valuations) if a != m)
    start = (first_end + 1) % p

    blocks: list[tuple[int, int, int]] = []
    index = start
    covered = 0
    while covered < p:
        source = cycle[index]
        ell = 0
        while True:
            terminal = valuations[(index + ell) % p]
            ell += 1
            if terminal != m:
                break
        blocks.append((source, ell, m - terminal))
        index = (index + ell) % p
        covered += ell

    assert covered == p
    assert index == start
    return valuations, blocks


def verify_cycle(X: int, m: int, d: int, cycle: list[int]) -> None:
    B = 1 << m
    valuations, blocks = partition_cycle(X, m, cycle)
    p = len(cycle)
    A = sum(valuations)
    D = m * p - A

    assert D >= 1
    assert sum(ell for _, ell, _ in blocks) == p
    assert sum(c for _, _, c in blocks) == D

    correction_product = Fraction(1, 1)
    ratio_product = Fraction(1, 1)
    for source, ell, credit in blocks:
        correction = Fraction(1, 1) + Fraction(
            pow(B, ell) - pow(X, ell),
            pow(X, ell) * d * source,
        )
        correction_product *= correction
        ratio_product *= (
            pow2_fraction(credit)
            * Fraction(pow(X, ell), pow(B, ell))
            * correction
        )

    assert ratio_product == 1
    assert correction_product == Fraction(
        pow(B, p),
        (1 << D) * pow(X, p),
    )


def find_odd_u(B_power: int, scale: int, d: int) -> int:
    for u in range(1, 10_000, 2):
        if (B_power * scale * u + 1) % d == 0:
            return u
    raise AssertionError("no odd core found")


def main() -> None:
    # Regression cycles for X=5=2^3-3, including a neutral complete block.
    verify_cycle(5, 3, 3, [1, 3])
    verify_cycle(5, 3, 3, [13, 33, 83])
    verify_cycle(5, 3, 3, [17, 43, 27])

    # Finite exact grids for general near-power maps.
    for m in range(3, 9):
        B = 1 << m
        for d in range(1, min(B - 5, 13) + 1, 2):
            X = B - d
            if X < 5:
                continue
            for n in range(1, 301, 2):
                if d * n > 1:
                    verify_block(X, m, d, n)

    # Structured X=2^156-9 examples: low, long nonexceptional, exceptional.
    m = 156
    B = 1 << m
    d = 9
    X = B - d
    verify_block(X, m, d, 1)

    s = 4
    u = find_odd_u(B, 1 << s, d)
    n = (B * (1 << s) * u + 1) // d
    verify_block(X, m, d, n)

    u = find_odd_u(B, 1, d)
    n = (B * u + 1) // d
    verify_block(X, m, d, n)
    assert u == 17
    assert n == (17 * B + 1) // 9

    print("verified complete-block ratio and cycle ledger identities")
    print("known 5n+1 cycles: 3")
    print("general finite block grid: passed")
    print(f"least X156 exceptional source: {n}")


if __name__ == "__main__":
    main()
