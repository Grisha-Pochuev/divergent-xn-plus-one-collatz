# Validated results registry

This file contains only retained results that currently have a mathematical derivation and, where practical, an exact checker or regression test.

Last structural update: 2026-07-10.

## A. Fixed candidate and finite cycle barrier

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the repository retains the following conclusions:

1. `C_X(1) != 1` and the orbit cannot later return to `1`.
2. Every element of any nontrivial cycle reached by this orbit is at least `25`.
3. Every nontrivial positive cycle of accelerated length

```text
p <= 170000000000000000000
```

is impossible.

The proof uses:

- the divisor `M=15099` of `X`;
- `ord_M(2)=2154`;
- the resulting `2154` allowed odd output classes modulo `2M`;
- distinctness of elements in a nontrivial cycle;
- a logarithmic upper envelope for the reciprocal sum of possible cycle elements;
- exact rational inequalities for even and odd cycle lengths.

Files:

```text
docs/RESIDUE_CROWDING_CYCLE_BARRIER.md
tools/verify_residue_crowding_barrier.py
docs/ULTRA_STRONG_CANDIDATE.md
tools/verify_ultra_candidate.py
```

The conclusion is only the dichotomy:

```text
the orbit tends to +infinity
or
it enters a nontrivial positive cycle longer than the finite barrier.
```

## B. Exact iterate and growth criterion

For exact valuations

```text
a_t = v2(X*n_t+1),
A_N = sum_{t=0}^{N-1} a_t,
```

the accelerated iterate has an exact affine formula. In particular, if along an orbit

```text
A_N/N <= log2(X)-epsilon
```

for all sufficiently large `N` and some `epsilon>0`, then the orbit grows exponentially.

This is a sufficient criterion, not a proof that a particular orbit satisfies it.

## C. Exact finite valuation-word coding

Every finite exact valuation word has one coding residue class modulo `2^(A+1)`, where `A` is its total valuation. Every positive representative of that class follows the word exactly.

Consequences:

- every positive-drift finite word has infinitely many positive starts producing that finite growth block;
- compatible infinite prefixes define one 2-adic integer;
- those prefixes come from an ordinary nonnegative integer exactly when their least representatives eventually stabilize.

Files:

```text
docs/VALUATION_WORD_CODING.md
tools/valuation_word_codec.py
tests/test_valuation_word_codec.py
```

## D. Periodic valuation obstruction

For every exact finite valuation block there is a finite bound on how many times a noncyclic positive orbit can repeat it consecutively. If the exceptional affine fixed-point condition holds, the block represents a genuine cycle.

Therefore an eventually periodic exact valuation sequence forces an eventually periodic integer orbit. A divergent orbit must have genuinely aperiodic exact valuations.

Files:

```text
docs/PERIODIC_VALUATION_OBSTRUCTION.md
tools/analyze_periodic_block.py
tests/test_periodic_block.py
```

## E. Fermat-type macroblocks

For

```text
X = 2^m+1,
n0 = 2^(mL)*u-1
```

with positive odd `u`, the first `L-1` accelerated valuations are exactly `m`. If

```text
r = v2(X^L*u-1),
```

then the complete endpoint is

```text
T_(m,L)(u) = (X^L*u-1)/2^r.
```

There are arbitrarily long complete finite blocks whose endpoint exceeds their start. For prescribed finite exit valuation `r`, the admissible odd core lies in one exact residue class modulo `2^(r+1)`.

Files:

```text
docs/FERMAT_MACROBLOCK_REGENERATION.md
docs/GENERAL_FERMAT_BURST_REDUCTION.md
tools/analyze_fermat_macroblock.py
tools/verify_general_fermat_burst.py
```

This does not yet construct one ordinary positive integer supporting infinitely many net-positive blocks.

## F. Arbitrary finite programs of growing macroblocks

For `X=2^m+1`, choose arbitrary finite boundary lengths

```text
L_0,...,L_R >= 1
```

and prescribed excess exit valuations

```text
r_0,...,r_(R-1) >= 1.
```

There exist infinitely many positive odd core tuples `q_0,...,q_R` for which the accelerated orbit follows exactly those complete macroblocks in sequence. If every block satisfies

```text
L_i*log2(1+2^(-m)) > r_i+1,
```

then every boundary value is strictly larger than the preceding boundary value.

Thus any finite, including aperiodic, program of complete growing macroblocks can be realized exactly by positive odd integers. The theorem is finite: as the number of prescribed blocks grows, the required starting congruence generally changes, so it does not yet produce one fixed start supporting infinitely many blocks.

Files:

```text
docs/FINITE_MACROBLOCK_PROGRAMS.md
tools/build_macroblock_program.py
tests/test_macroblock_program.py
```

## G. 2-adic regeneration structure

For fixed Fermat-type macroblock parameters, the endpoint map on the odd core is a 2-adic isometry. At every finite precision there is one unique residue class regenerating a chosen target such as `-1`.

The compatible target is generally a genuinely nonintegral 2-adic number. Thus arbitrary finite regeneration does not automatically produce an ordinary positive starting value.

## H. Logarithmic cycle-height reduction

For every fixed odd `X>=5`, if a positive accelerated cycle has length `p` and minimum element `m`, then effective lower bounds for the nonzero linear form

```text
A*log(2)-p*log(X)
```

imply effectively computable constants `K_X,D_X>0` with

```text
m <= K_X*p^D_X.
```

This is a global structural reduction. The constants have not yet been combined with a growing modular lower bound strong enough to exclude all cycles.

File:

```text
docs/LOGARITHMIC_CYCLE_REDUCTION.md
```

## I. General logical dichotomy

A positive integer orbit that is bounded must eventually repeat and enter a cycle. Hence every positive orbit is either eventually periodic or tends to positive infinity.

For the main candidate, proving that no positive cycle can ever be reached would therefore finish the strict prize problem.

## Verification policy

A result belongs in this registry only if:

- its hypotheses and conclusion are stated precisely;
- known small examples do not contradict it;
- exact arithmetic is used where floating-point error could matter;
- any superseded or invalid stronger claim is removed or explicitly marked as retracted.
