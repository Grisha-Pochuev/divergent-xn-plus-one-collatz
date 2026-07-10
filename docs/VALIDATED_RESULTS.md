# Validated results registry

This file contains only retained results with a mathematical derivation and, where practical, an exact verifier.

Last structural update: 2026-07-10.

## A. Fixed candidate frontier

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the repository proves:

1. the orbit leaves `1` and cannot return to `1`;
2. every element of a reached nontrivial positive cycle is at least `25`;
3. every nontrivial cycle length

```text
p <= 177780727155637125192
```

is impossible;
4. every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193
177780727155637125195.
```

This remains a finite/sparse cycle obstruction, not a proof of divergence.

## B. Exact iterate and growth criterion

For exact valuations `a_t=v2(X*n_t+1)` and `A_N=sum_(t<N)a_t`, the accelerated iterate has an exact affine formula. If eventually

```text
A_N/N <= log2(X)-epsilon
```

for some `epsilon>0`, then the orbit grows exponentially. This criterion is sufficient but has not been proved for one explicit orbit.

## C. Exact finite valuation-word coding

Every finite exact valuation word is coded by one odd residue class modulo `2^(A+1)`. Every positive representative follows the word exactly. Compatible infinite prefixes define one 2-adic integer; they correspond to an ordinary nonnegative integer exactly when the least representatives eventually stabilize.

Files:

```text
docs/VALUATION_WORD_CODING.md
tools/valuation_word_codec.py
tests/test_valuation_word_codec.py
```

## D. Periodic valuation obstruction

A noncyclic positive orbit can repeat a fixed exact valuation block only finitely often unless the affine fixed-point condition gives a genuine cycle. Therefore eventually periodic exact valuations force an eventually periodic integer orbit.

Files:

```text
docs/PERIODIC_VALUATION_OBSTRUCTION.md
tools/analyze_periodic_block.py
tests/test_periodic_block.py
```

## E. Fermat-type macroblocks and finite programs

For `X=2^m+1`, exact complete growing macroblocks exist, and any prescribed finite program of such blocks can be realized by infinitely many positive odd starts. The theorem is finite: it does not produce one fixed ordinary start supporting infinitely many growing blocks.

Files:

```text
docs/FERMAT_MACROBLOCK_REGENERATION.md
docs/GENERAL_FERMAT_BURST_REDUCTION.md
docs/FINITE_MACROBLOCK_PROGRAMS.md
tools/analyze_fermat_macroblock.py
tools/verify_general_fermat_burst.py
tools/build_macroblock_program.py
```

## F. 2-adic regeneration structure

For fixed Fermat-type macroblock parameters, the endpoint map on the odd core is a 2-adic isometry with one finite-precision residue regenerating a chosen target. The compatible infinite target is generally nonintegral 2-adically.

## G. Logarithmic cycle-height reduction

For fixed odd `X>=5`, effective lower bounds for

```text
A*log(2)-p*log(X)
```

give computable `K_X,D_X>0` such that the minimum cycle element satisfies

```text
m <= K_X*p^D_X.
```

No growing modular lower bound has yet been combined with it to exclude all cycles.

## H. Positive-orbit dichotomy

A bounded positive integer orbit eventually repeats. Hence every positive orbit is either eventually periodic or tends to positive infinity. Excluding every positive cycle for the main candidate would finish the strict prize problem.

## I. Bare and augmented transition no-go theorems

For `M=15099` and `H=ord_M(2)=2154`:

- every directed transition between the `2154` allowed output classes is realizable;
- every finite class word is realizable;
- every compatible finite exact-valuation word remains realizable together with an arbitrary initial output class;
- adding any finite collection of layers `q=(a-t)/H` does not create forbidden finite words.

Therefore the missing obstruction must be global.

Files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
docs/AUGMENTED_TRANSITION_NO_GO.md
tools/verify_augmented_transition_no_go.py
```

## J. Valuation budget, flow balance, and occupancy dual

For a hypothetical cycle with class occupancies `c_t`,

```text
sum c_t=p,
sum t*c_t<=67p-1.
```

Cycle closure gives exact source/target flow balance. A rational tangent/Lagrange-dual certificate using both constraints gives a reciprocal upper bound approximately `3.217731`.

Files:

```text
docs/RESIDUE_VALUATION_BUDGET.md
tools/verify_residue_valuation_budget.py
docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md
tools/verify_transition_balance.py
docs/BALANCED_OCCUPANCY_DUAL_BOUND.md
tools/verify_balanced_occupancy_barrier.py
```

## K. Large-divisor valuation split

The factorization

```text
X=15099*6911089648497401
```

places an output entered with exact valuation `a` in one odd progression modulo twice the large divisor. Splitting low and high valuations yields exact reciprocal envelopes, including approximately `2.774599` at cutoff `400000`.

Files:

```text
docs/LARGE_DIVISOR_VALUATION_SPLIT.md
tools/verify_large_divisor_split_barrier.py
```

## L. Sharp logarithmic interval certificate

Finite positive atanh-series sums give rigorous lower bounds for the gaps between `X^p` and adjacent powers of two. This raises the first contiguous obstruction to

```text
177780727155637125182.
```

Files:

```text
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
```

## M. First sparse cycle window

After the first near-power-of-two crossing, the gap to the following power jumps back to almost `log(2)`. Exact endpoint inequalities exclude every length through

```text
355561454311274250377
```

except seven isolated odd lengths.

Files:

```text
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
```

## N. First exceptional length eliminated

A midpoint harmonic inequality and an exact valuation split with cutoff `5000000` give

```text
sum 1/n_i < 2.527289
```

at `p=177780727155637125183`, contradicting the exact interval gap.

Files:

```text
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
```

## O. Global transition-balance identities

Every positive accelerated cycle satisfies

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

Files:

```text
docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md
tools/verify_global_transition_identities.py
```

## P. Full-modulus activation bound

The checker proves

```text
ord_X(2)=1860810887857924950.
```

If a cycle activates `m` different full output classes modulo `2X`, their distinct minimum valuation labels and the remaining steps imply

```text
A >= p + m*(m-1)/2.
```

This bounds `m` by about `1.53*10^11` in the first exceptional window. Combined with full-class spacing `2X`, it eliminates

```text
p=177780727155637125185.
```

Files:

```text
docs/FULL_MODULUS_ACTIVATION_BOUND.md
tools/verify_full_modulus_activation_bound.py
```

## Q. Index-eight subgroup sieve

The large factor `P=6911089648497401` is prime and

```text
ord_P(2)=(P-1)/8.
```

Hence genuine full output representatives form an index-eight subset modulo `P`. An exact sieve of `71318` small candidates below `10^6`, combined with the activation bound, eliminates

```text
177780727155637125187
177780727155637125189.
```

Files:

```text
docs/INDEX_EIGHT_SMALL_REPRESENTATIVE_SIEVE.md
tools/verify_index_eight_small_sieve.py
```

## R. Third-exception subgroup sieve

An exact membership check of `4279760` modular candidates below `60000000` finds `536735` genuine full representatives. The resulting reciprocal bound is approximately

```text
0.913331,
```

below the exact required threshold `0.913636`. Therefore

```text
p=177780727155637125191
```

is impossible.

Files:

```text
docs/THIRD_EXCEPTION_SUBGROUP_SIEVE.md
tools/verify_third_exception_subgroup_sieve.py
```

## Verification policy

A result belongs here only if:

- hypotheses and conclusions are precise;
- known small cycles do not contradict it;
- exact arithmetic is used where rounding matters;
- a checker is supplied where practical;
- invalid stronger claims remain explicitly retracted.