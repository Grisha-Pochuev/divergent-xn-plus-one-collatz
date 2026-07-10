from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from verify_continued_fraction_barrier import (
    ELL,
    P_MAX,
    X,
    harmonic_upper,
    ln_bounds,
    verify_barrier,
    verify_order,
)
from fractions import Fraction


def test_exact_order_certificate() -> None:
    verify_order()
    assert pow(2, ELL, X) == 1


def test_legendre_condition_at_barrier() -> None:
    ln2_lo, _ = ln_bounds(Fraction(2))
    assert 2 * P_MAX * harmonic_upper(P_MAX) < ELL * X * ln2_lo


def test_full_continued_fraction_barrier() -> None:
    result = verify_barrier()
    assert result["excluded_nontrivial_cycle_lengths_through"] == 10**37
    assert result["upper_convergents_checked"] == 19
    assert result["largest_checked_upper_denominator"] == 7286014786354216885839578116495624057
    assert result["first_certified_convergent_denominator_beyond_barrier"] == 61591102310422922843464723184177907160
