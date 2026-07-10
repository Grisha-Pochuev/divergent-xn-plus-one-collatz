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
170000000000000000000
```

can occur.

Therefore this orbit either tends to positive infinity or enters a nontrivial cycle longer than the retained finite barrier. This is not yet a proof of divergence.

Primary certificate:

```text
docs/RESIDUE_CROWDING_CYCLE_BARRIER.md
tools/verify_residue_crowding_barrier.py
```

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
