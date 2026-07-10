# Current status

The strict target is to exhibit odd integers `X>=5` and `n0>=1` whose accelerated odd-only orbit tends to positive infinity.

## Main explicit candidate

The strongest fixed candidate is

```text
X  = 104350542602662257699,
n0 = 1.
```

For this pair the repository proves:

1. the orbit leaves `1` and can never return to `1`;
2. every possible nontrivial cycle element is at least `25`;
3. every nontrivial positive cycle of accelerated length at most

```text
10^37
```

is impossible.

Therefore the orbit either tends to positive infinity or enters a nontrivial cycle longer than `10^37` accelerated steps.

The exact certificate uses

```text
ord_X(2)=1860810887857924950,
```

the `2154` allowed output residue classes modulo `15099`, distinctness of cycle elements, rational logarithm intervals, Legendre's theorem, and elimination of all `19` possible upper continued-fraction convergents through denominator `10^37`.

See `CONTINUED_FRACTION_CYCLE_BARRIER.md` and `tools/verify_continued_fraction_barrier.py`.

This improves the original fixed barrier

```text
148557456445856651509
```

by almost seventeen orders of magnitude.

## General finite barrier theorems

For every prescribed `B`, the repository constructs a multiplier `X_B` whose orbit from `1` never returns to `1` and cannot enter a nontrivial cycle of length at most `B`.

For every pair `(B,H)`, it also constructs a multiplier whose hypothetical cycle must be both longer than `B` and contain no value at most `H`.

The multiplier changes with the requested bounds, so these theorems do not alone solve the prize.

## Exact valuation-word coding

Every finite exact valuation word has exactly one coding class modulo `2^(A+1)`, and every positive representative of that class follows the word. Positive-drift finite words therefore always have infinitely many rigorously growing positive starts.

Compatible prefixes of an infinite word define one 2-adic integer. They come from an ordinary nonnegative integer exactly when their least representatives eventually stabilize. This identifies the global obstruction in symbolic constructions.

See `VALUATION_WORD_CODING.md` and `tools/valuation_word_codec.py`.

## Other established results

1. Exact accelerated map and iterate formula.
2. Average-valuation criterion for exponential divergence.
3. Arbitrarily long rigorously increasing finite orbit segments.
4. Finite repetition bound for every exact valuation block.
5. Eventually periodic valuations force an eventually periodic orbit.
6. Complete `X=2^m+1` macroblock formula including its exceptional exit.
7. Complete macroblocks whose accumulated growth survives the exit.
8. A 2-adic isometry and unique regeneration target at every finite precision.
9. Exact coordinate normal forms around `n=-1` and `n=1` for Fermat- and Mersenne-type multipliers.
10. Positive integer orbits are either eventually periodic or tend to positive infinity.
11. For `(X,n0)=(1093,1)`, the orbit never returns to `1`.
12. Exact inverse coding of every finite valuation word.
13. Continued-fraction exclusion of every nontrivial cycle of length at most `10^37` for the main fixed candidate.

## Literature audit

A published claim that Mersenne multipliers have only the trivial positive cycle cannot currently be used. A key lemma has the counterexample

```text
m=3, q=7, k=9, c=2:
7 divides 9*2^2-1=35,
```

although `9` is not a power of two. See `LITERATURE_AUDIT_SANTOS.md`.

## Not established

- No explicit orbit has yet been proved to tend to infinity.
- Cycles longer than `10^37` remain logically possible for the main candidate.
- An arbitrarily large finite barrier is not an infinite barrier.
- No ordinary positive integer supporting infinitely many net-positive regenerative blocks has yet been constructed.
- No low-average infinite valuation word with an eventually stable positive coding residue has yet been constructed.

## Current frontier

### Route A: finish the explicit candidate

Exclude cycles of every length for

```text
X=104350542602662257699,
n0=1.
```

The current method reduces all cycles through `10^37` to finitely many exact rational checks. A completion needs either a global modular/descent obstruction or a sufficiently strong theorem for every remaining rational approximation.

### Route B: infinite regenerative chain

For `X=2^m+1`, turn the exact macroblock and 2-adic regeneration formulas into one ordinary positive start with an infinite aperiodic sequence of net-positive blocks.

### Route C: stabilized low-average code

Construct an infinite valuation word with average below `log2(X)` whose exact coding residues eventually stabilize at a positive integer.

Any route would finish the strict prize problem.

## Reproducibility

Run

```text
python run_checks.py
```

or separately

```text
python tools/verify_continued_fraction_barrier.py
```
