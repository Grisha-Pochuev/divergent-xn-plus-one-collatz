#!/usr/bin/env python3
"""Check that durable project-memory files agree on the retained frontier."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_BARRIER = 177_780_727_155_637_125_192
SPARSE_CAP = 355_561_454_311_274_250_377
SPARSE_EXCEPTIONS = (
    177_780_727_155_637_125_193,
    177_780_727_155_637_125_195,
)
RETRACTED_BARRIER_TEXT = "10^37"

MEMORY_FRONTIER_FILES = (
    "START_HERE.md",
    "README.md",
    "docs/CURRENT_STATUS.md",
    "docs/VALIDATED_RESULTS.md",
    "docs/NEXT_STEPS.md",
    "docs/LATEST_VALID_PROGRESS.md",
)

RETRACTION_FILES = (
    "START_HERE.md",
    "README.md",
    "docs/CURRENT_STATUS.md",
    "docs/RETRACTIONS.md",
    "docs/LATEST_VALID_PROGRESS.md",
)

REQUIRED_PRIORITY1_FILES = (
    "docs/RESIDUE_TRANSITION_NO_GO.md",
    "tools/verify_residue_transition_no_go.py",
    "docs/AUGMENTED_TRANSITION_NO_GO.md",
    "tools/verify_augmented_transition_no_go.py",
    "docs/BALANCED_OCCUPANCY_DUAL_BOUND.md",
    "tools/verify_balanced_occupancy_barrier.py",
    "docs/LARGE_DIVISOR_VALUATION_SPLIT.md",
    "tools/verify_large_divisor_split_barrier.py",
    "docs/FIRST_SPARSE_CYCLE_WINDOW.md",
    "tools/verify_first_sparse_cycle_window.py",
    "docs/FIRST_EXCEPTION_ELIMINATION.md",
    "tools/verify_first_exception_elimination.py",
    "docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md",
    "tools/verify_global_transition_identities.py",
    "docs/FULL_MODULUS_ACTIVATION_BOUND.md",
    "tools/verify_full_modulus_activation_bound.py",
    "docs/INDEX_EIGHT_SMALL_REPRESENTATIVE_SIEVE.md",
    "tools/verify_index_eight_small_sieve.py",
    "docs/THIRD_EXCEPTION_SUBGROUP_SIEVE.md",
    "tools/verify_third_exception_subgroup_sieve.py",
)

LATEST_TOOLS = (
    "verify_full_modulus_activation_bound.py",
    "verify_index_eight_small_sieve.py",
    "verify_third_exception_subgroup_sieve.py",
)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"missing durable project file: {relative}")
    return path.read_text(encoding="utf-8")


def check() -> None:
    barrier_plain = str(CURRENT_BARRIER)
    cap_plain = str(SPARSE_CAP)

    for relative in REQUIRED_PRIORITY1_FILES:
        read(relative)

    for relative in MEMORY_FRONTIER_FILES:
        text = read(relative)
        if barrier_plain not in text:
            raise AssertionError(
                f"{relative} does not contain barrier {barrier_plain}"
            )
        if cap_plain not in text:
            raise AssertionError(
                f"{relative} does not contain sparse cap {cap_plain}"
            )
        for exception in SPARSE_EXCEPTIONS:
            if str(exception) not in text:
                raise AssertionError(
                    f"{relative} does not contain exception {exception}"
                )

    for relative in RETRACTION_FILES:
        text = read(relative)
        if RETRACTED_BARRIER_TEXT not in text:
            raise AssertionError(
                f"{relative} does not mention retracted {RETRACTED_BARRIER_TEXT}"
            )
        lowered = text.lower()
        if "retract" not in lowered and "отоз" not in lowered:
            raise AssertionError(f"{relative} lacks a retraction marker")

    audit = read("tools/verify_continued_fraction_barrier.py")
    if f"CURRENT_RETAINED_BARRIER = {barrier_plain}" not in audit:
        raise AssertionError("retraction audit records a different barrier")
    if f"CURRENT_SPARSE_CAP = {cap_plain}" not in audit:
        raise AssertionError("retraction audit records a different sparse cap")

    checks = read("run_checks.py")
    for tool in LATEST_TOOLS:
        if tool not in checks:
            raise AssertionError(f"run_checks.py does not include {tool}")

    print("project-memory consistency verified")
    print(f"current contiguous barrier={CURRENT_BARRIER}")
    print(f"current sparse cap={SPARSE_CAP}")
    print(f"remaining sparse exceptions={SPARSE_EXCEPTIONS}")
    print(f"priority-1 certificate files={len(REQUIRED_PRIORITY1_FILES)}")


if __name__ == "__main__":
    check()
