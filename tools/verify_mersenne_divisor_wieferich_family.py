#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm


def vp(n: int, p: int) -> int:
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def harmonic(n: int) -> Fraction:
    out = Fraction(0, 1)
    for j in range(1, n + 1):
        out += Fraction(1, j)
    return out


def verify_order_500(modulus: int) -> None:
    assert pow(2, 500, modulus) == 1
    assert pow(2, 250, modulus) != 1
    assert pow(2, 100, modulus) != 1


def main() -> None:
    # Explicit member of the general family.
    k = 500
    m = 4501
    r = m % k
    t = 349
    N = (1 << k) - 1
    d = (1 << r) + t * N
    B = 1 << m
    X = B - d
    n0 = 1

    q = 1093
    h = 364
    Q = q * q

    assert r == 1
    assert d == 349 * (1 << 500) - 347
    assert X == (1 << 4501) - 349 * (1 << 500) + 347
    assert X >= 5 and X % 2 == 1 and n0 == 1
    assert d < B // 2

    # N divides X and 2 has exact order k modulo N.
    assert B % N == 1 << r
    assert d % N == 1 << r
    assert X % N == 0
    verify_order_500(N)

    # The Wieferich prime 1093 divides X exactly once.
    assert pow(2, h, Q) == 1
    assert vp(X, q) == 1
    assert (X // q) % q == 334

    # The first step leaves 1.  Symbolically, q||X then forbids return.
    assert B // 2 < X + 1 < B
    assert (X + 1) & X != 0  # X+1 is not a power of two.

    # One-label classes modulo N are exactly the k powers of two.
    residues = {
        pow(pow(2, s, N), -1, N)
        for s in range(1, k + 1)
    }
    assert len(residues) == k
    assert residues == {1} | {1 << j for j in range(1, k)}

    # Their least allowed positive odd representatives exclude 1.
    representatives = [1 + 2 * N]
    representatives.extend(N + (1 << j) for j in range(1, k))
    assert all(n > N and n % 2 == 1 for n in representatives)
    base_sum = sum((Fraction(1, n) for n in representatives), Fraction())
    assert base_sum < Fraction(k, N)

    # Combination with the 1093^2 adjacent-label coordinate.
    g = gcd(k, h)
    K = h * lcm(k, h)
    M = N * Q
    layers = K // k
    assert g == 4
    assert K == 16_562_000
    assert layers == h * h // g == 33_124

    combined_base_bound = Fraction(k, N) * (1 + harmonic(layers) / 2)
    assert combined_base_bound < Fraction(1, 10**147)
    assert combined_base_bound > Fraction(1, 10**148)

    tail_coefficient = Fraction(K, 2 * M)
    assert tail_coefficient < Fraction(1, 10**149)
    assert tail_coefficient > Fraction(1, 10**150)

    # It strictly dominates the previously promoted dual-Wieferich density.
    previous_density = Fraction(17_886_960, 14_726_582_775_529)
    new_density = Fraction(K, M)
    assert previous_density / new_density > 10**143
    assert previous_density / new_density < 10**144

    # Elementary near-power barrier.
    barrier = (2 * X) // (3 * d)
    assert barrier > 10**1201
    assert barrier < 10**1202

    print("Mersenne-divisor Wieferich family example verified")
    print("X=2^4501-349*2^500+347, n0=1")
    print(f"one-label classes={k} modulo N=2^{k}-1")
    print(f"combined classes={K} modulo (2^{k}-1)*1093^2")
    print("combined base reciprocal bound is between 10^-148 and 10^-147")
    print("tail coefficient is between 10^-150 and 10^-149")
    print("density improvement over the dual-Wieferich candidate is between 10^143 and 10^144")
    print("cycle barrier is between 10^1201 and 10^1202")


if __name__ == "__main__":
    main()
