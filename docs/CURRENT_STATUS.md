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
148,557,456,445,856,651,509.
```

Therefore the orbit satisfies the rigorous dichotomy

```text
it tends to +infinity,
```

or

```text
it enters a nontrivial positive cycle longer than
148,557,456,445,856,651,509 accelerated steps.
```

The proof is a compact exact certificate, not a simulation of that many steps. It uses a complete enumeration of the `2154` powers-of-two residue classes modulo `15099=3*7*719`, exact integer inequalities, and a rational Taylor bound. See `ULTRA_STRONG_CANDIDATE.md` and `tools/verify_ultra_candidate.py`.

## General arbitrary-barrier theorem

For every prescribed positive integer `B`, the repository gives an explicit construction of an odd multiplier `X_B` such that the orbit from `1`

1. never returns to `1`; and
2. cannot enter a nontrivial positive cycle of length at most `B`.

The construction chooses a multiple of `21` immediately above a half-integral power of two. Thus finite cycle barriers can be made arbitrarily large by proof, without long trajectory iteration.

This theorem does not by itself solve the prize because the multiplier changes with `B`. See `ARBITRARY_CYCLE_BARRIER.md` and `tools/generate_cycle_barrier.py`.

## Simultaneous length-and-height barriers

For every pair of prescribed positive integers `(B,H)`, the repository gives an explicit multiplier `X_(B,H)` such that the orbit from `1`

1. never returns to `1`;
2. cannot enter a nontrivial cycle of length at most `B`;
3. cannot enter a nontrivial cycle containing any value at most `H`.

Thus a hypothetical exceptional cycle can be forced to be simultaneously arbitrarily long and arbitrarily high. Again, the multiplier changes with `(B,H)`, so this is an arbitrarily strong finite theorem rather than one infinite divergent example. See `TWO_PARAMETER_CYCLE_BARRIER.md` and `tools/generate_two_parameter_barrier.py`.

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
2. if `A/N<log2(X)`, every positive representative has net growth across the whole word;
3. compatible coding classes of an infinite word define one 2-adic integer;
4. they come from an ordinary nonnegative integer exactly when their least representatives eventually stabilize.

Thus arbitrarily long finite growth is locally automatic. The genuinely global obstruction is to keep positive average drift while making the nested coding residues stabilize at one ordinary positive integer rather than converge only 2-adically. See `VALUATION_WORD_CODING.md` and `tools/valuation_word_codec.py`.

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
11. For `(X,n0)=(1093,1)`, the orbit never returns to `1`, reducing that candidate to nontrivial-cycle exclusion.
12. Exact inverse coding of every finite valuation word and a precise ordinary-integer stabilization criterion for infinite words.

## Literature audit

A tempting published claim that Mersenne multipliers have only the trivial positive cycle was checked and cannot currently be used: a key lemma in the supplied proof has the elementary counterexample

```text
m=3, q=7, k=9, c=2:
7 divides 9*2^2-1=35,
```

although `9` is not a power of two. This is recorded in `LITERATURE_AUDIT_SANTOS.md` to prevent an invalid shortcut from being mistaken for a prize solution.

## Not established

- No explicit orbit has yet been proved to tend to infinity.
- Cycles longer than the fixed `148,557,456,445,856,651,509` barrier have not been excluded for the main candidate.
- An arbitrarily large finite barrier is not the same as an infinite barrier.
- The finite 2-adic regeneration targets have not been converted into one ordinary positive integer supporting infinitely many regenerations.
- No low-average infinite valuation word with an eventually stable positive coding residue has yet been constructed.

## Current frontier

The project now has three precise routes rather than a blind trajectory search.

### Route A: finish the explicit candidate

For

```text
X=104350542602662257699,
n0=1,
```

exclude every nontrivial positive cycle, not only cycles through the current finite barrier. A useful next ingredient would be either

1. a global upper bound on possible cycle length for this fixed multiplier that is smaller than the proved barrier; or
2. a modular/descent argument ruling out cycles of all lengths.

### Route B: infinite regenerative chain

For `X=2^m+1`, turn the exact macroblock and 2-adic regeneration formulas into one ordinary positive starting integer with an infinite aperiodic chain of net-positive blocks.

### Route C: stabilized low-average code

Construct an aperiodic infinite valuation word whose prefix averages stay below `log2(X)` and whose unique coding residues eventually stabilize at a positive integer. The new coding theorem gives an exact checker for every prefix and shows precisely where a proposed symbolic construction fails.

Any of these routes would finish the strict prize problem.

## Reproducibility

Run

```text
python run_checks.py
```

to execute all direct tests and principal finite certificates. The strongest fixed certificate is also checked separately by

```text
python tools/verify_ultra_candidate.py
```
