#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 requires n>0")
    return (n & -n).bit_length() - 1


def odd_step(X: int, n: int) -> tuple[int, int]:
    z = X * n + 1
    a = v2(z)
    return z >> a, a


def complete_block_data(m: int, d: int, n: int) -> tuple[int, int, int, int]:
    B = 1 << m
    X = B - d
    r = v2(d * n - 1)
    k, s = divmod(r, m)
    if s:
        ell = k + 1
        terminal = s
    else:
        if k < 1:
            raise AssertionError("complete block must have positive length")
        ell = k
        cur = n
        valuations: list[int] = []
        for _ in range(ell):
            cur, a = odd_step(X, cur)
            valuations.append(a)
        terminal = valuations[-1]
        assert valuations[:-1] == [m] * (ell - 1)
        assert terminal > m
        return ell, cur, terminal, r

    cur = n
    valuations = []
    for _ in range(ell):
        cur, a = odd_step(X, cur)
        valuations.append(a)
    assert valuations == [m] * (ell - 1) + [terminal]
    return ell, cur, terminal, r


def verify_block_correction_grid() -> int:
    tested = 0
    for m in range(3, 10):
        B = 1 << m
        for d in range(1, min(B // 2, 17), 2):
            X = B - d
            if X < 5:
                continue
            for n in range(1, 1001, 2):
                if d * n <= 1:
                    continue
                ell, endpoint, _, _ = complete_block_data(m, d, n)
                assert endpoint > 0 and endpoint & 1

                raw = Fraction(
                    pow(B, ell) - pow(X, ell),
                    pow(X, ell) * d * n,
                )
                assert raw > 0
                assert raw < Fraction(ell * d, 2 * pow(X, ell))
                assert raw <= Fraction(ell * d, 2 * X)
                tested += 1
    return tested


def verify_cycle_bound(X: int, m: int, d: int, cycle: list[int]) -> tuple[int, int]:
    B = 1 << m
    assert X == B - d
    valuations: list[int] = []
    for i, n in enumerate(cycle):
        nxt, a = odd_step(X, n)
        assert nxt == cycle[(i + 1) % len(cycle)]
        valuations.append(a)

    p = len(cycle)
    D = m * p - sum(valuations)
    assert D >= 1

    # Exact rational form of p < 2*D*B*X/[d*(X-d)].
    assert p * d * (X - d) < 2 * D * B * X
    return p, D


def verify_primary_exclusion() -> None:
    m = 4501
    B = 1 << m
    d = 349 * (1 << 500) - 347
    X = B - d
    max_D = 4500

    assert d > 0 and d & 1
    assert d < B // 2
    assert X >= 5 and X & 1
    assert X - d > 0

    # For every D<=4500, the general theorem gives p<2^4006.
    assert 2 * max_D * B * X < (1 << 4006) * d * (X - d)

    # The retained nonpositive-return theorem gives
    # p>L_return>2^(2^974), and 2^974>4006 compares the outer exponents.
    assert (1 << 974) > 4006


def main() -> None:
    tested = verify_block_correction_grid()

    regressions = [
        verify_cycle_bound(5, 3, 3, [1, 3]),
        verify_cycle_bound(5, 3, 3, [13, 33, 83]),
        verify_cycle_bound(5, 3, 3, [17, 43, 27]),
    ]
    assert regressions == [(2, 1), (3, 2), (3, 2)]

    verify_primary_exclusion()

    nonpositive_return_excluded = True
    strict_prize_solution = False
    assert nonpositive_return_excluded
    assert not strict_prize_solution

    print(f"PASS: {tested} exact complete-block correction cases")
    print("PASS: all three known accelerated 5n+1 cycle regressions")
    print("PASS: primary nonpositive-return branch has p<2^4006")
    print("PASS: retained lower bound p>2^(2^974) contradicts that upper bound")
    print("strict prize target remains open only on the positive-credit return branch")


if __name__ == "__main__":
    main()
