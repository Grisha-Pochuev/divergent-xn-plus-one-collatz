#!/usr/bin/env python3
from __future__ import annotations

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


def distinct_prime_factors(n: int) -> list[int]:
    out: list[int] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def verify_exact_order(base: int, order: int, modulus: int) -> None:
    assert pow(base, order, modulus) == 1
    for p in distinct_prime_factors(order):
        assert pow(base, order // p, modulus) != 1


def main() -> None:
    m = 3803
    d = 4_162_203
    B = 1 << m
    X = B - d
    n0 = 1

    q_square = 3511
    h_square = 1755
    Q_square = q_square * q_square

    q_linear = 1093
    h_linear = 364
    Q_linear = q_linear * q_linear

    assert X >= 5 and X % 2 == 1 and n0 == 1

    # Both primes are base-2 Wieferich with the displayed exact orders.
    verify_exact_order(2, h_square, q_square)
    verify_exact_order(2, h_square, Q_square)
    verify_exact_order(2, h_linear, q_linear)
    verify_exact_order(2, h_linear, Q_linear)

    # The chosen near-power difference gives q_square^2 | X and q_linear || X.
    assert B % Q_square == d % Q_square == 4_162_203
    assert vp(X, q_square) == 2
    assert (X // Q_square) % q_square == 1526

    assert B % q_linear == d % q_linear == 59
    assert vp(X, q_linear) == 1
    assert (X // q_linear) % q_linear == 219

    # The orbit leaves 1 immediately.  The symbolic note proves no later return.
    assert v2(X + 1) == 1
    n1 = (X + 1) // 2
    assert n1 > 1 and n1 % q_linear != 0

    # Permanent class counts.
    # q_square^2 | X: one current valuation label gives one residue class.
    square_classes = h_square
    assert len({pow(pow(2, s, Q_square), -1, Q_square)
                for s in range(1, h_square + 1)}) == square_classes

    # q_linear || X: the adjacent-label theorem supplies h_linear^2 classes.
    # The current labels modulo the two orders must agree modulo gcd=13.
    g = gcd(h_square, h_linear)
    L = lcm(h_square, h_linear)
    assert g == 13 and L == 49_140
    combined_classes = h_linear * L
    combined_modulus = Q_square * Q_linear
    assert combined_classes == 17_886_960
    assert combined_modulus == 14_726_582_775_529

    # Exact density comparison against the current X=2^156-9 sieve.
    current_classes = h_linear * h_linear
    current_modulus = Q_linear
    improvement_num = current_classes * combined_modulus
    improvement_den = current_modulus * combined_classes
    assert improvement_num > 91_312 * improvement_den
    assert improvement_num < 91_313 * improvement_den

    # Exact exceptional-source progression v2(d*n-1)=m.
    modulus_2B = 2 * B
    n_exc = ((B + 1) * pow(d, -1, modulus_2B)) % modulus_2B
    assert 0 < n_exc < modulus_2B
    assert v2(d * n_exc - 1) == m
    u0 = (d * n_exc - 1) // B
    assert u0 == 1_422_295 and u0 % 2 == 1

    # Combine that progression with the q_square^2 one-label classes.
    step_inverse = pow(modulus_2B, -1, Q_square)
    best: tuple[int, int, int, int] | None = None
    for s in range(1, h_square + 1):
        residue = pow(pow(2, s, Q_square), -1, Q_square)
        t = ((residue - n_exc % Q_square) * step_inverse) % Q_square
        n = n_exc + modulus_2B * t
        row = (n, t, s, residue)
        if best is None or row < best:
            best = row

    assert best is not None
    n_min, t_min, s_min, residue_min = best
    u_min = (d * n_min - 1) // B
    assert t_min == 2377
    assert s_min == 1615
    assert residue_min == 9_391_230
    assert u_min == 19_788_535_357
    assert n_min == (u_min * B + 1) // d
    assert v2(d * n_min - 1) == m
    assert n_min % Q_square == residue_min

    # Add the adjacent-label q_linear^2 sieve and prove the exact first
    # compatible exceptional progression layer by scanning all smaller layers.
    c_linear = (X // q_linear) % q_linear
    square_label_by_residue = {
        pow(pow(2, s, Q_square), -1, Q_square): s
        for s in range(1, h_square + 1)
    }
    adjacent_pair_by_residue: dict[int, tuple[int, int]] = {}
    for previous in range(1, h_linear + 1):
        previous_mod_q = pow(pow(2, previous, q_linear), -1, q_linear)
        for current in range(1, h_linear + 1):
            current_inverse = pow(pow(2, current, Q_linear), -1, Q_linear)
            residue = (
                current_inverse
                * (1 + q_linear * c_linear * previous_mod_q)
            ) % Q_linear
            assert residue not in adjacent_pair_by_residue
            adjacent_pair_by_residue[residue] = (previous, current)
    assert len(adjacent_pair_by_residue) == h_linear * h_linear

    combined_t = 2_350_560
    residue_square = n_exc % Q_square
    residue_linear = n_exc % Q_linear
    step_square = modulus_2B % Q_square
    step_linear = modulus_2B % Q_linear
    first_compatible: tuple[int, int, tuple[int, int], int, int] | None = None
    for t in range(combined_t + 1):
        square_label = square_label_by_residue.get(residue_square)
        if square_label is not None:
            adjacent_pair = adjacent_pair_by_residue.get(residue_linear)
            if (
                adjacent_pair is not None
                and (square_label - adjacent_pair[1]) % g == 0
            ):
                first_compatible = (
                    t, square_label, adjacent_pair, residue_square, residue_linear
                )
                break
        residue_square = (residue_square + step_square) % Q_square
        residue_linear = (residue_linear + step_linear) % Q_linear

    assert first_compatible == (
        combined_t, 40, (99, 222), 11_331_739, 820_246
    )
    n_combined_min = n_exc + modulus_2B * combined_t
    u_combined_min = (d * n_combined_min - 1) // B
    assert u_combined_min == 19_567_017_189_655
    assert n_combined_min == (u_combined_min * B + 1) // d
    assert v2(d * n_combined_min - 1) == m

    # Elementary cycle barrier: p <= floor(2X/(3d)) is impossible.
    barrier = (2 * X) // (3 * d)
    assert barrier > 10**1138

    print("dual-Wieferich square-sieve candidate verified")
    print(f"m={m}, d={d}")
    print(f"v_3511(X)={vp(X, q_square)}, v_1093(X)={vp(X, q_linear)}")
    print(f"combined classes={combined_classes}/{combined_modulus}")
    print("density improvement over X156 is between 91312 and 91313")
    print(f"square-only exceptional minimum: u={u_min}, label={s_min}, layer={t_min}")
    print(
        "combined exceptional minimum: "
        f"u={u_combined_min}, layer={combined_t}, labels=(99,222;40)"
    )
    print(f"cycle barrier has {len(str(barrier))} decimal digits and exceeds 10^1138")


if __name__ == "__main__":
    main()
