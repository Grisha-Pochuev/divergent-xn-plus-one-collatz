#!/usr/bin/env python3
"""Check that compact durable project-memory files agree on the frontier."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRIMARY_X = "2^4501-349*2^500+347"
PRIMARY_CLASSES = "16562000"
PRIMARY_BARRIER = "10^1201"
GLOBAL_MIN_ORDINARY_BLOCKS = "245833"
POSITIVE_RETURN_FRONTIER = "2^3990"
NONPOSITIVE_RETURN_LOWER = "2^(2^974)"
NONPOSITIVE_CYCLE_UPPER = "2^4006"
EXCLUSION_DOC = "NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION"
EXCLUSION_TOOL = "verify_nonpositive_return_block_correction_exclusion.py"
GLOBAL_PHASE_DOC = "GLOBAL_BLOCK_GCD_PHASE_SIEVE"
GLOBAL_PHASE_TOOL = "verify_global_block_gcd_phase_sieve.py"
SAME_DEFICIT_DOC = "SAME_DEFICIT_FINITE_PERSISTENCE_NO_GO"
SAME_DEFICIT_TOOL = "verify_same_deficit_finite_persistence.py"
GLOBAL_DIVISOR_MARKER = "S_h/g divides 2^D-1"
PHASE_MARKER = "n_t==B^(-j)*S_j (mod g)"
CORRECT_CYCLE_RELATION = "2^A*product_i(n_i)==1 (mod X)"
RETRACTED_BARRIER = "10^37"

CORE_MEMORY_FILES = (
    "START_HERE.md",
    "docs/WORKING_PROTOCOL.md",
    "docs/CURRENT_STATUS.md",
    "docs/RETRACTIONS.md",
)

HISTORICAL_FILES = (
    "docs/SESSION_CHECKPOINT_2026-07-13_GLOBAL_BLOCK_GCD_PHASE_SIEVE.md",
    "docs/LATEST_VALID_PROGRESS.md",
    "docs/archive/LEGACY_LATEST_VALID_PROGRESS_PRE_NEAR_POWER.md",
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
    "docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md",
    "tools/verify_near_power_cycle_block_ledger.py",
    "docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md",
    "tools/verify_nonpositive_return_block_correction_exclusion.py",
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
    "docs/ODD_H_PHASE_HARMONIC_BARRIER.md",
    "tools/verify_odd_h_phase_harmonic_barrier.py",
    "docs/NONPOSITIVE_RETURN_ORDINARY_BLOCK_EXPLOSION.md",
    "tools/verify_nonpositive_return_ordinary_block_explosion.py",
    "docs/SAME_DEFICIT_FINITE_PERSISTENCE_NO_GO.md",
    "tools/verify_same_deficit_finite_persistence.py",
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
    for relative in CORE_MEMORY_FILES + HISTORICAL_FILES + CURRENT_STRUCTURE_FILES:
        read(relative)

    require(
        "START_HERE.md",
        "docs/WORKING_PROTOCOL.md",
        "docs/CURRENT_STATUS.md",
        PRIMARY_X,
        "G3 all nontrivial positive cycles excluded: open",
        POSITIVE_RETURN_FRONTIER,
        NONPOSITIVE_RETURN_LOWER,
        NONPOSITIVE_CYCLE_UPPER,
        EXCLUSION_DOC,
        EXCLUSION_TOOL,
        "The only surviving branch is now",
        CORRECT_CYCLE_RELATION,
    )

    require(
        "docs/WORKING_PROTOCOL.md",
        "START_HERE.md",
        "docs/CURRENT_STATUS.md",
        "one primary proof target",
        "at most two active exploratory directions",
        "Run the new standalone checker first",
        "Prefer one coherent result commit per sprint",
        "docs/LATEST_VALID_PROGRESS.md",
    )

    require(
        "docs/CURRENT_STATUS.md",
        PRIMARY_X,
        PRIMARY_CLASSES,
        PRIMARY_BARRIER,
        GLOBAL_MIN_ORDINARY_BLOCKS,
        POSITIVE_RETURN_FRONTIER,
        NONPOSITIVE_RETURN_LOWER,
        NONPOSITIVE_CYCLE_UPPER,
        "R<=0 is impossible",
        "Only surviving return branch",
        EXCLUSION_DOC,
        EXCLUSION_TOOL,
        GLOBAL_PHASE_DOC,
        GLOBAL_PHASE_TOOL,
        GLOBAL_DIVISOR_MARKER,
        "S_h/gcd(S_h,2^D-1) divides g divides S_h",
        PHASE_MARKER,
        "fixed finite `N`-adic depth",
        CORRECT_CYCLE_RELATION,
    )

    require(
        "docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md",
        "p < 2*D*B*X/[d*(X-d)]",
        "2*4500*B*X < 2^4006*d*(X-d)",
        "A hypothetical positive cycle cannot have R<=0",
        POSITIVE_RETURN_FRONTIER,
        "strict prize problem is not yet solved",
    )

    require(
        "tools/verify_nonpositive_return_block_correction_exclusion.py",
        "verify_block_correction_grid",
        "verify_primary_exclusion",
        "nonpositive_return_excluded",
        "strict_prize_solution",
    )

    require(
        "docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md",
        GLOBAL_DIVISOR_MARKER,
        "S_h/gcd(S_h,2^D-1) divides g divides S_h",
        PHASE_MARKER,
        "43 -> 27 -> 17 -> 43",
    )

    require(
        "tools/verify_global_block_gcd_phase_sieve.py",
        "gcd_checks_D_1_to_4500",
        "conditional_full_cycle_frontier",
        "conditional_return_frontier",
        "small_cycles_checked",
    )

    require(
        "docs/SAME_DEFICIT_FINITE_PERSISTENCE_NO_GO.md",
        "d*x_j==2^e (mod X)",
        "x_j==2^(e-1) (mod N)",
        "arbitrary finite same-deficit",
        "does not prove divergence",
    )

    require(
        "tools/verify_same_deficit_finite_persistence.py",
        "construct_instance",
        "verify_primary_depth_ladder",
        "small same-deficit constructions",
    )

    checks = read("run_checks.py")
    for tool in (
        EXCLUSION_TOOL,
        GLOBAL_PHASE_TOOL,
        SAME_DEFICIT_TOOL,
    ):
        if tool not in checks:
            raise AssertionError(f"run_checks.py does not include {tool}")

    require(
        "docs/RETRACTIONS.md",
        RETRACTED_BARRIER,
        CORRECT_CYCLE_RELATION,
        "least-source endpoint identification",
    )

    require(
        "docs/LATEST_VALID_PROGRESS.md",
        "docs/CURRENT_STATUS.md",
        "not the current source",
        RETRACTED_BARRIER,
        "docs/archive/LEGACY_LATEST_VALID_PROGRESS_PRE_NEAR_POWER.md",
    )

    require(
        "docs/archive/LEGACY_LATEST_VALID_PROGRESS_PRE_NEAR_POWER.md",
        "104350542602662257699",
        "older candidate",
    )

    print("compact project-memory consistency verified")
    print("startup files=3")
    print(f"primary candidate={PRIMARY_X}")
    print(f"global ordinary-block minimum={GLOBAL_MIN_ORDINARY_BLOCKS}")
    print(f"positive-return frontier={POSITIVE_RETURN_FRONTIER}")
    print(f"nonpositive-return lower={NONPOSITIVE_RETURN_LOWER}")
    print(f"nonpositive-cycle upper={NONPOSITIVE_CYCLE_UPPER}")
    print("nonpositive-return branch=excluded")
    print("only surviving branch=positive-credit return")
    print("strict prize target=open")


if __name__ == "__main__":
    check()
