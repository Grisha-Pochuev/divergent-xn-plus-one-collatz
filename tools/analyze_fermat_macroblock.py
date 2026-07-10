#!/usr/bin/env python3
"""Exact macroblock and precision-transfer analysis for X = 2^m + 1."""
from __future__ import annotations

import argparse
import json
import math

from xn1 import v2


def multiplier(m: int) -> int:
    if m < 2:
        raise ValueError("m must be at least 2")
    return (1 << m) + 1


def macro_endpoint(m: int, length: int) -> int:
    """Endpoint after the complete L-step block from 2^(mL)-1."""
    if length < 1:
        raise ValueError("L must be positive")
    x = multiplier(m)
    k = v2(length)
    numerator = x**length - 1
    assert v2(numerator) == m + k
    return numerator >> (m + k)


def pow_sum_mod(base: int, exponent: int, modulus: int) -> tuple[int, int]:
    """Return (base^exponent, sum_{j<exponent} base^j) modulo modulus."""
    if exponent < 0 or modulus < 1:
        raise ValueError("require exponent >= 0 and modulus >= 1")
    if exponent == 0:
        return 1 % modulus, 0
    if exponent % 2 == 0:
        power, total = pow_sum_mod(base, exponent // 2, modulus)
        return power * power % modulus, total * (1 + power) % modulus
    power, total = pow_sum_mod(base, exponent - 1, modulus)
    return power * base % modulus, (total + power) % modulus


def endpoint_mod_for_odd_part(m: int, k: int, odd_part: int, bits: int) -> int:
    """E_{m,k}(u) modulo 2^bits for L=2^k*u, u odd."""
    if k < 0 or bits < 1 or odd_part < 1 or odd_part % 2 == 0:
        raise ValueError("require k >= 0, bits >= 1, and positive odd u")
    x = multiplier(m)
    modulus = 1 << bits
    lifted_modulus = 1 << (m + k + bits)
    a_lift = pow(x, 1 << k, lifted_modulus)
    c = (a_lift - 1) >> (m + k)
    a = a_lift % modulus
    _, geometric_sum = pow_sum_mod(a, odd_part, modulus)
    return c * geometric_sum % modulus


def hensel_target_odd_part(m: int, k: int, bits: int) -> int:
    """Unique odd u mod 2^bits with E_{m,k}(u) == -1 mod 2^bits."""
    if bits < 1:
        raise ValueError("bits must be positive")
    u = 1
    for known_bits in range(1, bits):
        next_bits = known_bits + 1
        candidates = (u, u + (1 << known_bits))
        good = [
            candidate
            for candidate in candidates
            if (endpoint_mod_for_odd_part(m, k, candidate, next_bits) + 1)
            % (1 << next_bits)
            == 0
        ]
        if len(good) != 1:
            raise AssertionError("precision target did not lift uniquely")
        u = good[0]
    return u


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--L", type=int)
    parser.add_argument("--k", type=int, default=0)
    parser.add_argument("--precision", type=int, default=16)
    args = parser.parse_args()

    x = multiplier(args.m)
    target_u = hensel_target_odd_part(args.m, args.k, args.precision)
    report: dict[str, object] = {
        "m": args.m,
        "X": x,
        "target_k": args.k,
        "target_precision": args.precision,
        "unique_target_odd_part_mod_2^precision": target_u,
    }

    target_length = (1 << args.k) * target_u
    if target_length.bit_length() <= 24:
        target_endpoint = macro_endpoint(args.m, target_length)
        report["target_positive_representative_length"] = target_length
        report["target_endpoint_v2_plus_1"] = v2(target_endpoint + 1)

    if args.L is not None:
        endpoint = macro_endpoint(args.m, args.L)
        start = (1 << (args.m * args.L)) - 1
        k = v2(args.L)
        odd_part = args.L >> k
        predicted_residue = (
            odd_part
            if k == 0
            else odd_part + (1 << (args.m - 1))
        ) % (1 << args.m)
        report.update({
            "L": args.L,
            "v2_L": k,
            "odd_part_L": odd_part,
            "start_bit_length": start.bit_length(),
            "endpoint_bit_length": endpoint.bit_length(),
            "endpoint_v2_plus_1": v2(endpoint + 1),
            "endpoint_mod_2^m": endpoint % (1 << args.m),
            "predicted_endpoint_mod_2^m": predicted_residue,
            "net_growth_after_exit": endpoint > start,
            "sufficient_growth_margin_bits": (
                args.L * math.log2(x / (1 << args.m)) - (args.m + k + 1)
            ),
        })
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
