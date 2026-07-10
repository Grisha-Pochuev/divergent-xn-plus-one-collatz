# The Open Mathematics Project

## Divergent accelerated `Xn+1` orbit

This repository is an open, reproducible research project about the following problem. For an odd integer `X >= 5`, define the accelerated odd-only map

```text
C_X(n) = (X*n + 1) / 2^v2(X*n + 1),
```

where `n` is a positive odd integer. The strict target is to find at least one explicit pair `(X,n0)` for which

```text
C_X^t(n0) -> +infinity.
```

A nontrivial cycle avoiding `1`, a long finite trajectory, or an arbitrarily large finite cycle barrier is not treated as a solution.

This repository is part of **The Open Mathematics Project**: a public workflow for attacking open mathematical problems with human direction, AI-assisted reasoning, reproducible computation, and independent verification.

## Start here

Every new work session should read these files in order:

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
run_checks.py
```

A ready-to-copy new-chat prompt is stored in:

```text
docs/CHAT_HANDOFF_TEMPLATE.md
```

GitHub files, not chat history, are the durable source of project truth.

## Current strongest retained result

**The strict problem is not solved.** No explicit positive orbit has yet been proved to tend to infinity.

The strongest retained fixed candidate is

```text
X  = 104350542602662257699,
n0 = 1.
```

For this pair the repository rigorously proves:

1. the orbit leaves `1` and cannot return to `1`;
2. every element of any nontrivial cycle reached by the orbit is at least `25`;
3. no nontrivial positive cycle of accelerated length at most

```text
170000000000000000000
```

can occur.

Therefore the orbit either tends to positive infinity or enters a nontrivial positive cycle longer than this finite barrier.

The current barrier uses `2154` allowed output residue classes modulo `2*15099`, distinctness of cycle elements, and exact rational interval bounds. It does not require a long trajectory simulation or heavy CPU search.

Primary files:

```text
docs/RESIDUE_CROWDING_CYCLE_BARRIER.md
tools/verify_residue_crowding_barrier.py
```

## Important retraction

A former claimed cycle barrier `10^37` is retracted. It incorrectly assumed that a cycle must satisfy

```text
2^A == 1 (mod X).
```

The correct congruence is

```text
2^A * product_i(n_i) == 1 (mod X).
```

The accelerated `5n+1` cycle `13 -> 33 -> 83 -> 13` is a regression counterexample to the discarded condition. See `docs/RETRACTIONS.md` and `docs/AUDIT_INVALID_ORDER_CONDITION.md`.

## Other retained structural results

The repository also contains:

- the exact accelerated iterate formula;
- an average-valuation sufficient criterion for exponential divergence;
- a finite repetition bound for every exact valuation block;
- a proof that eventually periodic exact valuations force an eventual cycle;
- exact coding of every finite valuation word;
- complete growing macroblocks for `X=2^m+1`;
- an arbitrary-core Fermat-burst reduction;
- a 2-adic isometry and unique finite-precision regeneration targets;
- an effective polynomial upper bound on the minimum element of a hypothetical cycle in terms of its length.

The authoritative list, with limitations, is `docs/VALIDATED_RESULTS.md`.

## Basic divergence criterion

Let

```text
a_t = v2(X*n_t+1),
A_N = a_0+...+a_(N-1).
```

Then

```text
n_N = [X^N*n_0 + sum_(j=0)^(N-1) X^(N-1-j)*2^(A_j)] / 2^(A_N),
```

and therefore

```text
n_N >= n_0 * X^N / 2^(A_N).
```

If, for some `epsilon>0` and all sufficiently large `N`,

```text
A_N/N <= log2(X)-epsilon,
```

then the orbit grows at least exponentially. The unresolved difficulty is proving such control for one explicit ordinary positive orbit.

## Reproducibility

No external Python packages are required for the retained core checks.

Run:

```bash
python run_checks.py
```

The suite includes the current residue-crowding certificate and a regression audit preventing the invalid cycle-order condition from being reintroduced.

Selected lightweight checks:

```bash
python tools/verify_residue_crowding_barrier.py
python tools/verify_continued_fraction_barrier.py
python tools/analyze_fermat_macroblock.py --m 3 --L 599 --k 0 --precision 17
```

The file named `verify_continued_fraction_barrier.py` is now an audit of the retracted argument, not a verifier of the discarded `10^37` claim.

## Repository layout

```text
START_HERE.md   Durable entry point for every work session.
docs/           Proof notes, status, audits, roadmap, and handoff material.
tools/          Exact integer implementations and verification scripts.
tests/          Independent tests and regression checks.
results/        Exploratory outputs, never treated as proof.
```

## Research principles

1. Separate proved statements from experiments and conjectures.
2. Never treat a long trajectory as proof of divergence.
3. Prefer finite, independently checkable certificates.
4. Record failed approaches and exact counterexamples.
5. Keep the checker smaller and simpler than the search procedure.
6. Do not launch long CPU searches without explicit approval.
7. Update the durable status files after every major result or retraction.

## References

- Ingo Althöfer, generalized Collatz prizes.
- Richard E. Crandall, *On the 3x+1 Problem* (1978).
- Zachary Franco and Carl Pomerance, *On a Conjecture of Crandall Concerning the qx+1 Problem* (1995).
- Alex V. Kontorovich and Jeffrey C. Lagarias, *Stochastic Models for the 3x+1 and 5x+1 Problems*.
- Jeffrey C. Lagarias, *The 3x+1 Problem: An Overview*.

## License

Code, notes, and reproducibility material are released under the MIT License.
