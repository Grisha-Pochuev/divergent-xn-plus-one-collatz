#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from xn1 import odd_step, v2


def verify(m: int, length: int, core: int) -> dict[str, object]:
    if m < 2:
        raise ValueError("m must be at least 2")
    if length < 1:
        raise ValueError("length must be positive")
    if core <= 0 or core % 2 == 0:
        raise ValueError("core must be a positive odd integer")

    x = (1 << m) + 1
    start = (1 << (m * length)) * core - 1
    n = start
    valuations: list[int] = []

    for j in range(length):
        if j < length - 1:
            expected = (1 << (m * (length - j))) * (x**j) * core - 1
            assert n == expected
        n, a = odd_step(x, n)
        valuations.append(a)

    raw_exit = (x**length) * core - 1
    exit_r = v2(raw_exit)
    expected_endpoint = raw_exit >> exit_r

    assert n == expected_endpoint
    assert valuations[:-1] == [m] * (length - 1)
    assert valuations[-1] == m + exit_r

    # Exact exit-class check modulo 2^(r+1).
    modulus = 1 << (exit_r + 1)
    coded_core = (pow(pow(x, length, modulus), -1, modulus) * ((1 << exit_r) + 1)) % modulus
    assert core % modulus == coded_core

    return {
        "m": m,
        "X": x,
        "length": length,
        "core": core,
        "start_bit_length": start.bit_length(),
        "exit_v2": exit_r,
        "endpoint_bit_length": n.bit_length(),
        "endpoint_greater_than_start": n > start,
        "valuations": valuations if length <= 32 else valuations[:8] + ["..."] + valuations[-8:],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--L", type=int, required=True)
    parser.add_argument("--u", type=int, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.m, args.L, args.u), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
