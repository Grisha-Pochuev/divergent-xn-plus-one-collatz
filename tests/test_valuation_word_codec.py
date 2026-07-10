from itertools import product
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from valuation_word_codec import coding_residue, observed_word, word_constants


def test_known_cycle_word_code() -> None:
    pattern = (1, 1, 5)
    residue, modulus = coding_residue(5, pattern)
    assert modulus == 256
    assert residue == 13
    observed, endpoint = observed_word(5, residue, len(pattern))
    assert observed == pattern
    assert endpoint == residue


def test_all_small_words_are_exactly_coded() -> None:
    for x in (5, 7, 9, 11):
        for length in range(1, 5):
            for pattern in product(range(1, 5), repeat=length):
                residue, modulus = coding_residue(x, pattern)
                n = residue if residue > 0 else residue + modulus
                observed, _ = observed_word(x, n, length)
                assert observed == pattern
                observed2, _ = observed_word(x, n + 3 * modulus, length)
                assert observed2 == pattern


def test_positive_drift_words_grow_for_all_representatives() -> None:
    examples = [
        (5, (1, 1, 1, 1)),
        (7, (1, 2, 1, 2)),
        (9, (3, 3, 3, 3, 3)),
        (33, (5, 5, 5, 5)),
    ]
    for x, pattern in examples:
        total, _ = word_constants(x, pattern)
        assert x ** len(pattern) > (1 << total)
        residue, modulus = coding_residue(x, pattern)
        for q in range(1, 6):
            n = residue + q * modulus
            observed, endpoint = observed_word(x, n, len(pattern))
            assert observed == pattern
            assert endpoint > n


def test_prefix_codes_are_compatible() -> None:
    x = 5
    word = (2, 1, 3, 1, 1, 4, 2)
    previous_residue = None
    previous_modulus = None
    for length in range(1, len(word) + 1):
        residue, modulus = coding_residue(x, word[:length])
        if previous_residue is not None:
            assert residue % previous_modulus == previous_residue
        previous_residue, previous_modulus = residue, modulus
