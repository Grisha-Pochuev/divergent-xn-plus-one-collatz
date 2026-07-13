#!/usr/bin/env python3
"""Check that durable project-memory files agree on the current frontier."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRIMARY_X = "2^4501-349*2^500+347"
PRIMARY_CLASSES = "16562000"
PRIMARY_BARRIER = "10^1201"
GLOBAL_MIN_ORDINARY_BLOCKS = "245833"
POSITIVE_RETURN_FRONTIER = "2^3990"
OLD_NONPOSITIVE_RETURN_FRONTIER = "2^(2^974)"
EVEN_H_CYCLE_FRONTIER = "2^(2^4979)"
EVEN_H_RETURN_FRONTIER = "2^(2^4978)"
GLOBAL_PHASE_DOC = "GLOBAL_BLOCK_GCD_PHASE_SIEVE"
GLOBAL_PHASE_TOOL = "verify_global_block_gcd_phase_sieve.py"
GLOBAL_DIVISOR_MARKER = "S_h/g divides 2^D-1"
PRIMARY_GCD_MARKER = "gcd(S_2,2^D-1)=1"
PHASE_MARKER = "n_t==B^(-j)*S_j (mod g)"
RETRACTED_BARRIER = "10^37"

CURRENT_CHECKPOINT = (
    "docs/SESSION_CHECKPOINT_2026-07-13_"
    "GLOBAL_BLOCK_GCD_PHASE_SIEVE.md"
)

CURRENT_MEMORY_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    CURRENT_CHECKPOINT,
)

CURRENT_STRUCTURE_FILES = (
    "docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md",
    "tools/verify_global_ordinary_block_count_frontier.py",
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
    "docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md",
    "tools/verify_complete_block_gcd_compression_no_go.py",
    "docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md",
    "tools/verify_geometric_factor_strong_divisibility.py",
    "docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md",
    "tools/verify_global_block_gcd_phase_sieve.py",
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

    for relative in ("START_HERE.md", "docs/CURRENT_STATUS.md"):
        require(
            relative,
            PRIMARY_CLASSES,
            PRIMARY_BARRIER,
            GLOBAL_MIN_ORDINARY_BLOCKS,
            POSITIVE_RETURN_FRONTIER,
            OLD_NONPOSITIVE_RETURN_FRONTIER,
            EVEN_H_CYCLE_FRONTIER,
            EVEN_H_RETURN_FRONTIER,
            GLOBAL_PHASE_DOC,
            GLOBAL_PHASE_TOOL,
            GLOBAL_DIVISOR_MARKER,
            PRIMARY_GCD_MARKER,
            PHASE_MARKER,
            CURRENT_CHECKPOINT if relative == "START_HERE.md" else "h even",
        )

    require(
        CURRENT_CHECKPOINT,
        GLOBAL_DIVISOR_MARKER,
        PRIMARY_GCD_MARKER,
        EVEN_H_CYCLE_FRONTIER,
        EVEN_H_RETURN_FRONTIER,
        "2^4500",
        GLOBAL_PHASE_TOOL,
    )

    require(
        "docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md",
        GLOBAL_DIVISOR_MARKER,
        "S_h/gcd(S_h,2^D-1) divides g divides S_h",
        PHASE_MARKER,
        PRIMARY_GCD_MARKER,
        EVEN_H_CYCLE_FRONTIER,
        EVEN_H_RETURN_FRONTIER,
        "43 -> 27 -> 17 -> 43",
    )

    require(
        "tools/verify_global_block_gcd_phase_sieve.py",
        "gcd_checks_D_1_to_4500",
        "conditional_full_cycle_frontier",
        "conditional_return_frontier",
        "small_cycles_checked",
    )

    checks = read("run_checks.py")
    if GLOBAL_PHASE_TOOL not in checks:
        raise AssertionError(f"run_checks.py does not include {GLOBAL_PHASE_TOOL}")

    for relative in ("docs/RETRACTIONS.md", "docs/LATEST_VALID_PROGRESS.md"):
        text = read(relative)
        if RETRACTED_BARRIER not in text:
            raise AssertionError(f"{relative} does not mention retracted {RETRACTED_BARRIER}")
        lowered = text.lower()
        if "retract" not in lowered and "отоз" not in lowered:
            raise AssertionError(f"{relative} lacks a retraction marker")

    print("project-memory consistency verified")
    print(f"primary candidate={PRIMARY_X}")
    print(f"global ordinary-block minimum={GLOBAL_MIN_ORDINARY_BLOCKS}")
    print(f"positive-return frontier={POSITIVE_RETURN_FRONTIER}")
    print(f"general nonpositive-return frontier={OLD_NONPOSITIVE_RETURN_FRONTIER}")
    print(f"even-h full-cycle frontier={EVEN_H_CYCLE_FRONTIER}")
    print(f"even-h return frontier={EVEN_H_RETURN_FRONTIER}")
    print("global common-boundary divisor and phase sieve=active")
    print("strict prize target=open")


if __name__ == "__main__":
    check()
