#!/usr/bin/env python3
from __future__ import annotations

from itertools import product
from math import lcm


def main() -> None:
    k = 500
    m = 4501
    N = (1 << k) - 1
    q = 1093
    h = 364
    Q = q * q
    M = N * Q

    B = 1 << m
    d = 349 * (1 << 500) - 347
    X = B - d
    c = (X // q) % q

    # Two consecutive valuation-m labels determine one exact combined class.
    label_N = m % k
    label_Q = m % h
    assert label_N == 1
    assert label_Q == 133
    assert c == 334

    residue_N = pow(pow(2, label_N, N), -1, N)
    previous_inverse_q = pow(pow(2, label_Q, q), -1, q)
    current_inverse_Q = pow(pow(2, label_Q, Q), -1, Q)
    residue_Q = (
        current_inverse_Q * (1 + q * c * previous_inverse_q)
    ) % Q

    assert residue_N == 1 << 499
    assert residue_Q == 1_041_489

    crt_layer = ((residue_Q - residue_N % Q) * pow(N, -1, Q)) % Q
    residue_M = residue_N + N * crt_layer
    assert residue_M % N == residue_N
    assert residue_M % Q == residue_Q
    assert 0 <= residue_M < M
    assert residue_M % 2 == 0

    least_odd = residue_M + M
    assert least_odd == int(
        "731967947587098522573547868551649529205849263710861084326782"
        "481921597027221433704463008094413638533731953355312124105196"
        "4811350229730788630140247134779072813"
    )
    assert least_odd > M

    # Combinatorial block count: in any cyclic word, if J entries are not m,
    # at least p-2J positions are preceded and followed by m labels.
    for p in range(1, 13):
        for word in product((False, True), repeat=p):
            # True means valuation m.  The all-m word has no terminal block and
            # is excluded independently by D>=1.
            J = sum(not bit for bit in word)
            if J == 0:
                continue
            deep = sum(word[i - 1] and word[i] for i in range(p))
            assert deep >= p - 2 * J

    # Fixed constants used by the theorem.
    K = h * lcm(k, h)
    assert K == 16_562_000
    assert M == ((1 << 500) - 1) * 1093**2

    print("no-exceptional deep-class concentration verified")
    print(f"fixed N residue={residue_N}")
    print(f"fixed 1093^2 residue={residue_Q}")
    print(f"least odd combined representative={least_odd}")
    print("cyclic count checked exhaustively through length 12")


if __name__ == "__main__":
    main()
