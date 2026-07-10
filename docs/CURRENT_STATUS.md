# Current status

## Strict target

Find explicit odd positive `X>=5,n0` whose accelerated odd-only orbit tends to positive infinity. The strict problem is not solved.

## Main candidate

```text
X  = 104350542602662257699,
n0 = 1.
```

The repository proves:

1. the orbit cannot return to `1`;
2. every element of a reached nontrivial cycle is at least `25`;
3. every cycle length

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

## Retained Priority 1 results

### Local transition no-go

The graph on the `2154` output classes modulo `2*15099` is complete. Every compatible finite exact-valuation word, including arbitrary finite valuation layers, is realizable by infinitely many starts. Local forbidden-edge and forbidden-word enumeration cannot supply the missing proof.

### Global class constraints

For cycle occupancies `c_t`,

```text
sum c_t=p,
sum t*c_t<=67p-1.
```

Cycle closure also forces exact source/target flow balance.

Writing every valuation as

```text
a=t+2154*q,
```

fewer than `11/359` of all cycle steps can have `q>=1`.

### Exact transition progressions and finite truncation

A transition with source class `s`, target label `t`, and layer `q` lies in one exact arithmetic progression modulo

```text
15099*2^(t+2154*q+1).
```

For every cycle length through the current sparse cap, all steps with exact valuation `a>=200` contribute less than

```text
10^(-19)
```

to `sum 1/n_i`. Therefore the non-negligible transition-circulation problem contains only

```text
2154*199 = 428646
```

oriented source-target cells. This is a finite exact reduction, not yet an elimination of the final two lengths.

### Full-modulus activation cost

For

```text
P=6911089648497401,
ord_X(2)=1860810887857924950,
```

each full output class modulo `2X` has a distinct minimum valuation label. If `m` full classes are active, the total valuation satisfies

```text
A >= p + m*(m-1)/2.
```

This sharply limits the number of active classes.

### Index-eight subgroup sieve

`P` is prime and

```text
ord_P(2)=(P-1)/8.
```

Therefore genuine full output representatives are an index-eight subset of the numbers admitted by the `2154` small progressions. Exact sieves below `10^6` and `6*10^7`, combined with activation costs, eliminated four of the former sparse-window exceptions.

### Global closure identities

Every positive cycle satisfies

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

## Main certificate files

```text
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
docs/FULL_MODULUS_ACTIVATION_BOUND.md
tools/verify_full_modulus_activation_bound.py
docs/INDEX_EIGHT_SMALL_REPRESENTATIVE_SIEVE.md
tools/verify_index_eight_small_sieve.py
docs/THIRD_EXCEPTION_SUBGROUP_SIEVE.md
tools/verify_third_exception_subgroup_sieve.py
docs/HIGH_LAYER_RARITY_AND_EDGE_PROGRESSIONS.md
docs/VALUATION_TAIL_TRUNCATION.md
tools/verify_transition_tail_truncation.py
docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md
tools/verify_global_transition_identities.py
```

## Not established

- No explicit orbit is proved divergent.
- The two displayed lengths are not excluded.
- Cycles beyond the sparse cap remain possible.
- Finite certificates do not prove divergence.

## Exact next step

Use the fixed total valuation of the two remaining lengths together with exact full-class activation prices and the finite `428646`-cell transition circulation. Seek a rational dual potential that couples source-class balance, target valuation cost, and reciprocal contribution. Simply extending the subgroup sieve or enumerating local words is not the preferred route.

## Retraction

The former `10^37` claim remains retracted because it assumed `2^A==1 mod X`. The correct congruence retains `product(n_i)`.

## Reproduction

```text
python run_checks.py
```
