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

X156_BARRIER = (
    7_034_970_411_803_187_993_997_906_985_047_212_163_795_395_134
)
X156_THRESHOLD = X156_BARRIER + 1
X156_EXCEPTIONAL_FLOOR = (
    1_268_664_615_738_631_005_385_143_083_955_106_787_895_774_776_889
)

FAMILY_K = 500
FAMILY_M = 4501
FAMILY_CLASSES = 16_562_000
FAMILY_X_TEXT = "2^4501-349*2^500+347"
FAMILY_BARRIER_TEXT = "10^1201"
FAMILY_EXCEPTIONAL_CORE = (
    "141554173562669451979142234479211407387695161061947663158036"
    "275475013035570532072821977692485924548874811696146286209742"
    "307923384940182399969083204712328957713629782297601610389067"
    "903491331197096456313288013542743720638224927691460837892079"
    "910386115268969408753656537834465197519183303759432510875217219"
)
RETRACTED_BARRIER_TEXT = "10^37"

OLD_FRONTIER_FILES = (
    "README.md",
    "docs/VALIDATED_RESULTS.md",
    "docs/NEXT_STEPS.md",
    "docs/LATEST_VALID_PROGRESS.md",
)

X156_FRONTIER_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    "docs/PROGRESS_METRICS.md",
    "docs/SESSION_CHECKPOINT_2026-07-11_SHARP_BLOCK_SIGN.md",
    "docs/SESSION_CHECKPOINT_2026-07-11_BLOCK_LEDGER_AND_EXCEPTIONAL_SIEVE.md",
    "docs/NEAR_POWER_SHARP_BLOCK_SIGN.md",
)

X156_EXCEPTIONAL_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    "docs/PROGRESS_METRICS.md",
    "docs/SESSION_CHECKPOINT_2026-07-11_BLOCK_LEDGER_AND_EXCEPTIONAL_SIEVE.md",
    "docs/X156_EXCEPTIONAL_Q2_SIEVE.md",
)

FAMILY_MEMORY_FILES = (
    "START_HERE.md",
    "README.md",
    "docs/CURRENT_STATUS.md",
    "docs/PROGRESS_METRICS.md",
    "docs/SESSION_CHECKPOINT_2026-07-12_MERSENNE_DIVISOR_FAMILY_FRONTIER.md",
    "docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md",
)

FAMILY_HARMONIC_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    "docs/PROGRESS_METRICS.md",
    "docs/SESSION_CHECKPOINT_2026-07-12_MERSENNE_DIVISOR_FAMILY_FRONTIER.md",
    "docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md",
)

FAMILY_EXCEPTIONAL_FILES = (
    "START_HERE.md",
    "docs/CURRENT_STATUS.md",
    "docs/PROGRESS_METRICS.md",
    "docs/SESSION_CHECKPOINT_2026-07-12_MERSENNE_DIVISOR_FAMILY_FRONTIER.md",
    "docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md",
)

X156_STRUCTURE_FILES = (
    "docs/NEAR_POWER_SHARP_BLOCK_SIGN.md",
    "tools/verify_near_power_block_sign_threshold.py",
    "docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md",
    "tools/verify_near_power_cycle_block_ledger.py",
    "docs/X156_EXCEPTIONAL_Q2_SIEVE.md",
    "tools/verify_x156_exceptional_q2_sieve.py",
)

DUAL_STRUCTURE_FILES = (
    "docs/DUAL_WIEFERICH_SQUARE_SIEVE_CANDIDATE.md",
    "tools/verify_dual_wieferich_square_sieve_candidate.py",
    "docs/DUAL_WIEFERICH_HARMONIC_PACKING.md",
    "tools/verify_dual_wieferich_harmonic_packing.py",
)

FAMILY_STRUCTURE_FILES = (
    "docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md",
    "docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md",
    "tools/verify_mersenne_divisor_wieferich_family.py",
)

RETRACTION_FILES = (
    "README.md",
    "docs/CURRENT_STATUS.md",
    "docs/RETRACTIONS.md",
    "docs/LATEST_VALID_PROGRESS.md",
)

REQUIRED_LEGACY_FILES = (
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
    "verify_near_power_block_sign_threshold.py",
    "verify_near_power_cycle_block_ledger.py",
    "verify_x156_exceptional_q2_sieve.py",
    "verify_dual_wieferich_square_sieve_candidate.py",
    "verify_dual_wieferich_harmonic_packing.py",
    "verify_mersenne_divisor_wieferich_family.py",
)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"missing durable project file: {relative}")
    return path.read_text(encoding="utf-8")


def require_text(relative: str, required: tuple[str, ...]) -> None:
    text = read(relative)
    for marker in required:
        if marker not in text:
            raise AssertionError(f"{relative} lacks required marker {marker}")


def check() -> None:
    old_barrier_plain = str(OLD_CONTIGUOUS_BARRIER)
    old_cap_plain = str(OLD_SPARSE_CAP)
    x156_barrier_plain = str(X156_BARRIER)
    x156_threshold_plain = str(X156_THRESHOLD)
    x156_exceptional_plain = str(X156_EXCEPTIONAL_FLOOR)

    for relative in (
        REQUIRED_LEGACY_FILES
        + X156_STRUCTURE_FILES
        + DUAL_STRUCTURE_FILES
        + FAMILY_STRUCTURE_FILES
    ):
        read(relative)

    for relative in OLD_FRONTIER_FILES:
        require_text(
            relative,
            (old_barrier_plain, old_cap_plain)
            + tuple(str(x) for x in OLD_SPARSE_EXCEPTIONS),
        )

    for relative in X156_FRONTIER_FILES:
        require_text(relative, (x156_barrier_plain, x156_threshold_plain))

    for relative in X156_EXCEPTIONAL_FILES:
        require_text(relative, (x156_exceptional_plain,))

    family_markers = (
        FAMILY_X_TEXT,
        str(FAMILY_CLASSES),
        FAMILY_BARRIER_TEXT,
    )
    for relative in FAMILY_MEMORY_FILES:
        require_text(relative, family_markers)

    for relative in FAMILY_HARMONIC_FILES:
        require_text(relative, ("10^(-147)", "ceil(p/K)", "p*delta-D"))

    for relative in FAMILY_EXCEPTIONAL_FILES:
        require_text(relative, (FAMILY_EXCEPTIONAL_CORE, "1505"))

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
    if f"CURRENT_RETAINED_BARRIER = {old_barrier_plain}" not in audit:
        raise AssertionError("retraction audit records a different old barrier")
    if f"CURRENT_SPARSE_CAP = {old_cap_plain}" not in audit:
        raise AssertionError("retraction audit records a different sparse cap")

    checks = read("run_checks.py")
    for tool in LATEST_TOOLS:
        if tool not in checks:
            raise AssertionError(f"run_checks.py does not include {tool}")

    print("project-memory consistency verified")
    print(
        "primary Mersenne-divisor candidate: "
        f"k={FAMILY_K}, m={FAMILY_M}, classes={FAMILY_CLASSES}"
    )
    print(f"primary exceptional core digits={len(FAMILY_EXCEPTIONAL_CORE)}")
    print(f"former-primary X156 barrier={X156_BARRIER}")
    print(f"former-primary X156 first threshold={X156_THRESHOLD}")
    print(f"former-primary X156 exceptional floor={X156_EXCEPTIONAL_FLOOR}")
    print(f"old contiguous barrier={OLD_CONTIGUOUS_BARRIER}")
    print(f"old sparse cap={OLD_SPARSE_CAP}")
    print(f"old sparse exceptions={OLD_SPARSE_EXCEPTIONS}")
    print(f"legacy certificate files={len(REQUIRED_LEGACY_FILES)}")
    print(f"primary structure files={len(FAMILY_STRUCTURE_FILES)}")


if __name__ == "__main__":
    check()
