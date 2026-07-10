# The Open Mathematics Project

## Divergent accelerated `Xn+1` orbit

For odd `X>=5`, define

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

on positive odd integers. The strict target is one explicit pair `(X,n0)` whose orbit tends to positive infinity. A cycle, avoidance of `1`, a long finite trajectory, or a finite barrier is not a solution.

## Start here

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
run_checks.py
```

## Strongest current result

The strict problem is not solved. For

```text
X  = 104350542602662257699,
n0 = 1,
```

the repository proves:

- the orbit cannot return to `1`;
- every element of a reached nontrivial cycle is at least `25`;
- every cycle length

```text
p <= 177780727155637125192
```

is impossible;
- every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193
177780727155637125195.
```

The first sparse-window argument originally left seven isolated values. Five have been eliminated by exact modular and rational certificates.

## Latest Priority 1 structure

Use

```text
M=15099,
ord_M(2)=2154,
P=6911089648497401,
ord_P(2)=(P-1)/8,
O=ord_X(2)=1860810887857924950.
```

For every cycle valuation there is a unique decomposition

```text
a_i=s_(i+1)+O*q_i,
1<=s_i<=O.
```

The full class label is paid by every occurrence, so

```text
A=sum_i s_i+O*sum_i q_i.
```

At either remaining length this gives

```text
sum_i q_i<=6257.
```

Further exact results:

- a permanent predecessor sieve removes exactly one third of the refined classes modulo `6*15099`;
- possible predecessors of a fixed full representative form a linear progression modulo `X`;
- the first layer in which that predecessor is itself a full output gives an exact transition cost;
- below one million, those full predecessor delays range from `0` to `347`;
- through sixty million they range from `0` to `558`;
- for the harder remaining length,

```text
sum_(n_i<=60000000) 1/n_i < 0.087618737,
```

while the cycle identity requires a total greater than `0.099934206`;
- hence at least `738929` distinct values above sixty million are still needed;
- inverse windows of depths two and three strengthen the small-value bound further;
- any hypothetical remaining cycle is either entirely least-layer, or contains at least `28413093679980362` consecutive least-layer steps;
- if a positive layer occurs, one such block grows by more than

```text
2^1860810887857924884.
```

These are necessary structural constraints, not yet a proof of divergence.

## Latest certificate files

```text
docs/PERMANENT_PREDECESSOR_MOD3_SIEVE.md
tools/verify_permanent_predecessor_mod3_sieve.py
docs/FULL_LABEL_OCCUPANCY_BUDGET.md
tools/verify_full_label_occupancy_budget.py
docs/FULL_PREDECESSOR_DELAY.md
tools/verify_full_predecessor_delay.py
docs/FULL_PREDECESSOR_RECIPROCAL_BOUND.md
tools/verify_full_predecessor_reciprocal_bound.py
docs/FINITE_INVERSE_WINDOW_CHARGING.md
tools/verify_finite_inverse_window_charging.py
docs/GIANT_ZERO_LAYER_BLOCK.md
tools/verify_giant_zero_layer_block.py
docs/GIANT_COMPENSATING_GROWTH_BLOCK.md
tools/verify_giant_compensating_growth_block.py
```

The earlier sparse-window, activation, subgroup, transition-balance, and retraction certificates remain part of `run_checks.py`.

## Exact next target

Do not enlarge the cutoff blindly. The missing object is a global certificate for the large zero-delay tail, for example:

1. a rational potential or minimum-mean inequality for long inverse windows;
2. an explicit distribution bound for the initial full-class sequence `2^(-s) mod X`;
3. a full source/target circulation inequality coupled to the global height identities.

## Important retraction

The former `10^37` barrier is retracted. It incorrectly assumed

```text
2^A == 1 (mod X).
```

The correct congruence is

```text
2^A * product_i(n_i) == 1 (mod X).
```

The accelerated `5n+1` cycle `13 -> 33 -> 83 -> 13` is the regression counterexample.

## Reproduction

No external Python packages are required.

```bash
python run_checks.py
```

The modular sieves are deterministic certificate checks, not Collatz trajectory searches.

## Repository layout

```text
START_HERE.md   Durable entry point.
docs/           Proof notes, status, audits, and roadmap.
tools/          Exact verification scripts.
tests/          Independent tests and regressions.
results/        Exploratory outputs, never treated as proof.
```

## License

MIT.
