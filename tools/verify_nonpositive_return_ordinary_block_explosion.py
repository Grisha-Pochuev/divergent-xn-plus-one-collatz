#!/usr/bin/env python3
"""Verify the ordinary-block explosion forced by a nonpositive return."""
from __future__ import annotations

import json
from fractions import Fraction

M = 4501
D_MAX = 4500
GAP_EXPONENT = 4023
DELTA_LOSS = GAP_EXPONENT + 1

D0 = 349 * (1 << 500) - 347
B = 1 << M
X = B - D0


def ln2_bounds(terms: int = 2200) -> tuple[Fraction, Fraction]:
    z = Fraction(1, 3)
    z2 = z * z
    power = z
    lower = Fraction(0, 1)
    for j in range(terms):
        lower += power / (2 * j + 1)
        power *= z2
    lower *= 2
    remainder = 2 * power / (2 * terms + 1) / (1 - z2)
    return lower, lower + remainder


def ln1py_bounds() -> tuple[Fraction, Fraction]:
    y = Fraction(D0, X)
    lower = y - y * y / 2
    upper = lower + y * y * y / 3
    return lower, upper


def continued_fraction(value: Fraction, count: int) -> list[int]:
    out: list[int] = []
    current = value
    for _ in range(count):
        integer = current.numerator // current.denominator
        out.append(integer)
        remainder = current - integer
        if remainder <= 0:
            raise AssertionError("continued fraction terminated early")
        current = 1 / remainder
    return out


def convergents(coefficients: list[int]) -> list[tuple[int, int]]:
    p_m2, p_m1 = 0, 1
    q_m2, q_m1 = 1, 0
    out: list[tuple[int, int]] = []
    for coefficient in coefficients:
        p = coefficient * p_m1 + p_m2
        q = coefficient * q_m1 + q_m2
        out.append((p, q))
        p_m2, p_m1 = p_m1, p
        q_m2, q_m1 = q_m1, q
    return out


def verify_gap() -> dict[str, object]:
    ln2_lo, ln2_hi = ln2_bounds()
    lny_lo, lny_hi = ln1py_bounds()
    beta_lo = ln2_lo / lny_hi
    beta_hi = ln2_hi / lny_lo
    cf_lo = continued_fraction(beta_lo, 10)
    cf_hi = continued_fraction(beta_hi, 10)
    if cf_lo != cf_hi:
        raise AssertionError("continued-fraction interval is not stable")
    conv = convergents(cf_lo)
    p7, q7 = conv[7]
    p8, q8 = conv[8]
    _, q9 = conv[9]
    p_star = p7 + p8
    q_star = q7 + q8
    eta_lower = Fraction(p_star, 1) - q_star * beta_hi
    gap_lower = lny_lo * eta_lower
    if q9 != 1_106_246_945 or not D_MAX < q9:
        raise AssertionError("denominator frontier changed")
    if not gap_lower > Fraction(1, 1 << GAP_EXPONENT):
        raise AssertionError("continued-fraction gap is too small")
    return {
        "credit_range": f"1..{D_MAX}",
        "gap_lower": f">2^-{GAP_EXPONENT}",
        "delta_gap_loss": DELTA_LOSS,
        "denominator_frontier": q9,
    }


def verify_tower_case(tower_exponent: int) -> dict[str, object]:
    # Input theorem: p > 2^(2^tower_exponent).
    # Proposed contradiction range: J <= 2^(2^(tower_exponent-1)-7).
    H = (1 << (tower_exponent - 1)) - 7
    overhead_exponent = tower_exponent - 12
    U = 1 << overhead_exponent

    # If J<=2^H, then log2(J)<=H.  The signed elimination inequalities and
    # Delta>2^(M*p-D-DELTA_LOSS) force every block length <=J+U.
    if not H + D_MAX + DELTA_LOSS < M * U:
        raise AssertionError("block-length margin failed")

    # For J>=U: p<2^14 J^2 <= 2^(14+2H)=2^(2^tower_exponent).
    target_log2 = 1 << tower_exponent
    if 14 + 2 * H != target_log2:
        raise AssertionError("large-J tower identity failed")

    # For J<U: p<2^14 U^2, far below the same tower frontier.
    small_case_log2_upper = 14 + 2 * overhead_exponent
    if not small_case_log2_upper < target_log2:
        raise AssertionError("small-J tower comparison failed")

    repeated_type_exponent = H - 13
    if repeated_type_exponent != (1 << (tower_exponent - 1)) - 20:
        raise AssertionError("repeated-type exponent failed")
    if not 4500 < (1 << 13):
        raise AssertionError("boundary-type count bound failed")

    return {
        "cycle_frontier": f"p>2^(2^{tower_exponent})",
        "forced_ordinary_blocks": f"J>2^(2^{tower_exponent-1}-7)",
        "forced_repetition_one_type": f">2^(2^{tower_exponent-1}-20)",
        "uniform_block_overhead": f"2^{overhead_exponent}",
        "small_J_log2_upper": small_case_log2_upper,
        "large_J_log2_upper_equals_target": True,
    }


def main() -> None:
    report = {
        "continued_fraction": verify_gap(),
        "general_nonpositive": verify_tower_case(974),
        "nonpositive_h_ge_2": verify_tower_case(4979),
        "strict_prize_solution": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
