#!/usr/bin/env python3
"""Verify the multi-edge repetition ladder exactly."""
from __future__ import annotations

X = 104350542602662257699
TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
CASES = (
    (2, 349, 14_230_475, 3_114_290_401_257,
     7077391788339522082878518496985204893557388703844566593307772732359784688),
    (3, 491, 12_157_734_961, 2_918_613_523,
     692126427931979192228790418011743147969714364959656132701343054118705629843703466512831844),
    (4, 629, 13_180_060_652_871, 2_251_677,
     55719787664457027479737747699827589970881363580579180213349939166117827517013940621066136776234942443748648),
    (5, 762, 16_650_853_633_108_401, 1_500,
     3870792567252275975939498201310492491155314740805796060324781763695205605253434152368864087556133785129469874414691399795398),
)


def word_count(edges: int, threshold: int) -> int:
    """Count positive label words with adjacent sums <= threshold+1."""
    dp = [1] * threshold
    for _ in range(edges):
        prefix: list[int] = []
        running = 0
        for value in dp:
            running += value
            prefix.append(running)
        dp = [prefix[threshold - v] for v in range(1, threshold + 1)]
    return sum(dp)


def verify() -> None:
    for edges, threshold, expected_words, expected_repeat, expected_diameter in CASES:
        words = word_count(edges, threshold)
        assert words == expected_words

        common_repeat = None
        for p in TARGETS:
            A = (133 * p + 1) // 2
            bad_edges = 2 * (A - p) // threshold
            good_windows = p - edges * bad_edges
            assert good_windows > 0
            repetitions = (good_windows + words - 1) // words
            assert repetitions >= expected_repeat
            common_repeat = repetitions if common_repeat is None else min(common_repeat, repetitions)

        assert common_repeat == expected_repeat
        diameter = 2 * X ** (edges + 1) * (expected_repeat - 1)
        assert diameter == expected_diameter

        print(f"m={edges}, K={threshold}")
        print(f"admissible words={words}")
        print(f"forced repetitions={expected_repeat}")
        print(f"forced diameter>={diameter}")

    print("multi-edge repetition ladder verified")


if __name__ == "__main__":
    verify()
