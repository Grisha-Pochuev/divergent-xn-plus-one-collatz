#!/usr/bin/env python3
"""Check that durable project-memory files agree on retained frontiers."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_CONTIGUOUS_BARRIER = 177_780_727_155_637_125_192
OLD_SPARSE_CAP = 355_561_454_311_274_250_377
OLD_SPARSE_EXCEPTIONS = (
    177_780_727_155_637_125_193,
    177_780_727_155_637_125_195,
)

PRIMARY_X156_BARRIER = (
    7_034_970_411_803_187_993_997_906_985_047_212_163_795_395_134
)
PRIMARY_THRESHOLD = PRIMARY_X156_BARRIER + 1
RETRACTED_BARRIER_TEXT = "10^37"

OLD_FRONTIER_FILES = (
    "README.md",
    "docs/CURRENT_STATUS.md",
    "docs/VALIDATED_RESULTS.md",
    "docs/NEXT_STEPS.md",
    "docs/LATEST_VALID_PROGRESS.md",
)

PRIMARY_FRONTIER_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    "docs/SESSION_CHECKPOINT_2026-07-11_SHARP_BLOCK_SIGN.md",
    "docs/NEAR_POWER_SHARP_BLOCK_SIGN.md",
)

RETRACTION_FILES = (
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
    "verify_near_power_block_sign_threshold.py",
)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"missing durable project file: {relative}")
    return path.read_text(encoding="utf-8")


def check() -> None:
    old_barrier_plain = str(OLD_CONTIGUOUS_BARRIER)
    old_cap_plain = str(OLD_SPARSE_CAP)
    primary_barrier_plain = str(PRIMARY_X156_BARRIER)
    primary_threshold_plain = str(PRIMARY_THRESHOLD)

    for relative in REQUIRED_PRIORITY1_FILES:
        read(relative)

    for relative in OLD_FRONTIER_FILES:
        text = read(relative)
        if old_barrier_plain not in text:
            raise AssertionError(
                f"{relative} does not contain old barrier {old_barrier_plain}"
            )
        if old_cap_plain not in text:
            raise AssertionError(
                f"{relative} does not contain old sparse cap {old_cap_plain}"
            )
        for exception in OLD_SPARSE_EXCEPTIONS:
            if str(exception) not in text:
                raise AssertionError(
                    f"{relative} does not contain old exception {exception}"
                )

    for relative in PRIMARY_FRONTIER_FILES:
        text = read(relative)
        if primary_barrier_plain not in text:
            raise AssertionError(
                f"{relative} does not contain X156 barrier "
                f"{primary_barrier_plain}"
            )
        if primary_threshold_plain not in text:
            raise AssertionError(
                f"{relative} does not contain X156 threshold "
                f"{primary_threshold_plain}"
            )

    for relative in RETRACTION_FILES:
        text = read(relative)
        if RETRACTED_BARRIER_TEXT not in text:
            raise AssertionError(
                f"{relative} does not mention retracted "
                f"{RETRACTED_BARRIER_TEXT}"
            )
        lowered = text.lower()
        if "retract" not in lowered and "отоз" not in lowered:
            raise AssertionError(f"{relative} lacks a retraction marker")

    audit = read("tools/verify_continued_fraction_barrier.py")
    if f"CURRENT_RETAINED_BARRIER = {old_barrier_plain}" not in audit:
        raise AssertionError("retraction audit records a different old barrier")
    if f"CURRENT_SPARSE_CAP = {old_cap_plain}" not in audit:
        raise AssertionError("retraction audit records a different sparse cap")

    checks = read("run_checks.py")
    for tool in LATEST_TOOLS:
        if tool not in checks:
            raise AssertionError(f"run_checks.py does not include {tool}")

    print("project-memory consistency verified")
    print(f"primary X156 barrier={PRIMARY_X156_BARRIER}")
    print(f"primary X156 first threshold={PRIMARY_THRESHOLD}")
    print(f"old contiguous barrier={OLD_CONTIGUOUS_BARRIER}")
    print(f"old sparse cap={OLD_SPARSE_CAP}")
    print(f"old sparse exceptions={OLD_SPARSE_EXCEPTIONS}")
    print(f"priority-1 certificate files={len(REQUIRED_PRIORITY1_FILES)}")


if __name__ == "__main__":
    check()
