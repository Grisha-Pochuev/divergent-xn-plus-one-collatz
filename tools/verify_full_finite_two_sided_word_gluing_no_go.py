#!/usr/bin/env python3
"""Verify full finite two-sided valuation-word gluing and closure reduction."""
from __future__ import annotations


def v2(value: int) -> int:
    assert value > 0
    return (value & -value).bit_length() - 1


def odd_step(X: int, n: int) -> tuple[int, int]:
    numerator = X * n + 1
    valuation = v2(numerator)
    return numerator >> valuation, valuation


def word_constants(X: int, word: tuple[int, ...]) -> tuple[int, int]:
    assert X >= 3 and X % 2 == 1
    assert word and all(a >= 1 for a in word)
    total = 0
    additive = 0
    length = len(word)
    for j, valuation in enumerate(word):
        additive += X ** (length - 1 - j) * (1 << total)
        total += valuation
    return total, additive


def outgoing_code(X: int, word: tuple[int, ...]) -> tuple[int, int]:
    total, additive = word_constants(X, word)
    modulus = 1 << (total + 1)
    residue = (
        ((1 << total) - additive) * pow(X, -len(word), modulus)
    ) % modulus
    assert residue % 2 == 1
    return residue, modulus


def incoming_endpoint_code(
    X: int, word: tuple[int, ...]
) -> tuple[int, int]:
    total, additive = word_constants(X, word)
    modulus = X ** len(word)
    residue = additive * pow(1 << total, -1, modulus) % modulus
    return residue, modulus


def crt_pair(
    first_residue: int,
    first_modulus: int,
    second_residue: int,
    second_modulus: int,
) -> tuple[int, int]:
    assert first_modulus % 2 == 1
    assert second_modulus & (second_modulus - 1) == 0
    multiplier = (
        (second_residue - first_residue)
        * pow(first_modulus, -1, second_modulus)
    ) % second_modulus
    value = first_residue + first_modulus * multiplier
    period = first_modulus * second_modulus
    assert value % first_modulus == first_residue % first_modulus
    assert value % second_modulus == second_residue % second_modulus
    return value, period


def observe(
    X: int, start: int, word: tuple[int, ...]
) -> tuple[int, tuple[int, ...]]:
    assert start > 0 and start % 2 == 1
    valuations: list[int] = []
    current = start
    for _ in word:
        current, valuation = odd_step(X, current)
        valuations.append(valuation)
    assert tuple(valuations) == word
    return current, tuple(valuations)


def backward_source(
    X: int, endpoint: int, word: tuple[int, ...]
) -> tuple[int, list[int]]:
    current = endpoint
    reverse_states = [current]
    for valuation in reversed(word):
        numerator = (1 << valuation) * current - 1
        assert numerator % X == 0
        current = numerator // X
        assert current % 2 == 1
        reverse_states.append(current)
    states = list(reversed(reverse_states))
    return current, states


def glue_words(
    X: int,
    incoming: tuple[int, ...],
    outgoing: tuple[int, ...],
    lift: int,
) -> tuple[int, int, int, int]:
    incoming_residue, odd_modulus = incoming_endpoint_code(X, incoming)
    outgoing_residue, two_modulus = outgoing_code(X, outgoing)
    boundary, period = crt_pair(
        incoming_residue,
        odd_modulus,
        outgoing_residue,
        two_modulus,
    )
    boundary += lift * period

    while True:
        source, backward_states = backward_source(X, boundary, incoming)
        if boundary > 0 and min(backward_states) > 0:
            break
        boundary += period

    incoming_endpoint, _ = observe(X, source, incoming)
    assert incoming_endpoint == boundary
    outgoing_endpoint, _ = observe(X, boundary, outgoing)

    assert boundary % odd_modulus == incoming_residue
    assert boundary % two_modulus == outgoing_residue
    assert boundary % 2 == 1
    return source, boundary, outgoing_endpoint, period


def closure_data(
    X: int,
    outgoing: tuple[int, ...],
    incoming: tuple[int, ...],
) -> tuple[int, int]:
    outgoing_total, outgoing_additive = word_constants(X, outgoing)
    incoming_total, incoming_additive = word_constants(X, incoming)
    denominator = (
        (1 << (outgoing_total + incoming_total))
        - X ** (len(outgoing) + len(incoming))
    )
    numerator = (
        X ** len(incoming) * outgoing_additive
        + (1 << outgoing_total) * incoming_additive
    )
    return numerator, denominator


def verify_residual_identity(
    X: int,
    incoming: tuple[int, ...],
    outgoing: tuple[int, ...],
    source: int,
    boundary: int,
    outgoing_endpoint: int,
) -> None:
    outgoing_total, _ = word_constants(X, outgoing)
    numerator, denominator = closure_data(X, outgoing, incoming)
    residual = denominator * boundary - numerator
    expected = (
        (1 << outgoing_total)
        * X ** len(incoming)
        * (source - outgoing_endpoint)
    )
    assert residual == expected
    assert (residual == 0) == (source == outgoing_endpoint)


def verify_small_grid() -> int:
    words = (
        (1,),
        (2,),
        (1, 1),
        (1, 2),
        (2, 1),
        (3, 2),
        (1, 3, 2),
        (4, 1, 2),
    )
    checked = 0
    for X in range(5, 52, 2):
        for incoming in words:
            for outgoing in words:
                source, boundary, endpoint, _ = glue_words(
                    X, incoming, outgoing, lift=3
                )
                verify_residual_identity(
                    X,
                    incoming,
                    outgoing,
                    source,
                    boundary,
                    endpoint,
                )
                checked += 1
    assert checked == 1536
    return checked


def verify_primary_candidate() -> int:
    m = 4501
    d = 349 * (1 << 500) - 347
    X = (1 << m) - d
    cases = (
        ((1,), (1, 2)),
        ((m,), (1, 2, 3)),
        ((m, m - 7), (2, 1)),
        ((m + 5, 2), (m, 1)),
        ((1, m, 3), (4, 2)),
        ((m, m + 7), (1, m - 1)),
    )
    for index, (incoming, outgoing) in enumerate(cases):
        source, boundary, endpoint, period = glue_words(
            X, incoming, outgoing, lift=index + 2
        )
        assert boundary.bit_length() > 4500
        assert period.bit_length() > 4500
        verify_residual_identity(
            X,
            incoming,
            outgoing,
            source,
            boundary,
            endpoint,
        )
    return len(cases)


def verify_known_cycle_split() -> None:
    X = 5
    outgoing = (1,)
    incoming = (1, 5)
    numerator, denominator = closure_data(X, outgoing, incoming)
    assert numerator == 39
    assert denominator == 3
    assert numerator % denominator == 0
    boundary = numerator // denominator
    assert boundary == 13
    outgoing_endpoint, _ = observe(X, boundary, outgoing)
    assert outgoing_endpoint == 33
    incoming_endpoint, _ = observe(X, outgoing_endpoint, incoming)
    assert incoming_endpoint == boundary


def main() -> None:
    small = verify_small_grid()
    primary = verify_primary_candidate()
    verify_known_cycle_split()
    print("full finite two-sided word gluing no-go verified")
    print(f"small exact gluings checked={small}")
    print(f"primary-candidate gluings checked={primary}")
    print("known 5n+1 split closure reproduced: 13 -> 33 -> 83 -> 13")
    print("exact closure is equivalent to incoming-source/outgoing-endpoint matching")


if __name__ == "__main__":
    main()
