#!/usr/bin/env python3
"""Check that durable project-memory files agree on the current frontier."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRIMARY_X = "2^4501-349*2^500+347"
PRIMARY_CLASSES = "16562000"
PRIMARY_BARRIER = "10^1201"
GLOBAL_MIN_ORDINARY_BLOCKS = "245833"
GLOBAL_LENGTH_UPPER = "544026748963771"
CIRCULATION_MAX_CREDIT = "20250000"
CIRCULATION_MAX_BLOCKS = "20254499"
ACTUAL_MAX_CREDIT = "4500"
ACTUAL_MAX_EXCESS = "4499"
ACTUAL_MAX_BLOCKS = "4500"
GAP_MARKER = "2^-4023"
POSITIVE_RETURN_FRONTIER = "2^3990"
NONPOSITIVE_RETURN_FRONTIER = "2^(2^974)"
FIXED_ENDPOINT_NO_GO = "FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO"
FULL_WORD_NO_GO = "FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO"
CYCLIC_GCD_THEOREM = "CYCLIC_ROTATION_CLOSURE_GCD"
CYCLIC_GCD_MARKER = "gcd(Q_k,Q_(k+1))=Delta"
RETRACTED_BARRIER = "10^37"

CURRENT_CHECKPOINT = (
    "docs/SESSION_CHECKPOINT_2026-07-12_"
    "CYCLIC_ROTATION_CLOSURE_GCD.md"
)

CURRENT_MEMORY_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    CURRENT_CHECKPOINT,
)

CURRENT_STRUCTURE_FILES = (
    "docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md",
    "tools/verify_mersenne_divisor_wieferich_family.py",
    "docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md",
    "docs/NO_EXCEPTIONAL_X_ADIC_LADDER.md",
    "tools/verify_no_exceptional_x_adic_ladder.py",
    "docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md",
    "tools/verify_global_ordinary_block_count_frontier.py",
    "docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md",
    "tools/verify_minimum_boundary_positive_circulation.py",
    "docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md",
    "tools/verify_minimum_boundary_actual_expanding_segment.py",
    "docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md",
    "tools/verify_minimum_boundary_return_credit_dichotomy.py",
    "docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md",
    "tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py",
    "docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md",
    "tools/verify_fixed_local_endpoint_congruence_no_go.py",
    "docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md",
    "tools/verify_full_finite_two_sided_word_gluing_no_go.py",
    "docs/CYCLIC_ROTATION_CLOSURE_GCD.md",
    "tools/verify_cyclic_rotation_closure_gcd.py",
)

RETRACTION_FILES = (
    "docs/RETRACTIONS.md",
    "docs/LATEST_VALID_PROGRESS.md",
)

LATEST_TOOLS = (
    "verify_mersenne_divisor_wieferich_family.py",
    "verify_no_exceptional_x_adic_ladder.py",
    "verify_no_exceptional_block_count_frontier.py",
    "verify_one_exception_one_ordinary_no_go.py",
    "verify_one_exception_block_count_frontier.py",
    "verify_global_ordinary_block_count_frontier.py",
    "verify_minimum_boundary_positive_circulation.py",
    "verify_minimum_boundary_actual_expanding_segment.py",
    "verify_minimum_boundary_return_credit_dichotomy.py",
    "verify_minimum_boundary_nonpositive_return_harmonic_barrier.py",
    "verify_fixed_local_endpoint_congruence_no_go.py",
    "verify_full_finite_two_sided_word_gluing_no_go.py",
    "verify_cyclic_rotation_closure_gcd.py",
)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"missing durable project file: {relative}")
    return path.read_text(encoding="utf-8")


def require(relative: str, *markers: str) -> None:
    text = read(relative)
    for marker in markers:
        if marker not in text:
            raise AssertionError(f"{relative} lacks required marker {marker}")


def check() -> None:
    for relative in CURRENT_STRUCTURE_FILES:
        read(relative)

    for relative in CURRENT_MEMORY_FILES:
        require(relative, PRIMARY_X)

    require(
        "START_HERE.md",
        PRIMARY_CLASSES,
        PRIMARY_BARRIER,
        GLOBAL_MIN_ORDINARY_BLOCKS,
        CIRCULATION_MAX_CREDIT,
        CIRCULATION_MAX_BLOCKS,
        ACTUAL_MAX_EXCESS,
        POSITIVE_RETURN_FRONTIER,
        NONPOSITIVE_RETURN_FRONTIER,
        FIXED_ENDPOINT_NO_GO,
        FULL_WORD_NO_GO,
        CYCLIC_GCD_THEOREM,
        CYCLIC_GCD_MARKER,
        CURRENT_CHECKPOINT,
    )

    require(
        "docs/CURRENT_STATUS.md",
        PRIMARY_CLASSES,
        PRIMARY_BARRIER,
        GLOBAL_MIN_ORDINARY_BLOCKS,
        GLOBAL_LENGTH_UPPER,
        CIRCULATION_MAX_CREDIT,
        CIRCULATION_MAX_BLOCKS,
        ACTUAL_MAX_EXCESS,
        GAP_MARKER,
        POSITIVE_RETURN_FRONTIER,
        NONPOSITIVE_RETURN_FRONTIER,
        FULL_WORD_NO_GO,
        CYCLIC_GCD_THEOREM,
        CYCLIC_GCD_MARKER,
        "1536",
        "6820",
    )

    require(
        CURRENT_CHECKPOINT,
        POSITIVE_RETURN_FRONTIER,
        NONPOSITIVE_RETURN_FRONTIER,
        FULL_WORD_NO_GO,
        CYCLIC_GCD_MARKER,
        "6820",
        "known 5n+1 cycles checked=3",
    )

    require(
        "docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md",
        ACTUAL_MAX_CREDIT,
        ACTUAL_MAX_EXCESS,
        ACTUAL_MAX_BLOCKS,
        GAP_MARKER,
        "L*log2(B/X)<C",
    )

    require(
        "docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md",
        POSITIVE_RETURN_FRONTIER,
        "2^-3990",
    )

    require(
        "docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md",
        NONPOSITIVE_RETURN_FRONTIER,
        PRIMARY_CLASSES,
        GAP_MARKER,
    )

    require(
        "docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md",
        "1984",
        "Chinese remainder theorem",
        "X^ell",
    )

    require(
        "docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md",
        "Chinese remainder theorem",
        "X^r*2^(A_W+1)",
        "2^(A_W+A_V)-X^(t+r)",
        "13 -> 33 -> 83 -> 13",
    )

    require(
        "docs/CYCLIC_ROTATION_CLOSURE_GCD.md",
        "2^a_k*Q_(k+1)=X*Q_k+Delta",
        CYCLIC_GCD_MARKER,
        "Delta|Q_0",
        "Q(U)=X^r*Q_W+2^A_W*Q_V",
        "Q_t>Q_0",
    )

    require(
        "docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md",
        CIRCULATION_MAX_CREDIT,
        CIRCULATION_MAX_BLOCKS,
        GAP_MARKER,
    )

    require(
        "docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md",
        GLOBAL_MIN_ORDINARY_BLOCKS,
        GLOBAL_LENGTH_UPPER,
    )

    for relative in RETRACTION_FILES:
        text = read(relative)
        if RETRACTED_BARRIER not in text:
            raise AssertionError(
                f"{relative} does not mention retracted {RETRACTED_BARRIER}"
            )
        lowered = text.lower()
        if "retract" not in lowered and "отоз" not in lowered:
            raise AssertionError(f"{relative} lacks a retraction marker")

    checks = read("run_checks.py")
    for tool in LATEST_TOOLS:
        if tool not in checks:
            raise AssertionError(f"run_checks.py does not include {tool}")

    print("project-memory consistency verified")
    print(f"primary candidate={PRIMARY_X}")
    print(f"global ordinary-block minimum={GLOBAL_MIN_ORDINARY_BLOCKS}")
    print(f"formal circulation maximum blocks={CIRCULATION_MAX_BLOCKS}")
    print(f"actual expanding segment maximum blocks={ACTUAL_MAX_BLOCKS}")
    print(f"positive-return frontier={POSITIVE_RETURN_FRONTIER}")
    print(f"nonpositive-return frontier={NONPOSITIVE_RETURN_FRONTIER}")
    print("full finite endpoint-congruence route=no-go without closure")
    print("exact cycle closure=cyclic adjacent-numerator gcd reaches Delta")


if __name__ == "__main__":
    check()
