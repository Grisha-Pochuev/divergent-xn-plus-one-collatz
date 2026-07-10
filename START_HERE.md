# START HERE

This file is the durable entry point for every new work session on this repository.

## Strict target

Find explicit positive odd integers

```text
X >= 5,
n0 >= 1,
```

such that the accelerated odd-only map

```text
C_X(n) = (X*n + 1) / 2^v2(X*n+1)
```

satisfies

```text
C_X^t(n0) -> +infinity.
```

A nontrivial cycle or merely avoiding `1` does **not** solve the strict target.

## Read these files first

1. `START_HERE.md`
2. `docs/CURRENT_STATUS.md`
3. `docs/VALIDATED_RESULTS.md`
4. `docs/RETRACTIONS.md`
5. `docs/NEXT_STEPS.md`
6. `run_checks.py`

Do not rely on claims marked as retracted, superseded, heuristic, or unverified.

## Current strongest fixed candidate

```text
X  = 104350542602662257699,
n0 = 1.
```

Retained rigorous conclusions:

- the orbit leaves `1` and cannot return to `1`;
- any nontrivial cycle reached by it contains only values at least `25`;
- no nontrivial positive cycle of accelerated length at most

```text
176022359338834903228
```

can occur.

Therefore this orbit either tends to positive infinity or enters a nontrivial cycle longer than the retained finite barrier. This is not yet a proof of divergence.

Primary barrier certificate:

```text
docs/TRANSITION_BUDGET_CYCLE_BARRIER.md
tools/verify_transition_budget_barrier.py
```

## Priority 1 transition results

Let

```text
M = 15099,
ord_M(2) = 2154.
```

The following are now proved:

1. The directed graph on the `2154` allowed output classes is complete, including loops. Every finite class word is realizable by some positive start. Therefore the bare class labels cannot yield forbidden edges or forbidden short words.
2. If `c_t` is the number of cycle elements in class `t`, then every hypothetical cycle of length `p` satisfies

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

3. Cycle closure forces exact flow balance: the number of elements whose current class is `t` equals the number of outgoing steps whose target class is `t`.
4. Combining the valuation-cost bound with residue crowding gives the retained barrier above.

Structural files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
docs/RESIDUE_VALUATION_BUDGET.md
tools/verify_residue_valuation_budget.py
docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md
tools/verify_transition_balance.py
```

Fair numerical comparison: the old independent-class envelope, if saturated with the same rational bounds, reaches `176022359338834903224`; the transition budget adds exactly `4` further lengths. The larger approximately `3.54%` increase is relative to the previously recorded round barrier `170000000000000000000`.

## Critical retraction

The former claimed cycle barrier `10^37` is invalid and retracted. It used the false cycle condition

```text
2^A == 1 (mod X).
```

The correct congruence is

```text
2^A * product_i(n_i) == 1 (mod X).
```

The accelerated `5n+1` cycle

```text
13 -> 33 -> 83 -> 13
```

is a regression counterexample to the false condition. Never reintroduce the discarded order argument.

## Working rules

1. GitHub files, not chat history, are the source of durable project memory.
2. Work on one major route per session.
3. Separate proved statements from heuristics and computational observations.
4. Before announcing a theorem:
   - derive it independently a second time;
   - test it against known small cycles;
   - add an exact verifier or unit test where practical;
   - run the retained checks;
   - update the project status files.
5. Do not run long CPU searches in ChatGPT sessions. Use exact arithmetic, symbolic work, and short checks. Any large external computation requires explicit user approval.
6. A long finite trajectory is evidence only, never a proof of divergence.
7. A finite cycle barrier, however large, is not an infinite barrier.

## Required end-of-session checkpoint

Before finishing a substantial work session, record:

- what was rigorously proved;
- what remains conjectural;
- any failed or retracted approach;
- files and commit SHAs changed;
- the exact next mathematical step;
- a conservative progress estimate, clearly labelled subjective.

## Reproduction

Run

```text
python run_checks.py
```

to execute the retained certificates and regression audits. Individual lightweight certificates may also be run directly from `tools/`.
