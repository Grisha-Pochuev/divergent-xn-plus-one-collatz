# Validated results registry

This file contains only retained results with a mathematical derivation and, where practical, an exact checker or regression test.

Last structural update: 2026-07-10.

## A. Fixed candidate, contiguous barrier, and sparse window

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the repository retains:

1. `C_X(1) != 1` and the orbit cannot later return to `1`.
2. Every element of any nontrivial cycle reached by this orbit is at least `25`.
3. Every nontrivial positive cycle of accelerated length

```text
p <= 177780727155637125184
```

is impossible.
4. More strongly, every length

```text
p <= 355561454311274250377
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

The conclusion remains only:

```text
the orbit tends to +infinity
or
it enters a nontrivial positive cycle.
```

If a cycle has length at most the sparse cap, its length must be one of the six listed values.

Primary files:

```text
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
```

## B. Exact iterate and growth criterion

For exact valuations

```text
a_t = v2(X*n_t+1),
A_N = sum_(t=0)^(N-1) a_t,
```

the accelerated iterate has an exact affine formula. If

```text
A_N/N <= log2(X)-epsilon
```

for all sufficiently large `N` and some `epsilon>0`, then the orbit grows exponentially. This is a sufficient criterion, not a proof for a particular orbit.

## C. Exact finite valuation-word coding

Every finite exact valuation word has one coding residue class modulo `2^(A+1)`, where `A` is its total valuation. Every positive representative follows the word exactly.

Consequences:

- every positive-drift finite word has infinitely many positive starts producing it;
- compatible infinite prefixes define one 2-adic integer;
- those prefixes come from an ordinary nonnegative integer exactly when their least representatives eventually stabilize.

Files:

```text
docs/VALUATION_WORD_CODING.md
tools/valuation_word_codec.py
tests/test_valuation_word_codec.py
```

## D. Periodic valuation obstruction

Every exact finite valuation block has a finite repetition bound on a noncyclic positive orbit. The exceptional affine fixed-point condition represents a genuine cycle. Therefore an eventually periodic exact valuation sequence forces an eventually periodic integer orbit.

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
n0 = 2^(mL)*u-1,
```

with positive odd `u`, the first `L-1` accelerated valuations are exactly `m`. If

```text
r = v2(X^L*u-1),
```

then the endpoint is

```text
T_(m,L)(u) = (X^L*u-1)/2^r.
```

There are arbitrarily long complete finite blocks whose endpoint exceeds their start. This does not yet produce one fixed ordinary integer with infinitely many growing blocks.

Files:

```text
docs/FERMAT_MACROBLOCK_REGENERATION.md
docs/GENERAL_FERMAT_BURST_REDUCTION.md
tools/analyze_fermat_macroblock.py
tools/verify_general_fermat_burst.py
```

## F. Arbitrary finite programs of growing macroblocks

For `X=2^m+1`, any prescribed finite program of complete macroblocks and prescribed finite exit valuations can be realized by infinitely many positive odd core tuples. If each block satisfies its retained growth inequality, every boundary value grows.

The theorem is finite; the required starting congruence generally changes with program length.

Files:

```text
docs/FINITE_MACROBLOCK_PROGRAMS.md
tools/build_macroblock_program.py
tests/test_macroblock_program.py
```

## G. 2-adic regeneration structure

For fixed Fermat-type macroblock parameters, the endpoint map on the odd core is a 2-adic isometry. At every finite precision there is one unique residue class regenerating a chosen target. The compatible infinite target is generally nonintegral 2-adically.

## H. Logarithmic cycle-height reduction

For every fixed odd `X>=5`, if a positive accelerated cycle has length `p` and minimum `m`, effective lower bounds for

```text
A*log(2)-p*log(X)
```

give computable constants `K_X,D_X>0` with

```text
m <= K_X*p^D_X.
```

The constants have not yet been combined with a growing modular lower bound that excludes all cycles.

File: `docs/LOGARITHMIC_CYCLE_REDUCTION.md`.

## I. General logical dichotomy

A bounded positive integer orbit eventually repeats. Hence every positive orbit is either eventually periodic or tends to positive infinity. For the fixed candidate, excluding all positive cycles would finish the prize problem.

## J. Completeness of the bare 2154-class graph

For `M=15099`, every directed transition between the `2154` allowed output classes is realizable, including loops. Every finite class word is realized by infinitely many positive starts.

Files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
```

## K. Augmented finite-path no-go theorem

Retaining any prescribed finite word of exact valuations, including the layer

```text
q=(a-t)/2154,
```

does not create forbidden finite paths. Exact valuation-word coding modulo a power of two and an arbitrary initial class modulo `2M` remain compatible by the generalized Chinese remainder theorem.

Thus no bounded local state made only from residue labels and finitely many exact valuation layers can yield the missing obstruction.

Files:

```text
docs/AUGMENTED_TRANSITION_NO_GO.md
tools/verify_augmented_transition_no_go.py
```

## L. Valuation budget, flow balance, and balanced occupancy dual

For a hypothetical cycle of length `p`, with `c_t` elements in class `t`,

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

Cycle closure gives exact source/target flow balance. A rational Lagrange-dual tangent certificate using both global constraints gives a reciprocal upper bound approximately

```text
3.217731.
```

Files:

```text
docs/RESIDUE_VALUATION_BUDGET.md
tools/verify_residue_valuation_budget.py
docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md
tools/verify_transition_balance.py
docs/BALANCED_OCCUPANCY_DUAL_BOUND.md
tools/verify_balanced_occupancy_barrier.py
```

## M. Large-divisor valuation split

The factorization

```text
X = 15099 * 6911089648497401
```

allows an incoming exact valuation `a` to place the output in one odd progression modulo twice the large divisor. Splitting low and high valuations gives a reciprocal envelope approximately

```text
2.774599
```

with `K=400000`.

The exact checker uses a short deterministic modular enumeration, not a trajectory search.

Files:

```text
docs/LARGE_DIVISOR_VALUATION_SPLIT.md
tools/verify_large_divisor_split_barrier.py
```

## N. Sharp logarithmic interval certificate

Finite positive atanh-series sums give rigorous lower bounds for the gaps

```text
log(2),
log(2^67/X).
```

Using these instead of the former one-term bound raises the first contiguous obstruction to

```text
177780727155637125182.
```

Files:

```text
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
```

## O. First sparse cycle window

After the first near-power-of-two crossing, the gap to the following power jumps back to almost `log(2)`. Exact rational endpoint inequalities therefore exclude every cycle length up to

```text
355561454311274250377
```

except seven isolated odd lengths.

Files:

```text
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
```

## P. First exceptional length eliminated

For the first exceptional odd length, use:

- the midpoint harmonic inequality for reciprocal progressions;
- the exact valuation split at `K=5000000` using the large divisor;
- exact lower and upper logarithm series.

This gives

```text
sum_i 1/n_i < 2.527289
```

and contradicts the exact interval gap. Consequently the first exception is impossible, leaving six and raising the contiguous barrier to the value in Section A.

Files:

```text
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
```

## Q. Global transition-balance identities

Every positive accelerated cycle satisfies

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

These are genuine global closure conditions and are the preferred next tools for the six remaining lengths.

Files:

```text
docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md
tools/verify_global_transition_identities.py
```

## Verification policy

A result belongs here only if:

- its hypotheses and conclusion are precise;
- known small examples do not contradict it;
- exact arithmetic is used where floating-point error could matter;
- an exact checker is supplied where practical;
- invalid stronger claims remain explicitly retracted.