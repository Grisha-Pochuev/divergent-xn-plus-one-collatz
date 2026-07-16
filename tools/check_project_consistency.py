#!/usr/bin/env python3
"""Check that compact durable project-memory files agree on the frontier."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRIMARY_X = "2^4501-349*2^500+347"
PRIMARY_CLASSES = "16562000"
PRIMARY_BARRIER = "10^1201"
GLOBAL_MIN_ORDINARY_BLOCKS = "245833"
POSITIVE_RETURN_FRONTIER = "2^3992"
NONPOSITIVE_RETURN_LOWER = "2^(2^974)"
NONPOSITIVE_CYCLE_UPPER = "2^4006"
CORRECT_CYCLE_RELATION = "2^A*product_i(n_i)==1 (mod X)"
RETRACTED_BARRIER = "10^37"

CREDIT_FRONTIER = "924679364903952241768234680715310598867316370441120757898246831506500507205080014535351439406991342585993538327845986892977536682537320095988153612270886695873966778097766981798062925612878469213187733241206117142814414961418054803443235355123715316220902421623921086365374327267387194352877014114959"
NEW_LENGTH_FRONTIER = "2^4988"

EXCLUSION_DOC = "NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION"
EXCLUSION_TOOL = "verify_nonpositive_return_block_correction_exclusion.py"
GLOBAL_PHASE_DOC = "GLOBAL_BLOCK_GCD_PHASE_SIEVE"
GLOBAL_PHASE_TOOL = "verify_global_block_gcd_phase_sieve.py"
SAME_DEFICIT_TOOL = "verify_same_deficit_finite_persistence.py"
BALLOT_TOOL = "verify_minimum_block_boundary_credit_ballot.py"
PURE_EXIT_TOOL = "verify_minimum_block_boundary_pure_ordinary_exit.py"
SPONSOR_ARCH_DOC = "EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT"
SPONSOR_ARCH_TOOL = "verify_exceptional_sponsor_arch_macro_exit.py"
DELTA_DOC = "PRIMARY_DELTA_TWO_BIT_SHARPENING"
DELTA_TOOL = "verify_primary_delta_two_bit_sharpening.py"
STRIP_DOC = "PRIMARY_ONE_OVER_1007_CYCLE_STRIP"
STRIP_TOOL = "verify_primary_one_over_1007_cycle_strip.py"
CREDIT_DOC = "PRIMARY_CREDIT_CONTINUED_FRACTION_FRONTIER"
CREDIT_TOOL = "verify_primary_credit_continued_fraction_frontier.py"

CORE_FILES = (
    "START_HERE.md",
    "docs/WORKING_PROTOCOL.md",
    "docs/CURRENT_STATUS.md",
    "docs/RETRACTIONS.md",
    "docs/LATEST_VALID_PROGRESS.md",
    "docs/archive/LEGACY_LATEST_VALID_PROGRESS_PRE_NEAR_POWER.md",
)

CURRENT_FILES = (
    "docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md",
    "tools/verify_near_power_cycle_block_ledger.py",
    "docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md",
    "tools/verify_nonpositive_return_block_correction_exclusion.py",
    "docs/MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md",
    "tools/verify_minimum_block_boundary_credit_ballot.py",
    "docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md",
    "tools/verify_minimum_block_boundary_pure_ordinary_exit.py",
    "docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md",
    "tools/verify_exceptional_sponsor_arch_macro_exit.py",
    "docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md",
    "tools/verify_primary_delta_two_bit_sharpening.py",
    "docs/PRIMARY_ONE_OVER_1007_CYCLE_STRIP.md",
    "tools/verify_primary_one_over_1007_cycle_strip.py",
    "docs/PRIMARY_CREDIT_CONTINUED_FRACTION_FRONTIER.md",
    "tools/verify_primary_credit_continued_fraction_frontier.py",
    "docs/CYCLIC_ROTATION_CLOSURE_GCD.md",
    "tools/verify_cyclic_rotation_closure_gcd.py",
    "docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md",
    "tools/verify_global_block_gcd_phase_sieve.py",
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
    for relative in CORE_FILES + CURRENT_FILES:
        read(relative)

    require(
        "START_HERE.md",
        "docs/WORKING_PROTOCOL.md",
        "docs/CURRENT_STATUS.md",
        PRIMARY_X,
        "G3 all nontrivial positive cycles excluded: open",
        PRIMARY_CLASSES,
        GLOBAL_MIN_ORDINARY_BLOCKS,
        POSITIVE_RETURN_FRONTIER,
        NONPOSITIVE_RETURN_LOWER,
        NONPOSITIVE_CYCLE_UPPER,
        EXCLUSION_DOC,
        EXCLUSION_TOOL,
        SPONSOR_ARCH_DOC,
        SPONSOR_ARCH_TOOL,
        DELTA_DOC,
        DELTA_TOOL,
        STRIP_DOC,
        STRIP_TOOL,
        CREDIT_DOC,
        CREDIT_TOOL,
        CREDIT_FRONTIER,
        NEW_LENGTH_FRONTIER,
        "remaining actual return",
        CORRECT_CYCLE_RELATION,
    )

    require(
        "docs/WORKING_PROTOCOL.md",
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
        "every nonpositive return is",
        "Strongest current exit-return decomposition",
        EXCLUSION_DOC,
        EXCLUSION_TOOL,
        SPONSOR_ARCH_DOC,
        SPONSOR_ARCH_TOOL,
        DELTA_DOC,
        DELTA_TOOL,
        STRIP_DOC,
        STRIP_TOOL,
        CREDIT_DOC,
        CREDIT_TOOL,
        CREDIT_FRONTIER,
        NEW_LENGTH_FRONTIER,
        GLOBAL_PHASE_DOC,
        "S_h/g divides 2^D-1",
        "S_h/gcd(S_h,2^D-1) divides g divides S_h",
        "n_t==B^(-j)*S_j (mod g)",
        "fixed finite `N`-adic ladders",
        CORRECT_CYCLE_RELATION,
    )

    require(
        "docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md",
        "canonical sponsor arch",
        "0<=C<=m-2",
        "Laminarity",
        "L < 2*C*B*X/[d*(X-d)]",
        "L_macro<2^4006",
        "The theorem does not exclude the final positive-credit return",
    )

    require(
        "tools/verify_exceptional_sponsor_arch_macro_exit.py",
        "sponsor_arches",
        "maximal_arches",
        "verify_small_ballot_ledgers",
        "verify_local_segment_bound_grid",
        "small positive-prefix ledgers",
        "maximal sponsor arches are laminar",
    )

    require(
        "docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md",
        "delta<2^-3992",
        "349/511<11/16",
        "56/81>11/16",
        "L>C*2^3992",
        "L_return>R*2^3992",
    )

    require(
        "tools/verify_primary_delta_two_bit_sharpening.py",
        "verify_rational_drift_bound",
        "verify_segment_consequences",
        "delta=log2(B/X) < 2^-3992",
        "L > C*2^3992",
    )

    require(
        "docs/PRIMARY_ONE_OVER_1007_CYCLE_STRIP.md",
        "1007*2^-4002",
        "1008*2^-4002",
        "1/1007<0.001",
        "Gate G3 therefore remains open",
    )

    require(
        "tools/verify_primary_one_over_1007_cycle_strip.py",
        "verify_primary_drift_bracket",
        "D*2^4002/1008 < p < D*2^4002/1007",
    )

    require(
        "docs/PRIMARY_CREDIT_CONTINUED_FRACTION_FRONTIER.md",
        CREDIT_FRONTIER,
        "p<2^4991",
        "p>2^4988",
        "Gate G3 remains open",
    )

    require(
        "tools/verify_primary_credit_continued_fraction_frontier.py",
        "CF_COUNT = 554",
        "coefficients[553] == 36",
        CREDIT_FRONTIER,
        "gap_lower > total_correction_upper",
    )

    require(
        "docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md",
        "p < 2*D*B*X/[d*(X-d)]",
        "A hypothetical positive cycle cannot have R<=0",
        "strict prize problem is not yet solved",
    )

    require(
        "docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md",
        "S_h/g divides 2^D-1",
        "S_h/gcd(S_h,2^D-1) divides g divides S_h",
        "n_t==B^(-j)*S_j (mod g)",
        "43 -> 27 -> 17 -> 43",
    )

    require(
        "docs/SAME_DEFICIT_FINITE_PERSISTENCE_NO_GO.md",
        "d*x_j==2^e (mod X)",
        "x_j==2^(e-1) (mod N)",
        "arbitrary finite same-deficit",
        "does not prove divergence",
    )

    checks = read("run_checks.py")
    for tool in (
        EXCLUSION_TOOL,
        GLOBAL_PHASE_TOOL,
        SAME_DEFICIT_TOOL,
        BALLOT_TOOL,
        PURE_EXIT_TOOL,
        SPONSOR_ARCH_TOOL,
        DELTA_TOOL,
        STRIP_TOOL,
        CREDIT_TOOL,
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
    print(f"credit frontier digits={len(CREDIT_FRONTIER)}")
    print(f"positive-cycle length frontier={NEW_LENGTH_FRONTIER}")
    print(f"nonpositive-return lower={NONPOSITIVE_RETURN_LOWER}")
    print(f"nonpositive-cycle upper={NONPOSITIVE_CYCLE_UPPER}")
    print("sponsor-arch macro decomposition=active")
    print("nonpositive-return branch=excluded")
    print("only surviving branch=enormous positive-credit return")
    print("strict prize target=open")


if __name__ == "__main__":
    check()
