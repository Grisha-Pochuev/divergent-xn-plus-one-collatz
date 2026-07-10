#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
from xn1 import trajectory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--X", type=int, required=True)
    parser.add_argument("--n0", type=int, required=True)
    parser.add_argument("--steps", type=int, default=10000)
    args = parser.parse_args()

    n = args.n0
    total_a = 0
    max_a = 0
    min_n = n
    for _, current, a, nxt in trajectory(args.X, args.n0, args.steps):
        total_a += a
        max_a = max(max_a, a)
        min_n = min(min_n, current, nxt)
        n = nxt

    digest = hashlib.sha256(str(n).encode()).hexdigest()
    report = {
        "X": args.X,
        "n0": args.n0,
        "steps": args.steps,
        "average_v2": total_a / args.steps if args.steps else 0.0,
        "max_v2": max_a,
        "minimum_value_seen": min_n,
        "final_bit_length": n.bit_length(),
        "final_sha256_decimal": digest,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
