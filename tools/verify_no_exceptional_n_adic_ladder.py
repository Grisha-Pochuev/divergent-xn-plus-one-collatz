#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd


def main() -> None:
    k = 500
    m = 4501
    N = (1 << k) - 1
    B = 1 << m
    d = 349 * (1 << 500) - 347
    X = B - d
    q = 1093
    Q = q * q

    # X is exactly one N-layer deep.
    assert B % (N * N) == (2 + 18 * N) % (N * N)
    assert d == 2 + 349 * N
    assert X % (N * N) == (-331 * N) % (N * N)
    assert gcd(331, N) == 1
    assert gcd(X // N, N) == 1
    assert d < N * N

    # The depth-j fixed residue is d^{-1} modulo N^j.
    residues: list[int] = []
    for j in range(1, 9):
        modulus = N**j
        residue = pow(d, -1, modulus)
        residues.append(residue)
        assert (d * residue - 1) % modulus == 0
        if j >= 3:
            assert residue >= N ** (j - 2)

    r1, r2 = residues[:2]
    assert r1 == (N + 1) // 2
    assert r2 == r1 + N * ((N - 351) // 4)
    assert r2 > N * N // 5

    # Directly verify the contraction-to-fixed-point congruence for samples:
    # F^j(n) == d^{-1} mod N^j whenever j consecutive valuation-m steps occur.
    # Algebraically B*F(n)=X*n+1; the modular recurrence is enough here.
    for seed in [1, 3, 17, N + 2, 7 * N + 4]:
        value = seed
        for j in range(1, 7):
            value = ((X * value + 1) * pow(B, -1, N**j)) % (N**j)
            assert value == pow(d, -1, N**j)

    # Exact simplification constants used in the theorem.
    assert Fraction(2, 3 * N + 1) < Fraction(2, 3 * N)
    assert Fraction(5, N * N) + Fraction(1, N - 1) < Fraction(4, 3 * N)
    assert Fraction(1, 2 * Q * N * (N - 1)) < Fraction(1, 2 * N)

    print("no-exceptional N-adic ladder verified")
    print("X is exactly one N-layer deep")
    print("depth-j residue is d^-1 modulo N^j")
    print("r2>N^2/5 and r_j>=N^(j-2) for j>=3")
    print("simplified reciprocal constants verified exactly")


if __name__ == "__main__":
    main()
