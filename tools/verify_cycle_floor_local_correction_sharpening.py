#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

M_EXP = 4501
B = 1 << M_EXP
D0 = 349 * (1 << 500) - 347
X = B - D0
N = (1 << 500) - 1


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects a positive integer")
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


def complete_blocks(X0: int, B0: int, cycle: list[int]) -> list[tuple[int, int, int]]:
    m0 = B0.bit_length() - 1
    assert B0 == 1 << m0
    valuations = [v2(X0 * n + 1) for n in cycle]
    terminal = next(i for i, a in enumerate(valuations) if a != m0)
    index = (terminal + 1) % len(cycle)
    current: list[int] = []
    blocks: list[tuple[int, int, int]] = []
    for _ in range(len(cycle)):
        current.append(index)
        if valuations[index] != m0:
            source = cycle[current[0]]
            endpoint = cycle[(index + 1) % len(cycle)]
            blocks.append((source, endpoint, len(current)))
            current = []
        index = (index + 1) % len(cycle)
    assert not current
    return blocks


def verify_ln2_upper_bound() -> None:
    # exp(7/10) > 1 + 7/10 + (7/10)^2/2 + (7/10)^3/6 > 2.
    # Therefore ln(2) < 7/10, with no floating-point arithmetic.
    denominators = [1, 1, 2, 6]
    partial_exp = sum(
        Fraction(7, 10) ** k / denominators[k] for k in range(4)
    )
    assert partial_exp > 2


def verify_primary_floor_coefficient() -> None:
    # For complete-block length ell=1 the cycle floor n>N gives
    # q=1/(X*n)<1/(X*N). For ell>=2 the coordinate bound gives
    # q<ell*d/(2*X^ell)<=ell*d/(2*X^2).
    # The first term is the larger one for the primary candidate.
    assert 2 * X > D0 * N

    floor_u = Fraction(1, X * N)
    coordinate_u = Fraction(D0, 2 * X * X)
    assert floor_u > coordinate_u

    # delta-epsilon > (d/B-1/(X*N))/ln(2).
    # With ln(2)<7/10, the following exact rational comparison proves
    # delta-epsilon > 997*2^-4002.
    rational_lower = Fraction(10, 7) * (Fraction(D0, B) - floor_u)
    target = Fraction(997, 1 << 4002)
    assert rational_lower > target

    # Consequences for a nondecreasing segment of positive net credit C:
    # L < C/(delta-epsilon) < C*2^4002/997 < C*2^3993.
    assert Fraction(1 << 4002, 997) < (1 << 3993)

    # For the initial macro-exit C<=4500 this improves the uniform bound.
    assert Fraction(4500 * (1 << 4002), 997) < (1 << 4005)


def verify_small_cycle_regressions() -> None:
    # Exact checks of the q-bound on two known accelerated 5n+1 cycles.
    X0, B0, d0 = 5, 8, 3
    cycles = [
        [13, 33, 83],
        [17, 43, 27],
    ]
    for cycle in cycles:
        floor = min(cycle) - 1
        assert floor >= 1
        u = max(Fraction(1, X0 * floor), Fraction(d0, 2 * X0 * X0))
        for source, endpoint, ell in complete_blocks(X0, B0, cycle):
            q = Fraction(B0**ell - X0**ell, X0**ell * d0 * source)
            assert q < ell * u

            # Check the exact complete-block affine identity as a regression.
            n = source
            total_a = 0
            for _ in range(ell):
                a = v2(X0 * n + 1)
                total_a += a
                n = (X0 * n + 1) >> a
            assert n == endpoint
            s_ell = (B0**ell - X0**ell) // d0
            assert (1 << total_a) * endpoint == X0**ell * source + s_ell


def main() -> None:
    verify_ln2_upper_bound()
    verify_primary_floor_coefficient()
    verify_small_cycle_regressions()
    print("cycle-floor local correction sharpening verified")
    print("uniform block correction coefficient: epsilon=1/(X*N*ln(2))")
    print("delta-epsilon > 997*2^-4002")
    print("nondecreasing positive-credit segment: L < C*2^4002/997 < C*2^3993")
    print("primary initial macro-exit: L_macro < 2^4005")


if __name__ == "__main__":
    main()
