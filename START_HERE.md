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
177780727155637125184
```

can occur;
- more strongly, every length at most

```text
355561454311274250377
```

is impossible except the following six odd values:

```text
177780727155637125185
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

Therefore the orbit either tends to positive infinity or enters a nontrivial cycle longer than the contiguous barrier. If its cycle length is at most the larger sparse cap, it must be one of the six displayed values. This is not yet a proof of divergence.

Primary current certificates:

```text
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
```

## Priority 1 transition results

Let

```text
M = 15099,
ord_M(2) = 2154,
P = 6911089648497401,
X = M*P.
```

The following are proved:

1. The directed graph on the `2154` allowed output classes is complete, including loops. Every finite class word is realizable by infinitely many positive starts.
2. This no-go theorem remains true after retaining any prescribed finite word of exact valuations, including the layer `q=(a-t)/2154`. Local forbidden-word searches cannot solve the problem.
3. If `c_t` is the number of cycle elements in class `t`, then every hypothetical cycle of length `p` satisfies

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

4. Cycle closure forces exact source/target flow balance.
5. A balanced occupancy dual certificate reduces the reciprocal envelope from about `3.820166` to about `3.217731`.
6. Splitting incoming exact valuations using the large divisor `P` reduces it further; the midpoint refinement used for the first exceptional length gives about `2.527289`.
7. Exact global closure identities hold:

```text
sum_i (2^a_(i-1)-X)*n_i = p,

sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

Structural files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
docs/AUGMENTED_TRANSITION_NO_GO.md
docs/RESIDUE_VALUATION_BUDGET.md
docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md
docs/BALANCED_OCCUPANCY_DUAL_BOUND.md
docs/LARGE_DIVISOR_VALUATION_SPLIT.md
docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md
```

## Exact next mathematical step

Attack the six remaining odd lengths directly. The preferred route is to combine their fixed total valuation with the two global transition-balance identities and full-`X` valuation costs. Do not return to local forbidden-edge or bounded-window enumeration: the augmented no-go theorem proves that every compatible finite word is realizable.

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
7. A finite or sparse cycle barrier, however large, is not an infinite barrier.

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

to execute the retained certificates and regression audits. Individual certificates may also be run directly from `tools/`.