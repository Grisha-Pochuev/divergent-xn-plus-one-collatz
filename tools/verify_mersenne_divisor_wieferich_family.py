#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


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

    # Exact exceptional progression v2(d*n-1)=m.
    modulus_2B = 2 * B
    n_exc = ((B + 1) * pow(d, -1, modulus_2B)) % modulus_2B
    assert 0 < n_exc < modulus_2B
    assert v2(d * n_exc - 1) == m
    u0 = (d * n_exc - 1) // B
    assert u0 == int(
        "937578593120856832981657775299654199170120439926424550439880"
        "178791932328513240962911286104786705519512179141903420156424"
        "601516442564181262667387896197461"
    )

    # For each N-label, solve the exceptional progression layer T modulo N.
    step_N_inverse = pow(modulus_2B % N, -1, N)
    n_rows: list[tuple[int, int, int]] = []
    for s in range(1, k + 1):
        residue_N = pow(pow(2, s, N), -1, N)
        T_N = ((residue_N - n_exc % N) * step_N_inverse) % N
        n_rows.append((T_N, s, residue_N))
    n_rows.sort()

    base_T = int(
        "619540103469531942802682103632394849868765662283779367706995"
        "419025010391745742656926941661665053778874732747814509798848"
        "06889457995961777808814539620"
    )
    assert n_rows[:4] == [
        (base_T, 498, 4),
        (base_T + 1, 497, 8),
        (base_T + 3, 496, 16),
        (base_T + 7, 495, 32),
    ]
    assert n_rows[4][0] > base_T + 7

    # Build the injective q^2 adjacent-label layer map.
    c = (X // q) % q
    step_Q_inverse = pow(modulus_2B % Q, -1, Q)
    pair_by_layer: dict[int, tuple[int, int, int]] = {}
    for previous in range(1, h + 1):
        previous_inverse_q = pow(pow(2, previous, q), -1, q)
        for current in range(1, h + 1):
            current_inverse_Q = pow(pow(2, current, Q), -1, Q)
            residue_Q = (
                current_inverse_Q
                * (1 + q * c * previous_inverse_q)
            ) % Q
            T_Q = ((residue_Q - n_exc % Q) * step_Q_inverse) % Q
            assert T_Q not in pair_by_layer
            pair_by_layer[T_Q] = (previous, current, residue_Q)
    assert len(pair_by_layer) == h * h

    # Any full CRT layer below N must equal one of the N-layers above.  The
    # first three smallest N-layers have no q^2 adjacent-label lift.  The fourth
    # has the unique compatible pair (161,311).
    assert pair_by_layer.get(base_T % Q) is None
    assert pair_by_layer.get((base_T + 1) % Q) is None
    assert pair_by_layer.get((base_T + 3) % Q) is None
    assert pair_by_layer[(base_T + 7) % Q] == (161, 311, 209_910)
    assert 495 % g == 311 % g

    exceptional_T = base_T + 7
    assert exceptional_T < N
    exceptional_u = u0 + 2 * d * exceptional_T
    assert exceptional_u == int(
        "141554173562669451979142234479211407387695161061947663158036"
        "275475013035570532072821977692485924548874811696146286209742"
        "307923384940182399969083204712328957713629782297601610389067"
        "903491331197096456313288013542743720638224927691460837892079"
        "910386115268969408753656537834465197519183303759432510875217219"
    )
    exceptional_n = (exceptional_u * B + 1) // d
    assert v2(d * exceptional_n - 1) == m
    assert len(str(exceptional_n)) == 1505

    print("Mersenne-divisor Wieferich family example verified")
    print("X=2^4501-349*2^500+347, n0=1")
    print(f"one-label classes={k} modulo N=2^{k}-1")
    print(f"combined classes={K} modulo (2^{k}-1)*1093^2")
    print("combined base reciprocal bound is between 10^-148 and 10^-147")
    print("tail coefficient is between 10^-150 and 10^-149")
    print("density improvement over the dual-Wieferich candidate is between 10^143 and 10^144")
    print("cycle barrier is between 10^1201 and 10^1202")
    print(f"first exceptional layer={exceptional_T}, labels=(495;161,311)")
    print("first exceptional source has 1505 decimal digits")


if __name__ == "__main__":
    main()
