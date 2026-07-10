#!/usr/bin/env python3
"""Check that durable project-memory files agree on the retained frontier.

This is deliberately lightweight.  It does not prove the mathematics again;
it prevents stale status text from silently disagreeing with the exact
certificate and the retraction audit.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_BARRIER = 170_000_000_000_000_000_000
RETRACTED_BARRIER_TEXT = "10^37"

BARRIER_FILES = (
    "START_HERE.md",
    "README.md",
    "docs/CURRENT_STATUS.md",
    "docs/VALIDATED_RESULTS.md",
    "docs/NEXT_STEPS.md",
    "docs/LATEST_VALID_PROGRESS.md",
    "tools/verify_residue_crowding_barrier.py",
    "tools/verify_continued_fraction_barrier.py",
)

RETRACTION_FILES = (
    "START_HERE.md",
    "README.md",
    "docs/CURRENT_STATUS.md",
    "docs/RETRACTIONS.md",
    "docs/LATEST_VALID_PROGRESS.md",
)

REQUIRED_MEMORY_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    "docs/VALIDATED_RESULTS.md",
    "docs/RETRACTIONS.md",
    "docs/NEXT_STEPS.md",
    "docs/CHAT_HANDOFF_TEMPLATE.md",
)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"missing durable project file: {relative}")
    return path.read_text(encoding="utf-8")


def check() -> None:
    barrier_plain = str(CURRENT_BARRIER)

    for relative in REQUIRED_MEMORY_FILES:
        read(relative)

    for relative in BARRIER_FILES:
        text = read(relative)
        if barrier_plain not in text:
            raise AssertionError(
                f"{relative} does not contain current retained barrier {barrier_plain}"
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

    audit_text = read("tools/verify_continued_fraction_barrier.py")
    if "CURRENT_RETAINED_BARRIER" not in audit_text:
        raise AssertionError("retraction audit does not expose the current barrier")

    certificate_text = read("tools/verify_residue_crowding_barrier.py")
    if f"BARRIER = {barrier_plain}" not in certificate_text:
        raise AssertionError("residue-crowding verifier uses a different barrier")

    print("project-memory consistency verified")
    print(f"current retained barrier={CURRENT_BARRIER}")
    print(f"durable memory files={len(REQUIRED_MEMORY_FILES)}")


if __name__ == "__main__":
    check()
