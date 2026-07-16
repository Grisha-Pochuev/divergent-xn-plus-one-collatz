#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

M_EXP = 4501
B = 1 << M_EXP
D0 = 349 * (1 << 500) - 347
X = B - D0
N = (1 << 500) - 1
ALPHA = Fraction(997, 1 << 4002)


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects a positive integer")
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


def verify_primary_constant() -> None:
    # The cycle-floor correction coefficient is u=1/(X*N).
    assert 2 * X > D0 * N
    floor_u = Fraction(1, X * N)

    # -ln(1-d/B)>d/B and ln(2)<7/10 give the exact lower bound
    # delta-epsilon>(10/7)*(d/B-1/(X*N))>alpha.
    rational_lower = Fraction(10, 7) * (Fraction(D0, B) - floor_u)
    assert rational_lower > ALPHA

    # Exact global strip constants.
    upper_per_credit = 1 / ALPHA
    lower_per_credit = 1 << 3992
    assert upper_per_credit / lower_per_credit == Fraction(1024, 997)
    assert Fraction(1024, 997) - 1 == Fraction(27, 997)
    assert Fraction(27, 997) < Fraction(271, 10000)

    # Retained coarse consequences used by the status files.
    assert upper_per_credit < (1 << 3993)
    assert 4500 * upper_per_credit < (1 << 4005)

    # A zero-credit arch of length 2^4002 loses more than 997 bits.
    assert ALPHA * (1 << 4002) == 997


def verify_zero_credit_arch_regression() -> None:
    # In the accelerated 5n+1 cycle 13 -> 33 -> 83 -> 13, with B=8,
    # the canonical zero-credit sponsor arch is 33 -> 83 -> 13.
    X0 = 5
    B0 = 8
    m0 = 3
    cycle = [13, 33, 83]

    valuations = [v2(X0 * n + 1) for n in cycle]
    assert valuations == [1, 1, 5]
    credits = [m0 - a for a in valuations]
    assert credits == [2, 2, -2]

    prefixes = [0]
    for credit in credits:
        prefixes.append(prefixes[-1] + credit)

    exceptional_index = 2
    final_level = prefixes[exceptional_index + 1]
    sponsor_index = max(
        i for i in range(exceptional_index + 1) if prefixes[i] <= final_level
    )
    assert (sponsor_index, exceptional_index) == (1, 2)
    assert sum(credits[sponsor_index : exceptional_index + 1]) == 0

    source = cycle[sponsor_index]
    endpoint = cycle[(exceptional_index + 1) % len(cycle)]
    length = exceptional_index - sponsor_index + 1
    assert (source, endpoint, length) == (33, 13, 2)

    n = source
    total_valuation = 0
    for _ in range(length):
        a = v2(X0 * n + 1)
        total_valuation += a
        n = (X0 * n + 1) >> a
    assert n == endpoint
    assert total_valuation == m0 * length
    assert endpoint < source

    # Exact affine segment identity for the two accelerated steps.
    # 2^A*y = X^L*x + sum_j X^(L-1-j)*2^A_j.
    a0 = v2(X0 * source + 1)
    affine_sum = X0 + (1 << a0)
    assert (1 << total_valuation) * endpoint == X0**length * source + affine_sum


def main() -> None:
    verify_primary_constant()
    verify_zero_credit_arch_regression()
    print("zero-credit arch quantitative contraction verified")
    print("alpha=997*2^-4002")
    print("zero-credit arch: log2(source/endpoint) > alpha*L")
    print("global cycle strip: D*2^3992 < p < D*2^4002/997")
    print("relative strip width: 27/997 < 2.71%")


if __name__ == "__main__":
    main()
