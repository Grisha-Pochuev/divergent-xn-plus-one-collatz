#!/usr/bin/env python3
from __future__ import annotations
import argparse
from xn1 import odd_step


def verify(m: int, length: int) -> None:
    if m < 2 or length < 2:
        raise ValueError("require m >= 2 and L >= 2")
    x = (1 << m) + 1
    n = (1 << (m * length)) - 1
    for j in range(length - 1):
        expected = (1 << (m * (length - j))) * (x**j) - 1
        assert n == expected
        nxt, a = odd_step(x, n)
        assert a == m
        assert nxt > n
        n = nxt
    expected_last = (1 << m) * (x ** (length - 1)) - 1
    assert n == expected_last
    print(f"verified m={m}, L={length}, X={x}, controlled_steps={length-1}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--L", type=int, required=True)
    args = parser.parse_args()
    verify(args.m, args.L)


if __name__ == "__main__":
    main()
