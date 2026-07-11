#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

M = 4501
B = 1 << M
D0 = 349 * (1 << 500) - 347
X = B - D0


def main() -> None:
    assert 1 < D0 < X
    assert X % 2 == 1 and D0 % 2 == 1

    inverse_d = pow(D0, -1, X)
    power_two = 1
    terminal_rows: list[tuple[int, int]] = []

    for deficit in range(1, M):
        power_two = (2 * power_two) % X
        residue = (power_two * inverse_d) % X
        representative = residue if residue % 2 == 1 else residue + X
        if representative == 1:
            representative += 2 * X

        # Every terminal output with deficit e is in this odd class.
        assert (D0 * representative - (1 << deficit)) % X == 0
        assert 3 * deficit * representative > X
        terminal_rows.append((deficit, representative))

    assert len(terminal_rows) == M - 1
    worst_deficit, worst_representative = max(
        terminal_rows,
        key=lambda row: Fraction(X, row[0] * row[1]),
    )
    worst_ratio = Fraction(X, worst_deficit * worst_representative)
    assert worst_ratio < 3
    assert worst_ratio > Fraction(14, 5)
    assert worst_deficit == 7

    # Repeated valuation-M steps converge to d^{-1} modulo X^j.
    for depth in range(1, 7):
        modulus = X**depth
        residue = pow(D0, -1, modulus)
        assert (D0 * residue - 1) % modulus == 0
        assert residue >= (modulus + 1) // D0

    # Exact geometric simplifications used in the theorem.
    assert Fraction(D0, X) + Fraction(D0, X * (X - 1)) == Fraction(D0, X - 1)
    assert Fraction(1, 2 * X) + Fraction(1, 2 * X * (X - 1)) == Fraction(1, 2 * (X - 1))

    print("no-exceptional X-adic ladder verified")
    print("all 4500 terminal classes satisfy rho_e>X/(3e)")
    print(f"worst terminal coefficient occurs at e={worst_deficit}")
    print("depth-j internal outputs are fixed modulo X^j")


if __name__ == "__main__":
    main()
