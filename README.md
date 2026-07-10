# The Open Mathematics Project

## Divergent accelerated `Xn+1` orbit

For an odd integer `X>=5`, define

```text
C_X(n) = (X*n + 1) / 2^v2(X*n + 1)
```

on positive odd integers. The strict target is one explicit pair `(X,n0)` for which

```text
C_X^t(n0) -> +infinity.
```

A cycle avoiding `1`, a long finite trajectory, or an arbitrarily large finite cycle barrier is not a solution.

This repository is part of **The Open Mathematics Project**: public AI-assisted mathematical research designed for reproducibility and independent verification.

## Start here

Read:

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
run_checks.py
```

GitHub files, not chat history, are the durable source of truth.

## Current strongest retained result

**The strict problem is not solved.** The strongest fixed candidate is

```text
X  = 104350542602662257699,
n0 = 1.
```

The repository rigorously proves:

1. the orbit leaves `1` and cannot return to `1`;
2. every element of a nontrivial cycle reached by it is at least `25`;
3. no nontrivial positive cycle has length

```text
p <= 177780727155637125184;
```

4. up to

```text
p <= 355561454311274250377,
```

all cycle lengths are excluded except six odd values:

```text
177780727155637125185
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

Thus the fixed orbit either tends to positive infinity or enters a nontrivial positive cycle. If the cycle length is within the larger sparse range, it must be one of the six listed values.

Primary certificates:

```text
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
```

## Priority 1 findings

Use

```text
M = 15099,
ord_M(2) = 2154,
X = M * 6911089648497401.
```

The following are retained:

- the graph on the `2154` allowed output classes is complete, including loops;
- every compatible finite word remains realizable even when exact valuations and finite height layers are retained;
- hypothetical cycle occupancies satisfy

```text
sum c_t=p,
sum t*c_t<=67p-1;
```

- cycle closure gives exact source/target flow balance;
- the large divisor of `X` places outputs with fixed incoming valuation in sparse progressions;
- exact logarithm intervals cross the first near-power-of-two window;
- the first of seven isolated exceptional lengths is eliminated;
- every cycle satisfies

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

The exact next target is to use these global identities to eliminate the remaining six lengths.

## Important retraction

A former claimed barrier `10^37` is retracted. It incorrectly assumed

```text
2^A == 1 (mod X).
```

The correct congruence is

```text
2^A * product_i(n_i) == 1 (mod X).
```

The accelerated `5n+1` cycle `13 -> 33 -> 83 -> 13` is the preserved regression counterexample.

## Other retained structures

The repository also contains:

- the exact accelerated iterate formula;
- an average-valuation sufficient criterion for exponential divergence;
- exact finite valuation-word coding;
- a finite repetition bound for every exact valuation block;
- Fermat-type growing macroblocks and finite macroblock programs;
- a 2-adic regeneration isometry;
- an effective polynomial upper bound on the minimum element of a hypothetical cycle;
- the bare and augmented transition no-go theorems;
- balanced occupancy, large-divisor, sharp-logarithm, and sparse-window certificates.

See `docs/VALIDATED_RESULTS.md` for hypotheses and limitations.

## Reproducibility

No external Python packages are required for the retained checks.

Run:

```bash
python run_checks.py
```

Selected Priority 1 checks:

```bash
python tools/verify_balanced_occupancy_barrier.py
python tools/verify_augmented_transition_no_go.py
python tools/verify_large_divisor_split_barrier.py
python tools/verify_sharp_log_barrier.py
python tools/verify_first_sparse_cycle_window.py
python tools/verify_first_exception_elimination.py
python tools/verify_global_transition_identities.py
```

The five-million-step certificate enumerates modular inverse powers, not a Collatz trajectory or a broad parameter search.

## Repository layout

```text
START_HERE.md   Durable entry point.
docs/           Proof notes, status, audits, and roadmap.
tools/          Exact verification scripts.
tests/          Independent tests and regressions.
results/        Exploratory outputs, never treated as proof.
```

## Research principles

1. Separate proofs from experiments.
2. Never treat finite trajectory size as proof of divergence.
3. Prefer independently checkable exact certificates.
4. Preserve failed arguments and counterexamples.
5. Keep verifiers simpler than exploratory searches.
6. Do not launch long computations without explicit approval.

## References

- Ingo Althöfer, generalized Collatz prizes.
- Richard E. Crandall, *On the 3x+1 Problem* (1978).
- Zachary Franco and Carl Pomerance, *On a Conjecture of Crandall Concerning the qx+1 Problem* (1995).
- Alex V. Kontorovich and Jeffrey C. Lagarias, *Stochastic Models for the 3x+1 and 5x+1 Problems*.
- Jeffrey C. Lagarias, *The 3x+1 Problem: An Overview*.

## License

MIT.