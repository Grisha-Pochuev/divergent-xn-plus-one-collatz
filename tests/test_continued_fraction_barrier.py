from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from verify_continued_fraction_barrier import audit


def test_invalid_order_condition_counterexample() -> None:
    result = audit()
    assert result["status"] == "retracted"
    assert result["counterexample_X"] == 5
    assert result["counterexample_cycle"] == [13, 33, 83]
    assert result["A"] == 7
    assert result["2^A_mod_X"] == 3


def test_correct_cycle_congruence() -> None:
    result = audit()
    assert result["product_cycle_mod_X"] == 2
    assert result["correct_relation_mod_X"] == 1
    assert result["current_retained_fixed_barrier"] == 177780727155637125192
