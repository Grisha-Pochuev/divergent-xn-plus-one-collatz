#!/usr/bin/env python3
"""Check that durable project-memory files agree on the retained frontier."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_BARRIER = 177_780_727_155_637_125_184
SPARSE_CAP = 355_561_454_311_274_250_377
SPARSE_EXCEPTIONS = (
    177_780_727_155_637_125_185,
    177_780_727_155_637_125_187,
    177_780_727_155_637_125_189,
    177_780_727_155_637_125_191,
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

REQUIRED_FILES = (
    "docs/RESIDUE_TRANSITION_NO_GO.md",
    "tools/verify_residue_transition_no_go.py",
    "docs/AUGMENTED_TRANSITION_NO_GO.md",
    "tools/verify_augmented_transition_no_go.py",
    "docs/BALANCED_OCCUPANCY_DUAL_BOUND.md",
    "tools/verify_balanced_occupancy_barrier.py",
    "docs/LARGE_DIVISOR_VALUATION_SPLIT.md",
    "tools/verify_large_divisor_split_barrier.py",
    "docs/SHARP_LOG_INTERVAL_BARRIER.md",
    "tools/verify_sharp_log_barrier.py",
    "docs/FIRST_SPARSE_CYCLE_WINDOW.md",
    "tools/verify_first_sparse_cycle_window.py",
    "docs/FIRST_EXCEPTION_ELIMINATION.md",
    "tools/verify_first_exception_elimination.py",
    "docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md",
    "tools/verify_global_transition_identities.py",
)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"missing durable project file: {relative}")
    return path.read_text(encoding="utf-8")


def check() -> None:
    barrier_plain = str(CURRENT_BARRIER)
    cap_plain = str(SPARSE_CAP)

    for relative in REQUIRED_FILES:
        read(relative)

    for relative in MEMORY_FRONTIER_FILES:
        text = read(relative)
        if barrier_plain not in text:
            raise AssertionError(
                f"{relative} does not contain current contiguous barrier {barrier_plain}"
            )
        if cap_plain not in text:
            raise AssertionError(
                f"{relative} does not contain current sparse cap {cap_plain}"
            )
        for exception in SPARSE_EXCEPTIONS:
            if str(exception) not in text:
                raise AssertionError(
                    f"{relative} does not contain sparse exception {exception}"
                )

    for relative in RETRACTION_FILES:
        text = read(relative)
        if RETRACTED_BARRIER_TEXT not in text:
            raise AssertionError(
                f"{relative} does not mention retracted barrier {RETRACTED_BARRIER_TEXT}"
            )
        lowered = text.lower()
        if "retract" not in lowered and "отоз" not in lowered:
            raise AssertionError(
                f"{relative} mentions {RETRACTED_BARRIER_TEXT} without a retraction marker"
            )

    exception_text = read("tools/verify_first_exception_elimination.py")
    if "TARGET = 177780727155637125183" not in exception_text:
        raise AssertionError("first-exception verifier uses an unexpected target")

    sparse_text = read("tools/verify_first_sparse_cycle_window.py")
    if f"CAP = {cap_plain}" not in sparse_text:
        raise AssertionError("sparse-window verifier uses a different cap")

    audit_text = read("tools/verify_continued_fraction_barrier.py")
    if f"CURRENT_RETAINED_BARRIER = {barrier_plain}" not in audit_text:
        raise AssertionError("retraction audit records a different barrier")
    if f"CURRENT_SPARSE_CAP = {cap_plain}" not in audit_text:
        raise AssertionError("retraction audit records a different sparse cap")

    run_checks = read("run_checks.py")
    for tool in (
        "verify_balanced_occupancy_barrier.py",
        "verify_augmented_transition_no_go.py",
        "verify_large_divisor_split_barrier.py",
        "verify_sharp_log_barrier.py",
        "verify_first_sparse_cycle_window.py",
        "verify_first_exception_elimination.py",
        "verify_global_transition_identities.py",
    ):
        if tool not in run_checks:
            raise AssertionError(f"run_checks.py does not include {tool}")

    print("project-memory consistency verified")
    print(f"current contiguous barrier={CURRENT_BARRIER}")
    print(f"current sparse cap={SPARSE_CAP}")
    print(f"sparse exceptions={len(SPARSE_EXCEPTIONS)}")
    print(f"priority-1 certificate files={len(REQUIRED_FILES)}")


if __name__ == "__main__":
    check()
