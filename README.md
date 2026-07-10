# The Open Mathematics Project

## Divergent accelerated `Xn+1` orbit

This repository is an open, reproducible research project about the following problem.
For an odd integer `X >= 5`, define the accelerated odd-only map

```text
C_X(n) = (X*n + 1) / 2^v2(X*n + 1),
```

where `n` is a positive odd integer and `v2(k)` is the exponent of `2` in `k`.
The target is to find at least one explicit pair `(X, n0)` for which

```text
C_X^t(n0) -> +infinity.
```

This is the strict working version of Ingo Althöfer's first generalized-Collatz prize problem.
A non-trivial cycle that avoids `1` is not treated here as a divergent orbit.

This repository is part of **The Open Mathematics Project**: a public workflow for attacking open mathematical problems with human direction, AI-assisted reasoning, reproducible computation, and independent verification.

## Current status

**The problem is not solved in this repository.**

The present checkpoint contains:

- the exact accelerated map and a small independent implementation;
- the standard exact iterate formula;
- a sufficient criterion for exponential divergence in terms of the average value of `v2(X*n+1)`;
- a proved structural lemma for `X = 2^m + 1`;
- a proved construction of arbitrarily long, but finite, strictly increasing orbit segments;
- reproducible exploratory trajectory statistics;
- a record of approaches that were tested and found insufficient.

The main unresolved step is to replace finite experiments by a finite certificate that controls an infinite orbit.

## Exact results recorded here

Let

```text
a_t = v2(X*n_t + 1),
A_N = a_0 + ... + a_(N-1).
```

Then

```text
n_N = [X^N*n_0 + sum_(j=0)^(N-1) X^(N-1-j)*2^(A_j)] / 2^(A_N).
```

In particular,

```text
n_N >= n_0 * X^N / 2^(A_N).
```

Therefore, if for some `epsilon > 0` and all sufficiently large `N`,

```text
A_N / N <= log2(X) - epsilon,
```

then the orbit grows at least exponentially.

For `X = 2^m + 1`, write `s = v2(n+1)`. Then

```text
v2(X*n+1) = s     if s < m,
v2(X*n+1) = m     if s > m,
v2(X*n+1) > m     if s = m.
```

The equality layer `s = m` is the only exceptional layer in this description.

Finally, for integers `m >= 2` and `L >= 2`, let

```text
X  = 2^m + 1,
n0 = 2^(m*L) - 1.
```

For `0 <= j <= L-1`,

```text
n_j = 2^(m*(L-j)) * X^j - 1,
```

and the first `L-1` accelerated steps have exactly `v2(X*n_j+1)=m` and are strictly increasing. This proves the existence of rigorously controlled increasing segments of any prescribed finite length. It does **not** prove an infinite divergent orbit.

## Reproducibility

No external Python packages are required.

Run all checks:

```bash
python run_checks.py
```

Generate trajectory statistics:

```bash
python tools/trajectory_report.py --X 5 --n0 7 --steps 10000
python tools/trajectory_report.py --X 1048577 --n0 5 --steps 10000
```

Verify a finite-growth block:

```bash
python tools/verify_finite_growth_block.py --m 20 --L 50
```

See `docs/REPRODUCIBILITY.md` for details.

## Repository layout

```text
docs/       Problem statement, current frontier, research notes, reproducibility.
tools/      Exact integer implementation and verification scripts.
tests/      Independent unit tests for the map and proved identities.
results/    Small reproducible exploratory outputs; never treated as proof.
```

## Research principles

1. Separate proved statements from experiments and conjectures.
2. Do not treat a long trajectory as proof of divergence.
3. Prefer finite, independently checkable certificates.
4. Record failed approaches so they are not repeatedly rediscovered.
5. Keep the checker smaller and simpler than the search procedure.

## References

- Ingo Althöfer, generalized Collatz prizes: https://althofer.de/collatz-prizes.html
- Richard E. Crandall, *On the 3x+1 Problem* (1978).
- Zachary Franco and Carl Pomerance, *On a Conjecture of Crandall Concerning the qx+1 Problem* (1995).
- Alex V. Kontorovich and Jeffrey C. Lagarias, *Stochastic Models for the 3x+1 and 5x+1 Problems*.
- Jeffrey C. Lagarias, *The 3x+1 Problem: An Overview*.

## License

Code, notes, and reproducibility material are released under the MIT License.
