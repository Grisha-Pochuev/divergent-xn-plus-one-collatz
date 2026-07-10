# The Open Mathematics Project

## Divergent accelerated `Xn+1` orbit

This repository is an open, reproducible research project about the following problem. For an odd integer `X >= 5`, define the accelerated odd-only map

```text
C_X(n) = (X*n + 1) / 2^v2(X*n + 1),
```

where `n` is a positive odd integer. The target is to find at least one explicit pair `(X,n0)` for which

```text
C_X^t(n0) -> +infinity.
```

This is the strict working version of Ingo Althöfer's first generalized-Collatz prize problem. A non-trivial cycle avoiding `1` is not treated as a divergent orbit.

This repository is part of **The Open Mathematics Project**: a public workflow for attacking open mathematical problems with human direction, AI-assisted reasoning, reproducible computation, and independent verification.

## Current status

**The problem is not solved in this repository.** No explicit infinite divergent positive orbit has yet been proved.

The present checkpoint contains:

- the exact accelerated map and independent tests;
- the exact iterate formula and average-valuation divergence criterion;
- a finite repetition bound for every exact valuation block;
- a proof that eventually periodic halving counts force an eventual cycle;
- a complete macroblock theorem for `X=2^m+1`, including the exceptional exit;
- a sufficient condition under which the complete macroblock still has net growth;
- an exact 2-adic isometry describing how much precision the endpoint regenerates;
- a unique regeneration target modulo every power of two;
- reproducible search and checking tools.

The main unresolved step is to turn arbitrarily accurate finite regeneration into one ordinary positive orbit that regenerates indefinitely.

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

then the orbit grows at least exponentially.

## Periodic-valuation obstruction

An exact valuation block cannot repeat forever on a divergent positive orbit. More generally, if the sequence

```text
v2(X*n_t+1)
```

is eventually periodic, then the integer orbit itself is eventually periodic.

See `docs/PERIODIC_VALUATION_OBSTRUCTION.md` and `tools/analyze_periodic_block.py`.

## Complete macroblock result for `X=2^m+1`

For

```text
X=2^m+1,
n0=2^(mL)-1,
k=v2(L),
```

the exact endpoint after the whole `L`-step macroblock, including its exceptional last division, is

```text
E_m(L) = (X^L-1)/2^(m+k).
```

If

```text
L*log2(1+2^(-m)) > m+v2(L)+1,
```

then

```text
E_m(L) > n0.
```

Thus the accumulated gain can survive the exceptional exit.

Writing `L=2^k*u` with odd `u`, the endpoint map is a 2-adic isometry:

```text
v2(E(u)-E(v)) = v2(u-v).
```

Consequently, for every precision `S`, there is exactly one odd class `u mod 2^S` for which

```text
E(u) == -1 mod 2^S.
```

This turns the next stage from blind trajectory search into an exact lifting problem. See `docs/FERMAT_MACROBLOCK_REGENERATION.md` and `tools/analyze_fermat_macroblock.py`.

## Reproducibility

No external Python packages are required.

Run all checks:

```bash
python run_checks.py
```

Verify the new macroblock examples:

```bash
python tools/analyze_fermat_macroblock.py --m 3 --L 599 --k 0 --precision 17
python tools/analyze_fermat_macroblock.py --m 4 --L 78 --k 1 --precision 10
```

Generate trajectory statistics:

```bash
python tools/trajectory_report.py --X 5 --n0 7 --steps 10000
```

## Repository layout

```text
docs/       Proof notes, current frontier, and reproducibility.
tools/      Exact integer implementation and verification scripts.
tests/      Independent tests for the map and proved identities.
results/    Exploratory outputs, never treated as proof.
```

## Research principles

1. Separate proved statements from experiments and conjectures.
2. Never treat a long trajectory as proof of divergence.
3. Prefer finite, independently checkable certificates.
4. Record failed approaches so they are not rediscovered.
5. Keep the checker smaller and simpler than the search procedure.

## References

- Ingo Althöfer, generalized Collatz prizes.
- Richard E. Crandall, *On the 3x+1 Problem* (1978).
- Zachary Franco and Carl Pomerance, *On a Conjecture of Crandall Concerning the qx+1 Problem* (1995).
- Alex V. Kontorovich and Jeffrey C. Lagarias, *Stochastic Models for the 3x+1 and 5x+1 Problems*.
- Jeffrey C. Lagarias, *The 3x+1 Problem: An Overview*.

## License

Code, notes, and reproducibility material are released under the MIT License.
