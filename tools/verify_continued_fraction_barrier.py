#!/usr/bin/env python3
"""Exact 10^37 cycle-length barrier for the main fixed candidate.

Only integer and Fraction arithmetic is used. Logarithms are enclosed by
atanh-series rational intervals.
"""
from __future__ import annotations

from fractions import Fraction
import json

X = 104_350_542_602_662_257_699
ELL = 1_860_810_887_857_924_950
P_MAX = 10**37
MIN_CYCLE_VALUE = 25
OUTPUT_MODULUS = 15_099
OUTPUT_ORDER = 2_154
X_FACTORS = (3, 7, 719, 6_911_089_648_497_401)
ELL_FACTORIZATION = {2: 1, 3: 1, 5: 2, 359: 1, 2677: 1, 15137: 1, 852763: 1}
TERMS = 180


def ln_near_one_bounds(z: Fraction) -> tuple[Fraction, Fraction]:
    if z <= 0:
        raise ValueError("log argument must be positive")
    t = (z - 1) / (z + 1)
    t2 = t * t
    power = t
    partial = Fraction(0)
    for j in range(TERMS):
        partial += power / (2 * j + 1)
        power *= t2
    lower = 2 * partial
    tail = 2 * abs(power) / ((2 * TERMS + 1) * (1 - t2))
    return lower, lower + tail


def ln_bounds(z: Fraction) -> tuple[Fraction, Fraction]:
    """Rational enclosure of ln(z), scaling z into [1,2)."""
    if z <= 0:
        raise ValueError("log argument must be positive")
    k = z.numerator.bit_length() - z.denominator.bit_length()
    scaled = z / (1 << k) if k >= 0 else z * (1 << (-k))
    while scaled < 1:
        scaled *= 2
        k -= 1
    while scaled >= 2:
        scaled /= 2
        k += 1
    ln2_lo, ln2_hi = ln_near_one_bounds(Fraction(2))
    s_lo, s_hi = ln_near_one_bounds(scaled)
    if k >= 0:
        return k * ln2_lo + s_lo, k * ln2_hi + s_hi
    return k * ln2_hi + s_lo, k * ln2_lo + s_hi


def continued_fraction(fr: Fraction) -> list[int]:
    out: list[int] = []
    x = fr
    while True:
        a = x.numerator // x.denominator
        out.append(a)
        remainder = x - a
        if remainder == 0:
            return out
        x = 1 / remainder


def convergents(partials: list[int]):
    p0, p1 = 0, 1
    q0, q1 = 1, 0
    for a in partials:
        p2 = a * p1 + p0
        q2 = a * q1 + q0
        yield p2, q2
        p0, p1 = p1, p2
        q0, q1 = q1, q2


def common_prefix(left: list[int], right: list[int]) -> list[int]:
    out: list[int] = []
    for a, b in zip(left, right):
        if a != b:
            break
        out.append(a)
    return out


def verify_order() -> None:
    product = 1
    for factor in X_FACTORS:
        product *= factor
    if product != X:
        raise AssertionError("factorization of X failed")

    ell_product = 1
    for prime, exponent in ELL_FACTORIZATION.items():
        ell_product *= prime**exponent
    if ell_product != ELL:
        raise AssertionError("factorization of ELL failed")

    if pow(2, ELL, X) != 1:
        raise AssertionError("ELL is not an exponent of 2 modulo X")
    for prime in ELL_FACTORIZATION:
        if pow(2, ELL // prime, X) == 1:
            raise AssertionError("ELL is not the exact order")


def allowed_bases() -> list[int]:
    """Least nontrivial odd representatives of all output classes mod 15099."""
    if pow(2, OUTPUT_ORDER, OUTPUT_MODULUS) != 1:
        raise AssertionError("bad output period")
    residues = {pow(2, -a, OUTPUT_MODULUS) for a in range(OUTPUT_ORDER)}
    if len(residues) != OUTPUT_ORDER:
        raise AssertionError("incomplete output subgroup")
    bases: list[int] = []
    for residue in residues:
        value = residue if residue % 2 else residue + OUTPUT_MODULUS
        if value == 1:
            value += 2 * OUTPUT_MODULUS
        bases.append(value)
    if min(bases) != MIN_CYCLE_VALUE:
        raise AssertionError("wrong minimum output")
    return bases


def harmonic_upper(p: int) -> Fraction:
    """Upper bound for reciprocal sum of p distinct allowed cycle values."""
    bases = allowed_bases()
    classes = len(bases)
    levels = (p + classes - 1) // classes
    base_sum = sum((Fraction(1, value) for value in bases), Fraction(0))
    if levels <= 1:
        return base_sum
    # For each residue class, all further odd representatives are spaced by
    # 2*OUTPUT_MODULUS. Replacing every base by the smallest possible base 25
    # in the integral tail gives a rigorous common upper bound.
    ratio = Fraction(MIN_CYCLE_VALUE + 2 * OUTPUT_MODULUS * (levels - 1), MIN_CYCLE_VALUE)
    _lo, log_hi = ln_bounds(ratio)
    return base_sum + Fraction(classes, 2 * OUTPUT_MODULUS) * log_hi


def verify_barrier() -> dict[str, object]:
    verify_order()
    ln2_lo, ln2_hi = ln_bounds(Fraction(2))
    lnx_lo, lnx_hi = ln_bounds(Fraction(X))

    beta_lo = lnx_lo / (ELL * ln2_hi)
    beta_hi = lnx_hi / (ELL * ln2_lo)
    prefix = common_prefix(continued_fraction(beta_lo), continued_fraction(beta_hi))
    if len(prefix) < 20:
        raise AssertionError("log interval does not determine enough CF digits")

    hmax = harmonic_upper(P_MAX)
    if not 2 * P_MAX * hmax < ELL * X * ln2_lo:
        raise AssertionError("Legendre reduction failed at P_MAX")

    checked: list[dict[str, int]] = []
    first_beyond: int | None = None
    for num, den in convergents(prefix):
        if den > P_MAX:
            first_beyond = den
            break
        gap_lo = ELL * num * ln2_lo - den * lnx_hi
        if gap_lo <= 0:
            continue
        if not gap_lo > hmax / X:
            raise AssertionError("an upper convergent survives the correction bound")
        checked.append({"numerator": num, "denominator": den})

    if first_beyond is None or first_beyond <= P_MAX:
        raise AssertionError("continued-fraction prefix does not pass P_MAX")
    if len(checked) != 19:
        raise AssertionError(f"expected 19 upper convergents, got {len(checked)}")

    return {
        "X": X,
        "n0": 1,
        "order_of_2_mod_X": ELL,
        "output_residue_classes": OUTPUT_ORDER,
        "excluded_nontrivial_cycle_lengths_through": P_MAX,
        "upper_convergents_checked": len(checked),
        "largest_checked_upper_denominator": checked[-1]["denominator"],
        "first_certified_convergent_denominator_beyond_barrier": first_beyond,
        "arithmetic": "exact integers and rational intervals only",
    }


def main() -> None:
    print(json.dumps(verify_barrier(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
