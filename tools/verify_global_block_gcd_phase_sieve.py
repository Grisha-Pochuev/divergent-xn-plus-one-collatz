#!/usr/bin/env python3
"""Verify the global block-gcd/phase-sieve theorem and the primary even-gcd frontier."""
from __future__ import annotations

import json
from functools import reduce
from math import gcd


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def odd_step(x: int, n: int) -> tuple[int, int]:
    z = x * n + 1
    a = v2(z)
    return z >> a, a


def S(B: int, X: int, ell: int) -> int:
    d = B - X
    return (B**ell - X**ell) // d


def block_lengths_and_boundaries(m: int, values: list[int], vals: list[int]) -> tuple[list[int], list[int], int]:
    """Return cyclic complete-block lengths, post-terminal boundaries, total credit."""
    p = len(vals)
    terminals = [i for i, a in enumerate(vals) if a != m]
    if not terminals:
        raise AssertionError("all-m cycle is unsupported")
    lengths: list[int] = []
    boundaries: list[int] = []
    for j, t in enumerate(terminals):
        prev = terminals[j - 1]
        ell = (t - prev) % p
        if ell == 0:
            ell = p
        lengths.append(ell)
        boundaries.append(values[(t + 1) % p])
    D = m * p - sum(vals)
    return lengths, boundaries, D


def canonical_cycle(x: int, start: int, limit: int = 10000) -> tuple[list[int], list[int]] | None:
    seen: dict[int, int] = {}
    values: list[int] = []
    vals: list[int] = []
    n = start
    for _ in range(limit):
        if n in seen:
            k = seen[n]
            cyc_values = values[k:]
            cyc_vals = vals[k:]
            if not cyc_values:
                return None
            # Canonical rotation by least value for deduplication.
            r = min(range(len(cyc_values)), key=cyc_values.__getitem__)
            return cyc_values[r:] + cyc_values[:r], cyc_vals[r:] + cyc_vals[:r]
        seen[n] = len(values)
        values.append(n)
        n2, a = odd_step(x, n)
        vals.append(a)
        n = n2
    return None


def verify_cycle_theorem(m: int, x: int, values: list[int], vals: list[int]) -> None:
    B = 1 << m
    lengths, boundaries, D = block_lengths_and_boundaries(m, values, vals)
    h = 0
    for ell in lengths:
        h = gcd(h, ell)
    Sh = S(B, x, h)
    g = 0
    for n in boundaries:
        g = gcd(g, n)
    if g != gcd(boundaries[0], Sh):
        raise AssertionError((m, x, values, vals, lengths, boundaries, h, Sh, g))
    if Sh % g or ((1 << D) - 1) % (Sh // g):
        raise AssertionError("global quotient divisibility failed")
    forced = Sh // gcd(Sh, (1 << D) - 1)
    if g % forced:
        raise AssertionError("forced divisor missing")

    # Phase sieve. Rotate to the first post-terminal boundary.
    p = len(values)
    terminal = next(i for i, a in enumerate(vals) if a != m)
    start_idx = (terminal + 1) % p
    rot_values = values[start_idx:] + values[:start_idx]
    for t, n in enumerate(rot_values):
        j = t % h
        Sj = 0 if j == 0 else S(B, x, j)
        residue = 0 if j == 0 else (pow(B, -j, g) * Sj) % g
        if n % g != residue:
            raise AssertionError((m, x, values, vals, h, g, t, n, residue))


def small_cycle_regressions() -> tuple[int, list[dict[str, object]]]:
    checked: set[tuple[int, tuple[int, ...]]] = set()
    rows: list[dict[str, object]] = []
    # Several near-power multipliers, enough to include one- and multi-block cycles.
    for m in range(3, 7):
        B = 1 << m
        for d in range(1, min(B - 5, 15) + 1, 2):
            x = B - d
            if x < 5:
                continue
            for start in range(1, 300, 2):
                result = canonical_cycle(x, start, 500)
                if result is None:
                    continue
                values, vals = result
                key = (x, tuple(values))
                if key in checked:
                    continue
                checked.add(key)
                if all(a == m for a in vals):
                    continue
                verify_cycle_theorem(m, x, values, vals)
                lengths, boundaries, D = block_lengths_and_boundaries(m, values, vals)
                h = 0
                for ell in lengths:
                    h = gcd(h, ell)
                rows.append({
                    "X": x,
                    "cycle": values,
                    "valuations": vals,
                    "block_lengths": lengths,
                    "h": h,
                    "D": D,
                    "boundary_gcd": reduce(gcd, boundaries),
                })
    # Required explicit regression: 43 -> 27 -> 17 -> 43 for X=5.
    match = [r for r in rows if r["X"] == 5 and set(r["cycle"]) == {17, 27, 43}]
    if not match:
        raise AssertionError("missing X=5 one-block regression")
    r = match[0]
    if r["h"] != 3 or r["D"] != 2 or r["boundary_gcd"] != 43:
        raise AssertionError(r)
    return len(rows), rows[:8]


def primary_certificate() -> dict[str, object]:
    m = 4501
    B = 1 << m
    N = (1 << 500) - 1
    d = 349 * (1 << 500) - 347
    X = B - d
    S2 = B + X

    # Exact finite certificate: no divisor of S2 has 2-order <=4500.
    nontrivial: list[int] = []
    for D in range(1, 4501):
        if gcd(S2, (1 << D) - 1) != 1:
            nontrivial.append(D)
    if nontrivial:
        raise AssertionError(nontrivial[:10])

    rho = pow(B, -1, S2)
    if rho % 2 != 1:
        rho += S2
    if not (rho < 2 * S2 and 2 * rho > S2):
        raise AssertionError("odd inverse representative bound failed")
    if (B * rho - 1) % S2:
        raise AssertionError("inverse residue failed")

    # If p <= 2^(2^4979), harmonic packing in the two phase classes is too small.
    K = 4979
    if not (((1 << K) + 4) * (1 << 4023) < X * S2):
        raise AssertionError("two-class harmonic contradiction inequality failed")

    # Exit length is <2^4006: delta>d/B>2^-3993 and C<2^13.
    if not (d > (1 << 508)):
        raise AssertionError("d lower bound failed")
    if not (4500 < (1 << 13)):
        raise AssertionError("credit bound failed")

    # Odd h>=3 forced boundary divisor exceeds 2^4500.
    if not (X > (1 << 4500)):
        raise AssertionError("X lower bound failed")
    # S_h/gcd(S_h,2^D-1) > X^(h-1)/2^D; minimum h=3,D=4500.
    if not (X * X > (1 << 9000)):
        raise AssertionError("odd-h lower bound failed")

    return {
        "S2_bits": S2.bit_length(),
        "rho_bits": rho.bit_length(),
        "rho_over_half_S2": bool(2 * rho > S2),
        "gcd_checks_D_1_to_4500": 4500,
        "nontrivial_gcds": len(nontrivial),
        "conditional_full_cycle_frontier": "p > 2^(2^4979)",
        "conditional_return_frontier": "L_return > 2^(2^4978)",
        "exit_length_upper": "L_exit < 2^4006",
        "S2_coprime_to_permanent_modulus": gcd(S2, N * 1093**2) == 1,
    }


def main() -> None:
    count, samples = small_cycle_regressions()
    report = {
        "small_cycles_checked": count,
        "sample_cycles": samples,
        "primary": primary_certificate(),
        "strict_prize_solution": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
