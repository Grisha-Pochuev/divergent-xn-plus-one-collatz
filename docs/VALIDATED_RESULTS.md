# Validated results registry

This file contains only retained results with a mathematical derivation and, where practical, an exact verifier.

Last structural update: 2026-07-11.

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

## J. Small-class valuation budget and flow balance

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

## K. Large-divisor split and valuation-tail truncation

The factorization

```text
X=15099*6911089648497401
```

places an output entered with exact valuation `a` in one odd progression modulo twice the large divisor. Splitting low and high valuations gives exact reciprocal envelopes. Through the current sparse cap, all steps with `a>=200` contribute less than `10^(-19)` to `sum 1/n_i`, reducing the non-negligible small-class transition problem to `428646` cells.

Files:

```text
docs/LARGE_DIVISOR_VALUATION_SPLIT.md
tools/verify_large_divisor_split_barrier.py
docs/VALUATION_TAIL_TRUNCATION.md
tools/verify_transition_tail_truncation.py
```

## L. Sharp logarithmic interval and first sparse window

Finite positive atanh-series sums give rigorous gaps between `X^p` and adjacent powers of two. The first contiguous obstruction reaches

```text
177780727155637125182.
```

After the first crossing, every length through

```text
355561454311274250377
```

is excluded except seven isolated odd lengths.

Files:

```text
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
```

## M. Five sparse-window exceptions eliminated

The seven original exceptions were reduced to two by exact certificates:

- a midpoint harmonic inequality and valuation split eliminate `...183`;
- the full-modulus activation bound eliminates `...185`;
- the index-eight sieve below `10^6` eliminates `...187` and `...189`;
- the index-eight sieve below `6*10^7` eliminates `...191`.

Files:

```text
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
docs/FULL_MODULUS_ACTIVATION_BOUND.md
tools/verify_full_modulus_activation_bound.py
docs/INDEX_EIGHT_SMALL_REPRESENTATIVE_SIEVE.md
tools/verify_index_eight_small_sieve.py
docs/THIRD_EXCEPTION_SUBGROUP_SIEVE.md
tools/verify_third_exception_subgroup_sieve.py
```

## N. Global transition-balance identities

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

## O. Permanent mod-3 predecessor sieve

Since `X==3 (mod 9)` and every accelerated output is coprime to `X`, an allowed refined residue is permanently unreachable when all its direct predecessors are divisible by `3`.

Every one of the `2154` small output classes has three compatible lifts modulo `6M`. Exactly one lift is dead. Therefore the exact refined counts are

```text
2154 dead classes,
4308 surviving classes.
```

The surviving mod-3 edge types also obey

```text
N_(1->2)=N_(2->1)
```

around every cycle.

Files:

```text
docs/PERMANENT_PREDECESSOR_MOD3_SIEVE.md
tools/verify_permanent_predecessor_mod3_sieve.py
```

## P. Exact full-label occupancy budget

Let

```text
O=ord_X(2)=1860810887857924950.
```

If `s_i` is the least positive full output label of the target `n_i`, then every incoming valuation has the unique form

```text
a_(i-1)=s_i+O*q_(i-1),
1<=s_i<=O,
q_(i-1)>=0.
```

Hence exactly

```text
A=sum_i s_i+O*sum_i q_i.
```

For either remaining sparse-window length,

```text
sum_i q_i<=6257.
```

Equivalently, almost every edge must use its least full-order layer. For any selected set of distinct possible cycle values, the correct incremental budget is

```text
sum [s(n)-1+O*d(n)] <= A-p,
```

where `d(n)` is any proved lower bound on its layer.

Files:

```text
docs/FULL_LABEL_OCCUPANCY_BUDGET.md
tools/verify_full_label_occupancy_budget.py
```

## Q. Full-modulus predecessor delay

For a genuine full representative `n` with least label `s`, its possible predecessors satisfy

```text
m_q=(2^(s+qO)*n-1)/X,
m_q == m_0+q*63726582940809041391 (mod X).
```

A predecessor belonging to a reached cycle must itself lie in the full output subgroup. Let `d_X(n)` be the first layer `q` for which this happens. Then every hypothetical cycle satisfies

```text
sum_i d_X(n_i)<=6257.
```

Below one million, among the `5824` representatives surviving the permanent sieve:

```text
only 133 have d_X=0,
maximum d_X=347,
sum of all listed delays=207287.
```

Through sixty million:

```text
358103 representatives survive the permanent sieve,
9462 have d_X=0,
maximum d_X=558,
sum of listed delays=12752005.
```

Files:

```text
docs/FULL_PREDECESSOR_DELAY.md
tools/verify_full_predecessor_delay.py
```

## R. Full-predecessor reciprocal dual

For the harder remaining length

```text
p=177780727155637125195,
A=11822418355849868825468,
```

the exact interval requires

```text
sum_i 1/n_i > 0.099934206.
```

Using the incremental item cost `s-1+O*d_X` and an exact rational fractional-selection dual gives

```text
sum_(n_i<=1000000) 1/n_i < 0.087551912,
sum_(n_i<=60000000) 1/n_i < 0.087618737.
```

Thus more than `0.012315` must come from distinct values above sixty million, requiring at least

```text
738929
```

such values.

Files:

```text
docs/FULL_PREDECESSOR_RECIPROCAL_BOUND.md
tools/verify_full_predecessor_reciprocal_bound.py
```

## S. Finite inverse-window charging

Let `h_L(n)` be the minimum sum of full-order layers in an admissible inverse chain of `L` steps ending at `n`. Summing selected inverse windows around a cycle counts every actual layer at most `L` times, so

```text
sum h_L(n_i)<=L*sum q_i.
```

The exact scaled item cost is

```text
L*(s-1)+O*h_L.
```

Below one million the reciprocal bounds strictly improve with inverse depth:

```text
L=1: <0.087551912
L=2: <0.085634587
L=3: <0.085243521.
```

This proves that longer inverse information adds genuine strength, but the large zero-delay tail remains unexcluded.

Files:

```text
docs/FINITE_INVERSE_WINDOW_CHARGING.md
tools/verify_finite_inverse_window_charging.py
```

## Verification policy

A result belongs here only if:

- hypotheses and conclusions are precise;
- known small cycles do not contradict it;
- exact arithmetic is used where rounding matters;
- a checker is supplied where practical;
- invalid stronger claims remain explicitly retracted.
