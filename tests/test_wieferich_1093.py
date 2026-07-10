from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from verify_wieferich_1093 import (
    EXPECTED_ORDER,
    Q,
    multiplicative_order_2_mod_q,
    verify_certificate,
)
from xn1 import odd_step


def test_order_and_wieferich_congruence() -> None:
    assert multiplicative_order_2_mod_q() == EXPECTED_ORDER == 364
    assert pow(2, EXPECTED_ORDER, Q) == 1
    assert pow(2, EXPECTED_ORDER, Q * Q) == 1


def test_output_coprime_to_q() -> None:
    for n in range(1, 1000, 2):
        nxt, _ = odd_step(Q, n)
        assert nxt % Q != 0


def test_direct_predecessor_samples_divisible_by_q() -> None:
    for k in range(1, 6):
        m = (pow(2, EXPECTED_ORDER * k) - 1) // Q
        assert m % Q == 0


def test_full_wieferich_certificate() -> None:
    report = verify_certificate()
    assert report["first_accelerated_value_from_1"] == 547
    assert report["pow_2_order_mod_q_squared"] == 1
