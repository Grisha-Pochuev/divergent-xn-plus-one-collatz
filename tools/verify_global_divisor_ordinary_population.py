#!/usr/bin/env python3
from __future__ import annotations

from math import gcd

K_BITS = 500
M_BITS = 4501
Q = 1093

N = (1 << K_BITS) - 1
B = 1 << M_BITS
D0 = 349 * (1 << 500) - 347
X = B - D0
PERMANENT_MODULUS = N * Q * Q
CLASS_COUNT = 16_562_000
MAX_ORDINARY_CREDIT = 4500

Q_CREDIT = 924679364903952241768234680715310598867316370441120757898246831506500507205080014535351439406991342585993538327845986892977536682537320095988153612270886695873966778097766981798062925612878469213187733241206117142814414961418054803443235355123715316220902421623921086365374327267387194352877014114959


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def verify_candidate_coprimality() -> None:
    assert X % N == 0
    assert X % Q == 0
    assert B % N == 2
    assert D0 % N == 2
    assert gcd(D0, N) == 1
    assert B % Q == D0 % Q
    assert gcd(B, Q) == 1

    # Check the closed congruence formula for a broad exact sample of h.
    inv_d_n = pow(D0, -1, N)
    inv_d_q = pow(D0, -1, Q)
    for h in range(1, 2001):
        s_mod_n = (pow(B, h, N) - pow(X, h, N)) * inv_d_n % N
        s_mod_q = (pow(B, h, Q) - pow(X, h, Q)) * inv_d_q % Q
        assert s_mod_n == pow(2, h - 1, N)
        assert s_mod_q == pow(B, h - 1, Q)
        assert gcd(s_mod_n, N) == 1
        assert s_mod_q != 0


def verify_population_frontier() -> tuple[int, int]:
    assert (1 << 996) < Q_CREDIT < (1 << 997)
    ordinary_min = ceil_div(Q_CREDIT, MAX_ORDINARY_CREDIT)
    type_count = MAX_ORDINARY_CREDIT * CLASS_COUNT
    repetition_min = ceil_div(ordinary_min, type_count)

    assert type_count == 74_529_000_000
    assert type_count < (1 << 37)
    assert MAX_ORDINARY_CREDIT * type_count < (1 << 49)
    assert repetition_min > (1 << 947)
    assert repetition_min - 1 >= (1 << 947)

    assert N > (1 << 499)
    assert Q * Q > (1 << 20)
    assert (repetition_min - 1) * PERMANENT_MODULUS > (1 << 1466)
    return ordinary_min, repetition_min


def main() -> None:
    verify_candidate_coprimality()
    ordinary_min, repetition_min = verify_population_frontier()
    print("global-divisor ordinary population verified")
    print(f"ordinary blocks >= {ordinary_min}")
    print(f"one joint same-credit boundary type occurs >= {repetition_min}")
    print("repetition count >2^947")
    print("boundary-source diameter >g*2^1466")


if __name__ == "__main__":
    main()
