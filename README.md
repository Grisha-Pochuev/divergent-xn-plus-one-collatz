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

The first sparse-window argument originally left seven isolated values. Five have now been eliminated by exact modular and rational certificates.

## Main Priority 1 mechanisms

```text
M=15099,
ord_M(2)=2154,
P=6911089648497401,
ord_P(2)=(P-1)/8,
ord_X(2)=1860810887857924950.
```

Retained results include:

- completeness of the bare and finitely augmented local transition graphs;
- global occupancy and flow-balance constraints;
- balanced reciprocal envelopes;
- exact-valuation progressions modulo the large divisor;
- sharp logarithmic power-of-two intervals;
- full-class activation cost

```text
A >= p + m*(m-1)/2;
```

- an exact index-eight subgroup sieve for small genuine full representatives;
- the global cycle identities

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

The next target is an exact activation-price or neighbour-height certificate for the final two first-window lengths.

## Latest certificate files

```text
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FULL_MODULUS_ACTIVATION_BOUND.md
tools/verify_full_modulus_activation_bound.py
docs/INDEX_EIGHT_SMALL_REPRESENTATIVE_SIEVE.md
tools/verify_index_eight_small_sieve.py
docs/THIRD_EXCEPTION_SUBGROUP_SIEVE.md
tools/verify_third_exception_subgroup_sieve.py
```

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

Selected latest checks:

```bash
python tools/verify_full_modulus_activation_bound.py
python tools/verify_index_eight_small_sieve.py
python tools/verify_third_exception_subgroup_sieve.py
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