from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from verify_strong_candidate import EXPONENT_BOUND
from verify_ultra_candidate import (
    BARRIER,
    COFACTOR,
    K,
    X,
    Y_DEN,
    Y_NUM,
    verify_certificate,
    verify_cycle_barrier,
    verify_structure,
)
from xn1 import odd_step


def test_ultra_candidate_structure() -> None:
    verify_structure()
    assert X == 21 * COFACTOR
    assert COFACTOR % 6 == 1
    assert X % 9 == 3


def test_ultra_candidate_first_step() -> None:
    assert odd_step(X, 1) == (26_087_635_650_665_564_425, 2)


def test_ultra_candidate_cycle_inequalities() -> None:
    details = verify_cycle_barrier()
    assert details["maximum_even_r"] == BARRIER // 2
    assert (BARRIER // 2) * Y_NUM * EXPONENT_BOUND.denominator < (
        Y_DEN * EXPONENT_BOUND.numerator
    )
    assert K == 66


def test_ultra_candidate_full_certificate() -> None:
    report = verify_certificate()
    assert report["X"] == X
    assert report["n0"] == 1
    assert report["excluded_nontrivial_cycle_lengths_through"] == BARRIER
