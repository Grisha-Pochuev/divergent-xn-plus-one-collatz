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
CF_DENOMINATOR = "1106246945"
RETRACTED_BARRIER = "10^37"

CURRENT_MEMORY_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    "docs/SESSION_CHECKPOINT_2026-07-12_GLOBAL_BLOCK_COUNT_FRONTIER.md",
    "docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md",
)

CURRENT_STRUCTURE_FILES = (
    "docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md",
    "tools/verify_mersenne_divisor_wieferich_family.py",
    "docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md",
    "docs/NO_EXCEPTIONAL_X_ADIC_LADDER.md",
    "tools/verify_no_exceptional_x_adic_ladder.py",
    "docs/ONE_EXCEPTION_BLOCK_COUNT_FRONTIER.md",
    "tools/verify_one_exception_block_count_frontier.py",
    "docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md",
    "tools/verify_global_ordinary_block_count_frontier.py",
)

RETRACTION_FILES = (
    "docs/CURRENT_STATUS.md",
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
        require(
            relative,
            PRIMARY_X,
            GLOBAL_MIN_ORDINARY_BLOCKS,
        )

    require(
        "START_HERE.md",
        PRIMARY_CLASSES,
        PRIMARY_BARRIER,
        "GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md",
    )

    require(
        "docs/CURRENT_STATUS.md",
        PRIMARY_CLASSES,
        PRIMARY_BARRIER,
        CF_DENOMINATOR,
        GLOBAL_LENGTH_UPPER,
    )

    require(
        "docs/SESSION_CHECKPOINT_2026-07-12_GLOBAL_BLOCK_COUNT_FRONTIER.md",
        CF_DENOMINATOR,
        GLOBAL_LENGTH_UPPER,
    )

    require(
        "docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md",
        CF_DENOMINATOR,
        GLOBAL_LENGTH_UPPER,
        "ordinary blocks",
        "exceptional blocks",
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
    print(f"permanent classes={PRIMARY_CLASSES}")
    print(f"global ordinary-block minimum={GLOBAL_MIN_ORDINARY_BLOCKS}")
    print(f"continued-fraction denominator={CF_DENOMINATOR}")
    print(f"excluded-range cycle-length upper={GLOBAL_LENGTH_UPPER}")


if __name__ == "__main__":
    check()
