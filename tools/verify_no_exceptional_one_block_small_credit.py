#!/usr/bin/env python3
from __future__ import annotations


def main() -> None:
    k = 500
    m = 4501
    N = (1 << k) - 1
    B = 1 << m
    d = 349 * (1 << 500) - 347
    X = B - d

    assert X % N == 0
    assert m % k == 1
    assert X % 8 == 3

    # For 1<=D<=500, any positive odd Delta<=2^D-1<=N satisfying
    # Delta==2^(m*p-D) mod N must be Delta=1 and p==D mod 500.
    for D in range(1, 501):
        upper = (1 << D) - 1
        assert upper <= N
        for p_mod_k in range(k):
            exponent = (m * p_mod_k - D) % k
            residue = pow(2, exponent, N)
            if exponent == 0:
                assert residue == 1
                # The only positive number <=N in this residue class is 1.
            else:
                assert residue == 1 << exponent
                assert residue % 2 == 0
                # No positive odd number <=N has this residue.

    # If Delta=1, the exact equation is 2^A-X^p=1.  For A>=3,
    # X==3 mod 8 makes the left side 5 or 7 mod 8 according to p parity.
    assert (0 - pow(X, 1, 8)) % 8 == 5
    assert (0 - pow(X, 2, 8)) % 8 == 7

    print("one-block no-exceptional cycles with D<=500 are excluded")
    print("modulo 2^500-1 forces Delta=1")
    print("modulo 8 then gives the contradiction")


if __name__ == "__main__":
    main()
