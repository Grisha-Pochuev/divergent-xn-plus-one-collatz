from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from build_macroblock_program import (
    Program,
    boundary_value,
    build_q_values,
    terminal_congruence,
    verify_program,
)
from xn1 import odd_step


def test_general_complete_macroblock_formula() -> None:
    m = 3
    x = (1 << m) + 1
    length = 5
    q_value = 11
    n = boundary_value(m, length, q_value)

    observed = []
    for _ in range(length):
        n, valuation = odd_step(x, n)
        observed.append(valuation)

    r = ((x**length) * q_value - 1 & -((x**length) * q_value - 1)).bit_length() - 1
    expected = ((x**length) * q_value - 1) >> r
    assert observed == [m] * (length - 1) + [m + r]
    assert n == expected


def test_three_complete_growing_blocks() -> None:
    program = Program(m=2, lengths=(7, 7, 7, 7), exits=(1, 1, 1))
    q_values = build_q_values(program)
    report = verify_program(program, q_values)

    assert report["all_boundaries_strictly_grow"] is True
    assert report["all_sufficient_margins_positive"] is True
    assert report["boundary_bit_lengths"] == [60, 62, 63, 64]
    assert q_values[0] == 69890900113755


def test_aperiodic_ten_block_program() -> None:
    program = Program(
        m=2,
        lengths=(7, 8, 8, 7, 8, 7, 7, 8, 8, 7, 7),
        exits=(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    )
    q_values = build_q_values(program)
    report = verify_program(program, q_values)

    assert report["all_boundaries_strictly_grow"] is True
    assert report["all_sufficient_margins_positive"] is True
    assert report["boundary_bit_lengths"] == [
        175,
        177,
        178,
        180,
        181,
        183,
        184,
        185,
        187,
        188,
        189,
    ]


def test_terminal_class_has_infinite_odd_lifts() -> None:
    program = Program(m=2, lengths=(7, 8, 7), exits=(1, 1))
    residue, modulus = terminal_congruence(program)
    q0 = build_q_values(program, lift=0)
    q1 = build_q_values(program, lift=1)

    assert q1[-1] - q0[-1] == 2 * modulus
    assert q0[-1] % modulus == residue % modulus
    assert q1[-1] % modulus == residue % modulus
    assert all(value > 0 and value % 2 == 1 for value in q0)
    assert all(value > 0 and value % 2 == 1 for value in q1)
    verify_program(program, q0)
    verify_program(program, q1)
