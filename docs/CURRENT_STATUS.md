# Current status

The strict target is to exhibit odd integers `X>=5` and `n0>=1` whose accelerated odd-only orbit tends to positive infinity.

## Main explicit candidate

The strongest fixed candidate currently proved in this repository is

```text
X  = 104350542602662257699,
n0 = 1.
```

For this pair we have proved:

1. the orbit leaves `1` and can never return to `1`;
2. every possible element of a nontrivial cycle reached by the orbit is at least `25`;
3. the orbit cannot enter a nontrivial positive cycle of accelerated odd length at most

```text
10^36.
```

Therefore the orbit satisfies the rigorous dichotomy

```text
it tends to +infinity,
```

or

```text
it enters a nontrivial positive cycle longer than 10^36 accelerated steps.
```

The new proof is a compact exact certificate, not a trajectory simulation. It uses:

- the exact order

```text
ord_X(2)=1860810887857924950;
```

- distinctness of cycle elements, which makes the logarithmic correction grow only harmonically with the cycle length;
- Legendre's continued-fraction theorem;
- exact rational intervals for `ln(2)` and `ln(X)`;
- elimination of all `18` possible upper convergents through denominator `10^36`.

See `CONTINUED_FRACTION_CYCLE_BARRIER.md` and `tools/verify_continued_fraction_barrier.py`.

This improves the previous fixed barrier

```text
148557456445856651509
```

by more than fifteen orders of magnitude.

## General arbitrary-barrier theorem

For every prescribed positive integer `B`, the repository gives an explicit construction of an odd multiplier `X_B` such that the orbit from `1`

1. never returns to `1`; and
2. cannot enter a nontrivial positive cycle of length at most `B`.

The multiplier changes with `B`, so this theorem alone does not solve the prize.

## Simultaneous length-and-height barriers

For every pair `(B,H)`, the repository gives an explicit multiplier `X_(B,H)` such that the orbit from `1`

1. never returns to `1`;
2. cannot enter a nontrivial cycle of length at most `B`;
3. cannot enter a nontrivial cycle containing a value at most `H`.

Again, the multiplier changes with `(B,H)`.

## Exact valuation-word coding theorem

For every finite exact valuation word

```text
a=(a_0,...,a_(N-1)),
A=sum a_i,
```

there is exactly one residue class modulo `2^(A+1)` whose positive representatives follow that word. Writing

```text
B = sum_(j=0)^(N-1) X^(N-1-j) * 2^(a_0+...+a_(j-1)),
```

the class is

```text
r(a) == (2^A-B)*(X^N)^(-1)  (mod 2^(A+1)).
```

Consequences:

1. every finite valuation word is realized by infinitely many positive odd starts;
2. if `A/N<log2(X)`, every positive representative has net growth across the word;
3. compatible coding classes of an infinite word define one 2-adic integer;
4. they come from an ordinary nonnegative integer exactly when their least representatives eventually stabilize.

Thus arbitrarily long finite growth is locally automatic. The global obstruction is stabilization at one ordinary integer while preserving positive average drift.

## Other established structural results

1. Exact implementation of the accelerated map and exact iterate formula.
2. The sufficient average-valuation criterion for exponential divergence.
3. Arbitrarily long rigorously increasing finite orbit segments for `X=2^m+1`.
4. A finite repetition bound for every exact valuation block.
5. An eventually periodic sequence of exact halving counts forces an eventually periodic integer orbit.
6. The complete `X=2^m+1` macroblock formula, including the exceptional exit.
7. Complete macroblocks whose net growth survives the exceptional exit.
8. A 2-adic isometry theorem and a unique finite regeneration target at every precision.
9. Exact coordinate normal forms around `n=-1` for `X=2^m+1` and around `n=1` for `X=2^m-1`.
10. The positive-integer orbit dichotomy: every orbit is either eventually periodic or tends to positive infinity.
11. For `(X,n0)=(1093,1)`, the orbit never returns to `1`.
12. Exact inverse coding of every finite valuation word.
13. A continued-fraction exclusion of every nontrivial cycle of length at most `10^36` for the main fixed candidate.

## Literature audit

A published claim that Mersenne multipliers have only the trivial positive cycle cannot currently be used: a key lemma has the counterexample

```text
m=3, q=7, k=9, c=2:
7 divides 9*2^2-1=35,
```

although `9` is not a power of two. See `LITERATURE_AUDIT_SANTOS.md`.

## Not established

- No explicit orbit has yet been proved to tend to infinity.
- Cycles longer than `10^36` have not been excluded for the main fixed candidate.
- An arbitrarily large finite barrier is not an infinite barrier.
- The finite 2-adic regeneration targets have not been converted into one ordinary positive integer supporting infinitely many regenerations.
- No low-average infinite valuation word with an eventually stable positive coding residue has yet been constructed.

## Current frontier

### Route A: finish the explicit candidate

For

```text
X=104350542602662257699,
n0=1,
```

exclude every nontrivial positive cycle, not only cycles through `10^36`. The current continued-fraction method reduces all shorter cycles to finitely many exact rational checks. A completion needs either:

1. a global irrationality-measure estimate strong enough to dominate the harmonic cycle correction for every denominator; or
2. a modular/descent argument excluding all remaining continued-fraction candidates.

### Route B: infinite regenerative chain

For `X=2^m+1`, turn the exact macroblock and 2-adic regeneration formulas into one ordinary positive starting integer with an infinite aperiodic chain of net-positive blocks.

### Route C: stabilized low-average code

Construct an aperiodic infinite valuation word whose prefix averages stay below `log2(X)` and whose coding residues eventually stabilize at a positive integer.

Any of these routes would finish the strict prize problem.

## Reproducibility

Run

```text
python run_checks.py
```

to execute all direct tests and principal finite certificates. The strongest fixed certificate is also checked separately by

```text
python tools/verify_continued_fraction_barrier.py
```
