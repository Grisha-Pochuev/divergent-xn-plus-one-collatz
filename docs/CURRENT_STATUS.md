# Current status

## Project navigation

Every new work session must begin with:

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
run_checks.py
```

GitHub is the durable source of truth. The strict target is an explicit positive odd orbit tending to positive infinity.

## Main fixed candidate

```text
X  = 104350542602662257699,
n0 = 1.
```

For this pair the repository proves:

1. the orbit leaves `1` and cannot return to `1`;
2. every possible element of a nontrivial cycle reached by the orbit is at least `25`;
3. every nontrivial positive cycle of accelerated length

```text
p <= 177780727155637125184
```

is impossible;
4. every length

```text
p <= 355561454311274250377
```

is impossible except the six odd values

```text
177780727155637125185
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

Thus the strict problem remains open. The fixed orbit either tends to positive infinity or enters a nontrivial cycle. Up to the sparse cap, only the six listed lengths remain possible.

## Priority 1 results

Use

```text
M = 15099,
H = ord_M(2) = 2154,
P = 6911089648497401,
X = M*P.
```

### 1. Complete local graph and augmented no-go theorem

The graph on the `2154` allowed odd output classes modulo `2M` is complete, including loops. Every finite class word is realized by infinitely many positive starts.

More strongly, every compatible finite word of exact valuations is realizable together with any prescribed initial class. Adding the exact valuation or the layer

```text
q=(a-t)/H
```

therefore does not create forbidden finite words. A successful obstruction must use cycle closure, global height, or another nonlocal condition.

Files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
docs/AUGMENTED_TRANSITION_NO_GO.md
tools/verify_augmented_transition_no_go.py
```

### 2. Occupancy and flow constraints

For class occupancies `c_t` in a hypothetical cycle of length `p`,

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

Cycle closure also gives exact source/target flow balance. These conditions reduce the reciprocal problem to a finite concave allocation problem.

A rational dual certificate yields the reciprocal upper bound approximately

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

### 3. Large-divisor exact-valuation split

Because

```text
P = 6911089648497401
```

divides `X`, an output entered with exact valuation `a` lies in one odd progression modulo `2P`.

Splitting low and high incoming valuations gives progressively stronger reciprocal envelopes:

- with `K=400000`: approximately `2.774599`;
- with the midpoint progression inequality and `K=5000000`: approximately `2.527289` for the first exceptional length.

Files:

```text
docs/LARGE_DIVISOR_VALUATION_SPLIT.md
tools/verify_large_divisor_split_barrier.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
```

### 4. Sharp logarithmic intervals and sparse window

Exact positive atanh-series bounds replace the former coarse one-term logarithm estimate. This raises the first contiguous interval obstruction to

```text
177780727155637125182.
```

After the first near-power-of-two crossing, the gap to the following power jumps back to almost `log(2)`. This excludes every length through

```text
355561454311274250377
```

except seven isolated odd values. The midpoint large-divisor certificate eliminates the first of those seven, producing the current six-value list and contiguous barrier.

Files:

```text
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
```

### 5. Global transition-balance identities

Every positive accelerated cycle satisfies the exact identities

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

These are genuine cycle-closure constraints not imposed by arbitrary finite valuation coding.

Files:

```text
docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md
tools/verify_global_transition_identities.py
```

## Not established

- No explicit orbit has yet been proved to tend to infinity.
- The six exceptional lengths have not yet been excluded.
- Cycles beyond the sparse cap remain logically possible.
- The finite barriers, though enormous, do not constitute a proof of divergence.

## Exact next step

Attack the six exceptional odd lengths directly. Their total valuation is fixed exactly. Combine that fact with:

1. the two global transition-balance identities;
2. exact incoming-valuation progression costs modulo the full multiplier or its large divisor;
3. a height inequality coupling a valuation spike to neighbouring cycle values.

Do not search again for forbidden finite words in any bounded augmentation of the class labels; the augmented no-go theorem closes that route.

## Retraction audit

The former `10^37` claim remains retracted. It incorrectly used

```text
2^A == 1 (mod X).
```

The correct relation is

```text
2^A * product_i(n_i) == 1 (mod X).
```

The `5n+1` cycle `13 -> 33 -> 83 -> 13` is the preserved regression counterexample.

## Reproducibility

Run

```text
python run_checks.py
```

to execute all retained certificates and regression checks. No long trajectory computation or large search is part of the Priority 1 proof chain.