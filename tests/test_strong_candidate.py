from pathlib import Path
import math
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from verify_strong_candidate import (
    MAX_EXCLUDED_CYCLE_LENGTH,
    ORDER,
    Q,
    Y_DEN,
    Y_NUM,
    verify_certificate,
    verify_cycle_length_obstruction,
    verify_order,
    verify_wieferich_condition,
)
from xn1 import odd_step


def test_strong_candidate_order_and_wieferich_data() -> None:
    verify_order()
    assert verify_wieferich_condition() == 3
    assert pow(2, ORDER, Q) == 1


def test_strong_candidate_first_step() -> None:
    nxt, a = odd_step(Q, 1)
    assert (nxt, a) == (189_812_533, 2)
    assert math.gcd(nxt, Q) == 1


def test_strong_candidate_cycle_bound_inequalities() -> None:
    details = verify_cycle_length_obstruction()
    assert details["maximum_even_r"] == 17_500_000
    assert details["maximum_odd_r"] == 17_499_999
    assert 2 * 17_500_000 * Y_NUM < Y_DEN


def test_strong_candidate_full_certificate() -> None:
    report = verify_certificate()
    assert report["Q"] == Q
    assert report["excluded_nontrivial_cycle_lengths_through"] == MAX_EXCLUDED_CYCLE_LENGTH
    assert report["wieferich_common_factor"] == 3
