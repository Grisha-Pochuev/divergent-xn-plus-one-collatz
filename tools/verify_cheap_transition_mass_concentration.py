#!/usr/bin/env python3
"""Verify the cheap-transition mass concentration theorem exactly."""
from __future__ import annotations

from fractions import Fraction

X = 104350542602662257699
O = 1860810887857924950
TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
K = 5000
PAIR_COUNT = 12502500
EXPECTED_EXPENSIVE_CAP = 4657855051477692680
EXPECTED_MIN_REP = 781563824454394220933608138645145
EXPECTED_MIN_PAIR = (2395, 2209)
REQUIRED_RECIPROCAL_LOWER = (
    Fraction(506785306, 10**9),
    Fraction(99934206, 10**9),
)
EXPECTED_SMALL_EXPENSIVE_TARGET = (
    9190982840926584716,
    46609216582838682965,
)


def log_bounds(z: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Positive atanh-series lower and upper bounds for log(z), z>=1."""
    assert z >= 1
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= y2
    lower = 2 * partial
    upper = lower + 2 * power / (2 * terms + 1) / (1 - y2)
    return lower, upper


def odd_transition_class(u: int, v: int, inv_x: list[int], inv_x2: list[int]) -> int:
    modulus = X * X
    residue = (inv_x2[v] * (1 + X * inv_x[u])) % modulus
    return residue if residue & 1 else residue + modulus


def exact_minimum_cheap_representative() -> tuple[int, tuple[int, int], int]:
    modulus = X * X
    inv_x = [0] + [pow(2, -u, X) for u in range(1, K + 1)]
    inv_x2 = [0] + [pow(2, -v, modulus) for v in range(1, K + 1)]

    minimum = 2 * modulus
    argmin = (0, 0)
    count = 0
    for u in range(1, K + 1):
        rhs = 1 + X * inv_x[u]
        for v in range(1, K + 2 - u):
            representative = (inv_x2[v] * rhs) % modulus
            if not representative & 1:
                representative += modulus
            if representative < minimum:
                minimum = representative
                argmin = (u, v)
            count += 1
    return minimum, argmin, count


def verify() -> None:
    assert pow(2, O, X) == 1
    assert K < 2 * O
    assert PAIR_COUNT == K * (K + 1) // 2

    minimum, argmin, count = exact_minimum_cheap_representative()
    assert count == PAIR_COUNT
    assert minimum == EXPECTED_MIN_REP
    assert argmin == EXPECTED_MIN_PAIR

    u, v = argmin
    modulus = X * X
    inv_x = [0] + [pow(2, -j, X) for j in range(1, K + 1)]
    inv_x2 = [0] + [pow(2, -j, modulus) for j in range(1, K + 1)]
    representative = odd_transition_class(u, v, inv_x, inv_x2)
    assert representative == minimum
    source = ((1 << v) * representative - 1) // X
    assert source > 0 and source & 1
    assert X * source + 1 == (1 << v) * representative
    assert source % X == pow(2, -u, X)

    # Independently verify the retained rational lower bounds for X*Lambda.
    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)

    outputs: list[tuple[int, int, int, Fraction, int]] = []
    for p, required, expected_target in zip(
        TARGETS,
        REQUIRED_RECIPROCAL_LOWER,
        EXPECTED_SMALL_EXPENSIVE_TARGET,
    ):
        A = (133 * p + 1) // 2
        expensive_cap = 2 * (A - p) // K
        cheap_count = p - expensive_cap
        assert expensive_cap == EXPECTED_EXPENSIVE_CAP

        x_lambda_lower = X * (log2_lower - p * eta_upper) / 2
        assert x_lambda_lower > required

        cheap_reciprocal_bound = Fraction(cheap_count, minimum)
        residual = required - cheap_reciprocal_bound
        assert residual > 0

        # If every expensive target were at least M+1, its reciprocal sum
        # would be at most expensive_cap/(M+1).  The largest possible M is
        # ceil(expensive_cap/residual)-1.
        forced_target = (
            expensive_cap * residual.denominator + residual.numerator - 1
        ) // residual.numerator - 1
        assert forced_target == expected_target
        assert forced_target < X

        outputs.append(
            (p, cheap_count, expensive_cap, cheap_reciprocal_bound, forced_target)
        )

    print("cheap-transition mass concentration verified")
    print(f"cheap pairs={PAIR_COUNT}")
    print(f"minimum cheap representative={minimum} at pair={argmin}")
    for p, cheap, expensive, bound, target in outputs:
        print(f"p={p}")
        print(f"cheap edges>={cheap}, expensive edges<={expensive}")
        print(f"cheap reciprocal bound approximately {float(bound):.15e}")
        print(f"forced expensive target<={target}")


if __name__ == "__main__":
    verify()
